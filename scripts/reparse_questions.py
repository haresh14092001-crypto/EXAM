import json
import re
import sys

def parse_questions(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return []

    clean_questions = []
    global_id = 1

    # Regex to find numbers starting a sentence (e.g. "1. ", "12. ", "(1) ")
    # Or multiple choice options (a), (b), etc if they stand alone as questions (unlikely, usually they are options)
    # We will split by \b\d+\.\s
    split_pattern = re.compile(r'(?=\b\d+\.\s+)')

    for chunk in data:
        text = chunk.get('question_text', '')
        if not text:
            continue
            
        subject = chunk.get('subject', 'General')
        topic = chunk.get('topic', 'General')

        # Split the chunk into parts
        parts = split_pattern.split(text)
        
        for part in parts:
            part = part.strip()
            # Ignore empty parts or tiny headers (like "True or False:")
            if len(part) < 10 and not re.search(r'\d+\.', part):
                continue
                
            # If it's just a chunk of text without a number, it might be a header.
            # But let's keep it if it's long enough, as it might be a question that lost its number in OCR.
            
            clean_q = {
                "id": global_id,
                "subject": subject,
                "topic": topic,
                "question_text": part
            }
            clean_questions.append(clean_q)
            global_id += 1

    return clean_questions

if __name__ == "__main__":
    input_file = r"C:\Users\hares\.antigravity\EXAM\master_questions.json"
    output_file = r"C:\Users\hares\.antigravity\EXAM\database.js"
    
    print("Parsing questions...")
    parsed_data = parse_questions(input_file)
    
    print(f"Extracted {len(parsed_data)} individual questions.")
    
    # Save to database.js
    js_content = "// Auto-generated Clean Exam Database\n"
    js_content += "window.examData = " + json.dumps(parsed_data, indent=2) + ";\n"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print("Successfully wrote clean questions to database.js!")
