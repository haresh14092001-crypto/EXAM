import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3254: {
        "topic": "Sterilization of Sharp Instruments",
        "Core_Anatomy": "Surgical instruments.",
        "Pathogenesis_Immediate": "Sharp surgical instruments (like scissors and scalpel handles) are traditionally sterilized by a Hot Air Oven (dry heat).",
        "Pathogenesis_Deep": "Autoclaving uses moist heat (steam under pressure). The moisture and high pressure rapidly dull the delicate cutting edges of sharp instruments and cause microscopic rusting at the hinges. Therefore, instruments requiring extreme sharpness are sterilized using Dry Heat (a Hot Air Oven at 160°C for 2 hours) or by cold chemical sterilization (soaking in 2% Glutaraldehyde).",
        "Why_Not": "Ethylene oxide gas is used for heat-sensitive plastics (endotracheal tubes). Gamma irradiation is used for commercial pre-packaged single-use items (suture packets).",
        "Wow_Approach": "Scalpel blades themselves are never sterilized in the clinic; they are manufactured sterile and simply discarded after a single use."
    },
    3255: {
        "topic": "Eschar - Burn Slough",
        "Core_Anatomy": "Skin epidermis and dermis.",
        "Pathogenesis_Immediate": "An Eschar is commonly caused due to a Burn.",
        "Pathogenesis_Deep": "An eschar is a thick, dry, black, leathery piece of dead (necrotic) tissue. It is the classic hallmark of a full-thickness (3rd degree) thermal or chemical burn. The intense heat instantly coagulates the proteins in the skin, turning it into a rigid crust.",
        "Why_Not": "An abscess contains liquid pus. A tumor is living, growing tissue. An eschar is specifically a plaque of dry, coagulated, dead burn tissue.",
        "Wow_Approach": "Because a 3rd-degree burn destroys the dermal nerve endings, the eschar itself is completely painless. However, it must be surgically removed (debrided) because it acts like a rigid tourniquet (preventing blood flow to underlying tissues) and provides a massive breeding ground for bacteria."
    },
    3256: {
        "topic": "Soda Lime Composition",
        "Core_Anatomy": "Anaesthetic machine (Rebreathing circuit).",
        "Pathogenesis_Immediate": "The primary active ingredient in a soda lime canister is Calcium Hydroxide.",
        "Pathogenesis_Deep": "In a rebreathing anaesthetic circuit, the patient exhales Carbon Dioxide (CO2) back into the machine. If this CO2 is not removed, the patient will quickly die of respiratory acidosis. The exhaled gas passes through the soda lime canister. Soda lime is primarily composed of Calcium Hydroxide (94%), with small amounts of Sodium Hydroxide (5%) and Potassium Hydroxide (1%) acting as catalysts. A chemical reaction occurs, neutralizing the CO2 gas into solid Calcium Carbonate, water, and heat.",
        "Why_Not": "Sodium chloride is table salt. Calcium chloride is a calcium supplement.",
        "Wow_Approach": "The chemical reaction releases water and heat. This is actually highly beneficial, as it physically warms and humidifies the dry, cold oxygen coming from the tank before it goes back into the patient's lungs, helping to prevent intraoperative hypothermia."
    },
    3257: {
        "topic": "Steroidal Anaesthetic - Alfaxalone",
        "Core_Anatomy": "Central nervous system (GABA receptors).",
        "Pathogenesis_Immediate": "Alfaxalone (Alphaxalone) is classified as a Steroidal Anaesthetic.",
        "Pathogenesis_Deep": "Alfaxalone is a neuroactive steroid molecule. Despite being a steroid structurally, it has absolutely zero glucocorticoid or mineralocorticoid (hormonal) effects. Instead, it binds to GABA-A receptors in the brain to produce rapid, profound unconsciousness. It is used as an IV induction agent similar to Propofol.",
        "Why_Not": "Azaperone and Acepromazine are tranquilizers. Etorphine is a massive opioid. Alfaxalone is the only steroidal induction agent.",
        "Wow_Approach": "Because Alfaxalone causes virtually zero cardiovascular depression, it is the absolute gold-standard induction agent for dogs with severe heart failure or animals presenting in hypovolemic shock."
    },
    3258: {
        "topic": "Oxygen Cylinder PSI (Review)",
        "Core_Anatomy": "Anaesthetic machine.",
        "Pathogenesis_Immediate": "The pressure of a full medical oxygen cylinder is 2200 psi.",
        "Pathogenesis_Deep": "Reiterating that oxygen is stored as a highly compressed gas, and the pressure drops linearly as the tank empties.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3259: {
        "topic": "Ultra-Short Acting Barbiturate - Thiopental",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "Thiopental sodium is the classic Ultra-short acting barbiturate.",
        "Pathogenesis_Deep": "As a thiobarbiturate (having a sulfur atom at position 2 of the ring), Thiopental is extremely lipid-soluble. When injected IV, it crosses the blood-brain barrier instantly, inducing unconsciousness in less than 30 seconds. Its effect only lasts 10-15 minutes because it rapidly redistributes OUT of the brain and into the body's muscle and fat.",
        "Why_Not": "Phenobarbital is LONG-acting (used as a daily oral anti-seizure medication). Pentobarbital is SHORT-acting (lasts 1-2 hours, historically used for surgery, now mostly for euthanasia).",
        "Wow_Approach": "Because greyhounds have virtually no body fat, Thiopental has nowhere to redistribute to. If you induce a greyhound with Thiopental, it will sleep for 2 days instead of 10 minutes. It is contraindicated in sighthounds."
    },
    3260: {
        "topic": "Tungsten Melting Point",
        "Core_Anatomy": "X-ray tube target/filament.",
        "Pathogenesis_Immediate": "The melting point of Tungsten in the X-ray tube is 3370°C.",
        "Pathogenesis_Deep": "When high-speed electrons crash into the anode target to create X-rays, 99% of their kinetic energy is converted instantly into pure heat, and only 1% becomes X-rays. Because the heat generated is so massive, the target MUST be made of a metal that will not melt. Tungsten has the highest melting point of all metals in pure form (3370°C / 6100°F).",
        "Why_Not": "N/A",
        "Wow_Approach": "To further prevent melting, most modern high-powered veterinary machines use a 'Rotating Anode'. The tungsten disk spins at 3,000 RPM during the exposure so that the electron beam constantly hits a fresh, cooler spot on the target, spreading the heat over a large area."
    },
    3262: {
        "topic": "Radiosensitive Tissue Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Kidney, Brain, Nerve, Bone Marrow) for the most radiosensitive tissue question.",
        "Pathogenesis_Deep": "Structural artifact. Bone marrow is the correct answer.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3263: {
        "topic": "Ultrasound Modes Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (B-Mode, A-Mode, M-Mode, E-Mode) for the echocardiography question.",
        "Pathogenesis_Deep": "Structural artifact. M-Mode is the correct answer.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3264: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching question section.",
        "Pathogenesis_Deep": "Structural marker.",
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
print(f"Batch 4/5 DONE: Updated {updated} questions.")
