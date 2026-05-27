"""
Docling-based OCR Pipeline for Veterinary Exam Questions
Converts scanned PDF question papers to structured JSON with layout preservation.
"""

import json
import logging
import sys
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime

from docling.document_converter import DocumentConverter


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ocr_pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DoclingOCRPipeline:
    """
    Batch OCR pipeline using Docling for converting scanned PDFs to structured JSON.
    """

    def __init__(self, pdf_input_dir: str = "pdfs", json_output_dir: str = "output"):
        """
        Initialize the OCR pipeline.
        
        Args:
            pdf_input_dir: Directory containing source PDF files
            json_output_dir: Directory to write converted JSON files
        """
        self.pdf_dir = Path(pdf_input_dir)
        self.output_dir = Path(json_output_dir)
        self.pdf_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Pipeline initialized: Input={self.pdf_dir}, Output={self.output_dir}")
        
        # Initialize Docling converter
        self.converter = DocumentConverter()

    def process_single_pdf(self, pdf_path: Path) -> Optional[Dict[str, Any]]:
        """
        Convert a single PDF to structured JSON using Docling.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Structured document dictionary or None if conversion fails
        """
        try:
            logger.info(f"Processing: {pdf_path.name}")
            
            # Convert PDF using Docling
            result = self.converter.convert(str(pdf_path))

            # Some Docling versions expose an enum in `result.status`; to avoid
            # compatibility issues we treat a missing `result.document` as failure
            if not getattr(result, 'document', None):
                logger.error(f"Conversion failed for {pdf_path.name}: no document in result")
                return None

            # Export to dictionary
            doc_dict = result.document.model_dump()
            
            # Add metadata
            doc_dict['metadata'] = {
                'source_file': pdf_path.name,
                'conversion_timestamp': datetime.now().isoformat(),
                'converter': 'Docling v1.0+',
                'layout_preserved': True
            }
            
            logger.info(f"Successfully converted {pdf_path.name}")
            return doc_dict
            
        except Exception as e:
            logger.error(f"Error processing {pdf_path.name}: {str(e)}", exc_info=True)
            return None

    def extract_text_blocks(self, doc_dict: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract text blocks from Docling document dictionary.
        Attempts to identify questions, options, and answers.
        
        Args:
            doc_dict: Document dictionary from Docling
            
        Returns:
            List of extracted text block objects
        """
        blocks = []

        # Docling has evolved schemas. Common shapes:
        # - Old: top-level 'pages' each with 'blocks'
        # - Newer: top-level 'texts' where each text item has 'prov' listing page_no and bbox
        if 'pages' in doc_dict and isinstance(doc_dict.get('pages'), list):
            for page_idx, page in enumerate(doc_dict.get('pages', [])):
                if isinstance(page, dict) and 'blocks' in page:
                    for block in page['blocks']:
                        block_info = {
                            'page': page_idx + 1,
                            'type': block.get('type', 'unknown'),
                            'content': block.get('text', ''),
                            'bbox': block.get('bbox', {}),
                        }
                        blocks.append(block_info)

        elif 'texts' in doc_dict and isinstance(doc_dict.get('texts'), list):
            for text_item in doc_dict.get('texts', []):
                content = text_item.get('text') or text_item.get('orig') or ''
                prov = text_item.get('prov') or []
                page_no = None
                bbox = {}
                if prov and isinstance(prov, list) and len(prov) > 0:
                    first = prov[0]
                    page_no = first.get('page_no')
                    bbox = first.get('bbox', {})

                block_info = {
                    'page': page_no,
                    'type': text_item.get('label', 'text'),
                    'content': content,
                    'bbox': bbox,
                }
                blocks.append(block_info)

        return blocks

    def batch_process_pdfs(self) -> Dict[str, Any]:
        """
        Process all PDFs in the input directory.
        
        Returns:
            Summary statistics and conversion report
        """
        # Support PDFs placed in subdirectories (subject folders)
        pdf_files = sorted(self.pdf_dir.rglob("*.pdf"))
        
        if not pdf_files:
            logger.warning(f"No PDF files found in {self.pdf_dir}")
            return {'total': 0, 'successful': 0, 'failed': 0, 'files': []}
        
        logger.info(f"Found {len(pdf_files)} PDF file(s) to process")
        
        stats = {
            'total': len(pdf_files),
            'successful': 0,
            'failed': 0,
            'files': []
        }
        
        for pdf_path in pdf_files:
            doc_dict = self.process_single_pdf(pdf_path)
            
            if doc_dict:
                # Save JSON output
                output_filename = pdf_path.stem + "_docling.json"
                output_path = self.output_dir / output_filename
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(doc_dict, f, indent=2, ensure_ascii=False)
                
                # Save extracted text blocks (easier to parse later)
                blocks = self.extract_text_blocks(doc_dict)
                blocks_filename = pdf_path.stem + "_blocks.json"
                blocks_path = self.output_dir / blocks_filename
                
                with open(blocks_path, 'w', encoding='utf-8') as f:
                    json.dump(blocks, f, indent=2, ensure_ascii=False)
                
                stats['successful'] += 1
                stats['files'].append({
                    'input': pdf_path.name,
                    'output': output_filename,
                    'blocks': blocks_filename,
                    'status': 'success'
                })
            else:
                stats['failed'] += 1
                stats['files'].append({
                    'input': pdf_path.name,
                    'status': 'failed'
                })
        
        # Save conversion report
        report = {
            'timestamp': datetime.now().isoformat(),
            'statistics': stats,
            'pipeline_config': {
                'converter': 'Docling',
                'layout_preservation': True,
                'ocr_engine': 'Built-in Docling vision models'
            }
        }
        
        report_path = self.output_dir / "conversion_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        return stats

    def print_summary(self, stats: Dict[str, Any]) -> None:
        """Print a summary of conversion results."""
        print("\n" + "="*60)
        print("OCR PIPELINE EXECUTION SUMMARY")
        print("="*60)
        print(f"Total PDFs: {stats['total']}")
        print(f"✓ Successful: {stats['successful']}")
        print(f"✗ Failed: {stats['failed']}")
        print(f"Output Directory: {self.output_dir}")
        print("="*60 + "\n")


def main():
    """Main entry point for the OCR pipeline."""
    try:
        pipeline = DoclingOCRPipeline(pdf_input_dir="pdfs", json_output_dir="output")
        stats = pipeline.batch_process_pdfs()
        pipeline.print_summary(stats)
        
        logger.info("Pipeline execution completed")
        return 0
    
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
