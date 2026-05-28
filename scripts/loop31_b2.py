import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3502: {
        "topic": "Corns (Equine Hoof)",
        "Core_Anatomy": "Equine Hoof (Angle of the sole).",
        "Pathogenesis_Immediate": "Contusion of the sensitive laminae specifically at the angle between the hoof wall and the bars is known as a Corn.",
        "Pathogenesis_Deep": "A corn is a localized bruise (hematoma) in the corium of the sole, almost always occurring at the 'seat of corn' (the palmar/plantar angle of the hoof, usually on the medial side of the forelimb). It is caused by improper shoeing where the shoe is left on too long, causing the heel of the shoe to aggressively dig into and crush the sole.",
        "Why_Not": "A bruised sole can happen anywhere. A 'Corn' is strictly defined by its anatomical location in the angle between the wall and the bars.",
        "Wow_Approach": "To treat a corn, the shoe must be removed, the bruised horn pared out with a hoof knife to relieve the pressure, and a bar shoe applied to transfer weight off the heels."
    },
    3503: {
        "topic": "Dropped Sole - Laminitis",
        "Core_Anatomy": "Equine hoof (Sole and P3).",
        "Pathogenesis_Immediate": "A 'Dropped Sole' is the classic pathognomonic symptom noticed in severe or Chronic Laminitis.",
        "Pathogenesis_Deep": "As the deep digital flexor tendon pulls the inflamed coffin bone (P3) downward and backward, the sharp distal tip of P3 presses directly against the horny sole from the inside out. The normally concave sole is pushed downward until it becomes completely flat or even convex (dropped). In extreme cases, the bone pierces right through the sole.",
        "Why_Not": "Navicular disease causes heel pain, not sole dropping. Acute laminitis has pain but no physical dropping of the sole yet.",
        "Wow_Approach": "Once the sole drops, the horse's prognosis for ever returning to athletic function is extremely poor."
    },
    3504: {
        "topic": "Seedy Toe (Review)",
        "Core_Anatomy": "Hoof wall (White line).",
        "Pathogenesis_Immediate": "Separation between the wall and the laminae of the hoof is seen in Seedy toe.",
        "Pathogenesis_Deep": "Reiterating the crumbly, hollow deterioration of the white line at the toe.",
        "Why_Not": "Sandcrack is a vertical fissure of the outer wall, not a separation of the inner layers.",
        "Wow_Approach": "N/A"
    },
    3505: {
        "topic": "Spinal Deformity Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Lordosis, Scoliosis, Kyphosis, Torticollis) for a spinal deformity question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3506: {
        "topic": "Hindlimb Lameness Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Gonitis, Calcaneal bursitis, Upward fixation of patella, Curb) for a stifle/hock question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3508: {
        "topic": "Bone Plate Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Compression, Buttress, Neutralization) for a bone plate function question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3509: {
        "topic": "Dishing (Equine Gait)",
        "Core_Anatomy": "Equine Forelimbs.",
        "Pathogenesis_Immediate": "Throwing the feet inward while in motion is called Dishing.",
        "Pathogenesis_Deep": "Dishing is a gait abnormality typical of horses with a 'base-wide' or 'toes-out' (splay-footed) conformation. As they bring their foreleg forward, it swings in an inward arc before landing. This wastes energy and reduces speed.",
        "Why_Not": "Paddling is throwing the feet OUTWARD (seen in pigeon-toed horses). Plaiting is rope-walking (one foot in front of the other). Interference is when one hoof physically strikes the opposite leg.",
        "Wow_Approach": "N/A"
    },
    3510: {
        "topic": "Sweeny - Suprascapular Paralysis",
        "Core_Anatomy": "Scapula and Shoulder joint.",
        "Pathogenesis_Immediate": "Sweeny is the severe, rapid atrophy (myopathy) of the supraspinatus and infraspinatus muscles in the horse.",
        "Pathogenesis_Deep": "It is caused by traumatic damage to the Suprascapular nerve. This nerve wraps tightly around the cranial edge of the scapula, making it highly vulnerable to being crushed by a kick or from slamming into a rigid object (like a door frame or draft harness). Because the nerve is crushed, the muscles it supplies instantly lose their tone and rapidly waste away. The spine of the scapula becomes extremely prominent.",
        "Why_Not": "Radial nerve paralysis causes a dropped elbow, not shoulder muscle atrophy.",
        "Wow_Approach": "Because the supraspinatus and infraspinatus act as the primary collateral ligaments of the equine shoulder joint, a horse with severe Sweeny will show a very characteristic lateral 'popping out' (subluxation) of the shoulder joint every time it bears weight on the leg."
    },
    3511: {
        "topic": "Complicated Fracture",
        "Core_Anatomy": "Bone and adjacent organs.",
        "Pathogenesis_Immediate": "A fracture accompanied by the opening of a joint cavity, injury to major vessels/nerves, or damage to a visceral cavity is termed a Complicated fracture.",
        "Pathogenesis_Deep": "A simple/closed fracture involves only the bone. A compound/open fracture breaks the skin. A Complicated fracture means the sharp bone fragments have physically pierced and destroyed an adjacent critical structure. Examples: a fractured rib puncturing the lungs (causing pneumothorax), or a fractured pelvis tearing the urethra.",
        "Why_Not": "A comminuted fracture means many pieces, but does not inherently imply visceral damage.",
        "Wow_Approach": "N/A"
    },
    3512: {
        "topic": "Ringbone Radiography",
        "Core_Anatomy": "Pastern and Coffin joints.",
        "Pathogenesis_Immediate": "The primary radiographic signs of Ringbone are osteophyte formation and periosteal bony proliferation around the pastern.",
        "Pathogenesis_Deep": "Ringbone is osteoarthritis of the interphalangeal joints (High Ringbone = pastern joint; Low Ringbone = coffin joint). On an X-ray, you will see massive, irregular white spikes of new bone (osteophytes/exostoses) attempting to bridge and fuse the degenerating joint.",
        "Why_Not": "Collapse of the joint space is also seen in advanced osteoarthritis, but the hallmark of 'ring' bone is the bony proliferation forming a ring around the pastern.",
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
