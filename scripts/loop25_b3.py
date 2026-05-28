import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2868: {
        "topic": "Scrotal Hernia - Tunica Vaginalis",
        "Core_Anatomy": "Scrotum and Inguinal Canal.",
        "Pathogenesis_Immediate": "In a scrotal hernia, the Tunica Vaginalis forms the Hernial Sac.",
        "Pathogenesis_Deep": "A hernia consists of three parts: the ring (defect in the wall), the sac (peritoneum), and the contents (intestine/omentum). In a male animal (especially pigs and horses), the tunica vaginalis is a direct evagination of the abdominal peritoneum that descends through the inguinal ring to cover the testicle. Therefore, if a loop of intestine slides down the inguinal canal into the scrotum, it sits directly inside the tunica vaginalis. The tunic itself acts as the hernial sac.",
        "Why_Not": "The pleural cavity is in the chest. Hernial contents are the intestines themselves, not the sac holding them.",
        "Wow_Approach": "This anatomical reality is why a pig with a scrotal hernia MUST undergo a 'closed' castration. If you cut open the tunica vaginalis (open castration), the abdominal cavity is now completely open to the outside world, and the intestines will eviscerate onto the floor."
    },
    2869: {
        "topic": "MAC - Isoflurane",
        "Core_Anatomy": "Central nervous system and Alveoli.",
        "Pathogenesis_Immediate": "The Minimum Alveolar Concentration (MAC) of Isoflurane in dogs is approximately 1.28%.",
        "Pathogenesis_Deep": "MAC is the standard measure of potency for inhalation anaesthetics. It is defined as the alveolar concentration of an inhalant that prevents gross purposeful movement in 50% of patients in response to a standard painful stimulus (like a surgical skin incision). The LOWER the MAC, the MORE POTENT the drug. Because it only covers 50% of patients, a clinical surgical plane of anaesthesia usually requires setting the vaporizer to 1.5 times the MAC (e.g., about 1.9% for Isoflurane).",
        "Why_Not": "Halothane has a lower MAC (0.87%), making it more potent. Sevoflurane has a higher MAC (2.36%), making it less potent (requiring a higher vaporizer setting).",
        "Wow_Approach": "MAC is significantly reduced (meaning you need less inhalant gas) by premedicating the patient with opioids or sedatives, by severe hypothermia, or by old age."
    },
    2870: {
        "topic": "Isoflurane MAC Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "This represents the correct numerical option (1.28%) for the preceding MAC question.",
        "Pathogenesis_Deep": "Remembering the baseline MAC values for the three common gases is essential for clinical practice: Halothane ~0.9%, Isoflurane ~1.3%, Sevoflurane ~2.4%.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2871: {
        "topic": "Pulse Oximetry - SpO2",
        "Core_Anatomy": "Hemoglobin (Arterial blood).",
        "Pathogenesis_Immediate": "Normal SpO2 in inhalation anaesthesia should be greater than 95%.",
        "Pathogenesis_Deep": "Pulse oximetry (SpO2) measures the percentage of hemoglobin binding sites in arterial blood that are saturated with oxygen. Because animals under inhalant anaesthesia are typically breathing 100% pure oxygen (from the Boyle's machine), their SpO2 should theoretically read 98-100%. A reading dropping below 95% is a severe warning sign (hypoxemia). A reading of 90% SpO2 actually corresponds to a dangerously low PaO2 of 60 mmHg (the critical drop-off point on the oxyhemoglobin dissociation curve).",
        "Why_Not": "A reading of 70-80% means the animal is cyanotic and actively suffocating. Anything above 100% is a physical impossibility for a percentage scale.",
        "Wow_Approach": "Pulse oximeters can be fooled. In Carbon Monoxide poisoning (e.g., a dog rescued from a house fire), the CO binds to hemoglobin and looks bright red. The SpO2 monitor will happily read 100%, even while the dog is dying of cellular asphyxiation."
    },
    2872: {
        "topic": "X-Ray Energy Levels",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "The diagnostic energy level of X-rays used in veterinary medicine is typically between 25-125 KeV (kilo-electron volts).",
        "Pathogenesis_Deep": "X-rays used for diagnostic imaging are highly energetic, short-wavelength electromagnetic waves. The energy (penetrating power) is determined by the kilovoltage peak (kVp) set on the machine. Veterinary machines typically operate between 40 kVp (for a tiny cat paw) and 120 kVp (for a massive horse abdomen). This produces X-ray photons with energy levels roughly in the 25 to 125 KeV range. This energy is enough to penetrate tissue without completely destroying the cells.",
        "Why_Not": "Lower energy (like 5 KeV) would not penetrate the skin (useless for imaging). Extremely high energy (Mega-electron volts) is used for radiation therapy to kill cancer, not for taking pictures.",
        "Wow_Approach": "Increasing the kVp by just 15% completely doubles the penetrating power of the X-ray beam, effectively doubling the darkness (density) of the final image."
    },
    2873: {
        "topic": "Perivascular Necrosis - Thiopentone",
        "Core_Anatomy": "Jugular/Cephalic veins and surrounding subcutaneous fascia.",
        "Pathogenesis_Immediate": "Thiopentone (Thiopental Sodium), if injected perivascularly, will cause severe tissue necrosis.",
        "Pathogenesis_Deep": "As highlighted previously, Thiopentone is supplied as a highly alkaline powder (pH 10.5 - 11) that must be reconstituted. It must be administered strictly intravenously. If the needle slips out of the vein and the drug is injected into the surrounding subcutaneous tissue (perivascularly), the extreme alkalinity causes immediate, agonizing chemical burns, followed by massive tissue necrosis, sloughing, and potential nerve damage.",
        "Why_Not": "Propofol and Azaperone do not cause tissue sloughing if given outside the vein. Thiopentone is uniquely dangerous in this regard.",
        "Wow_Approach": "To treat a perivascular injection of Thiopentone, you must immediately infiltrate the area with large volumes of sterile saline to dilute the alkalinity, mixed with Lidocaine to prevent local vasospasm and provide pain relief."
    },
    2874: {
        "topic": "MRI Units - Tesla",
        "Core_Anatomy": "Diagnostic imaging physics.",
        "Pathogenesis_Immediate": "The magnetic field strength of an MRI (Magnetic Resonance Imaging) machine is measured in units called Tesla (T).",
        "Pathogenesis_Deep": "MRI does not use ionizing radiation (X-rays). Instead, it uses a massive, super-conducting magnet to align the hydrogen protons in the body's water molecules, and radiofrequency pulses to knock them out of alignment. As the protons snap back, they emit signals that create highly detailed images of soft tissues (brain, spinal cord). The strength of this magnet is measured in Tesla. Most veterinary clinical MRIs are 1.5 T or 3.0 T.",
        "Why_Not": "Hounsfield units measure tissue density on a CT scan. REM and Grey measure ionizing radiation dose. Tesla exclusively measures magnetic field strength.",
        "Wow_Approach": "A 1.5 Tesla MRI magnet is roughly 30,000 times stronger than the magnetic field of the Earth. It will violently pull any ferromagnetic metal object (scissors, oxygen tanks, collars) across the room and pin it into the machine, which is a lethal hazard."
    },
    2875: {
        "topic": "Antiseptics and Organic Matter - Chlorhexidine",
        "Core_Anatomy": "Contaminated surgical wounds.",
        "Pathogenesis_Immediate": "Chlorhexidine is preferred as an antiseptic in the presence of organic matter (blood, pus).",
        "Pathogenesis_Deep": "Surgical antiseptics behave differently when faced with heavy contamination. Povidone-Iodine is rapidly inactivated by organic debris (blood, pus, necrotic tissue) because the free iodine binds to the organic proteins rather than the bacterial walls. Chlorhexidine (a biguanide) is uniquely resistant to organic inactivation. It remains highly effective and provides excellent residual antibacterial activity for up to 6 hours after application.",
        "Why_Not": "Povidone-iodine loses its efficacy in a dirty, bloody wound.",
        "Wow_Approach": "This is why Chlorhexidine is the superior choice for scrubbing a severely contaminated traumatic wound or for routine surgical hand scrubbing (where residual activity under gloves is required)."
    },
    2876: {
        "topic": "Penetrating Wound",
        "Core_Anatomy": "Body cavities (Thorax, Abdomen, Joints).",
        "Pathogenesis_Immediate": "A deep wound communicating with cavities like the abdomen, thorax, trachea, or joints is classified as a Penetrating wound.",
        "Pathogenesis_Deep": "Wounds are classified by depth. (1) Superficial (epidermis only). (2) Deep (through the dermis and muscle fascia). (3) Penetrating: The weapon (stick, bullet, tooth) completely breaches the protective wall of a body cavity, entering the thorax, abdomen, or a synovial joint capsule. (4) Perforating: The weapon goes completely through the body (an entrance and an exit wound). Penetrating wounds are surgical emergencies because they introduce massive environmental contamination directly into sterile, life-sustaining cavities, inevitably causing septic peritonitis or pyothorax.",
        "Why_Not": "A simple deep wound might hit muscle, but a penetrating wound specifically breaches a cavity lining (peritoneum/pleura).",
        "Wow_Approach": "NEVER pull a stick or arrow out of a penetrating thoracic wound in the field. The object is acting as a plug holding the severed blood vessels closed and preventing a massive pneumothorax. It must be removed surgically in the operating room under controlled conditions."
    },
    2877: {
        "topic": "Innovar-Vet - Neuroleptanalgesia",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "Innovar-Vet is a commercial neuroleptanalgesic combination containing Droperidol and Fentanyl.",
        "Pathogenesis_Deep": "Similar to Hypnorm, Innovar-Vet is a classic, potent neuroleptanalgesic. It combines a massive dose of a potent Mu-opioid agonist (Fentanyl) with a strong butyrophenone tranquilizer (Droperidol). It was historically popular in canine medicine to provide profound, reversible sedation and analgesia for minor surgical procedures without requiring general anaesthesia.",
        "Why_Not": "Fluanisone + Fentanyl is Hypnorm. Acepromazine + Etorphine is Immobilon. Droperidol + Fentanyl is specifically Innovar-Vet.",
        "Wow_Approach": "A major side effect of Innovar-Vet in dogs is profound auditory hypersensitivity. A loud noise (like dropping a metal pan in the clinic) will cause the heavily sedated dog to suddenly violently thrash or bite."
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
