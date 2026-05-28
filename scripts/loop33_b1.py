import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3688: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of a short notes section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3705: {
        "topic": "Objective Type Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the objective question section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3706: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3719: {
        "topic": "Choose the Best Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3720: {
        "topic": "Splints Anatomy - MC2 and MC3",
        "Core_Anatomy": "Equine Metacarpus (MC2, MC3, MC4).",
        "Pathogenesis_Immediate": "Splint in the horse most commonly occurs between the 2nd and 3rd metacarpus (MC2 and MC3).",
        "Pathogenesis_Deep": "The medial splint bone (MC2) bears significantly more weight than the lateral splint bone (MC4) due to the anatomy of the carpal bones (the trapezoid sits directly on MC2). Consequently, the interosseous ligament between MC2 and the large cannon bone (MC3) is subjected to much greater strain and shearing forces, making medial splints (between MC2 and MC3) extremely common in young horses, while lateral splints (between MC3 and MC4) are rare.",
        "Why_Not": "MC1 does not exist in the horse. MC3 and MC4 represent the lateral side, which bears much less concussive force.",
        "Wow_Approach": "N/A"
    },
    3721: {
        "topic": "Bunny Hopping Gait - Hip Dysplasia",
        "Core_Anatomy": "Coxofemoral joints and Hindlimbs.",
        "Pathogenesis_Immediate": "A 'Bunny Hopping' gait in young, growing dogs is highly characteristic of Hip Dysplasia.",
        "Pathogenesis_Deep": "When a puppy has severe hip joint laxity (hip dysplasia), bearing weight unilaterally on a single hip during a normal trot is highly painful and unstable. To bypass this, the puppy will move both hind legs forward together at the same time (mimicking the hopping motion of a rabbit) when running. This allows them to distribute their weight evenly across the pelvis, minimizing joint shearing.",
        "Why_Not": "Cruciate rupture causes a unilateral non-weight bearing lameness. Patellar luxation causes a classic skipping gait (holding the leg up for a few steps then extending it), not bilateral hopping.",
        "Wow_Approach": "If a giant breed puppy (like a Golden Retriever or Mastiff) trotts with a cute 'bunny hop', it is NOT normal or cute; it is a clinical red flag for early, severe hip dysplasia."
    },
    3722: {
        "topic": "Laminitis in Cattle - Acidosis",
        "Core_Anatomy": "Bovine Hoof (Corium).",
        "Pathogenesis_Immediate": "A major cause of laminitis in cattle is Ruminitis / Lactic Acidosis (often due to high grain intake).",
        "Pathogenesis_Deep": "Ingestion of excessive concentrates (easily fermentable carbohydrates) causes a massive explosion of Streptococcus bovis in the rumen. These bacteria produce lactic acid, dropping the rumen pH below 5.0 (rumen acidosis). This acidic environment kills the normal gram-negative bacteria, releasing massive amounts of endotoxins and vasoactive histamines into the circulation. These toxins travel to the hoof corium, causing severe vasospasm, thrombosis, and swelling of the sensitive laminae.",
        "Why_Not": "Spinal deformities (lordosis/kyphosis) have absolutely no metabolic link to hoof laminae.",
        "Wow_Approach": "N/A"
    },
    3723: {
        "topic": "Paraplegia Definition",
        "Core_Anatomy": "Spinal Cord (Thoracolumbar).",
        "Pathogenesis_Immediate": "Paraplegia is the complete paralysis of the hindquarters (both hind limbs).",
        "Pathogenesis_Deep": "It is caused by a severe lesion in the spinal cord caudal to the T2 vertebra (e.g., Hansen Type I IVDD or spinal trauma). The sensory and motor signals are completely cut off from the caudal half of the body.",
        "Why_Not": "Hemiplegia is paralysis of one side of the body. Tetraplegia/Quadriplegia is paralysis of all four limbs (cervical lesion). Monoplegia is one limb.",
        "Wow_Approach": "N/A"
    },
    3724: {
        "topic": "Calving Paralysis - Sciatic/Obturator",
        "Core_Anatomy": "Sciatic and Obturator nerves.",
        "Pathogenesis_Immediate": "Caudal paresis or paralysis associated with calving is typically caused by damage to the Obturator nerve or the Sciatic nerve.",
        "Pathogenesis_Deep": "As reviewed, both nerves run close to the bony walls of the pelvic canal. In prolonged dystocia, the fetus crushes the obturator nerve (adductor failure) and/or the sciatic nerve (femoral extensor failure, leading to a dropped hock and knuckling).",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3725: {
        "topic": "Bone Development Regions Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Diaphysis, Epiphyseal, Metaphysis, Apophysis) for a bone growth or anatomy question.",
        "Pathogenesis_Deep": "Structural artifact.",
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
