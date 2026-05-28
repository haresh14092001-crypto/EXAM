import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3564: {
        "topic": "Closed Fracture (Review)",
        "Core_Anatomy": "Bone and overlying skin.",
        "Pathogenesis_Immediate": "A fracture with no breaks in the skin is a closed fracture.",
        "Pathogenesis_Deep": "Reiterating that the fracture hematoma remains sterile, vastly improving the prognosis compared to an open fracture.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3565: {
        "topic": "Complete Fracture (Review)",
        "Core_Anatomy": "Bone cortex.",
        "Pathogenesis_Immediate": "Total disruption of the bone is a complete fracture.",
        "Pathogenesis_Deep": "Reiterating that the fracture line traverses the entire circumference of the bone.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3566: {
        "topic": "Hip Dysplasia (Review)",
        "Core_Anatomy": "Coxofemoral joint.",
        "Pathogenesis_Immediate": "Abnormal development of the hip joint is Hip Dysplasia.",
        "Pathogenesis_Deep": "Reiterating the developmental laxity of the joint leading to osteoarthritis.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3567: {
        "topic": "IVDD Breeds (Review)",
        "Core_Anatomy": "Intervertebral disc.",
        "Pathogenesis_Immediate": "Intervertebral disc disease is most common in chondrodystrophic breeds like the Dachshund.",
        "Pathogenesis_Deep": "Reiterating the premature calcification and explosive rupture of the nucleus pulposus.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3568: {
        "topic": "Multiple Choice Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the start of the multiple choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3569: {
        "topic": "Hypertrophic Osteodystrophy Age (Review)",
        "Core_Anatomy": "Metaphysis.",
        "Pathogenesis_Immediate": "HOD is most common at 3-8 months of age.",
        "Pathogenesis_Deep": "Reiterating the window of explosive skeletal growth in giant breed dogs.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3570: {
        "topic": "Craniomandibular Osteopathy Breed (Review)",
        "Core_Anatomy": "Mandible.",
        "Pathogenesis_Immediate": "The Scottish Terrier is predisposed to CMO.",
        "Pathogenesis_Deep": "Reiterating the proliferative 'Lion Jaw' disease of young terriers.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3571: {
        "topic": "Bone Graft Harvesting (Review)",
        "Core_Anatomy": "Cancellous bone.",
        "Pathogenesis_Immediate": "A bone curette is used to harvest cancellous bone graft.",
        "Pathogenesis_Deep": "Reiterating that the spoon-like instrument scoops the bloody, osteoblast-rich marrow from the proximal humerus.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3572: {
        "topic": "IM Pinning Techniques (Review)",
        "Core_Anatomy": "Medullary cavity.",
        "Pathogenesis_Immediate": "IM pinning uses Normograde and Retrograde patterns.",
        "Pathogenesis_Deep": "Reiterating the directional methods of driving the pin.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3573: {
        "topic": "IM Pin Diameter (Review)",
        "Core_Anatomy": "Diaphysis.",
        "Pathogenesis_Immediate": "The ideal IM pin fills 60-70% of the medullary cavity.",
        "Pathogenesis_Deep": "Reiterating the balance between mechanical strength and the risk of splitting the cortex.",
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
