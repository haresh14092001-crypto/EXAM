import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2587: {
        "topic": "Corneal Opacity - Leukoma",
        "Core_Anatomy": "Corneal stroma.",
        "Pathogenesis_Immediate": "A dense, dense white opacity of the cornea is called a Leukoma.",
        "Pathogenesis_Deep": "Corneal opacities resulting from scarring (fibrosis) are graded by their density. (1) Nebula: A very faint, cloud-like opacity that allows underlying iris details to be seen. (2) Macula: A moderately dense opacity. (3) Leukoma: A completely dense, opaque, white scar that totally obscures the underlying intraocular structures (iris and pupil). This usually results from deep stromal ulceration where the cornea heals with opaque disorganized scar tissue (fibrosis) rather than perfectly parallel collagen fibrils.",
        "Why_Not": "Nebulae and Maculae are less dense. Pannus is a specific immune-mediated chronic superficial keratitis (vascularized pink/pigmented tissue), not just a white scar.",
        "Wow_Approach": "If the leukoma has a tiny strand of iris tissue adhered to its posterior surface (adherent leukoma), it indicates that a previous deep corneal ulcer actually perforated, and the iris plugged the hole to save the eye from collapsing."
    },
    2588: {
        "topic": "Omphalophlebitis - Umbilicus",
        "Core_Anatomy": "Umbilical vein and neonatal systemic circulation.",
        "Pathogenesis_Immediate": "Omphalophlebitis is the inflammation/infection of the Umbilicus and its associated veins (Navel Ill).",
        "Pathogenesis_Deep": "At birth, the umbilical cord contains two umbilical arteries, one umbilical vein, and the urachus. If the stump is heavily contaminated with environmental bacteria (E. coli, Trueperella pyogenes, Streptococcus) before it dries and closes, bacteria ascend the umbilical vein (which leads directly to the liver). This causes omphalophlebitis (Navel Ill). The bacteria then shower into the systemic circulation, causing septicemia and localizing in the joints (producing the classic 'Joint Ill' or suppurative polyarthritis in calves and foals).",
        "Why_Not": "Omasum and Abomasum are stomach compartments. The umbilicus is the anatomical structure affected in omphalophlebitis.",
        "Wow_Approach": "Because the umbilical vein travels cranially to the liver, a severe case of omphalophlebitis in a calf often results in massive hepatic abscessation, necessitating surgical resection (omphalectomy) of the entire infected stalk up to the liver margin."
    },
    2589: {
        "topic": "Oesophageal Anatomy - Devoid of Serosa",
        "Core_Anatomy": "Oesophageal wall layers.",
        "Pathogenesis_Immediate": "The oesophagus is unique among the gastrointestinal tract because it is devoid of a Serosa layer (in its cervical portion).",
        "Pathogenesis_Deep": "The histological layers of the intestine are mucosa, submucosa, muscularis, and serosa. The serosa (visceral peritoneum) is critical for surgical healing because it rapidly exudes fibrin, creating a water-tight seal over a surgical incision within hours. The cervical oesophagus lacks a serosa; it is covered only by loose connective tissue (adventitia). Furthermore, the oesophagus undergoes constant movement (swallowing) and lacks a redundant blood supply. Combined, these factors make the oesophagus the most notoriously difficult organ in the body to heal surgically, with a very high risk of postoperative dehiscence and stricture.",
        "Why_Not": "It possesses a mucosa, submucosa (the holding layer for sutures), and muscularis. The absence of the serosa is its key surgical vulnerability.",
        "Wow_Approach": "Due to this poor healing capacity, oesophageal surgery is avoided whenever possible. If an oesophageal foreign body cannot be removed endoscopically, it is generally pushed INTO the stomach for a gastrotomy removal, rather than cutting the oesophagus itself."
    },
    2590: {
        "topic": "Urate Calculi - Dalmatian Dogs",
        "Core_Anatomy": "Hepatic purine metabolism and urinary bladder.",
        "Pathogenesis_Immediate": "Urate (ammonium biurate) urinary calculi are most common in Dalmatian dogs.",
        "Pathogenesis_Deep": "Due to a unique autosomal recessive genetic mutation in the SLC2A9 gene, Dalmatians have a defect in uric acid transport. Most dogs convert uric acid (a byproduct of purine metabolism) into highly water-soluble allantoin via the hepatic enzyme uricase. Dalmatians cannot transport uric acid into the hepatocytes efficiently for this conversion. Therefore, they excrete massive amounts of insoluble uric acid into their urine. In acidic urine, this precipitates to form ammonium urate calculi (stones), leading to severe lower urinary tract obstruction.",
        "Why_Not": "Dachshunds are prone to cystine calculi. Boxers and Dobermans do not have this specific purine metabolism defect. The Dalmatian is the classic board exam breed for urate stones.",
        "Wow_Approach": "Urate stones are radiolucent (they do not show up well on plain X-rays). Diagnosis requires ultrasound or double-contrast cystography. Medical management involves feeding a low-purine diet and administering Allopurinol to inhibit xanthine oxidase."
    },
    2591: {
        "topic": "Scrotal Hernia - Oscheocele",
        "Core_Anatomy": "Inguinal canal and vaginal tunic.",
        "Pathogenesis_Immediate": "A scrotal hernia is otherwise technically called an Oscheocele.",
        "Pathogenesis_Deep": "An inguinal hernia occurs when abdominal contents pass through the inguinal ring. If the herniated contents (usually omentum or a loop of intestine) travel all the way down the inguinal canal and descend fully into the scrotum alongside the testicle, it is termed a scrotal hernia (Oscheocele). This is common in pigs and horses. In pigs, it is highly heritable.",
        "Why_Not": "Bubonocele is an incomplete inguinal hernia (the contents remain in the groin/inguinal canal and do not reach the scrotum). Hydrocele is a fluid accumulation in the tunica vaginalis, not a hernia. Vesiculocele is a hernia containing the bladder.",
        "Wow_Approach": "During castration of a piglet with a scrotal hernia, the surgeon MUST use a 'closed castration' technique (ligating the tunica vaginalis tightly) without opening the tunic. Doing an open castration will result in the pig's intestines immediately spilling out onto the floor."
    },
    2592: {
        "topic": "Intussusception - Ileocecocolic Junction",
        "Core_Anatomy": "Ileum, cecum, and colon.",
        "Pathogenesis_Immediate": "The Ileocecocolic junction is the most common anatomical site for intestinal intussusception in dogs.",
        "Pathogenesis_Deep": "Intussusception is the telescoping of one segment of the intestine (the intussusceptum) into the lumen of an adjacent distal segment (the intussuscipiens), causing mechanical obstruction and ischemic necrosis of the trapped bowel. This most frequently occurs at the ileocecocolic junction, where the narrow, highly motile ileum telescopes into the wider, less motile colon. It is commonly triggered by hypermotility secondary to heavy parasitism (hookworms), parvovirus enteritis, or sudden diet changes in puppies.",
        "Why_Not": "While jejuno-jejunal intussusceptions occur, the ileocecocolic junction is the classic textbook location due to the abrupt change in luminal diameter and motility patterns at that specific valve.",
        "Wow_Approach": "On abdominal palpation, an ileocecocolic intussusception feels like a firm, painful, 'sausage-shaped' mass in the mid-abdomen. On ultrasound, it produces a pathognomonic 'target sign' or 'bullseye' appearance (concentric rings of bowel wall in cross-section)."
    },
    2593: {
        "topic": "Left Displaced Abomasum (LDA) - Right Flank Omentopexy",
        "Core_Anatomy": "Abomasum, greater omentum, and abdominal wall.",
        "Pathogenesis_Immediate": "Right flank omentopexy is the most widely utilized and reliable surgical correction for Left Displaced Abomasum (LDA) in dairy cattle.",
        "Pathogenesis_Deep": "In an LDA, the abomasum fills with gas and shifts under the rumen to the left side of the abdomen. The Right Flank Omentopexy is performed on the standing cow. The surgeon enters the right paralumbar fossa, reaches across the abdomen behind the rumen to deflate the abomasum with a needle, pulls the abomasum back to the right side, and sutures the greater omentum (near its attachment to the pylorus) to the right abdominal wall incision. This permanently anchors the abomasum on the right side, preventing recurrence.",
        "Why_Not": "Left flank omentopexy is possible but technically more difficult as the rumen is in the way. Ventral paramedian abomasopexy requires rolling the cow onto her back (general anaesthesia/heavy sedation), which is stressful. Right flank omentopexy is the standard standing procedure.",
        "Wow_Approach": "Because the omentum is sutured into the muscle closure, the cow heals with a permanent, strong fibrous adhesion holding the abomasum perfectly in place. 'Pexy' means surgical fixation."
    },
    2594: {
        "topic": "Gastroduodenostomy - Billroth I",
        "Core_Anatomy": "Stomach (pylorus) and duodenum.",
        "Pathogenesis_Immediate": "Gastroduodenostomy is the technical surgical term for the Billroth I procedure.",
        "Pathogenesis_Deep": "When a tumor (like adenocarcinoma) or a severe ulcer affects the pylorus of the stomach, the entire pyloric section must be resected. After resection, the remaining stomach must be reconnected to the intestinal tract. (1) Billroth I (Gastroduodenostomy): The stomach is anastomosed directly back to the duodenum (the normal anatomical route). (2) Billroth II (Gastrojejunostomy): If the duodenum cannot be used, the stomach is bypassed and anastomosed directly to the jejunum.",
        "Why_Not": "V-Y plasty is for skin reconstruction. Saculectomy is for anal glands. Billroth I is strictly a gastrointestinal resection-anastomosis procedure.",
        "Wow_Approach": "Because the stomach lumen is much larger than the duodenal lumen, a Billroth I requires specialized suturing techniques to match the diameters, often closing part of the stomach opening before joining the smaller duodenum to it."
    },
    2595: {
        "topic": "Reconstructive Surgery - V-Y Plasty",
        "Core_Anatomy": "Skin and subcutaneous tissue.",
        "Pathogenesis_Immediate": "V-Y plasty is a specific reconstructive skin flap technique used to relieve tension or correct defects like ectropion.",
        "Pathogenesis_Deep": "V-Y plasty is a type of local advancement flap. A V-shaped incision is made in the skin, the triangular flap is undermined and advanced to cover an adjacent defect or relieve a stricture, and the resulting gap is sutured closed in the shape of a Y. The advancement of the tissue adds length to the skin in that specific direction. It is famously used to correct cicatricial ectropion (outward rolling of the eyelid caused by scarring pulling the lid down).",
        "Why_Not": "Cheiloplasty is surgery of the lip. Billroth II is gastrointestinal surgery. V-Y plasty is a specific geometrical skin reconstruction technique.",
        "Wow_Approach": "To remember the effect of skin plasties: V-Y plasty lengthening relieves tension; Z-plasty changes the direction of a scar by 90 degrees to prevent contracture over joints."
    },
    2596: {
        "topic": "Anal Gland Disease - Saculectomy",
        "Core_Anatomy": "Anal sacs (paranal sinuses).",
        "Pathogenesis_Immediate": "The surgical removal of the anal glands is termed Anal Saculectomy.",
        "Pathogenesis_Deep": "Dogs have two anal sacs located at 4 o'clock and 8 o'clock around the anus, situated between the internal and external anal sphincter muscles. When these glands become chronically impacted, infected, or develop apocrine gland adenocarcinomas (a highly malignant, hypercalcemia-inducing tumor), surgical removal is required. The procedure (Anal Saculectomy) requires meticulous dissection to remove the entire secretory lining without damaging the surrounding anal sphincter muscles.",
        "Why_Not": "Cheiloplasty is lip surgery. The term for anal gland removal is unambiguously saculectomy.",
        "Wow_Approach": "The major risk of bilateral anal saculectomy is fecal incontinence. If the surgeon damages the external anal sphincter muscle or the caudal rectal nerve during the dissection, the dog will lose voluntary control of defecation."
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
print(f"Batch 4/5 DONE: Updated {updated} questions.")
