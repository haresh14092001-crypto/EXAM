import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    4046: {
        "topic": "Poll Evil (Cranial Nuchal Bursitis)",
        "Core_Anatomy": "Cranial Nuchal Bursa (Atlanto-axial region).",
        "Pathogenesis_Immediate": "Poll Evil is the clinical term for chronic, suppurative inflammation of the cranial nuchal bursa in horses.",
        "Pathogenesis_Deep": "The nuchal bursa sits over the atlas (C1) and axis (C2) to protect the nuchal ligament from friction. Infection is classically initiated by trauma or systemic hematogenous spread of Brucella abortus or Actinomyces bovis. The bursa undergoes intense, chronic suppurative necrosis, leading to deep, draining fistulous tracts in the poll region that are exceptionally difficult to heal due to the poor blood supply of the nuchal ligament.",
        "Why_Not": "Fistulous withers is a similar suppurative infection but is located at the supraspinous bursa over the thoracic vertebrae, not the poll.",
        "Wow_Approach": "N/A"
    },
    4051: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a short notes section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4063: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4064: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4065: {
        "topic": "Exam Instruction (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating handing over the paper.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4066: {
        "topic": "Objective Type Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of an objective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4067: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4085: {
        "topic": "Multiple Choice Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4086: {
        "topic": "Colles' Fracture (Review)",
        "Core_Anatomy": "Distal Radius.",
        "Pathogenesis_Immediate": "A Colles' fracture is a fracture of the distal end of the radius.",
        "Pathogenesis_Deep": "Reiterating that this involves transverse fracture of the distal radial metaphysis.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4087: {
        "topic": "Z-Tenotomy - Tendon Lengthening",
        "Core_Anatomy": "Tendons.",
        "Pathogenesis_Immediate": "Z-Tenotomy is the definitive surgical technique used for tendon Lengthening.",
        "Pathogenesis_Deep": "When a tendon is severely contracted (such as congenital flexural deformity in calves), it holds the joint in a permanent, non-functional flexed state. Z-tenotomy involves making a Z-shaped incision through the tendon: cutting longitudinally down the middle and then transversely at opposite ends of the cut. The two halves are slid apart to the desired length and sutured, permanently lengthening the tendon.",
        "Why_Not": "Tendon folding is used for shortening a lax tendon, which is the exact opposite of Z-tenotomy.",
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
print(f"Batch 2/5 DONE: Updated {updated} questions.")
