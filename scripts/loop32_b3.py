import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3640: {
        "topic": "Multiple Choice Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting a multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3641: {
        "topic": "Pericardiectomy Approach",
        "Core_Anatomy": "Thorax (4th or 5th Intercostal Space) and Pericardium.",
        "Pathogenesis_Immediate": "A Pericardiectomy or pericardiotomy is classically performed through a left lateral thoracotomy at the 4th or 5th intercostal space.",
        "Pathogenesis_Deep": "This procedure is the definitive treatment for chronic pericardial effusion or constrictive pericarditis (where a thickened, rigid pericardium prevents the heart from filling with blood during diastole, causing right-sided heart failure). A sub-total pericardiectomy involves removing the entire pericardial sac ventral to the phrenic nerves. This allows any fluid that forms to safely drain into the large pleural cavity where it is easily absorbed, completely curing the deadly cardiac tamponade.",
        "Why_Not": "A median sternotomy is also possible, but a left 5th intercostal thoracotomy provides excellent, direct access to the left auricle and the bulk of the pericardial sac.",
        "Wow_Approach": "Because you are opening the chest cavity, the animal MUST be on a ventilator before the pleura is breached, otherwise the lungs will instantly collapse."
    },
    3642: {
        "topic": "Vesicocele (Review)",
        "Core_Anatomy": "Urinary bladder.",
        "Pathogenesis_Immediate": "Vesicocele is the herniation of the bladder.",
        "Pathogenesis_Deep": "Reiterating that this is a surgical emergency, typically seen in perineal hernias.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3643: {
        "topic": "Traumatic Reticuloperitonitis (TRP)",
        "Core_Anatomy": "Bovine Reticulum and Peritoneum.",
        "Pathogenesis_Immediate": "Traumatic Reticuloperitonitis (TRP / 'Hardware Disease') is caused by the ingestion of metallic foreign bodies that pierce the reticulum.",
        "Pathogenesis_Deep": "Cattle are non-discriminatory eaters. If they eat a sharp wire or nail, it falls into the heavy reticulum (the 'honeycomb'). When the reticulum violently contracts to push cud up the esophagus, the sharp metal is driven straight through the anterior wall of the reticulum into the peritoneal cavity, causing focal peritonitis. If it travels a few inches further cranial, it pierces the diaphragm and the pericardial sac, causing fatal suppurative pericarditis.",
        "Why_Not": "Simple indigestion does not involve peritonitis. Left Displaced Abomasum (LDA) is a metabolic/mechanical gas displacement, not a penetrating injury.",
        "Wow_Approach": "The best preventative measure is to administer a heavy magnet orally via a balling gun. The magnet stays in the reticulum for the cow's entire life, safely catching and trapping any ingested metal before it can pierce the wall."
    },
    3644: {
        "topic": "Overlapping Sutures - Hernia (Review)",
        "Core_Anatomy": "Abdominal wall fascia.",
        "Pathogenesis_Immediate": "Overlapping sutures are indicated for Hernia closure.",
        "Pathogenesis_Deep": "Reiterating that the vest-over-pants pattern provides massive double-layer fascial strength.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3645: {
        "topic": "Gastric Dilatation-Volvulus (GDV)",
        "Core_Anatomy": "Canine Stomach.",
        "Pathogenesis_Immediate": "Deep-chested dogs are highly prone to Gastric Dilatation-Volvulus (GDV / Bloat).",
        "Pathogenesis_Deep": "GDV is a catastrophic surgical emergency in large, deep-chested breeds (Great Danes, Irish Setters, Standard Poodles). The stomach rapidly fills with gas/food and then violently twists on its mesenteric axis (usually 180 to 360 degrees clockwise). This instantly occludes both the cardiac sphincter (dog can't vomit) and pylorus (gas can't escape). Worse, the massively bloated, twisted stomach crushes the caudal vena cava, cutting off venous return to the heart, causing profound hypovolemic/distributive shock.",
        "Why_Not": "Intussusception is small intestine telescoping. Diaphragmatic hernia is a tear in the diaphragm.",
        "Wow_Approach": "The definitive preventative surgery is a prophylactic Gastropexy, where the right side of the stomach is permanently sutured to the right abdominal wall, making it physically impossible for the stomach to twist."
    },
    3646: {
        "topic": "Perianal Fistula (Anal Furunculosis)",
        "Core_Anatomy": "Canine Perianal skin.",
        "Pathogenesis_Immediate": "Perianal fistula (Anal Furunculosis) is overwhelmingly most common in German Shepherd Dogs.",
        "Pathogenesis_Deep": "Unlike a simple anal sac abscess, perianal fistulas are a chronic, progressive, immune-mediated disease characterized by deep, painful, malodorous ulcerating tracts surrounding the anus. German Shepherds are highly predisposed, likely due to a combination of genetic immune dysregulation and their broad, low-carriage tails creating a humid, anaerobic environment.",
        "Why_Not": "Pugs and Spitz breeds do not have the genetic predisposition or the tail carriage anatomy that drives this specific immune-mediated disease.",
        "Wow_Approach": "Surgery (amputation of the diseased tissue or tail) is NO LONGER the treatment of choice. The gold standard treatment is now immunosuppressive medical therapy using Cyclosporine or Tacrolimus."
    },
    3647: {
        "topic": "Nephrosplenic Entrapment (Left Dorsal Displacement)",
        "Core_Anatomy": "Equine Large Colon, Spleen, and Left Kidney.",
        "Pathogenesis_Immediate": "Nephrosplenic entrapment is a specific type of colic (Left Dorsal Displacement of the Large Colon) exclusively seen in Horses.",
        "Pathogenesis_Deep": "The horse's massive left large colon is unfixed and highly mobile. In this specific colic, the left colon migrates dorsally and hooks itself completely OVER the nephrosplenic ligament (a thick band of tissue running between the left kidney and the spleen). The colon becomes trapped, filling with gas and stretching the ligament, causing severe pain.",
        "Why_Not": "Cattle and dogs do not have the same massive, mobile, unfixed ascending colon anatomy as the horse.",
        "Wow_Approach": "This is one of the only forms of colic that can be treated non-surgically by giving an IV injection of Phenylephrine (to massively shrink the spleen) and then heavily lunging the horse, hoping the colon physically bounces off the ligament and falls back into place."
    },
    3648: {
        "topic": "Corkscrew Penis",
        "Core_Anatomy": "Bovine Penis (Corpus cavernosum).",
        "Pathogenesis_Immediate": "A Corkscrew penis is a common anatomical defect leading to breeding failure in the Bull.",
        "Pathogenesis_Deep": "Instead of extending straight forward during erection, the free end of the penis deviates ventrally and spirals like a corkscrew. This is usually due to a congenital disproportion in the lengths of the dorsal apical ligament and the corpus cavernosum, or secondary to trauma. The bull cannot achieve intromission.",
        "Why_Not": "Rams and Bucks have a urethral process, but the classic corkscrew deviation defect is a major economic problem in breeding Bulls.",
        "Wow_Approach": "Surgical correction involves a 'fascia lata graft' to physically tie down and straighten the dorsal apical ligament."
    },
    3649: {
        "topic": "Phallectomy",
        "Core_Anatomy": "Penis.",
        "Pathogenesis_Immediate": "Phallectomy is the surgical amputation of the Penis.",
        "Pathogenesis_Deep": "This salvage procedure is performed in cases of irreparable trauma, severe squamous cell carcinoma (e.g., in horses), or permanent paralysis of the retractor penis muscle leading to gangrenous paraphimosis. The penis is amputated, and a permanent new urethral opening (urethrostomy) is created to allow urination.",
        "Why_Not": "Orchiectomy is amputation of the testis (castration). Onychectomy is amputation of the digits (declawing).",
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
