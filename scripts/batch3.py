import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    44: {
        "topic": "Traumatic Reticulo-Peritonitis (Hardware Disease) in Cattle",
        "Core_Anatomy": "The reticulum (honeycomb compartment), the diaphragm, pericardium, and the peritoneal cavity.",
        "Pathogenesis_Immediate": "Hardware Disease (TRP) is caused by ingestion of metallic foreign bodies (wire, nails) that penetrate the reticular wall, causing local peritonitis and pleuritis, presenting as acute abdominal pain, grunting, reluctance to walk, and decreased milk production.",
        "Pathogenesis_Deep": "Cattle's non-selective grazing habits lead to ingestion of metallic debris from fields or feeds. The heavy metals settle in the reticulum due to gravity and reticular motility. During late pregnancy (enlarged uterus pushes the rumen forward) or at the onset of rumination, the reticulum contracts forcefully, driving the sharp metal through the reticular wall into the peritoneum. This causes a localized fibrinous peritonitis (acute phase) or, if the metal migrates forward, traumatic pericarditis.",
        "Why_Not": "Abomasal displacement (LDA/RDA) also causes decreased milk production and abdominal pain but the pain is more insidious, without grunting at defaecation, and the ping on percussion is located differently (left or right paralumbar fossa). TRP pain is elicited by applying pressure on the xiphoid/withers pinch test.",
        "Wow_Approach": "Prevent TRP by administering a 70 mm x 9 mm cylindrical magnets (hardware magnet) orally to all calves at purchase. The magnet lodges permanently in the reticulum, attracting and retaining ferrous metals before they can penetrate the wall. Confirmed TRP cases require exploratory rumenotomy and foreign body retrieval."
    },
    47: {
        "topic": "ECG Interpretation - QRS Complex and Cardiac Conduction",
        "Core_Anatomy": "The sinoatrial node, the atrioventricular node, the Bundle of His, Purkinje fibre system, and ventricular myocardium.",
        "Pathogenesis_Immediate": "The QRS complex on the electrocardiogram (ECG) represents ventricular depolarization — the simultaneous electrical activation spreading from the Bundle of His through the Purkinje fibres to all ventricular cardiomyocytes, triggering ventricular contraction (systole).",
        "Pathogenesis_Deep": "Normal cardiac conduction: Sinoatrial node → P-wave (atrial depolarization) → AV node delay → Q-wave (septal depolarization left to right) → R-wave (ventricular free wall depolarization) → S-wave (basal depolarization) → T-wave (ventricular repolarization). A wide QRS (>0.12 sec) indicates bundle branch block or ventricular ectopic origin. A peaked P-wave indicates right atrial enlargement.",
        "Why_Not": "The P-wave represents atrial depolarization; the T-wave represents ventricular repolarization. The QRS complex strictly represents ventricular depolarization. Atrial repolarization is hidden within the QRS complex and is not visible on surface ECG.",
        "Wow_Approach": "In large animal practice, a base-apex lead ECG (positive electrode at the left cardiac apex, negative at the jugular furrow) is the standard. Ventricular premature contractions (VPCs) present as wide, bizarre QRS complexes without a preceding P-wave and are a common finding in horses with myocarditis."
    },
    48: {
        "topic": "Acute Peritonitis - Haematological Changes and Diagnosis",
        "Core_Anatomy": "The peritoneal cavity, the serosal surfaces of the visceral organs, and the systemic inflammatory response cascade.",
        "Pathogenesis_Immediate": "Acute local peritonitis in cattle (most commonly from TRP or perforated abomasal ulcer) produces a characteristic left-shifted neutrophilia on the hemogram: the bone marrow rapidly releases immature band neutrophils into circulation due to the high demand from the peritoneal exudate.",
        "Pathogenesis_Deep": "Bacterial peritonitis triggers local production of IL-1, IL-6, and TNF-alpha from activated peritoneal macrophages. These cytokines stimulate the bone marrow to increase neutrophil production and mobilization. The accelerated release causes immature band neutrophils to appear in systemic blood (degenerative left shift). In severe peritonitis, total WBC may paradoxically drop due to neutrophil margination and trapping in the peritoneal space.",
        "Why_Not": "Eosinophilia indicates parasitic or allergic processes. Leukopenia with a degenerative left shift indicates an overwhelming infection where demand exceeds bone marrow supply (bad prognosis). Simple neutrophilia without a left shift indicates a mild, localized infection with adequate bone marrow reserve.",
        "Wow_Approach": "Peritoneal fluid analysis (abdominocentesis) is the gold standard: Total protein >3 g/dl and WBC >10,000 cells/μl with >80% neutrophils confirms septic peritonitis. Treat with broad-spectrum antibiotics (Penicillin + Gentamicin or Florfenicol) and peritoneal lavage if accessible."
    },
    49: {
        "topic": "Rumen Fluid pH and Acid Indigestion in Cattle",
        "Core_Anatomy": "The rumen epithelium, reticular pillar, omasum, and the rumen microbial ecosystem.",
        "Pathogenesis_Immediate": "Rumen fluid becomes dark brown and acidic (pH <5.0) in cases of acute grain overload (acid indigestion/ruminal acidosis), caused by excessive fermentation of rapidly digestible carbohydrates to lactic acid.",
        "Pathogenesis_Deep": "Overfeeding grain causes rapid proliferation of lactic-acid-producing bacteria (*Streptococcus bovis*, then *Lactobacillus* spp.), shifting rumen pH from normal (6.5-7.0) to severely acidic (<5.0). Low pH kills cellulolytic organisms and protozoa, disrupting normal fermentation. Lactic acid is absorbed into the blood, causing systemic metabolic acidosis. The concentrated rumen contents cause osmotic fluid shift from blood into the rumen, leading to dehydration and circulatory shock.",
        "Why_Not": "Alkaline indigestion (rumen alkalosis, pH >7.5) is caused by excess protein fermentation producing ammonia (NH3), typically from sudden access to urea-supplemented feeds or high-protein legumes. The rumen fluid is green-black with a pungent ammoniacal smell.",
        "Wow_Approach": "Treat acute lactic acidosis by oral administration of large volumes of water with 150g sodium bicarbonate to buffer rumen acids. In severe cases (pH <5, recumbent animal), perform emergency rumenotomy and scoop out the acidic contents by hand, followed by rumen inoculation with healthy rumen fluid from a donor cow."
    },
    50: {
        "topic": "Regurgitation vs Vomiting - Clinical Differentiation",
        "Core_Anatomy": "The oesophagus, cardia, lower oesophageal sphincter, and the vomiting centre (emetic centre) in the medulla oblongata.",
        "Pathogenesis_Immediate": "Regurgitation is the passive, retrograde movement of ingested food from the oesophagus or stomach back to the mouth, occurring WITHOUT nausea, retching, or abdominal contractions. It represents a mechanical failure of the oesophagus or cardia.",
        "Pathogenesis_Deep": "Regurgitation occurs via passive gravitational or mechanical forces without activation of the vomiting centre. Causes include megaoesophagus (congenital/acquired dilated oesophagus), vascular ring anomalies, and oesophageal strictures. The regurgitated material is undigested, tubular-shaped, and non-acidic. In contrast, vomiting is an active, forceful expulsion mediated by the medullary vomiting centre, involving nausea, ptyalism, retching, and abdominal contractions, expelling acidic, digested material.",
        "Why_Not": "Ruminant regurgitation (cudding/rumination) is a completely normal physiological process where the rumen bolus is regurgitated, re-chewed, and re-swallowed. Pathological regurgitation in ruminants involves undigested rumen contents appearing suddenly without cuddling behaviour.",
        "Wow_Approach": "Distinguish megaoesophagus-related regurgitation from vomiting in dogs clinically: megaoesophagus causes passive regurgitation immediately or 30+ minutes post-feeding (no nausea), confirmed by thoracic radiograph showing a gas-distended oesophagus. Treat with elevated feeding (Bailey chair method) and small, frequent, wet food meals."
    },
    51: {
        "topic": "Colloid vs Crystalloid IV Fluid Therapy",
        "Core_Anatomy": "The systemic capillary endothelium, the interstitial space, and the intravascular oncotic pressure system.",
        "Pathogenesis_Immediate": "Ringer's Lactate Solution is a crystalloid electrolyte solution that distributes throughout the extracellular fluid (ECF) space. Colloids (Hydroxyethyl Starch/HES, Dextran-40, Human Serum Albumin) contain large molecular weight particles that remain intravascular, exerting colloid osmotic pressure (COP) and restoring plasma volume more efficiently.",
        "Pathogenesis_Deep": "Crystalloids (Ringer's Lactate, Normal Saline) rapidly equilibrate across capillary walls; only 25-30% remains intravascular after 30 minutes, limiting their effectiveness in true hypovolaemic shock. Colloids (HES, Dextran-40) have large molecules (>70,000 Da) that cannot cross the capillary endothelium, maintaining a sustained intravascular volume expansion effect, making them essential in cases of severe plasma protein loss (burns, gastrointestinal protein loss).",
        "Why_Not": "Ringer's Solution (not Ringer's Lactate) is also a crystalloid and is NOT a colloid. The distinguishing factor is molecular size: colloids have high molecular weight particles maintaining COP; crystalloids have small ions that distribute freely into the ECF.",
        "Wow_Approach": "In haemorrhagic shock management, use the rule of three: for every 1 ml of blood lost, administer 3 ml of crystalloid (or 1:1 ratio of colloid). Monitor plasma colloid osmotic pressure (target >15 mmHg) and avoid crystalloid overload, which causes pulmonary oedema."
    },
    52: {
        "topic": "Biot's Respiration - Ataxic Breathing Pattern in CNS Disease",
        "Core_Anatomy": "The pontine and medullary respiratory centres (the dorsal respiratory group and pneumotaxic centre).",
        "Pathogenesis_Immediate": "Biot's respiration is characterized by irregular, alternating periods of hyperpnoea (fast deep breathing) and sudden apnoea (complete breathing cessation), caused by damage to the pontine respiratory centres due to elevated intracranial pressure or meningitis.",
        "Pathogenesis_Deep": "Normal respiratory rhythm is regulated by the dorsal respiratory group (DRG) in the medulla and the pneumotaxic centre in the pons. Elevated intracranial pressure (from meningitis, encephalitis, or head trauma) compresses and disrupts the pontine respiratory rhythm generator. This causes random, erratic alternation between bursts of hyperventilation and complete apnoea, with no predictable cyclical pattern.",
        "Why_Not": "Cheyne-Stokes respiration alternates between gradual crescendo hyperpnoea and decrescendo apnoea in a predictable cyclic pattern and is associated with congestive heart failure and bilateral cerebral hemisphere disease. Biot's respiration is completely irregular with abrupt transitions and indicates pontine or medullary damage.",
        "Wow_Approach": "Biot's breathing in a large animal indicates severe, life-threatening intracranial pathology. Emergency therapy: mannitol (20%, 1-2 g/kg IV over 20 minutes) to reduce cerebral oedema, dexamethasone to reduce blood-brain barrier permeability, and hyperventilation to reduce PaCO2."
    },
    53: {
        "topic": "Normal Physiological Parameters - Respiratory Rate in Horses",
        "Core_Anatomy": "The equine lower respiratory tract (bronchi, bronchioles, alveoli) and the intercostal muscles.",
        "Pathogenesis_Immediate": "The normal resting respiratory rate in adult horses is 8-16 breaths per minute. Rates exceeding 20/min at rest (tachypnoea) indicate respiratory distress, pain, fever, or metabolic acidosis.",
        "Pathogenesis_Deep": "Equine respiration is unique due to the locomotory-respiratory coupling: at the canter/gallop, each stride synchronizes with one breath, restricting the horse to one breath per stride. This limits ventilatory compensation during extreme exercise. Elevated resting respiratory rates in horses should prompt auscultation for airway sounds, evaluation for pleuritis, and measurement of arterial blood gases.",
        "Why_Not": "Cattle have a normal respiratory rate of 26-50/min, dogs 15-30/min, and cats 20-30/min. The horse's low resting respiratory rate (8-16/min) reflects its large tidal volume and highly efficient pulmonary gas exchange system.",
        "Wow_Approach": "Always count respiratory rate by observing nostril flare or flank movement before touching the horse, as handling immediately raises the rate due to excitement. An exercise-induced post-work respiratory rate exceeding 40/min that does not resolve within 30 minutes of rest indicates significant cardiopulmonary compromise."
    },
    54: {
        "topic": "Normal Rectal Temperature in Goats and Small Ruminants",
        "Core_Anatomy": "The rectal mucosa, the hypothalamic thermoregulatory set-point, and the sympathetic nervous system thermoeffectors.",
        "Pathogenesis_Immediate": "The normal rectal temperature for goats (*Capra hircus*) is 38.5–39.5°C (average 39.0°C). Temperatures exceeding 40°C indicate fever; temperatures below 37.5°C indicate hypothermia.",
        "Pathogenesis_Deep": "Body temperature is maintained by the hypothalamus balancing heat production (metabolic rate, shivering thermogenesis) against heat dissipation (evaporation, radiation, conduction). In goats, the thermoregulatory set-point is slightly higher than cattle. Environmental heat stress causes panting (evaporative cooling) and peripheral vasodilation (radiation/conduction) to maintain normothermia.",
        "Why_Not": "Normal rectal temperatures: Cattle 38.5-39.5°C, Horses 37.5-38.5°C, Goats 38.5-39.5°C, Sheep 38.5-39.5°C, Pigs 38.0-40.0°C, Dogs 38.5-39.5°C, Cats 38.5-39.5°C. Goats and cattle share similar ranges, but horses are notably cooler.",
        "Wow_Approach": "Rectal thermometry in goats requires gentle restraint with one person holding the goat against their body. Insert the thermometer 2-3 cm into the rectum against the mucosal wall (not into faeces). Wait 60 seconds for digital thermometers to equilibrate. Always assess temperature in the context of the animal's recent activity and ambient temperature."
    },
    55: {
        "topic": "Hypomagnesaemic Tetany (Grass Tetany/Lactation Tetany) in Cattle",
        "Core_Anatomy": "The synaptic terminals of the neuromuscular junction, NMDA glutamate receptors in the CNS, and the renal tubular magnesium reabsorption system.",
        "Pathogenesis_Immediate": "Hypomagnesaemic Tetany (Grass Tetany) is an acute, life-threatening metabolic disorder in adult lactating cows grazing lush spring pastures, characterized by muscle tremors, hypersensitivity, tetanic spasms, and death within 2-4 hours without treatment.",
        "Pathogenesis_Deep": "Magnesium is essential for neuronal membrane stabilization. Mg2+ normally blocks NMDA glutamate receptors in a voltage-dependent manner, modulating neuronal excitability. When blood Mg2+ falls below 0.4 mmol/L (normal: 0.8-1.2 mmol/L), the NMDA receptor blockade is lost. This causes uncontrolled, excessive neuronal firing, manifesting as muscle fasciculations, exaggerated startle response, hypersalivation, galloping movements, and fatal tonic-clonic convulsions.",
        "Why_Not": "Milk fever (hypocalcaemia) causes flaccid paralysis due to reduced acetylcholine release at the neuromuscular junction. Hypomagnesaemia causes hyperexcitability and tetany due to loss of NMDA receptor inhibition. Both are common periparturient metabolic diseases but are pharmacologically and mechanistically opposite.",
        "Wow_Approach": "Emergency treatment: Slow IV 400 ml of 20% Calcium Magnesium Borogluconate (which contains both Ca and Mg) for Stages 1-2. In severe convulsing animals, first sedate with IV diazepam (0.5 mg/kg), then administer 200 ml of 20% Magnesium Sulphate subcutaneously in multiple sites for slow absorption."
    },
    56: {
        "topic": "Dextran-40 and Colloid Osmotic Therapy in Shock",
        "Core_Anatomy": "The intravascular compartment, capillary endothelium, and the systemic circulation in shocked animals.",
        "Pathogenesis_Immediate": "Dextran-40 (MW 40,000 Da) is a synthetic, branched polysaccharide colloid solution used for rapid plasma volume expansion in hypovolaemic and distributive shock states, drawing fluid from the interstitial space into the intravascular compartment.",
        "Pathogenesis_Deep": "Dextran-40 molecules remain confined to the intravascular space due to their large size, exerting a colloidal oncotic pressure higher than plasma (approximately 40 mmHg). This creates an osmotic gradient drawing interstitial fluid into the vasculature, rapidly restoring circulating blood volume and cardiac preload. Additionally, Dextran-40 reduces red blood cell aggregation (rouleaux formation) and improves microvascular blood flow in shock.",
        "Why_Not": "Dextran-70 (MW 70,000 Da) provides volume expansion but does not reduce blood viscosity as effectively as Dextran-40. Normal Saline (crystalloid) does not provide oncotic pressure; it distributes equally throughout the ECF, causing oedema if given in excess. Dextran-40 is specifically indicated when improved microvascular flow is critical.",
        "Wow_Approach": "Monitor for Dextran-associated coagulopathy: doses exceeding 20 ml/kg impair platelet function and reduce Factor VIII levels, increasing bleeding risk. Administer the first 10 ml slowly (over 5 minutes) to test for rare anaphylactoid reactions before administering the full dose."
    },
    57: {
        "topic": "Blood Typing in Dogs - Universal Donor (DEA 1.1 Negative)",
        "Core_Anatomy": "The red blood cell surface membrane antigens in canine blood (Dog Erythrocyte Antigens, DEA).",
        "Pathogenesis_Immediate": "Dog Erythrocyte Antigen 1.1 (DEA 1.1) is the most clinically important canine blood group antigen. DEA 1.1 negative dogs are universal blood donors, as their blood can be safely transfused to both DEA 1.1 positive and negative recipients without triggering haemolytic transfusion reactions.",
        "Pathogenesis_Deep": "Canine blood groups are complex; the major blood group system includes DEA 1.1, 1.2, 3, 4, 5, and 7. DEA 1.1 is the most immunogenic antigen. A DEA 1.1 negative dog transfused with DEA 1.1 positive blood will form anti-DEA 1.1 alloantibodies. Subsequent transfusion with DEA 1.1 positive blood triggers a type II hypersensitivity (complement-mediated haemolysis), causing a potentially fatal acute haemolytic transfusion reaction (AHTR).",
        "Why_Not": "In cats, the AB blood group system is the dominant system. Type A cats can receive only Type A blood; Type B cats have strong anti-A antibodies and will experience fatal haemolysis with any Type A blood. Unlike dogs, cats do not have a universal donor type.",
        "Wow_Approach": "Always crossmatch donor and recipient blood (major and minor crossmatch) before every transfusion, regardless of known blood types. Store donor blood at 4°C in CPDA-1 anticoagulant; do not use blood stored >35 days. Monitor the recipient for the first 15 minutes of transfusion (the highest risk window for AHTR)."
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

print(f"Batch 3/5 DONE: Updated {updated} questions.")
