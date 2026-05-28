import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3419: {
        "topic": "Choose the Correct Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the start of the multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3420: {
        "topic": "Hypertrophic Osteodystrophy - Age (Review)",
        "Core_Anatomy": "Metaphysis of long bones.",
        "Pathogenesis_Immediate": "HOD is most common in rapidly growing large dogs aged 3-8 months.",
        "Pathogenesis_Deep": "Reiterating the developmental window for this severe metaphyseal inflammation.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3421: {
        "topic": "Panosteitis Radiographic Finding (Review)",
        "Core_Anatomy": "Diaphysis medullary cavity.",
        "Pathogenesis_Immediate": "Panosteitis shows a 'Blurring pattern' or increased medullary opacity on X-rays.",
        "Pathogenesis_Deep": "Reiterating the thumbprint-like patches of woven bone inside the marrow cavity.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3422: {
        "topic": "Craniomandibular Osteopathy Breed (Review)",
        "Core_Anatomy": "Mandible/TMJ.",
        "Pathogenesis_Immediate": "The Scottish Terrier is the classic predisposed breed for CMO.",
        "Pathogenesis_Deep": "Reiterating the non-neoplastic, proliferative bone disease causing 'Lion Jaw'.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3423: {
        "topic": "Cancellous Bone Graft Harvesting - Bone Curette",
        "Core_Anatomy": "Proximal humerus or Proximal tibia (Metaphysis).",
        "Pathogenesis_Immediate": "The primary equipment used for harvesting cancellous bone graft material is a Bone Curette.",
        "Pathogenesis_Deep": "To treat a non-union fracture, the surgeon must pack the fracture gap with fresh osteoblasts and osteoinductive proteins. The best source is the patient's own cancellous (spongy) bone, usually harvested from the greater tubercle of the humerus. A drill is used to breach the hard outer cortex, and then a Bone Curette (a small, spoon-shaped instrument with sharp edges) is inserted into the metaphysis to scoop out the soft, bloody cancellous bone marrow.",
        "Why_Not": "An IM pin or drill bit cannot scoop out the soft marrow. They only make the initial access hole.",
        "Wow_Approach": "The harvested cancellous bone must be kept moist in a blood-soaked sponge; if it dries out under the surgical lights, all the delicate osteoblasts will die before they can be transplanted."
    },
    3424: {
        "topic": "IM Pinning Techniques (Review)",
        "Core_Anatomy": "Medullary cavity.",
        "Pathogenesis_Immediate": "IM pinning can be done by Normograde or Retrograde patterns.",
        "Pathogenesis_Deep": "Reiterating the two directional methods for driving an intramedullary pin.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3425: {
        "topic": "IM Pin Diameter Selection (Review)",
        "Core_Anatomy": "Diaphysis.",
        "Pathogenesis_Immediate": "The ideal IM pin fills 60-70% of the medullary cavity.",
        "Pathogenesis_Deep": "Reiterating that <60% is too weak and >70% risks splitting the bone cortex.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3426: {
        "topic": "Cortical Screws Usage (Review)",
        "Core_Anatomy": "Cortical bone.",
        "Pathogenesis_Immediate": "Cortical screws are designed for dense cortical bone.",
        "Pathogenesis_Deep": "Reiterating that they have fine, closely spaced threads to grip the hard outer bone shell.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3427: {
        "topic": "Orthopaedic Wire - Monofilament",
        "Core_Anatomy": "Fracture site (Cerclage).",
        "Pathogenesis_Immediate": "Orthopaedic wire used in surgery is a Monofilament.",
        "Pathogenesis_Deep": "Orthopaedic wire (cerclage wire) is made of 316L stainless steel. It is manufactured as a single, solid, smooth strand (monofilament) to provide maximum tensile strength and to prevent bacteria from harboring in microscopic crevices. It is wrapped tightly around long oblique or spiral fractures to compress the bone fragments together.",
        "Why_Not": "A multifilament wire (like braided cable) is occasionally used for massive tension band applications, but standard cerclage wire is strictly monofilament.",
        "Wow_Approach": "Cerclage wire MUST be applied in full 360-degree circles. If it is applied in a half-circle or loose loop, it will not compress the bone; instead, it will act like a saw and physically cut through the bone as the animal walks."
    },
    3428: {
        "topic": "Interlocking Nail Sizes (Review)",
        "Core_Anatomy": "Long bones.",
        "Pathogenesis_Immediate": "Standard veterinary interlocking nails come in 6mm and 8mm sizes.",
        "Pathogenesis_Deep": "Reiterating the common diameters used for stabilizing complex diaphyseal fractures in dogs.",
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
