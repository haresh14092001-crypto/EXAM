import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2523: {
        "topic": "Thoracocentesis - Optimal Site",
        "Core_Anatomy": "Thoracic cavity (pleural space) and intercostal spaces.",
        "Pathogenesis_Immediate": "The appropriate site for thoracocentesis (pleural fluid aspiration) is the 7th intercostal space.",
        "Pathogenesis_Deep": "Thoracocentesis is performed to relieve pleural effusion (e.g., chylothorax, hemothorax, pyothorax) or pneumothorax. In most domestic species (dogs, cats, cattle, horses), the optimal safe window for needle insertion is the 7th or 8th intercostal space, low on the chest wall for fluid (which settles ventrally) or high for air (which rises dorsally). Puncturing too far cranial risks hitting the heart; puncturing too far caudal risks penetrating the diaphragm and entering the abdomen.",
        "Why_Not": "The 5th ICS is too close to the heart (used for pericardiocentesis, not thoracocentesis). The 7th-8th ICS avoids major thoracic organs while safely entering the pleural cavity.",
        "Wow_Approach": "Always insert the needle just CRANIAL to the rib (e.g., just in front of the 8th rib in the 7th space) because the intercostal artery, vein, and nerve run along the CAUDAL border of every rib."
    },
    2524: {
        "topic": "Brisket Edema - Traumatic Pericarditis",
        "Core_Anatomy": "Pericardium and systemic venous circulation (jugular/caval system).",
        "Pathogenesis_Immediate": "Brisket edema in cattle is classically seen in Traumatic Pericarditis (a sequela of Traumatic Reticuloperitonitis).",
        "Pathogenesis_Deep": "When a sharp metallic foreign body (wire/nail) penetrates the reticulum, passes through the diaphragm, and punctures the pericardial sac, it introduces mixed ruminal microflora into the pericardium. This causes severe purulent, fibrinous pericarditis. The thickened pericardium and massive fluid accumulation physically restrict the heart from filling during diastole (cardiac tamponade). This right-sided heart failure causes venous congestion, leading to jugular distension and massive transudation of fluid into the dependent subcutaneous tissues of the brisket and ventral abdomen.",
        "Why_Not": "Obstructive urolithiasis causes ventral edema (urine infiltration) but 'brisket edema' is the classic pathognomonic term for cardiac failure/traumatic pericarditis in bovine medicine.",
        "Wow_Approach": "The classic clinical triad for Traumatic Pericarditis: (1) Engorged, pulsating jugular veins, (2) Massive brisket edema, (3) 'Washing machine' murmur (splashing sounds) on cardiac auscultation."
    },
    2525: {
        "topic": "Urolithiasis - Subcutaneous Urine Infiltration",
        "Core_Anatomy": "Subcutaneous tissues of the ventral abdomen.",
        "Pathogenesis_Immediate": "Multiple stab incisions in the affected ventral area is the emergency treatment for Obstructive Urolithiasis that has progressed to urethral rupture.",
        "Pathogenesis_Deep": "In obstructive urolithiasis in steers or rams, if the urethra ruptures completely before the bladder does, urine leaks rapidly into the subcutaneous connective tissues of the ventral abdomen and prepuce (producing 'Water Belly'). Urine is highly irritating; it causes severe chemical cellulitis, tissue necrosis, and sloughing. The immediate emergency treatment is making multiple deep stab incisions through the skin of the swollen ventral abdomen to allow the trapped, necrotic urine to drain out, preventing fatal systemic uremia and gangrene.",
        "Why_Not": "Traumatic peritonitis is in the abdomen, not subcutaneous. This specific stab-incision drainage protocol is exclusively for subcutaneous urine infiltration following urethral rupture.",
        "Wow_Approach": "These stab incisions must be left open to heal by second intention. Concurrently, a perineal urethrostomy or tube cystostomy must be performed to divert new urine away from the ruptured urethral site."
    },
    2526: {
        "topic": "Urolithiasis - Urethral Process Amputation",
        "Core_Anatomy": "Urethral process (processus urethrae) of the glans penis.",
        "Pathogenesis_Immediate": "The urethral process is surgically cut (amputated) to relieve Obstructive Urolithiasis in sheep and goats.",
        "Pathogenesis_Deep": "Rams and bucks have a unique anatomical extension of the urethra at the tip of the penis called the urethral process (or vermiform appendage). Because this process is extremely narrow, it is the most common site for urinary calculi (stones) to lodge, causing complete urinary obstruction. The fastest, simplest first-line treatment is to exteriorize the penis and amputate the urethral process with scissors. This often immediately releases the lodged stone and restores urine flow without affecting future breeding ability.",
        "Why_Not": "Paraphimosis is the inability to retract the penis, treated by reduction or circumcision, not cutting the urethral process. Cystitis is bladder inflammation. The urethral process amputation is strictly for urolithiasis.",
        "Wow_Approach": "While amputating the urethral process fixes the immediate blockage in about 50% of cases, many goats have additional stones lodged higher up at the sigmoid flexure, requiring more invasive surgery (tube cystostomy) if amputation fails to restore flow."
    },
    2527: {
        "topic": "Pervious Urachus - Umbilical Urine Dribbling",
        "Core_Anatomy": "Urachus and umbilicus.",
        "Pathogenesis_Immediate": "A condition where urine dribbles from the umbilicus and the area remains constantly wet is called Pervious Urachus (Patent Urachus).",
        "Pathogenesis_Deep": "The urachus is the embryonic tube connecting the fetal urinary bladder to the allantoic sac via the umbilical cord. Normally, this tube closes and atrophies immediately at birth as the bladder shifts to urethral voiding. If the urachus fails to close (congenital patent urachus) or reopens due to neonatal umbilical infection (acquired pervious urachus), urine will continuously leak from the umbilicus. This causes scalding of the ventral abdomen and provides a direct route for bacteria to ascend into the bladder and bloodstream (sepsis/joint ill).",
        "Why_Not": "Obstructive urolithiasis causes urethral/bladder rupture, not umbilical leakage. Traumatic peritonitis does not involve urine.",
        "Wow_Approach": "In foals, patent urachus can sometimes be resolved chemically by cauterizing the umbilical stump with silver nitrate or strong iodine. If this fails after a few days, surgical resection of the urachus and the apex of the bladder is mandatory."
    },
    2528: {
        "topic": "Utrecht Method - Uterine Torsion / Prolapse",
        "Core_Anatomy": "Bovine reproductive tract and abdominal wall.",
        "Pathogenesis_Immediate": "The Utrecht method is classically associated with surgical/obstetrical techniques developed at Utrecht University, particularly the Left Flank approach for Caesarean section and Omentopexy.",
        "Pathogenesis_Deep": "In veterinary surgery, the 'Utrecht method' frequently refers to the Left Flank Omentopexy technique developed by the Utrecht veterinary school for correcting Left Displaced Abomasum (LDA), or the specific suturing technique for closing the uterus during a C-section (the Utrecht suture pattern: a continuous, inverting, sero-muscular pattern that minimizes exposed suture material to prevent adhesions). In the context of the MCQ options, Left Flank Omentopexy is the intended answer.",
        "Why_Not": "Traumatic reticuloperitonitis is treated via rumenotomy, not the Utrecht method.",
        "Wow_Approach": "The Utrecht uterine suture pattern is revolutionary because it buries the knot at both ends of the incision, leaving zero exposed suture material in the abdomen, virtually eliminating the risk of postoperative uterine adhesions to the rumen or intestines."
    },
    2529: {
        "topic": "Shift to the Left - Traumatic Reticuloperitonitis",
        "Core_Anatomy": "Bone marrow (neutrophil production) and systemic circulation.",
        "Pathogenesis_Immediate": "A 'Shift to the Left' in the leukogram (blood test) is used diagnostically to confirm severe acute inflammation, classically applied in bovine Traumatic Reticuloperitonitis (TRP).",
        "Pathogenesis_Deep": "A 'left shift' refers to the presence of immature, unsegmented neutrophils (band cells) in the peripheral blood. When a foreign body pierces the reticulum and causes acute peritonitis (TRP), the massive tissue demand for neutrophils rapidly depletes the mature segmented neutrophils in the blood. The bone marrow responds by releasing immature band cells prematurely. A 'regenerative left shift' (elevated total WBCs with band cells) strongly supports the diagnosis of an acute, localized suppurative process like TRP before it becomes chronic walled-off.",
        "Why_Not": "Diaphragmatic hernias are mechanical disruptions, not acute suppurative infections, so they do not cause a massive left shift. TRP is the classic bovine disease producing this hematological profile.",
        "Wow_Approach": "In cattle, the bone marrow reserve of mature neutrophils is very small compared to dogs. Therefore, in acute TRP, a cow's total white cell count initially drops (neutropenia) as cells rush to the abdomen, followed by a massive release of band cells (degenerative left shift) within 24 hours."
    },
    2530: {
        "topic": "Horn Cancer - Bovine Squamous Cell Carcinoma",
        "Core_Anatomy": "Horn core (processus cornualis) and squamous epithelium.",
        "Pathogenesis_Immediate": "Horn cancer in cattle (particularly Zebu breeds) is a Squamous Cell Carcinoma.",
        "Pathogenesis_Deep": "Horn cancer is unique to Bos indicus (Zebu) cattle and is virtually never seen in Bos taurus breeds. It originates from the squamous epithelium at the mucocutaneous junction of the horn base. The tumor aggressively invades the frontal sinus, causing a unilateral nasal discharge, head tilt, and a foul-smelling, cauliflower-like ulcerated growth at the base of the horn. Chronic irritation from ropes used to tie the horns, combined with prolonged solar UV exposure, are the primary etiological factors.",
        "Why_Not": "Horn cancer does not involve air in the thoracic cavity (pneumothorax). The treatment is surgical amputation of the horn and curettage of the frontal sinus.",
        "Wow_Approach": "Because the horn core communicates directly with the frontal sinus in cattle, horn cancer is rarely just a surface skin tumor—by the time it is visible, it has almost always invaded the sinus cavity, making complete surgical excision very difficult."
    },
    2531: {
        "topic": "Guttural Pouch - Viborg's Triangle",
        "Core_Anatomy": "Equine head (Eustachian tube diverticulum).",
        "Pathogenesis_Immediate": "The Guttural Pouch is surgically accessed via Viborg's Triangle to treat empyema or chondroids.",
        "Pathogenesis_Deep": "The guttural pouches are large, air-filled outpouchings of the Eustachian tubes unique to equids. When infected (e.g., by Streptococcus equi in Strangles), they fill with pus (empyema) which can desiccate into hard, stone-like 'chondroids'. To surgically drain the pouch, the surgeon approaches through Viborg's Triangle—a safe surgical window bordered by the mandible (cranial), the linguofacial vein (ventral), and the tendon of the sternocephalicus muscle (dorsocaudal)—avoiding the critical cranial nerves and carotid arteries passing through the pouch.",
        "Why_Not": "Cushing suture pattern is for hollow organs (bladder/uterus), not the guttural pouch.",
        "Wow_Approach": "The guttural pouch houses the internal carotid artery and cranial nerves IX, X, XI, and XII. Fungal infection (Guttural Pouch Mycosis) can erode the carotid artery, causing sudden, catastrophic, and often fatal epistaxis (nosebleed)."
    },
    2532: {
        "topic": "Eye Worm - Setaria / Thelazia",
        "Core_Anatomy": "Conjunctival sac and anterior chamber of the eye.",
        "Pathogenesis_Immediate": "The term 'Eye worm' in large animals is matched to Setaria species (aberrant migration) or Thelazia species (true eye worm).",
        "Pathogenesis_Deep": "Thelazia (e.g., T. rhodesii in cattle, T. lacrymalis in horses) is the true eye worm, living in the conjunctival sac and lacrimal ducts, transmitted by face flies. However, in India, aberrant migration of the microfilariae of Setaria digitata (or Setaria equina) frequently results in the worm ending up in the anterior chamber of the horse's eye, swimming visibly in the aqueous humor. This causes severe immune-mediated uveitis and corneal opacity.",
        "Why_Not": "Setaria normally lives in the peritoneal cavity of cattle; its appearance in the eye is an aberrant (mistaken) migration. True eye worms are Thelazia.",
        "Wow_Approach": "Surgical removal of a Setaria worm from the anterior chamber requires a clear corneal stab incision (paracentesis) under standing sedation and local nerve block—the worm is literally flushed out with a jet of sterile saline to save the horse's vision."
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
