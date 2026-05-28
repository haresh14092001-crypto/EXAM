import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3052: {
        "topic": "Roentgen - Unit of Exposure",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "The Roentgen (R) is the legacy unit of X-ray exposure in air.",
        "Pathogenesis_Deep": "It measures the ionization produced in air by X-rays or gamma rays. It is not a measure of the biological effect (which is the Sievert) or the absorbed dose (which is the Gray).",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3053: {
        "topic": "Closed Wound Healing",
        "Core_Anatomy": "Skin and soft tissues.",
        "Pathogenesis_Immediate": "A closed surgical wound heals by Primary Intention (first intention).",
        "Pathogenesis_Deep": "When wound edges are apposed precisely with sutures, with minimal tissue loss and no infection, epithelialization and rapid fibrous union occur within days.",
        "Why_Not": "Open wounds heal by secondary intention (granulation tissue).",
        "Wow_Approach": "N/A"
    },
    3054: {
        "topic": "Potter-Bucky Diaphragm",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "The Potter-Bucky diaphragm absorbs scattered radiation.",
        "Pathogenesis_Deep": "As reviewed earlier, it is an oscillating lead grid under the X-ray table that absorbs off-angle scattered X-rays coming from thick patients (>10cm), drastically improving image contrast without leaving visible grid lines on the film.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3066: {
        "topic": "Define/Explain Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a short-answer subjective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3074: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of a short essay section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3081: {
        "topic": "VSR Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology Paper I.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3082: {
        "topic": "VSR Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3083: {
        "topic": "Exam Instruction - Time Limit",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating the objective section time limit is 30 minutes.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3084: {
        "topic": "Objective Questions Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the objective type questions.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3085: {
        "topic": "Alpha-2 Adrenergic Sedatives",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "An example of an alpha-2 adrenergic sedative is Xylazine (or Detomidine, Medetomidine).",
        "Pathogenesis_Deep": "Alpha-2 agonists bind to presynaptic alpha-2 receptors in the CNS, inhibiting the release of norepinephrine. This causes profound sedation, excellent muscle relaxation, and good analgesia. However, they also cause severe, potentially fatal cardiovascular side effects (initial massive hypertension followed by profound bradycardia and hypotension).",
        "Why_Not": "Acepromazine is an alpha-1 antagonist (phenothiazine). Diazepam is a GABA agonist (benzodiazepine).",
        "Wow_Approach": "The bradycardia caused by alpha-2 agonists (like Dexmedetomidine) should NEVER be treated with Atropine unless you reverse the drug first. Giving Atropine while the massive peripheral vasoconstriction is still present will force the heart to pump incredibly fast against a closed system, leading to fatal cardiac workload and failure."
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
