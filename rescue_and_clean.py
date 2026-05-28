import json
import re
from pathlib import Path

# Paths
workspace_dir = Path(r"c:\Users\hares\.antigravity\EXAM")
copilot_dir = Path(r"c:\Users\hares\.copilot\EXAM")

master_path = workspace_dir / "master_questions.json"
one_marks_path = workspace_dir / "one_marks.json"
heavy_path = workspace_dir / "heavy_questions.json"
database_src_path = copilot_dir / "database.js"
database_out_path = workspace_dir / "database.js"

print("Starting Python Rescue & Sanitization Script...")

# Load master questions
with open(master_path, "r", encoding="utf-8") as f:
    master_questions = json.load(f)
print(f"Loaded {len(master_questions)} master questions.")

# Load triage files
with open(one_marks_path, "r", encoding="utf-8") as f:
    one_marks = json.load(f)
with open(heavy_path, "r", encoding="utf-8") as f:
    heavy_questions = json.load(f)
print(f"Loaded {len(one_marks)} one-mark questions and {len(heavy_questions)} heavy questions from triage.")

# Load existing database.js to rescue answers
with open(database_src_path, "r", encoding="utf-8") as f:
    db_content = f.read()
# Extract JSON array from database.js
json_str = db_content[db_content.find('['):db_content.rfind(']')+1]
database_src = json.loads(json_str)
print(f"Loaded {len(database_src)} items from the original database.js source.")

def normalize_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

# Create sets of normalized question texts for fast lookup
one_marks_set = {normalize_text(q.get('question_text')) for q in one_marks if q.get('question_text')}
heavy_set = {normalize_text(q.get('question_text')) for q in heavy_questions if q.get('question_text')}

def clean_question_text(text):
    if not text:
        return ""
    
    # 1. Mark breakdowns
    # (10 x 0.5 = 5), (10*0.5=5), [10x1=10], (5), (10×0.5=5), (16 \u00d7 0.5 = 8), etc.
    text = re.sub(r'\(?\d+\s*[\*x\u00d7×]\s*\d+(?:\.\d+)?\s*=\s*\d+\)?', '', text)
    text = re.sub(r'\[\d+\s*[\*x\u00d7×]\s*\d+(?:\.\d+)?\s*=\s*\d+\]', '', text)
    text = re.sub(r'\(\s*\d+\s*marks?\s*\)', '', text, flags=re.IGNORECASE)
    
    # 2. Instruction fluff
    fluff_patterns = [
        r"\(?Objective type question's\)?",
        r"\(?Objective type questions\)?",
        r"Objective type",
        r"Read the following sentences carefully and answer whether the statement is I\.",
        r"Read the following sentences carefully and answer whether the statement is",
        r"Read the following sentences carefully",
        r"answer whether the statement is",
        r"True or false",
        r"True/false",
        r"State True or False",
        r"State True or FALSE",
        r"Fill in the blanks",
        r"Fill in the blank",
        r"Fill ups",
        r"Fill up",
        r"Answer any five",
        r"Answer any 5",
        r"Answer any three",
        r"Answer any 3",
        r"Answer any four",
        r"Answer any 4",
        r"Answer any TWO",
        r"Answer any 2",
        r"Write in detail on any",
        r"Write short notes on any",
        r"Write short notes on",
        r"Match the following",
        r"Choose the correct",
        r"Do not write on this area",
        r"State True or False\s*:\s*\(20\s*x\s*1\.0\s*=\s*20\)",
        r"State True or False\s*:\s*\(10\s*x\s*1\s*=\s*10\)"
    ]
    
    for pattern in fluff_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
        
    # 3. Course codes and headers
    text = re.sub(r'\(?VE[P|S|M|G|C]\s*\d+\s*(?:-\s*[A-Z\s\-]+)?\)?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(?VM[D|G|S|C]\s*\d+\s*(?:-\s*[A-Z\s\-]+)?\)?', '', text, flags=re.IGNORECASE)
    
    course_headers = [
        r"VETERINARY EPIDEMIOLOGY AND PREVENTIVE MEDICINE\s*(?:-\s*II)?",
        r"VETERINARY EPIDEMIOLOGY AND PREVENTIVE MEDICINE",
        r"VETERINARY MEDICINE",
        r"CLINICAL MEDICINE",
        r"VETERINARY, GYNAECOLOGY AND OBSTETRICS",
        r"GENERAL AND SYSTEMIC",
        r"METABOLIC AND DEFICIENCY DISEASES",
        r"SECTION\s*(?:I|II|III|IV|H|HI|I-|II-)",
        r"PREV\s*MED\s*\d*\s*(?:[A-Za-z]+)?",
        r"\(\d{4}-\d{2}\s*Regulations\)"
    ]
    
    for header in course_headers:
        text = re.sub(header, '', text, flags=re.IGNORECASE)
        
    # 4. Clean spacing & punctuation
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'^[:\-\.\s\u00d7×\*,]+', '', text)
    
    # 5. Remove leading orphaned numbers/letters
    # e.g., "1. ", "12. ", "a. ", "i. ", "(a) ", "4 FMD"
    text = re.sub(r'^(?:\d+\.|\b[a-z]\.|\b[ivx]+\.|\([a-z]\)|\(\d+\))\s*', '', text, flags=re.IGNORECASE)
    
    # Clean again in case of new leading spaces/junk
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'^[:\-\.\s\u00d7×\*,]+', '', text)
    
    return text

reassembled_db = []
heavy_merged_count = 0
one_mark_merged_count = 0

for i, q in enumerate(master_questions):
    orig_text = q.get('question_text', '')
    cleaned_text = clean_question_text(orig_text)
    
    norm_text = normalize_text(orig_text)
    
    is_high_yield = False
    
    # Check if this question is high yield (exists in triage files)
    is_in_one_marks = norm_text in one_marks_set
    is_in_heavy = norm_text in heavy_set
    
    db_item = database_src[i] if i < len(database_src) else {}
    
    # Initialize the target object
    new_q = {
        "id": i + 1,
        "subject": q.get('subject', 'General'),
        "topic": db_item.get('topic', q.get('topic', 'General')),
        "marks": q.get('marks', 5),
        "question_text": cleaned_text,
        "is_high_yield": False
    }
    
    # Bring over answers if is_high_yield
    if is_in_one_marks or is_in_heavy or db_item.get('is_high_yield'):
        new_q["is_high_yield"] = True
        
        # Try to rescue generated answers from database.js
        new_q["Core_Anatomy"] = db_item.get("Core_Anatomy", "N/A")
        new_q["Pathogenesis_Immediate"] = db_item.get("Pathogenesis_Immediate", "N/A")
        new_q["Pathogenesis_Deep"] = db_item.get("Pathogenesis_Deep", "N/A")
        new_q["Why_Not"] = db_item.get("Why_Not", "N/A")
        new_q["Wow_Approach"] = db_item.get("Wow_Approach", "N/A")
        
        if is_in_heavy:
            heavy_merged_count += 1
        elif is_in_one_marks:
            one_mark_merged_count += 1
    else:
        # Fill empty fields for non-high yield
        new_q["Core_Anatomy"] = ""
        new_q["Pathogenesis_Immediate"] = ""
        new_q["Pathogenesis_Deep"] = ""
        new_q["Why_Not"] = ""
        new_q["Wow_Approach"] = ""
        
    reassembled_db.append(new_q)

# Safe Export to database.js in strict format
js_content = "const examData = " + json.dumps(reassembled_db, indent=2, ensure_ascii=False) + ";\n"

with open(database_out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully reassembled database with {len(reassembled_db)} questions.")
print(f"Heavy questions merged: {heavy_merged_count}")
print(f"One-mark questions merged: {one_mark_merged_count}")
print(f"Total High Yield questions preserved: {sum(1 for q in reassembled_db if q['is_high_yield'])}")
