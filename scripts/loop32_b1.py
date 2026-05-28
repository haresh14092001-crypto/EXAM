import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3583: {
        "topic": "Thermotherapy Indications (Review)",
        "Core_Anatomy": "Peripheral vasculature.",
        "Pathogenesis_Immediate": "Thermotherapy is indicated for Sub-acute and Chronic inflammation.",
        "Pathogenesis_Deep": "Reiterating that heat causes vasodilation, which flushes out chronic inflammatory debris but worsens acute bleeding.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3584: {
        "topic": "Short Wave IR Wavelength (Review)",
        "Core_Anatomy": "Physical therapy modalities.",
        "Pathogenesis_Immediate": "The wavelength of Short-wave Infrared radiation is 770-1500 nm.",
        "Pathogenesis_Deep": "Reiterating its ability to penetrate deeper into the tissues than longwave IR.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3585: {
        "topic": "Diathermy Contraindications (Review)",
        "Core_Anatomy": "Physical therapy modalities.",
        "Pathogenesis_Immediate": "Diathermy is contraindicated in acute inflammation, hemorrhage, and tumors.",
        "Pathogenesis_Deep": "Reiterating the risk of accelerating bleeding and metastatic spread due to deep tissue heating.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3586: {
        "topic": "Wound Healing Modalities (Review)",
        "Core_Anatomy": "Skin and soft tissues.",
        "Pathogenesis_Immediate": "Infrared and Low-Level Laser Therapy accelerate wound healing.",
        "Pathogenesis_Deep": "Reiterating their role in stimulating fibroblast proliferation and angiogenesis.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3587: {
        "topic": "Tendinitis Treatment (Review)",
        "Core_Anatomy": "Tendons.",
        "Pathogenesis_Immediate": "NSAIDs are the most common drugs used to treat acute tendinitis.",
        "Pathogenesis_Deep": "Reiterating that they reduce severe acute inflammation and provide analgesia.",
        "Why_Not": "Corticosteroids inhibit collagen synthesis and risk complete tendon rupture.",
        "Wow_Approach": "N/A"
    },
    3588: {
        "topic": "Time Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options representing hours after trauma.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3589: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3590: {
        "topic": "Green Osselets (Review)",
        "Core_Anatomy": "Fetlock joint.",
        "Pathogenesis_Immediate": "Green osselets are the acute, serous inflammation of the dorsal fetlock joint capsule.",
        "Pathogenesis_Deep": "Reiterating the traumatic origin in young racehorses.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3591: {
        "topic": "Infected by Bacteria Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Option 'Infected by bacteria' for a matching question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3592: {
        "topic": "True Osselets (Review)",
        "Core_Anatomy": "Fetlock joint.",
        "Pathogenesis_Immediate": "True osselets are chronic, bony exostoses on the dorsal fetlock.",
        "Pathogenesis_Deep": "Reiterating the permanent osteoarthritic progression.",
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
