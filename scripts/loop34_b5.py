import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3922: {
        "topic": "Discovery of X-Rays",
        "Core_Anatomy": "Diagnostic Imaging.",
        "Pathogenesis_Immediate": "X-rays were discovered by Wilhelm Conrad Roentgen in 1895.",
        "Pathogenesis_Deep": "Roentgen discovered X-rays while experimenting with cathode ray tubes in a dark room. He noticed a nearby barium platinocyanide screen fluorescing, leading to the discovery of this highly penetrating electromagnetic radiation.",
        "Why_Not": "Lister is the father of antiseptic surgery. Eberlin is not associated with the primary discovery of X-rays.",
        "Wow_Approach": "N/A"
    },
    3923: {
        "topic": "Potter-Bucky Diaphragm",
        "Core_Anatomy": "Diagnostic Imaging.",
        "Pathogenesis_Immediate": "The Potter-Bucky Diaphragm indicates a Moving Grid assembly in radiography.",
        "Pathogenesis_Deep": "A radiographic grid is placed between the patient and the film to absorb scattered radiation, improving image contrast. However, a stationary grid leaves visible white grid lines on the film. The Potter-Bucky diaphragm actively moves (vibrates) the grid perpendicular to the grid lines during the exposure, completely blurring out the grid lines while still successfully absorbing scatter.",
        "Why_Not": "A stationary focused grid does not move, leaving thin grid lines visible on the final radiograph.",
        "Wow_Approach": "N/A"
    },
    3924: {
        "topic": "Stationary Anode - Low Output Machines",
        "Core_Anatomy": "Diagnostic Imaging.",
        "Pathogenesis_Immediate": "A Stationary Anode is used in X-ray machines of low mA output (portable, dental, or veterinary field units).",
        "Pathogenesis_Deep": "In an X-ray tube, 99% of electron kinetic energy is converted into heat, and only 1% into X-rays. High-output machines (high mA) generate massive heat that would instantly melt a stationary target. They require a rotating anode to spin the target disk and distribute the heat. Low-output machines (low mA, typically portable units) generate far less heat, allowing the use of a simpler, cheaper stationary tungsten target embedded in a copper block for heat dissipation.",
        "Why_Not": "High mA and high kVp machines generate extreme heat that absolutely mandates a rotating anode to prevent tube failure.",
        "Wow_Approach": "N/A"
    },
    3925: {
        "topic": "Tungsten Target - X-Ray Tube",
        "Core_Anatomy": "Diagnostic Imaging.",
        "Pathogenesis_Immediate": "Tungsten is used as the target material in X-ray tubes primarily because of its exceptionally high melting point.",
        "Pathogenesis_Deep": "Tungsten has an extremely high atomic number (Z=74) which ensures highly efficient conversion of electron energy into X-rays (Bremsstrahlung). More critically, it has an incredibly high melting point of 3422°C and high thermal conductivity, allowing it to withstand the focal electron bombardment without melting or vaporizing.",
        "Why_Not": "A low melting point metal would vaporize instantly during the very first high-output exposure, destroying the vacuum inside the tube.",
        "Wow_Approach": "N/A"
    },
    3926: {
        "topic": "X-Ray Penetration - Wavelength",
        "Core_Anatomy": "Diagnostic Imaging.",
        "Pathogenesis_Immediate": "The penetration power of X-rays is directly dependent on its Wavelength.",
        "Pathogenesis_Deep": "X-rays are high-frequency electromagnetic waves. Their energy (and therefore penetration power) is inversely proportional to their wavelength. Shorter wavelengths represent higher energy photons (often called 'hard' X-rays), which easily pierce dense structures. Longer wavelengths represent lower energy ('soft') X-rays, which are easily absorbed by the skin.",
        "Why_Not": "Speed is a constant—all electromagnetic waves (including X-rays) travel at the speed of light in a vacuum.",
        "Wow_Approach": "N/A"
    },
    3927: {
        "topic": "X-Ray Tube Current (mA)",
        "Core_Anatomy": "Diagnostic Imaging.",
        "Pathogenesis_Immediate": "The milliampere (mA) setting in an X-ray machine controls the tubular current (flow of electrons).",
        "Pathogenesis_Deep": "Increasing the mA increases the heating of the tungsten filament in the cathode. This releases a larger cloud of electrons via thermionic emission. When the high voltage is applied, a larger quantity of electrons flows to the anode, resulting in a higher number (quantity) of X-ray photons produced, directly affecting image density (blackness).",
        "Why_Not": "Potential difference is controlled by kVp, which determines energy/quality, not tube current quantity.",
        "Wow_Approach": "N/A"
    },
    3928: {
        "topic": "Excretory Urography (Pyelography)",
        "Core_Anatomy": "Kidneys and Ureters.",
        "Pathogenesis_Immediate": "A contrast radiographic study of the ureters and renal pelvis is called Pyelography (Excretory Urography).",
        "Pathogenesis_Deep": "An organic iodine contrast medium is injected intravenously. The kidneys rapidly filter and excrete the contrast. As it travels down the collecting ducts, it highlights the renal pelvis, diverticula, and ureters, allowing the diagnosis of ectopic ureters, hydronephrosis, or ureteral calculi.",
        "Why_Not": "Cystography is contrast study of the bladder. Myelography is contrast study of the spinal cord.",
        "Wow_Approach": "N/A"
    },
    3929: {
        "topic": "Double Contrast Cystography",
        "Core_Anatomy": "Urinary Bladder.",
        "Pathogenesis_Immediate": "A double contrast radiography is most commonly performed in the Bladder (Double Contrast Cystography).",
        "Pathogenesis_Deep": "Double contrast cystography involves infusing a small amount of positive contrast (liquid organic iodine) to coat the bladder mucosa, followed by a large volume of negative contrast (air or carbon dioxide) to distend the bladder. This provides stunning mucosal detail, allowing the clinician to easily see bladder wall thickening, polyps, radiolucent uroliths (like cystine or urate), or transitional cell carcinoma.",
        "Why_Not": "Solid parenchymal organs like the liver or heart cannot be hollow-distended, making double contrast studies impossible.",
        "Wow_Approach": "Using Carbon Dioxide (CO2) is highly preferred over room air. If room air is used and there is severe mucosal bleeding, the air can enter the blood vessels causing a fatal venous air embolism. CO2 is 20 times more soluble in blood and is safely absorbed."
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

# Final validation
with open(db_path, "r", encoding="utf-8") as f:
    c2 = f.read()
d2 = json.loads(re.sub(r'^.*?const examData = ', '', c2, flags=re.DOTALL).rsplit(';',1)[0].strip())
empty2 = [x for x in d2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
