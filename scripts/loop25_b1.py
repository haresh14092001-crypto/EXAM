import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2819: {
        "topic": "Schmieden Suture Pattern",
        "Core_Anatomy": "Hollow organs (Intestine, Uterus).",
        "Pathogenesis_Immediate": "The Schmieden suture technique is a continuous, inverting suture pattern used primarily for Intestinal anastomosis or closing hollow organs.",
        "Pathogenesis_Deep": "The Schmieden pattern is an continuous inverting suture where the needle passes through all layers of the tissue from the MUCOSA (inside) to the SEROSA (outside) on every bite. This creates a secure, watertight inversion of the wound edges, bringing the serosal surfaces into direct contact (which is critical for rapid fibrin sealing and healing in the GI tract).",
        "Why_Not": "Teat fistulas and rectal prolapses require different specific closures. Tail gangrene requires amputation.",
        "Wow_Approach": "Because the Schmieden suture penetrates the full thickness of the bowel wall (including the contaminated mucosa), it is rarely used as a single layer today. It is usually the first layer, followed by a second layer of Lembert or Cushing sutures to bury the contaminated first layer."
    },
    2820: {
        "topic": "Thoracocentesis - Anatomical Site",
        "Core_Anatomy": "Thorax (7th intercostal space).",
        "Pathogenesis_Immediate": "The appropriate site for thoracocentesis (chest tap) in dogs and cats is the 7th or 8th intercostal space.",
        "Pathogenesis_Deep": "Thoracocentesis is a life-saving emergency procedure to drain pleural effusion or pneumothorax. The needle is inserted at the 7th or 8th intercostal space (ICS). Critically, the needle MUST be inserted just CRANIAL to the rib (e.g., just in front of the 8th rib). This is because the intercostal artery, vein, and nerve run along the CAUDAL border of each rib. Hitting the artery causes fatal iatrogenic hemothorax.",
        "Why_Not": "Going too cranial (e.g., 4th ICS) risks puncturing the heart. Going too caudal (e.g., 10th ICS) risks puncturing the diaphragm and liver.",
        "Wow_Approach": "For pneumothorax (air), tap in the DORSAL third of the thorax (air rises). For pleural effusion (fluid), tap in the VENTRAL third of the thorax (fluid sinks)."
    },
    2821: {
        "topic": "Brisket Edema - TRP",
        "Core_Anatomy": "Pericardium and Right Heart.",
        "Pathogenesis_Immediate": "Severe brisket edema (fluid accumulation in the ventral neck/chest) in cattle is the classic clinical sign of Traumatic Reticuloperitonitis (TRP) progressing to Traumatic Pericarditis.",
        "Pathogenesis_Deep": "When a sharp metallic foreign body (nail/wire) pierces the reticulum, travels through the diaphragm, and punctures the pericardial sac, it causes severe purulent pericarditis. The massive accumulation of pus and fibrin restricts the right heart's ability to fill with blood (cardiac tamponade). This causes severe backward failure (right-sided heart failure). The venous pressure in the jugular and cranial vena cava skyrockets, forcing fluid out of the vessels and creating massive dependent edema in the brisket and submandibular area.",
        "Why_Not": "Urolithiasis causes water belly (ventral abdominal edema), not brisket edema. Pervious urachus causes an umbilical drip.",
        "Wow_Approach": "A cow with traumatic pericarditis will stand with its elbows abducted (pointing outward) to relieve pressure on the chest, and will have an engorged jugular vein with a visible jugular pulse extending all the way up to the mandible."
    },
    2822: {
        "topic": "Multiple Stab Incisions - Ruptured Urethra",
        "Core_Anatomy": "Ventral abdominal subcutaneous tissue.",
        "Pathogenesis_Immediate": "Multiple stab incisions in the affected ventral abdominal area is the emergency field treatment for Subcutaneous Urine Infiltration secondary to a Ruptured Urethra.",
        "Pathogenesis_Deep": "If an obstructive urolith (stone) is not resolved, the pressure builds until the urethra ruptures. The bladder continues to pump urine, which now tracks through the fascial planes and pools in the subcutaneous tissue of the ventral abdomen and prepuce (producing 'Water Belly'). Urine is highly irritating and hyperosmolar; it rapidly causes severe subcutaneous tissue necrosis and sloughing. The immediate emergency treatment is making multiple deep stab incisions through the skin to let the trapped, toxic urine drain out by gravity.",
        "Why_Not": "TRP requires a rumenotomy. An intact obstruction requires urethrotomy or amputation of the urethral process.",
        "Wow_Approach": "A ruptured urethra is technically 'better' in the short term than a ruptured bladder. A ruptured bladder causes instant uroabdomen and rapid death from hyperkalemia. A ruptured urethra leaks into the subcutaneous space, which absorbs potassium much more slowly, buying the surgeon a little time."
    },
    2823: {
        "topic": "Urethral Process Amputation - Urolithiasis",
        "Core_Anatomy": "Urethral process (vermiform appendage).",
        "Pathogenesis_Immediate": "The urethral process is surgically cut (amputated) to treat Urolithiasis (urinary obstruction) in small ruminants.",
        "Pathogenesis_Deep": "Because the urethral process is the narrowest point of the urinary tract in rams and bucks, calculi frequently lodge there. Amputating this small, worm-like extension removes the bottleneck and often allows the stone to pass or be flushed out, immediately relieving the obstruction.",
        "Why_Not": "Cystitis is bladder inflammation. Paraphimosis is the inability to retract the penis. Urethral process amputation specifically treats distal obstruction.",
        "Wow_Approach": "Amputating the urethral process does NOT render the ram infertile; he can still breed successfully without it. It is the cheapest and most effective first-line emergency procedure for a blocked goat."
    },
    2824: {
        "topic": "Pervious Urachus - Umbilical Dribbling",
        "Core_Anatomy": "Urachus and Umbilicus.",
        "Pathogenesis_Immediate": "The condition where urine continuously dribbles from the umbilicus, keeping the area wet, is called a Pervious (Patent) Urachus.",
        "Pathogenesis_Deep": "The urachus is the embryonic tube that connects the fetal bladder to the allantoic sac via the umbilicus, allowing the fetus to excrete urine into the placenta. Normally, this tube seals and atrophies at birth (becoming the median umbilical ligament). If it fails to close (Patent Urachus), the neonate (often a foal or calf) will constantly drip urine from its belly button every time it urinates. This creates a severe risk of ascending infection (omphalitis/cystitis).",
        "Why_Not": "Urolithiasis blocks urine. Traumatic peritonitis is foreign body disease. Pervious urachus specifically involves umbilical urine leakage.",
        "Wow_Approach": "Treatment involves cauterizing the tract with silver nitrate, or surgically resecting the urachal stalk down to the apex of the bladder (omphalectomy)."
    },
    2825: {
        "topic": "Utrecht Method - Left Flank Abomasopexy",
        "Core_Anatomy": "Abomasum and Abdominal Wall.",
        "Pathogenesis_Immediate": "The Utrecht method is a surgical technique used for the correction of a Left Displaced Abomasum (LDA), specifically via a Left Flank Abomasopexy.",
        "Pathogenesis_Deep": "Unlike the Right Flank Omentopexy (the most common LDA fix), the Utrecht method approaches the cow from the LEFT flank. The surgeon reaches in, grasps the displaced, gas-filled abomasum, places a series of heavy continuous sutures (the 'Utrecht suture') directly into the greater curvature of the abomasum, leaving long ends. These heavy suture ends are then passed ventrally through the abdominal floor with a massive curved needle and tied by an assistant on the outside of the cow's belly. This physically pulls the abomasum back into its normal ventral position and anchors it permanently.",
        "Why_Not": "It is not for diaphragmatic hernias or TRP. It is a highly specific, very secure technique for anchoring a displaced abomasum.",
        "Wow_Approach": "This technique provides the strongest possible fixation for an LDA, but it requires the surgeon to pass a massive, sharp needle blindly through the cow's ventral abdominal wall, carrying a slight risk of puncturing the milk vein."
    },
    2826: {
        "topic": "Shift to the Left - TRP Hemogram",
        "Core_Anatomy": "Bone marrow (Myelopoiesis).",
        "Pathogenesis_Immediate": "A 'Shift to the left' on a leukocyte count is a key diagnostic indicator for Traumatic Reticuloperitonitis (TRP) in cattle.",
        "Pathogenesis_Deep": "A 'left shift' means there is an increased number of immature, unsegmented neutrophils (band cells) in the peripheral blood. This indicates a massive, acute systemic demand for neutrophils—the bone marrow is pumping out immature cells because the mature reserves are exhausted. In a cow presenting with sudden anorexia and abdominal pain, a severe left shift strongly supports a diagnosis of acute, purulent Traumatic Reticuloperitonitis (a hardware disease abscess).",
        "Why_Not": "Hernias do not typically cause massive purulent inflammation and left shifts unless the bowel is completely strangulated and ruptured.",
        "Wow_Approach": "Unlike dogs, cattle have very small bone marrow neutrophil reserves. Therefore, in acute TRP, a cow may actually present with NEUTROPENIA (low total white blood cells) combined with a massive left shift (lots of bands), because the infection consumes cells faster than the marrow can make them."
    },
    2827: {
        "topic": "Horn Cancer Matching",
        "Core_Anatomy": "Horn core (Processus cornualis) and frontal sinus.",
        "Pathogenesis_Immediate": "Horn cancer in cattle is matched with Squamous Cell Carcinoma.",
        "Pathogenesis_Deep": "As established in earlier loops, horn cancer is almost exclusively a Squamous Cell Carcinoma affecting the mucosal lining of the cornual diverticulum. It is overwhelmingly seen in draft breeds of Zebu cattle (Bos indicus) in India. Treatment requires complete radical amputation of the horn, often including the underlying frontal bone, to achieve clean surgical margins.",
        "Why_Not": "It is not related to air in the thorax or Setaria parasites.",
        "Wow_Approach": "The classic early clinical sign of horn cancer is unilateral epistaxis (bleeding from one nostril). Why? Because the tumor in the horn bleeds into the frontal sinus, which drains directly into the nasal cavity on that side."
    },
    2828: {
        "topic": "Guttural Pouch Matching",
        "Core_Anatomy": "Equine cervical anatomy.",
        "Pathogenesis_Immediate": "Guttural pouch is matched with Viborg's Triangle.",
        "Pathogenesis_Deep": "Viborg's triangle is the primary surgical landmark for accessing the guttural pouch (an air-filled out-pouching of the eustachian tube unique to horses) to drain empyema or treat mycosis.",
        "Why_Not": "N/A",
        "Wow_Approach": "Fungal plaques (Aspergillus) in the guttural pouch love to grow directly over the internal carotid artery. If the fungus erodes the artery wall, the horse will suddenly bleed to death from its nose. Treatment involves tying off the artery (ligation) or blocking it with a coil to starve the fungus and stop the bleeding."
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
