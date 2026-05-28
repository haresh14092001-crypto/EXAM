import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    4088: {
        "topic": "Skyline View (Review)",
        "Core_Anatomy": "Stifle (Femoropatellar joint).",
        "Pathogenesis_Immediate": "The Skyline (tangential) radiographic view is used to diagnose Patellar Luxation.",
        "Pathogenesis_Deep": "Reiterating that this view allows direct visualization of the trochlear groove depth and patellar positioning.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4089: {
        "topic": "P3 Rotation - Chronic Laminitis (Review)",
        "Core_Anatomy": "Hoof laminae and P3.",
        "Pathogenesis_Immediate": "Rotation of the third phalanx (coffin bone) is seen in Chronic Laminitis.",
        "Pathogenesis_Deep": "Reiterating that the necrotic laminae fail to resist the upward pull of the deep digital flexor tendon, rotating the tip of P3 ventrally.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4091: {
        "topic": "Robert Jones Bandage Sites",
        "Core_Anatomy": "Distal limbs.",
        "Pathogenesis_Immediate": "A Robert Jones Bandage is strictly indicated for temporary stabilization of Distal fore/hind limb fractures.",
        "Pathogenesis_Deep": "The Robert Jones is a heavily padded cotton bandage that relies on extreme bulk and compression to temporarily immobilize fractures below the elbow or stifle. It cannot be used for proximal fractures (e.g., humerus or femur) because it is impossible to secure the bandage high enough on the shoulder or hip, and the heavy weight would act as a pendulum, worsening fracture displacement.",
        "Why_Not": "Proximal limb fractures require a Spica splint or immediate internal fixation.",
        "Wow_Approach": "N/A"
    },
    4092: {
        "topic": "Hansen Type I IVDD - Dachshund (Review)",
        "Core_Anatomy": "Intervertebral Disc.",
        "Pathogenesis_Immediate": "Hansen Type I IVDD is overwhelmingly most common in Chondrodystrophic breeds, classically the Dachshund.",
        "Pathogenesis_Deep": "Reiterating the rapid calcification and explosive extrusion of the nucleus pulposus through the annulus fibrosus into the spinal cord.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4093: {
        "topic": "Ringbone - Forefeet Prevalence",
        "Core_Anatomy": "Equine Forelimb digits.",
        "Pathogenesis_Immediate": "Ringbone (interphalangeal osteoarthritis) is significantly more common in the Forefeet.",
        "Pathogenesis_Deep": "The equine forelimbs bear 60-65% of the horse's total body weight. Furthermore, they act as the primary shock-absorbers during a gallop, taking intense concussive forces directly through the vertical bony axis of the digit, while the hindlimbs are angled and serve primarily for propulsion. This extreme, repetitive concussion makes joint degeneration (ringbone) far more common in the forefeet.",
        "Why_Not": "The hip and stifle are proximal joint structures, not phalangeal.",
        "Wow_Approach": "N/A"
    },
    4095: {
        "topic": "Chondrodystrophic Breeds Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Spitz, Dachshund, Pug, Great Dane) for a breed predisposition question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4096: {
        "topic": "Desmotomy Definition",
        "Core_Anatomy": "Ligament.",
        "Pathogenesis_Immediate": "Surgical severing of a ligament is called a Desmotomy.",
        "Pathogenesis_Deep": "For example, a Medial Patellar Desmotomy involves cutting the medial patellar ligament to relieve upward patellar fixation in cattle. A tenotomy is cutting a tendon (e.g., deep digital flexor tenectomy).",
        "Why_Not": "Myotomy is cutting muscle. Osteotomy is cutting bone.",
        "Wow_Approach": "N/A"
    },
    4097: {
        "topic": "Flat Foot - Equine Hoof",
        "Core_Anatomy": "Equine Hoof (Sole).",
        "Pathogenesis_Immediate": "An equine hoof that lacks the normal protective concavity of the sole is called a Flat Foot.",
        "Pathogenesis_Deep": "Normally, the sole of the horse's hoof is concave (arched upward) so that it does not bear direct weight on hard ground, which protects the sensitive sole corium. In a flat foot, the sole sits flat or even bulges downward. This leads to constant bruising of the sole corium, severe lameness, and high susceptibility to solar abscesses.",
        "Why_Not": "A club foot is an abnormally upright hoof with a high heel, often due to flexor contracture.",
        "Wow_Approach": "N/A"
    },
    4098: {
        "topic": "Teat Ring Block",
        "Core_Anatomy": "Bovine Teat.",
        "Pathogenesis_Immediate": "The 'Ring Block' regional anesthesia technique is classically related to Teat Surgery.",
        "Pathogenesis_Deep": "To perform surgery on the highly sensitive bovine teat (like repairing a teat laceration or fistula), a ring block is applied. Local anesthetic (like Lidocaine) is injected subcutaneously in a continuous ring entirely around the base of the teat. This blocks the dorsal and ventral teat nerves as they travel down from the udder skin, providing complete surgical analgesia of the entire teat.",
        "Why_Not": "Rumenotomy requires an inverted-L block or paravertebral block, not a circular ring block.",
        "Wow_Approach": "N/A"
    },
    4099: {
        "topic": "Teat Surgery Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Udder fistula, Enterotomy) for a surgery block question.",
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
