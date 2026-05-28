import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1577: {
        "topic": "Nutritional Pathology - Responsive Diseases",
        "Core_Anatomy": "Systemic metabolism.",
        "Pathogenesis_Immediate": "Deficiency diseases are clinically classified as 'Responsive Diseases' because providing the missing nutrient rapidly and specifically reverses the clinical signs.",
        "Pathogenesis_Deep": "Unlike infectious or neoplastic diseases which cause irreversible tissue destruction or require complex immune clearance, nutritional deficiencies (e.g., scurvy, rickets, thiamine deficiency) represent a stalled biochemical pathway due to a missing co-factor. When the specific vitamin or mineral is administered intravenously or orally, the biochemical pathway instantly resumes. The rapid, dramatic clinical recovery essentially serves as both the definitive diagnostic test and the cure.",
        "Why_Not": "Infectious diseases are 'antimicrobial-responsive', but nutritional diseases are uniquely defined by their immediate physiological response to a single dietary element.",
        "Wow_Approach": "This principle is used diagnostically: if a polioencephalomalacia (PEM) goat recovers its vision within 12 hours of receiving IV Thiamine (B1), the diagnosis is confirmed without needing a brain biopsy."
    },
    1579: {
        "topic": "Piglet Anemia - Etiology and Clinical Signs",
        "Core_Anatomy": "Bone marrow, erythrocytes, and hepatic iron stores.",
        "Pathogenesis_Immediate": "Piglet anemia is a severe microcytic, hypochromic anemia caused by an absolute Iron deficiency in rapidly growing neonatal piglets kept indoors.",
        "Pathogenesis_Deep": "Piglets are born with extremely low hepatic iron stores (only ~50 mg). Sow's milk is notoriously deficient in iron (providing only 1 mg/day). However, the modern piglet has a massive genetic growth rate, requiring 7-10 mg of iron per day to synthesize hemoglobin for its rapidly expanding blood volume. If raised on concrete (unable to root in iron-rich soil), the piglet rapidly exhausts its iron reserves by day 7-10, leading to severe anemia, pale mucous membranes, 'thumps' (spasmodic diaphragmatic breathing due to hypoxia), and high susceptibility to enteritis.",
        "Why_Not": "Copper or Cobalt deficiency also causes anemia, but iron is the primary, explosive deficiency seen universally in indoor swine operations.",
        "Wow_Approach": "A classic sign of advanced piglet anemia is wrinkly, pale skin with generalized edema, particularly around the neck and jowls, often called 'Paper-Skin' or 'Edema of the Neck'."
    },
    1580: {
        "topic": "Piglet Anemia - Prevention and Treatment",
        "Core_Anatomy": "Intramuscular tissue (neck) and systemic blood.",
        "Pathogenesis_Immediate": "The gold standard treatment and prevention for piglet anemia is the intramuscular injection of 200 mg of Iron Dextran.",
        "Pathogenesis_Deep": "Because oral iron is poorly absorbed and can cause severe diarrhea in neonates, parenteral iron is required. Iron dextran is a large molecular complex that is slowly absorbed from the injection site by macrophages, transporting the iron to the liver and bone marrow for erythropoiesis over several weeks. It must be administered deep IM into the neck muscles (behind the ear) to avoid staining the valuable ham muscles in the hindleg.",
        "Why_Not": "Painting the sow's udder with iron sulfate is an older, messy, and unreliable method. Injection ensures every piglet receives the exact 200 mg required to bridge them until they start eating solid creep feed.",
        "Wow_Approach": "Always inject Iron Dextran strictly between Day 1 and Day 3 of life. Delaying until Day 7 guarantees subclinical growth retardation and compromises the immune system."
    },
    1584: {
        "topic": "Ruminal Environment - Normal pH",
        "Core_Anatomy": "Rumen fluid and ruminal microbiome.",
        "Pathogenesis_Immediate": "The normal physiological pH of rumen fluid in a healthy, forage-fed bovine is slightly acidic, ranging from 6.5 to 6.8.",
        "Pathogenesis_Deep": "Rumen microbes continuously ferment carbohydrates into Volatile Fatty Acids (VFAs) like acetate, propionate, and butyrate, which drive the pH down. The cow constantly buffers this acid by secreting massive amounts of alkaline saliva (rich in bicarbonate and phosphate) during rumination (cud-chewing). This balance maintains the pH at 6.5-6.8, which is optimal for the cellulolytic bacteria required to digest roughage.",
        "Why_Not": "A pH below 5.5 indicates Acute Rumen Lactic Acidosis (grain overload), where Streptococcus bovis produces lactic acid, killing off the normal flora. A pH > 7.5 indicates ruminal putrefaction or urea toxicity.",
        "Wow_Approach": "You can roughly estimate the cow's diet by her rumen pH: a pasture-fed cow will be near 6.8, while a high-producing dairy cow on a high-grain TMR will naturally sit lower, around 6.0-6.2."
    },
    1585: {
        "topic": "Falling Disease - Bovine Copper Deficiency",
        "Core_Anatomy": "Myocardium and systemic vascular system.",
        "Pathogenesis_Immediate": "The sudden death syndrome known as 'Falling Disease' in cattle is caused by a severe deficiency of Copper.",
        "Pathogenesis_Deep": "Copper is a vital component of the enzyme lysyl oxidase, which is required to cross-link collagen and elastin. In severely copper-deficient cattle (often due to high dietary molybdenum/sulfur which binds copper in the rumen), the elastin in the cardiovascular system becomes weak. The myocardium undergoes acute atrophy and fibrosis. When the cow is stressed or exercised, she suffers acute heart failure or spontaneous aortic rupture, collapsing and dying instantly ('Falling Disease').",
        "Why_Not": "Selenium deficiency causes White Muscle Disease (skeletal muscle). Magnesium deficiency causes Grass Tetany (convulsions). Copper specifically causes the sudden cardiovascular collapse of Falling Disease.",
        "Wow_Approach": "Before the fatal cardiac collapse, copper-deficient cattle will often show classic early signs: severe depigmentation of the hair (achromotrichia), specifically presenting as 'spectacles' (pale rings) around the eyes."
    },
    1587: {
        "topic": "Physical Examination - General Principles",
        "Core_Anatomy": "Multisystemic clinical examination.",
        "Pathogenesis_Immediate": "The four pillars of physical examination are Inspection, Palpation, Percussion, and Auscultation.",
        "Pathogenesis_Deep": "A structured examination always follows a strict sequence to avoid altering physiological sounds before they can be assessed. (1) Inspection: visual observation from a distance (mentation, respiratory rate). (2) Palpation: feeling for heat, swelling, or pain. (3) Percussion: tapping to assess underlying tissue density (gas vs fluid). (4) Auscultation: listening with a stethoscope (heart, lungs, GI tract).",
        "Why_Not": "Skipping directly to auscultation without inspecting the animal from a distance often causes the clinician to miss critical postural clues (e.g., abducted elbows in pneumonia).",
        "Wow_Approach": "In the abdomen, always Auscultate BEFORE you Palpate or Percuss, because aggressive palpation can temporarily alter or stop normal bowel sounds (borborygmi)."
    },
    1588: {
        "topic": "Ascites Diagnosis - Fluid Thrill / Ballotment",
        "Core_Anatomy": "Peritoneal cavity and abdominal wall.",
        "Pathogenesis_Immediate": "The physical examination technique most important for diagnosing ascites (free fluid in the abdomen) in dogs is Tactile Percussion (Fluid Thrill) or Ballotment.",
        "Pathogenesis_Deep": "Ascites is the accumulation of transudate/exudate in the peritoneal space (commonly due to right-sided heart failure or hypoalbuminemia). To diagnose it physically, the clinician places one hand flat against one side of the dog's abdomen and sharply taps (flicks) the opposite side. If free fluid is present, a distinct mechanical wave (fluid thrill) will travel through the abdomen and strike the resting hand. Ballotment involves pushing the fist deep into the abdomen; in ascites, the solid organs will bounce away and float back to strike the hand.",
        "Why_Not": "Auscultation is useless for detecting free abdominal fluid (though it is used for pleural effusion). Simple palpation may just feel like fat or an enlarged organ.",
        "Wow_Approach": "If you detect a fluid wave, the immediate next step is an abdominocentesis (belly tap) using a 22-gauge needle to classify the fluid as a transudate, modified transudate, or exudate."
    },
    1589: {
        "topic": "Systemic Acid-Base - Normal Blood pH",
        "Core_Anatomy": "Systemic arterial/venous blood and renal/respiratory buffers.",
        "Pathogenesis_Immediate": "The normal physiological pH of systemic blood in a healthy animal is tightly regulated between 7.35 and 7.45.",
        "Pathogenesis_Deep": "Blood pH must be strictly maintained slightly on the alkaline side of neutral (7.40) to preserve the structural conformation and function of all systemic enzymes and proteins. It is regulated by three systems: (1) Blood buffers (bicarbonate, hemoglobin) react instantly. (2) Respiratory system adjusts CO2 exhalation within minutes. (3) Kidneys excrete H+ or retain HCO3- over hours to days. A pH < 7.35 is acidemia; a pH > 7.45 is alkalemia.",
        "Why_Not": "A blood pH of 7.0 is theoretically 'neutral' in chemistry, but in biology, it represents catastrophic, fatal acidemia (e.g., severe diabetic ketoacidosis).",
        "Wow_Approach": "Arterial blood is slightly more alkaline (closer to 7.45) than venous blood (closer to 7.35) because venous blood carries acidic dissolved CO2 back to the lungs."
    },
    1590: {
        "topic": "Myocardial Affections - Cardiac Arrhythmias",
        "Core_Anatomy": "Myocardium, SA node, and Purkinje fibers.",
        "Pathogenesis_Immediate": "Affections of the myocardium (heart muscle) are most characteristically defined clinically by the presence of an Arrhythmia.",
        "Pathogenesis_Deep": "The myocardium contains the specialized electrical conduction system of the heart. When the heart muscle itself is damaged—whether by ischemia, viral myocarditis (e.g., Parvovirus), or toxicosis (e.g., Oleander)—the damaged myocytes become electrically unstable and spontaneously fire off action potentials. This disrupts the normal sinus rhythm, causing premature ventricular contractions (PVCs), ventricular tachycardia, or atrial fibrillation. Thus, arrhythmias are the hallmark of myocardial disease.",
        "Why_Not": "Murmurs indicate valvular disease (endocardium), not muscle disease. Cardiac tamponade is fluid in the pericardium. Stenosis is a narrowing of a vessel/valve.",
        "Wow_Approach": "If a dog presents with a sudden, irregular heartbeat (arrhythmia) and a history of recent blunt force trauma (like being hit by a car), the primary diagnosis is Traumatic Myocarditis, which often appears 12-24 hours after the trauma."
    },
    1591: {
        "topic": "Electrocardiogram (ECG) - The P Wave",
        "Core_Anatomy": "Sinoatrial (SA) node and atrial myocardium.",
        "Pathogenesis_Immediate": "On a standard Electrocardiogram (ECG), the P wave specifically indicates Atrial Depolarization.",
        "Pathogenesis_Deep": "An ECG traces the electrical activity of the heart over time. The cycle begins when the Sinoatrial (SA) node fires. The electrical wave spreads across both the right and left atria, causing the myocardial cells to depolarize (become positive inside) and contract. Because the atria possess relatively little muscle mass, the resulting voltage deflection on the ECG is a small, rounded, positive bump known as the P wave.",
        "Why_Not": "Ventricular depolarization creates the massive QRS complex. Ventricular repolarization creates the T wave. Atrial repolarization is so small it is completely hidden (buried) inside the massive QRS complex.",
        "Wow_Approach": "If you look at an ECG and see NO P-waves at all, but the QRS complexes are still occurring irregularly, the animal is in Atrial Fibrillation (a classic finding in large breed dogs with Dilated Cardiomyopathy or horses with poor performance)."
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
