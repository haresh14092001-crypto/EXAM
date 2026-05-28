import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2878: {
        "topic": "Brain Cyst - Dermoid Cyst",
        "Core_Anatomy": "Central nervous system and neural tube.",
        "Pathogenesis_Immediate": "A congenital cyst present in the brain (or spinal cord) can be a Dermoid cyst.",
        "Pathogenesis_Deep": "Dermoid cysts (or dermoid sinuses) are congenital neural tube defects resulting from the incomplete separation of the skin (ectoderm) from the neural tube during embryonic development. They are classically seen in Rhodesian Ridgeback dogs (Dermoid Sinus). While typically found in the cervical/cranial thoracic spine, they can extend deep into the subarachnoid space and dura mater. Intracranial dermoid cysts can cause severe neurological deficits and recurrent meningitis as the hair and sebum produced by the cyst wall irritate the CNS.",
        "Why_Not": "A Meibomian cyst (chalazion) is strictly on the eyelid margin. A true parasitic cyst in the ruminant brain is Coenurus cerebralis (Gid).",
        "Wow_Approach": "Surgical excision of a dermoid sinus in a Ridgeback requires meticulous dissection all the way down to the spinal cord. If even a microscopic piece of the epithelial lining is left behind, the cyst will inevitably recur."
    },
    2879: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the start of a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2887: {
        "topic": "True or False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a True or False evaluation section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2895: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching question block.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2896: {
        "topic": "Hare Lip - Cheiloschisis",
        "Core_Anatomy": "Maxilla and Lips (Primary palate).",
        "Pathogenesis_Immediate": "Hare lip (Cheiloschisis) is a congenital cleft of the upper lip.",
        "Pathogenesis_Deep": "It results from the failure of the maxillary and medial nasal processes to fuse during embryonic development. It must be repaired surgically via a Cheiloplasty once the neonate is old enough to undergo anaesthesia safely.",
        "Why_Not": "Split jaw usually refers to a traumatic mandibular symphyseal separation. Parrot mouth refers to an overbite (brachygnathism).",
        "Wow_Approach": "N/A"
    },
    2897: {
        "topic": "Split Jaw",
        "Core_Anatomy": "Mandibular symphysis.",
        "Pathogenesis_Immediate": "A 'Split Jaw' typically refers to a traumatic Mandibular Symphyseal Separation.",
        "Pathogenesis_Deep": "The mandibular symphysis is the fibrous joint connecting the two halves of the lower jaw in cats and dogs. When a cat falls from a height ('high-rise syndrome'), the impact on the chin forcefully splits the symphysis in half. It is easily repaired using a figure-of-8 orthopedic wire passed around the canine teeth to hold the two mandibles together until the fibrous joint heals (usually 4-6 weeks).",
        "Why_Not": "Parrot mouth is a congenital overbite. Hare lip is a congenital lip cleft. Split jaw is a traumatic injury.",
        "Wow_Approach": "During the wiring procedure, a large gauge needle (like a 14G IV catheter) is passed through the skin behind the canine teeth to act as a guide for threading the cerclage wire, minimizing trauma to the gums."
    },
    2898: {
        "topic": "Lampas",
        "Core_Anatomy": "Hard palate (Equine).",
        "Pathogenesis_Immediate": "Lampas is the inflammation and swelling of the mucous membrane of the hard palate (palatine ridges) just behind the upper incisors in young horses.",
        "Pathogenesis_Deep": "It is a physiologic, temporary condition most commonly seen in young horses (2-3 years old) during the eruption of their permanent incisors. The palatine ridges swell down below the level of the incisor teeth, sometimes making eating mildly painful. Historically, ignorant farriers would surgically burn or cut this swollen tissue out. Modern veterinary medicine recognizes that this requires ZERO treatment and resolves spontaneously once the teeth finish erupting.",
        "Why_Not": "It is not a tumor or a congenital defect; it is physiological teething inflammation.",
        "Wow_Approach": "Never lance or burn a lampas. The palatine artery runs directly underneath this tissue; aggressive 'treatment' by laymen often results in massive, difficult-to-control arterial hemorrhage."
    },
    2913: {
        "topic": "VSR Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of a Veterinary Surgery and Radiology paper.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2914: {
        "topic": "VSR Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the Veterinary Surgery and Radiology section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2916: {
        "topic": "Choose the Correct Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for a 20-mark multiple choice section.",
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
print(f"Batch 4/5 DONE: Updated {updated} questions.")
