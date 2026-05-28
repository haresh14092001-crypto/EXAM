import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3858: {
        "topic": "Cortical Screws (Review)",
        "Core_Anatomy": "Cortical bone.",
        "Pathogenesis_Immediate": "Cortical screws are designed for dense cortical bone.",
        "Pathogenesis_Deep": "Reiterating that they have fine, closely spaced threads to grip the hard outer shell.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3859: {
        "topic": "Orthopaedic Wire (Review)",
        "Core_Anatomy": "Fracture site.",
        "Pathogenesis_Immediate": "Orthopaedic (cerclage) wire is a monofilament.",
        "Pathogenesis_Deep": "Reiterating the use of solid stainless steel strands for maximum tensile strength and minimal infection risk.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3860: {
        "topic": "Interlocking Nail Sizes (Review)",
        "Core_Anatomy": "Long bones.",
        "Pathogenesis_Immediate": "Veterinary interlocking nails come in 6mm and 8mm sizes.",
        "Pathogenesis_Deep": "Reiterating their use in severe comminuted diaphyseal fractures.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3861: {
        "topic": "Plate Removal Indications (Review)",
        "Core_Anatomy": "Healed fracture site.",
        "Pathogenesis_Immediate": "Bone plates are removed due to irritation, infection, or stress shielding.",
        "Pathogenesis_Deep": "Reiterating the specific complications that necessitate a second surgery to extract the hardware.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3862: {
        "topic": "Hydrotherapy - Downer Cow (Review)",
        "Core_Anatomy": "Skeletal muscle.",
        "Pathogenesis_Immediate": "The buoyancy of water in a hydrotherapy pool is used to treat Downer Cow syndrome.",
        "Pathogenesis_Deep": "Reiterating that removing the crushing weight of gravity allows ischemic muscles to perfuse and the cow to stand.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3863: {
        "topic": "Thermotherapy Indications (Review)",
        "Core_Anatomy": "Peripheral vasculature.",
        "Pathogenesis_Immediate": "Thermotherapy is indicated for Sub-acute and Chronic inflammation.",
        "Pathogenesis_Deep": "Reiterating that heat causes vasodilation, which flushes out chronic inflammatory debris but worsens acute bleeding.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3864: {
        "topic": "Short Wave IR Wavelength (Review)",
        "Core_Anatomy": "Physical therapy modalities.",
        "Pathogenesis_Immediate": "The wavelength of Short-wave Infrared radiation is 770-1500 nm.",
        "Pathogenesis_Deep": "Reiterating its ability to penetrate deeper into the tissues than longwave IR.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3865: {
        "topic": "Diathermy Contraindications (Review)",
        "Core_Anatomy": "Physical therapy modalities.",
        "Pathogenesis_Immediate": "Diathermy is contraindicated in acute inflammation, hemorrhage, and tumors.",
        "Pathogenesis_Deep": "Reiterating the risk of accelerating bleeding and metastatic spread due to deep tissue heating.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3866: {
        "topic": "Tendinitis Treatment (Review)",
        "Core_Anatomy": "Tendons.",
        "Pathogenesis_Immediate": "NSAIDs are the most common drugs used to treat acute tendinitis.",
        "Pathogenesis_Deep": "Reiterating that they reduce severe acute inflammation and provide analgesia.",
        "Why_Not": "Corticosteroids inhibit collagen synthesis and risk complete tendon rupture.",
        "Wow_Approach": "N/A"
    },
    3867: {
        "topic": "Abomasopexy - LDA",
        "Core_Anatomy": "Bovine Abomasum.",
        "Pathogenesis_Immediate": "Abomasopexy is the definitive surgical treatment for Left Displaced Abomasum (LDA).",
        "Pathogenesis_Deep": "LDA is a common postpartum metabolic condition in dairy cows where the gas-filled abomasum slips under the rumen to the left abdominal wall. Abomasopexy involves physically suturing the abomasum (specifically the greater curvature) directly to the ventral abdominal wall, permanently anchoring it in its correct anatomical position.",
        "Why_Not": "An abomasopexy does not treat primary abomasal impaction or rupture.",
        "Wow_Approach": "A quick, minimally invasive alternative is the 'toggle-pin' suture method, where the cow is rolled onto her back and a suture is placed blindly through the abdominal wall into the abomasum, guided by the unique high-pitched 'ping' sound heard when tapping the gas-filled organ."
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
