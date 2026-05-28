import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3461: {
        "topic": "Avulsion of Hoof (Exungulation)",
        "Core_Anatomy": "Equine/Bovine Hoof.",
        "Pathogenesis_Immediate": "The traumatic avulsion (tearing off) of the entire hoof capsule is called Exungulation.",
        "Pathogenesis_Deep": "This is a catastrophic traumatic injury where the entire keratinized hoof capsule is violently torn away from the underlying sensitive corium (often from getting the foot trapped in a fence or cattle guard while the animal struggles). The completely exposed corium bleeds profusely and is excruciatingly painful.",
        "Why_Not": "N/A",
        "Wow_Approach": "If the corium is relatively undamaged, a new hoof wall will eventually grow back from the coronary band, but it will take 9 to 12 months. During this entire time, the foot must be heavily bandaged and kept immaculately clean to prevent fatal osteomyelitis of the pedal bone."
    },
    3466: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting a short essay section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3473: {
        "topic": "Exam Instruction",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating a one-hour time limit.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3474: {
        "topic": "Objective Type Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of objective questions.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3475: {
        "topic": "Conformation Definition",
        "Core_Anatomy": "Skeletal and muscular system.",
        "Pathogenesis_Immediate": "The term that refers to the structure or outline of an animal as determined by the arrangement of its parts is Conformation.",
        "Pathogenesis_Deep": "In veterinary orthopaedics (especially equine), conformation is paramount. Poor conformation (e.g., base-narrow, sickle-hocked, or calf-kneed) drastically alters the biomechanical stress placed on bones and ligaments, directly predisposing the animal to specific traumatic injuries and osteoarthritis.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3483: {
        "topic": "True/False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a True or False section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3484: {
        "topic": "Interlocking Nails Biomechanics",
        "Core_Anatomy": "Long bones.",
        "Pathogenesis_Immediate": "The statement 'Interlocking nails cannot resist bending force' is FALSE.",
        "Pathogenesis_Deep": "Interlocking nails are the biomechanically strongest implants available for diaphyseal fractures. Because they are placed exactly in the neutral mechanical axis (the medullary cavity) AND locked with transverse screws, they perfectly resist ALL forces: bending, rotation, shear, and axial compression.",
        "Why_Not": "Standard smooth IM pins cannot resist rotation or compression, but INTERLOCKING nails resist everything.",
        "Wow_Approach": "N/A"
    },
    3499: {
        "topic": "Multiple Choice Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3500: {
        "topic": "Broken Down Horse",
        "Core_Anatomy": "Suspensory apparatus (Fetlock).",
        "Pathogenesis_Immediate": "A horse is said to be 'broken down' if there is a massive rupture of the suspensory apparatus or flexor tendons.",
        "Pathogenesis_Deep": "The term 'breakdown' is used on the racetrack to describe a catastrophic, career-ending (and often life-ending) musculoskeletal failure. The most common cause is the complete rupture of the Suspensory Ligament or the Superficial/Deep Digital Flexor Tendons. The fetlock completely loses its support and literally drops to the ground, touching the dirt when the horse bears weight.",
        "Why_Not": "A simple chip fracture or sprain does not cause the fetlock to drop to the floor. 'Broken down' implies catastrophic mechanical collapse.",
        "Wow_Approach": "If the blood supply to the distal limb is compromised during the breakdown, euthanasia is usually the only humane option on the track."
    },
    3501: {
        "topic": "Splints (Metacarpal Exostosis)",
        "Core_Anatomy": "Equine Metacarpals (Interosseous ligament).",
        "Pathogenesis_Immediate": "An exostosis between the cannon bone and the splint bones (or suspensory ligament) is called a Splint.",
        "Pathogenesis_Deep": "Splints are the tearing of the interosseous ligament that binds the small metacarpal bones (splint bones, MC2 and MC4) to the large cannon bone (MC3). Due to the tearing and bleeding, the periosteum is stimulated to form a massive lump of new bone (exostosis) to fuse the bones together. A 'Blind Splint' is an exostosis that grows INWARD, pressing on the suspensory ligament and causing severe lameness.",
        "Why_Not": "N/A",
        "Wow_Approach": "Once the splint bone completely fuses to the cannon bone (which takes a few months), the inflammation stops, the lameness disappears, and the remaining hard bony lump is just a permanent cosmetic blemish."
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
