import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2008: {
        "topic": "Avian Pathology - Bronze Liver",
        "Core_Anatomy": "Hepatic parenchyma.",
        "Pathogenesis_Immediate": "The pathognomonic necropsy finding of a swollen, friable, 'Bronze' or greenish-brown colored liver in adult poultry is classically matched to Fowl Typhoid.",
        "Pathogenesis_Deep": "Fowl Typhoid is a severe septicemic disease of adult chickens and turkeys caused by Salmonella enterica serovar Gallinarum. The bacteria aggressively invade the liver, causing massive acute hepatomegaly and severe focal necrosis. The resulting profound hepatic dysfunction and bile stasis impart a characteristic bronze or metallic greenish-brown discoloration to the entire liver.",
        "Why_Not": "Pullorum disease (Salmonella Pullorum) affects young chicks (white diarrhea), whereas Fowl Typhoid specifically causes the Bronze Liver in adult birds.",
        "Wow_Approach": "Because Salmonella Gallinarum is transmitted vertically (through the egg), eradication requires blood testing all breeder flocks and culling reactors; you cannot simply treat it with antibiotics."
    },
    2009: {
        "topic": "Bovine Listeriosis - Circling Disease",
        "Core_Anatomy": "Brainstem and Trigeminal nerve.",
        "Pathogenesis_Immediate": "Listeriosis is classically matched with 'Circling Disease' or 'Silage Disease'.",
        "Pathogenesis_Deep": "Listeria monocytogenes thrives in poorly fermented, high-pH silage. When ingested, it penetrates the oral mucosa and travels retrogradely up the cranial nerves into the brainstem, causing unilateral meningoencephalitis. This unilateral damage to the vestibular and facial nuclei forces the cow to compulsively walk in circles toward the paralyzed side of her face.",
        "Why_Not": "It is not a generalized cortical disease (like Rabies), which is why the neurological signs are strictly asymmetrical (unilateral).",
        "Wow_Approach": "If a farmer reports multiple cows walking in circles and dropping their cud, immediately ask if they recently opened a new, perhaps spoiled or moldy, silage bunker."
    },
    2010: {
        "topic": "Bovine Brucellosis - Bang's Disease",
        "Core_Anatomy": "Placentome and reticuloendothelial system.",
        "Pathogenesis_Immediate": "Brucellosis in cattle is historically and classically referred to as 'Bang's Disease'.",
        "Pathogenesis_Deep": "Named after the Danish veterinarian Bernhard Bang who isolated the bacterium (Brucella abortus) in 1897. The bacteria have a massive tropism for erythritol, a sugar alcohol found in high concentrations in the bovine placenta. This causes severe necrotic placentitis and late-term abortion storms. In humans, it causes 'Undulant Fever', characterized by severe, cyclical, recurring fevers.",
        "Why_Not": "Leptospirosis causes early/mid-term abortions and nephritis. Brucellosis is the classic late-term 'Bang's' abortion.",
        "Wow_Approach": "Because it is highly zoonotic, a veterinarian must wear shoulder-length obstetrical sleeves when assisting a cow with a retained placenta, as Brucella can easily penetrate intact human skin."
    },
    2019: {
        "topic": "Subjective Questions - Define/Explain Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces short-answer essay questions requiring precise clinical or legal definitions.",
        "Pathogenesis_Deep": "For definition questions, the examiner expects a strict, textbook definition encompassing the etiology, primary lesion, and clinical outcome, rather than a broad, rambling essay.",
        "Why_Not": "Do not list differentials here; explicitly define the exact term asked.",
        "Wow_Approach": "If defining a disease, always include the causative agent's full binomial name (e.g., 'Caused by *Mycobacterium bovis*')."
    },
    2027: {
        "topic": "VMD Ethics and Jurisprudence Header",
        "Core_Anatomy": "Veterinary Legal Framework.",
        "Pathogenesis_Immediate": "This section tests the legal and ethical framework governing veterinary practice, animal welfare, and forensics.",
        "Pathogenesis_Deep": "Jurisprudence requires rote memorization of the Indian Penal Code (IPC), the Prevention of Cruelty to Animals (PCA) Act, and the rules of the Veterinary Council of India (VCI).",
        "Why_Not": "Answers cannot be deduced biologically; they must match the statutory text.",
        "Wow_Approach": "Always memorize the specific Sections (e.g., IPC 428, 429) and the exact years acts were passed."
    },
    2028: {
        "topic": "Veterinary Jurisprudence - Objective Focus",
        "Core_Anatomy": "Veterinary Legal Framework.",
        "Pathogenesis_Immediate": "Continuation of the Ethics and Jurisprudence section.",
        "Pathogenesis_Deep": "Focuses on the practical application of law in the field, such as how to properly write a post-mortem report that will stand up to cross-examination in a court of law.",
        "Why_Not": "Veterinarians must maintain strict objectivity; they are expert witnesses, not judges.",
        "Wow_Approach": "In forensic reports, never use the word 'Murder' (a human legal term); use 'Malicious Killing' or 'Poisoning'."
    },
    2029: {
        "topic": "Exam Instructions - Time Limit",
        "Core_Anatomy": "N/A - Examination Rules.",
        "Pathogenesis_Immediate": "Standard examination protocol denoting the time limit for Part A.",
        "Pathogenesis_Deep": "Forces rapid recall of objective facts before allowing students to proceed to subjective essays.",
        "Why_Not": "Prevents students from using essay prompts to deduce answers for the objective section.",
        "Wow_Approach": "Pace yourself strictly; do not spend more than 30 seconds on a single MCQ."
    },
    2030: {
        "topic": "Objective Type Questions Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Marks the beginning of the rapid-recall objective testing phase.",
        "Pathogenesis_Deep": "This section heavily tests pathognomonic clinical signs, specific antidotes, and etiological agents.",
        "Why_Not": "Subjective essays test the pathogenesis; this section tests the exact etiology.",
        "Wow_Approach": "Always read the units (mg vs mcg) carefully in pharmacology objective questions."
    },
    2031: {
        "topic": "VMD Fill in the Blanks Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of clinical terms without the benefit of elimination.",
        "Pathogenesis_Deep": "Tests whether a clinical sign or legal parameter has been perfectly linked in memory to its specific pathophysiological etiology.",
        "Why_Not": "Vague answers will not receive credit.",
        "Wow_Approach": "Rely on your first instinct for these blanks."
    },
    2040: {
        "topic": "Companion Animal Endocrinology - Diabetes Mellitus Types",
        "Core_Anatomy": "Pancreatic Islets of Langerhans (Beta cells).",
        "Pathogenesis_Immediate": "Type 1 Diabetes Mellitus is typically seen in dogs, whereas Type 2 is classically seen in cats.",
        "Pathogenesis_Deep": "The pathophysiology of diabetes fundamentally differs between the two species. (1) Dogs almost exclusively develop Type 1 (Insulin-Dependent) Diabetes due to the absolute immune-mediated destruction or severe pancreatitis-induced necrosis of the pancreatic beta cells. They produce zero insulin and require lifelong injections. (2) Cats primarily develop Type 2 (Non-Insulin-Dependent) Diabetes, driven by obesity, high-carbohydrate diets, and severe peripheral insulin resistance, often complicated by amyloid deposition in the islets.",
        "Why_Not": "Treating a diabetic cat exactly like a diabetic dog is a severe error; cats can often achieve diabetic 'remission' (stop needing insulin) if their diet is strictly corrected to high-protein/low-carb and they lose weight.",
        "Wow_Approach": "If an intact female dog develops diabetes, you must spay her immediately; the progesterone produced during diestrus causes massive peripheral insulin resistance, making her diabetes impossible to regulate."
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
