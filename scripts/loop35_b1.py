import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3930: {
        "topic": "Ultraviolet Radiation Wavelength",
        "Core_Anatomy": "Physical therapy modalities.",
        "Pathogenesis_Immediate": "The wavelength of therapeutic Ultraviolet (UV) waves is between 2000 and 4000 Angstroms (200-400 nm).",
        "Pathogenesis_Deep": "Therapeutic UV radiation is divided into UV-A (3150-4000 A), UV-B (2800-3150 A), and UV-C (2000-2800 A). UV-C has extremely potent bactericidal properties, directly destroying bacterial DNA, and is used to sterilize superficial chronic wounds and ulcers.",
        "Why_Not": "Wavelengths >4000 Angstroms represent visible violet light and have no significant photochemical or bactericidal effects.",
        "Wow_Approach": "N/A"
    },
    3931: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3932: {
        "topic": "Cherry Eye (Third Eyelid Gland Prolapse)",
        "Core_Anatomy": "Eye (Nictitating membrane / Third Eyelid).",
        "Pathogenesis_Immediate": "Cherry Eye is the clinical term for the congenital prolapse or hypertrophy of the gland of the third eyelid.",
        "Pathogenesis_Deep": "The gland of the third eyelid produces about 30-50% of the tear film's aqueous portion. In predisposed breeds (Cocker Spaniels, Bulldogs), the fibrous attachment securing the gland to the orbital rim is congenitally weak or absent. The gland pops out (prolapses) and appears as a bright red, swollen, cherry-like mass in the medial canthus of the eye, where it undergoes chronic drying and inflammation.",
        "Why_Not": "The gland must NEVER be surgically excised or cut off. Doing so drastically reduces tear production, predisposing the dog to severe, permanent Dry Eye (Keratoconjunctivitis Sicca - KCS) later in life.",
        "Wow_Approach": "The standard surgical cure is the Morgan Pocket Technique, where a pocket is surgically incised in the conjunctiva on the inner surface of the nictitans, the gland is tucked back inside, and the pocket is sutured closed, preserving tear function."
    },
    3933: {
        "topic": "Oesophagotomy",
        "Core_Anatomy": "Oesophagus.",
        "Pathogenesis_Immediate": "Oesophagotomy is the surgical incision into the lumen of the oesophagus.",
        "Pathogenesis_Deep": "This procedure is primarily performed to retrieve sharp, wedged foreign bodies (like bones or toys) that cannot be retrieved endoscopically. The oesophagus has no serosal layer and a very poor segmental blood supply, making healing exceptionally difficult and heavily predisposing it to post-surgical leakage, stricture, or fatal mediastinitis.",
        "Why_Not": "Enterotomy is an incision into the small intestine. Gastrotomy is into the stomach.",
        "Wow_Approach": "Because the oesophagus lacks a serosa (which normally seals incisions within hours in the abdomen), the closure MUST be performed in two distinct layers, with the mucosal layer closed using an inverting or simple interrupted pattern with the knots tied inside the lumen."
    },
    3934: {
        "topic": "Hydroquinone - X-Ray Developer",
        "Core_Anatomy": "Diagnostic Imaging.",
        "Pathogenesis_Immediate": "Hydroquinone is a critical chemical used as the primary reducing (developing) agent in manual X-ray film development.",
        "Pathogenesis_Deep": "During film exposure, silver halide crystals in the emulsion that were hit by X-ray photons form a latent image. When the film is placed in the developer, Hydroquinone acts as a reducing agent, donating electrons to convert the exposed, sensitized silver ions into black, metallic silver, creating the black parts of the image.",
        "Why_Not": "Ammonium thiosulfate is the fixer agent, which washes away the unexposed silver crystals, not the developer.",
        "Wow_Approach": "N/A"
    },
    3942: {
        "topic": "Subjective Type Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting a subjective (Define/Explain) section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3945: {
        "topic": "Ringbone (Review)",
        "Core_Anatomy": "Interphalangeal joints.",
        "Pathogenesis_Immediate": "Exostosis on the phalangeal bones is called Ringbone.",
        "Pathogenesis_Deep": "Reiterating that this is chronic osteoarthritis of the proximal (High) or distal (Low) interphalangeal joints.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3953: {
        "topic": "Choose the Correct Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3954: {
        "topic": "Double Breasting Sutures - Hernia (Review)",
        "Core_Anatomy": "Abdominal wall fascia.",
        "Pathogenesis_Immediate": "Double breasting (overlapping) sutures are classically applied to close a Hernial Ring.",
        "Pathogenesis_Deep": "Reiterating the overlapping 'vest-over-pants' configuration to provide a secure, double-layered fascial closure.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3955: {
        "topic": "Laparotomy Indications",
        "Core_Anatomy": "Abdominal cavity.",
        "Pathogenesis_Immediate": "Laparotomy (incising the abdominal wall) is performed for intestinal obstruction, diaphragmatic hernia, and Caesarean section.",
        "Pathogenesis_Deep": "Laparotomy (or celiotomy) is the basic entry portal for any surgical intervention inside the abdominal cavity, providing exposure to the viscera.",
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
print(f"Batch 1/5 DONE: Updated {updated} questions.")
