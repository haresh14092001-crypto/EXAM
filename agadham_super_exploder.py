import json
import re
import copy
from pathlib import Path

def clean_text(text):
    if not text:
        return ""
    
    # 1. Mark breakdowns (e.g. (10 x 0.5 = 5), [10*0.5=5])
    text = re.sub(r'\(?\d+\s*[\*x\u00d7×]\s*\d+(?:\.\d+)?\s*=\s*\d+\)?', '', text)
    text = re.sub(r'\[\d+\s*[\*x\u00d7×]\s*\d+(?:\.\d+)?\s*=\s*\d+\]', '', text)
    text = re.sub(r'\(\s*\d+\s*marks?\s*\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d+X\d+(?:\.\d+)?\b', '', text, flags=re.IGNORECASE)
    
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
        r"State True or False\s*:\s*\(10\s*x\s*1\s*=\s*10\)",
        r"Multiple choice\s*\(Tick the most appropriate answer\)\s*:",
        r"Multiple choice",
        r"Column A Column B",
        r"Twoof the following\s*:",
        r"Two of the following",
        r"FOUR",
        r"ELLED",
        r"CANCEL\s*:",
        r"I\)\s+MEDICINE",
        r"MEDICINE CANCEL",
        r"VETERINARYEPIDEMIOLOGY AND PREVENTIVE MEDICINE"
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
    text = re.sub(r'^[:\-\.\s\u00d7×\*,()]+', '', text)
    
    # 5. Remove leading orphaned numbers/letters
    # e.g., "1. ", "12. ", "a. ", "i. ", "(a) ", "4 FMD"
    text = re.sub(r'^(?:\d+\.|\b[a-z]\.|\b[ivx]+\.|\([a-z]\)|\(\d+\))\s*', '', text, flags=re.IGNORECASE)
    
    # Clean again in case of new leading spaces/junk
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'^[:\-\.\s\u00d7×\*,()]+', '', text)
    return text

def parse_and_split_aggressive(text):
    if not text:
        return []
        
    # Phase A: Initial split on hard statements separated by period and capital letter
    # e.g. "Snail is a intermediate host. Bottle jaw condition seen."
    # We avoid splitting abbreviations like spp. or e.g.
    parts = re.split(r'(?<!\bspp)(?<!\bsp)(?<!\be\.g)(?<!\bi\.e)\.\s+(?=[A-Z])', text)
    
    sub_parts = []
    for part in parts:
        part_clean = clean_text(part)
        if not part_clean:
            continue
            
        # Phase B: Split on sub-numbered items in run-on lists, e.g. "1. Tricalbendazole... 2. Ivermectin..."
        # or "a) Aerosal route b) By contact"
        sub_list = re.split(r'\s*(?:\b\d+\.|\b[ivx]+\.|\(\d+\)|\b[a-zA-Z]\)\s+|\(\s*[a-zA-Z]\s*\))\s*', part_clean)
        for item in sub_list:
            item_clean = clean_text(item)
            if item_clean and len(item_clean) > 8:
                # Avoid splitting options of a single small MCQ question
                # e.g. if the item is just "Staphylococcus aureus", it's an option, let's keep it if it's part of a single stem
                sub_parts.append(item_clean)
                
    # Phase C: Let's clean up and filter out items that are too short or just noisy fragments
    final_parts = []
    for p in sub_parts:
        c = clean_text(p)
        if c and len(c) > 8:
            # Check if this looks like a fragment (e.g. "and (b)")
            if c.lower() in ["and", "both", "none", "none of the above", "and both", "and (b)"]:
                continue
            # Remove leading/trailing fragments
            c = re.sub(r'^(?:and|or|but|with)\s+', '', c, flags=re.IGNORECASE)
            c = clean_text(c)
            if c and len(c) > 8:
                final_parts.append(c)
                
    return final_parts

def main():
    workspace_dir = Path(r"c:\Users\hares\.antigravity\EXAM")
    database_path = workspace_dir / "database.js"
    
    print("Loading database.js for aggressive explosion...")
    with open(database_path, "r", encoding="utf-8") as f:
        db_content = f.read()
        
    start_idx = db_content.find('[')
    end_idx = db_content.rfind(']') + 1
    db = json.loads(db_content[start_idx:end_idx])
    print(f"Loaded {len(db)} questions from database.js.")
    
    new_db = []
    split_count = 0
    total_exploded_questions = 0
    
    for q in db:
        orig_text = q.get("question_text", "")
        is_hy = q.get("is_high_yield", False)
        
        # Aggressive split
        splits = parse_and_split_aggressive(orig_text)
        
        if len(splits) > 1:
            split_count += 1
            total_exploded_questions += len(splits)
            for part in splits:
                new_q = {
                    "id": 0,  # Will assign later
                    "subject": q.get("subject", "General"),
                    "topic": q.get("topic", "General"),
                    "marks": q.get("marks", 5),
                    "question_text": part,
                    "is_high_yield": True,  # Tag exploded parts as high_yield = True
                    "Core_Anatomy": "",
                    "Pathogenesis_Immediate": "",
                    "Pathogenesis_Deep": "",
                    "Why_Not": "",
                    "Wow_Approach": ""
                }
                new_db.append(new_q)
        else:
            part_text = splits[0] if splits else clean_text(orig_text)
            new_q = {
                "id": 0,
                "subject": q.get("subject", "General"),
                "topic": q.get("topic", "General"),
                "marks": q.get("marks", 5),
                "question_text": part_text,
                "is_high_yield": is_hy,
                "Core_Anatomy": q.get("Core_Anatomy", ""),
                "Pathogenesis_Immediate": q.get("Pathogenesis_Immediate", ""),
                "Pathogenesis_Deep": q.get("Pathogenesis_Deep", ""),
                "Why_Not": q.get("Why_Not", ""),
                "Wow_Approach": q.get("Wow_Approach", "")
            }
            new_db.append(new_q)
            
    # Re-assign sequential IDs from 1 to N
    for idx, q in enumerate(new_db):
        q["id"] = idx + 1
        
    print(f"Aggressively processed database. Exploded {split_count} questions into {total_exploded_questions} sub-questions.")
    print(f"Total questions in new database: {len(new_db)}")
    print(f"High yield questions in new database: {sum(1 for q in new_db if q['is_high_yield'])}")
    
    # Save back to database.js in strict global assignment format
    js_content = "const examData = " + json.dumps(new_db, indent=2, ensure_ascii=False) + ";\n"
    with open(database_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Pristine database.js written successfully.")

if __name__ == "__main__":
    main()
