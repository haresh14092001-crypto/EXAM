import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3650: {
        "topic": "Urethral Calculi Site - Cattle",
        "Core_Anatomy": "Bovine Urethra (Sigmoid flexure).",
        "Pathogenesis_Immediate": "The most common site of urethral calculi obstruction in cattle is the distal aspect of the Sigmoid Flexure.",
        "Pathogenesis_Deep": "Unlike small ruminants (where stones lodge in the tiny urethral process), bovine stones typically lodge just proximal to the insertion of the retractor penis muscle at the distal curve of the sigmoid flexure. At this exact point, the urethra becomes extremely narrow and the fibrous tunica albuginea prevents the tissue from expanding to let the stone pass.",
        "Why_Not": "The ischial urethra is very wide. The os penis is found in dogs, not cattle.",
        "Wow_Approach": "To relieve the obstruction in a steer, a perineal urethrostomy is performed to bypass the sigmoid flexure entirely, allowing the animal to survive until slaughter weight."
    },
    3651: {
        "topic": "Sweeny (Review)",
        "Core_Anatomy": "Scapula.",
        "Pathogenesis_Immediate": "Sweeny is characterized by the severe atrophy of the Supraspinatus and Infraspinatus muscles.",
        "Pathogenesis_Deep": "Reiterating that this is caused by traumatic damage to the suprascapular nerve.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3652: {
        "topic": "Obturator Nerve Paralysis",
        "Core_Anatomy": "Pelvis and Hindlimb Adductors.",
        "Pathogenesis_Immediate": "Obturator nerve paralysis is most commonly caused by prolonged Dystocia (difficult birth) in cattle.",
        "Pathogenesis_Deep": "The obturator nerve runs along the medial shaft of the ilium inside the pelvic canal. When a cow tries to deliver a massively oversized calf (fetal macrosomia), the calf's hips become wedged in the birth canal. The immense pressure physically crushes the mother's obturator nerve against her own pelvic bones. Because the obturator nerve supplies the adductor muscles of the hindlimbs, the cow cannot pull her legs together. When she tries to stand, her legs uncontrollably splay outward, often causing her to permanently dislocate her hips or tear her gracilis muscles.",
        "Why_Not": "Pelvic fractures can cause it, but dystocia is overwhelmingly the most common cause of the 'calving paralysis' syndrome.",
        "Wow_Approach": "To prevent the cow from doing the 'splits' and tearing her muscles while recovering, her hind fetlocks must be hobbled (tied together) with a soft rope, leaving about 18 inches of slack."
    },
    3653: {
        "topic": "Splayed Foot Conformation",
        "Core_Anatomy": "Distal limb conformation.",
        "Pathogenesis_Immediate": "A 'Splayed foot' refers to a conformation where the toes point outward ('Toe out').",
        "Pathogenesis_Deep": "This is a base-wide, 'toes-out' conformation. Because the weight is not distributed evenly across the hoof, it places extreme asymmetric stress on the medial collateral ligaments and the medial aspect of the joints, heavily predisposing the animal to early osteoarthritis and the 'dishing' gait.",
        "Why_Not": "Pigeon toe is 'toe in'.",
        "Wow_Approach": "N/A"
    },
    3655: {
        "topic": "Equine Pathology Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Spavin, Thoroughpin, Navicular disease, Canker) for an equine lameness question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3656: {
        "topic": "Equine Dentistry - Floating",
        "Core_Anatomy": "Equine Teeth (Premolars/Molars).",
        "Pathogenesis_Immediate": "The surgical procedure of 'Floating' is used exclusively for the Tooth.",
        "Pathogenesis_Deep": "Because horses chew in a figure-8 motion and their upper jaw is wider than their lower jaw, their continuously erupting cheek teeth wear unevenly. Over time, razor-sharp enamel points develop on the buccal (cheek) edge of the upper teeth and the lingual (tongue) edge of the lower teeth. These points cause severe oral ulceration, preventing the horse from chewing properly (quidding). 'Floating' involves using a specialized rasp (float) to manually file down these sharp points.",
        "Why_Not": "You trim hooves and dehorn cattle, but you FLOAT teeth.",
        "Wow_Approach": "Modern equine dentistry utilizes motorized diamond-burr floats with water cooling, which are vastly faster and more precise than traditional manual rasps."
    },
    3657: {
        "topic": "Coxofemoral Luxation - Cranio-dorsal",
        "Core_Anatomy": "Coxofemoral joint.",
        "Pathogenesis_Immediate": "The most common direction for hip dislocation (luxation) in domestic animals is Cranio-Dorsal.",
        "Pathogenesis_Deep": "When severe trauma (like a car accident or a slip on concrete) ruptures the ligament of the head of the femur, the massive gluteal muscles instantly spasm. The force of these muscles pulls the free femoral head forward (cranially) and upward (dorsally) out of the acetabulum, lodging it on the dorsal rim of the pelvis. The affected leg will appear noticeably shorter than the normal leg.",
        "Why_Not": "Ventral luxations are rare because the animal's weight normally pushes the femur upward.",
        "Wow_Approach": "N/A"
    },
    3658: {
        "topic": "Interdigital Pododermatitis (Foot Rot)",
        "Core_Anatomy": "Bovine Hoof (Interdigital space).",
        "Pathogenesis_Immediate": "Interdigital pododermatitis is the medical term for Foot Rot.",
        "Pathogenesis_Deep": "It is an acute, highly contagious, necrotizing bacterial infection (primarily caused by Fusobacterium necrophorum and Dichelobacter nodosus) that invades the skin between the claws. The hallmark sign is a foul-smelling, necrotic fissure in the interdigital space causing severe, acute lameness and swelling of the coronary band.",
        "Why_Not": "A corn is a non-infectious bruise. A wart (Hairy Heel Wart) is caused by Treponema spirochetes.",
        "Wow_Approach": "Unlike deep abscesses, Foot Rot is extremely responsive to systemic antibiotics (like long-acting Oxytetracycline) because the bacteria are highly susceptible and the tissue is still vascularized."
    },
    3659: {
        "topic": "Degenerative Myelopathy",
        "Core_Anatomy": "Spinal Cord (Thoracolumbar white matter).",
        "Pathogenesis_Immediate": "Degenerative myelopathy (DM) is classically most common in older German Shepherd Dogs.",
        "Pathogenesis_Deep": "DM is a genetic, progressive neurodegenerative disease similar to ALS (Lou Gehrig's disease) in humans. It causes the slow, painless demyelination and axonal loss of the white matter tracts in the spinal cord. It begins as mild hindlimb ataxia and dragging of the toes, and over 6-12 months, progresses to complete paraplegia and eventually forelimb paralysis.",
        "Why_Not": "Pugs get Pug Dog Encephalitis. Dobermans get Cervical Spondylomyelopathy (Wobblers).",
        "Wow_Approach": "Because it is completely painless, the primary differential is IVDD (which is excruciatingly painful). There is no cure for DM."
    },
    3660: {
        "topic": "Intervertebral Disc Anatomy",
        "Core_Anatomy": "Vertebral column.",
        "Pathogenesis_Immediate": "Intervertebral disks are located between the vertebral bodies starting at C2-C3 and ending at L7-S1.",
        "Pathogenesis_Deep": "There is anatomically NO intervertebral disc between the skull and C1 (the atlanto-occipital joint) or between C1 and C2 (the atlanto-axial joint). These are specialized synovial joints that allow the head to nod ('yes') and rotate ('no'). The very first intervertebral disc in the entire body is located between the Axis (C2) and the third cervical vertebra (C3).",
        "Why_Not": "Any option claiming a disc exists at C1-C2 is anatomically impossible.",
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
