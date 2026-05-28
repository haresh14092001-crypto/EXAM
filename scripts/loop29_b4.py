import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3347: {
        "topic": "Cancelled Question - Bone Instruments",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a cancelled question regarding intramedullary pins or bone curettes.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3348: {
        "topic": "Intramedullary Pinning Techniques",
        "Core_Anatomy": "Long bones (Medullary cavity).",
        "Pathogenesis_Immediate": "Intramedullary (IM) pinning can be done by either a Normograde or Retrograde pattern.",
        "Pathogenesis_Deep": "In Normograde pinning, the pin is introduced at the epiphysis/metaphysis of the bone (e.g., the trochanteric fossa of the femur) and driven down the marrow cavity across the fracture line. In Retrograde pinning, the pin is inserted directly into the medullary canal at the fracture site, driven UP through the proximal bone segment until it exits the skin, and then driven back DOWN across the fracture into the distal segment.",
        "Why_Not": "Retrograde pinning is faster but CANNOT be used in the tibia, because driving a pin proximally out of the tibia will destroy the crucial stifle joint (cruciate ligaments and meniscus).",
        "Wow_Approach": "For a fractured femur, retrograde pinning is standard. For a fractured tibia, strictly normograde pinning must be used."
    },
    3349: {
        "topic": "IM Pin Diameter Selection",
        "Core_Anatomy": "Diaphysis (Medullary cavity).",
        "Pathogenesis_Immediate": "The ideal intramedullary pin diameter should fill approximately 60-70% of the medullary cavity at the narrowest point of the diaphysis.",
        "Pathogenesis_Deep": "If the pin is too small (<60%), it will be mechanically weak and will bend or break under the animal's weight, or it will 'chatter' (move around) inside the bone, preventing healing. If the pin is too large (>70%), the surgeon risks cracking/splitting the cortex of the bone longitudinally while trying to hammer or drill the pin into the tight medullary canal.",
        "Why_Not": "An IM pin ONLY resists bending forces. It provides absolutely ZERO resistance to rotation or axial compression. Therefore, it must almost always be combined with a bone plate, external fixator, or cerclage wires.",
        "Wow_Approach": "N/A"
    },
    3350: {
        "topic": "Cortical vs Cancellous Screws",
        "Core_Anatomy": "Bone cortex (Diaphysis).",
        "Pathogenesis_Immediate": "Cortical screws are specifically designed for use in the diaphysis where Cortical bone predominates.",
        "Pathogenesis_Deep": "Cortical bone (the hard outer shell of the shaft) is very dense. Therefore, Cortical Screws have fine, closely spaced threads (smaller thread pitch) to maximize the number of threads gripping the hard, thin bone. Cancellous bone (the spongy bone at the metaphysis/epiphysis) is very soft. Cancellous Screws have very deep, widely spaced threads to grab as much of the soft, spongy bone as possible without stripping it out.",
        "Why_Not": "Using a cortical screw in soft cancellous bone will result in the screw instantly pulling out under tension.",
        "Wow_Approach": "N/A"
    },
    3351: {
        "topic": "Suture Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Monofilament, Multifilament, Flexible) belonging to a suture or wire question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3352: {
        "topic": "Interlocking Nail Sizes",
        "Core_Anatomy": "Long bones.",
        "Pathogenesis_Immediate": "Veterinary interlocking nails are typically available in 6mm and 8mm sizes for standard dogs.",
        "Pathogenesis_Deep": "An interlocking nail is an advanced IM pin that has holes drilled horizontally through it. Once the nail is in the medullary cavity, screws are driven through the bone cortex, through the holes in the nail, and out the other side. This incredibly strong construct resists ALL forces (bending, rotation, and compression) without needing an external plate. Standard sizes for dogs are 6mm and 8mm diameter nails.",
        "Why_Not": "N/A",
        "Wow_Approach": "Interlocking nails are mechanically superior to bone plates for severe comminuted fractures because they sit directly in the central mechanical axis of the bone (the marrow cavity), rather than off to the side like a plate."
    },
    3353: {
        "topic": "Complications of Internal Fixation",
        "Core_Anatomy": "Fracture site.",
        "Pathogenesis_Immediate": "Common complications of internal fixation (plates/pins) include Non-union, Mal-union, and Delayed union.",
        "Pathogenesis_Deep": "These are all failures of osteogenesis. Delayed union = healing takes longer than expected but is progressing. Mal-union = the bone heals, but in an abnormal, crooked alignment. Non-union = the healing process completely stops before the bone is united (often forming a false joint / pseudoarthrosis).",
        "Why_Not": "Non-unions are typically caused by either poor mechanics (too much motion breaking the new capillaries) or poor biology (infection or stripping away all the periosteal blood supply during surgery).",
        "Wow_Approach": "A 'hypertrophic' non-union looks like a massive elephant's foot on X-ray (lots of callus but it won't bridge the gap—needs better stabilization). An 'atrophic' non-union looks like a sharpened pencil (the bone is dead and resorbing—needs a bone graft)."
    },
    3354: {
        "topic": "Plaster of Paris - Water Temperature",
        "Core_Anatomy": "External coaptation.",
        "Pathogenesis_Immediate": "When activating Plaster of Paris bandages, the water temperature should be lukewarm (approx. 37°C or room temp).",
        "Pathogenesis_Deep": "The chemical reaction that hardens Plaster of Paris (calcium sulfate hemihydrate turning into a dihydrate) is highly exothermic (it releases intense heat). Using cold water slows the reaction down (giving you more time to mold the cast but producing less sudden heat). Using hot water drastically speeds up the reaction, locking the cast instantly and producing so much heat it can cause severe 3rd-degree burns to the patient's skin underneath the cast.",
        "Why_Not": "Boiling water (100°C) would melt the cast padding and severely burn the animal.",
        "Wow_Approach": "Modern veterinary medicine almost exclusively uses fiberglass casting tape instead of Plaster of Paris because fiberglass is infinitely lighter, waterproof, radiolucent, and sets faster."
    },
    3355: {
        "topic": "Tibia Plating Approach - Medial",
        "Core_Anatomy": "Tibia (Medial surface).",
        "Pathogenesis_Immediate": "The standard surgical approach for applying a bone plate to the tibia is Medial.",
        "Pathogenesis_Deep": "The medial aspect of the tibia has absolutely zero muscle coverage; the skin and subcutaneous tissue sit directly on the periosteum. This makes surgical exposure incredibly fast, easy, and bloodless. The bone plate sits flat directly on the medial cortex.",
        "Why_Not": "The lateral, cranial, and caudal aspects of the tibia are heavily covered by the large muscles of the lower leg (cranial tibial, long digital extensor, gastrocnemius). Attempting to plate these sides requires massive, traumatic muscle dissection.",
        "Wow_Approach": "Because the medial tibia has no muscle covering, a plate placed here lies directly under the skin. If the incision breaks down or gets infected, the metal plate is instantly exposed to the outside world, requiring plate removal."
    },
    3356: {
        "topic": "Indications for Bone Plate Removal",
        "Core_Anatomy": "Healed fracture site.",
        "Pathogenesis_Immediate": "Indications for removing a bone plate include Irritation, Infection, and Corrosion (or stress shielding).",
        "Pathogenesis_Deep": "Once a bone is fully healed, the plate is no longer needed. Usually, they are left in for life to avoid a second surgery. However, they MUST be removed if: (1) A biofilm infection develops on the metal (antibiotics cannot cure biofilm). (2) The screws loosen and back out, causing skin irritation/ulceration. (3) 'Stress Shielding' occurs (the stiff metal plate takes all the weight-bearing forces, causing the bone underneath it to weaken and resorb, risking a new fracture).",
        "Why_Not": "If the plate is quiet and the dog is asymptomatic, leave it alone.",
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
