import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    4100: {
        "topic": "Hydrocele",
        "Core_Anatomy": "Scrotum (Tunica Vaginalis).",
        "Pathogenesis_Immediate": "The pathological accumulation of serous fluid between the visceral and parietal layers of the tunica vaginalis is called a Hydrocele.",
        "Pathogenesis_Deep": "The tunica vaginalis is a peritoneal pouch surrounding the testis. Chronic trauma, localized infection, or lymphatic obstruction prevents normal fluid reabsorption, leading to progressive swelling of the scrotum with clear, sterile fluid.",
        "Why_Not": "Sarcocoele is a fleshy tumor of the testis. Cystocoele is herniation of the bladder.",
        "Wow_Approach": "Diagnosis is easily confirmed via transillumination—shining a bright light through the scrotum in a dark room will show a clear, glowing red fluid compartment, confirming it is not a solid tumor or hernia.",
        "Wow_Approach": "N/A"
    },
    4101: {
        "topic": "Vest-over-Pant Suture - Hernia (Review)",
        "Core_Anatomy": "Hernial ring fascia.",
        "Pathogenesis_Immediate": "The vest-over-pant (overlapping) suture is classically used in Hernia repairs.",
        "Pathogenesis_Deep": "Reiterating that this pattern overlaps two layers of tough fascial edges to provide a high-strength, double-thick closure of the hernial ring.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4102: {
        "topic": "Phimosis (Review)",
        "Core_Anatomy": "Preputial orifice.",
        "Pathogenesis_Immediate": "The inability of the penis to protrude from the sheath is called Phimosis.",
        "Pathogenesis_Deep": "Reiterating that this is caused by a congenitally narrow preputial orifice or post-traumatic scarring.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4103: {
        "topic": "Hysterocele",
        "Core_Anatomy": "Uterus.",
        "Pathogenesis_Immediate": "Herniation of the uterus is called a Hysterocele.",
        "Pathogenesis_Deep": "A hysterocele occurs when the uterus slips through a hernial ring, most commonly an inguinal hernia in pregnant or intact bitches, or a traumatic ventral hernia in large animals. In pregnant animals, this is a severe emergency as the expanding uterus can become strangulated.",
        "Why_Not": "Vesicocele or Cystocele refers strictly to the herniation of the urinary bladder.",
        "Wow_Approach": "N/A"
    },
    4104: {
        "topic": "Scoliosis",
        "Core_Anatomy": "Vertebral column.",
        "Pathogenesis_Immediate": "The abnormal lateral (sideward) curvature of the vertebral column is called Scoliosis.",
        "Pathogenesis_Deep": "It can be congenital (due to hemivertebrae) or acquired due to asymmetrical muscle spasms or trauma. It forces the spine into a C-shaped or S-shaped lateral deviation.",
        "Why_Not": "Kyphosis is an abnormal dorsal curvature (humpback). Lordosis is an abnormal ventral curvature (swayback). Torticollis is twisted neck.",
        "Wow_Approach": "N/A"
    },
    4105: {
        "topic": "Non-Union - Fracture (Review)",
        "Core_Anatomy": "Bone.",
        "Pathogenesis_Immediate": "Non-union is a major complication of Fractures.",
        "Pathogenesis_Deep": "Reiterating that severe instability or blood supply failure prevents bone bridging, leaving a permanent gap.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4106: {
        "topic": "Left Paracostal Incision - Reticulum",
        "Core_Anatomy": "Bovine Reticulum.",
        "Pathogenesis_Immediate": "A crescent-shaped paracostal incision on the left side in cattle is classically performed to approach the Reticulum.",
        "Pathogenesis_Deep": "For rumenotomy or diaphragmatic hernia repairs where direct access to the reticulum and reticular-diaphragmatic space is required, a left paracostal incision is placed parallel to the caudal edge of the last rib. This provides direct, immediate access to the reticular wall for surgical exploration.",
        "Why_Not": "A standard right flank laparotomy is used to approach the abomasum or intestines, not the reticulum.",
        "Wow_Approach": "N/A"
    },
    4107: {
        "topic": "Post-Xiphoid Mid-Ventral Incision - Gastrotomy",
        "Core_Anatomy": "Stomach (Cranial abdomen).",
        "Pathogenesis_Immediate": "A post-xiphoid mid-ventral laparotomy incision is classically used in small animals to perform a Gastrotomy.",
        "Pathogenesis_Deep": "The stomach lies in the far cranial aspect of the abdomen, tucked immediately behind the liver and ribs. To gain sufficient exposure for a gastrotomy, the midline incision must extend all the way cranially to the xiphoid cartilage. This provides excellent visualization of the gastric body and pylorus.",
        "Why_Not": "Cystotomy requires a caudal midline (pre-pubic) incision, the opposite end of the abdomen.",
        "Wow_Approach": "N/A"
    },
    4108: {
        "topic": "Radiography - Bone Lesions (Review)",
        "Core_Anatomy": "Skeletal tissue.",
        "Pathogenesis_Immediate": "The ideal diagnostic aid to detect bone lesions is Radiography.",
        "Pathogenesis_Deep": "Reiterating that X-rays provide unmatched contrast between mineralized bone, soft tissue, and air.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4109: {
        "topic": "Forelimb Lameness - Head Nod",
        "Core_Anatomy": "Cervical muscles and forelimbs.",
        "Pathogenesis_Immediate": "The statement 'In forelimb lameness, the head raises when the lame limb touches the ground' is TRUE.",
        "Pathogenesis_Deep": "This is the classic 'head nod' of equine lameness evaluation. To minimize the painful concussive force on the injured forelimb, the horse actively jerks its head and neck upward as the lame hoof lands, shifting its center of gravity backward. Conversely, when the sound limb lands, the horse drops its head down to bear normal weight.",
        "Why_Not": "For hindlimb lameness, the horse nods its head down when the lame limb lands, which is the exact opposite behavior.",
        "Wow_Approach": "Mnemonic: 'Down on sound'—the head drops when the sound forelimb lands."
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
