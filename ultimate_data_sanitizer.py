import json
import re
import copy
from pathlib import Path

def clean_text(text):
    if not text:
        return ""
    
    # 1. Mark breakdowns
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

def parse_and_split_advanced(text):
    if not text:
        return []
        
    cleaned_initial = clean_text(text)
    if not cleaned_initial:
        return []
        
    # Find option markers
    opt_matches = list(re.finditer(r'\([a-eA-E]\)\s*|\b[a-eA-E]\)\s+', cleaned_initial))
    
    if not opt_matches:
        # Split by explicit numbered items first
        sub_parts = re.split(r'\s*(?:\b\d+\.|\b[ivx]+\.|\(\d+\))\s*', cleaned_initial)
        if len(sub_parts) > 1:
            res = []
            for part in sub_parts:
                c = clean_text(part)
                if c and len(c) > 6:
                    res.append(c)
            if res:
                return res
        # Split by sentence
        sub_parts = re.split(r'(?<=[.!?])\s+', cleaned_initial)
        res = []
        for part in sub_parts:
            c = clean_text(part)
            if c and len(c) > 6:
                res.append(c)
        return res if res else [cleaned_initial]

    # Process options
    segments = []
    first_stem = cleaned_initial[0:opt_matches[0].start()].strip()
    segments.append({
        "type": "stem",
        "text": first_stem
    })
    
    for i in range(len(opt_matches)):
        marker = opt_matches[i].group(0).strip()
        start = opt_matches[i].end()
        end = opt_matches[i+1].start() if i+1 < len(opt_matches) else len(cleaned_initial)
        content = cleaned_initial[start:end].strip()
        
        segments.append({
            "type": "option",
            "marker": marker,
            "text": content
        })
        
    questions = []
    current_stem = first_stem
    current_options = []
    
    for idx, seg in enumerate(segments):
        if seg["type"] == "stem":
            continue
            
        marker = seg["marker"]
        text_val = seg["text"]
        
        next_is_new_q = False
        if idx + 1 < len(segments):
            next_seg = segments[idx+1]
            if next_seg["type"] == "option" and next_seg["marker"].lower() in ["(a)", "a)"]:
                next_is_new_q = True
                
        if next_is_new_q:
            words = text_val.split()
            split_idx = -1
            for w_idx in range(1, len(words)):
                word = words[w_idx]
                if word[0].isupper() and word not in ["spp.", "spp", "I", "II", "III", "IV"]:
                    split_idx = w_idx
                    break
                elif re.match(r'^\d', word):
                    split_idx = w_idx
                    break
            
            if split_idx != -1:
                opt_part = " ".join(words[:split_idx])
                next_stem_part = " ".join(words[split_idx:])
            else:
                opt_part = text_val
                next_stem_part = ""
                
            current_options.append(f"{marker} {opt_part}")
            
            # --- STEM SPLITTING FOR CURRENT QUESTION ---
            stem_sentences = re.split(r'(?<=[.!?])\s+', current_stem)
            if len(stem_sentences) > 1:
                for s in stem_sentences[:-1]:
                    cs = clean_text(s)
                    if cs and len(cs) > 6:
                        questions.append(cs)
                active_stem = stem_sentences[-1]
            else:
                active_stem = current_stem
                
            q_text = active_stem
            if current_options:
                q_text += " " + " ".join(current_options)
            questions.append(q_text)
            
            current_stem = next_stem_part
            current_options = []
        else:
            current_options.append(f"{marker} {text_val}")
            
    # Save the last question
    stem_sentences = re.split(r'(?<=[.!?])\s+', current_stem)
    if len(stem_sentences) > 1:
        for s in stem_sentences[:-1]:
            cs = clean_text(s)
            if cs and len(cs) > 6:
                questions.append(cs)
        active_stem = stem_sentences[-1]
    else:
        active_stem = current_stem
        
    q_text = active_stem
    if current_options:
        q_text += " " + " ".join(current_options)
    questions.append(q_text)
    
    # Final clean of all questions
    final_qs = []
    for q in questions:
        c = clean_text(q)
        if c and len(c) > 6:
            final_qs.append(c)
    return final_qs

def main():
    workspace_dir = Path(r"c:\Users\hares\.antigravity\EXAM")
    database_path = workspace_dir / "database.js"
    
    print("Loading database.js...")
    with open(database_path, "r", encoding="utf-8") as f:
        db_content = f.read()
        
    # Extract JSON array
    start_idx = db_content.find('[')
    end_idx = db_content.rfind(']') + 1
    db = json.loads(db_content[start_idx:end_idx])
    print(f"Loaded {len(db)} questions from database.js.")
    
    # Store backup in memory
    db_backup = copy.deepcopy(db)
    
    new_db = []
    split_count = 0
    total_exploded_questions = 0
    
    for q in db:
        orig_text = q.get("question_text", "")
        is_hy = q.get("is_high_yield", False)
        
        # Advanced parse and split
        splits = parse_and_split_advanced(orig_text)
        
        if len(splits) > 1:
            split_count += 1
            total_exploded_questions += len(splits)
            # Create separate high-yield objects for each split part
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
            # Keep the original question and clean it
            part_text = splits[0] if splits else clean_text(orig_text)
            new_q = {
                "id": 0,
                "subject": q.get("subject", "General"),
                "topic": q.get("topic", "General"),
                "marks": q.get("marks", 5),
                "question_text": part_text,
                "is_high_yield": is_hy,
                # Preserve answers exactly if not split
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
        
    print(f"Processed database. Exploded {split_count} questions into {total_exploded_questions} sub-questions.")
    print(f"Total questions in new database: {len(new_db)}")
    print(f"High yield questions in new database: {sum(1 for q in new_db if q['is_high_yield'])}")
    print(f"Empty high yield questions to fill: {sum(1 for q in new_db if q['is_high_yield'] and (not q['Core_Anatomy'] or q['Core_Anatomy'] == 'N/A'))}")
    
    # Export back to database.js in strict format
    js_content = "const examData = " + json.dumps(new_db, indent=2, ensure_ascii=False) + ";\n"
    with open(database_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Pristine database.js written successfully.")

if __name__ == "__main__":
    main()
