import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    58: {
        "topic": "Vagal Indigestion - L-Shaped Abdomen and Forestomach Anatomy",
        "Core_Anatomy": "The rumen (dorsal and ventral sac), the reticulum, and the left and right paralumbar fossae.",
        "Pathogenesis_Immediate": "An 'L-shaped abdomen' (also called a papple-shaped distension) in cattle with vagal indigestion is caused by simultaneous distension of the rumen's left dorsal sac (creating a left paralumbar fossa bulge) and the right ventral sac/omasum (creating a right side fullness).",
        "Pathogenesis_Deep": "In vagal indigestion Type II (failure of omasal transport), failure of ingesta to pass the reticulo-omasal orifice causes progressive accumulation in both the dorsal and ventral ruminal sacs. The rumen's dorsal sac distends with free gas (left paralumbar fossa prominence), while accumulation of fluid ingesta in the ventral sac and omasum creates a right-sided fullness. The combined bilateral distension gives the characteristic 'L-shape' or papple appearance when viewed from behind.",
        "Why_Not": "In simple rumen bloat, the gas accumulates only in the left dorsal sac (left paralumbar distension). In LDA (Left Displaced Abomasum), there is high-pitched ping on the left paralumbar fossa from the gas-filled abomasum. Vagal indigestion creates a complex, bilateral distension pattern that is not relieved by stomach tube passage.",
        "Wow_Approach": "Diagnose vagal indigestion via rumen fluid analysis (pH, colour, motility), rectal palpation (feel the impacted omasum on the right), and the ping map (low-pitched pung sound in vagal indigestion vs high-pitched ping in LDA). Peritoneal fluid analysis confirms secondary peritonitis."
    },
    61: {
        "topic": "Pregnancy Toxaemia (Ketosis) in Ewes - Frog-Leg Posture",
        "Core_Anatomy": "The hepatic mitochondria (ketogenic pathway), the hypothalamus (glucose-sensing neurons), and the skeletal muscles of the hindlimbs.",
        "Pathogenesis_Immediate": "Pregnancy toxaemia ('twin lamb disease') is a fatal metabolic ketosis in ewes carrying multiple foetuses during the last 4-6 weeks of gestation, caused by severe negative energy balance, presenting with the classic 'frog-leg posture' (hindlimbs extended in lateral recumbency).",
        "Pathogenesis_Deep": "Multiple foetuses dramatically increase glucose demand in late gestation (up to 70-80% of maternal glucose is diverted to the foetuses). When dietary energy is insufficient, the ewe's hepatic capacity for gluconeogenesis is exceeded, and fat mobilization produces massive ketone body accumulation. Ketonaemia impairs glucose transport across the blood-brain barrier, causing CNS glucose deprivation. The resulting neurological dysfunction causes hindlimb muscle weakness (the 'frog posture'), blindness, and coma.",
        "Why_Not": "Grass tetany presents with hyperexcitability and muscular tetany. Polioencephalomalacia (Thiamine deficiency) presents with star-gazing (dorsiflexion of the neck) and cortical blindness. Pregnancy toxaemia presents with progressive weakness and lateral recumbency, with the hindlimbs pathognomonically extended in a frog-like posture.",
        "Wow_Approach": "Treat immediately with IV 50% Dextrose (100-200 ml) and oral Propylene Glycol (60-120 ml every 8 hours). Administer Vitamin B12 (cyanocobalamin) and soluble corticosteroids. In valuable ewes, perform emergency Caesarean section if foetuses are near term, as removing the foetal glucose demand immediately resolves the NEB."
    },
    62: {
        "topic": "White Muscle Disease (Nutritional Muscular Dystrophy) - Selenium and Vitamin E Deficiency",
        "Core_Anatomy": "The skeletal and cardiac myofibers, the mitochondrial electron transport chain, and the glutathione peroxidase antioxidant system.",
        "Pathogenesis_Immediate": "White Muscle Disease (WMD) is a fatal nutritional myopathy of neonatal lambs, calves, and foals caused by combined selenium and/or vitamin E deficiency, causing bilateral symmetrical skeletal muscle necrosis and sudden cardiac failure.",
        "Pathogenesis_Deep": "Selenium is a cofactor of glutathione peroxidase (GPx), an enzyme that reduces lipid hydroperoxides to non-toxic alcohols. Vitamin E (alpha-tocopherol) is a membrane-bound antioxidant that scavenges free radicals. Deficiency of either allows Reactive Oxygen Species (ROS) to accumulate inside myocytes, causing lipid peroxidation of the sarcoplasmic reticulum. Calcium homeostasis is disrupted, triggering uncontrolled calcium entry, proteolysis, and myofiber necrosis. The white muscle colour on gross pathology reflects myofibrillar protein denaturation and calcium deposition.",
        "Why_Not": "Enzootic Muscular Dystrophy (EMD) and WMD are synonymous. Azoturia (Exertional Rhabdomyolysis) also causes muscle necrosis and myoglobinuria, but in adult horses following exercise, not in neonates. WMD affects neonates of multiple species in selenium-deficient geographic areas.",
        "Wow_Approach": "Diagnose by measuring blood selenium levels (<0.1 ppm = deficient) and plasma CK/AST (highly elevated). Treat with injectable Se+Vit E (BoSe or Mu-Se) at 0.1 mg/kg selenium IM. Prevent by supplementing pregnant dams with selenium 4-6 weeks pre-partum. Avoid over-supplementation (selenium toxicosis causes 'Blind Staggers')."
    },
    63: {
        "topic": "Ceruloplasmin as a Copper Status Biomarker",
        "Core_Anatomy": "The hepatic parenchyma (site of ceruloplasmin synthesis), the plasma compartment, and copper-dependent enzyme systems.",
        "Pathogenesis_Immediate": "Ceruloplasmin (ferroxidase I) is a copper-containing glycoprotein synthesized by the liver, serving as the principal copper transport protein in blood and the definitive biochemical marker for diagnosing copper deficiency (Swayback, Enzootic Ataxia) in ruminants.",
        "Pathogenesis_Deep": "Copper is essential for the activity of dopamine beta-hydroxylase, cytochrome c oxidase, and lysyl oxidase (required for connective tissue cross-linking). The liver synthesizes ceruloplasmin, incorporating 6 copper atoms per molecule. In copper deficiency, hepatic copper stores are depleted, ceruloplasmin synthesis drops, and plasma levels fall below 0.2 mg/ml. This causes hypochromic anaemia (copper-deficient caeruloplasmin cannot facilitate iron mobilization), depigmentation, and neurological signs in calves (swayback).",
        "Why_Not": "Transferrin is the iron transport protein (measured for iron deficiency). Procalcitonin is a sepsis biomarker. Alpha-fetoprotein is a liver tumour marker. Ceruloplasmin is uniquely the specific serum copper marker — measuring plasma copper itself is an alternative but requires atomic absorption spectrophotometry.",
        "Wow_Approach": "Secondary copper deficiency (most common in ruminants) is caused by high dietary molybdenum and sulphate forming thiomolybdate complexes in the rumen that prevent copper absorption. Treat with IV copper glycinate or subcutaneous copper oxide wire boluses for slow release over months."
    },
    64: {
        "topic": "Zinc Phosphide Toxicosis in Rodenticide Poisoning",
        "Core_Anatomy": "The gastric mucosa, the hepatic mitochondria, and the pulmonary vascular endothelium.",
        "Pathogenesis_Immediate": "Zinc phosphide is a rodenticide that, when ingested and contacted with gastric acid or moisture, releases phosphine gas (PH3), causing rapid, often fatal mitochondrial electron transport chain (ETC) failure.",
        "Pathogenesis_Deep": "Zinc phosphide (Zn3P2) reacts with hydrochloric acid in the stomach: Zn3P2 + 6HCl → 3ZnCl2 + 2PH3. Phosphine gas is then absorbed through the gastric and intestinal mucosa into the portal circulation. Phosphine inhibits cytochrome c oxidase (Complex IV of the mitochondrial ETC), blocking oxygen utilization by mitochondria. The resulting histotoxic anoxia (cellular suffocation in the presence of oxygen) causes acute hepatocyte necrosis, pulmonary oedema, and myocardial failure. The classically described 'acetylene-like' odour is released from the stomach (garlic/rotten fish smell).",
        "Why_Not": "ANTU (Alpha-naphthylthiourea) causes massive pulmonary oedema (hydrothorax) without the characteristic phosphine smell. Red Squill causes cardiac arrhythmias by inhibiting the Na/K ATPase pump (like Digitalis). Fluoroacetate (1080) causes seizures by blocking the TCA cycle at aconitase (forming fluorocitrate).",
        "Wow_Approach": "There is no specific antidote for zinc phosphide toxicosis. Induce emesis immediately (if <1 hour post-ingestion, in dogs only) in a well-ventilated space (phosphine gas released during emesis is hazardous to attending veterinarians and staff). Administer activated charcoal, IV fluids, and treat pulmonary oedema supportively."
    },
    65: {
        "topic": "Sulkowich Test for Calcium in Urine - Parturient Paresis Diagnosis",
        "Core_Anatomy": "The renal tubules, the glomerular filtration membrane, and the calcium homeostatic axis.",
        "Pathogenesis_Immediate": "The Sulkowich Test is a qualitative bedside urine test for calcium, used to aid in the diagnosis of hypocalcaemia (milk fever/parturient paresis) in dairy cows. A negative test (no white turbidity) indicates marked urinary calcium depletion consistent with hypocalcaemia.",
        "Pathogenesis_Deep": "Sulkowich Reagent (oxalic acid + ammonium oxalate + glacial acetic acid + distilled water) forms a precipitate of calcium oxalate when mixed with calcium-containing urine. In normal animals, urine contains sufficient calcium to form a white, cloudy precipitate with the reagent. In hypocalcaemic cows, the kidney reabsorbs all available calcium, producing calcium-free urine; the Sulkowich test produces no turbidity (clear = negative).",
        "Why_Not": "The Xylidil Blue (Xylidil-blue) test measures serum or urine magnesium levels; Peat Scours is a clinical condition caused by copper deficiency on peaty soils; Selenium deficiency causes white muscle disease. Each deficiency has a specific biochemical test for diagnosis.",
        "Wow_Approach": "Perform the Sulkowich Test in the field: mix 5 ml of fresh urine with 2.5 ml of Sulkowich reagent. Grade: 0 (no turbidity = severe hypocalcaemia), 1+ (slight haze), 2+ (white cloud, normal), 3+ (heavy precipitate, hypercalcaemia). A Grade 0 result in a post-parturient cow strongly indicates milk fever requiring immediate calcium borogluconate treatment."
    },
    66: {
        "topic": "Parturient Paresis Staging and Clinical Assessment",
        "Core_Anatomy": "Neuromuscular junctions, the CNS (cerebral cortex), the rumen, and the cardiovascular system.",
        "Pathogenesis_Immediate": "Parturient Paresis (Milk Fever) progresses through 3 clinically distinct stages based on the degree of hypocalcaemia, allowing rapid triage and treatment decisions in the field.",
        "Pathogenesis_Deep": "Stage 1: Hypersensitivity, muscle tremors, shuffling gait, mild excitement (blood Ca: 1.5-2.0 mmol/L). Stage 2: Sternal recumbency, S-shaped lateral bend of the neck, loss of consciousness, rumen atony, cold extremities, dry muzzle (blood Ca: 1.0-1.5 mmol/L). Stage 3: Lateral recumbency, complete loss of consciousness, bloat (rumen atony), tachycardia with weak heart sounds, and imminent death (blood Ca: <1.0 mmol/L). Each stage requires immediate calcium supplementation.",
        "Why_Not": "Stage 3 milk fever may be confused with downer cow syndrome (myopathy due to prolonged recumbency). Downer cows are mentally alert but cannot rise. Stage 3 milk fever cows are completely unconscious and areflexive, requiring emergency IV calcium treatment before any further assessment.",
        "Wow_Approach": "Administer 400 ml of 40% Calcium Borogluconate IV at no faster than 1 ml/kg/min (monitoring cardiac rate constantly with a stethoscope). A positive treatment response (eructation, muscle tremors, attempts to rise) typically occurs within 15-20 minutes in Stage 1-2. Stage 3 cows may require a second bottle given subcutaneously."
    },
    69: {
        "topic": "Bovine Ketosis - Types, Diagnosis, and Treatment",
        "Core_Anatomy": "The hepatic mitochondria, the rumen epithelium (BHBA production from butyrate), and the mammary gland.",
        "Pathogenesis_Immediate": "Bovine Ketosis is a metabolic disorder of high-producing dairy cows occurring within the first 2-6 weeks of lactation, characterized by elevated blood Beta-Hydroxybutyrate (BHBA >1.2 mmol/L), reduced milk production, sweet acetone breath, and clinical or subclinical disease.",
        "Pathogenesis_Deep": "Type 1 (Underfeeding/Wasting) Ketosis: Insufficient energy intake forces excessive adipose mobilization. The liver produces ketone bodies (BHBA, Acetoacetate, Acetone) from acetyl-CoA in excess of TCA cycle capacity. Type 2 (Fatty Liver) Ketosis: Over-conditioned cows with pre-existing hepatic lipidosis; the fatty liver cannot perform gluconeogenesis or process acetyl-CoA efficiently, compounding ketone accumulation. Butyric acid silage produces BHBA directly in the rumen wall.",
        "Why_Not": "Type 3 (Butyric acid) Ketosis occurs in Europe due to poor silage fermentation producing high butyric acid. Unlike Types 1 and 2, there is no NEB — the ketosis is driven by exogenous butyric acid absorption directly from silage, not fat mobilization.",
        "Wow_Approach": "Screen all fresh cows at Day 4-14 post-calving using a Keto-Test strip (milk strip) or CoWside BHBA meter (blood). BHBA >1.4 mmol/L = subclinical ketosis (treat with PG). Reduce ketosis incidence using a well-managed transition cow programme: target BCS 3.25-3.5 at calving and feed a high-energy TMR in the close-up dry period."
    },
    74: {
        "topic": "Ileus (Paralytic Obstruction) vs Mechanical Intestinal Obstruction",
        "Core_Anatomy": "The enteric nervous system (Auerbach's myenteric plexus), the small intestinal smooth muscle, and the intestinal lumen.",
        "Pathogenesis_Immediate": "Ileus is the functional failure of intestinal peristalsis (no structural blockage) caused by neurogenic, vascular, or metabolic inhibition of the enteric nervous system, resulting in intestinal content accumulation and gas distension.",
        "Pathogenesis_Deep": "Paralytic (adynamic) ileus is caused by inhibition of the myenteric plexus via: (1) Peritoneal inflammation (endotoxins suppress peristaltic reflexes), (2) Electrolyte imbalances (hypokalaemia impairs smooth muscle depolarization), (3) Post-operative bowel handling (surgical stress). Intestinal gas accumulates, progressive abdominal distension occurs, and endotoxin absorption from stagnant luminal bacteria causes systemic toxaemia. Unlike mechanical obstruction, no physical blockage exists.",
        "Why_Not": "Mechanical obstruction involves a physical obstruction (intussusception, strangulation, volvulus) causing pain, shock, and high-pitched borborygmi. Ileus is silent (no borborygmi on auscultation), and the pain is less severe. Both can cause similar metabolic derangements (hypochloraemic metabolic alkalosis in abomasal volvulus).",
        "Wow_Approach": "Treat ileus by correcting the primary cause (rehydration, anti-endotoxin therapy with Flunixin meglumine 1.1 mg/kg IV), and stimulating motility with prokinetics (Metoclopramide 0.5 mg/kg slow IV, Neostigmine in horses). Mineral oil via nasogastric tube lubricates the intestinal contents."
    },
    75: {
        "topic": "Fluid Therapy in Shock - Dose Rates and Types",
        "Core_Anatomy": "The systemic vasculature, the central venous pressure (CVP) system, and the interstitial and intracellular fluid compartments.",
        "Pathogenesis_Immediate": "Hypovolaemic shock requires immediate aggressive fluid resuscitation. The standard IV crystalloid dose for acute shock therapy is 90 ml/kg/hour (dogs) and 70-90 ml/kg/hour (cats), given as a rapid bolus to restore circulating blood volume.",
        "Pathogenesis_Deep": "Shock causes cellular hypoxia through reduced cardiac output. Crystalloids (Lactated Ringer's, Normal Saline) rapidly restore intravascular volume by distributing throughout the ECF. However, only 25% of the administered crystalloid volume remains intravascular after 60 minutes. Therefore, large volumes (3x the estimated blood loss) are required. Monitoring during fluid resuscitation: HR, mucous membrane colour, CRT, pulse pressure, and urine output (>0.5-1 ml/kg/hr = adequate renal perfusion).",
        "Why_Not": "Doses of 30 ml/kg/hr are conservative maintenance rates used for stable patients with mild dehydration. The shock dose (90 ml/kg/hr) is only used in acute life-threatening hypovolaemia, and should be given in 25% aliquots with constant reassessment.",
        "Wow_Approach": "In cats and dogs with septic shock, use the FAST protocol: give 20 ml/kg Lactated Ringer's over 15 minutes, reassess, and repeat up to 3 times. Add colloids (HES 5 ml/kg) if albumin is <2 g/dl. Target MAP >65 mmHg. If unresponsive, initiate vasopressor therapy with Dopamine (5-15 mcg/kg/min IV CRI)."
    },
    76: {
        "topic": "Megaoesophagus and Regurgitation in Dogs",
        "Core_Anatomy": "The thoracic oesophagus, the lower oesophageal sphincter, and the vagal and recurrent laryngeal nerve innervation.",
        "Pathogenesis_Immediate": "Megaoesophagus is a generalized dilatation of the oesophagus caused by failure of normal peristaltic contractions, leading to passive food accumulation and regurgitation. It is the most common cause of regurgitation in dogs.",
        "Pathogenesis_Deep": "Primary (idiopathic or congenital) megaoesophagus results from incomplete development of the oesophageal mechanoreceptors or central vagal afferent pathways, preventing normal peristaltic wave initiation. Secondary megaoesophagus occurs in dogs with myasthenia gravis (most common acquired cause — acetylcholine receptor antibodies impair oesophageal smooth muscle stimulation), hypothyroidism, and Addison's disease. Food accumulates in the dilated oesophagus, is passively regurgitated before reaching the stomach, and causes aspiration pneumonia.",
        "Why_Not": "Oesophageal stricture also causes regurgitation but produces a focal obstruction visible on contrast fluoroscopy, not a generalized dilatation. In megaoesophagus, the entire thoracic oesophagus is dilated, creating the classic 'wind-sock' appearance on plain thoracic radiography.",
        "Wow_Approach": "Management: Feed from an elevated position (Bailey chair) to use gravity to assist oesophageal transit. Feed small, frequent, liquid-to-meatball consistency meals. Diagnose Myasthenia Gravis (the most treatable cause) via Tensilon (edrophonium) test or acetylcholine receptor antibody titre. Treat MG with oral Pyridostigmine bromide."
    },
    77: {
        "topic": "Biot's Respiration vs Cheyne-Stokes Respiration",
        "Core_Anatomy": "The pontine respiratory group (Biot's) and the forebrain/diencephalic respiratory control centres (Cheyne-Stokes).",
        "Pathogenesis_Immediate": "Biot's Respiration is characterized by irregularly varying periods of hyperpnoea and apnoea with no predictable pattern, indicating severe brainstem (pontine/medullary) damage. Cheyne-Stokes respiration shows a regular crescendo-decrescendo cycle with apnoea indicating bilateral cerebral hemisphere or thalamic dysfunction.",
        "Pathogenesis_Deep": "Biot's breathing results from direct damage to the pontine respiratory rhythm generator, disrupting all organized respiratory patterning. Cheyne-Stokes pattern occurs when the chemoreceptor feedback loop is exaggerated: in cardiac failure or bilateral cerebral disease, there is a circulatory delay between pulmonary gas exchange and chemoreceptor sensing, causing oscillating hyperpnoea and apnoea. The predictable crescendo-decrescendo pattern differentiates it from Biot's erratic pattern.",
        "Why_Not": "Kussmaul breathing (deep, regular, gasping breaths without apnoea) is the compensatory hyperventilation of severe metabolic acidosis (diabetic ketoacidosis). Apneusis (prolonged inspiratory hold) indicates mid-pontine damage. Only Biot's respiration is characterized by completely irregular alternation with abrupt apnoea.",
        "Wow_Approach": "Document respiratory pattern precisely before any sedation or anaesthesia: Cheyne-Stokes in a comatose dog suggests congestive heart failure or brain herniation (more reversible), while Biot's breathing indicates brainstem compression (grave prognosis). Emergency hyperventilation to reduce PaCO2 buys time while definitive brain oedema therapy is initiated."
    }
}

updated = 0
for q in data:
    if q['id'] in enrichment:
        q.update(enrichment[q['id']])
        updated += 1

with open(db_path, "w", encoding="utf-8") as f:
    f.write("// Auto-generated Hybrid Exam Database\n")
    f.write("const examData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"Batch 4/5 DONE: Updated {updated} questions.")
