import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3124: {
        "topic": "Viborg's Triangle Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "These are the incorrect options (Zygomatic, Temporal) for the Viborg's Triangle question.",
        "Pathogenesis_Deep": "Structural artifact from scanning.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3125: {
        "topic": "Cheilitis - Inflammation of Lips",
        "Core_Anatomy": "Lips (Labia oris).",
        "Pathogenesis_Immediate": "Inflammation specifically of the lips is clinically termed Cheilitis.",
        "Pathogenesis_Deep": "Cheilitis can be caused by trauma, contact allergies (e.g., plastic food bowls in dogs causing lip fold dermatitis), or autoimmune diseases. It frequently occurs in dogs with deep lip folds (Spaniels, Bulldogs) where saliva and food get trapped, creating a moist, anaerobic environment for bacterial and yeast (Malassezia) overgrowth.",
        "Why_Not": "Glossitis is inflammation of the tongue. Palatitis is the palate. Gnathitis refers to the jaw.",
        "Wow_Approach": "Severe, chronic lip fold cheilitis in dogs that does not respond to medical management is surgically cured by a 'Lip Fold Excision' (Cheiloplasty), which permanently removes the redundant skin fold, eliminating the moist pocket."
    },
    3126: {
        "topic": "Vesicocele - Herniation of the Bladder",
        "Core_Anatomy": "Urinary bladder and Body wall.",
        "Pathogenesis_Immediate": "Herniation of the urinary bladder is medically termed a Vesicocele (or Cystocele).",
        "Pathogenesis_Deep": "As reviewed, this is a life-threatening surgical emergency when it occurs secondary to a perineal hernia in an older, intact male dog. The bladder retroflexes backwards into the perineal sac and the urethra kinks, causing anuria, post-renal uremia, and rapid death from hyperkalemia if not reduced immediately.",
        "Why_Not": "Hysterocele = uterus. Ureterocele = ureter.",
        "Wow_Approach": "N/A"
    },
    3137: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching question section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3138: {
        "topic": "Neuroleptanalgesia - Innovar-Vet",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "Droperidol and Fentanyl combination is matched to Neuroleptanalgesia / Innovar-Vet.",
        "Pathogenesis_Deep": "Reiterating that combining a potent tranquilizer (Droperidol/butyrophenone) with a potent opioid (Fentanyl/Mu-agonist) produces profound neuroleptanalgesia.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3148: {
        "topic": "Cherry Eye Definition",
        "Core_Anatomy": "Nictitating membrane (Third eyelid).",
        "Pathogenesis_Immediate": "Header for a definition section, specifically asking for 'Cherry Eye'.",
        "Pathogenesis_Deep": "Cherry Eye is the prolapse of the gland of the third eyelid. It MUST be surgically replaced (Morgan pocket technique), never excised, to prevent keratoconjunctivitis sicca (dry eye).",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3153: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the short notes section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3168: {
        "topic": "VSR Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3169: {
        "topic": "VSR Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3170: {
        "topic": "Exam Instruction",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction regarding handing the paper to the hall superintendent.",
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
print(f"Batch 4/5 DONE: Updated {updated} questions.")
