import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3400: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3401: {
        "topic": "Gonitis (Review)",
        "Core_Anatomy": "Stifle joint.",
        "Pathogenesis_Immediate": "Inflammation of the stifle joint is Gonitis.",
        "Pathogenesis_Deep": "Reiterating that this applies to both acute and chronic inflammation of the largest joint in the hindlimb.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3402: {
        "topic": "Achilles Tendon Rupture (Review)",
        "Core_Anatomy": "Hock (Tuber calcanei).",
        "Pathogenesis_Immediate": "Rupture of the tendo-achillis causes a dropped hock (plantigrade stance).",
        "Pathogenesis_Deep": "Loss of the common calcanean tendon prevents the animal from keeping the hock extended under weight-bearing.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3403: {
        "topic": "Ossifying Myopathy (Review)",
        "Core_Anatomy": "Skeletal muscle.",
        "Pathogenesis_Immediate": "Ossifying myopathy results from chronic trauma to the muscle belly.",
        "Pathogenesis_Deep": "Reiterating the process of fibrotic healing undergoing dystrophic calcification.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3404: {
        "topic": "Chondromalacia Patellae (Review)",
        "Core_Anatomy": "Patella.",
        "Pathogenesis_Immediate": "Degenerative softening of the articular cartilage of the patella is Chondromalacia.",
        "Pathogenesis_Deep": "Usually secondary to patellar luxation or poor trochlear groove tracking.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3405: {
        "topic": "Thoroughpin (Review)",
        "Core_Anatomy": "Tarsal sheath.",
        "Pathogenesis_Immediate": "Distension of the tarsal sheath is called Thoroughpin.",
        "Pathogenesis_Deep": "A fluctuant swelling of the DDFT sheath just cranial to the point of the hock.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3408: {
        "topic": "Ulcerative Sole - Rusterholz Ulcer",
        "Core_Anatomy": "Bovine Hoof (Sole-bulb junction).",
        "Pathogenesis_Immediate": "A specific ulcerative sole condition commonly noticed in cattle is the Rusterholz Ulcer (Pododermatitis circumscripta).",
        "Pathogenesis_Deep": "This is a highly specific, focal area of necrosis and ulceration that occurs exactly at the junction of the sole and the heel bulb, almost exclusively on the lateral claw of the hindlimb. Due to the biomechanics of dairy cattle standing on hard concrete, maximum weight-bearing force is concentrated on this exact spot. The corium gets crushed between the pedal bone and the concrete, losing its blood supply, necrotizing, and forming a deep hole.",
        "Why_Not": "White line disease occurs at the junction of the wall and sole. A Rusterholz ulcer is strictly at the sole-bulb junction.",
        "Wow_Approach": "Treatment requires placing a wooden or plastic block on the HEALTHY (medial) claw. This instantly elevates the diseased lateral claw off the ground, removing all pressure and allowing the ulcer to heal."
    },
    3415: {
        "topic": "Closed Fracture (Simple Fracture)",
        "Core_Anatomy": "Bone and overlying skin.",
        "Pathogenesis_Immediate": "A fracture with no breaks in the overlying skin is called a Closed (or Simple) fracture.",
        "Pathogenesis_Deep": "Because the skin barrier remains intact, the fracture hematoma is sterile. The bone can heal normally without the massive complication of environmental bacterial contamination.",
        "Why_Not": "An Open (or Compound) fracture involves a bone spike piercing the skin from the inside out, or a projectile piercing the skin from the outside in. Open fractures are an immediate surgical emergency due to bone infection (osteomyelitis).",
        "Wow_Approach": "Even if a fracture is closed, if the soft tissue envelope is severely crushed (e.g., hit by a car), the skin may slough and die 3-5 days later, converting a closed fracture into an open one."
    },
    3416: {
        "topic": "Complete Fracture (Review)",
        "Core_Anatomy": "Bone cortex.",
        "Pathogenesis_Immediate": "Total disruption of the bone is a Complete fracture.",
        "Pathogenesis_Deep": "Reiterating that the fracture line completely traverses the cortex on all sides.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3417: {
        "topic": "Hip Dysplasia (Review)",
        "Core_Anatomy": "Coxofemoral joint.",
        "Pathogenesis_Immediate": "Abnormal development of the hip joint is Hip Dysplasia.",
        "Pathogenesis_Deep": "Reiterating the developmental laxity of the joint leading to osteoarthritis in large breed dogs.",
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
