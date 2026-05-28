import json
import re
import ast
from pathlib import Path

workspace_dir = Path(r"c:\Users\hares\.antigravity\EXAM")
database_path = workspace_dir / "database.js"
scripts_dir = workspace_dir / "scripts"

# Load current database.js
with open(database_path, "r", encoding="utf-8") as f:
    content = f.read()
start_idx = content.find('[')
end_idx = content.rfind(']') + 1
db = json.loads(content[start_idx:end_idx])
print(f"Loaded active database with {len(db)} questions.")

# We will extract all enrichment dictionaries from all loop python files
all_enrichments = {}

# Match files like loop*.py or batch*.py
py_files = list(scripts_dir.glob("*.py"))
print(f"Found {len(py_files)} python files in scripts.")

for py_file in py_files:
    # Skip non-enrichment files
    if py_file.name in ["fast_ocr.py", "hybrid_builder.py", "monitor_ocr_progress.py", "ocr_pipeline.py", "question_parser.py", "rapid_parser.py", "reparse_questions.py", "run_pipeline.py"]:
        continue
        
    with open(py_file, "r", encoding="utf-8") as f:
        file_content = f.read()
        
    # We want to parse the 'enrichment' or 'enrichment_data' dict from the file.
    # We can use ast to find dict definitions.
    try:
        tree = ast.parse(file_content)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in ["enrichment", "enrichment_data"]:
                        # Convert the dict node back to a python dict using ast.literal_eval or eval
                        # To be safe and handle multi-line strings, we can evaluate the dict node
                        # since it's just a static dict of strings.
                        dict_code = compile(ast.Expression(node.value), py_file.name, "eval")
                        dict_val = eval(dict_code)
                        if isinstance(dict_val, dict):
                            for qid, qdata in dict_val.items():
                                # Standardize keys
                                if qid not in all_enrichments:
                                    all_enrichments[qid] = qdata
                                else:
                                    all_enrichments[qid].update(qdata)
    except Exception as e:
        print(f"Failed to parse {py_file.name}: {e}")

print(f"Extracted {len(all_enrichments)} unique question enrichments from python loops.")

# Now, we want to match these enrichments to our active database questions.
# Since we exploded the database, the IDs might have shifted.
# How can we match?
# We can match by normalized question text!
# Let's create a map from normalized question text to the enrichment data.
def normalize_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

normalized_enrichments = {}
for qid, qdata in all_enrichments.items():
    # If the enrichment has clinical answers
    if qdata.get("Core_Anatomy"):
        # We need to find the question text associated with this qid.
        # But wait, does the enrichment dictionary have the question text?
        # Some enrichments only have topic, Core_Anatomy, etc., not the original question_text!
        # But wait, in the copilot folder's database.js, the qid matches the original question ID!
        # So we can load the copilot's database.js to find the original question_text for each qid!
        pass

# Let's load the copilot database to map qid -> question_text
copilot_db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
cop_qmap = {}
if copilot_db_path.exists():
    with open(copilot_db_path, "r", encoding="utf-8") as f:
        cop_content = f.read()
    c_start = cop_content.find('[')
    c_end = cop_content.rfind(']') + 1
    cop_db = json.loads(cop_content[c_start:c_end])
    for cq in cop_db:
        cop_qmap[cq["id"]] = cq.get("question_text", "")
    print(f"Mapped {len(cop_qmap)} questions from copilot database.")

# Map normalized original text to its clinical answer
normalized_answers = {}
for qid, qdata in all_enrichments.items():
    orig_text = cop_qmap.get(qid, "")
    if orig_text:
        norm_orig = normalize_text(orig_text)
        if norm_orig:
            normalized_answers[norm_orig] = qdata

# Also map the enrichment by topic in case question text shifted slightly
topic_answers = {}
for qid, qdata in all_enrichments.items():
    topic = qdata.get("topic")
    if topic:
        topic_answers[topic.lower()] = qdata

print(f"Created {len(normalized_answers)} text-based and {len(topic_answers)} topic-based lookup maps.")

# Apply to active database
matched_count = 0
for q in db:
    # Try to match by normalized question text first
    norm_q = normalize_text(q.get("question_text", ""))
    matched = False
    
    if norm_q in normalized_answers:
        ans = normalized_answers[norm_q]
        q["Core_Anatomy"] = ans.get("Core_Anatomy", "")
        q["Pathogenesis_Immediate"] = ans.get("Pathogenesis_Immediate", "")
        q["Pathogenesis_Deep"] = ans.get("Pathogenesis_Deep", "")
        q["Why_Not"] = ans.get("Why_Not", "")
        q["Wow_Approach"] = ans.get("Wow_Approach", "")
        if ans.get("topic"):
            q["topic"] = ans.get("topic")
        matched = True
    elif q.get("topic") and q.get("topic").lower() in topic_answers:
        ans = topic_answers[q["topic"].lower()]
        q["Core_Anatomy"] = ans.get("Core_Anatomy", "")
        q["Pathogenesis_Immediate"] = ans.get("Pathogenesis_Immediate", "")
        q["Pathogenesis_Deep"] = ans.get("Pathogenesis_Deep", "")
        q["Why_Not"] = ans.get("Why_Not", "")
        q["Wow_Approach"] = ans.get("Wow_Approach", "")
        matched = True
        
    if matched:
        matched_count += 1

print(f"Successfully matched and filled {matched_count} questions in the active database!")
print(f"Remaining empty high yield: {sum(1 for q in db if q['is_high_yield'] and not q['Core_Anatomy'])}")

# Save back to database.js
js_content = "const examData = " + json.dumps(db, indent=2, ensure_ascii=False) + ";\n"
with open(database_path, "w", encoding="utf-8") as f:
    f.write(js_content)
print("Updated database.js successfully.")
