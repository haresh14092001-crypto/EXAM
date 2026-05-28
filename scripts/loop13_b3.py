import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1511: {
        "topic": "VMD Clinical Problem Solving",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "The 'Choose the correct answer' section in VMD evaluates the ability to select the most probable diagnosis or best intervention from a list of highly similar differentials.",
        "Pathogenesis_Deep": "Success in VMD MCQs requires 'illness script' matching: recognizing the pathognomonic sign (e.g., papple shape for vagal indigestion) out of a list of generic signs (e.g., anorexia, fever).",
        "Why_Not": "Selecting a generic answer over a specific one is a common pitfall.",
        "Wow_Approach": "Always read all four options before selecting. Often, two options will be partially correct, but only one is the definitive 'gold standard' answer."
    },
    1512: {
        "topic": "Compton Metabolic Profile Test - Dairy Herds",
        "Core_Anatomy": "Systemic blood biochemistry and hepatic metabolism.",
        "Pathogenesis_Immediate": "A metabolic profile test is primarily needed when a herd consists of high-producing dairy animals experiencing a high incidence of production diseases.",
        "Pathogenesis_Deep": "The Compton Metabolic Profile Test is a herd-level diagnostic tool (not just for individual sick cows). It involves taking blood samples from distinct groups (e.g., dry cows, early lactation, late lactation) to measure BUN, glucose, NEFAs, BHBA, albumin, and minerals. It is used in high-producing herds to detect subclinical negative energy balance or protein deficiencies before they manifest as clinical outbreaks of ketosis, milk fever, or displaced abomasums.",
        "Why_Not": "It is not routinely used for low-producing herds or simple diet changes unless clinical signs of metabolic collapse are present.",
        "Wow_Approach": "A high NEFA (Non-Esterified Fatty Acid) level >0.4 mEq/L in a dry cow indicates she is mobilizing excessive fat before calving, making her a massive risk for hepatic lipidosis and ketosis post-calving."
    },
    1516: {
        "topic": "VMD 411 - Veterinary Clinical Medicine I",
        "Core_Anatomy": "Multi-systemic clinical examination.",
        "Pathogenesis_Immediate": "VMD 411 focuses on general, systemic, and metabolic diseases of domestic animals.",
        "Pathogenesis_Deep": "This course forms the foundation of veterinary diagnosis, emphasizing physical examination, clinical pathology (bloodwork, urinalysis), and the pathophysiology of organ failure (e.g., cardiac, respiratory, renal, and gastrointestinal systems).",
        "Why_Not": "Unlike surgery, medicine focuses on non-invasive diagnosis and pharmacological management.",
        "Wow_Approach": "Mastering VMD requires understanding the physiological 'why' behind a clinical sign (e.g., why does right-sided heart failure cause ascites, but left-sided causes pulmonary edema)."
    },
    1517: {
        "topic": "VMD 411 Objective Section - Fact Recall",
        "Core_Anatomy": "Systemic clinical terminology.",
        "Pathogenesis_Immediate": "The objective section of VMD 411 tests precise clinical definitions and pathognomonic signs.",
        "Pathogenesis_Deep": "Questions frequently cover specialized terms (e.g., 'Lampas' for inflammation of the hard palate, 'Papple' shape for vagal indigestion, 'Melena' for digested blood). Absolute precision in terminology is required to communicate effectively with other clinicians.",
        "Why_Not": "Using layman's terms (e.g., 'nosebleed' instead of 'epistaxis') is unacceptable in clinical records.",
        "Wow_Approach": "Flashcard-style memorization of 'Condition = Pathognomonic Sign' is highly effective for this specific exam section."
    },
    1518: {
        "topic": "Vagal Indigestion - The 'Papple' Shape",
        "Core_Anatomy": "Rumen, reticulum, abomasum, and vagus nerve.",
        "Pathogenesis_Immediate": "A 'Papple' (Pear + Apple) shaped abdomen is pathognomonic for Vagal Indigestion (Type II or Type III) in cattle.",
        "Pathogenesis_Deep": "Vagal indigestion is a syndrome of motor dysfunction of the ruminant forestomach, often secondary to traumatic reticuloperitonitis (TRP) which damages the ventral vagus nerve branches. This leads to failure of omasal transport (Type II) or abomasal impaction (Type III). The rumen fills with massive amounts of fluid and gas but cannot empty. Viewed from behind, the cow's left side is distended dorsally (Apple shape - rumen gas) and the right side is distended ventrally (Pear shape - fluid), creating the classic 'Papple' contour.",
        "Why_Not": "Simple ruminal tympany (bloat) causes bilateral dorsal apple distension. Abomasal volvulus causes acute right-sided distension.",
        "Wow_Approach": "Cows with vagal indigestion often have a characteristic 'L-shaped' rumen on rectal palpation and exhibit bradycardia (heart rate <60 bpm) due to increased parasympathetic tone."
    },
    1519: {
        "topic": "Cisapride - Gastrointestinal Prokinetic",
        "Core_Anatomy": "GI smooth muscle and myenteric plexus (5-HT4 receptors).",
        "Pathogenesis_Immediate": "Cisapride is a potent gastrointestinal prokinetic drug used to treat severe GI stasis, ileus, and megaesophagus (in cats).",
        "Pathogenesis_Deep": "Cisapride acts as an agonist at serotonin (5-HT4) receptors in the myenteric plexus, facilitating the release of acetylcholine. This stimulates smooth muscle contraction along the ENTIRE gastrointestinal tract (from the lower esophageal sphincter to the colon). It is highly effective for treating feline megacolon and gastric emptying disorders.",
        "Why_Not": "Metoclopramide (another prokinetic) works mainly on the upper GI tract and crosses the blood-brain barrier (causing neurological side effects). Cisapride works on the entire GI tract and does not cross the BBB.",
        "Wow_Approach": "Cisapride was removed from the human market due to causing fatal cardiac arrhythmias (prolonged QT interval), so it is only available for veterinary use through specialized compounding pharmacies."
    },
    1523: {
        "topic": "Cholecystitis - Gallbladder Inflammation",
        "Core_Anatomy": "Gallbladder, biliary tree, and liver.",
        "Pathogenesis_Immediate": "Inflammation of the gall bladder is clinically defined as Cholecystitis.",
        "Pathogenesis_Deep": "Cholecystitis in animals (most common in dogs) is often ascending bacterial infection (E. coli, Enterococcus) from the duodenum via the common bile duct, or secondary to a gallbladder mucocele. Inflammation of the wall can lead to necrosis, rupture, and catastrophic bile peritonitis. Clinical signs include severe cranial abdominal pain, vomiting, fever, and post-hepatic icterus (jaundice).",
        "Why_Not": "Cholangitis is inflammation of the bile ducts. Hepatitis is inflammation of the liver parenchyma. Cholecystitis strictly involves the gallbladder sac.",
        "Wow_Approach": "On ultrasound, a normal dog gallbladder should have thin walls (<2mm) and anechoic (black) fluid. In cholecystitis, the wall is thickened and hyperechoic, often with 'sludge' in the lumen."
    },
    1527: {
        "topic": "Methemoglobinemia - Blood Discoloration",
        "Core_Anatomy": "Erythrocytes and hemoglobin iron.",
        "Pathogenesis_Immediate": "The statement 'Cyanosis is caused by methemoglobinemia' is technically FALSE (or misleading); methemoglobinemia causes Chocolate-Brown blood, while true cyanosis (blue blood) is caused by unoxygenated hemoglobin.",
        "Pathogenesis_Deep": "Methemoglobinemia occurs when the iron in hemoglobin is oxidized from the normal ferrous state (Fe2+) to the ferric state (Fe3+), often due to nitrite poisoning (cattle) or acetaminophen toxicity (cats). Fe3+ cannot bind oxygen. This causes the mucous membranes and blood to turn a distinct, muddy Chocolate-Brown color. True cyanosis (blue/purplish membranes) is caused by an absolute increase in deoxygenated (but normal Fe2+) hemoglobin, typically >5g/dL, due to hypoxia or heart failure.",
        "Why_Not": "Equating the two misses the toxicological mechanism. Giving oxygen helps cyanosis; giving oxygen does nothing for methemoglobinemia (you must give a reducing agent like Methylene Blue to convert Fe3+ back to Fe2+).",
        "Wow_Approach": "Drop a spot of blood on a white paper towel. If it stays brown when exposed to room air, it is methemoglobin. If it turns bright red, it was just severe venous cyanosis."
    },
    1530: {
        "topic": "The Menace Response - Cranial Nerve Assessment",
        "Core_Anatomy": "Optic nerve (CN II), visual cortex, and Facial nerve (CN VII).",
        "Pathogenesis_Immediate": "The Menace test is a neurological reflex test used to assess the function of the Optic nerve (CN II) for vision and the Facial nerve (CN VII) for the blink response.",
        "Pathogenesis_Deep": "The test is performed by making a threatening hand gesture towards the animal's eye without creating an air current. (1) Afferent pathway: The retina sees the threat, and the Optic nerve (CN II) carries the signal to the contralateral visual cortex. (2) Efferent pathway: The motor cortex signals the Facial nerve (CN VII) to contract the orbicularis oculi muscle, causing the animal to blink. A failure to blink indicates a lesion anywhere along this pathway.",
        "Why_Not": "It does not test the Oculomotor nerve (CN III), which controls pupil constriction (tested via the Pupillary Light Reflex).",
        "Wow_Approach": "The menace response is a *learned* response, not an innate reflex. It is normally absent in puppies and kittens under 10-14 days of age, even if their eyes are open and neurological tracts are intact."
    },
    1534: {
        "topic": "Prognosis - Predicting Disease Outcome",
        "Core_Anatomy": "Clinical epidemiology and disease pathology.",
        "Pathogenesis_Immediate": "The clinical forecast of the probable outcome of a disease is defined as the Prognosis.",
        "Pathogenesis_Deep": "Prognosis is the clinician's educated prediction regarding the resolution of the disease, the probability of survival, and the return to normal function. It is categorized into grades: Excellent, Good, Fair, Guarded, Poor, or Grave. Formulating a prognosis requires integrating the diagnosis, the severity of pathological changes (e.g., chronic fibrosis vs acute inflammation), the species, and the owner's financial ability to pursue treatment.",
        "Why_Not": "Diagnosis identifies the disease. Etiology identifies the cause. Pathogenesis describes the mechanism. Prognosis predicts the future.",
        "Wow_Approach": "A 'Guarded' prognosis implies that the outcome is highly uncertain and could easily deteriorate. A 'Grave' prognosis implies that death is imminent and euthanasia should be strongly considered."
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
