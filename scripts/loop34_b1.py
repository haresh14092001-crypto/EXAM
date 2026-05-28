import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3816: {
        "topic": "Segmental Fracture",
        "Core_Anatomy": "Diaphysis of long bones.",
        "Pathogenesis_Immediate": "A Segmental fracture is a type of complete fracture where a middle piece of the bone shaft is completely isolated by two distinct fracture lines.",
        "Pathogenesis_Deep": "This is a severe, high-energy injury. Because there are two separate fracture lines, the blood supply to the central, free-floating bone segment (segmental piece) is severely compromised. This leads to a very high rate of delayed union, non-union, or bone necrosis, requiring highly stable internal fixation (like locking plates) to protect the biology.",
        "Why_Not": "A comminuted fracture involves multiple small, splintered fragments. A segmental fracture specifically leaves one large, intact, isolated central segment of bone.",
        "Wow_Approach": "N/A"
    },
    3817: {
        "topic": "Cauda Equina Syndrome",
        "Core_Anatomy": "Lumbosacral Junction (L7-S1).",
        "Pathogenesis_Immediate": "Cauda Equina Syndrome (Degenerative Lumbosacral Stenosis) is caused by the compression of the lumbosacral nerve roots caudal to the termination of the spinal cord.",
        "Pathogenesis_Deep": "In large breed dogs (like German Shepherds), chronic instability or disc protrusion at L7-S1 compresses the bundle of nerve roots (the cauda equina or 'horse's tail'). This leads to severe pain when the tail is lifted, pelvic limb weakness, urinary/fecal incontinence, and a classic 'low tail carriage'.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3819: {
        "topic": "Distraction Fracture",
        "Core_Anatomy": "Bone and opposing muscle groups.",
        "Pathogenesis_Immediate": "A Distraction fracture occurs when the bone fragments are pulled directly away from each other by massive muscular or ligamentous tension.",
        "Pathogenesis_Deep": "Unlike compression fractures (where bones are crushed together), distraction fractures pull the bone ends apart. The classic example is a transverse patellar fracture or olecranon fracture where the quadriceps/triceps pull the broken fragment proximally. Healing is impossible without surgery because the bone ends cannot touch.",
        "Why_Not": "A compression fracture involves bone ends being pushed into each other.",
        "Wow_Approach": "N/A"
    },
    3833: {
        "topic": "VSR III Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology Paper III.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3834: {
        "topic": "VSR III Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology Paper III.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3835: {
        "topic": "Exam Instruction (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating a thirty-minute time limit for Part-A.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3836: {
        "topic": "Objective Type Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of an objective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3837: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3856: {
        "topic": "Suspensory Ligament Rupture - Spay",
        "Core_Anatomy": "Ovarian Suspensory Ligament.",
        "Pathogenesis_Immediate": "Manual rupture of the ovarian suspensory ligament is a standard, essential surgical step during canine/feline Ovariohysterectomy (spay) to exteriorize the ovary.",
        "Pathogenesis_Deep": "The ovary is bound tightly to the dorsal body wall (near the caudal kidney pole) by the tough, fibrous suspensory ligament. To safely ligate the ovarian pedicle without tearing the delicate ovarian vessels, the surgeon must gain access and visibility. This is accomplished by sliding an index finger along the ligament and applying caudomedial traction to manually snap (rupture) the ligament close to its origin on the body wall.",
        "Why_Not": "This is NOT an accidental complication; it is a deliberate, highly beneficial maneuver. Tearing the ovarian PEDICLE (blood vessels) is the actual dangerous complication.",
        "Wow_Approach": "Snapping the ligament is done blindly by feel, and the surgeon will feel a characteristic, highly satisfying physical 'give' or 'pop' when the ligament ruptures, allowing the ovary to easily lift out of the abdomen."
    },
    3857: {
        "topic": "IM Pinning Patterns (Review)",
        "Core_Anatomy": "Medullary cavity.",
        "Pathogenesis_Immediate": "IM pinning uses Normograde and Retrograde patterns.",
        "Pathogenesis_Deep": "Reiterating the two directional insertion methods for intramedullary pins.",
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
