import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1592: {
        "topic": "Canine Blood Types - DEA 1.1",
        "Core_Anatomy": "Erythrocyte surface antigens.",
        "Pathogenesis_Immediate": "The most potent and clinically significant antigenic blood group in the dog is DEA 1.1 (Dog Erythrocyte Antigen 1.1).",
        "Pathogenesis_Deep": "Dogs do not have naturally occurring alloantibodies to DEA 1.1. If a DEA 1.1-negative dog receives DEA 1.1-positive blood for the first time, the transfusion will be safe, but the recipient's immune system will become highly sensitized, producing massive amounts of anti-DEA 1.1 antibodies within 7-10 days. If that dog ever receives a second DEA 1.1-positive transfusion, those antibodies will cause an acute, fatal hemolytic transfusion reaction.",
        "Why_Not": "DEA 1.2, 1.3, and 4 are far less antigenic and rarely cause acute, fatal hemolysis compared to DEA 1.1.",
        "Wow_Approach": "Because there are no naturally occurring antibodies, a dog's first-ever blood transfusion in an emergency can be given without a crossmatch, but a second transfusion in their lifetime MUST be crossmatched."
    },
    1593: {
        "topic": "Respiratory Patterns - Biot's Respiration",
        "Core_Anatomy": "Medulla oblongata (respiratory center).",
        "Pathogenesis_Immediate": "Biot's respiration (ataxic breathing) is typically observed in severe neurological diseases like Meningitis or severe brainstem trauma.",
        "Pathogenesis_Deep": "Biot's respiration is an abnormal breathing pattern characterized by groups of quick, shallow inspirations followed by completely irregular, unpredictable periods of apnea (breath-holding). It indicates direct damage to the respiratory centers in the medulla oblongata, often due to increased intracranial pressure compressing the brainstem, as seen in diffuse suppurative meningitis or head trauma.",
        "Why_Not": "Diabetic ketoacidosis causes Kussmaul respiration (deep, rapid, gasping breaths to blow off CO2). Myocarditis causes generalized tachypnea. Biot's is purely a neurological pattern.",
        "Wow_Approach": "If a patient with head trauma suddenly develops Biot's respiration, it is a grave prognostic sign indicating imminent medullary herniation and death."
    },
    1594: {
        "topic": "Vital Signs - Pulse to Respiration Ratio",
        "Core_Anatomy": "Cardiorespiratory systemic coupling.",
        "Pathogenesis_Immediate": "The normal physiological Pulse-to-Respiration ratio in most resting domestic mammals is approximately 4:1.",
        "Pathogenesis_Deep": "In a healthy resting state, the heart beats about four times for every one breath taken. This 4:1 ratio optimizes the coupling of pulmonary blood flow (perfusion) with alveolar air flow (ventilation), ensuring optimal oxygen uptake. If this ratio is disrupted, it immediately signals a localized pathology.",
        "Why_Not": "A 2:1 ratio would mean the animal is breathing exceptionally fast (severe respiratory disease/hypoxia). A 10:1 ratio means the animal is breathing too slowly or the heart is racing (severe shock/tachycardia).",
        "Wow_Approach": "If a dog has a heart rate of 120 bpm and a respiratory rate of 30 brpm (4:1), it is likely just excited. If the HR is 120 and the RR is 80 (1.5:1), the dog is in severe respiratory distress."
    },
    1595: {
        "topic": "Ruminant Ketosis - Cobalt Deficiency Link",
        "Core_Anatomy": "Rumen microbiome and hepatic gluconeogenesis.",
        "Pathogenesis_Immediate": "Primary ketosis in sheep (Pregnancy Toxemia) and cattle can occur secondary to a nutritional deficiency of Cobalt.",
        "Pathogenesis_Deep": "Cobalt is an absolute requirement for the rumen microbes to synthesize Vitamin B12 (Cyanocobalamin). Vitamin B12 is the essential coenzyme for methylmalonyl-CoA mutase, the enzyme that converts propionate (from the rumen) into glucose in the liver. Without Cobalt, there is no B12; without B12, the liver cannot use propionate for gluconeogenesis. The animal enters a severe negative energy balance and begins rapidly mobilizing body fat, producing massive amounts of toxic ketones.",
        "Why_Not": "Calcium deficiency causes milk fever. Magnesium causes grass tetany. Cobalt specifically paralyzes the primary gluconeogenic pathway in ruminants.",
        "Wow_Approach": "In cobalt-deficient areas (like parts of Australia or Florida), administering oral glucose to a ketotic sheep will fail if you do not also administer an injection of Vitamin B12 to unlock the hepatic pathway."
    },
    1596: {
        "topic": "Veterinary Jurisprudence - Wildlife Protection Act",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The Wildlife Protection Act (WPA) in India was implemented in the year 1972.",
        "Pathogenesis_Deep": "The WPA 1972 is the foundational legal framework for the protection of plant and animal species in India. It establishes Schedules (I to VI) that categorize the protection status of various species. Veterinary clinicians working with rescued wildlife, zoo animals, or dealing with poaching/forensic cases must operate strictly within the legal bounds of this act.",
        "Why_Not": "1970, 1775, and 1979 are incorrect historical dates. 1972 is the landmark year for Indian wildlife conservation legislation.",
        "Wow_Approach": "Under Schedule I of the WPA 1972, treating a highly endangered species (like a tiger or elephant) requires mandatory reporting and coordination with the Chief Wildlife Warden of the state."
    },
    1597: {
        "topic": "Poultry Pathology - Femoral Head Necrosis",
        "Core_Anatomy": "Proximal femur (growth plate) and articular cartilage.",
        "Pathogenesis_Immediate": "Femoral head necrosis in fast-growing poultry (broilers) is often linked to infectious osteomyelitis, but nutritionally can be exacerbated by imbalances in Calcium, Phosphorus, and trace minerals.",
        "Pathogenesis_Deep": "Bacterial Chondronecrosis with Osteomyelitis (BCO) is the primary cause of femoral head necrosis (often involving Staphylococcus or E. coli). However, the underlying structural weakness that allows the bacteria to settle in the bone is often due to rapid growth outstripping the bone's mineralization capacity. Severe deficiencies or imbalances in Calcium, Phosphorus, or Vitamin D3 lead to tibial dyschondroplasia and micro-fractures in the femoral head growth plate, creating a nidus for infection.",
        "Why_Not": "While Molybdenum (Mo) toxicity can induce Copper deficiency (leading to weak collagen), the primary macroscopic nutritional drivers of bone necrosis are Ca/P imbalances.",
        "Wow_Approach": "On necropsy, snapping the femur at the hip joint will reveal a fragile, crumbling, necrotic femoral head that easily detaches from the articular cartilage."
    },
    1598: {
        "topic": "Renal Pathology - Nephritis vs Nephrosis",
        "Core_Anatomy": "Renal parenchyma (glomeruli and tubules).",
        "Pathogenesis_Immediate": "Kidney disease characterized by BOTH degenerative changes (tubular necrosis) and inflammatory changes (leukocyte infiltration) is broadly termed Nephritis or Nephropathy.",
        "Pathogenesis_Deep": "Pathologists carefully distinguish between the two: (1) Nephrosis refers strictly to toxic or ischemic degeneration of the renal tubules WITHOUT primary inflammation (e.g., ethylene glycol toxicity). (2) Nephritis involves active inflammation driven by infectious agents or immune complexes (e.g., Leptospirosis, glomerulonephritis). In chronic, advanced clinical cases, the two processes overlap—initial inflammation causes ischemia, leading to secondary tubular degeneration.",
        "Why_Not": "Using the terms interchangeably is technically incorrect. Nephrosis is non-inflammatory degeneration; Nephritis is active inflammation.",
        "Wow_Approach": "A patient with pure nephrosis (like antifreeze poisoning) will often have a normal WBC count but massive urinary casts, whereas a patient with bacterial nephritis will have a severe leukocytosis and pyuria (pus in the urine)."
    },
    1604: {
        "topic": "Bovine Bloat - Primary vs Secondary Tympany",
        "Core_Anatomy": "Rumen and cardia (esophageal sphincter).",
        "Pathogenesis_Immediate": "The statement 'Feed lot bloat usually causes secondary tympany' is FALSE; feedlot bloat is a form of Primary (Frothy) Tympany.",
        "Pathogenesis_Deep": "Bloat (tympany) is classified into two types. Primary Bloat (Frothy Bloat) occurs when animals eat highly fermentable diets (lush legumes or high-grain feedlot rations). The rumen fluid becomes viscous, trapping the gas in millions of tiny bubbles (foam) that the cow cannot eructate. Secondary Bloat (Free-Gas Bloat) occurs due to a physical obstruction of the esophagus (e.g., a stuck potato) or vagal nerve damage, preventing the cow from burping a normal, single large gas pocket.",
        "Why_Not": "Feedlot bloat involves grain causing mucopolysaccharide slime production by bacteria, trapping the gas as froth. This is the definition of primary bloat.",
        "Wow_Approach": "Passing a stomach tube easily cures Secondary (free-gas) bloat as the gas rushes out. In Primary (frothy) bloat, passing a tube does nothing because the gas is trapped in foam; you must administer anti-foaming agents (like poloxalene or vegetable oil) to break the bubbles."
    },
    1605: {
        "topic": "Trace Minerals - Copper and Enzootic Ataxia",
        "Core_Anatomy": "Brainstem and spinal cord white matter.",
        "Pathogenesis_Immediate": "Copper deficiency in pregnant ewes matches to the classic neonatal neurological disease 'Enzootic Ataxia' (Swayback) in lambs.",
        "Pathogenesis_Deep": "Copper is required by the enzyme cytochrome c oxidase for normal myelin synthesis in the fetal CNS. If the ewe is severely copper deficient during mid-to-late gestation, the lamb's spinal cord (specifically the motor tracts) fails to myelinate properly. The lamb is born with irreversible posterior paresis, staggering, and swaying of the hindquarters ('Swayback').",
        "Why_Not": "Autoimmune hemolytic anemia is immune-mediated, not nutritional. Bleeding disorders are linked to Vitamin K.",
        "Wow_Approach": "Because the demyelination occurs in utero, treating the affected newborn lamb with copper is completely useless. The only prevention is supplementing the ewe during pregnancy."
    },
    1606: {
        "topic": "Urinalysis - The Benzidine Test",
        "Core_Anatomy": "Urinary tract and erythrocytes.",
        "Pathogenesis_Immediate": "The Benzidine test is a classic biochemical assay matched to the detection of Occult Blood in urine or feces.",
        "Pathogenesis_Deep": "The Benzidine test relies on the peroxidase-like activity of the heme molecule in hemoglobin. When a sample containing trace amounts of blood (even if visually undetectable, i.e., 'occult') is mixed with the benzidine reagent and hydrogen peroxide, the heme catalyzes the oxidation of benzidine into a brilliant blue/green color. It is highly sensitive for detecting micro-hematuria or upper GI bleeding (melena).",
        "Why_Not": "The test detects blood, not specific vitamins like Cyanocobalamin or Vitamin K.",
        "Wow_Approach": "Because benzidine was found to be a potent human carcinogen, modern veterinary clinics have largely replaced it with less toxic alternatives (like tetramethylbenzidine on standard urine dipsticks), though the biochemical principle remains identical."
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
print(f"Batch 2/5 DONE: Updated {updated} questions.")
