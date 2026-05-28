import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2493: {
        "topic": "Inhalant Anaesthesia - Fastest Recovery",
        "Core_Anatomy": "Pulmonary alveoli and blood-gas partition coefficient.",
        "Pathogenesis_Immediate": "Recovery is fastest with Inhalant anaesthesia.",
        "Pathogenesis_Deep": "Recovery from inhalation anaesthesia is directly controlled by ventilation—the animal simply breathes out the anaesthetic agent. Agents with low blood-gas solubility (like Sevoflurane: blood-gas partition coefficient = 0.69; Isoflurane = 1.4) equilibrate rapidly between blood and alveoli, allowing extremely fast elimination and quick return of consciousness when the vaporizer is turned off. By contrast, IV anaesthetics (barbiturates, ketamine) must be metabolized and excreted by the liver/kidneys, which takes much longer.",
        "Why_Not": "Intravenous anaesthesia recovery depends on hepatic metabolism and renal excretion (slower). Regional and infiltration anaesthesia recoveries depend on drug redistribution from nerve tissue—typically 1-4 hours.",
        "Wow_Approach": "The practical clinical implication: if an inhalant-anaesthetised animal is experiencing a complication, simply increasing the O2 flow and turning off the vaporizer allows the surgeon to lighten anaesthetic depth within minutes—something impossible with an IV overdose."
    },
    2494: {
        "topic": "Wound Cleaning - Potassium Permanganate Concentration",
        "Core_Anatomy": "Wound surface and bacteria.",
        "Pathogenesis_Immediate": "The concentration of Potassium Permanganate (KMnO4) solution used for cleaning wounds is 1% (1 in 1000 solution).",
        "Pathogenesis_Deep": "Potassium Permanganate is a powerful oxidising agent. At 1% concentration, it rapidly oxidises and destroys bacterial cell components by releasing nascent oxygen. It is particularly effective against anaerobic bacteria (like Clostridium spp. in gangrenous wounds) because the released oxygen creates an aerobic environment hostile to obligate anaerobes. At higher concentrations (>5%), it becomes severely caustic and damages healthy tissue, causing chemical burns.",
        "Why_Not": "10% is far too caustic (causes chemical burns to wound tissue). 5% and 3% are also excessively concentrated for wound lavage. Only 1% is safe and effective for wound cleaning.",
        "Wow_Approach": "KMnO4 is also used for treating foot rot in sheep/cattle as a 1-2% hoof-soaking bath—the released oxygen destroys the anaerobic Dichelobacter nodosus and Fusobacterium necrophorum responsible for the necrotic interdigital lesions."
    },
    2495: {
        "topic": "X-ray Film Storage Conditions",
        "Core_Anatomy": "Silver halide film emulsion.",
        "Pathogenesis_Immediate": "X-ray films should be stored in a Cool and Dry location.",
        "Pathogenesis_Deep": "X-ray film emulsion contains silver halide crystals suspended in gelatin. Improper storage causes: (1) Heat: accelerates chemical reactions, causing fogging (overall darkening) of unexposed film. (2) Humidity/moisture: the gelatin absorbs moisture, causing adjacent films to stick together and the emulsion to swell, distort, and degrade. (3) Chemical fumes: solvents, fixatives, and reducing agents can chemically fog the film. Cool (<21°C), dry (<50% relative humidity), and light-tight storage in upright boxes (not horizontal stacking, which compresses the emulsion) is mandatory.",
        "Why_Not": "Hot and humid conditions are the worst possible storage: heat causes gelatin swelling and chemical fog, while humidity causes emulsion adhesion and physical damage.",
        "Wow_Approach": "Unexposed X-ray film is date-stamped with an expiry date—beyond this date, background radioactivity and chemical fog accumulate, reducing image quality even without any X-ray exposure. Always use the oldest film first (FEFO)."
    },
    2496: {
        "topic": "Double Contrast Radiography - Lumen and Contour",
        "Core_Anatomy": "Hollow organ (stomach, bladder, colon).",
        "Pathogenesis_Immediate": "To study BOTH the lumen AND the contour of hollow organs, Double Contrast Radiography is employed.",
        "Pathogenesis_Deep": "Double contrast radiography uses BOTH a positive contrast agent (iodinated solution = radiopaque, coating the mucosal surface) AND a negative contrast agent (air or CO2 = radiolucent, filling the lumen). The positive contrast coats the mucosa like paint, beautifully outlining mucosal folds, ulcers, and tumors. The air then distends and outlines the lumen size and shape. This technique provides superior mucosal detail compared to single contrast studies—essential for diagnosing small mucosal lesions (early ulcers, polyps) that would be obscured in a lumen filled only with contrast solution.",
        "Why_Not": "Single positive contrast shows the lumen but obscures mucosal detail. Single negative (pneumo) contrast shows the organ contour but misses mucosal lesions. Only double contrast shows both simultaneously.",
        "Wow_Approach": "In dogs, double contrast cystography is the gold standard for diagnosing cystic calculi (stones appear as filling defects floating in the air column against the contrast-coated bladder wall) and transitional cell carcinoma (irregular mucosal thickening)."
    },
    2497: {
        "topic": "Hypovolemic Shock - Ringer's Lactate",
        "Core_Anatomy": "Systemic vasculature and interstitial fluid compartment.",
        "Pathogenesis_Immediate": "The most versatile crystalloid solution for treating hypovolemic shock is Ringer's Lactate (Hartmann's Solution).",
        "Pathogenesis_Deep": "Ringer's Lactate is a balanced, isotonic crystalloid solution containing Na⁺, K⁺, Ca²⁺, Cl⁻, and lactate. It closely mirrors the electrolyte composition of plasma and is rapidly distributed throughout the extracellular fluid compartment. Its key advantages: (1) Does not cause hyperchloremic metabolic acidosis (unlike normal saline which causes dilutional acidosis from excess Cl⁻). (2) Lactate is metabolized by the liver to bicarbonate, providing mild buffering. (3) The balanced electrolyte composition prevents dangerous hyperkalemia and hyponatremia.",
        "Why_Not": "Normal saline causes hyperchloremic metabolic acidosis when given in large volumes. Dextrose solutions are hypotonic and distribute throughout total body water (not just intravascular space), making them ineffective for volume expansion. Dextrose/saline is used for maintenance, not resuscitation.",
        "Wow_Approach": "The classic surgical teaching: 'Normal saline is the WORST resuscitation fluid for shock'—administering 5L of normal saline causes severe hyperchloremic acidosis, coagulopathy ('dilutional coagulopathy'), and immune dysfunction. Ringer's Lactate or Plasma-Lyte A is always preferred."
    },
    2498: {
        "topic": "Surgery Match the Following Header",
        "Core_Anatomy": "Surgical anatomy and radiology.",
        "Pathogenesis_Immediate": "This section pairs surgical instruments, techniques, and radiographic terms with their specific definitions.",
        "Pathogenesis_Deep": "Key surgical pairs: Tamponade = controlling haemorrhage from body cavities; Potter-Bucky diaphragm = absorbs scatter radiation; Roentgen = unit of X-ray exposure; Positive contrast = iodinated solutions appearing white on X-ray.",
        "Why_Not": "Use process of elimination; anchor on the most certain pairs first to resolve ambiguous ones.",
        "Wow_Approach": "For radiographic matching: always distinguish contrast MEDIUM (the substance) from contrast TECHNIQUE (the procedure): Positive contrast medium = Barium/Iodine; Negative = Air/CO2; Technique = Cystography, Myelography, etc."
    },
    2499: {
        "topic": "Tamponade - Controlling Haemorrhage from Cavities",
        "Core_Anatomy": "Body cavities (abdominal, thoracic, uterine).",
        "Pathogenesis_Immediate": "Tamponade plugging is a surgical haemostasis technique matched to controlling bleeding from body cavities.",
        "Pathogenesis_Deep": "Surgical tamponade involves packing a body cavity (uterus, nasal cavity, thoracic wound, or abdominal incision site) with sterile gauze, sponges, or purpose-made haemostatic materials to apply direct pressure on bleeding vessels. This technique is particularly valuable when individual vessel ligation is impossible due to extensive, diffuse bleeding surfaces. In obstetrics, uterine tamponade with gauze rolls controls post-partum haemorrhage when oxytocin alone fails.",
        "Why_Not": "Tamponade absorbs blood and applies pressure to stop bleeding. Potter-Bucky diaphragm absorbs RADIATION, not blood. These two 'absorption' functions are completely different.",
        "Wow_Approach": "Modern haemostatic sponges (Gelfoam, Surgicel) use the same tamponade principle but also chemically promote platelet aggregation and fibrin polymerization at the bleeding surface, combining mechanical and chemical haemostasis."
    },
    2500: {
        "topic": "Roentgen - Unit of Radiation",
        "Core_Anatomy": "X-ray physics.",
        "Pathogenesis_Immediate": "Roentgen (R) is the unit of X-ray or gamma-ray exposure (radiation).",
        "Pathogenesis_Deep": "Wilhelm Conrad Roentgen discovered X-rays in 1895. The Roentgen unit (R) is an older unit of radiation EXPOSURE—defined as the amount of X-ray or gamma radiation that produces a specific amount of ionization in air (2.58 × 10⁻⁴ coulombs per kilogram of air). Modern radiation units: Absorbed dose = Gray (Gy); Biological effect = Sievert (Sv). For veterinary board purposes: Roentgen = unit of X-ray exposure.",
        "Why_Not": "Gray (Gy) measures absorbed radiation energy (energy per unit mass). Sievert (Sv) measures biological radiation dose equivalence. Roentgen is specifically the exposure unit.",
        "Wow_Approach": "Veterinary radiographers are legally limited to a maximum annual radiation dose of 20 mSv (millisieverts). This is enforced by wearing personal dosimeter badges (TLD/film badges) that are checked quarterly by radiation safety officers."
    },
    2502: {
        "topic": "Potter-Bucky Diaphragm - Absorbs Secondary Radiation",
        "Core_Anatomy": "X-ray scatter radiation.",
        "Pathogenesis_Immediate": "The Potter-Bucky Diaphragm (Grid) is specifically designed to Absorb secondary (scatter) radiation.",
        "Pathogenesis_Deep": "The Potter-Bucky diaphragm is a moving grid that oscillates continuously during exposure to prevent the lead grid lines from appearing on the film. It consists of alternating radiopaque lead strips (to absorb scatter) and radiolucent interspaces (to allow the primary beam through). Its movement blurs the lead strip shadows, making them invisible on the final image while maintaining superior image contrast by eliminating 60-90% of scattered radiation.",
        "Why_Not": "Positive contrast agents cause tissues to appear white (radiopaque). Steam-produced sterilization is autoclaving. Roentgen is a radiation unit. Only the Potter-Bucky diaphragm is specifically designed to absorb secondary scatter radiation.",
        "Wow_Approach": "The Grid Factor (GF) is the increased exposure needed when using a grid (to compensate for absorbed primary beam). A 12:1 grid requires 5x more exposure than gridless technique—this must be calculated before setting exposure parameters to avoid underexposed films."
    },
    2503: {
        "topic": "Povidone-Iodine - Blue Color",
        "Core_Anatomy": "Bacterial cell membrane and sulfhydryl proteins.",
        "Pathogenesis_Immediate": "Povidone-Iodine (Betadine) is matched to its characteristic dark Brown/Blue color.",
        "Pathogenesis_Deep": "Povidone-Iodine (PVP-I) is a complex of polyvinylpyrrolidone polymer with iodine. The polymer acts as a carrier, slowly releasing free iodine (I2) continuously. Free iodine is the active germicidal agent—it penetrates microbial cell walls and rapidly oxidizes and iodates essential sulfhydryl groups in structural proteins and enzymes. The characteristic brown-blue color indicates the bound iodine is present; as the iodine is consumed fighting bacteria, the solution turns colorless, signaling that the antiseptic activity is exhausted.",
        "Why_Not": "Chlorhexidine is colorless to faintly pink. Sodium hypochlorite (bleach) is also colorless. The distinctive dark brown color is pathognomonic for Povidone-Iodine.",
        "Wow_Approach": "Povidone-Iodine should NOT be used in deep puncture wounds—the organic matter in deep tissue inactivates the iodine very rapidly, providing false security while allowing anaerobic bacteria (Clostridium) to proliferate undisturbed."
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
