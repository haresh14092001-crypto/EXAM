import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3593: {
        "topic": "Wind Puff (Review)",
        "Core_Anatomy": "Fetlock (Digital flexor tendon sheath).",
        "Pathogenesis_Immediate": "A Wind Puff is the distension of the digital flexor tendon sheath.",
        "Pathogenesis_Deep": "Reiterating that this is a non-painful, cosmetic idiopathic tenosynovitis.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3594: {
        "topic": "Septic Arthritis (Review)",
        "Core_Anatomy": "Synovial joints.",
        "Pathogenesis_Immediate": "Septic arthritis is the acute bacterial infection of a joint.",
        "Pathogenesis_Deep": "Reiterating the severe, rapid enzymatic destruction of articular cartilage.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3597: {
        "topic": "Chronic Laminitis (Review)",
        "Core_Anatomy": "Hoof (Pedal bone).",
        "Pathogenesis_Immediate": "Chronic laminitis involves the rotation or sinking of the pedal bone.",
        "Pathogenesis_Deep": "Reiterating the mechanical failure of the sensitive laminae.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3599: {
        "topic": "Seedy Toe (Review)",
        "Core_Anatomy": "Hoof wall (White line).",
        "Pathogenesis_Immediate": "Seedy toe is the separation of the hoof wall at the white line.",
        "Pathogenesis_Deep": "Reiterating the crumbly, anaerobic infection of the inner stratum medium.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3604: {
        "topic": "Myositis (Review)",
        "Core_Anatomy": "Skeletal muscle.",
        "Pathogenesis_Immediate": "Myositis is the inflammation of muscle tissue.",
        "Pathogenesis_Deep": "Reiterating its causes including severe exertion, immune-mediated diseases, or infections.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3607: {
        "topic": "Drawer Sign - Cranial Cruciate Ligament Rupture",
        "Core_Anatomy": "Stifle joint.",
        "Pathogenesis_Immediate": "The 'Drawer Sign' (Cranial Drawer Test) is the pathognomonic physical exam finding for a Cranial Cruciate Ligament (CCL) rupture.",
        "Pathogenesis_Deep": "The CCL prevents the tibia from sliding forward relative to the femur when the animal bears weight. If the CCL is completely torn, the examiner can physically grab the tibia and pull it cranially, sliding it back and forth exactly like opening and closing a desk drawer. This instability causes immediate, severe osteoarthritis and secondary tearing of the medial meniscus.",
        "Why_Not": "A positive drawer sign guarantees a CCL rupture; however, a negative drawer sign in a very large, tense, or heavily muscled dog does not rule it out. In those cases, a 'Tibial Compression Test' (or eliciting the drawer sign under deep sedation) is required.",
        "Wow_Approach": "Surgical repair (like a TPLO - Tibial Plateau Leveling Osteotomy) does not repair the torn ligament. Instead, it alters the biomechanical geometry of the tibia so that the dog no longer NEEDS a cranial cruciate ligament to bear weight stably."
    },
    3609: {
        "topic": "Avulsion Fracture (Review)",
        "Core_Anatomy": "Bone (Apophysis).",
        "Pathogenesis_Immediate": "An Avulsion fracture occurs when a piece of bone is torn away by a tendon or ligament.",
        "Pathogenesis_Deep": "Reiterating that tendons/ligaments are stronger than bone, resulting in the apophysis ripping off during explosive trauma.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3622: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3624: {
        "topic": "Objective Type Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of an objective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3625: {
        "topic": "Appropriate Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
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
print(f"Batch 2/5 DONE: Updated {updated} questions.")
