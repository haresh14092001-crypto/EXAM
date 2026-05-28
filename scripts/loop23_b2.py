import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2628: {
        "topic": "Anaesthetic Pharmacology Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "This represents another numerical option from the preceding Atropine dosage question.",
        "Pathogenesis_Deep": "Always strictly adhere to the 0.02 - 0.04 mg/kg range for canine Atropine.",
        "Why_Not": "Under-dosing or over-dosing anticholinergics causes severe cardiac arrhythmias.",
        "Wow_Approach": "In CPR (Cardiopulmonary Resuscitation), Atropine is used for treating asystole or PEA (Pulseless Electrical Activity), often administered at the higher end of the dose range or specifically via the intra-tracheal route if venous access is lost."
    },
    2629: {
        "topic": "Ischemic Ulcer - Pressure/Bed Sores",
        "Core_Anatomy": "Skin over bony prominences (e.g., greater trochanter, olecranon).",
        "Pathogenesis_Immediate": "An ulcer that occurs due to continuous lack of nutrition (blood supply) to local tissues, leading to pressure or bed sores, is termed an Ischemic Ulcer.",
        "Pathogenesis_Deep": "Decubitus ulcers (bed sores) develop in recumbent or paralyzed animals (e.g., spinal injury dogs, downer cows). When the animal's weight compresses the skin against a hard surface and an underlying bony prominence (like the tuber coxae or olecranon), the local capillary bed is crushed. If this pressure exceeds the capillary filling pressure for more than 2 hours, the tissue suffers from severe ischemia. Deprived of oxygen and nutrients, the skin and underlying subcutaneous fat undergo ischemic necrosis, sloughing off to form a deep, non-healing ulcer.",
        "Why_Not": "It is not primarily infective (though it gets secondarily infected) nor iatrogenic. The root cause is ischemia (lack of blood flow).",
        "Wow_Approach": "Prevention is the ONLY effective treatment for decubitus ulcers. A recumbent animal must be physically turned over every 2-4 hours, provided with deep, soft bedding (like a waterbed or thick foam), and kept perfectly dry from urine/feces."
    },
    2630: {
        "topic": "Ischemic Ulcer - Decubitus Pathogenesis",
        "Core_Anatomy": "Skin capillary beds.",
        "Pathogenesis_Immediate": "Confirmation that pressure/bed sores are classified pathologically as Ischemic ulcers.",
        "Pathogenesis_Deep": "The cascade of an ischemic decubitus ulcer: Prolonged pressure -> Capillary occlusion -> Tissue hypoxia -> Endothelial damage -> Microvascular thrombosis -> Full-thickness coagulative necrosis -> Sloughing of dead tissue (eschar) -> Deep open wound. These wounds heal extremely slowly because the surrounding tissue remains poorly perfused.",
        "Why_Not": "Neuropathic ulcers occur due to loss of sensation (e.g., a dog chewing its own foot after a nerve block), but the mechanism of a bed sore is strictly ischemic pressure.",
        "Wow_Approach": "In large animals (like downer cows), the massive body weight accelerates this process exponentially. A cow left on hard concrete on one side for just 6 hours will develop irreversible ischemic muscle necrosis (crush syndrome) in the 'down' hindlimb."
    },
    2631: {
        "topic": "Reactionary Haemorrhage - Timing",
        "Core_Anatomy": "Surgical vascular pedicles.",
        "Pathogenesis_Immediate": "Haemorrhage that occurs within 24 hours after the primary bleeding (surgery) is Reactionary Haemorrhage.",
        "Pathogenesis_Deep": "During surgery, an animal's blood pressure is typically lower due to the depressant effects of general anaesthesia (vasodilation, decreased cardiac output). A clot may form over an unligated small vessel, or a ligature may be tied just tightly enough to hold at this low pressure. When the animal recovers and wakes up, sympathetic tone returns, blood pressure spikes, and the increased hydrostatic pressure blows the clot off or slips the ligature, causing reactionary haemorrhage. This typically happens within the first 6-24 hours post-operatively.",
        "Why_Not": "Primary haemorrhage happens on the operating table. Secondary haemorrhage happens days later due to infection/tissue sloughing.",
        "Wow_Approach": "The classic sign of internal reactionary haemorrhage in a post-op spay dog is sudden onset of pale mucous membranes, tachycardia, and a progressively distending, fluid-filled abdomen hours after a seemingly perfect surgery."
    },
    2632: {
        "topic": "Cardiogenic Shock",
        "Core_Anatomy": "Myocardium (heart muscle).",
        "Pathogenesis_Immediate": "Inherent heart diseases such as arrhythmias or myocardial trauma cause Cardiogenic Shock.",
        "Pathogenesis_Deep": "Shock is defined as inadequate cellular energy production due to poor tissue perfusion. Cardiogenic shock occurs when the heart's pumping mechanism fails (a 'forward failure'), despite having an adequate blood volume in the body. Causes include severe arrhythmias (e.g., ventricular tachycardia), dilated cardiomyopathy, cardiac tamponade, or direct myocardial trauma (e.g., a dog hit by a car developing traumatic myocarditis). The heart simply cannot generate enough cardiac output to maintain blood pressure and tissue perfusion.",
        "Why_Not": "Hypovolemic shock = loss of blood volume. Vasogenic/Distributive shock (e.g., anaphylaxis, sepsis) = massive vasodilation (pipes too big). Cardiogenic shock = pump failure.",
        "Wow_Approach": "Treating cardiogenic shock with aggressive IV fluid therapy (which is the standard treatment for hypovolemic shock) is LETHAL. It overloads the already failing heart, instantly causing fatal pulmonary edema. Cardiogenic shock requires positive inotropes (Dobutamine) to strengthen the pump."
    },
    2633: {
        "topic": "Cornual Nerve - Trigeminal Branches (Goat)",
        "Core_Anatomy": "Cranial nerves and horn base.",
        "Pathogenesis_Immediate": "The Cornual nerve is a branch of the Trigeminal nerve (specifically, the goat horn receives innervation from the lacrimal/infratrochlear branches of the ophthalmic division AND the zygomaticotemporal branch of the maxillary division).",
        "Pathogenesis_Deep": "Horn innervation differs critically between cattle and goats. In cattle, the horn is innervated solely by the Cornual nerve (a branch of the zygomaticotemporal nerve, from the maxillary division of Trigeminal, CN V). In goats, the horn is innervated by TWO separate nerve branches: the Cornual branch of the zygomaticotemporal nerve (Maxillary division) AND the Cornual branch of the infratrochlear nerve (Ophthalmic division). Therefore, dehorning a goat requires a dual-point nerve block on each side of the head.",
        "Why_Not": "Facial nerve is motor. Vagus is autonomic. Trigeminal is the great sensory nerve of the head.",
        "Wow_Approach": "To block a goat's horn: inject local anaesthetic halfway between the lateral canthus and the horn base (for the zygomaticotemporal branch) AND halfway between the medial canthus and the horn base (for the infratrochlear branch)."
    },
    2634: {
        "topic": "Capillary Refill Time (CRT)",
        "Core_Anatomy": "Gingival mucous membranes and systemic microcirculation.",
        "Pathogenesis_Immediate": "The normal capillary refill time (CRT) is Less than 2 seconds.",
        "Pathogenesis_Deep": "CRT is a rapid, non-invasive clinical test used to assess peripheral tissue perfusion and cardiovascular function. When you press firmly on the unpigmented gingival mucosa, you squeeze blood out of the capillary bed (blanching it white). When you release, the time it takes for the pink color to return indicates how effectively the cardiovascular system is perfusing peripheral tissues. A normal, healthy animal with good cardiac output and vascular tone will refill in 1 to 2 seconds.",
        "Why_Not": "A CRT of >2 seconds (prolonged) indicates poor peripheral perfusion (shock, heart failure, severe dehydration, or deep anaesthesia). A CRT of <1 second (brisk) indicates hyperdynamic states (early sepsis, hyperthermia, severe stress/pain).",
        "Wow_Approach": "CRT assesses PERFUSION, not oxygenation. A dog can be suffocating with blue mucous membranes (cyanosis), but if its heart is still beating strongly, its CRT will still be a normal 2 seconds. Conversely, a dog bleeding to death will have pale membranes and a severely prolonged CRT (>4 seconds)."
    },
    2635: {
        "topic": "Hernioplasty - Prosthetic Repair",
        "Core_Anatomy": "Abdominal wall fascia and muscle.",
        "Pathogenesis_Immediate": "Repair of a hernia using a prosthesis (synthetic mesh) to close the ring is called Hernioplasty.",
        "Pathogenesis_Deep": "Hernia repair techniques depend on the size of the defect. (1) Herniorrhaphy: The direct suturing together of the anatomical edges of the hernia ring (e.g., closing an umbilical hernia with simple interrupted sutures). (2) Hernioplasty: Used when the hernia defect is so large that the edges cannot be pulled together without excessive tension (which would lead to suture tear-out and recurrence). The surgeon implants a synthetic prosthetic mesh (e.g., Polypropylene mesh) to bridge the gap. The body forms granulation and fibrous tissue through the pores of the mesh, creating a strong, permanent artificial abdominal wall.",
        "Why_Not": "Herniorrhaphy uses the patient's own tissue edges. Kelotomy is the surgical incision of a strictured hernia ring to relieve strangulation. Hernioplasty specifically implies the use of a graft or prosthetic mesh to reconstruct the defect.",
        "Wow_Approach": "Polypropylene mesh is non-absorbable and provides permanent strength, but if the hernia site is infected (e.g., a strangulated, ruptured bowel), using synthetic mesh is contraindicated because bacteria will colonize the mesh biofilm, leading to a chronic, intractable draining tract."
    },
    2636: {
        "topic": "Compound Fracture - Open Wound",
        "Core_Anatomy": "Bone, periosteum, and overlying skin/muscle.",
        "Pathogenesis_Immediate": "A fracture in which the bone fragments communicate to the outside through an open wound is called a Compound (Open) fracture.",
        "Pathogenesis_Deep": "Fractures are broadly classified by their relationship to the external environment. (1) Simple (Closed) fracture: The skin remains intact; the fracture hematoma is sterile. (2) Compound (Open) fracture: The skin and soft tissues are breached, allowing direct communication between the fracture site and the contaminated external environment. The bone may have pierced the skin from the inside out (Grade I), or external trauma may have destroyed the skin down to the bone (Grade II/III). Compound fractures are severe emergencies because bacterial contamination of the bone leads to osteomyelitis, which drastically impairs bone healing.",
        "Why_Not": "Comminuted means shattered into multiple pieces. Greenstick means an incomplete fracture in young, flexible bone. Compound specifically designates the open skin wound.",
        "Wow_Approach": "The immediate first aid for a compound fracture is NOT to push the dirty exposed bone back inside the skin—doing so pulls massive environmental contamination deep into the muscle planes. Simply cover the exposed bone with sterile, moist dressings and stabilize the limb for transport."
    },
    2637: {
        "topic": "External Coaptation - Splints and Casts",
        "Core_Anatomy": "Appendicular skeleton.",
        "Pathogenesis_Immediate": "External coaptation technique involves the use of splints, casts, or bandages applied to the OUTSIDE of the limb to stabilize a fracture.",
        "Pathogenesis_Deep": "Fracture stabilization techniques are divided into: (1) External Coaptation: Non-surgical stabilization using Plaster of Paris casts, fiberglass casts, Thomas splints, or Robert-Jones bandages. These rely on external rigidity to immobilize the joints above and below the fracture. They are only suitable for closed fractures below the elbow/stifle. (2) Internal Fixation (ORIF): Surgical implantation of plates, screws, or intramedullary pins directly onto the bone. (3) External Skeletal Fixation (ESF): Pins driven through the skin into the bone, connected to a rigid external frame.",
        "Why_Not": "Internal fixation involves surgical plates/screws inside the body. External coaptation is completely non-invasive.",
        "Wow_Approach": "The cardinal rule of external coaptation: A cast MUST immobilize the joint PROXIMAL to the fracture and the joint DISTAL to the fracture. Therefore, a femoral fracture can NEVER be casted, because you cannot immobilize the hip joint with a standard limb cast."
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
