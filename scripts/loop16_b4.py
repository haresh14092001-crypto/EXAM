import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1853: {
        "topic": "Canine Toxicology - Theobromine",
        "Core_Anatomy": "Myocardium and central nervous system.",
        "Pathogenesis_Immediate": "Theobromine is the primary toxic methylxanthine alkaloid found in Chocolate that causes fatal poisoning in dogs.",
        "Pathogenesis_Deep": "Dogs metabolize theobromine extremely slowly compared to humans (half-life of 17.5 hours vs 2-3 hours). Theobromine competitively inhibits cellular phosphodiesterase, leading to a massive accumulation of cyclic AMP (cAMP). It also directly antagonizes adenosine receptors. This causes profound, uninhibited stimulation of the central nervous system and the myocardium. The dog develops severe tachycardia, arrhythmias, muscle tremors, hyperthermia, and fatal status epilepticus.",
        "Why_Not": "Caffeine is also present in chocolate and acts similarly, but theobromine is present in vastly higher, lethal concentrations (especially in dark baker's chocolate).",
        "Wow_Approach": "Because theobromine undergoes extensive enterohepatic recirculation, you must administer activated charcoal repeatedly (every 4-6 hours) for 24-48 hours, not just a single dose, to prevent the dog from reabsorbing the toxin."
    },
    1854: {
        "topic": "Bovine Toxicology - Nitrate Poisoning",
        "Core_Anatomy": "Erythrocytes (hemoglobin).",
        "Pathogenesis_Immediate": "Nitrate poisoning in ruminants is classically treated with an intravenous injection of Methylene Blue.",
        "Pathogenesis_Deep": "When cattle graze heavily fertilized pastures or drought-stressed sorghum, they ingest massive amounts of nitrates. Rumen bacteria rapidly reduce nitrate (NO3) to highly toxic nitrite (NO2). Nitrite oxidizes the iron in hemoglobin from ferrous (Fe2+) to ferric (Fe3+), creating methemoglobin (which cannot carry oxygen). The blood turns chocolate brown, and the cow suffocates internally. Methylene blue acts as an artificial electron donor, rapidly reducing the ferric iron back to ferrous iron and instantly restoring the blood's oxygen-carrying capacity.",
        "Why_Not": "Sodium thiosulfate is the antidote for Cyanide, not Nitrate. 10% Calcium is for Milk Fever.",
        "Wow_Approach": "Methylene blue actually briefly forms *more* methemoglobin before reducing it, so administering an accidental overdose can paradoxically kill the cow by worsening the hypoxia."
    },
    1855: {
        "topic": "Canine Nutrition - Obesity Management",
        "Core_Anatomy": "Gastrointestinal tract (satiety centers).",
        "Pathogenesis_Immediate": "The primary dietary modification for managing Obesity in companion animals is switching to a High Fiber diet.",
        "Pathogenesis_Deep": "Obesity requires caloric restriction, but simply feeding less of a normal maintenance diet leaves the stomach physically empty, causing the dog to beg incessantly due to lack of gastric stretch-receptor activation (ghrelin release). A high-fiber diet utilizes insoluble carbohydrates (like cellulose or beet pulp) that provide physical bulk and trigger gastric stretch receptors without adding digestible calories. This safely induces satiety while the animal loses body fat.",
        "Why_Not": "A high-fat diet increases caloric density. A high-protein diet is used for muscle wasting (cachexia) or feline diabetes, but fiber is the key for mechanical satiety in dogs.",
        "Wow_Approach": "When prescribing a high-fiber weight loss diet, you must warn the owner that the dog's fecal volume will increase significantly, which is a normal, expected consequence of the indigestible bulk."
    },
    1865: {
        "topic": "Exam Instructions Header",
        "Core_Anatomy": "N/A - Examination Rules.",
        "Pathogenesis_Immediate": "Standard examination protocol header denoting the time limit for the objective section.",
        "Pathogenesis_Deep": "Objective questions require rapid cognitive recall; strict time limits prevent students from utilizing extensive deductive reasoning, forcing them to rely on ingrained rote knowledge.",
        "Why_Not": "Subjective sections allow for prolonged synthesis of information.",
        "Wow_Approach": "In objective exams, always answer the questions you know instantly first, then circle back to the challenging ones to maximize point yield."
    },
    1866: {
        "topic": "VMD Objective Section Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Marks the beginning of the objective testing phase for VMD, focusing on rapid recall of systemic pathology.",
        "Pathogenesis_Deep": "This section typically heavily tests toxicology and metabolic diseases because these present with acute, pathognomonic objective signs.",
        "Why_Not": "Subjective essays test the pathogenesis; this section tests the exact etiology.",
        "Wow_Approach": "Always read the units carefully in objective questions."
    },
    1867: {
        "topic": "VMD Fill in the Blanks Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of clinical terms without the benefit of elimination.",
        "Pathogenesis_Deep": "This format tests whether a clinical sign or legal parameter has been perfectly linked in memory to its specific pathophysiological etiology or statute.",
        "Why_Not": "Vague answers will not receive credit.",
        "Wow_Approach": "Rely on your first instinct for these blanks; overthinking often leads to changing a correct specific term to an incorrect generic one."
    },
    1885: {
        "topic": "VMD Objective Section - Multiple Choice Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces standard MCQs, requiring the clinician to eliminate distractor etiologies.",
        "Pathogenesis_Deep": "MCQs in veterinary medicine often pair a disease with its most confusing differential. Success depends on identifying the single 'rule-out' clinical sign.",
        "Why_Not": "Do not select an answer simply because it causes similar signs; it must cause the EXACT signs described.",
        "Wow_Approach": "Read all four options before selecting an answer; the 'best' answer is required, not just the first plausible one."
    },
    1886: {
        "topic": "Tuberculosis Prophylaxis - BCG Vaccine",
        "Core_Anatomy": "Cell-mediated immune system (Macrophages).",
        "Pathogenesis_Immediate": "The B.C.G. (Bacillus Calmette-Guérin) vaccine is utilized specifically against Tuberculosis.",
        "Pathogenesis_Deep": "BCG is a live, attenuated strain of Mycobacterium bovis developed by passaging the bacteria hundreds of times over 13 years until it lost its virulence. It is highly effective in humans for preventing severe childhood TB (like TB meningitis). However, its use in veterinary medicine (cattle) is strictly prohibited in most countries. If you vaccinate a cow with BCG, she will test positive on the mandatory Intradermal Tuberculin Test, making it impossible to distinguish between a vaccinated cow and a cow actively infected with virulent field TB.",
        "Why_Not": "Black quarter uses a Clostridium chauvoei bacterin. Brucellosis uses Strain 19 or RB51.",
        "Wow_Approach": "While banned for cattle, BCG is increasingly being researched as a bait-vaccine for wildlife reservoirs of TB, such as badgers in the UK or possums in New Zealand."
    },
    1887: {
        "topic": "Bovine Actinobacillosis - Wooden Tongue (Repeated)",
        "Core_Anatomy": "Lingual soft tissue and regional lymph nodes.",
        "Pathogenesis_Immediate": "The classic bovine disease 'Wooden tongue' is caused by Actinobacillus lignieresii.",
        "Pathogenesis_Deep": "A. lignieresii is a Gram-negative normal commensal of the bovine mouth. When coarse, stemmy forage physically pierces the mucosal barrier of the tongue, the bacteria invade the deep muscle layers. They provoke a massive, chronic, pyogranulomatous inflammatory response. The host encapsulates the bacteria in dense fibrous connective tissue, replacing the normal flexible muscle. The tongue becomes a rigid, swollen, immobile block of fibrous tissue ('wood'), forcing the cow to drool profusely and starve to death.",
        "Why_Not": "Actinomyces bovis (a Gram-positive bacterium) causes Lumpy Jaw (osteomyelitis of the mandible/maxilla), not wooden tongue. M. tuberculosis causes chronic wasting/pneumonia.",
        "Wow_Approach": "To definitively diagnose it, biopsy the tongue and look for classic 'sulfur granules' (club-shaped bacterial colonies surrounded by antigen-antibody complexes) under the microscope."
    },
    1888: {
        "topic": "Ovine Enterotoxemia - Pulpy Kidney Disease",
        "Core_Anatomy": "Renal parenchyma, intestines, and brain.",
        "Pathogenesis_Immediate": "The classic, rapidly fatal 'Pulpy kidney disease' in sheep is caused specifically by Clostridium perfringens type-D.",
        "Pathogenesis_Deep": "C. perfringens Type D is a normal intestinal commensal. When a sheep is suddenly switched to a rich, high-carbohydrate grain diet, the excess starch overflows into the intestine. This provides a massive food source for Type D, which multiplies explosively and secretes the Epsilon toxin. The Epsilon toxin destroys the vascular endothelium, causing severe edema in the brain (Focal Symmetrical Encephalomalacia) and massive, rapid post-mortem autolysis of the kidneys, turning them into a soft, mushy, 'pulpy' mass.",
        "Why_Not": "Type A causes necrotic enteritis in poultry. Type B causes lamb dysentery. Type C causes 'Struck' (hemorrhagic enterotoxemia). ONLY Type D produces the specific Epsilon toxin that causes Pulpy Kidney.",
        "Wow_Approach": "Because the disease is triggered by rich diets, it almost exclusively kills the fastest-growing, healthiest, 'best-looking' lambs in the flock."
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
