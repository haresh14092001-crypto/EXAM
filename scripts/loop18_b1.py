import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2042: {
        "topic": "Canine Allergic Reactions - Emergency Treatment",
        "Core_Anatomy": "Mast cells, histamine receptors, and systemic vasculature.",
        "Pathogenesis_Immediate": "For acute anaphylaxis and severe allergic reactions in dogs, the first-line emergency drug is Epinephrine (Adrenaline).",
        "Pathogenesis_Deep": "Anaphylaxis is a life-threatening Type I hypersensitivity reaction. Massive mast cell degranulation releases histamine, causing profound vasodilation, bronchospasm, and circulatory collapse. Epinephrine acts on Alpha-1 receptors to cause immediate peripheral vasoconstriction (restoring blood pressure) and on Beta-2 receptors to rapidly reverse bronchospasm. It also blocks further mast cell degranulation. It must be given within minutes to prevent irreversible cardiovascular collapse.",
        "Why_Not": "Antihistamines (like Diphenhydramine) block histamine receptors but cannot reverse the vasodilation already occurring. NSAIDs and Diuretics have no role in acute anaphylaxis.",
        "Wow_Approach": "In dogs, vaccine-induced anaphylaxis (particularly after killed bacterins) most commonly presents as acute vomiting, diarrhea, and facial swelling within 30 minutes. Always keep the dog in the clinic for 20 minutes post-vaccination to intervene immediately."
    },
    2043: {
        "topic": "Canine Epilepsy - Oral Antiepileptic Drugs",
        "Core_Anatomy": "Central nervous system (GABA receptors and sodium channels).",
        "Pathogenesis_Immediate": "Oral antiepileptic drugs routinely used for long-term management of canine epilepsy include Phenobarbitone, Diazepam, and Potassium Bromide (all of the above).",
        "Pathogenesis_Deep": "(1) Phenobarbitone is the gold standard first-line drug; it potentiates GABA-A receptors and blocks sodium channels, reducing neuronal excitability. (2) Potassium Bromide is added as a second-line drug when phenobarbitone alone fails; bromide ions compete with chloride ions at neuronal membranes, hyperpolarizing the cell. (3) Diazepam (a benzodiazepine) potentiates GABA-A receptors acutely, but its oral use for maintenance is limited due to rapid hepatic metabolism in dogs.",
        "Why_Not": "Cats cannot metabolize Potassium Bromide; it accumulates and causes fatal eosinophilic pneumonia. Phenobarbitone must be used with caution in cats at much lower doses.",
        "Wow_Approach": "Never abruptly stop Phenobarbitone; this precipitates severe status epilepticus. If the drug must be withdrawn, taper the dose over several weeks."
    },
    2044: {
        "topic": "Canine Gastric Dilatation-Volvulus (GDV)",
        "Core_Anatomy": "Stomach and greater omentum.",
        "Pathogenesis_Immediate": "A syndrome characterized by sudden onset of intense abdominal pain with shock, vomiting, diarrhea, and rapid changes in gastrointestinal motility is classically Gastric Dilatation-Volvulus (GDV).",
        "Pathogenesis_Deep": "GDV is a surgical emergency. The stomach fills with gas and then physically rotates on its mesenteric axis (volvulus). This rotation simultaneously seals the inflow (cardia) and outflow (pylorus), trapping gas. It also twists the splenic and gastric vasculature, causing massive ischemia. The trapped gas causes the abdomen to fill with air. Venous return to the heart is obstructed by the dilated stomach, causing distributive/obstructive shock within hours.",
        "Why_Not": "Simple gastritis causes vomiting but not the profound distension, tympany, and sudden cardiovascular collapse of GDV.",
        "Wow_Approach": "The classic presentation: a large deep-chested breed dog (Great Dane, St. Bernard) ate a large meal 1 hour ago, now retching unproductively with a visibly distended abdomen. This is a 1-hour emergency; delay equals death."
    },
    2045: {
        "topic": "Canine GDV - Predisposed Breeds",
        "Core_Anatomy": "Stomach (deep thoracic conformation and ligamentous laxity).",
        "Pathogenesis_Immediate": "The large, deep-chested breeds most predisposed to GDV include German Shepherd Dogs (GSD), Labrador Retrievers, and Golden Retrievers (all of the above).",
        "Pathogenesis_Deep": "GDV is strongly linked to an anatomical conformation where the thoracic cavity is narrow and deep relative to the abdomen. This conformation allows the stomach to swing more freely within the abdominal cavity. Combined with the hepatogastric and gastrophrenic ligamentous laxity that naturally increases with age, the probability of torsion dramatically increases. Deep-chested, large-breed dogs over 7 years of age have the highest lifetime risk.",
        "Why_Not": "Brachycephalic breeds (Pugs, Bulldogs) are at risk for GDV too but for different anatomical reasons related to aerophagia.",
        "Wow_Approach": "A prophylactic gastropexy (surgically tacking the stomach to the body wall) is strongly recommended during routine spay/neuter of high-risk breeds to prevent torsion, as recurrence after successful treatment is nearly 70-80%."
    },
    2046: {
        "topic": "Canine Pancreatitis - Praying Posture",
        "Core_Anatomy": "Pancreas and peritoneum.",
        "Pathogenesis_Immediate": "The classic 'Praying posture' (forelimbs extended, hindquarters elevated) is commonly and specifically manifested by dogs suffering from Abdominal pain, most classically seen in acute Pancreatitis.",
        "Pathogenesis_Deep": "When the pancreas is inflamed, the activated proteases (trypsin, lipase) begin digesting the surrounding peritoneal fat and mesentery. The resulting severe chemical peritonitis is extremely painful. The dog adopts the praying posture because stretching the cranial abdomen by extending the forelimbs relieves some of the pressure on the inflamed pancreas, temporarily reducing the sensation of pain.",
        "Why_Not": "Thoracic pain causes a rigid, splinting posture with reluctance to move. Lumbosacral pain causes the dog to be reluctant to move the hindquarters or climb stairs.",
        "Wow_Approach": "If a middle-aged, obese dog fed a high-fat meal the night before presents with the praying posture and vomiting, hyperamylasemia/hyperlipasemia, and a 'sentinel loop' sign on X-ray, acute pancreatitis is the diagnosis."
    },
    2047: {
        "topic": "Veterinary Hematology - Coagulation Factors",
        "Core_Anatomy": "Hepatocytes (liver parenchyma).",
        "Pathogenesis_Immediate": "The vast majority of clotting factors (Factors I, II, V, VII, IX, X, XI, XII) are synthesized primarily in the Liver.",
        "Pathogenesis_Deep": "The liver is the master manufacturer of the coagulation cascade. The Vitamin K-dependent clotting factors (II, VII, IX, X) require the liver to carboxylate their glutamic acid residues for them to function. This is why rodenticides like Bromadiolone (Vitamin K antagonists) cause fatal hemorrhage; they block the liver from activating these critical factors. Severe liver failure (like in dogs with portosystemic shunts) causes prolonged PT and APTT due to factor deficiencies.",
        "Why_Not": "Platelets are produced by megakaryocytes in the bone marrow. The spleen acts as a platelet reservoir but does not produce clotting factors.",
        "Wow_Approach": "In any dog with unexplained hemorrhage (bloody vomit, nosebleed, blood under the skin), immediately ask the owner if rodenticide bait is accessible. A simple Vitamin K1 injection can reverse the coagulopathy if caught early."
    },
    2048: {
        "topic": "Veterinary Critical Care - Septic Shock",
        "Core_Anatomy": "Systemic vasculature and cardiac output.",
        "Pathogenesis_Immediate": "Septic shock is mechanistically a combination of Distributive shock and Hypovolemic shock.",
        "Pathogenesis_Deep": "Septic shock results from the systemic inflammatory response to a severe infection (typically Gram-negative bacteremia releasing endotoxin). The endotoxin triggers massive cytokine release (TNF-α, IL-1, IL-6). These cytokines cause: (1) Distributive shock: massive peripheral vasodilation (the vessels become pathologically dilated and blood 'pools' in the periphery, dropping central pressure). (2) Hypovolemic shock: massive leakage of fluid from capillaries (endotoxin destroys the glycocalyx) into the interstitium, reducing effective circulating blood volume.",
        "Why_Not": "Cardiogenic shock results from pump failure (the heart cannot contract). While septic shock can eventually cause myocardial depression, it is primarily distributive at onset.",
        "Wow_Approach": "A septic dog initially presents in the 'warm shock' phase (high heart rate, bounding pulses, fever, injected mucous membranes) before progressing to 'cold shock' (cold extremities, poor pulses, pale/gray mucous membranes) as compensatory mechanisms fail."
    },
    2049: {
        "topic": "Renal Medicine - Anuria Definition",
        "Core_Anatomy": "Renal tubules and glomeruli.",
        "Pathogenesis_Immediate": "In veterinary medicine, Anuria is classically defined as the production of urine at a rate less than 0.5 mL/kg/hr (or <1 mL/kg/hr depending on the reference).",
        "Pathogenesis_Deep": "The kidneys must continuously produce urine to excrete nitrogenous waste products. If urine output drops below this critical threshold, it indicates severe acute renal failure (pre-renal, intrinsic renal, or post-renal). In acute tubular necrosis, the damaged tubules lose their concentrating ability and cannot reabsorb filtrate properly. The resulting anuria leads to rapid accumulation of urea, creatinine, potassium, and phosphorus, causing uremic encephalopathy and fatal cardiac arrhythmias (from hyperkalemia).",
        "Why_Not": "Oliguria is reduced (but not absent) urine output. Anuria denotes near-complete cessation of urine production.",
        "Wow_Approach": "The most common emergency cause of anuria in cats is urethral obstruction (blocked tom cat). Always palpate the abdomen for a distended, turgid, painful urinary bladder before diagnosing renal anuria."
    },
    2050: {
        "topic": "Canine Hepatology - Forrest Band Sign",
        "Core_Anatomy": "Hepatic parenchyma and biliary system.",
        "Pathogenesis_Immediate": "The 'Forrest band' is a specific ultrasonographic finding visible in canine Leptospirosis.",
        "Pathogenesis_Deep": "In dogs with acute hepatic leptospirosis (caused by Leptospira serovars Icterohaemorrhagiae or Copenhageni), the severe hepatocellular necrosis and associated periportal inflammation create a characteristic ultrasonographic finding. A hyperechoic (bright white) periportal rim or 'band' of echogenicity is visible surrounding the portal vasculature within the liver parenchyma. This 'Forrest band' (also described as a 'target pattern') represents the periportal edema, inflammation, and necrosis.",
        "Why_Not": "Cystitis changes the bladder wall. Ehrlichia canis causes thrombocytopenia. Babesiosis affects the spleen and causes intravascular hemolysis.",
        "Wow_Approach": "If a young dog presents with acute PU/PD, vomiting, severe icterus, and a periportal Forrest band on ultrasound, immediately run a MAT for Leptospirosis and start Penicillin/Doxycycline."
    },
    2051: {
        "topic": "Bovine Traumatic Reticuloperitonitis (TRP) - Withers Pinch",
        "Core_Anatomy": "Reticulum and diaphragm.",
        "Pathogenesis_Immediate": "A sharp pain response elicited upon the 'Withers Pinch' test or deep thoracic/xiphoid palpation is a classic positive finding for Traumatic Reticuloperitonitis (TRP/Hardware Disease).",
        "Pathogenesis_Deep": "Cattle are indiscriminate eaters and frequently ingest metallic hardware (nails, wire). These objects settle in the reticulum. During the powerful contractions of late pregnancy or heavy labor, the sharp metal penetrates the reticular wall. If it enters the peritoneal cavity, it causes severe local or generalized peritonitis. Applying external pressure over the reticular area (withers pinch, bar test, or pole test) triggers a profound pain response as the inflamed serosal surfaces are compressed.",
        "Why_Not": "Liver abscess and Splenic abscess cause fever and weight loss but do not produce acute pain on thoracic compression. Pleurisy causes pain on chest percussion, not xiphoid palpation.",
        "Wow_Approach": "Place a bar magnet into the reticulum prophylactically via a balling gun to attract and hold all future ingested hardware—a permanent, 100% effective preventative strategy."
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
