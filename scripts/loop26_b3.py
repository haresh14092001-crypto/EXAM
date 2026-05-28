import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2998: {
        "topic": "VSR Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper I.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2999: {
        "topic": "VSR Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper I.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3001: {
        "topic": "Objective Questions Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the objective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3002: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for fill in the blanks.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3021: {
        "topic": "Ranula - Marsupialization",
        "Core_Anatomy": "Sublingual salivary gland and oral mucosa.",
        "Pathogenesis_Immediate": "Marsupialization is the specific surgical treatment for a Ranula.",
        "Pathogenesis_Deep": "A ranula is a specific type of salivary mucocele (accumulation of saliva) located under the tongue, usually arising from the sublingual or mandibular salivary gland duct. It presents as a large, fluctuant swelling on the floor of the mouth that can physically push the tongue aside and interfere with swallowing. While most salivary mucoceles require gland extirpation, a ranula can be treated by Marsupialization. This involves excising an elliptical piece of the ranula roof (oral mucosa) and suturing the lining of the cyst directly to the oral mucosa, creating a permanent stoma (pouch) that allows the saliva to drain freely into the mouth.",
        "Why_Not": "Simple lancing/draining will result in the ranula closing over and instantly refilling within days.",
        "Wow_Approach": "The term 'marsupialization' comes from creating a pouch, like a marsupial (kangaroo)."
    },
    3022: {
        "topic": "Brain Cyst Distractor / Options",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "This line represents an OCR artifact blending multiple choice options (Cyst, Haematoma, Abscess, Tumour) with the subsequent question about brain cysts.",
        "Pathogenesis_Deep": "Structural artifact from scanning.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3023: {
        "topic": "Exploratory Surgery",
        "Core_Anatomy": "Usually Abdominal cavity (Celiotomy).",
        "Pathogenesis_Immediate": "Surgery performed specifically to arrive at a diagnosis is called Exploratory Surgery.",
        "Pathogenesis_Deep": "When advanced imaging (ultrasound/CT) is unavailable or inconclusive, and the patient is deteriorating, an exploratory surgery (usually an exploratory laparotomy/celiotomy) is indicated. The surgeon systematically evaluates every organ in the abdominal cavity to find the cause of the disease (e.g., finding a tiny perforated ulcer or an intestinal foreign body).",
        "Why_Not": "Clinical surgery treats a known problem. Cosmetic surgery alters appearance. Exploratory surgery is purely diagnostic.",
        "Wow_Approach": "A thorough exploratory laparotomy MUST be systematic. The standard method is to evaluate the cranial quadrant (liver/stomach/spleen), then 'run the bowel' entirely from duodenum to descending colon, then check the caudal quadrant (bladder/prostate/uterus), and finally the retroperitoneal space (kidneys/adrenals). Missing a step means missing the diagnosis."
    },
    3024: {
        "topic": "Gingival Tumor - Epulis",
        "Core_Anatomy": "Gingiva (Periodontal ligament).",
        "Pathogenesis_Immediate": "As noted previously, a tumor arising specifically from the gingiva is called an Epulis.",
        "Pathogenesis_Deep": "Revisiting this high-yield concept: Acanthomatous epulis requires bone resection due to local invasion, while fibromatous and ossifying epulides are benign and only require excision down to the periodontal ligament.",
        "Why_Not": "Odontoma is dental tissue. Chondroma is cartilage. Osteoma is bone.",
        "Wow_Approach": "Always radiograph the jaw before removing an epulis to check for underlying bone lysis."
    },
    3025: {
        "topic": "Triflupromazine Premedication - Barbiturate Sparing",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "Triflupromazine (a phenothiazine tranquilizer) is used before a barbiturate anaesthetic to Decrease the dose of barbiturates required.",
        "Pathogenesis_Deep": "Like Xylazine or Acepromazine, Triflupromazine is a premedication that provides CNS depression. The primary anaesthetic goal of ANY premedication is the 'dose-sparing effect'. By tranquilizing the patient first, the amount of the dangerous induction agent (Thiopental) required to cross the surgical threshold is drastically reduced (by up to 50%).",
        "Why_Not": "Increasing the barbiturate dose after giving a tranquilizer would cause a fatal overdose.",
        "Wow_Approach": "Triflupromazine also has potent anti-emetic properties, preventing the animal from vomiting during induction, which drastically reduces the risk of aspiration pneumonia."
    },
    3026: {
        "topic": "Inhalant Anaesthesia - Recovery Time",
        "Core_Anatomy": "Pulmonary alveoli.",
        "Pathogenesis_Immediate": "Recovery is faster in Inhalant anaesthesia compared to injectable anaesthesia.",
        "Pathogenesis_Deep": "As reviewed earlier, because inhalant agents (Isoflurane) are eliminated via respiration rather than hepatic metabolism, the patient wakes up within minutes of turning off the vaporizer.",
        "Why_Not": "Intravenous agents like Ketamine or Propofol require redistribution and metabolism, which delays recovery.",
        "Wow_Approach": "If a dog is hypothermic (cold) after surgery, its metabolism slows down. Injectable drugs will take hours to wear off. However, even a cold dog will wake up rapidly from inhalant anaesthesia as long as its lungs are ventilating."
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
