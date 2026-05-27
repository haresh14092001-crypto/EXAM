"""
Unified OCR + Question Extraction Pipeline
Orchestrates full workflow: PDF → Docling JSON → Parsed Questions
"""

import json
import sys
import logging
from pathlib import Path
from ocr_pipeline import DoclingOCRPipeline
from question_parser import QuestionParser


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_full_pipeline():
    """
    Execute complete OCR → parsing pipeline:
    1. Convert PDFs to Docling JSON
    2. Extract text blocks
    3. Parse structured questions
    4. Save enrichment-ready questions
    """
    logger.info("Starting full OCR pipeline...")
    
    # Step 1: OCR
    logger.info("\n[STEP 1] Running Docling OCR conversion...")
    ocr = DoclingOCRPipeline(pdf_input_dir="pdfs", json_output_dir="output")
    ocr_stats = ocr.batch_process_pdfs()
    ocr.print_summary(ocr_stats)
    
    if ocr_stats['successful'] == 0:
        logger.warning("No PDFs were successfully converted. Exiting.")
        return 1
    
    # Step 2: Parse questions
    logger.info("\n[STEP 2] Extracting questions from Docling output...")
    output_dir = Path("output")
    blocks_files = sorted(output_dir.glob("*_blocks.json"))
    
    all_questions = []
    for blocks_file in blocks_files:
        try:
            logger.info(f"  Parsing {blocks_file.name}...")
            parser = QuestionParser(blocks_file)
            questions = parser.extract_all_questions()
            all_questions.extend(questions)
        except Exception as e:
            logger.error(f"  ✗ Error parsing {blocks_file}: {str(e)}")
    
    logger.info(f"\n✓ Total questions extracted: {len(all_questions)}")
    
    # Step 3: Save combined dataset
    if all_questions:
        combined_output = {
            'metadata': {
                'total_questions': len(all_questions),
                'source_pdfs': ocr_stats['successful'],
                'status': 'awaiting_enrichment',
                'enrichment_framework': 'Why-How-WhyNot-Wow',
                'next_step': 'LLM enrichment with clinical context'
            },
            'questions': all_questions
        }
        
        output_file = output_dir / "all_questions_raw.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(combined_output, f, indent=2, ensure_ascii=False)
        
        logger.info(f"\n✓ Combined dataset saved to {output_file}")
        logger.info(f"  Ready for LLM enrichment (Why-How-WhyNot-Wow framework)")
    
    return 0


if __name__ == "__main__":
    sys.exit(run_full_pipeline())
