import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2478: {
        "topic": "Surgery Fill in the Blanks Header",
        "Core_Anatomy": "Surgical anatomy and wound healing.",
        "Pathogenesis_Immediate": "This fill-in-the-blank section tests precise recall of surgical principles, aseptic technique, and radiographic terminology.",
        "Pathogenesis_Deep": "Common surgical blanks: 'Potassium Permanganate wound concentration = 1%'; 'Cystography = radiographic study of bladder'; 'Boyle's apparatus = inhalation anaesthetic delivery'; 'Thiopentone = ultra-short-acting IV anaesthetic'.",
        "Why_Not": "Exact drug names and concentrations are required; generic descriptions are not accepted.",
        "Wow_Approach": "Surgical fill-in-the-blanks almost always test the CONCENTRATION of a specific solution (e.g., 1% KMnO4, 0.5% Chlorhexidine, 2% Lidocaine)—memorize these precisely."
    },
    2479: {
        "topic": "Aseptic Technique - Prevention of Surgical Infection",
        "Core_Anatomy": "Surgical wound and operating theatre environment.",
        "Pathogenesis_Immediate": "Rules of Aseptic technique must be followed to prevent surgical site infection (SSI) / wound sepsis.",
        "Pathogenesis_Deep": "Aseptic technique is the sum of all practices that prevent contamination of the sterile surgical field. Core principles: (1) Sterilization of all instruments and drapes (autoclave, ETO, or chemical sterilization). (2) Antiseptic preparation of the surgical site (clipping, scrubbing with Chlorhexidine or Povidone-Iodine, sterile draping). (3) Sterile surgical attire (gown, gloves, mask, cap). (4) Minimizing traffic in the theatre during surgery. (5) No talking or sneezing directly over the surgical field.",
        "Why_Not": "Disinfection kills most pathogens but not spores—sterilization achieves complete microbial destruction. Only sterilized instruments should contact the surgical field.",
        "Wow_Approach": "A common board exam trap: disinfection ≠ sterilization. Disinfection reduces pathogen load on surfaces. Sterilization eliminates ALL microbial life including spores. Surgical instruments require sterilization, NOT just disinfection."
    },
    2484: {
        "topic": "Cystography - Radiographic Study of Bladder",
        "Core_Anatomy": "Urinary bladder.",
        "Pathogenesis_Immediate": "The radiographic study of the bladder is called Cystography.",
        "Pathogenesis_Deep": "Cystography involves introducing a contrast medium (positive contrast = iodinated solution; negative contrast = air; double contrast = both) into the urinary bladder via a urinary catheter. It is used to diagnose: bladder rupture (contrast leaks into the peritoneal cavity), cystic calculi (filling defects within the contrast column), bladder wall thickening (cystitis, transitional cell carcinoma), and urethral obstruction. In cattle and horses, positive contrast cystography is particularly useful for identifying the site and extent of bladder rupture.",
        "Why_Not": "Intravenous Urography (IVU/excretory urography) visualizes the kidneys and ureters after IV contrast injection. Urethrostography visualizes the urethra. Only Cystography specifically targets the bladder.",
        "Wow_Approach": "In foals with suspected ruptured bladder (uroperitoneum), contrast cystography confirms the diagnosis faster than biochemistry—injecting methylene blue dye into the bladder and collecting peritoneal fluid; blue color confirms leakage."
    },
    2485: {
        "topic": "Boyle's Machine - Inhalation Anaesthetic Apparatus",
        "Core_Anatomy": "Pulmonary alveoli (inhalant agent absorption).",
        "Pathogenesis_Immediate": "The Boyle's Machine (Boyle's Apparatus) is the apparatus used for administering inhalation anaesthetics.",
        "Pathogenesis_Deep": "The Boyle's Machine is the classic continuous flow anaesthetic machine. It consists of: (1) Compressed gas cylinders (O2, N2O). (2) Pressure regulators and flowmeters (rotameters) to control gas flow. (3) A Vapouriser to volatilize liquid inhalant agents (Halothane, Isoflurane, Sevoflurane) into the gas stream. (4) A Breathing circuit (circle or non-rebreathing) with one-way valves and a CO2 absorbent (Soda-lime) to remove exhaled CO2. (5) A Rebreathing bag to buffer respiratory tidal volume.",
        "Why_Not": "Syringe drivers and infusion pumps are used for TIVA (Total Intravenous Anaesthesia) and are not Boyle's Machines. The Boyle's Machine is specifically an inhalant delivery system.",
        "Wow_Approach": "Modern Boyle's Machines use Isoflurane or Sevoflurane (replacing the older, hepatotoxic Halothane). The key safety principle: NEVER turn on the vaporizer without an adequate flow of carrier gas (O2)—doing so concentrates the anaesthetic in the circuit to dangerously fatal levels."
    },
    2487: {
        "topic": "Ultra-Short Acting IV Anaesthetic - Thiopentone",
        "Core_Anatomy": "Central nervous system (GABA-A receptors and reticular activating system).",
        "Pathogenesis_Immediate": "The classic example of an ultra-short-acting intravenous anaesthetic is Thiopentone Sodium (Sodium Thiopental).",
        "Pathogenesis_Deep": "Thiopentone is a highly lipid-soluble barbiturate. After IV injection, its extreme lipid solubility allows it to cross the blood-brain barrier within 30 seconds, causing rapid induction of unconsciousness (the 'single arm-brain circulation time'). However, because the body has such a large fat depot, the drug rapidly redistributes from the brain into skeletal muscle and then fat tissue, causing the animal to wake up within 10-15 minutes despite still having significant systemic thiopentone levels. This redistribution (NOT metabolism) causes its ultra-short action.",
        "Why_Not": "Ketamine is a dissociative anaesthetic with a longer action (20-30 min). Propofol is a short-acting (not ultra-short) IV anaesthetic. Thiopentone's ultra-short action is uniquely due to redistribution kinetics.",
        "Wow_Approach": "If thiopentone is re-administered repeatedly (multiple doses or CRI), it saturates the fat depots and loses its redistribution-based short action—each subsequent dose lasts longer than the last, risking dangerously prolonged deep anaesthesia."
    },
    2488: {
        "topic": "Eczema Treatment - UV Rays",
        "Core_Anatomy": "Skin epidermis and dermis.",
        "Pathogenesis_Immediate": "Eczema can be effectively treated by UV (Ultraviolet) rays using phototherapy.",
        "Pathogenesis_Deep": "Ultraviolet B (UVB) phototherapy is a well-established treatment for chronic inflammatory skin conditions including eczema (atopic dermatitis) and psoriasis. UVB rays penetrate the epidermis and have potent immunosuppressive effects: they deplete Langerhans cells (the skin's primary antigen-presenting cells), suppress local T-cell proliferation, and reduce pro-inflammatory cytokine production (IL-1, TNF-α). In veterinary medicine, UV therapy is occasionally used for localized chronic dermatitis in dogs and cats.",
        "Why_Not": "Infrared (IR) rays provide deep tissue heat therapy—used for muscle/joint conditions, NOT dermatological inflammatory conditions. VIBGYOR represents the visible light spectrum, not a medical treatment.",
        "Wow_Approach": "Excessive UV exposure also causes actinic (solar) keratosis and squamous cell carcinoma on depigmented skin in cattle and dogs—particularly on the white muzzle skin, eyelids, and periocular skin of Hereford cattle."
    },
    2489: {
        "topic": "Radiographic Grid - Tissue Thickness Indication",
        "Core_Anatomy": "X-ray physics and scatter radiation.",
        "Pathogenesis_Immediate": "A Grid is employed in radiography when tissue thickness exceeds >10 cm.",
        "Pathogenesis_Deep": "When X-rays pass through thick tissues (>10 cm), they undergo massive Compton scatter, producing secondary radiation that hits the X-ray film from random angles, reducing image contrast and sharpness dramatically. A Potter-Bucky Grid is placed between the patient and the cassette—it consists of alternating thin lead strips and radiolucent interspaces aligned with the primary beam. The grid absorbs the obliquely scattered secondary radiation while allowing the primary perpendicular beam through, dramatically improving image contrast and diagnostic quality.",
        "Why_Not": "For thin tissues (<10 cm, like extremities), the scatter radiation is minimal and a grid is unnecessary—it would just increase the required exposure (radiation dose) without improving image quality.",
        "Wow_Approach": "The Grid Ratio (height of lead strips / width of interspaces) determines efficiency: a 12:1 grid absorbs far more scatter than a 5:1 grid but requires much higher X-ray exposure settings to compensate for the absorbed primary beam."
    },
    2490: {
        "topic": "Haemorrhagic Shock - Treatment",
        "Core_Anatomy": "Systemic vasculature and circulating blood volume.",
        "Pathogenesis_Immediate": "The treatment of haemorrhagic shock requires a combination of all options: fluid therapy, blood transfusion, plasma transfusion, and oxygen therapy.",
        "Pathogenesis_Deep": "Haemorrhagic shock results from acute loss of circulating blood volume (whole blood). The immediate goals are: (1) Restore circulating volume: large-bore IV crystalloids (Ringer's Lactate) to expand intravascular space quickly. (2) Restore oxygen-carrying capacity: blood transfusion to replace lost RBCs. (3) Restore coagulation factors: fresh frozen plasma (FFP) or plasma transfusion. (4) Restore tissue oxygenation: intranasal or mask oxygen to maximize each surviving RBC's O2 carrying capacity.",
        "Why_Not": "Fluid therapy alone (without blood) may restore pressure but further dilutes the remaining RBCs, worsening tissue hypoxia. A comprehensive multi-component approach is required.",
        "Wow_Approach": "The critical clinical decision point in haemorrhagic shock is the 'shock index' (Heart Rate / Systolic Blood Pressure). A shock index >1 (e.g., HR 120/SBP 90 = 1.33) indicates class III-IV haemorrhagic shock requiring immediate blood transfusion, not just crystalloids."
    },
    2491: {
        "topic": "X-ray Film Development - Silver Reduction",
        "Core_Anatomy": "Silver halide crystals in the film emulsion.",
        "Pathogenesis_Immediate": "During X-ray film development, the exposed silver halide crystals are Reduced to metallic silver by the developer solution.",
        "Pathogenesis_Deep": "The X-ray film emulsion contains silver halide crystals (AgBr/AgI). When X-rays or light photons hit these crystals, they create a 'latent image' by liberating free electrons that reduce a tiny cluster of Ag⁺ ions to metallic silver (Ag⁰). During chemical development, the developer (hydroquinone + metol) amplifies this latent image by reducing all the silver ions in exposed crystals to black metallic silver. Unexposed crystals are then dissolved away by the fixer (sodium thiosulphate), leaving a clear background.",
        "Why_Not": "Silver is reduced (gains electrons) by the developer—it is NOT oxidized, converted to halide, or dissolved. The fixer removes unexposed silver halide, but the developer specifically REDUCES exposed crystals.",
        "Wow_Approach": "Digital radiography (DR and CR) has largely replaced film-screen systems, but the principle of 'silver reduction = black opacity' remains the conceptual basis for understanding X-ray image formation density."
    },
    2492: {
        "topic": "Xylazine + Barbiturate Interaction",
        "Core_Anatomy": "Central nervous system (sedation synergism).",
        "Pathogenesis_Immediate": "Xylazine pre-medication allows you to markedly Decrease the dose of barbiturates needed for anaesthetic induction.",
        "Pathogenesis_Deep": "Xylazine is a potent alpha-2 adrenoceptor agonist that causes profound sedation, muscle relaxation, and analgesia by reducing central norepinephrine release. When a barbiturate (Thiopentone) is administered after Xylazine pre-medication, the already-sedated CNS requires far less barbiturate to achieve surgical anaesthetic depth. This dose-sparing effect (up to 50-70% dose reduction) reduces barbiturate-related cardiovascular and respiratory depression, dramatically improving anaesthetic safety.",
        "Why_Not": "Pre-medication DECREASES (not increases) the required barbiturate dose. Failing to reduce the barbiturate dose after adequate pre-medication risks fatal barbiturate overdose.",
        "Wow_Approach": "This dose-sparing synergism is why 'balanced anaesthesia' (combining multiple agents at low doses) is far safer than using any single agent at full dose. The anaesthetic triad: sedation (Xylazine) + analgesia (Butorphanol/Buprenorphine) + muscle relaxation = dramatically reduced induction agent requirements."
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
