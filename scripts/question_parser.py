"""
Question Parser: Extract structured questions from Docling JSON output.
Parses text blocks to identify questions, options, and answers.
Prepares data for LLM enrichment (Why, How, Why Not, Wow framework).
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
import re


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QuestionParser:
    """
    Parse Docling-generated JSON to extract structured exam questions.
    """

    def __init__(self, blocks_json_path: Path):
        """
        Initialize parser with blocks JSON from Docling.
        
        Args:
            blocks_json_path: Path to _blocks.json file from OCR pipeline
        """
        with open(blocks_json_path, 'r', encoding='utf-8') as f:
            self.blocks = json.load(f)
        
        self.questions = []
        logger.info(f"Loaded {len(self.blocks)} text blocks")

    def identify_question_pattern(self, text: str) -> Optional[str]:
        """
        Detect if text block is a question (common patterns).
        
        Returns:
            'mcq', 'short_answer', 'long_essay', or None
        """
        text = text.strip()
        
        # Multiple choice question pattern (e.g., "1.", "A)", "i)")
        if re.match(r'^[a-d]\)', text) or re.match(r'^[A-D]\)', text):
            return 'mcq_option'
        
        # Question number pattern (e.g., "1.", "Q1", "Question 1:")
        if re.match(r'^(?:Q|Question)?\s*\d+[.:)]', text):
            return 'question_start'
        
        # Answer key pattern (e.g., "Answer: A", "Ans: B)
        if re.match(r'^(?:Answer|Ans|ANS)\s*[:=-]?\s*[a-dA-D]', text):
            return 'answer_key'
        
        return None

    def merge_text_blocks(self, start_idx: int, end_idx: int) -> str:
        """Merge multiple text blocks into single string."""
        merged = []
        for i in range(start_idx, min(end_idx, len(self.blocks))):
            if 'content' in self.blocks[i]:
                content = self.blocks[i]['content'].strip()
                if content:
                    merged.append(content)
        return '\n'.join(merged)

    def parse_mcq_section(self, block_idx: int) -> Optional[Dict[str, Any]]:
        """
        Parse a multiple choice question section.
        Assumes format:
            Q1: Question text here?
            a) Option A
            b) Option B
            c) Option C
            d) Option D
            Answer: A
        
        Args:
            block_idx: Starting index of question block
            
        Returns:
            Structured question dict or None
        """
        if block_idx >= len(self.blocks):
            return None
        
        question_text = self.blocks[block_idx].get('content', '').strip()
        
        # Skip if doesn't look like question start
        if not re.match(r'^(?:Q|Question)?\s*\d+', question_text):
            return None
        
        # Extract question number and text
        match = re.match(r'^(?:Q|Question)?\s*(\d+)[.:)]\s*(.*)', question_text, re.DOTALL)
        if not match:
            return None
        
        q_number = match.group(1)
        q_text = match.group(2).strip()
        
        options = []
        answer_key = None
        idx = block_idx + 1
        
        # Collect options and answer
        while idx < len(self.blocks) and len(options) < 4:
            content = self.blocks[idx].get('content', '').strip()
            
            # Check for answer key
            answer_match = re.match(r'^(?:Answer|Ans|ANS)\s*[:=-]?\s*([a-dA-D])', content)
            if answer_match:
                answer_key = answer_match.group(1).upper()
                break
            
            # Check for option
            option_match = re.match(r'^([a-d])\)\s*(.*)', content)
            if option_match:
                option_label = option_match.group(1).upper()
                option_text = option_match.group(2).strip()
                options.append({
                    'label': option_label,
                    'text': option_text
                })
            
            idx += 1
        
        # Only return if we have at least question and some options
        if q_text and len(options) >= 2:
            return {
                'type': 'mcq',
                'question_number': q_number,
                'question_text': q_text,
                'options': options,
                'answer_key': answer_key,
                'source_blocks': list(range(block_idx, idx)),
                'requires_enrichment': True  # Flag for LLM enrichment
            }
        
        return None

    def extract_all_questions(self) -> List[Dict[str, Any]]:
        """
        Scan all blocks and extract structured questions.
        
        Returns:
            List of question dictionaries
        """
        questions = []
        idx = 0
        
        while idx < len(self.blocks):
            pattern = self.identify_question_pattern(self.blocks[idx].get('content', ''))
            
            if pattern == 'question_start':
                q = self.parse_mcq_section(idx)
                if q:
                    questions.append(q)
                    idx += len(q.get('source_blocks', []))
                else:
                    idx += 1
            else:
                idx += 1
        
        logger.info(f"Extracted {len(questions)} questions from blocks")
        return questions

    def save_questions(self, output_path: Path) -> None:
        """Save extracted questions to JSON."""
        questions = self.extract_all_questions()
        
        output = {
            'metadata': {
                'total_questions': len(questions),
                'parser': 'QuestionParser v1.0',
                'status': 'raw_extraction'
            },
            'questions': questions
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved {len(questions)} questions to {output_path}")


def batch_parse_blocks(blocks_dir: Path, output_dir: Path) -> None:
    """
    Parse all _blocks.json files in a directory.
    
    Args:
        blocks_dir: Directory containing _blocks.json files
        output_dir: Directory to save parsed questions
    """
    blocks_files = sorted(blocks_dir.glob("*_blocks.json"))
    
    for blocks_file in blocks_files:
        try:
            parser = QuestionParser(blocks_file)
            output_file = output_dir / blocks_file.stem.replace('_blocks', '_parsed_questions') / '.json'
            parser.save_questions(output_file)
        except Exception as e:
            logger.error(f"Error parsing {blocks_file}: {str(e)}")


if __name__ == "__main__":
    # Example usage:
    # from pathlib import Path
    # parser = QuestionParser(Path("output/sample_blocks.json"))
    # parser.save_questions(Path("output/sample_parsed_questions.json"))
    pass
