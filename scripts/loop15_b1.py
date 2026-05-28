import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1647: {
        "topic": "VMD 512 - Zoo and Wild Animal Medicine",
        "Core_Anatomy": "Wildlife conservation and captive breeding.",
        "Pathogenesis_Immediate": "This header denotes the specialized section covering the management, restraint, and pathology of non-domesticated species.",
        "Pathogenesis_Deep": "Zoo medicine heavily emphasizes chemical immobilization (darting), zoonotic disease control in captive populations, and nutritional diseases unique to wild animals (like metabolic bone disease in reptiles or capture myopathy in ungulates).",
        "Why_Not": "Domestic animal medicine relies on physical restraint and standard dosages; wildlife medicine requires extreme stress-reduction and allometric scaling for drug dosages.",
        "Wow_Approach": "Always prioritize the safety of the human personnel first when approaching a wild animal question."
    },
    1648: {
        "topic": "Nutritional Mineral Ratios - Calcium to Phosphorus",
        "Core_Anatomy": "Skeletal system and renal excretion.",
        "Pathogenesis_Immediate": "The generally accepted ideal physiological ratio of dietary Calcium to Phosphorus for most domestic animals (including dogs) is approximately 1.2:1 to 2:1.",
        "Pathogenesis_Deep": "Maintaining more calcium than phosphorus in the diet is critical. If dietary phosphorus exceeds calcium (e.g., in an all-meat diet for dogs/cats, or high-grain diet in horses), the blood calcium drops slightly. This triggers the parathyroid gland to release PTH, which actively resorbs calcium from the bones to maintain blood levels. This results in Nutritional Secondary Hyperparathyroidism (Bran disease/Big head in horses, Rubber jaw in dogs).",
        "Why_Not": "An inverted ratio (e.g., 1:3) guarantees severe metabolic bone disease. A massive excess of calcium (e.g., 5:1) will precipitate zinc deficiency (parakeratosis) and bone deformities in growing large-breed puppies.",
        "Wow_Approach": "Never feed a growing large-breed puppy ad-libitum calcium supplements; the excess calcium suppresses normal bone remodeling, leading directly to Osteochondritis Dissecans (OCD) and Hip Dysplasia."
    },
    1649: {
        "topic": "Feline Upper Respiratory Tract Disease (Cat Flu)",
        "Core_Anatomy": "Feline conjunctiva, nasal mucosa, and oral cavity.",
        "Pathogenesis_Immediate": "The clinical syndrome colloquially known as 'Cat-Flu' is primarily caused by Feline Herpesvirus-1 (FHV-1) and Feline Calicivirus (FCV).",
        "Pathogenesis_Deep": "These two viruses account for 80-90% of feline upper respiratory infections. (1) FHV-1 typically causes severe conjunctivitis, dendritic corneal ulcers, and profuse sneezing; it establishes lifelong latency in the trigeminal ganglia, flaring up during stress. (2) FCV primarily causes painful oral ulcerations (especially on the tongue and hard palate), mild sneezing, and sometimes a limping syndrome (transient arthritis).",
        "Why_Not": "Feline Parvovirus causes panleukopenia (severe GI/bone marrow suppression), not respiratory disease. Feline Leukemia Virus causes immunosuppression.",
        "Wow_Approach": "If a sneezing kitten has a severe, crusted, painful eye with a branching (dendritic) ulcer, it is definitely Herpes. If the kitten is drooling profusely because its tongue is ulcerated, it is Calicivirus."
    },
    1650: {
        "topic": "Canine Infectious Tracheobronchitis - Kennel Cough",
        "Core_Anatomy": "Larynx, trachea, and bronchi.",
        "Pathogenesis_Immediate": "In Canine Infectious Tracheobronchitis (Kennel Cough), the classic harsh, 'honking' cough is produced by the inflammation of the Larynx and the Trachea.",
        "Pathogenesis_Deep": "Kennel cough is a highly contagious, multi-agent syndrome (most commonly Bordetella bronchiseptica + Canine Parainfluenza Virus). The pathogens specifically target the ciliated respiratory epithelium of the upper airways (larynx and trachea). They paralyze the mucociliary escalator and cause severe mucosal irritation. When the dog breathes in cold air or pulls on a collar, the inflamed trachea spasms, triggering a loud, dry, paroxysmal cough that often ends with a terminal retch (producing a small puddle of white foam).",
        "Why_Not": "If the inflammation descends into the lungs (alveoli/parenchyma), it progresses to bronchopneumonia, characterized by a soft, moist, productive cough and systemic illness (fever, lethargy), which is much more severe than simple kennel cough.",
        "Wow_Approach": "You can easily elicit this cough during a physical exam by gently squeezing the dog's trachea. A positive 'tracheal pinch' strongly supports the diagnosis of tracheobronchitis."
    },
    1651: {
        "topic": "Polyuria and Polydipsia (PU/PD) - Major Differentials",
        "Core_Anatomy": "Renal tubules and systemic osmolality.",
        "Pathogenesis_Immediate": "Polyuria (excessive urination) and Polydipsia (excessive drinking) occur concurrently in major metabolic diseases like Diabetes Mellitus, Diabetic Ketoacidosis, and Chronic Renal Failure.",
        "Pathogenesis_Deep": "PU/PD is a classic clinical triad symptom. (1) In Diabetes Mellitus / DKA, the blood glucose exceeds the renal threshold (180 mg/dL in dogs). Glucose spills into the urine, acting as an osmotic diuretic that pulls water out of the body (PU). The dog drinks excessively (PD) to compensate for the massive fluid loss. (2) In Chronic Renal Failure, the damaged nephrons lose their ability to concentrate urine (loss of medullary hypertonicity). Water flows straight through (PU), triggering compensatory PD.",
        "Why_Not": "These conditions ALWAYS present with PU/PD. Diseases like acute toxic nephrosis often present with oliguria (decreased urine) or anuria (no urine).",
        "Wow_Approach": "To differentiate: if the urine specific gravity (USG) is incredibly high (e.g., 1.040) but the dog is PU/PD, it is likely Diabetes (the heavy sugar makes the urine dense). If the USG is fixed exactly at 1.008-1.012 (isosthenuria), it is Chronic Renal Failure."
    },
    1652: {
        "topic": "Canine Pyoderma - Systemic Antibiotics",
        "Core_Anatomy": "Epidermis and hair follicles (Staphylococcus pseudintermedius).",
        "Pathogenesis_Immediate": "First-generation Cephalosporins (like Cephalexin) and potentiated sulfonamides are the standard, highly effective drugs of choice for the treatment of bacterial skin diseases (Pyoderma) in dogs.",
        "Pathogenesis_Deep": "Canine pyoderma is almost exclusively caused by Staphylococcus pseudintermedius, a normal skin commensal that overgrows when the skin barrier is compromised (e.g., by allergies or endocrinopathies). S. pseudintermedius naturally produces beta-lactamases, rendering basic penicillin/ampicillin completely useless. First-generation cephalosporins (Cephalexin) are highly resistant to these staphylococcal beta-lactamases, penetrate the skin exceptionally well, and are very safe for the prolonged courses (3-4 weeks) required to clear deep skin infections.",
        "Why_Not": "Using a potent fluoroquinolone (Enrofloxacin) as a first-line drug for simple pyoderma is a massive violation of antibiotic stewardship and rapidly breeds multidrug-resistant infections.",
        "Wow_Approach": "Never treat a deep canine pyoderma for less than 21 days. The rule of thumb is to treat for 1 full week PAST the point of complete clinical and visual resolution to prevent immediate relapse."
    },
    1653: {
        "topic": "VMD Clinical Medicine II - Advanced Pathologies",
        "Core_Anatomy": "Specialized systemic medicine.",
        "Pathogenesis_Immediate": "This header denotes the progression into advanced clinical medicine, often covering specialized topics like dermatology, neurology, and infectious diseases.",
        "Pathogenesis_Deep": "While VMD I covers general metabolic and physiological disturbances, VMD II dives deeply into specific infectious agents, vector-borne diseases, and complex multi-systemic immune-mediated conditions.",
        "Why_Not": "This section expects the clinician to integrate multiple body systems into a single unifying diagnosis.",
        "Wow_Approach": "Pay close attention to geographic and seasonal clues in these questions (e.g., 'a dog presenting in late summer with tick exposure')."
    },
    1654: {
        "topic": "Veterinary Jurisprudence - Subjective Essays",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "This header introduces subjective, essay-based questions on veterinary law, such as the roles of the State Veterinary Council or the legalities of doping.",
        "Pathogenesis_Deep": "Subjective answers require a structured breakdown of the legal definitions, the specific IPC sections, and the ethical responsibilities of the registered veterinary practitioner in preventing fraud (like altering a horse's age by tampering with teeth).",
        "Why_Not": "Vague moral arguments do not earn points; you must cite specific statutory regulations.",
        "Wow_Approach": "Structure jurisprudence essays strictly: Definition, Legal Section, Penalties, and Veterinarian's Duty."
    },
    1659: {
        "topic": "VMD Objective Section Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Marks the beginning of the objective testing phase for VMD, focusing on rapid recall of systemic pathology.",
        "Pathogenesis_Deep": "This section typically heavily tests toxicology and metabolic diseases because these present with acute, pathognomonic objective signs.",
        "Why_Not": "Subjective essays test the pathogenesis; this section tests the exact etiology.",
        "Wow_Approach": "Always read the units carefully in objective questions."
    },
    1660: {
        "topic": "VMD Fill in the Blanks Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of clinical terms without the benefit of elimination.",
        "Pathogenesis_Deep": "This format tests whether a clinical sign or legal parameter has been perfectly linked in memory to its specific pathophysiological etiology or statute.",
        "Why_Not": "Vague answers will not receive credit.",
        "Wow_Approach": "Rely on your first instinct for these blanks; overthinking often leads to changing a correct specific term to an incorrect generic one."
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
