import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3429: {
        "topic": "Complications of Internal Fixation (Review)",
        "Core_Anatomy": "Fracture site.",
        "Pathogenesis_Immediate": "Complications include Non-union, Mal-union, and Delayed union.",
        "Pathogenesis_Deep": "Reiterating the failures of osteogenesis associated with poor mechanical stability or biology.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3430: {
        "topic": "Plaster of Paris - Water Temperature (Review)",
        "Core_Anatomy": "External coaptation.",
        "Pathogenesis_Immediate": "The water used for activating Plaster of Paris should be around 37°C.",
        "Pathogenesis_Deep": "Reiterating that hot water accelerates the exothermic reaction and causes severe thermal burns.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3431: {
        "topic": "Tibia Plating Approach (Review)",
        "Core_Anatomy": "Tibia (Medial aspect).",
        "Pathogenesis_Immediate": "The standard approach for plating the tibia is Medial.",
        "Pathogenesis_Deep": "Reiterating that the medial tibia has absolutely zero muscle coverage, providing easy surgical exposure.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3432: {
        "topic": "Bone Plate Removal Indications (Review)",
        "Core_Anatomy": "Healed fracture site.",
        "Pathogenesis_Immediate": "Bone plates are removed if they cause irritation, infection, or stress shielding.",
        "Pathogenesis_Deep": "Reiterating that asymptomatic plates are generally left in place for the life of the animal.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3433: {
        "topic": "Thermotherapy Indications Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Sub acute, Chronic, Sprain) for the thermotherapy question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3434: {
        "topic": "Short Wave IR Wavelength Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options for the Short-wave IR wavelength (770-1500 nm).",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3435: {
        "topic": "Diathermy Contraindications Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Acute inflammation, Hemorrhages, Tumours) for the diathermy contraindications question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3436: {
        "topic": "Wound Healing Modalities Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Infra red, Short wave diathermy, Ultrasounds) for the wound healing question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3437: {
        "topic": "Tendinitis Treatment - NSAIDs",
        "Core_Anatomy": "Tendons (e.g., Superficial/Deep Digital Flexor).",
        "Pathogenesis_Immediate": "The drugs most often used in the primary medical treatment of acute tendinitis are NSAIDs.",
        "Pathogenesis_Deep": "Tendinitis (like a 'Bowed Tendon' in a racehorse) is characterized by severe acute inflammation, edema, and collagen fiber tearing within the tendon. Non-Steroidal Anti-Inflammatory Drugs (NSAIDs like Phenylbutazone or Flunixin) are the gold standard to rapidly reduce the swelling and provide analgesia, which prevents further mechanical tearing from the animal favoring the limb.",
        "Why_Not": "Systemic corticosteroids (Hydrocortisone) are strictly avoided because they inhibit collagen synthesis and severely delay tendon healing, increasing the risk of complete rupture.",
        "Wow_Approach": "Medical therapy alone will not heal a bowed tendon. The horse MUST undergo a strict, 9-to-12-month controlled rehabilitation program to allow the collagen fibers to realign properly along the lines of stress."
    },
    3438: {
        "topic": "Thermotherapy Contraindication - Acute Phase (Review)",
        "Core_Anatomy": "Peripheral vasculature.",
        "Pathogenesis_Immediate": "Thermotherapy should NEVER be used during the first 24 to 48 hours after acute trauma.",
        "Pathogenesis_Deep": "Reiterating that heat causes vasodilation and will massively exacerbate acute bleeding and swelling. Ice (cryotherapy) must be used initially.",
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
