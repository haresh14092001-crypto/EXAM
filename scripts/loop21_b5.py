import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2504: {
        "topic": "Positive Contrast Radiography - White/Opaque Appearance",
        "Core_Anatomy": "Hollow organ lumen.",
        "Pathogenesis_Immediate": "Positive contrast agents (Barium sulphate for GI; Iodinated solutions for urinary/vascular) appear White (radiopaque) on X-ray images.",
        "Pathogenesis_Deep": "Positive contrast media contain elements with high atomic numbers (Barium Z=56; Iodine Z=53). These high-Z elements efficiently absorb X-ray photons through photoelectric absorption, preventing X-rays from reaching the film/detector. On the developed image, areas filled with positive contrast appear bright WHITE (dense), providing striking contrast against the surrounding darker (radiolucent) soft tissue background.",
        "Why_Not": "Negative contrast media (air, CO2) are Radiolucent (appear BLACK on X-ray because X-rays pass through them freely). Positive = white; Negative = black.",
        "Wow_Approach": "Barium sulphate is NEVER used in cases of suspected GI perforation—if barium leaks into the peritoneal cavity, it causes a severe, fatal granulomatous peritonitis. Iodinated contrast (water-soluble, rapidly absorbed) must be substituted when perforation is suspected."
    },
    2506: {
        "topic": "Frostbite - Primary Healing",
        "Core_Anatomy": "Skin microcirculation and epidermal cells.",
        "Pathogenesis_Immediate": "Frostbite (freezing injury of tissues) is matched to Primary Healing in the context of superficial frostbite that resolves without significant tissue loss.",
        "Pathogenesis_Deep": "In superficial frostbite (Grade 1 and 2), ice crystals form in the extracellular fluid of the skin. The tissue thaws and the cells remain viable. The initial inflammatory response resolves, and the skin heals by primary intention—the wound edges come together naturally without significant tissue loss, producing minimal scarring. In severe frostbite (Grade 3-4), true full-thickness tissue necrosis occurs and healing is by secondary intention (granulation tissue formation).",
        "Why_Not": "Full-thickness burns and deep frostbite heal by secondary intention (granulation, contraction, and epithelialization). Primary healing specifically applies to clean, apposable wound edges.",
        "Wow_Approach": "The cardinal rule of frostbite management: 'Never rub frostbitten tissue.' Rubbing dislodges ice crystals, which act as razor blades within the cells, causing lethal mechanical cell membrane damage. Rapid rewarming in warm water (40-42°C) is the only correct treatment."
    },
    2509: {
        "topic": "Surgical Wound Classification - Immature Abscess & Fistula",
        "Core_Anatomy": "Subcutaneous and deep tissue planes.",
        "Pathogenesis_Immediate": "An immature abscess requires incision and drainage only when it has fully developed (pointing/fluctuating), not while still indurated. A fistula is an abnormal tract connecting two epithelial surfaces.",
        "Pathogenesis_Deep": "(1) Abscess: A localized collection of pus surrounded by a pyogenic membrane. An IMMATURE abscess is still indurated (firm, not yet fluctuant)—incising prematurely releases cellulitis, not pus. Maturation (softening/fluctuance) must be waited for, or hot fomentation applied to accelerate it. (2) Fistula: A chronic, epithelialized abnormal communication between two epithelial-lined surfaces (e.g., teat fistula connecting the teat lumen to the skin, or oronasal fistula in cleft palate patients). Fistulas require surgical excision of the entire epithelialized tract.",
        "Why_Not": "A sinus is a blind-ending tract (one opening). A fistula has TWO openings. This distinction is critical for surgical planning.",
        "Wow_Approach": "Teat fistulas in dairy cows are a specific surgical challenge—the teat's thin skin and mobile anatomy make fistula repair technically demanding. A Kerf technique (layered elliptical excision and closure) with bovine urethral catheter stenting is the preferred repair method."
    },
    2511: {
        "topic": "Schiotz Tonometry - Intraocular Pressure",
        "Core_Anatomy": "Aqueous humor and cornea.",
        "Pathogenesis_Immediate": "Schiotz tonometry is used to measure Intraocular Pressure (IOP).",
        "Pathogenesis_Deep": "The Schiotz (indentation) tonometer measures IOP by measuring how deeply a standardized weighted plunger indents the anaesthetised cornea. High IOP (glaucoma) resists indentation → small scale reading → high IOP. Low IOP (phthisis bulbi/hypotony) allows deep indentation → large scale reading → low IOP. In veterinary medicine, IOP is expressed in mmHg. Normal canine IOP = 15-25 mmHg; values above 30 mmHg indicate glaucoma requiring urgent treatment.",
        "Why_Not": "Ophthalmoscopy examines the fundus and retinal vessels. Slit-lamp biomicroscopy examines anterior segment. Only tonometry (Schiotz or applanation) measures IOP.",
        "Wow_Approach": "Schiotz tonometry requires topical anaesthetic (Proxymetacaine 0.5%) applied to the cornea before use. Failure to anaesthetize the cornea causes blepharospasm that elevates IOP artificially, producing false-positive glaucoma readings."
    },
    2519: {
        "topic": "Surgery MCQ Section Header",
        "Core_Anatomy": "Veterinary surgery and radiology.",
        "Pathogenesis_Immediate": "This MCQ section tests surgical decision-making, indications for procedures, suture technique selection, and radiographic principles.",
        "Pathogenesis_Deep": "Key surgical MCQ areas: indications for laparotomy, correct suture patterns for specific anatomical locations, anaesthetic drug selection, and dosing safety principles.",
        "Why_Not": "Always select the most specific surgical technique that matches the anatomical location and tissue being repaired.",
        "Wow_Approach": "For any suture pattern MCQ: always consider (1) whether the organ is under peristaltic tension (needs inverting pattern like Lembert/Cushing), (2) whether it's a skin wound (needs everting pattern like mattress sutures), or (3) whether it's fascia (needs simple interrupted)."
    },
    2520: {
        "topic": "Laparotomy - Indications",
        "Core_Anatomy": "Abdominal cavity.",
        "Pathogenesis_Immediate": "Laparotomy (surgical opening of the abdominal cavity) is indicated for ALL of the listed conditions: intestinal obstruction, diaphragmatic hernia, and Caesarean section.",
        "Pathogenesis_Deep": "(1) Intestinal obstruction: Emergency laparotomy to relieve mechanical blockage (intussusception, volvulus, foreign body) and resect necrotic bowel. (2) Diaphragmatic hernia repair: Abdominal approach to reduce herniated organs from the thoracic cavity and repair the diaphragmatic defect. (3) Caesarean section (C-section): Midline or para-inguinal laparotomy to deliver a fetus that cannot be delivered by the vaginal route. All three are definitive indications for laparotomy.",
        "Why_Not": "Minimally invasive laparoscopy can be used for diagnostics and some procedures, but the listed conditions typically require full laparotomy for adequate access.",
        "Wow_Approach": "In cattle, the RIGHT paralumbar fossa standing laparotomy under local anaesthetic is preferred for C-sections, LDA (Left Displaced Abomasum) correction, and ruminotomy—allowing the conscious, standing cow to bear weight and maintain rumen motility throughout surgery."
    },
    2521: {
        "topic": "Oesophageal Diverticulum - Surgical Treatment",
        "Core_Anatomy": "Oesophageal wall (muscularis layer).",
        "Pathogenesis_Immediate": "A diverticulum of the oesophagus is definitively treated Surgically (diverticulectomy).",
        "Pathogenesis_Deep": "An oesophageal diverticulum is a sac-like outpouching of the oesophageal wall. In horses, the most common presentation is a cervical oesophageal diverticulum caused by pressure from an obstruction (choke). The diverticulum progressively fills with food material, causing regurgitation, dysphagia, and aspiration pneumonia risk. Manual reduction and probing are temporizing measures only. Definitive treatment is surgical diverticulectomy—excision of the sac with layered closure of the oesophageal wall.",
        "Why_Not": "Manual reduction may temporarily reduce the diverticulum but does not address the underlying wall weakness—it will inevitably recur. Probing risks perforation of the already weakened oesophageal wall.",
        "Wow_Approach": "Post-oesophageal surgery feeding management is critical: the animal must be kept on gruel/slurry diet for 14-21 days to allow the oesophageal repair to heal without being stretched by solid food boluses."
    },
    2522: {
        "topic": "Schmieden Suture - Intestinal Anastomosis",
        "Core_Anatomy": "Intestinal wall (full-thickness continuous suture).",
        "Pathogenesis_Immediate": "The Schmieden suture technique is used for Intestinal anastomosis.",
        "Pathogenesis_Deep": "The Schmieden suture is a continuous through-and-through suture pattern used to complete intestinal anastomosis. It is typically used for the final (mucosal) layer in a two-layer intestinal anastomosis. The needle enters from the mucosal surface of one intestinal cut end, exits through the serosa, then re-enters the other intestinal end from the serosal surface and exits through the mucosa—creating a full-thickness, interlocking pattern. This creates a strong, leak-proof anastomosis. The second layer (Lembert pattern) then inverts the Schmieden layer to provide serosalization.",
        "Why_Not": "Lembert pattern is used for oesophageal/gastric/bladder inverting layer sutures. Simple interrupted is for skin. Mattress sutures are for skin tension. The Schmieden is specifically for the inner intestinal anastomosis layer.",
        "Wow_Approach": "After intestinal anastomosis, ALWAYS check: (1) the lumen is not narrowed (use one finger through the anastomosis to verify), (2) the blood supply to both ends is intact (pink, not cyanotic), (3) the serosa-to-serosa contact is complete (prevents peritoneal leakage). The '3-check rule.'"
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

# Final validation
with open(db_path, "r", encoding="utf-8") as f:
    c2 = f.read()
d2 = json.loads(re.sub(r'^.*?const examData = ', '', c2, flags=re.DOTALL).rsplit(';',1)[0].strip())
empty2 = [x for x in d2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
