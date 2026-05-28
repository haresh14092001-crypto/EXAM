import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3365: {
        "topic": "True Osselets",
        "Core_Anatomy": "Equine Fetlock (Metacarpophalangeal joint).",
        "Pathogenesis_Immediate": "True Osselets refers to the chronic, permanent osteoarthritis and exostosis (new bone formation) on the dorsal aspect of the fetlock joint.",
        "Pathogenesis_Deep": "As a progression from the acute, fluid-filled 'Green Osselets', if the horse continues to experience concussive trauma without rest, the torn joint capsule attachments calcify. Massive periosteal new bone (exostosis) grows on the dorsal distal metacarpal bone and proximal first phalanx. The joint capsule thickens, and the joint loses its normal range of motion.",
        "Why_Not": "Green osselets are acute and serous. True osselets are chronic and bony.",
        "Wow_Approach": "Once true osselets have formed, the mechanical damage is permanent. The horse will never regain its original speed and stride length."
    },
    3366: {
        "topic": "Septic Arthritis",
        "Core_Anatomy": "Synovial joints.",
        "Pathogenesis_Immediate": "Septic arthritis is the acute bacterial infection of a synovial joint cavity.",
        "Pathogenesis_Deep": "It can occur via direct penetrating trauma (e.g., stepping on a nail, or a bite wound) or via hematogenous spread (navel ill in foals/calves). The bacteria rapidly multiply in the nutrient-rich synovial fluid, releasing enzymes that utterly destroy the articular cartilage within 48-72 hours. The joint is hot, massively swollen, and the animal is usually non-weight-bearing lame (grade 5/5).",
        "Why_Not": "Osteoarthritis is sterile degeneration. Septic arthritis is an infectious surgical emergency.",
        "Wow_Approach": "Systemic antibiotics alone cannot cure septic arthritis because they do not penetrate the synovial fluid well enough. The joint MUST be aggressively flushed (arthrocentesis or arthrotomy) with liters of sterile saline to physically wash the bacteria and destructive enzymes out."
    },
    3369: {
        "topic": "Laminitis - Chronic Phase",
        "Core_Anatomy": "Equine Hoof (Corium and Pedal bone).",
        "Pathogenesis_Immediate": "The chronic phase of laminitis is characterized by the physical rotation and/or sinking of the pedal bone (P3).",
        "Pathogenesis_Deep": "In acute laminitis, the sensitive laminae (which hold the hoof wall to the coffin bone) become inflamed and ischemic. If the basement membrane detaches, the disease enters the chronic phase. Because the deep digital flexor tendon constantly pulls the back of the coffin bone upward, and the horse's weight pushes it downward, the bone physically detaches from the hoof wall and rotates point-downward. In severe cases, the point of P3 will penetrate straight through the sole of the hoof.",
        "Why_Not": "The acute phase is characterized by bounding digital pulses and heat, BEFORE any radiographic rotation has occurred.",
        "Wow_Approach": "Trimming the hooves of a chronically laminitic horse requires extreme skill to realign the hoof capsule with the newly rotated pedal bone, taking pressure off the toe."
    },
    3375: {
        "topic": "Myositis",
        "Core_Anatomy": "Skeletal muscle.",
        "Pathogenesis_Immediate": "Myositis is the generalized or localized inflammation of muscle tissue.",
        "Pathogenesis_Deep": "It can be caused by severe exertion (Exertional Rhabdomyolysis or 'Tying Up' in horses), immune-mediated diseases (Masticatory Muscle Myositis in dogs), or infectious agents (Clostridial myositis/Blackleg). The muscle becomes swollen, hard, and extremely painful, often releasing myoglobin into the urine (myoglobinuria).",
        "Why_Not": "Tendonitis is tendon inflammation. Osteomyelitis is bone infection.",
        "Wow_Approach": "N/A"
    },
    3383: {
        "topic": "Spondylosis Deformans",
        "Core_Anatomy": "Vertebral column.",
        "Pathogenesis_Immediate": "Spondylosis is the chronic degeneration of the intervertebral spaces leading to the formation of bony osteophytes (bridges) between vertebrae.",
        "Pathogenesis_Deep": "Common in older dogs (especially Boxers), it is a non-inflammatory, degenerative condition. Osteophytes grow from the ventral and lateral aspects of the vertebral bodies in an attempt to stabilize an unstable intervertebral joint. Eventually, these osteophytes can completely bridge and fuse adjacent vertebrae together.",
        "Why_Not": "Diskospondylitis is a destructive BACTERIAL INFECTION of the disc and endplates. Spondylosis is sterile, degenerative bridging.",
        "Wow_Approach": "Ironically, while it looks horrific on an X-ray (like a solid bony tube), spondylosis is usually completely asymptomatic and does not cause spinal cord compression because the bone grows OUTWARD, not into the spinal canal."
    },
    3389: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of a short essay section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3396: {
        "topic": "VSR III Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology Paper III.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3397: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3398: {
        "topic": "Exam Instruction - Time Limit",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating a one-hour time limit for Part A.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3399: {
        "topic": "Orthopaedics Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the Veterinary Orthopaedics and Lameness section.",
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
print(f"Batch 1/5 DONE: Updated {updated} questions.")
