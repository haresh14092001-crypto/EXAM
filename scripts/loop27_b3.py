import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3113: {
        "topic": "Lignocaine Duration of Action",
        "Core_Anatomy": "Peripheral nerves.",
        "Pathogenesis_Immediate": "The local analgesic effect of Lignocaine (Lidocaine) typically lasts for 45 minutes to 1 hour.",
        "Pathogenesis_Deep": "Lidocaine is a fast-onset, short-acting amide local anesthetic. It works by blocking voltage-gated sodium channels on the nerve axon, preventing depolarization. Because it is a potent vasodilator, it rapidly absorbs into the systemic circulation and is carried away from the injection site, limiting its duration of action to roughly 60 minutes.",
        "Why_Not": "Bupivacaine (Marcaine) is highly lipophilic and binds tightly to the sodium channels, providing much longer analgesia (up to 4-6 hours), making it superior for post-operative pain control.",
        "Wow_Approach": "To double the duration of Lidocaine (up to 2 hours), it is often formulated with 1:100,000 Epinephrine. The epinephrine causes intense local vasoconstriction, trapping the lidocaine at the injection site so it cannot be absorbed into the bloodstream."
    },
    3114: {
        "topic": "Opioid Analgesic - Butorphanol",
        "Core_Anatomy": "Central nervous system (Kappa/Mu receptors).",
        "Pathogenesis_Immediate": "An example of a narcotic opioid analgesic/sedative from the given options is Butorphanol.",
        "Pathogenesis_Deep": "Butorphanol (Torbugesic) is a synthetic opioid. Specifically, it is a Kappa-agonist and Mu-antagonist. Because it only stimulates the Kappa receptors, it provides mild to moderate visceral analgesia and excellent sedation, but has a 'ceiling effect' (giving more drug does not increase the pain relief). It is universally used in equine and small animal premedication.",
        "Why_Not": "Thiopentone and Phenobarbital are barbiturates. Chloral hydrate is an older sedative/hypnotic. Butorphanol is the only opioid.",
        "Wow_Approach": "Because Butorphanol is a Mu-antagonist, if you give it to a dog that is currently experiencing severe pain and being maintained on a pure Mu-agonist (like Fentanyl or Morphine), the Butorphanol will knock the Fentanyl off the receptors, instantly REVERSING the heavy pain control and causing the dog to wake up in agony."
    },
    3115: {
        "topic": "Skin Suture Material - Polyamide (Nylon)",
        "Core_Anatomy": "Skin epidermis and dermis.",
        "Pathogenesis_Immediate": "The ideal suture material for skin closure is Polyamide (Nylon).",
        "Pathogenesis_Deep": "Skin is heavily contaminated with environmental bacteria. Therefore, the ideal skin suture must be Non-Absorbable (so it doesn't break down prematurely before the skin heals) and Monofilament (so bacteria cannot hide inside it and wick deep into the wound). Polyamide (Nylon) and Polypropylene (Prolene) perfectly fit this criteria. They are chemically inert, causing almost zero tissue reaction.",
        "Why_Not": "Catgut and Collagen are highly reactive natural absorbable sutures; they will cause severe inflammation if left in the skin. Braided silk will wick bacteria directly into the wound, causing stitch abscesses.",
        "Wow_Approach": "Because Nylon is so smooth and has high 'memory', the knots can slip easily. You must always place at least four or five square throws on a Nylon skin suture to prevent the animal from licking the knot untied."
    },
    3116: {
        "topic": "Tissue Drag",
        "Core_Anatomy": "Surgical wound interface.",
        "Pathogenesis_Immediate": "The mechanical damage caused to the tissue as a suture is pulled through it is called Tissue Drag.",
        "Pathogenesis_Deep": "Tissue drag is the friction generated between the suture strand and the surrounding cells. High tissue drag acts like a microscopic saw, cutting the tissue and increasing inflammation. Multifilament (braided) sutures like Silk or Vicryl have very high tissue drag because of their rough, twisted surface. Monofilaments (like PDS or Nylon) have a perfectly smooth surface, resulting in zero tissue drag.",
        "Why_Not": "Manufacturers coat braided sutures (e.g., Polyglactin 910 coated with calcium stearate) specifically to reduce this tissue drag.",
        "Wow_Approach": "N/A"
    },
    3118: {
        "topic": "Spinal Cord Imaging - MRI",
        "Core_Anatomy": "Spinal cord and CNS.",
        "Pathogenesis_Immediate": "The ideal imaging method for evaluating the spinal cord (CNS parenchyma) is MRI (Magnetic Resonance Imaging).",
        "Pathogenesis_Deep": "While radiographs (X-rays) are excellent for bone, they cannot differentiate between soft tissues of similar density (like the spinal cord, CSF, and intervertebral discs). MRI uses magnetic fields and radio frequencies to provide exquisite, high-contrast detail of soft tissues. It is the gold standard for diagnosing spinal cord tumors, syringomyelia, and fibrocartilaginous embolisms (FCE).",
        "Why_Not": "A CT scan is excellent for complex bone fractures but is inferior to MRI for visualizing the actual gray and white matter of the spinal cord.",
        "Wow_Approach": "Before MRI became widely available, veterinarians had to perform Myelography (injecting iodine contrast directly into the subarachnoid space around the spinal cord) and taking an X-ray to indirectly look for spinal compressions. Myelograms carry a high risk of causing seizures."
    },
    3119: {
        "topic": "CT Scan Fundamentals",
        "Core_Anatomy": "Diagnostic imaging physics.",
        "Pathogenesis_Immediate": "This line represents an OCR artifact mixing options (Ultrasound, X-ray, CT, MRI) with a question about CT scan image composition.",
        "Pathogenesis_Deep": "Computed Tomography (CT) uses a rotating X-ray tube to take hundreds of cross-sectional images (slices) of the patient, which a computer then reconstructs into a 3D model.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3120: {
        "topic": "CT Image Element - Voxel",
        "Core_Anatomy": "Diagnostic imaging physics.",
        "Pathogenesis_Immediate": "In a CT scan, the 3D volume elements of the tissue represented by the computer are called Voxels.",
        "Pathogenesis_Deep": "A standard digital photograph is made of 2D squares called Pixels (Picture Elements). Because a CT scan represents a 3-dimensional slice of tissue (having length, width, and depth/slice thickness), the data points are 3-dimensional cubes called Voxels (Volume Elements). The computer assigns a Hounsfield Unit (density value) to every single voxel to construct the final image.",
        "Why_Not": "Pixels are 2D. Voxels are 3D.",
        "Wow_Approach": "N/A"
    },
    3121: {
        "topic": "Yoke Gall - Bullocks",
        "Core_Anatomy": "Dorsal neck and shoulder (Skin/Subcutis).",
        "Pathogenesis_Immediate": "Acute inflammation of the skin and subcutis on the dorsal neck of a working bullock due to friction is called a Yoke Gall.",
        "Pathogenesis_Deep": "Working draught cattle (bullocks) pull heavy loads using a wooden yoke placed across their dorsal neck. If the yoke is poorly fitted, the constant, massive mechanical friction causes acute severe dermatitis and subcutaneous bursitis. This is a Yoke Gall. If ignored, the continuous trauma causes the tissue to undergo fibrous hyperplasia, forming a massive, hard, permanent scar tissue mass (Yoke Tumor).",
        "Why_Not": "An abscess is filled with pus. A cyst is fluid-filled. A fistula is a draining tract. A gall is specifically friction-induced inflammation.",
        "Wow_Approach": "Treating a Yoke Gall medically is useless if the farmer puts the same poorly fitting wooden yoke back on the bullock the next day. Rest and padding are the only cures."
    },
    3122: {
        "topic": "Oxygen Cylinder Pressure",
        "Core_Anatomy": "Anaesthetic machine.",
        "Pathogenesis_Immediate": "The internal pressure of a full, standard Medical Oxygen cylinder (E-tank or H-tank) is 2200 psi.",
        "Pathogenesis_Deep": "Oxygen is stored as a compressed GAS, not a liquid, inside the standard high-pressure cylinders. A completely full cylinder reads ~2000 to 2200 pounds per square inch (psi) on the pressure gauge. Because it is a gas, the pressure drops completely linearly as the tank empties. If the gauge reads 1100 psi, the tank is exactly half full.",
        "Why_Not": "Nitrous oxide (N2O) is stored as a LIQUID under pressure. Its gauge will read 750 psi and will stay at exactly 750 psi until every drop of liquid has boiled away, at which point it drops to zero almost instantly.",
        "Wow_Approach": "If an unsecured 2200 psi H-tank is knocked over and the valve snaps off, the tank becomes an unguided missile capable of punching straight through a cinderblock wall."
    },
    3123: {
        "topic": "Viborg's Triangle Confirmation",
        "Core_Anatomy": "Equine Head and Neck.",
        "Pathogenesis_Immediate": "Viborg's triangle is the primary landmark for safely draining pus from the guttural pouch in horses.",
        "Pathogenesis_Deep": "The triangle is bordered by: (1) Cranially: the vertical ramus of the mandible. (2) Dorsally: the tendon of insertion of the sternocephalicus muscle. (3) Ventrally: the linguofacial vein. The surgeon incises exactly in the center of this triangle to avoid severing the carotid arteries or jugular vein while accessing the distended guttural pouch.",
        "Why_Not": "Zygomatic and Temporal triangles are made-up distractors.",
        "Wow_Approach": "Before cutting into Viborg's triangle, you must ensure the horse's head is extended. If the head is flexed, the anatomical borders shift, and you risk cutting the linguofacial vein."
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
