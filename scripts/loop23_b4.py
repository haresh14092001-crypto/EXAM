import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2668: {
        "topic": "Neuroleptanalgesia - Hypnorm",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "Hypnorm is a commercial neuroleptanalgesic combination containing Fentanyl (an opioid) and Fluanisone (a butyrophenone tranquilizer).",
        "Pathogenesis_Deep": "Neuroleptanalgesia is the state of profound sedation and analgesia achieved by combining a neuroleptic (tranquilizer) with a potent opioid analgesic. Hypnorm (Fentanyl + Fluanisone) is heavily utilized in laboratory animal medicine (rodents, rabbits). It provides deep surgical anaesthesia when combined with a benzodiazepine (like Midazolam). Because it relies on an opioid, the analgesic and respiratory depressant effects can be rapidly reversed with Naloxone or Buprenorphine at the end of the procedure.",
        "Why_Not": "Immobilon is Etorphine + Acepromazine. Innovar-Vet is Fentanyl + Droperidol. Hypnorm specifically pairs Fentanyl with Fluanisone.",
        "Wow_Approach": "In rabbits, combining Hypnorm with Midazolam provides a very safe, reversible surgical plane of anaesthesia, avoiding the severe cardiovascular depression caused by volatile agents (Isoflurane) in this sensitive species."
    },
    2674: {
        "topic": "Definitions Section Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the 'Definitions' section of the exam.",
        "Pathogenesis_Deep": "Surgical definitions require absolute precision. For example, 'Asepsis' vs 'Antisepsis', or 'Sinus' vs 'Fistula'.",
        "Why_Not": "Structural header.",
        "Wow_Approach": "A good surgical definition always includes the anatomical structure involved, the pathological process, and (if applicable) the surgical objective."
    },
    2682: {
        "topic": "Essay Section - Nerve Blocks of the Ox Head",
        "Core_Anatomy": "Bovine cranial nerves (Trigeminal branches).",
        "Pathogenesis_Immediate": "Essay question detailing fracture management, wound complications, and specific nerve blocks of the bovine head.",
        "Pathogenesis_Deep": "Nerve blocks of the bovine head are critical for standing surgery. Key blocks: (1) Cornual nerve block (midway between lateral canthus and horn base) for dehorning. (2) Auriculopalpebral nerve block (branch of CN VII, blocked on the zygomatic arch) to paralyze the eyelids for eye examination. (3) Retrobulbar block (depositing lidocaine deep behind the globe) for enucleation, blocking CN II, III, IV, V (ophthalmic), and VI. (4) Infraorbital block (at the infraorbital foramen) for upper lip/teeth surgery.",
        "Why_Not": "General anaesthesia in adult cattle carries huge risks of bloat, regurgitation, and aspiration pneumonia. Therefore, regional nerve blocks are the gold standard for bovine head surgery.",
        "Wow_Approach": "The Auriculopalpebral block is purely MOTOR. It stops the cow from blinking (blepharospasm) but provides ZERO pain relief to the eye itself. It must always be combined with a topical or sensory block (like a retrobulbar block) for painful procedures."
    },
    2686: {
        "topic": "VSR Exam Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for Veterinary Surgery and Radiology Paper I.",
        "Pathogenesis_Deep": "Structural marker for a new exam paper.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2687: {
        "topic": "Exam Instruction",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Administrative instruction regarding exam submission.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2688: {
        "topic": "VSR 411 Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the objective section for General Surgery, Anaesthesiology, and Diagnostic Imaging.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2689: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for the fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2695: {
        "topic": "Intravenous Pyelography (IVP)",
        "Core_Anatomy": "Kidneys and ureters.",
        "Pathogenesis_Immediate": "Intravenous pyelography (IVP) or Excretory Urography is used to study the structure and function of the Kidneys (and ureters).",
        "Pathogenesis_Deep": "IVP involves injecting a water-soluble iodinated contrast medium into a peripheral vein. The kidneys rapidly filter and excrete this contrast. Serial radiographs are taken at 5, 10, and 20 minutes. The study has three phases: (1) Nephrogram phase (contrast highlights the renal parenchyma, assessing renal blood flow and function). (2) Pyelogram phase (contrast fills the renal pelvis). (3) Excretory phase (contrast outlines the ureters as it travels to the bladder).",
        "Why_Not": "Cystography studies the bladder. Urethrography studies the urethra. IVP specifically assesses renal filtration function and the upper urinary tract anatomy (e.g., diagnosing ectopic ureters or torn ureters).",
        "Wow_Approach": "If you perform an IVP and one kidney completely fails to 'light up' with contrast during the nephrogram phase, it definitively proves that the kidney is completely non-functional (e.g., destroyed by hydronephrosis or end-stage pyelonephritis) or lacks blood supply."
    },
    2696: {
        "topic": "Bone Tumors - Radiographic Appearance",
        "Core_Anatomy": "Bone cortex and periosteum.",
        "Pathogenesis_Immediate": "Malignant primary bone tumors (Osteosarcoma) classically appear with a 'Sunburst' appearance or 'Codman's triangle' on X-ray.",
        "Pathogenesis_Deep": "Osteosarcoma (the most common primary bone tumor in dogs, usually 'away from the elbow, towards the knee') causes aggressive osteolysis (bone destruction) mixed with chaotic new bone proliferation. The tumor rapidly breaches the cortex and lifts the periosteum. The periosteum reacts by laying down spicules of new bone perpendicular to the cortex, creating a radiating, brush-like 'Sunburst' appearance. The edge of the elevated periosteum forms a triangular wedge of new bone called 'Codman's Triangle'.",
        "Why_Not": "Benign bone cysts appear as smooth, well-marginated radiolucencies (holes). Malignant tumors have ill-defined transition zones, cortical destruction, and chaotic 'sunburst' periosteal reactions.",
        "Wow_Approach": "Osteosarcoma never crosses the joint space. If a lytic bone lesion crosses an articular surface into the adjacent bone, it is almost certainly an infection (septic arthritis/osteomyelitis), NOT a primary bone tumor."
    },
    2697: {
        "topic": "Overlapping Suture Pattern - Hernia Closure",
        "Core_Anatomy": "Abdominal fascia and linea alba.",
        "Pathogenesis_Immediate": "Overlapping suture patterns (like the Mayo mattress/Vest-over-pants) are strongly indicated for Hernia closure.",
        "Pathogenesis_Deep": "The 'Vest-over-pants' (Mayo mattress) suture is a specialized overlapping mattress pattern. Instead of bringing the two edges of the fascia edge-to-edge (apposition), this suture draws one flap of fascia completely UNDER the other flap, creating a double-layer thickness of tissue over the defect. This massive imbrication (overlapping) provides extraordinary biomechanical strength and a very large surface area for fibrous tissue healing. It is the classic historical technique for repairing large umbilical or ventral hernias under high tension.",
        "Why_Not": "Oesophagus, Intestine, and Uterus are hollow organs; an overlapping suture would massively narrow their lumen (causing stricture) and expose mucosal surfaces to the peritoneum (causing fatal leakage). They require precise appositional or inverting sutures.",
        "Wow_Approach": "While the vest-over-pants suture is mechanically strong, modern veterinary surgery often prefers simple apposition of the fascial edges with non-absorbable monofilament or the use of prosthetic mesh, as extreme overlapping can distort abdominal anatomy and cause excessive postoperative pain."
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
