import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2699: {
        "topic": "Sterilization Methods Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Sterilization method question options (Autoclaving, Ethylene oxide, Hot air oven, Irradiation).",
        "Pathogenesis_Deep": "Knowing when to use each method is critical. (1) Autoclaving (Steam under pressure, 121°C for 15 mins) = routine surgical packs and drapes. (2) Ethylene Oxide (EtO gas) = heat-sensitive plastics, endoscopes, catheters. (3) Hot Air Oven (160°C for 2 hours) = sharp instruments (avoids rusting from steam), glassware, oils/powders. (4) Gamma Irradiation = commercial single-use items (sutures, needles).",
        "Why_Not": "Putting an expensive flexible endoscope in an autoclave will melt and destroy it. It must be sterilized with EtO or cold chemical sterilants (Glutaraldehyde).",
        "Wow_Approach": "EtO is highly toxic, carcinogenic, and explosive. After EtO sterilization, items MUST be aerated for 12-24 hours before use, or the residual gas will cause severe chemical burns to the patient's tissues."
    },
    2700: {
        "topic": "Eschar - Thermal Burn",
        "Core_Anatomy": "Skin (Epidermis and Dermis).",
        "Pathogenesis_Immediate": "An Eschar is a dry, dark scab or falling away of dead skin, commonly caused by a Burn (specifically, a full-thickness or 3rd-degree burn).",
        "Pathogenesis_Deep": "When dry heat (fire) completely destroys the full thickness of the skin, the dead tissue undergoes coagulative necrosis. The proteins denature and dehydrate, forming a tough, leathery, dark, inelastic plaque called an eschar. The eschar acts as a rigid tourniquet. If an eschar forms circumferentially around a limb or the thorax, it completely restricts swelling and movement. As underlying tissue swells from inflammation, the unyielding eschar causes compartment syndrome, cutting off arterial blood supply to the limb.",
        "Why_Not": "A scald causes blisters (vesicles) rather than a dry leathery eschar. An abscess contains liquid pus.",
        "Wow_Approach": "In human and veterinary burn units, a circumferential eschar requires an immediate emergency surgical procedure called an 'Escharotomy'—making deep longitudinal incisions completely through the dead leathery skin to allow the underlying tissues to expand and restore blood flow."
    },
    2701: {
        "topic": "Soda Lime - Calcium Hydroxide",
        "Core_Anatomy": "Anaesthetic breathing circuit (circle system).",
        "Pathogenesis_Immediate": "The active ingredient in a Soda Lime canister used in an anaesthetic machine is Calcium Hydroxide (Ca(OH)2).",
        "Pathogenesis_Deep": "In a rebreathing (circle) anaesthetic system, the patient exhales carbon dioxide back into the circuit. To prevent lethal hypercapnia, the exhaled gas passes through a canister of Soda Lime. The primary component (94%) is Calcium Hydroxide, mixed with small amounts of Sodium Hydroxide (5%). The CO2 reacts chemically with the water and hydroxides to form Calcium Carbonate, water, and heat (an exothermic neutralization reaction).",
        "Why_Not": "Calcium chloride and sodium chloride are salts, not alkaline hydroxides, and do not absorb CO2.",
        "Wow_Approach": "Soda lime contains a pH-sensitive dye (usually Ethyl Violet). As the alkaline calcium hydroxide is converted to neutral calcium carbonate, the pH drops, and the granules turn PURPLE. This visual indicator tells the anaesthetist the granules are exhausted. A critical safety point: exhausted granules that are rested may temporarily revert to white, so they must be changed based on hours of use, not just color."
    },
    2702: {
        "topic": "Steroidal Anaesthetic - Alfaxalone",
        "Core_Anatomy": "Central nervous system (GABA-A receptors).",
        "Pathogenesis_Immediate": "Alphaxalone (Alfaxalone) is classified as a Steroidal Anaesthetic.",
        "Pathogenesis_Deep": "Alfaxalone is a neuroactive steroid molecule. Despite its steroid ring structure, it has absolutely no glucocorticoid, mineralocorticoid, or sex hormone activity. It works similarly to propofol and barbiturates by enhancing the inhibitory effects of GABA at the GABA-A receptor. It is an extremely safe, rapidly metabolized intravenous induction agent that provides minimal cardiovascular depression. Unlike Propofol, Alfaxalone can also be given Intramuscularly (IM) to provide sedation in aggressive cats or exotic species.",
        "Why_Not": "Azaperone is a butyrophenone. Acepromazine is a phenothiazine. Etorphine is an opioid.",
        "Wow_Approach": "The original formulation of Alfaxalone (Saffan) was dissolved in Cremophor EL (castor oil), which caused massive histamine release and anaphylaxis in dogs. The modern formulation (Alfaxan) is dissolved in a cyclodextrin ring (sugar), eliminating this allergic reaction and making it completely safe for both dogs and cats."
    },
    2703: {
        "topic": "Oxygen Cylinder Pressure",
        "Core_Anatomy": "Anaesthetic machine physics.",
        "Pathogenesis_Immediate": "The standard pressure of a completely full medical Oxygen cylinder is approximately 2100 to 2200 psi.",
        "Pathogenesis_Deep": "Medical oxygen is stored as a compressed GAS (not a liquid) inside cylinders (E-tanks or H-tanks) painted White (international) or Green (USA). Because it is a true gas at room temperature, Boyle's Law applies: the pressure inside the tank is directly proportional to the volume of gas remaining. A full E-tank reads ~2200 psi and holds roughly 660 Liters. If the gauge drops to 1100 psi, exactly half the volume (330 Liters) remains.",
        "Why_Not": "Nitrous oxide (blue cylinder) is stored as a LIQUID under pressure. Its gauge will read 745 psi and will not drop until every drop of liquid has boiled off into gas. Therefore, a Nitrous gauge does not tell you how much is left until the tank is almost totally empty.",
        "Wow_Approach": "To calculate how many minutes of oxygen you have left before the patient wakes up: (Tank Pressure in PSI x 0.3) = Liters remaining. Divide by the O2 flow rate (L/min) to get minutes remaining."
    },
    2704: {
        "topic": "Ultra-Short Acting Barbiturate - Thiopental",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "Thiopental sodium (Thiopentone) is the classic Ultra-short acting barbiturate.",
        "Pathogenesis_Deep": "Barbiturates are classified by their duration of action. (1) Long-acting (Phenobarbital): 12-24 hours, used for chronic epilepsy control. (2) Short-acting (Pentobarbital): 1-2 hours, historically used for anaesthesia, now primarily used for Euthanasia. (3) Ultra-short acting (Thiopental, Methohexital): 10-15 minutes, used solely for rapid induction of anaesthesia prior to intubation. As previously noted, Thiopental's ultra-short action is due to rapid redistribution into fat, not hepatic metabolism.",
        "Why_Not": "Phenobarbital takes hours to work and lasts all day. Pentobarbital is too long for a smooth surgical induction and recovery. Thiopental acts in 30 seconds and lasts 15 minutes.",
        "Wow_Approach": "Thiopental is extremely alkaline (pH 10-11). If injected perivascularly (outside the vein), it causes severe, agonizing tissue necrosis and sloughing. If this happens, the area must be immediately infiltrated with saline and Lidocaine to dilute the drug and prevent vasospasm."
    },
    2705: {
        "topic": "X-ray Tube - Tungsten Melting Point",
        "Core_Anatomy": "Radiographic physics (X-ray tube).",
        "Pathogenesis_Immediate": "The melting point of Tungsten (used in the X-ray tube target) is 3370°C.",
        "Pathogenesis_Deep": "Inside an X-ray tube, high-speed electrons from the cathode crash into the anode target to produce X-rays. This process is incredibly inefficient: 99% of the kinetic energy is converted into HEAT, and only 1% becomes X-ray photons. The target must therefore be made of a material that can withstand extreme, sudden heat without melting. Tungsten (W, atomic number 74) is ideal because of its extremely high melting point (3370°C) and its high atomic number, which improves X-ray production efficiency (Bremsstrahlung radiation).",
        "Why_Not": "Lower melting point metals (like copper or aluminum) would instantly vaporize under the electron bombardment.",
        "Wow_Approach": "To dissipate this massive heat, the Tungsten target is embedded in a large block of copper (an excellent heat conductor), and in high-output machines, the entire anode rotates rapidly during exposure so the electron beam doesn't hit the exact same spot twice, preventing the target from melting."
    },
    2706: {
        "topic": "Radiation Susceptibility - Bone Marrow",
        "Core_Anatomy": "Hematopoietic stem cells.",
        "Pathogenesis_Immediate": "The tissue most susceptible to radiation damage is the Bone Marrow.",
        "Pathogenesis_Deep": "Revisiting the Law of Bergonié and Tribondeau: rapidly dividing, poorly differentiated cells are highly radiosensitive. The bone marrow is the body's primary factory for erythrocytes, leukocytes, and platelets, constantly undergoing rapid mitosis. When exposed to high doses of whole-body ionizing radiation (e.g., nuclear accidents, severe overexposure), the marrow stem cells are destroyed. The animal will die 2-4 weeks later from overwhelming sepsis (due to neutropenia) or massive hemorrhage (due to thrombocytopenia).",
        "Why_Not": "Nerves and Brain cells are fully differentiated and do not divide. They are the most radio-resistant tissues in the body.",
        "Wow_Approach": "Other highly radiosensitive tissues include the gastrointestinal crypt cells (leading to sloughing of the gut lining and bloody diarrhea) and the gonads (leading to sterility). This is why lead aprons used by radiographers specifically shield the torso (marrow, gut, gonads)."
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
