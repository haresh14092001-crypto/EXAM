import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2707: {
        "topic": "Ultrasound - B-Mode",
        "Core_Anatomy": "Diagnostic imaging physics.",
        "Pathogenesis_Immediate": "The mode most commonly used for diagnostic ultrasound scanning is B-Mode (Brightness Mode).",
        "Pathogenesis_Deep": "B-Mode ultrasound displays a two-dimensional, cross-sectional image of the tissue anatomy in real-time. The returning echoes are displayed as dots of varying brightness (hyperechoic = white, hypoechoic = dark grey, anechoic = black) based on the amplitude of the returning sound wave. This is the standard mode used for examining abdominal organs, pregnancy diagnosis, and echocardiography.",
        "Why_Not": "A-Mode (Amplitude mode) is a 1-D graph used mainly in ophthalmology for measuring eye length. M-Mode (Motion mode) is a 1-D tracing of moving structures over time, used specifically in echocardiography to measure heart valve/wall movement. B-Mode is the standard 2D image.",
        "Wow_Approach": "Fluid (urine, bile, cysts) appears anechoic (black) on B-Mode because it transmits sound waves perfectly without reflecting them back. Bone and gas reflect almost 100% of the sound, appearing bright white with a black 'acoustic shadow' underneath."
    },
    2718: {
        "topic": "VSR 421 - Regional Veterinary Surgery Header",
        "Core_Anatomy": "Regional surgical anatomy.",
        "Pathogenesis_Immediate": "Header denoting the objective section for Regional Veterinary Surgery (VSR 421).",
        "Pathogenesis_Deep": "Regional surgery applies general surgical principles to specific organ systems and anatomical locations.",
        "Why_Not": "Structural marker.",
        "Wow_Approach": "N/A"
    },
    2719: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Requires precise recall of surgical terminology.",
        "Why_Not": "Structural marker.",
        "Wow_Approach": "N/A"
    },
    2720: {
        "topic": "Aural Hematoma",
        "Core_Anatomy": "Auricular cartilage and skin.",
        "Pathogenesis_Immediate": "The collection of blood within the ear cartilage (between the cartilage and skin) is called an Aural Hematoma.",
        "Pathogenesis_Deep": "Aural hematomas usually result from violent head shaking or ear scratching secondary to otitis externa (ear mites, yeast, bacterial infection). The centrifugal force ruptures the small blood vessels passing through the auricular cartilage. Blood accumulates rapidly, separating the skin from the cartilage and creating a large, fluctuant swelling. If left untreated, the hematoma will eventually organize and contract, causing a severely deformed 'cauliflower ear'.",
        "Why_Not": "It is not a cyst (no epithelial lining) or an abscess (no pus initially). It is a hematoma.",
        "Wow_Approach": "Surgical repair requires incising and draining the hematoma, then placing multiple through-and-through mattress sutures parallel to the blood vessels to securely tack the skin back down to the cartilage, eliminating the dead space."
    },
    2728: {
        "topic": "Choose the Best Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for the multiple-choice section.",
        "Pathogenesis_Deep": "Surgical MCQs testing specific anatomical landmarks.",
        "Why_Not": "Structural marker.",
        "Wow_Approach": "N/A"
    },
    2729: {
        "topic": "Carnassial Tooth Root Abscess (Pus in Antrum)",
        "Core_Anatomy": "Maxillary 4th premolar and maxillary sinus.",
        "Pathogenesis_Immediate": "Pus in the maxillary antrum (sinus) of a dog, frequently presenting as a draining tract below the eye, is classically caused by an affection of the 4th upper cheek tooth (the Maxillary 4th Premolar or Carnassial tooth).",
        "Pathogenesis_Deep": "The maxillary 4th premolar is the massive carnassial (shearing) tooth in dogs. Its three deep roots extend upward, lying immediately adjacent to (and sometimes penetrating) the maxillary sinus/nasal cavity. When this tooth fractures (slab fracture from chewing bones) or develops severe periodontal disease, bacteria track down the roots, forming a periapical abscess. Because the path of least resistance is outward, the abscess typically bursts through the maxillary bone and skin, creating a chronic draining tract just below the medial canthus of the eye.",
        "Why_Not": "The other cheek teeth roots do not sit directly beneath this specific area of the maxilla. The 4th upper premolar is the definitive anatomical culprit for infraorbital draining tracts.",
        "Wow_Approach": "Antibiotics will temporarily dry up the draining tract, but it will inevitably recur once the drugs are stopped. The only permanent cure is the surgical extraction of the massive 3-rooted 4th premolar tooth."
    },
    2730: {
        "topic": "Numerical Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "This appears to be an orphaned numerical option from a measurement question.",
        "Pathogenesis_Deep": "Recognizing distractors.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2731: {
        "topic": "Frontal Sinus Empyema - Horn Affection",
        "Core_Anatomy": "Frontal sinus and horn core (processus cornualis).",
        "Pathogenesis_Immediate": "Empyema (pus) of the frontal sinus in cattle is a direct complication of Horn affection (e.g., dehorning, horn fracture, or horn cancer).",
        "Pathogenesis_Deep": "In adult cattle, the frontal sinus is massive and extends directly into the core of the horn (the cornual diverticulum of the frontal sinus). Therefore, when an adult cow is dehorned, or if a horn breaks off traumatically, the frontal sinus is laid wide open to the external environment. Rain, dirt, and flies can easily enter the open sinus hole, causing a severe, foul-smelling suppurative sinusitis (empyema).",
        "Why_Not": "Tooth affections cause maxillary sinusitis. Nasal affections cause nasal cavity issues. Horn affections specifically open the frontal sinus.",
        "Wow_Approach": "To prevent this, dehorning should ideally be performed on young calves (disbudding) BEFORE the frontal sinus pneumatizes (hollows out) and extends into the horn bud. In adults, the open hole must be protected until granulation tissue seals it."
    },
    2732: {
        "topic": "Cherry Eye",
        "Core_Anatomy": "Gland of the Third Eyelid (Nictitating membrane).",
        "Pathogenesis_Immediate": "Cherry eye is the clinical term for the prolapse of the gland of the 3rd eyelid.",
        "Pathogenesis_Deep": "The third eyelid (nictitating membrane) contains an accessory lacrimal gland at its base, responsible for producing roughly 30-50% of the eye's aqueous tear film. In certain breeds (Bulldogs, Beagles, Mastiffs), the connective tissue anchoring this gland is weak. The gland prolapses (flips up and outward), appearing as a swollen, red, fleshy mass at the medial canthus of the eye (hence 'cherry eye').",
        "Why_Not": "It is not a prolapse of the conjunctiva, cornea, or sclera. It specifically involves the secretory gland of the 3rd eyelid.",
        "Wow_Approach": "NEVER surgically excise (cut out) a prolapsed cherry eye. Removing this gland drastically reduces tear production, predisposing the dog to severe 'Dry Eye' (Keratoconjunctivitis Sicca - KCS) later in life. The gland MUST be surgically repositioned (tucked back in) using a Morgan pocket technique."
    },
    2733: {
        "topic": "Viborg's Triangle - Guttural Pouch Approach",
        "Core_Anatomy": "Equine neck (Guttural Pouch).",
        "Pathogenesis_Immediate": "Viborg's triangle approach is used for surgical access to the Guttural pouch in horses.",
        "Pathogenesis_Deep": "As covered in the previous loop, Viborg's Triangle (bordered by the mandible, linguofacial vein, and sternocephalicus tendon) provides a safe surgical window to drain guttural pouch empyema while avoiding the critical cranial nerves and internal carotid artery.",
        "Why_Not": "Salivary mucoceles involve salivary glands. The cranial thoracic esophagus requires a cervical or thoracotomy approach. Viborg's is exclusively for the equine guttural pouch.",
        "Wow_Approach": "Repeated high-yield concept across exams—memorize the borders of Viborg's triangle: Cranial = angle of mandible; Ventral = linguofacial vein; Dorsocaudal = tendon of sternocephalicus."
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
