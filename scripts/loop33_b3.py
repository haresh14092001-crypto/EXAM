import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3743: {
        "topic": "Azoturia (Exertional Rhabdomyolysis)",
        "Core_Anatomy": "Gluteal and Femoral muscles.",
        "Pathogenesis_Immediate": "Azoturia (Monday Morning Sickness / Exertional Rhabdomyolysis) is characterized by severe muscle necrosis and myoglobinuria after exercise.",
        "Pathogenesis_Deep": "In draft horses kept on full grain rations while resting over the weekend, resuming work on Monday triggers explosive glycogen metabolism, leading to lactic acid accumulation, severe muscle cell lysis, and release of myoglobin into the urine (turning it dark red/brown). The gluteal and thigh muscles become rock-hard and extremely painful.",
        "Why_Not": "Founder (laminitis) is a hoof disease, not muscle necrosis.",
        "Wow_Approach": "N/A"
    },
    3750: {
        "topic": "Boccar's Operation - Stringhalt",
        "Core_Anatomy": "Equine Hindlimb (Lateral Digital Extensor).",
        "Pathogenesis_Immediate": "Boccar's Operation (Lateral Digital Extensor Tenectomy) is the definitive surgical treatment for classic Stringhalt.",
        "Pathogenesis_Deep": "Stringhalt is a neuromuscular disorder in horses characterized by an involuntary, hyperflexion 'spasm' of the hock joint during walking, where the hoof violently jerks up toward the abdomen. Boccar's operation involves surgically resecting a 5-10 cm piece of the lateral digital extensor tendon at the lateral aspect of the metatarsus, along with a portion of its muscle belly, completely breaking the hyperactive reflex arc.",
        "Why_Not": "Cunean tenotomy is for Bone Spavin, not Stringhalt.",
        "Wow_Approach": "N/A"
    },
    3762: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3763: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3765: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3780: {
        "topic": "Choose the Best Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3781: {
        "topic": "Avulsion Fracture - Tibial Tuberosity",
        "Core_Anatomy": "Stifle (Tibial tuberosity/Knee).",
        "Pathogenesis_Immediate": "A classic avulsion fracture in young dogs involves the Tibial Tuberosity (Knee/Stifle).",
        "Pathogenesis_Deep": "In young, growing large-breed dogs, the tibial tuberosity is a separate growth plate (apophysis) where the massive patellar ligament attaches. During explosive jumping or landing, the quadriceps muscle contracts violently, pulling on the patellar ligament, which physically tears the tibial tuberosity clean off the tibia. The dog cannot extend the stifle joint.",
        "Why_Not": "Mandibular fractures are usually traumatic transverse/comminuted, not avulsion.",
        "Wow_Approach": "N/A"
    },
    3783: {
        "topic": "Joint Disease Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Elbow dysplasia, Hip dysplasia, Patellar luxation, Cruciate rupture) for a canine lameness question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3784: {
        "topic": "IM Pinning Biomechanics (Review)",
        "Core_Anatomy": "Medullary cavity.",
        "Pathogenesis_Immediate": "Intramedullary pinning neutralizes Bending forces only.",
        "Pathogenesis_Deep": "Reiterating that because a round pin sits loosely inside a round cavity, it has zero grip against rotation (torsion) or axial compression.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3785: {
        "topic": "Ortolani Sign - Hip Dysplasia (Review)",
        "Core_Anatomy": "Coxofemoral joint.",
        "Pathogenesis_Immediate": "A positive Ortolani sign is diagnostic for Hip Dysplasia (laxity).",
        "Pathogenesis_Deep": "Reiterating the palpable 'clunk' felt when subluxated hips are abducted, forcing the femoral head back into the acetabulum.",
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
