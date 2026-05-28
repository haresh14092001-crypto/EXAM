import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    4010: {
        "topic": "Delayed Union Causes",
        "Core_Anatomy": "Fracture site.",
        "Pathogenesis_Immediate": "The most common causes of Delayed Union in bone healing are inadequate fixation (instability) and poor local blood supply.",
        "Pathogenesis_Deep": "Bone healing (osteogenesis) requires mechanical stability and a rich blood supply to bring osteoblasts and nutrients. If the fracture is poorly immobilized (interrupted fixation), the micro-movement constantly tears the delicate early blood vessels and cartilage callus. If the local blood supply is stripped during surgery or initial trauma, cells cannot survive, delaying bone bridging.",
        "Why_Not": "Anatomical reduction (lining the bones up perfectly) speeds up healing; poor reduction causes mal-union, not necessarily delayed union.",
        "Wow_Approach": "N/A"
    },
    4012: {
        "topic": "Upward Patellar Luxation (Review)",
        "Core_Anatomy": "Stifle (Femoropatellar joint).",
        "Pathogenesis_Immediate": "The most common femoropatellar articulation defect in cattle and buffaloes is Upward Luxation of the Patella.",
        "Pathogenesis_Deep": "Reiterating that the medial patellar ligament becomes locked over the medial trochlear ridge of the femur, locking the hindlimb in extension.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3013: {
        "topic": "Stifle Joint - Complex Joint",
        "Core_Anatomy": "Stifle Joint (Femorotibial).",
        "Pathogenesis_Immediate": "The stifle joint is classified anatomically as a Complex Joint.",
        "Pathogenesis_Deep": "A simple joint involves only two bones. A compound joint involves more than two bones (like the carpus). A complex joint is specifically defined as a joint that contains an invaginating fibrocartilaginous structure (meniscus or disc) that completely or partially divides the joint cavity. The stifle contains two C-shaped fibrocartilaginous menisci (medial and lateral) to absorb shock and distribute weight between the curved femoral condyles and flat tibial plateau.",
        "Why_Not": "A pseudo-joint (false joint) is a pathological non-union, not a normal anatomical classification.",
        "Wow_Approach": "N/A"
    },
    4013: {
        "topic": "Stifle Joint - Complex Joint (Duplicate)",
        "Core_Anatomy": "Stifle Joint (Femorotibial).",
        "Pathogenesis_Immediate": "The stifle joint is classified anatomically as a Complex Joint.",
        "Pathogenesis_Deep": "A complex joint is specifically defined as a joint that contains an invaginating fibrocartilaginous structure (meniscus or disc) that completely or partially divides the joint cavity. The stifle contains two C-shaped fibrocartilaginous menisci (medial and lateral).",
        "Why_Not": "A pseudo-joint is a pathological non-union.",
        "Wow_Approach": "N/A"
    },
    4014: {
        "topic": "Exertional Myopathy (Review)",
        "Core_Anatomy": "Skeletal muscle.",
        "Pathogenesis_Immediate": "Exertional Myopathy is also known as Monday Morning Sickness, Azoturia, or Exertional Rhabdomyolysis.",
        "Pathogenesis_Deep": "Reiterating that exercise after rest on full grain rations causes severe glycogen metabolism, muscle necrosis, and dark red myoglobinuria.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4015: {
        "topic": "Sesamoiditis",
        "Core_Anatomy": "Proximal Sesamoid Bones and Suspensory Ligament.",
        "Pathogenesis_Immediate": "The clinical condition characterized by pain associated with the proximal sesamoid bones and the insertions of the suspensory ligament is called Sesamoiditis.",
        "Pathogenesis_Deep": "It is a chronic, painful inflammatory condition common in performance horses, caused by repetitive strain on the suspensory apparatus. Radiographically, it appears as demineralization, osteophyte formation, and enlargement of the vascular channels inside the proximal sesamoid bones, heavily predisposing the horse to suspensory ligament tear.",
        "Why_Not": "Navicular disease affects the distal sesamoid bone at the hoof, not the proximal sesamoids at the fetlock.",
        "Wow_Approach": "N/A"
    },
    4016: {
        "topic": "Gonitis",
        "Core_Anatomy": "Stifle Joint (Knee).",
        "Pathogenesis_Immediate": "Gonitis is the specific clinical term for inflammation of the Stifle Joint.",
        "Pathogenesis_Deep": "It can be acute (due to trauma, meniscus tear, or cranial cruciate rupture) or chronic (degenerative joint disease or osteochondrosis). It presents with severe hindlimb lameness, joint effusion (swelling of the joint capsule), and pain on flexion.",
        "Why_Not": "Coxitis is inflammation of the hip joint. Arthritis is a generic term for any joint.",
        "Wow_Approach": "N/A"
    },
    4017: {
        "topic": "Ringbone (Review)",
        "Core_Anatomy": "Interphalangeal joints.",
        "Pathogenesis_Immediate": "Exostosis at the level of the interphalangeal joints is called Ringbone.",
        "Pathogenesis_Deep": "Reiterating the osteophyte formation (exostosis) at the proximal (High) or distal (Low) interphalangeal joints.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4018: {
        "topic": "Sidebone",
        "Core_Anatomy": "Hoof (Ungual cartilages).",
        "Pathogenesis_Immediate": "Sidebone is the ossification (calcification) of the collateral (ungual) cartilages of the third phalanx.",
        "Pathogenesis_Deep": "The collateral cartilages sit on the medial and lateral sides of P3 inside the hoof, acting as shock absorbers. Due to chronic concussion (especially working on hard roads) or poor hoof balance, these cartilages naturally undergo dystrophic calcification and turn into rigid bone. It is common in draft horses and rarely causes significant lameness once ossified.",
        "Why_Not": "Thrush is an anaerobic bacterial infection of the frog. Spavin is osteoarthritis of the hock.",
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

# Final validation
with open(db_path, "r", encoding="utf-8") as f:
    c2 = f.read()
d2 = json.loads(re.sub(r'^.*?const examData = ', '', c2, flags=re.DOTALL).rsplit(';',1)[0].strip())
empty2 = [x for x in d2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
