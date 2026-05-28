import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    4117: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4118: {
        "topic": "Ileus",
        "Core_Anatomy": "Intestine.",
        "Pathogenesis_Immediate": "Ileus refers to the complete failure of normal intestinal peristalsis (paralysis), leading to non-mechanical intestinal obstruction.",
        "Pathogenesis_Deep": "It can be caused by peritoneal inflammation (peritonitis), electrolyte imbalances (hypokalemia), or handling of the bowel during surgery (post-operative ileus). Without motility, gas and fluid accumulate inside the bowel, causing severe distension and clinical signs resembling mechanical colic.",
        "Why_Not": "Mechanical obstruction is a physical block (like a foreign body or volvulus), whereas ileus is strictly functional paralysis.",
        "Wow_Approach": "N/A"
    },
    4119: {
        "topic": "Frothy Bloat (Review)",
        "Core_Anatomy": "Rumen.",
        "Pathogenesis_Immediate": "Frothy bloat is caused by feeding on highly digestible pasture legumes or heavy grains, trapping gas in a stable foam.",
        "Pathogenesis_Deep": "Reiterating that soluble proteins in legumes form a stable foam that traps normal fermentation gases, preventing the cow from belching (eructation).",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4120: {
        "topic": "5th Rib Resection (Review)",
        "Core_Anatomy": "Thorax.",
        "Pathogenesis_Immediate": "Resection of the 5th rib is the standard approach for a pericardiectomy in cases of constrictive pericarditis.",
        "Pathogenesis_Deep": "Reiterating that removing a portion of the 5th rib provides direct access to the cardiac apex and pericardial sac.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4121: {
        "topic": "Endoscopy",
        "Core_Anatomy": "Internal luminal organs.",
        "Pathogenesis_Immediate": "Endoscopy is a minimally invasive diagnostic aid used to directly visualize the interior of hollow internal organs.",
        "Pathogenesis_Deep": "An endoscope containing a fiberoptic light source and video camera is guided into luminal cavities (such as the esophagus, stomach, trachea, or colon) to evaluate mucosal health, take biopsies, or retrieve foreign bodies.",
        "Why_Not": "Radiography provides shadow projections of density, not direct color visualization of mucosal surfaces.",
        "Wow_Approach": "N/A"
    },
    4129: {
        "topic": "Subjective Questions Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a subjective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4131: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a short notes section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    }
}

updated = 0
for q in data:
    if q['id'] in enrichment and not q.get('Core_Anatomy'):
        q.update(enrichment[q['id']])
        updated += 1

with open(db_path, "w", encoding="utf-8") as f:
    f.write("// Auto-generated Hybrid Exam Database\n")
    f.write("const examData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n")

# Final validation
with open(db_path, "r", encoding="utf-8") as f:
    c2 = f.read()
d2 = json.loads(re.sub(r'^.*?const examData = ', '', c2, flags=re.DOTALL).rsplit(';',1)[0].strip())
empty2 = [x for x in d2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
