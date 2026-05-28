import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3236: {
        "topic": "Exam Marks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating mark distributions.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3237: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the short notes section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3241: {
        "topic": "VSR Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology Paper I.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3242: {
        "topic": "VSR Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3243: {
        "topic": "Objective Section Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the General Surgery and Anaesthesiology objective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3244: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3250: {
        "topic": "Intravenous Pyelography (IVP) - Kidneys",
        "Core_Anatomy": "Kidneys and Ureters.",
        "Pathogenesis_Immediate": "Intravenous pyelography (IVP) is used to study the function and structure of the Kidneys.",
        "Pathogenesis_Deep": "Also known as Excretory Urography. A water-soluble, iodinated contrast agent (like Iohexol) is injected into the jugular or cephalic vein. It travels to the kidneys and is rapidly filtered by the glomeruli. Serial radiographs are taken at 5, 10, and 20 minutes. This allows the radiologist to visualize the nephrogram phase (kidney parenchyma), the pyelogram phase (renal pelvis), and finally the ureters as the contrast drains into the bladder. It tests both renal anatomy (e.g., ectopic ureters, hydronephrosis) and renal function (if the kidneys don't filter the contrast, they are failing).",
        "Why_Not": "Cystography specifically targets the bladder.",
        "Wow_Approach": "Because the contrast agent is highly hyperosmolar, it acts as an osmotic diuretic. You must ensure the patient is fully hydrated before an IVP, otherwise the sudden fluid shift can cause acute renal failure."
    },
    3251: {
        "topic": "Bone Tumors - Radiopaque / Sunburst",
        "Core_Anatomy": "Appendicular skeleton (Metaphysis).",
        "Pathogenesis_Immediate": "Bone tumors will typically appear as Radiopaque, often with a characteristic 'sunburst' appearance, on an X-ray.",
        "Pathogenesis_Deep": "Primary bone tumors (like Osteosarcoma in large breed dogs) are highly aggressive. They cause both osteolysis (destroying the normal bone cortex, appearing black/lucent) and osteogenesis (producing new, chaotic tumor bone, appearing white/radiopaque). When the tumor bone grows aggressively outward from the cortex into the soft tissue, it creates spicules of bone radiating outward, classically described as a 'sunburst' periosteal reaction.",
        "Why_Not": "A simple fracture has sharp, clean lines. A bone cyst is purely radiolucent (black). An aggressive tumor is a chaotic mix of lysis and sunburst radiopacity.",
        "Wow_Approach": "Osteosarcoma almost always occurs 'Towards the knee, Away from the elbow' (distal femur/proximal tibia, distal radius/proximal humerus)."
    },
    3252: {
        "topic": "Choose the Best Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3253: {
        "topic": "Overlapping Suture - Hernia Closure",
        "Core_Anatomy": "Abdominal wall fascia / Linea alba.",
        "Pathogenesis_Immediate": "Overlapping suture patterns (like the Mayo mattress / vest-over-pants) are specifically indicated for Hernia closure.",
        "Pathogenesis_Deep": "When closing a massive fascial defect (like a large ventral or umbilical hernia) that is under extreme tension, standard appositional sutures will tear through the tissue. An overlapping pattern (Vest-over-pants) pulls one edge of the thick fascial ring completely UNDER the other edge. This creates a massive, double-layer surface area of fascia-to-fascia contact. This provides immense mechanical strength and rapid fibrous healing, preventing the hernia from tearing open again.",
        "Why_Not": "Using an overlapping suture on the intestine (oesophagus/uterus) would massively narrow the lumen and cause an instant, fatal obstruction. Hollow organs require appositional or inverting sutures.",
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
