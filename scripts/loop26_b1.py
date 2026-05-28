import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2942: {
        "topic": "Xylazine - Pregnancy Contraindication",
        "Core_Anatomy": "Myometrium (Uterus) and CNS.",
        "Pathogenesis_Immediate": "Xylazine is strongly contraindicated in pregnant cows, particularly in the third trimester.",
        "Pathogenesis_Deep": "Xylazine, an alpha-2 agonist, has an oxytocin-like effect on the bovine myometrium. It causes a profound, prolonged increase in uterine tone and contractility. In late-stage pregnancy, this can compress the placental blood supply, causing fetal hypoxia, or directly trigger premature parturition/abortion. Additionally, the profound systemic hypotension and bradycardia reduce uterine perfusion.",
        "Why_Not": "Detomidine and Diazepam have less effect on uterine tone. Acepromazine causes vasodilation but does not trigger contractions. Xylazine is the classic abortifacient sedative in cattle.",
        "Wow_Approach": "If standing sedation is absolutely required in a heavily pregnant cow (e.g., for a flank laparotomy), low-dose Acepromazine combined with local nerve blocks (Paravertebral) is the safest choice."
    },
    2944: {
        "topic": "Retrobulbar Nerve Block",
        "Core_Anatomy": "Cranial Nerves within the orbit.",
        "Pathogenesis_Immediate": "A retrobulbar block aims to anesthetize cranial nerves II, III, IV, V (ophthalmic branch), and VI.",
        "Pathogenesis_Deep": "When performing an enucleation in a standing cow, the surgeon injects local anesthetic deep into the orbital cone behind the globe. This single block paralyzes the extraocular muscles (CN III - Oculomotor, CN IV - Trochlear, CN VI - Abducens), blocks all sensation to the globe and cornea (CN V - Trigeminal, ophthalmic division), and blocks the optic nerve (CN II).",
        "Why_Not": "If you miss CN VI, the retractor bulbi muscle will pull the eye deep into the socket, making surgery extremely difficult.",
        "Wow_Approach": "Because the optic nerve is surrounded by a sheath continuous with the meninges, accidentally injecting the local anesthetic directly INTO the optic nerve sheath will deliver the drug straight to the brain, causing instant, fatal respiratory arrest."
    },
    2945: {
        "topic": "Barbiturate Classification",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "Thiopental, Hexobarbital, Thiamylal, and Pentobarbital are all classified as Barbiturates.",
        "Pathogenesis_Deep": "This question tests the ability to recognize drug classes. All options listed are barbiturates, characterized by a barbituric acid ring. They differ only by their side chains, which determine their lipid solubility and duration of action (Thiobarbiturates like Thiopental are ultra-short acting; Oxybarbiturates like Pentobarbital are short acting).",
        "Why_Not": "If the test asks which drug is NOT a barbiturate, look for a drug ending in '-fol' (Propofol) or '-xalone' (Alfaxalone), which are non-barbiturate induction agents.",
        "Wow_Approach": "N/A"
    },
    2946: {
        "topic": "Diffusion Hypoxia - Nitrous Oxide",
        "Core_Anatomy": "Pulmonary alveoli.",
        "Pathogenesis_Immediate": "Diffusion hypoxia is a specific, dangerous complication associated with the administration and rapid withdrawal of Nitrous Oxide (N2O).",
        "Pathogenesis_Deep": "Nitrous oxide is relatively insoluble in blood. At the end of surgery, when the N2O is turned off, the massive volume of N2O dissolved in the patient's blood rapidly diffuses OUT of the bloodstream and back into the alveoli. This massive outpouring of N2O physically displaces and dilutes the oxygen in the alveoli. If the patient is breathing room air (21% O2) during this time, the alveolar oxygen concentration drops plummeting below life-sustaining levels, causing acute, severe 'diffusion hypoxia'.",
        "Why_Not": "Halothane and Isoflurane do not cause this because they are used at very low concentrations (1-2%), whereas N2O is used at very high concentrations (50-70%).",
        "Wow_Approach": "To prevent diffusion hypoxia, every patient receiving Nitrous Oxide MUST be maintained on 100% pure oxygen for at least 5 to 10 minutes AFTER the N2O is turned off."
    },
    2947: {
        "topic": "X-Ray Production - Bremsstrahlung",
        "Core_Anatomy": "X-ray tube target (Tungsten).",
        "Pathogenesis_Immediate": "As electrons reach the target, they produce X-rays primarily by 'Sudden braking' (Bremsstrahlung radiation).",
        "Pathogenesis_Deep": "In the X-ray tube, high-speed electrons from the cathode are fired at the tungsten anode target. As an electron approaches the strong positive nucleus of a tungsten atom, it is violently pulled off course and rapidly decelerates ('sudden braking'). The kinetic energy lost during this sudden deceleration is emitted as an X-ray photon. This process (Bremsstrahlung) produces about 90% of the diagnostic X-ray beam.",
        "Why_Not": "The other 10% is 'Characteristic radiation' (an electron knocks an inner shell electron out of orbit). Scattering happens in the patient, not in the tube.",
        "Wow_Approach": "Bremsstrahlung is German for 'braking radiation'."
    },
    2948: {
        "topic": "Radiation Susceptibility - Bone Marrow",
        "Core_Anatomy": "Hematopoietic stem cells.",
        "Pathogenesis_Immediate": "Reiterating that the Bone Marrow is the tissue most susceptible to radiation damage.",
        "Pathogenesis_Deep": "Cells that are rapidly dividing and poorly differentiated are highly sensitive to ionizing radiation because their DNA is unwound and actively replicating, making it highly vulnerable to being shattered by X-ray photons.",
        "Why_Not": "Nerve cells do not divide (post-mitotic) and are highly resistant.",
        "Wow_Approach": "This principle is the entire basis of radiation therapy for cancer: cancer cells divide rapidly and wildly, so they are selectively killed by radiation doses that normal, resting tissues can survive."
    },
    2949: {
        "topic": "Anode Heel Effect",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "Due to the Anode Heel Effect, the thickest part of the patient should be placed towards the Cathode side of the X-ray tube.",
        "Pathogenesis_Deep": "The tungsten target on the anode is angled. Because X-rays are produced deep within this target, the X-rays heading toward the anode end of the tube must pass through more tungsten metal to escape, which absorbs some of their energy. The X-rays heading toward the cathode end escape easily. Therefore, the X-ray beam is significantly STRONGER (more intense) on the Cathode side. To get an even exposure, the radiographer places the thickest, densest part of the animal (e.g., the deep thorax) under the stronger Cathode beam.",
        "Why_Not": "Placing the thick part under the weaker anode side will result in an underexposed (too white) image of the thick tissues.",
        "Wow_Approach": "Mnemonic: 'Fat Cat' (Thickest part towards the Cathode)."
    },
    2950: {
        "topic": "Protective Radiographic Gadgets - Lead",
        "Core_Anatomy": "Occupational safety.",
        "Pathogenesis_Immediate": "Protective radiographic gadgets (aprons, thyroid shields, gloves) are made of Lead.",
        "Pathogenesis_Deep": "Lead (Pb) has a very high atomic number (82) and high density. This allows it to efficiently absorb low-energy scattered X-ray photons via the photoelectric effect, preventing them from penetrating into the radiographer's body. Standard aprons contain a 0.5 mm lead equivalent.",
        "Why_Not": "Iron, Tungsten, and Titanium are not used for flexible aprons. Tungsten is used inside the X-ray tube, not in wearable safety gear.",
        "Wow_Approach": "Lead aprons must NEVER be folded, as folding cracks the inner lead lining. They must be hung flat on specialized racks. A cracked apron is useless, allowing radiation to stream straight through the cracks to the operator."
    },
    2951: {
        "topic": "Echocardiography - M-Mode",
        "Core_Anatomy": "Heart (Valves and myocardium).",
        "Pathogenesis_Immediate": "The ultrasound mode specifically used for echocardiographic evaluation is M-Mode (Motion Mode).",
        "Pathogenesis_Deep": "While B-Mode gives a 2D picture of the heart, M-Mode takes a single, ultra-thin slice (a single line of ultrasound crystals) and tracks the motion of the structures along that line over time. The output is a scrolling graph showing exactly how fast and how far the heart walls and valves are moving during systole and diastole. It is the gold standard for measuring fractional shortening and myocardial contractility.",
        "Why_Not": "B-mode shows anatomy. A-mode is for the eye. M-mode specifically charts rapid cardiac MOTION.",
        "Wow_Approach": "M-mode traces have an extremely high sampling rate (up to 1,000 times per second), making it the only ultrasound mode fast enough to capture the exact millisecond a heart valve snaps shut."
    },
    2952: {
        "topic": "Ultrasound Fluid Appearance - Anechoic",
        "Core_Anatomy": "Diagnostic imaging physics.",
        "Pathogenesis_Immediate": "Fluid in an ultrasound image appears Anechoic (black).",
        "Pathogenesis_Deep": "Ultrasound images are formed by sound waves bouncing back (echoing) to the probe. Pure fluid (urine, bile, ascites) transmits sound waves perfectly and does not reflect them back. Because no echoes return from the fluid, the ultrasound machine colors that area pure black on the screen (Anechoic).",
        "Why_Not": "Hyperechoic (white) = bone/gas. Isoechoic = same shade of grey as surrounding tissue. Hypoechoic = dark grey.",
        "Wow_Approach": "Because sound travels so easily through a full bladder, the tissue immediately deep to the bladder receives a massive dose of sound waves. This makes the deep tissue look artificially bright (white). This artifact is called 'Acoustic Enhancement' and confirms that the black structure above it is truly fluid."
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
