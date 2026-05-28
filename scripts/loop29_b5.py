import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3357: {
        "topic": "Hydrotherapy - Downer Cow",
        "Core_Anatomy": "Skeletal muscle and limbs.",
        "Pathogenesis_Immediate": "The buoyancy of water is classically utilized as a physical therapy modality for Downer Cow Syndrome.",
        "Pathogenesis_Deep": "A cow that has been recumbent for >24 hours suffers from severe ischemic necrosis (crush syndrome) of her down-side muscles. Because she weighs 600kg, she cannot lift herself. Placing the cow in a warm flotation tank (hydrotherapy pool) uses the physical principle of buoyancy to completely remove the crushing weight of gravity. This instantly restores perfusion to the ischemic muscles and allows the cow to stand and exercise her legs without bearing weight.",
        "Why_Not": "An open fracture is a strict contraindication for a hydrotherapy pool due to massive infection risk. Acidosis is a metabolic problem, not a mechanical one.",
        "Wow_Approach": "If a cow can stand in the float tank, her prognosis improves drastically. However, the water must be kept warm; cold water will induce severe hypothermia."
    },
    3358: {
        "topic": "Thermotherapy Indications",
        "Core_Anatomy": "Peripheral vasculature.",
        "Pathogenesis_Immediate": "Thermotherapy (the application of heat) is indicated for Sub-acute and Chronic inflammation.",
        "Pathogenesis_Deep": "Heat causes vasodilation, increases local tissue metabolism, enhances leukocyte infiltration, and relaxes muscle spasms. This is highly beneficial for resolving chronic, indolent infections (pointing an abscess) or treating chronic osteoarthritis.",
        "Why_Not": "Heat is strictly contraindicated in ACUTE inflammation because the vessels are already massively dilated and leaking. Adding heat to a fresh sprain will cause the swelling to explode.",
        "Wow_Approach": "N/A"
    },
    3359: {
        "topic": "Short Wave Infrared Wavelength",
        "Core_Anatomy": "Physical therapy modalities.",
        "Pathogenesis_Immediate": "The wavelength of Short-wave Infrared radiation is approximately 770 nm to 1500 nm.",
        "Pathogenesis_Deep": "Infrared (IR) radiation sits just beyond the visible red spectrum. Short-wave IR penetrates deeper into the tissues (up to 5-10 mm) compared to long-wave IR (which only heats the superficial epidermis). It provides deep, soothing, dry radiant heat for chronic musculoskeletal injuries.",
        "Why_Not": "Ultraviolet (UV) has a shorter wavelength (<400 nm) and is used for killing surface bacteria or treating skin conditions, not deep heating.",
        "Wow_Approach": "N/A"
    },
    3360: {
        "topic": "Diathermy Contraindications",
        "Core_Anatomy": "Physical therapy modalities.",
        "Pathogenesis_Immediate": "Contraindications for Diathermy include Acute inflammation, Hemorrhages, and Tumors.",
        "Pathogenesis_Deep": "Diathermy (Shortwave, Microwave, or Ultrasound) uses high-frequency electromagnetic or sound waves to generate intense heat DEEP within the tissues (muscles/joints). Because it causes massive deep vasodilation, it will severely worsen acute bleeding (hemorrhage) and exacerbate acute inflammation. Crucially, increasing the blood flow and metabolic rate of a Tumor will drastically accelerate its growth and metastasis.",
        "Why_Not": "It is indicated for chronic joint stiffness and deep muscle contractures.",
        "Wow_Approach": "Never use Diathermy over metal surgical implants (like bone plates), as the metal will absorb the energy, superheat, and literally cook the surrounding bone from the inside out."
    },
    3361: {
        "topic": "Wound Healing Modalities - Infrared / Laser",
        "Core_Anatomy": "Skin and soft tissues.",
        "Pathogenesis_Immediate": "Wound healing is clinically accelerated when treated with modalities like Infrared radiation or Low-Level Laser Therapy (LLLT).",
        "Pathogenesis_Deep": "These modalities stimulate fibroblast proliferation, enhance local angiogenesis (new blood vessel formation), and increase ATP production within the cells via photobiomodulation. This speeds up the granulation and epithelialization phases of wound healing.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3362: {
        "topic": "Pharmacology Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (NSAIDs, Hydrocortisone, Antibiotics, H2 blockers) likely belonging to an anti-inflammatory or ulcer question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3363: {
        "topic": "Thermotherapy Contraindication - Acute Phase",
        "Core_Anatomy": "Peripheral vasculature.",
        "Pathogenesis_Immediate": "Thermotherapy (heat) should NEVER be used during the first 24 to 48 hours after acute trauma.",
        "Pathogenesis_Deep": "The first 24-48 hours represent the acute inflammatory phase, characterized by active hemorrhage, massive vasodilation, and edema. Applying heat will dramatically worsen the bleeding and swelling. The correct modality for the first 48 hours is Cryotherapy (Cold/Ice), which causes intense vasoconstriction, stopping hemorrhage and preventing the edema from forming.",
        "Why_Not": "Once the acute phase passes (after 48-72 hours), the vessels stabilize, and you can switch to heat (Thermotherapy) to help flush out the accumulated inflammatory debris.",
        "Wow_Approach": "Mnemonic: Ice for the first 48, Heat to negotiate."
    },
    3364: {
        "topic": "Green Osselets",
        "Core_Anatomy": "Equine Fetlock (Metacarpophalangeal joint).",
        "Pathogenesis_Immediate": "Green Osselets refers to the acute, hot, painful serous inflammation of the dorsal fetlock joint capsule.",
        "Pathogenesis_Deep": "This is a common traumatic injury in young, rapidly growing racehorses subjected to heavy training before their bones are fully mature. The massive, repetitive overextension of the fetlock joint at a gallop tears the dorsal joint capsule attachment off the distal cannon bone. 'Green' osselets refers to the initial, acute, fluid-filled stage. If the horse continues to run, it progresses to 'True' osselets: severe osteoarthritis and permanent new bone formation (exostosis) on the dorsal aspect of the joint.",
        "Why_Not": "Ringbone is the pastern/coffin joint. Splints involve the interosseous ligament of the metacarpals. Osselets specifically target the dorsal fetlock.",
        "Wow_Approach": "The only cure for green osselets is immediate, complete rest for several months. If the horse is rested, the capsule heals. If pushed to run, the horse will be permanently crippled by arthritis."
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

# Final validation
with open(db_path, "r", encoding="utf-8") as f:
    c2 = f.read()
d2 = json.loads(re.sub(r'^.*?const examData = ', '', c2, flags=re.DOTALL).rsplit(';',1)[0].strip())
empty2 = [x for x in d2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
