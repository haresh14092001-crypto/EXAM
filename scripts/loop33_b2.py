import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3726: {
        "topic": "Sesamoid Fractures - Horses",
        "Core_Anatomy": "Proximal sesamoid bones (Fetlock).",
        "Pathogenesis_Immediate": "Sesamoid fractures are notoriously common in racehorses and can present as deferred/delayed lameness.",
        "Pathogenesis_Deep": "The two proximal sesamoid bones sit inside the suspensory apparatus behind the fetlock joint, subjected to immense tensile forces during a gallop. Fractures can be apical, basilar, or abaxial. Because these bones have a very poor blood supply (strictly entering from the distal and proximal poles) and are constantly pulled by the suspensory ligament and distal sesamoidean ligaments, they have an extremely high rate of non-union, often requiring surgical removal of the fragment or internal fixation.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3727: {
        "topic": "Hip Dislocation in Large Animals (Review)",
        "Core_Anatomy": "Coxofemoral joint.",
        "Pathogenesis_Immediate": "The most common type of hip dislocation in large animals is Cranio-dorsal.",
        "Pathogenesis_Deep": "Reiterating that gluteal muscle contraction pulls the femoral head forward and upward once the ligamentum teres ruptures.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3728: {
        "topic": "Type Ia External Skeletal Fixator",
        "Core_Anatomy": "Bone (Fixator construct).",
        "Pathogenesis_Immediate": "A unilateral, uniplanar external skeletal fixator is classified as a Type Ia fixator.",
        "Pathogenesis_Deep": "External skeletal fixators (ESF) use transfixation pins driven through the bone that are connected externally by rigid bars. A Type Ia fixator uses pins that only pierce ONE side of the skin and bone cortex (percutaneous) and are connected by a single external bar on a single side of the leg. It is the easiest to apply but is the mechanically weakest ESF type.",
        "Why_Not": "Type II is bilateral, uniplanar (pins go completely through the leg and are connected by bars on BOTH sides). Type III is a massive, three-dimensional bilateral, biplanar frame used for severe non-unions.",
        "Wow_Approach": "N/A"
    },
    3729: {
        "topic": "UMN vs LMN Lesions - Hyperreflexia",
        "Core_Anatomy": "Central nervous system (Motor pathways).",
        "Pathogenesis_Immediate": "In an Upper Motor Neuron (UMN) lesion, the classic clinical sign is Hyperreflexia (increased spinal reflexes).",
        "Pathogenesis_Deep": "UMNs originate in the brain and descend down the spinal cord. Their primary job is to tell the Lower Motor Neurons (LMNs, which go directly to the muscles) what to do, acting largely as a constant brake (inhibitory signal). If a UMN is damaged (e.g., a thoracic spinal cord compression), the brake is completely removed. The LMNs fire uncontrollably, resulting in spastic paresis, hyperreflexia (wildly exaggerated reflexes), and hypertonia (increased muscle tone).",
        "Why_Not": "An LMN lesion (damage to the actual nerve leaving the spine, like radial nerve paralysis) causes Hyporeflexia, Hypotonia (flaccidity), and rapid neurogenic atrophy.",
        "Wow_Approach": "Mnemonic: UMN = Up (reflexes/tone go UP); LMN = Lower (reflexes/tone go DOWN)."
    },
    3730: {
        "topic": "Pastern Arthrodesis - High Ringbone",
        "Core_Anatomy": "Pastern Joint (Proximal Interphalangeal joint).",
        "Pathogenesis_Immediate": "Pastern Arthrodesis (surgical joint fusion) is the definitive treatment of choice for severe High Ringbone.",
        "Pathogenesis_Deep": "High ringbone is severe osteoarthritis of the pastern joint. Because this is a 'low-motion' joint, its normal movement is not critical for gait. However, the bone-on-bone grinding of severe arthritis is excruciatingly painful. By surgically removing the remaining cartilage and locking the two phalanges together with a plate and screws, the joint is fused (arthrodesed) into a single bone. Once fused, there is zero motion, and therefore zero pain, curing the lameness.",
        "Why_Not": "Low ringbone (coffin joint) is a high-motion joint; fusing it severely impairs the horse's gait. Low ringbone has a much poorer prognosis.",
        "Wow_Approach": "N/A"
    },
    3731: {
        "topic": "Equine Hoof Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Canker, Cab horse disease, Quittor, Pyramidal disease) for a hoof pathology question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3732: {
        "topic": "Varus vs Valgus Deformity",
        "Core_Anatomy": "Limb alignment.",
        "Pathogenesis_Immediate": "Medial deviation of the limb distal to the location of the deformity is called Varus.",
        "Pathogenesis_Deep": "Angular limb deformities in foals/puppies are classified by direction. Varus ('bow-legged') is a medial deviation—if the knee is the site of deformity, the hoof deviates inward toward the midline. Valgus ('knock-kneed') is a lateral deviation—the hoof points outward, away from the midline.",
        "Why_Not": "Recurvatum is hyperextension of a joint (backward bending), not an angular lateral/medial deviation.",
        "Wow_Approach": "Mnemonic: VaLgus has a 'L' for Lateral deviation. Varus does not."
    },
    3733: {
        "topic": "Synarthrosis - Skull Sutures",
        "Core_Anatomy": "Fibrous joints (Sutures).",
        "Pathogenesis_Immediate": "A classic example of a Synarthrosis is the sutures of the Skull.",
        "Pathogenesis_Deep": "Joints are classified by mobility. Synarthroses are completely immovable fibrous joints where the bones are bound tightly by dense fibrous tissue, such as the cranial sutures of the skull. Over time, these joints naturally ossify.",
        "Why_Not": "The shoulder, elbow, and hip are Diarthroses (highly mobile synovial joints).",
        "Wow_Approach": "N/A"
    },
    3734: {
        "topic": "Legg-Calve-Perthes Disease",
        "Core_Anatomy": "Femoral head.",
        "Pathogenesis_Immediate": "The statement 'Legg-Perthes disease is common in toy breeds' is TRUE.",
        "Pathogenesis_Deep": "Legg-Calve-Perthes disease is aseptic, avascular necrosis of the femoral head, seen almost exclusively in young (4-11 months), toy and small breed dogs (Poodles, Yorkies, Westies). The blood supply to the femoral head spontaneously fails, causing the bone to die and collapse under weight-bearing. The dog presents with severe hindlimb lameness and muscle atrophy.",
        "Why_Not": "Large breeds get Hip Dysplasia, not Legg-Perthes.",
        "Wow_Approach": "The definitive, highly successful treatment is a Femoral Head and Neck Osteotomy (FHO), where the dead femoral head is simply sawed off, allowing the gluteal muscles to form a pain-free 'false joint' (pseudoarthrosis)."
    },
    3742: {
        "topic": "Tension Band Wiring - Avulsion Fractures",
        "Core_Anatomy": "Tendon/Ligament attachments.",
        "Pathogenesis_Immediate": "Tension Band Wiring is the absolute method of choice for stabilizing Avulsion Fractures.",
        "Pathogenesis_Deep": "As reviewed, when a tendon rips a piece of bone off (like the triceps pulling off the olecranon), the muscle is constantly pulling the fragment away, preventing healing. A tension band construct uses two parallel K-wires driven across the fracture and a figure-8 wire loop. As the triceps muscle contracts, the mechanical setup physically CONVERTS the pulling tension into compressive force at the fracture line, pressing the bones together and speeding up healing.",
        "Why_Not": "Using standard plates or screws would strip out instantly under the massive pulling force of the muscle.",
        "Wow_Approach": "This is one of the most beautiful biomechanical concepts in orthopaedics: using the body's own destructive muscle pull to physically compress and heal the fracture."
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
print(f"Batch 2/5 DONE: Updated {updated} questions.")
