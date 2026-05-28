import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2771: {
        "topic": "VSR 411 - General Surgery Objective Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of the General Surgery, Anaesthesiology, and Diagnostic Imaging objective section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2772: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for the fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2773: {
        "topic": "Aseptic Technique - Prevention of Infection",
        "Core_Anatomy": "Surgical wound bed.",
        "Pathogenesis_Immediate": "Rules of Aseptic technique must be followed to prevent Surgical Site Infection (SSI) / Sepsis.",
        "Pathogenesis_Deep": "As reviewed previously, aseptic technique includes autoclaving instruments, surgical scrubbing, sterile draping, and minimizing theatre traffic. The goal is to prevent any pathogenic microorganisms from entering the sterile surgical field, thereby preventing postoperative wound sepsis, delayed healing, and systemic bacteremia.",
        "Why_Not": "Disinfection only reduces pathogens; asepsis aims for complete exclusion.",
        "Wow_Approach": "If a surgeon's glove touches an unsterile surface (like the edge of the surgical light handle), the glove is considered contaminated and must be changed immediately (the 'sterile conscience' principle)."
    },
    2779: {
        "topic": "Cystography - Bladder Radiography",
        "Core_Anatomy": "Urinary bladder.",
        "Pathogenesis_Immediate": "The radiographic study of the bladder is called Cystography.",
        "Pathogenesis_Deep": "Cystography requires catheterizing the urethra and instilling contrast. It is the definitive imaging modality for diagnosing a ruptured bladder (uroabdomen), cystic calculi (radiolucent stones like urate), or bladder wall neoplasms (Transitional Cell Carcinoma).",
        "Why_Not": "Intravenous urography evaluates the kidneys and ureters. Cystography specifically targets the bladder.",
        "Wow_Approach": "In trauma cases (e.g., dog hit by a car with a fractured pelvis), always perform a positive contrast cystogram to ensure the bladder hasn't ruptured before proceeding with orthopedic surgery."
    },
    2780: {
        "topic": "Boyle's Apparatus - Inhalation Anaesthesia",
        "Core_Anatomy": "Lungs (alveolar absorption).",
        "Pathogenesis_Immediate": "Boyle's apparatus is the machine used for administering inhalation anaesthetics.",
        "Pathogenesis_Deep": "The Boyle's machine mixes carrier gases (Oxygen, Nitrous Oxide) via rotameters, passes the gas through a precision vaporizer (to pick up Halothane/Isoflurane), and delivers it to the patient via a breathing circuit. It also includes a CO2 absorber (soda lime) to allow safe rebreathing of the gases.",
        "Why_Not": "Syringe drivers are for TIVA (Total Intravenous Anaesthesia). Boyle's machine is exclusively for inhalants.",
        "Wow_Approach": "Before connecting a patient to a Boyle's machine, the anaesthetist MUST perform a 'leak test' by closing the pop-off valve, inflating the rebreathing bag, and ensuring the pressure holds. A leaking circuit will result in the patient waking up during surgery."
    },
    2783: {
        "topic": "Choose the Correct Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2784: {
        "topic": "Eczema Treatment - UV Rays",
        "Core_Anatomy": "Skin epidermis.",
        "Pathogenesis_Immediate": "Eczema (chronic atopic dermatitis) can be effectively treated by UV rays (Phototherapy).",
        "Pathogenesis_Deep": "UVB phototherapy suppresses the local cutaneous immune response by depleting Langerhans cells and reducing pro-inflammatory cytokines. This helps control the intense pruritus and inflammation associated with severe atopic dermatitis when topical steroids fail.",
        "Why_Not": "IR (Infrared) provides deep heat for muscles, not immunosuppression for the skin.",
        "Wow_Approach": "While UV therapy is useful, long-term exposure significantly increases the risk of cutaneous squamous cell carcinoma, especially in sparsely haired, unpigmented skin."
    },
    2785: {
        "topic": "Radiographic Grid - Tissue Thickness",
        "Core_Anatomy": "X-ray physics and scatter radiation.",
        "Pathogenesis_Immediate": "A radiographic Grid is employed when tissue thickness is >10 cm.",
        "Pathogenesis_Deep": "Tissues thicker than 10 cm (like the abdomen or thorax of a medium/large dog) generate massive amounts of Compton scatter radiation. This scatter hits the film at random angles, producing a 'fog' that drastically reduces image contrast. The Potter-Bucky grid absorbs this scattered radiation before it reaches the film, restoring diagnostic contrast.",
        "Why_Not": "For a cat's leg (<10 cm), scatter is minimal. Using a grid would just force the radiographer to double the radiation dose (to compensate for the grid absorbing some primary beam) with no diagnostic benefit.",
        "Wow_Approach": "If you accidentally place a focused grid upside down, the lead strips will absorb almost the entire primary X-ray beam, resulting in a completely blank (white) film with only a tiny dark strip down the exact center (grid cutoff)."
    },
    2786: {
        "topic": "Haemorrhagic Shock Treatment - Blood Transfusion",
        "Core_Anatomy": "Systemic vasculature and Erythrocytes.",
        "Pathogenesis_Immediate": "The definitive specific treatment for severe haemorrhagic shock is a Blood Transfusion.",
        "Pathogenesis_Deep": "While fluid therapy (crystalloids) is the first-line immediate response to restore circulating volume and blood pressure, it causes hemodilution. If the animal has lost >20% of its blood volume, it lacks the red blood cells (hemoglobin) necessary to carry oxygen to the tissues. Only a whole blood transfusion (or packed RBCs) can restore oxygen-carrying capacity. Without RBCs, restoring blood pressure with fluids still results in fatal tissue hypoxia.",
        "Why_Not": "Fluids and oxygen are supportive. Plasma replaces volume and clotting factors, but NOT oxygen-carrying capacity. Whole blood provides all three.",
        "Wow_Approach": "Dogs have a universal donor blood type (DEA 1.1 negative). In an acute, life-threatening emergency, a dog can safely receive one un-crossmatched transfusion of DEA 1.1 negative blood. Cats, however, have naturally occurring alloantibodies; an un-crossmatched transfusion in a cat can cause immediate fatal anaphylaxis."
    },
    2787: {
        "topic": "X-ray Film Development - Silver Reduction",
        "Core_Anatomy": "Silver halide emulsion.",
        "Pathogenesis_Immediate": "During development, the exposed silver halide crystals are Reduced to metallic silver.",
        "Pathogenesis_Deep": "The chemical developer (hydroquinone) acts as an electron donor (reducing agent). It donates electrons to the silver ions (Ag+) that were exposed to X-rays, reducing them to stable, black metallic silver (Ag0). This creates the dark/black areas on the X-ray film.",
        "Why_Not": "Oxidation means losing electrons. The silver must gain electrons (Reduction) to become visible metallic silver.",
        "Wow_Approach": "The fixing solution (which follows the developer) removes all the UNEXPOSED silver halide crystals. If you skip the fixer and expose the wet film to room light, the remaining unexposed crystals will instantly turn black, destroying the image."
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
