import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3027: {
        "topic": "Teat Surgery - Ring Block",
        "Core_Anatomy": "Bovine Teat (Papilla mammae).",
        "Pathogenesis_Immediate": "The specific nerve block employed for teat surgery in cattle is the Ring Block.",
        "Pathogenesis_Deep": "The bovine teat is highly innervated and exquisitely sensitive. For surgical procedures (like treating a teat spider, fistula, or laceration) in a standing cow, a Ring Block is performed. Local anaesthetic (Lidocaine without epinephrine) is injected subcutaneously and muscularly in a complete circle around the base of the teat. This blocks all descending nerve fibers, completely desensitizing the entire teat distal to the ring.",
        "Why_Not": "A paravertebral block is for the flank (laparotomy). An epidural blocks the perineum/hindlimbs. A cornual block is for the horn.",
        "Wow_Approach": "Never use Lidocaine with Epinephrine for a teat ring block or any extremity block (like a toe/tail). Epinephrine causes intense vasoconstriction, which can completely cut off the blood supply to the teat, causing it to undergo ischemic necrosis and slough off."
    },
    3029: {
        "topic": "Pharmacology Distractor - Drug Classes",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "This line represents options from a pharmacology classification question (Anticholinergic, Sedative, General Anaesthetic, Opioids).",
        "Pathogenesis_Deep": "Recognizing drug classes is fundamental to balanced anaesthesia.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3030: {
        "topic": "Ketamine Dose - Equine Anaesthesia",
        "Core_Anatomy": "Central nervous system (NMDA receptors).",
        "Pathogenesis_Immediate": "The standard induction dose of Ketamine in the horse is 2.2 mg/kg IV.",
        "Pathogenesis_Deep": "Ketamine is a dissociative anaesthetic (NMDA receptor antagonist). In horses, it provides a very rapid, smooth induction (the horse goes down within 60 seconds). However, Ketamine causes severe muscle rigidity and excitement if given alone. Therefore, it MUST ALWAYS be preceded by profound sedation with an alpha-2 agonist (like Xylazine at 1.1 mg/kg or Detomidine). The combination (Xylazine-Ketamine) provides about 15-20 minutes of safe surgical anaesthesia in the field.",
        "Why_Not": "If you give Ketamine to a horse that is not properly sedated, the horse will experience a violent, thrashing excitatory phase that is extremely dangerous to both the animal and the surgical team.",
        "Wow_Approach": "Equine field anaesthesia mnemonic: Xylazine drops the head, Ketamine drops the horse."
    },
    3031: {
        "topic": "Ketamine Dose - Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "This represents an incorrect numerical option (3.3 mg/kg) for the equine Ketamine dose.",
        "Pathogenesis_Deep": "While 2.2 mg/kg is the standard IV induction dose for horses, higher doses (like 3-5 mg/kg) are often required for intramuscular (IM) sedation in aggressive cats or dogs.",
        "Why_Not": "Overdosing Ketamine in horses prolongs recovery and increases the risk of a violent, uncoordinated standing attempt (myoclonus and thrashing).",
        "Wow_Approach": "N/A"
    },
    3032: {
        "topic": "Ketamine Dose - Equine (Confirmation)",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "Confirmation that 2.2 mg/kg is the correct standard induction dose of Ketamine for a horse.",
        "Pathogenesis_Deep": "Because Ketamine has a short duration of action, if the surgery takes longer than 15 minutes, the anaesthesia must be maintained either by connecting the horse to an inhalant machine (Isoflurane) or by administering a 'top-up' dose of IV Ketamine + Xylazine (typically 1/3 to 1/2 of the original induction dose).",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3033: {
        "topic": "Radiographic Grid - Tissue Thickness (Review)",
        "Core_Anatomy": "X-ray physics.",
        "Pathogenesis_Immediate": "As reviewed previously, a grid is employed in radiography when the tissue thickness is >10 cm.",
        "Pathogenesis_Deep": "Tissues >10 cm produce significant Compton scatter, degrading image contrast. The grid absorbs this scatter.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3034: {
        "topic": "Radiographic Developer - Silver Reduction (Review)",
        "Core_Anatomy": "Silver halide emulsion.",
        "Pathogenesis_Immediate": "Developing is the process in which the silver halide in the film emulsion is Reduced to metallic silver.",
        "Pathogenesis_Deep": "The chemical reduction of exposed silver ions into black metallic silver creates the visible radiographic image.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3035: {
        "topic": "X-Ray Film Storage (Review)",
        "Core_Anatomy": "Silver halide emulsion.",
        "Pathogenesis_Immediate": "Unexposed X-ray films should be stored in a Cool and dry location.",
        "Pathogenesis_Deep": "Heat and humidity destroy the delicate gelatin emulsion and cause chemical fogging.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3036: {
        "topic": "Dacryocystorhinography",
        "Core_Anatomy": "Nasolacrimal duct system.",
        "Pathogenesis_Immediate": "The contrast radiographic study of the nasolacrimal duct is called Dacryocystorhinography.",
        "Pathogenesis_Deep": "The nasolacrimal duct drains tears from the medial canthus of the eye into the nasal cavity. When this duct becomes blocked (e.g., by a foreign body, stricture, or tooth root abscess compressing it), tears constantly spill over the face (Epiphora). To diagnose the exact location of the blockage, a fine catheter is placed into the lacrimal punctum, iodinated contrast is injected, and radiographs are taken. This illuminates the entire 'Dacryocystorhinography' tract.",
        "Why_Not": "Cystography is for the bladder. Rhinography is for the nasal cavity itself. Dacryo- refers specifically to tears.",
        "Wow_Approach": "In rabbits, the roots of the maxillary incisors sit directly adjacent to the nasolacrimal duct. Dental disease (tooth root elongation) is the #1 cause of a blocked tear duct and chronic weeping eyes in rabbits."
    },
    3037: {
        "topic": "Father of Veterinary Radiology - R. Eberlin",
        "Core_Anatomy": "History of Veterinary Medicine.",
        "Pathogenesis_Immediate": "The Father of Veterinary Radiology is generally considered to be R. Eberlin (Richard Eberlein).",
        "Pathogenesis_Deep": "Wilhelm Röntgen discovered X-rays in 1895. Within a year (1896), Richard Eberlein, a German veterinarian, was one of the very first to systematically apply this new technology to veterinary medicine, founding the field of Veterinary Radiology by taking radiographs of horses.",
        "Why_Not": "Madame Curie discovered Radium/Polonium (radioactivity). Lister pioneered surgical antisepsis. Eberlein specifically pioneered veterinary X-rays.",
        "Wow_Approach": "Early pioneers of radiology did not understand the dangers of ionizing radiation. Many, including human and veterinary radiographers, suffered severe radiation burns, amputations, and died of radiation-induced cancers before lead shielding was mandated."
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
