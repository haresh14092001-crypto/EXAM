import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3786: {
        "topic": "Filleting - Dewclaw Amputation",
        "Core_Anatomy": "Digits (Dewclaw).",
        "Pathogenesis_Immediate": "The surgical technique of 'Filleting' is commonly used for the amputation of the Dewclaw.",
        "Pathogenesis_Deep": "To remove a diseased or traumatic dewclaw, a vertical incision is made over the bone. The phalanges are meticulously dissected out ('shelled out') from the surrounding soft tissue, leaving the entire skin envelope intact. The bone is removed (amputated), and the preserved skin sleeve is sutured closed over the empty space, providing excellent cosmetic results and rapid healing.",
        "Why_Not": "A tail amputation (caudectomy) uses a circular cut, not a filleting technique.",
        "Wow_Approach": "N/A"
    },
    3788: {
        "topic": "Ulnar Nerve Injury",
        "Core_Anatomy": "Forelimb (Flexor muscles and caudal sensation).",
        "Pathogenesis_Immediate": "Ulnar nerve injury leads to loss of sensation in the caudal forearm and mild hyperextension of the carpus.",
        "Pathogenesis_Deep": "The ulnar nerve arises from the brachial plexus (C8-T2) and runs caudally to supply the flexor carpi ulnaris and deep digital flexor. Traumatic injury leads to loss of cutaneous sensation over the caudal aspect of the forearm and metacarpus. Unlike radial nerve paralysis, the animal can still bear weight normally.",
        "Why_Not": "Radial nerve paralysis completely prevents weight-bearing (dropped elbow).",
        "Wow_Approach": "N/A"
    },
    3789: {
        "topic": "Incomplete Fracture - Greenstick (Review)",
        "Core_Anatomy": "Young bone cortex.",
        "Pathogenesis_Immediate": "A classic type of incomplete fracture is the Greenstick fracture.",
        "Pathogenesis_Deep": "Reiterating that because young bone is highly flexible, it bends and breaks on only one cortex, leaving the opposite cortex intact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3790: {
        "topic": "Transverse Fracture Stability",
        "Core_Anatomy": "Bone shaft.",
        "Pathogenesis_Immediate": "A Transverse fracture is classified as a highly stable fracture once reduced.",
        "Pathogenesis_Deep": "A transverse fracture line runs perpendicular (90 degrees) to the long axis of the bone. When the bone ends are lined up (reduced) and subjected to weight-bearing (axial compression), the flat bone edges push directly against each other, preventing telescoping or shifting.",
        "Why_Not": "An oblique or spiral fracture is highly unstable because axial weight-bearing forces the bone ends to slide past each other, causing the leg to collapse.",
        "Wow_Approach": "N/A"
    },
    3791: {
        "topic": "Patella - Largest Sesamoid Bone",
        "Core_Anatomy": "Stifle Joint.",
        "Pathogenesis_Immediate": "The largest sesamoid bone in the animal body is the Patella.",
        "Pathogenesis_Deep": "A sesamoid bone is a bone that develops entirely within a tendon to protect the tendon from extreme frictional wear and to increase its mechanical leverage. The Patella is embedded completely within the massive tendon of insertion of the quadriceps femoris muscle (the patellar ligament), sliding inside the trochlear groove of the femur.",
        "Why_Not": "The navicular bone (distal sesamoid) is much smaller. The accessory carpal is a carpal bone, not a true sesamoid.",
        "Wow_Approach": "N/A"
    },
    3793: {
        "topic": "Spastic Paresis (Elso Heel)",
        "Core_Anatomy": "Bovine Hindlimb (Tibial nerve / Gastrocnemius).",
        "Pathogenesis_Immediate": "Spastic Paresis (Elso Heel) is a hereditary neuromuscular disease in calves characterized by extreme spastic contraction of the gastrocnemius muscle.",
        "Pathogenesis_Deep": "Affected calves (usually 2-10 months old) present with a stiff, hyperextended hindlimb that swings forward without flexing the hock. The gastrocnemius muscle and superficial digital flexor are in a permanent state of spastic contraction, pulling the hock into extension. The leg appears noticeably shorter and is held off the ground.",
        "Why_Not": "Hemiparesis is weakness of one side of the body, not focal spastic contraction.",
        "Wow_Approach": "Surgical treatment requires a Tibial Neurectomy (cutting a portion of the tibial nerve) or gastrocnemius tenectomy to permanently break the spastic contraction loop."
    },
    3794: {
        "topic": "Bone Healing Complications Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Non-union, Mal-union, Delayed union) for a bone healing question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3795: {
        "topic": "LMN Lesion - Hyporeflexia (Review)",
        "Core_Anatomy": "Lower Motor Neuron.",
        "Pathogenesis_Immediate": "In a Lower Motor Neuron (LMN) lesion, there is Hyporeflexia and Hypotonia.",
        "Pathogenesis_Deep": "Reiterating that because the actual reflex arc nerve is destroyed, the muscle loses all tone and reflexes are completely absent.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3796: {
        "topic": "Os Corona (Second Phalanx)",
        "Core_Anatomy": "Equine Digit (P2).",
        "Pathogenesis_Immediate": "The second phalangeal bone is anatomically named the Os Corona (Crown bone).",
        "Pathogenesis_Deep": "The three phalanges of the horse's digit are: First Phalanx (P1) = Os Suffraginis (Pastern bone); Second Phalanx (P2) = Os Corona (Short pastern bone); Third Phalanx (P3) = Os Pedis (Coffin bone).",
        "Why_Not": "Os coxa is the pelvic bone. Os pedis is P3.",
        "Wow_Approach": "N/A"
    },
    3797: {
        "topic": "Diarthrodial Joint Anatomy",
        "Core_Anatomy": "Synovial joints.",
        "Pathogenesis_Immediate": "A Diarthrodial joint is a highly mobile synovial joint, with classic examples including the Shoulder, Hip, Stifle, and Elbow joints.",
        "Pathogenesis_Deep": "Diarthrodial joints are characterized by having a joint cavity filled with synovial fluid, a fibrous joint capsule lined by a synovial membrane, and bone ends covered by friction-reducing articular cartilage. They allow wide ranges of movement.",
        "Why_Not": "Synarthroses (skull sutures) and Amphiarthroses (pelvic symphysis) have minimal to zero mobility.",
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
