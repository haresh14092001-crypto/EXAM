import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3966: {
        "topic": "Colic (Review)",
        "Core_Anatomy": "Abdomen.",
        "Pathogenesis_Immediate": "Acute abdominal pain is termed Colic.",
        "Pathogenesis_Deep": "Reiterating that this represents visceral pain arising from distension, twisting, or inflammation of abdominal organs.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3967: {
        "topic": "Bovine Caecal Dilatation",
        "Core_Anatomy": "Caecum.",
        "Pathogenesis_Immediate": "Caecal dilatation in dairy cattle is heavily associated with high grain feeding.",
        "Pathogenesis_Deep": "Similar to LDA, feeding excess concentrates leads to a massive flow of fermentable carbohydrates into the large intestine. The resulting fermentation produces volatile fatty acids that cause complete caecal hypomotility and gas accumulation, leading to caecal dilatation, which can progress to caecal torsion.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3973: {
        "topic": "Flail Chest",
        "Core_Anatomy": "Rib cage and Pleural Cavity.",
        "Pathogenesis_Immediate": "Flail Chest is a life-threatening thoracic trauma characterized by the fracture of multiple consecutive ribs in two or more places.",
        "Pathogenesis_Deep": "This creates a completely free-floating segment of the chest wall. During inhalation, as the diaphragm contracts and creates negative pressure inside the chest, the flail segment is sucked INWARD instead of moving outward (paradoxical respiration). This severely compromises ventilation and gas exchange, leading to rapid hypoxia and respiratory acidosis, compounded by severe underlying pulmonary contusion.",
        "Why_Not": "A simple rib fracture only involves a single break, maintaining the rigid structure of the thoracic wall.",
        "Wow_Approach": "To temporarily stabilize a flail chest, the dog must be placed in lateral recumbency on the affected side, using the floor to physically splint and hold the flail segment in place."
    },
    3979: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3980: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3981: {
        "topic": "Exam Instruction (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating a thirty-minute time limit for Part-A.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3982: {
        "topic": "Objective Type Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of an objective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3983: {
        "topic": "Rumenotomy Frame (Review)",
        "Core_Anatomy": "Rumen and Abdominal Wall.",
        "Pathogenesis_Immediate": "Weingarth's frame is used for securing the rumen to the skin.",
        "Pathogenesis_Deep": "Reiterating that the frame clamps the rumen edges to prevent fatal peritoneal contamination.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3998: {
        "topic": "Mal-union (Review)",
        "Core_Anatomy": "Healed bone.",
        "Pathogenesis_Immediate": "The healing of a bone in a non-functional or abnormal anatomic position is a Mal-union.",
        "Pathogenesis_Deep": "Reiterating the mechanical consequences of poor reduction, leading to angular, rotational, or short-limb deformities.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3999: {
        "topic": "Multiple Choice Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple-choice section.",
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
