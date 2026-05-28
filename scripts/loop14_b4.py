import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1624: {
        "topic": "Metabolic Acidosis - Clinical Pathology",
        "Core_Anatomy": "Systemic circulation and cellular metabolism.",
        "Pathogenesis_Immediate": "Severe metabolic acidosis (e.g., from grain overload or shock) leads to an increase in blood lactate (L-lactate or D-lactate) and often an increase in Non-Protein Nitrogen (NPN/BUN) if renal perfusion drops.",
        "Pathogenesis_Deep": "Metabolic acidosis occurs when fixed acids accumulate in the blood faster than they can be buffered or excreted. In acute shock or ischemia, cells switch to anaerobic glycolysis, producing massive amounts of L-lactate. In ruminant grain overload, bacteria produce massive amounts of D-lactate. As the acidosis worsens, cardiac output drops, leading to decreased renal perfusion (prerenal azotemia), causing BUN/NPN to rise concurrently.",
        "Why_Not": "Metabolic acidosis never *decreases* lactate; lactate is the primary driver of the acidosis in most hypoxic/ischemic conditions.",
        "Wow_Approach": "Mammalian enzymes can easily clear L-lactate (from exercise), but they cannot metabolize D-lactate (from bacterial fermentation). Therefore, D-lactic acidosis in a grain-overloaded cow is far more neurotoxic and difficult to reverse."
    },
    1625: {
        "topic": "White Muscle Disease - Nutritional Myopathy",
        "Core_Anatomy": "Skeletal and cardiac muscle.",
        "Pathogenesis_Immediate": "The classic nutritional myopathy (White Muscle Disease) in calves and lambs is caused by a combined deficiency of Selenium and Vitamin E.",
        "Pathogenesis_Deep": "Selenium (as a component of Glutathione Peroxidase) and Vitamin E (alpha-tocopherol) are the body's primary antioxidant defense systems. They protect lipid membranes from free-radical damage. When both are deficient, the highly active, oxygen-demanding muscle cells (especially the myocardium and heavily used skeletal muscles like the diaphragm and thighs) undergo massive oxidative lipid peroxidation. The muscle fibers necrotize and calcify, appearing as pale white streaks on necropsy.",
        "Why_Not": "Iron toxicity causes hepatic necrosis. Iron deficiency causes anemia. Only the Se/Vit E combination causes this specific pale, chalky muscle necrosis.",
        "Wow_Approach": "If a calf is born weak, unable to stand, and has a stiff, trembling gait, suspect the skeletal form. If it suddenly drops dead without prior signs, suspect the cardiac form (myocardial necrosis)."
    },
    1626: {
        "topic": "Canine Epilepsy - Long-Term Seizure Control",
        "Core_Anatomy": "Cerebral cortex (GABA receptors).",
        "Pathogenesis_Immediate": "The gold-standard drug of choice for the long-term, chronic control of seizure disorders (epilepsy) in dogs is Phenobarbital.",
        "Pathogenesis_Deep": "Phenobarbital is a long-acting barbiturate that binds to GABA-A receptors in the brain, increasing the duration of chloride channel opening. This hyperpolarizes the neurons, raising the seizure threshold and preventing the spread of abnormal electrical discharges. It is highly effective, inexpensive, and has a predictable half-life, making it ideal for twice-daily oral maintenance therapy.",
        "Why_Not": "Diazepam (Valium) is the drug of choice for stopping an *acute* active seizure (status epilepticus) intravenously, but it cannot be used for long-term control in dogs due to rapid tolerance (it stops working within a week). Acepromazine lowers the seizure threshold and is contraindicated.",
        "Wow_Approach": "Because phenobarbital is heavily metabolized by the liver, it potently induces hepatic cytochrome P450 enzymes. This causes the dog's liver enzymes (specifically ALP) to elevate dramatically on bloodwork, which is a normal, expected finding, not necessarily liver failure."
    },
    1627: {
        "topic": "Post-Mortem Diagnostics - Hypomagnesemia",
        "Core_Anatomy": "Eye (vitreous humor) and central nervous system (CSF).",
        "Pathogenesis_Immediate": "The ideal post-mortem samples for the definitive diagnosis of Hypomagnesaemia (Grass Tetany) are the Vitreous humor of the eye and Cerebrospinal Fluid (CSF).",
        "Pathogenesis_Deep": "In a living animal, serum magnesium reflects the acute status. However, cows with grass tetany often die suddenly in the pasture. Post-mortem, blood serum undergoes rapid autolysis and potassium/magnesium leaks out of the red blood cells, making serum samples useless. Vitreous humor and CSF are physically protected behind the blood-brain/blood-ocular barriers. They degrade very slowly, accurately reflecting the animal's true magnesium status at the exact moment of death for up to 24-48 hours post-mortem.",
        "Why_Not": "Post-mortem blood serum will almost always show falsely elevated magnesium due to cell lysis. Urine magnesium can be low, but is easily contaminated.",
        "Wow_Approach": "Extracting vitreous humor is simple in the field: insert a 16-gauge needle attached to a syringe directly into the posterior chamber of the eye and aspirate the clear jelly."
    },
    1628: {
        "topic": "Uroperitoneum Diagnosis - Creatinine Ratio",
        "Core_Anatomy": "Peritoneal cavity and systemic blood.",
        "Pathogenesis_Immediate": "The definitive biochemical diagnostic marker for Uroperitoneum (a ruptured bladder) in a foal/horse is a Peritoneal Fluid Creatinine level that is at least 2:1 greater than the Serum Creatinine level.",
        "Pathogenesis_Deep": "When the bladder ruptures (common in newborn colt foals during parturition), urine spills directly into the abdomen (uroperitoneum). Urine contains extremely high concentrations of urea, potassium, and creatinine. Urea is a small molecule that equilibrates quickly back into the blood, so peritoneal urea vs serum urea is often similar. However, Creatinine is a large molecule that equilibrates very slowly across the peritoneum. Therefore, comparing the fluid from a belly tap to a simultaneous blood draw will show massive creatinine levels in the belly but lower levels in the blood.",
        "Why_Not": "Comparing urea/BUN is unreliable due to rapid equilibration. Glucose levels are used to diagnose septic peritonitis (bacteria eat the glucose), not uroperitoneum.",
        "Wow_Approach": "A foal with a ruptured bladder will often present with severe hyperkalemia (high blood potassium) which causes fatal cardiac arrhythmias. You must stabilize the heart with IV calcium and drain the belly *before* attempting surgical repair."
    },
    1629: {
        "topic": "VMD Objective Section - True or False Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces statements that must be evaluated for absolute clinical accuracy.",
        "Pathogenesis_Deep": "True/False questions often contain a single modifying word (e.g., 'always', 'never', 'more severe') that dictates the answer.",
        "Why_Not": "Assuming a partially correct statement is true will lead to lost marks.",
        "Wow_Approach": "If a statement contains absolute terms (always/never), it is statistically more likely to be False in medicine."
    },
    1630: {
        "topic": "Equine Colic - Strangulating vs Spasmodic Severity",
        "Core_Anatomy": "Equine gastrointestinal tract and mesenteric vasculature.",
        "Pathogenesis_Immediate": "The statement 'Spasmodic and gas colic is more severe than strangulating colic' is absolutely FALSE.",
        "Pathogenesis_Deep": "Spasmodic colic (hyper-motility/cramping) and gas colic (tympanic distension) are highly painful but generally non-fatal and respond rapidly to medical treatment (Flunixin/Buscopan). Strangulating colic (e.g., large colon volvulus, epiploic foramen entrapment) physically cuts off the mesenteric blood supply to the bowel. This causes acute ischemic necrosis, massive endotoxic shock, and rapid death within hours. Strangulating colic is the most severe, catastrophic emergency in equine practice.",
        "Why_Not": "Believing a gas colic is worse than a volvulus would lead a clinician to delay life-saving emergency surgery.",
        "Wow_Approach": "On clinical exam, a horse with spasmodic colic has loud, hyperactive gut sounds (borborygmi). A horse with a strangulating volvulus will have a completely silent abdomen (dead bowel)."
    },
    1631: {
        "topic": "Copper Deficiency - Steely Wool",
        "Core_Anatomy": "Integument (wool follicles).",
        "Pathogenesis_Immediate": "The classic pathognomonic sign 'Steely Wool' or 'Stringy Wool' in sheep is matched to Copper deficiency.",
        "Pathogenesis_Deep": "Copper is an essential co-factor for the enzyme Tyrosinase (required for melanin pigment production) and for the enzymes that cross-link keratin disulfide bonds in wool. When a sheep is copper deficient, black sheep turn white (achromotrichia), and the wool loses its natural tight crimp. The fleece becomes straight, stringy, and looks like dull steel wire ('steely wool').",
        "Why_Not": "Pantothenic acid causes goose-stepping in pigs. Cobalt deficiency causes ovine white liver disease and wasting.",
        "Wow_Approach": "Wool quality is heavily downgraded at market if it lacks crimp; thus, copper deficiency is a massive economic loss for Merino sheep farmers even before the sheep show systemic signs of illness."
    },
    1632: {
        "topic": "VMD 511 - Animal Welfare, Ethics, and Jurisprudence",
        "Core_Anatomy": "Veterinary Legal Framework.",
        "Pathogenesis_Immediate": "This header introduces the legal and ethical framework governing veterinary practice in India.",
        "Pathogenesis_Deep": "VMD 511 covers the Prevention of Cruelty to Animals Act, the Wildlife Protection Act, veterinary negligence, sound certification (for sale/insurance), and the legal definitions of animal abuse (mischief, maiming).",
        "Why_Not": "This is the only course in the curriculum where the answers are dictated by statutory law rather than biology.",
        "Wow_Approach": "Precision is paramount here; misinterpreting legal terminology in the real world can result in the loss of a veterinary license or criminal charges."
    },
    1635: {
        "topic": "Veterinary Jurisprudence - Mischief (IPC 428/429)",
        "Core_Anatomy": "N/A - Legal Definition.",
        "Pathogenesis_Immediate": "Under the Indian Penal Code (IPC), intentionally causing injury, maiming, or rendering an animal useless (e.g., slashing a cow's udder) is legally defined as 'Mischief'.",
        "Pathogenesis_Deep": "In veterinary jurisprudence, IPC Sections 428 and 429 deal specifically with 'Mischief by killing or maiming animal'. If a malicious neighbor slashes a dairy cow's udder, they haven't just committed animal cruelty; they have committed 'Mischief' by destroying the economic value of the animal. A veterinarian must carefully document the wounds (clean cuts vs accidental barbed wire tears) because their forensic report will form the basis of the police FIR.",
        "Why_Not": "Negligence implies an accident. Cruelty implies suffering without necessarily destroying economic value. Mischief specifically involves intentional destruction/maiming of property.",
        "Wow_Approach": "When performing a medicolegal examination on a maimed animal, never write 'The neighbor did it.' You must only write the objective facts: 'Sharp, incised wound consistent with a bladed instrument, inflicted from a downward angle.'"
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
