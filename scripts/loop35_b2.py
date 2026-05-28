import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3956: {
        "topic": "Brisket Edema - Traumatic Pericarditis",
        "Core_Anatomy": "Subcutaneous tissue of the brisket and Cranial Vena Cava.",
        "Pathogenesis_Immediate": "Brisket edema (ventral edema) is a classic pathognomonic clinical sign of advanced Traumatic Reticuloperitonitis (specifically Traumatic Pericarditis) in cattle.",
        "Pathogenesis_Deep": "As reviewed, when a foreign body penetrates the reticulum and enters the pericardial sac, it causes severe, septic, suppurative pericarditis. The heart is compressed by massive accumulations of pus (cardiac tamponade), preventing normal venous return. This causes intense passive venous congestion in the cranial vena cava and jugular veins, forcing fluid to leak into the loose subcutaneous tissues of the brisket (chest), causing a cold, painless, massive swelling.",
        "Why_Not": "Obstructive urolithiasis causes 'water belly' (edema of the ventral abdomen/prepuce), not isolated brisket edema.",
        "Wow_Approach": "Cattle with traumatic pericarditis often show a 'jugular pulse'—the jugular veins in the neck appear like thick, rigid ropes and visibly pulsate with every heartbeat."
    },
    3957: {
        "topic": "Thoracocentesis Incision Site",
        "Core_Anatomy": "Pleural Cavity and Intercostal space.",
        "Pathogenesis_Immediate": "The appropriate site for a thoracocentesis (chest tap) incision in dogs is the 5th to 7th intercostal space.",
        "Pathogenesis_Deep": "Thoracocentesis is performed to drain pleural effusion or air (pneumothorax). The needle must be inserted at the 6th or 7th intercostal space, just cranial to the rib edge. The needle is inserted near the costochondral junction for fluid (which accumulates ventrally due to gravity) and near the dorsal third for air (which rises).",
        "Why_Not": "Inserting the needle near the caudal edge of the rib is strictly avoided because the intercostal artery, vein, and nerve run right along the caudal border of each rib, risking severe hemorrhage.",
        "Wow_Approach": "N/A"
    },
    3958: {
        "topic": "Utrecht Suture Method - C-Section",
        "Core_Anatomy": "Uterus.",
        "Pathogenesis_Immediate": "The Utrecht method is a highly specialized, continuous inverting suture pattern used exclusively for closing the Uterus during a Caesarean section.",
        "Pathogenesis_Deep": "To close the massive incision in the pregnant uterus, the suture must be fluid-tight to prevent leakage of lochia, and completely inverting so that no suture material is exposed to the peritoneal cavity (preventing post-surgical abdominal adhesions). The Utrecht pattern is a modified continuous Lembert suture where the needle is inserted obliquely (angled) through the muscularis/serosa, completely burying the knots.",
        "Why_Not": "Left flank omentopexy (like the Utrecht method LDA fix) is a technique for correcting LDA, but the primary Utrecht surgical method is for hysterotomy closure.",
        "Wow_Approach": "N/A"
    },
    3959: {
        "topic": "Weingarth's Rumenotomy Frame",
        "Core_Anatomy": "Rumen and Abdominal Wall.",
        "Pathogenesis_Immediate": "Weingarth's Rumenotomy Frame is a specialized surgical device used during a Rumenotomy (usually for foreign body retrieval in Traumatic Reticulitis).",
        "Pathogenesis_Deep": "A rumenotomy involves opening the massive rumen (which contains hundreds of liters of highly fermentable, bacteria-rich ingesta). If any rumen fluid leaks into the peritoneal cavity, the cow will die of septic peritonitis. Weingarth's frame consists of a metal frame with multiple sharp hooks. The rumen wall is pulled out of the laparotomy incision, clamped securely to the frame's hooks, and the frame is secured to the skin, creating a perfect seal that completely isolates the rumen contents from the abdomen.",
        "Why_Not": "A C-section or diaphragmatic hernia surgery does not open the rumen, making the frame unnecessary.",
        "Wow_Approach": "N/A"
    },
    3960: {
        "topic": "Paraphimosis Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Sheep, Goat, Buffalo, All) for a paraphimosis question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3961: {
        "topic": "Paraphimosis",
        "Core_Anatomy": "Penis and Prepuce.",
        "Pathogenesis_Immediate": "Paraphimosis refers specifically to the inability to retract the extended penis back into the prepuce.",
        "Pathogenesis_Deep": "It is caused by trauma, severe swelling of the prepuce or penis, or retractor penis muscle paralysis (e.g., secondary to acepromazine sedation in horses). The exposed penis undergoes intense venous congestion and edema, making it increasingly swollen and heavy, eventually leading to thrombosis and gangrene if not treated.",
        "Why_Not": "Phimosis is the inability to EXTEND the penis out of the prepuce, usually congenital.",
        "Wow_Approach": "N/A"
    },
    3962: {
        "topic": "Schmiden's Suture - Intestinal Anastomosis",
        "Core_Anatomy": "Gastrointestinal tract wall.",
        "Pathogenesis_Immediate": "Schmiden's suture is a continuous, inverting, all-coats suture pattern classically used for Intestinal Anastomosis.",
        "Pathogenesis_Deep": "Schmiden's pattern involves passing the suture needle from the inside (mucosa) out through the serosa, and then repeating this on the opposite side. This provides excellent mucosal inversion and an airtight seal, which is critical during bowel resection and anastomosis to prevent leakage.",
        "Why_Not": "It is strictly a visceral suture and has no application in teat fistulas or tail gangrene.",
        "Wow_Approach": "N/A"
    },
    3963: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3964: {
        "topic": "Intussusception",
        "Core_Anatomy": "Intestinal Tract (Ileocolic junction).",
        "Pathogenesis_Immediate": "Intussusception is the telescoping (invagination) of one segment of the intestine into an adjacent segment.",
        "Pathogenesis_Deep": "The invaginating segment is called the intussusceptum, and the receiving segment is the intussuscipiens. This occurs secondary to abnormal hypermotility (e.g., severe enteritis or parasite burden). As it telescopes, the mesentery is dragged inside, cutting off the blood supply and causing rapid necrosis and complete intestinal obstruction.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3965: {
        "topic": "Intestinal Obstruction",
        "Core_Anatomy": "Gastrointestinal lumen.",
        "Pathogenesis_Immediate": "Intestinal obstruction is a mechanical block of the flow of ingesta through the bowel.",
        "Pathogenesis_Deep": "It leads to severe gas and fluid distension proximal to the block. The massive distension stimulates nociceptors, causing intense, acute abdominal pain (colic).",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
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
