import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2564: {
        "topic": "Immobilon LA - Etorphine + Acepromazine",
        "Core_Anatomy": "Central nervous system (mu-opioid and dopamine receptors).",
        "Pathogenesis_Immediate": "Immobilon LA (Large Animal Immobilon) contains Etorphine (2.45 mg/ml) and Acepromazine (10 mg/ml).",
        "Pathogenesis_Deep": "Immobilon LA is a potent neuroleptanalgesic combination used primarily for capturing/immobilizing large wild animals and horses. Etorphine (M99) is a synthetic opioid 1,000 to 3,000 times more potent than morphine, providing profound analgesia and immobilization. Acepromazine is a phenothiazine tranquilizer that provides sedation and muscle relaxation, counteracting the excitatory side-effects of the pure opioid. Because Etorphine is extremely concentrated (2.45 mg/ml), a tiny volume (e.g., 2 ml) is sufficient to drop an adult horse or rhino.",
        "Why_Not": "Different concentrations exist for Small Animal Immobilon, but the Large Animal (LA) formulation is specifically concentrated (2.45 mg/ml Etorphine) to allow delivery via dart gun.",
        "Wow_Approach": "Etorphine is extremely dangerous to humans. A single accidental scratch from an Immobilon dart needle can cause fatal respiratory arrest in a human within 2 minutes. The specific antidote, Diprenorphine (Revivon) or Naloxone, MUST be drawn up in a syringe and ready for human injection before the Etorphine bottle is even opened."
    },
    2565: {
        "topic": "Pure Opioid Agonist - Oxymorphone",
        "Core_Anatomy": "Central nervous system (Mu-opioid receptors).",
        "Pathogenesis_Immediate": "Oxymorphone is a pure Mu-opioid agonist.",
        "Pathogenesis_Deep": "Opioids are classified by their receptor activity. (1) Pure agonists (Oxymorphone, Morphine, Fentanyl, Methadone) bind strongly to Mu-receptors, providing profound, dose-dependent analgesia for severe surgical pain. (2) Partial agonists (Buprenorphine) bind tightly but do not fully activate the receptor, providing moderate analgesia. (3) Agonist-antagonists (Butorphanol) stimulate Kappa receptors but block Mu receptors, providing mild analgesia and strong sedation. (4) Pure antagonists (Naloxone) block all receptors.",
        "Why_Not": "Butorphanol is an agonist-antagonist. Buprenorphine is a partial agonist. Nalorphine is an antagonist. Only Oxymorphone represents the pure, full Mu-agonist category here.",
        "Wow_Approach": "Because Oxymorphone is a pure Mu-agonist, its profound respiratory depression can be fully and rapidly reversed with Naloxone if the patient stops breathing during anaesthesia."
    },
    2566: {
        "topic": "Corneal Nerve - Trigeminal Nerve Branch",
        "Core_Anatomy": "Ophthalmic nerve and cornea.",
        "Pathogenesis_Immediate": "The corneal nerve is a branch of the ophthalmic division of the Trigeminal nerve (Cranial Nerve V).",
        "Pathogenesis_Deep": "Sensory innervation to the cornea is extremely dense, making it one of the most pain-sensitive tissues in the body. The sensory pathway originates from the Trigeminal nerve (CN V) -> Ophthalmic branch (V1) -> Nasociliary nerve -> Long ciliary nerves -> Corneal nerves. This sensory pathway is the afferent (inward) arm of the Corneal Reflex. The efferent (outward) motor arm that causes the blink is the Facial nerve (CN VII) innervating the orbicularis oculi muscle.",
        "Why_Not": "The Facial nerve (CN VII) is MOTOR to the eyelids (blinking). The Trigeminal nerve (CN V) is SENSORY to the cornea (feeling the touch).",
        "Wow_Approach": "During general anaesthesia monitoring, lightly touching the cornea tests this Trigeminal-Facial reflex arc. The corneal reflex disappears in deep (Stage III, Plane III) anaesthesia—if it is absent, the animal is dangerously deep."
    },
    2567: {
        "topic": "Intensifying Screen - Reducing Patient Dose",
        "Core_Anatomy": "X-ray cassette and radiographic physics.",
        "Pathogenesis_Immediate": "The intensifying screen in an X-ray cassette is used primarily to reduce patient radiation dose.",
        "Pathogenesis_Deep": "X-ray film is actually very insensitive to direct X-ray photons. An intensifying screen is a layer of rare-earth phosphors (like gadolinium or lanthanum) placed inside the cassette, pressing tightly against the film. When an X-ray photon strikes the screen, the phosphor fluoresces, emitting thousands of visible light photons. It is this LIGHT (not the X-rays themselves) that primarily exposes the film. This massive amplification allows the radiographer to use significantly fewer mAs (lower X-ray exposure), drastically reducing the radiation dose to both the patient and the staff holding the animal.",
        "Why_Not": "The screen does NOT convert electrons to light (that happens in the X-ray tube target). The primary purpose is amplification to allow lower exposure (reducing dose).",
        "Wow_Approach": "The trade-off for this dose reduction is a slight loss of image sharpness (due to light diffusion from the screen). However, the massive safety benefit (a 50x reduction in radiation dose) makes intensifying screens mandatory for veterinary radiography."
    },
    2568: {
        "topic": "Thoracic Radiography - Inspiration",
        "Core_Anatomy": "Thoracic cavity (lungs, diaphragm, heart).",
        "Pathogenesis_Immediate": "A thoracic radiograph should always be taken on peak Inspiration.",
        "Pathogenesis_Deep": "Taking the exposure during maximum inspiration serves two critical purposes: (1) It maximizes the amount of air (radiolucent/black) in the alveoli. This creates maximum contrast between the black air-filled lungs and white soft-tissue lesions (tumors, pulmonary edema, vessels), making lesions highly visible. (2) It pushes the diaphragm caudally, expanding the visible lung field and preventing the heart and diaphragm from compressing lung lobes (which mimics pathology like atelectasis or pneumonia).",
        "Why_Not": "Taking an exposure on expiration causes the lungs to appear falsely dense (white) and the heart to look falsely enlarged, leading to misdiagnosis of pulmonary edema or cardiomegaly.",
        "Wow_Approach": "To catch the peak of inspiration in a panting dog, blow gently on its nose just before pressing the exposure button—the dog will briefly stop panting, take a deep breath in, and hold it."
    },
    2569: {
        "topic": "Radiation Damage - Bone Marrow Susceptibility",
        "Core_Anatomy": "Bone marrow and systemic cell turnover.",
        "Pathogenesis_Immediate": "The tissue most susceptible to radiation damage is the Bone marrow.",
        "Pathogenesis_Deep": "According to the Law of Bergonié and Tribondeau in radiobiology, the radiosensitivity of a tissue is directly proportional to its rate of cell division (mitotic activity) and inversely proportional to its degree of differentiation. Bone marrow contains rapidly dividing, undifferentiated hematopoietic stem cells, making it exquisitely sensitive to ionizing radiation. Radiation damages the DNA during mitosis, causing cell death. This results in severe leukopenia, thrombocytopenia, and anemia (Acute Radiation Syndrome).",
        "Why_Not": "Brain, nerve, and kidney tissues consist of highly differentiated cells that rarely divide (post-mitotic). They are highly RESISTANT to radiation damage.",
        "Wow_Approach": "This principle is the basis of radiation therapy for cancer—tumors consist of rapidly dividing, poorly differentiated cells, making them more sensitive to radiation destruction than the surrounding stable healthy tissue."
    },
    2570: {
        "topic": "Phlegmon - Spreading Cellulitis",
        "Core_Anatomy": "Subcutaneous and deep fascial connective tissue.",
        "Pathogenesis_Immediate": "Phlegmon is defined as a spreading, diffuse purulent inflammation of loose connective tissue (Cellulitis).",
        "Pathogenesis_Deep": "Unlike an abscess (which is a walled-off, localized collection of pus confined by a pyogenic membrane), a phlegmon is an unconfined, rapidly spreading suppurative inflammation extending along fascial planes and through loose subcutaneous connective tissue. It is typically caused by highly invasive bacteria that produce spreading enzymes (e.g., Streptococcus producing hyaluronidase and streptokinase). The affected area is hot, painful, swollen, and doughy, with no distinct boundaries.",
        "Why_Not": "Cyclophosphamide is an alkylating chemotherapy agent (answer to the next question). A phlegmon is an infectious pathology.",
        "Wow_Approach": "Because there is no distinct cavity of pus, attempting to lance or drain a phlegmon is generally ineffective and contra-indicated; treatment relies heavily on aggressive systemic antibiotics, anti-inflammatories, and hot fomentation to encourage localization into an abscess."
    },
    2571: {
        "topic": "Alkylating Agents - Cyclophosphamide",
        "Core_Anatomy": "Cell nucleus (DNA replication machinery).",
        "Pathogenesis_Immediate": "Cyclophosphamide is matched as an Alkylating agent.",
        "Pathogenesis_Deep": "Cyclophosphamide is one of the most widely used chemotherapy drugs in veterinary oncology (e.g., in the CHOP protocol for canine lymphoma). As an alkylating agent, it works by adding alkyl groups to the guanine bases of DNA. This causes intra-strand and inter-strand DNA cross-linking. When the cancer cell attempts to replicate its DNA for mitosis, the cross-links prevent the DNA strands from separating, triggering apoptosis (cell death).",
        "Why_Not": "Vincristine is a microtubule inhibitor. Doxorubicin is an anthracycline antibiotic. Cyclophosphamide specifically represents the alkylating class.",
        "Wow_Approach": "A unique, severe side-effect of Cyclophosphamide is Sterile Hemorrhagic Cystitis. The drug is metabolized in the liver to Acrolein, a toxic metabolite excreted in the urine that physically burns the bladder mucosa. This is prevented by administering the drug in the morning and ensuring the dog drinks plenty of water to dilute the urine."
    },
    2579: {
        "topic": "VSR 421 - Regional Veterinary Surgery Header",
        "Core_Anatomy": "Systemic surgical anatomy by region.",
        "Pathogenesis_Immediate": "Header indicating the start of the Regional Veterinary Surgery exam section.",
        "Pathogenesis_Deep": "Unlike General Surgery (which covers principles), Regional Surgery tests specific anatomical approaches, specialized procedures (e.g., laparotomy, ophthalmology, dentistry), and species-specific surgical diseases.",
        "Why_Not": "This section tests applied anatomy: knowing exactly which muscle layers to cut through for a specific procedure.",
        "Wow_Approach": "High-yield topics in this section include: surgical correction of LDA, specific hernia repairs, and anatomical names of surgical approaches."
    },
    2586: {
        "topic": "Regional Surgery MCQ Header",
        "Core_Anatomy": "Regional surgical anatomy.",
        "Pathogenesis_Immediate": "Header for the multiple-choice section of Regional Surgery.",
        "Pathogenesis_Deep": "Expect questions on specific anatomical structures, specialized surgical terms (e.g., Schmieden, Lembert), and classic surgical diseases of specific breeds.",
        "Why_Not": "Read options carefully; surgical MCQs often include minor variations of surgical techniques as distractors.",
        "Wow_Approach": "Surgical nomenclature is highly logical: '-otomy' = to cut into; '-ectomy' = to remove; '-ostomy' = to create a permanent opening; '-pexy' = to surgically fixate."
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
