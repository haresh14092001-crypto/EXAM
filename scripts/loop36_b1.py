import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    799: {
        "topic": "True or False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a True or False section in Theriogenology.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    809: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section in Theriogenology.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4020: {
        "topic": "Buttress Foot (Pyramidal Disease)",
        "Core_Anatomy": "Equine Hoof (Extensor process of P3).",
        "Pathogenesis_Immediate": "Buttress foot (Pyramidal Disease) is characterized by severe exostosis at the extensor process of the third phalanx.",
        "Pathogenesis_Deep": "This is caused by chronic pull and strain of the common digital extensor tendon at its insertion point on the extensor process of P3, often secondary to poor hoof conformation or trauma. The body reacts by laying down massive exostosis (new bone), creating a prominent bulge at the coronary band ('pyramidal' appearance) and eventually leading to severe lameness and deformity of the hoof wall.",
        "Why_Not": "Thrush is an infectious disease of the frog. Sand crack is a simple fissure in the wall.",
        "Wow_Approach": "N/A"
    },
    4021: {
        "topic": "Equine Foot Diseases Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Corn, Canker, Ringbone, All) for a hoof disease question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4022: {
        "topic": "True or False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a True or False section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4033: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4034: {
        "topic": "Joint Mice - OCD",
        "Core_Anatomy": "Synovial Joint (Cartilage).",
        "Pathogenesis_Immediate": "Joint mice are loose, free-floating pieces of articular cartilage or bone within the joint space, classically caused by Osteochondrosis Dissecans (OCD).",
        "Pathogenesis_Deep": "In growing animals, defective endochondral ossification leaves thick, unmineralized areas of joint cartilage. Under loading, this cartilage flaps off, eventually tearing completely free to float inside the joint cavity. These free fragments (joint mice) survive by absorbing nutrients from the synovial fluid, occasionally growing larger and getting caught between articulating bones, causing acute pain and lock-up.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4035: {
        "topic": "Guttural Pouch Empyema",
        "Core_Anatomy": "Equine Guttural Pouch.",
        "Pathogenesis_Immediate": "Guttural Pouch Empyema is the accumulation of purulent exudate (pus) within the guttural pouch, classically secondary to Strangles (Streptococcus equi infection).",
        "Pathogenesis_Deep": "The guttural pouch is a large air-filled diverticulum of the eustachian tube in horses. Upper respiratory infections by S. equi invade the retropharyngeal lymph nodes, which abscess and rupture directly into the guttural pouch. Over time, the pus thickens and dehydrates into hard, egg-shaped stones called chondroids, preventing drainage and causing chronic nasal discharge and cranial nerve deficits.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4036: {
        "topic": "Urolithiasis - Cattle (Review)",
        "Core_Anatomy": "Bovine Urethra.",
        "Pathogenesis_Immediate": "Urethral calculi in cattle lodge at the distal Sigmoid flexure.",
        "Pathogenesis_Deep": "Reiterating that the narrowing of the urethral lumen at the distal curve of the sigmoid flexure is the primary site of obstruction.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4037: {
        "topic": "Gastropexy - GDV (Review)",
        "Core_Anatomy": "Stomach.",
        "Pathogenesis_Immediate": "Gastropexy is the definitive surgical prevention for GDV recurrence.",
        "Pathogenesis_Deep": "Reiterating the creation of a permanent adhesion between the pyloric antrum and right abdominal wall.",
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
print(f"Batch 1/5 DONE: Updated {updated} questions.")
