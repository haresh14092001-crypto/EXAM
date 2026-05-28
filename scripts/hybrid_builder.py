import json
from pathlib import Path
import re
import collections

def normalize_text(text):
    # Lowercase, remove non-alphanumeric characters, and strip spaces
    return re.sub(r'[^a-z0-9]', '', text.lower())

def is_one_mark(text):
    text_lower = text.lower()
    # Patterns indicating 1-mark sections
    one_mark_indicators = [
        "true or false", "true/false", "fill in the blank", "fill up",
        "match the following", "choose the correct", "multiple choice",
        "objective type", "1x1=", "1*1=", "0.5=", "1 =", "1="
    ]
    if any(indicator in text_lower for indicator in one_mark_indicators):
        return True
    
    # Also check if it looks like an MCQ option block
    if re.search(r'\([a-d]\)', text_lower) or re.search(r'\b[a-d]\)', text_lower):
        return True
        
    return False

def build_hybrid_database(master_json_path: str, output_js_path: str):
    master_path = Path(master_json_path)
    
    if not master_path.exists():
        print(f"Error: {master_json_path} does not exist.")
        return
        
    with open(master_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)
        
    print(f"Loaded {len(questions)} questions from {master_json_path}")
    
    # Identify duplicates/repetitions (frequently repeated short/long answers)
    normalized_counts = collections.Counter()
    for q in questions:
        norm = normalize_text(q.get("question_text", ""))
        if len(norm) > 20: # ignore very short noises
            normalized_counts[norm] += 1
            
    # Compile the hybrid list
    hybrid_questions = []
    high_yield_count = 0
    
    for idx, q in enumerate(questions):
        text = q.get("question_text", "")
        norm = normalize_text(text)
        
        # Check if high yield
        one_mark = is_one_mark(text)
        is_repeated = normalized_counts[norm] >= 2 if len(norm) > 20 else False
        
        is_high_yield = one_mark or is_repeated
        if is_high_yield:
            high_yield_count += 1
            
        hybrid_questions.append({
            "id": idx + 1,
            "subject": q.get("subject", "General"),
            "topic": q.get("topic", "General"),
            "marks": q.get("marks", 5),
            "question_text": text,
            "is_high_yield": is_high_yield,
            "Core_Anatomy": "",
            "Pathogenesis_Immediate": "",
            "Pathogenesis_Deep": "",
            "Why_Not": "",
            "Wow_Approach": ""
        })
        
    # Write to database.js
    with open(output_js_path, 'w', encoding='utf-8') as f:
        f.write("// Auto-generated Hybrid Exam Database\n")
        f.write("const examData = ")
        json.dump(hybrid_questions, f, indent=2, ensure_ascii=False)
        f.write(";\n")
        
    print(f"Successfully processed {len(hybrid_questions)} questions.")
    print(f"High-Yield questions identified: {high_yield_count}")
    print(f"Saved to {output_js_path}")

if __name__ == "__main__":
    build_hybrid_database(
        r"C:\Users\hares\.copilot\EXAM\master_questions.json",
        r"C:\Users\hares\.copilot\EXAM\database.js"
    )
