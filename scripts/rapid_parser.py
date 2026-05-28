import json
from pathlib import Path
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_questions_from_texts(texts, subject):
    questions = []
    current_q = []
    
    def save_q():
        if current_q:
            text = " ".join(current_q).strip()
            # Basic validation to ensure it's not just a header or empty
            if len(text) > 15 and not re.match(r'^(?:[A-D]\)|\([a-d]\))$', text):
                # Try to extract marks if present e.g. "(5 marks)" or "(5x1=5)"
                marks = 5 # Default
                
                questions.append({
                    "subject": subject,
                    "topic": "General",
                    "marks": marks,
                    "question_text": text
                })
            current_q.clear()

    for text in texts:
        text = text.strip()
        if not text: continue
        
        # Start a new block if we hit a question number
        if re.match(r'^(?:Q|Question)?\s*\d+[.:)]', text) or re.match(r'^(?:[IVX]+)\.', text) or re.match(r'^Write short notes', text, re.IGNORECASE):
            save_q()
            current_q.append(text)
        # Headers/Footers to ignore
        elif re.match(r'^(?:Part|PART)\s*[A-Z]', text, re.IGNORECASE) or re.match(r'^(?:Time|Maximum|Register|CANCELLED|B\.V\.Sc)', text, re.IGNORECASE) or re.match(r'^MU\s*\d+', text):
            save_q()
        else:
            current_q.append(text)
            
    save_q()
    return questions

def parse_blocks_to_questions(input_dir: str, output_file: str):
    input_path = Path(input_dir)
    all_questions = []
    
    for file_path in input_path.glob("*_blocks.json"):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                logger.error(f"Error loading JSON from {file_path.name}: {e}")
                continue
                
        # Determine subject from filename
        subject_match = re.match(r'^([a-z]+)', file_path.name.lower())
        subject_code = subject_match.group(1).upper() if subject_match else "General"
        if subject_code == "VMD": subject = "Medicine"
        elif subject_code == "VSR": subject = "Surgery"
        elif subject_code == "VGO": subject = "Theriogenology"
        else: subject = subject_code
        
        texts = []
        if isinstance(data, dict) and "pages" in data:
            for page in data["pages"]:
                texts.extend(page.get("texts", []))
        elif isinstance(data, list):
            for block in data:
                if "content" in block:
                    texts.append(block["content"])
        else:
            continue
            
        questions = extract_questions_from_texts(texts, subject)
        all_questions.extend(questions)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Saved {len(all_questions)} questions to {output_file}")

if __name__ == "__main__":
    parse_blocks_to_questions(r"C:\Users\hares\.copilot\EXAM\output", r"C:\Users\hares\.copilot\EXAM\master_questions.json")
