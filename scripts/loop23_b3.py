import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2638: {
        "topic": "Gingival Tumor - Epulis",
        "Core_Anatomy": "Gingiva (periodontal ligament / mucosa).",
        "Pathogenesis_Immediate": "A benign tumor arising from the gingiva (gums) is clinically referred to as an Epulis.",
        "Pathogenesis_Deep": "Epulis is a broad clinical term for any localized, exophytic growth on the gingiva. In dogs, they are extremely common and are histologically classified into three types: Fibromatous epulis, Ossifying epulis, and Acanthomatous epulis. The Acanthomatous epulis (now formally called Acanthomatous Ameloblastoma) is locally highly invasive, frequently destroying the underlying maxillary or mandibular bone, despite not metastasizing. The others are benign and originate from the periodontal ligament.",
        "Why_Not": "Odontoma is a tumor of tooth-forming tissue (enamel/dentin). Chondroma is cartilage. Osteoma is bone. Epulis is specifically the gingival mass.",
        "Wow_Approach": "Because an Acanthomatous Epulis invades bone, simply slicing it off the gum line guarantees recurrence. Curative treatment requires a partial mandibulectomy or maxillectomy to remove the affected teeth and the surrounding bone with a 1cm margin."
    },
    2639: {
        "topic": "Aseptic Surgery - Free of Micro-organisms",
        "Core_Anatomy": "Surgical operating environment and wound bed.",
        "Pathogenesis_Immediate": "Aseptic surgery is surgery performed in an environment that is kept Free of pathogenic micro-organisms.",
        "Pathogenesis_Deep": "Asepsis (absence of pathogenic microbes) is the goal of modern surgery, achieved through strict adherence to Aseptic Technique. This contrasts with 'Antiseptic surgery' (the historical practice of spraying carbolic acid into a contaminated wound). Aseptic technique includes sterilizing instruments (autoclaving), preparing the patient's skin (chlorhexidine scrub), the surgical team wearing sterile attire, and utilizing positive-pressure ventilation in the operating theatre to prevent airborne contamination from entering.",
        "Why_Not": "'Free of contamination' is close, but 'Free of micro-organisms' specifically defines the absolute sterile goal of the environment, tools, and drapes interacting with the surgical wound.",
        "Wow_Approach": "The primary source of bacterial contamination in a clean surgical wound is actually the patient's own endogenous skin flora (e.g., Staphylococcus intermedius in dogs) that survives in the deep hair follicles despite aggressive preoperative surgical scrubbing."
    },
    2640: {
        "topic": "Vertical Mattress Suture - Tension Relieving",
        "Core_Anatomy": "Skin and subcutaneous fascia.",
        "Pathogenesis_Immediate": "The vertical mattress suture is a Tension-relieving, Everting type of suture pattern.",
        "Pathogenesis_Deep": "Suture patterns are classified by their effect on tissue edges: Appositional (edges meet flush), Inverting (edges roll inward, used for hollow organs), and Everting (edges roll outward). The vertical mattress is a strongly everting, tension-relieving pattern. The needle passes 'far-far' (taking a deep, wide bite to distribute tension across the fascia) and then 'near-near' (taking a shallow bite right at the wound edge for precise skin apposition). It is ideal for closing skin wounds under high tension, such as on the limbs.",
        "Why_Not": "Simple interrupted sutures cut through tissue (cheese-wiring) when placed under high tension. The vertical mattress prevents this by distributing the load away from the incision line.",
        "Wow_Approach": "The mnemonic for vertical mattress placement is 'Far-Far, Near-Near'. A key surgical tip: always place the 'near-near' bites exactly at the dermal-epidermal junction to ensure perfect epidermal alignment."
    },
    2654: {
        "topic": "Orthopedics Definition",
        "Core_Anatomy": "Skeletal system (bones, joints, ligaments).",
        "Pathogenesis_Immediate": "Orthopedics is the surgical specialty concerned with the preservation and restoration of the function of the skeletal system.",
        "Pathogenesis_Deep": "Veterinary orthopedics encompasses fracture repair, joint stabilization (e.g., Tibial Plateau Leveling Osteotomy for cruciate ligament rupture), correction of angular limb deformities, and management of developmental diseases like Osteochondritis Dissecans (OCD) and Hip Dysplasia. It relies heavily on biomechanical engineering principles—utilizing plates, screws, and pins to neutralize rotational, bending, and shear forces acting on the healing bone.",
        "Why_Not": "Soft tissue surgery handles viscera. Neurology handles the nervous system. Orthopedics is strictly the musculoskeletal system.",
        "Wow_Approach": "Bone is one of the only tissues in the body that heals by completely regenerating its original tissue (osteonal remodeling) rather than forming a fibrous scar—provided it is rigidly stabilized and has an intact blood supply."
    },
    2655: {
        "topic": "Crepitating Sound - Bone Fracture",
        "Core_Anatomy": "Bone cortices.",
        "Pathogenesis_Immediate": "A crepitating sound (crepitus) is the classic physical sign of a Bone Fracture.",
        "Pathogenesis_Deep": "Crepitus is the harsh, grating, crunching sound and tactile sensation produced when the sharp, broken ends of a fractured bone rub against each other during manipulation. It is a definitive diagnostic sign of a complete fracture. However, eliciting crepitus causes excruciating pain and further damages the surrounding soft tissues, blood vessels, and periosteum. Therefore, if a fracture is suspected, the limb should be immediately radiographed rather than manipulated aggressively to 'feel for the crunch'.",
        "Why_Not": "Dislocations (luxations) do not produce bony crepitus; they feel 'springy' or 'rubbery' due to muscle spasm and intact articular cartilage. Subcutaneous emphysema produces a soft 'bubble wrap' popping, not a hard bony grating.",
        "Wow_Approach": "In chronic osteoarthritis, a softer 'articular crepitus' can be felt due to the loss of smooth hyaline cartilage, but it is distinct from the harsh 'fracture crepitus' of broken bone."
    },
    2656: {
        "topic": "Burn vs Scald",
        "Core_Anatomy": "Skin (epidermis/dermis).",
        "Pathogenesis_Immediate": "A Burn is caused by dry heat (fire, hot metal, friction, chemicals).",
        "Pathogenesis_Deep": "Thermal injuries are categorized by the heat source. A true 'burn' is caused by dry heat. The intense temperature rapidly coagulates the cellular proteins, leading to a dry, leathery eschar (in 3rd degree). Because the heat source is often extremely high temperature (e.g., flame at 800°C), burns tend to be deeper and more severe. Friction burns ('road rash' in dogs dragged by cars) also fall into this category, combining thermal coagulation with massive mechanical abrasion.",
        "Why_Not": "A scald is caused by moist heat (hot water, steam).",
        "Wow_Approach": "The 'Rule of Nines' is used to estimate the Total Body Surface Area (TBSA) affected by burns. If a burn exceeds 20% TBSA, the animal will suffer severe systemic effects (Burn Shock) due to massive fluid loss, protein exudation, and systemic inflammatory response syndrome (SIRS)."
    },
    2658: {
        "topic": "Scald - Moist Heat",
        "Core_Anatomy": "Skin (epidermis/dermis).",
        "Pathogenesis_Immediate": "A Scald is specifically caused by moist heat, such as boiling water, hot oil, or steam.",
        "Pathogenesis_Deep": "Scalds are very common in veterinary practice (e.g., a dog pulling a pot of boiling water off a stove). Moist heat penetrates tissue differently than dry heat. Hot water transfers heat into the skin very rapidly and deeply, but usually at a lower maximum temperature (100°C) than a flame. This typically results in extensive superficial (1st degree) or partial-thickness (2nd degree) burns characterized by severe erythema, rapid fluid exudation, and blister formation, rather than the dry charring seen in fire burns.",
        "Why_Not": "Burns are dry heat; Scalds are moist heat.",
        "Wow_Approach": "The immediate first aid for a scald is applying COOL (not freezing/ice) running water for at least 15-20 minutes. This arrests the progression of the thermal wave traveling deeper into the dermis. Ice causes vasoconstriction, worsening the ischemia."
    },
    2665: {
        "topic": "Halogenated Ether - Halothane / Isoflurane",
        "Core_Anatomy": "Pulmonary alveoli and Central Nervous System.",
        "Pathogenesis_Immediate": "Halothane, Isoflurane, and Sevoflurane are classified chemically as Halogenated Ethers (or halogenated alkanes).",
        "Pathogenesis_Deep": "Modern inhalation anaesthetics are volatile liquids that are halogenated (containing fluorine, chlorine, or bromine). Halogenation dramatically reduces flammability and explosiveness (a major problem with historical agents like diethyl ether or cyclopropane). Halothane is a halogenated alkane, while Isoflurane and Sevoflurane are halogenated ethers. They work by dissolving in the lipid bilayer of neuronal membranes or binding directly to GABA-A receptors, inducing unconsciousness, amnesia, and muscle relaxation.",
        "Why_Not": "Nitrous oxide is an inorganic gas. Morphine is an opioid. The halogenated agents are the liquid inhalants used in vaporizers.",
        "Wow_Approach": "Halothane was largely abandoned in veterinary medicine because it heavily sensitizes the myocardium to catecholamines (epinephrine), causing fatal ventricular arrhythmias if the animal becomes stressed or if epinephrine is administered."
    },
    2666: {
        "topic": "Diazepam Reversal Agent - Flumazenil",
        "Core_Anatomy": "Central nervous system (GABA-A receptors).",
        "Pathogenesis_Immediate": "The specific reversal agent (antagonist) for Diazepam and other benzodiazepines is Flumazenil.",
        "Pathogenesis_Deep": "Diazepam (Valium) and Midazolam are benzodiazepines that enhance the inhibitory neurotransmitter GABA in the brain, providing muscle relaxation, anticonvulsant activity, and mild sedation. If an overdose occurs, or if rapid recovery is desired, Flumazenil is administered. Flumazenil acts as a competitive antagonist directly at the benzodiazepine binding site on the GABA-A receptor complex, rapidly displacing the Diazepam and reversing the CNS depression.",
        "Why_Not": "Naloxone reverses opioids. Yohimbine reverses Xylazine. Flumazenil specifically reverses benzodiazepines.",
        "Wow_Approach": "Unlike reversing opioids or alpha-2 agonists (which can abruptly remove analgesia and cause sudden pain responses upon waking), reversing benzodiazepines is very smooth, as benzodiazepines provide no analgesia in the first place."
    },
    2667: {
        "topic": "Xylazine Reversal Agent - Yohimbine",
        "Core_Anatomy": "Central nervous system (Alpha-2 receptors).",
        "Pathogenesis_Immediate": "The specific reversal agent for Xylazine is Yohimbine.",
        "Pathogenesis_Deep": "Xylazine is an alpha-2 adrenoceptor agonist. Yohimbine is a competitive alpha-2 adrenoceptor ANTAGONIST. When administered intravenously, Yohimbine displaces Xylazine from the receptors in the CNS and peripheral vasculature. This completely reverses the sedation, analgesia, bradycardia, and hypotension within 1-3 minutes. The animal goes from being deeply asleep to standing and alert almost immediately.",
        "Why_Not": "Atipamezole is the specific reversal agent for Dexmedetomidine. While it can reverse Xylazine, Yohimbine is the classic specific reversal taught for Xylazine.",
        "Wow_Approach": "Because the reversal is so sudden, it can be dangerous. The sudden return of sympathetic tone and loss of analgesia can cause extreme panic, thrashing, and tachycardia. In large animals, it should be given slowly to allow a controlled standing recovery."
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
