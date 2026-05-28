import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    4000: {
        "topic": "Intestinal Viability Criteria",
        "Core_Anatomy": "Intestinal Wall and Microvasculature.",
        "Pathogenesis_Immediate": "The three prime clinical indicators used to determine intestinal viability before enterectomy are color, peristalsis, and bleeding from the cut edge.",
        "Pathogenesis_Deep": "When a loop of bowel has been incarcerated or twisted, the surgeon must decide whether to resect it or save it. Healthy, viable intestine is warm, pink/red (not black/gray), actively contracts (peristalsis) when gently pinched, and demonstrates active, bright-red arterial bleeding when a small incision is made in the antimesenteric border.",
        "Why_Not": "Presence of adhesions only indicates past inflammation, not current tissue viability.",
        "Wow_Approach": "If viability is borderline, the surgeon can wrap the bowel in a warm, saline-soaked laparotomy sponge for 5 minutes and re-evaluate. If the color improves to pink and motility returns, the segment can be safely preserved."
    },
    4001: {
        "topic": "Strabismus",
        "Core_Anatomy": "Extraocular muscles (CN III, IV, VI).",
        "Pathogenesis_Immediate": "The abnormal deviation of the eyeball relative to the normal visual axis is called Strabismus.",
        "Pathogenesis_Deep": "It is caused by an imbalance in the tone of the extraocular muscles, which can be congenital (e.g., convergent strabismus or 'cross-eyed' in Siamese cats) or acquired due to cranial nerve damage (oculomotor, trochlear, or abducens nerves).",
        "Why_Not": "Coloboma is a congenital cleft in the iris/eyelid. Chalazion is a blockage of the meibomian gland.",
        "Wow_Approach": "N/A"
    },
    4002: {
        "topic": "Typhlectomy (Review)",
        "Core_Anatomy": "Caecum.",
        "Pathogenesis_Immediate": "Surgical resection of the caecum is termed Typhlectomy.",
        "Pathogenesis_Deep": "Reiterating that this involves amputating the caecum close to the ileocecocal junction.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4003: {
        "topic": "Sertoli Cell Tumor - Feminizing Syndrome",
        "Core_Anatomy": "Testis (Sertoli cells).",
        "Pathogenesis_Immediate": "Sertoli Cell Tumor in dogs classically causes Male Feminizing Syndrome due to hyperestrogenism.",
        "Pathogenesis_Deep": "Sertoli cells inside the testicle naturally support sperm production. When they undergo neoplastic transformation (highly common in cryptorchid/retained testicles), they secrete massive amounts of estrogen. This extreme estrogen level feminizes the male dog, presenting as bilateral symmetrical alopecia, gynecomastia (enlarged nipples/mammary glands), penile atrophy, attraction of other male dogs, and life-threatening squamous metaplasia of the prostate and bone marrow suppression.",
        "Why_Not": "Seminomas and Leydig (interstitial) cell tumors are typically benign and do not produce massive amounts of estrogen.",
        "Wow_Approach": "The definitive, curative treatment is bilateral castration, which causes the estrogen levels to drop, reversing the skin changes over several months."
    },
    4004: {
        "topic": "Struvite Urolithiasis - Alkaline pH",
        "Core_Anatomy": "Urinary Tract.",
        "Pathogenesis_Immediate": "Struvite crystals (Magnesium Ammonium Phosphate) are highly associated with Alkaline (less acidic) urine pH.",
        "Pathogenesis_Deep": "In dogs, struvite urolithiasis is almost always secondary to a urinary tract infection by urease-producing bacteria (like Staphylococcus or Proteus). These bacteria split urea in the urine into ammonia, raising the pH to >7.5. This alkaline environment drastically reduces the solubility of magnesium, ammonium, and phosphate ions, causing them to rapidly precipitate and form large, smooth, radiopaque stones.",
        "Why_Not": "Calcium oxalate and silica stones form in acidic urine and are highly resistant to dissolution.",
        "Wow_Approach": "Unlike calcium stones, sterile struvite stones can be completely dissolved medically without surgery by feeding a specialized urine-acidifying, low-protein, low-mineral diet."
    },
    4005: {
        "topic": "Ovariohysterectomy Definition",
        "Core_Anatomy": "Ovaries and Uterus.",
        "Pathogenesis_Immediate": "Ovariohysterectomy is the complete surgical removal of both the ovaries and the uterus.",
        "Pathogenesis_Deep": "It is the standard sterilization surgery performed in female dogs and cats to prevent pregnancy, eliminate estrus, and prevent pyometra or mammary neoplasia.",
        "Why_Not": "Ovariectomy is the removal of the ovaries only. Ovariotomy is an incision into the ovary.",
        "Wow_Approach": "N/A"
    },
    4006: {
        "topic": "Volvulus (Review)",
        "Core_Anatomy": "Gastrointestinal tract.",
        "Pathogenesis_Immediate": "Twisting of the intestine along its mesenteric axis is called a Volvulus.",
        "Pathogenesis_Deep": "Reiterating that this causes double-lumen occlusion and rapid intestinal wall necrosis.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4007: {
        "topic": "Entropion",
        "Core_Anatomy": "Eyelid margin.",
        "Pathogenesis_Immediate": "The inward rolling or inversion of the eyelid margin is called Entropion.",
        "Pathogenesis_Deep": "This causes the eyelashes and outer hair of the eyelid to constantly rub directly against the cornea. The constant abrasion leads to intense pain, blepharospasm, epiphora, corneal ulceration, and eventual pigmentation/blindness if not corrected.",
        "Why_Not": "Ectropion is the outward rolling/eversion of the eyelid margin (drooping eyelid). Dystrichiasis is lashes emerging from abnormal sites.",
        "Wow_Approach": "N/A"
    },
    4008: {
        "topic": "Canine Urethral Calculi Site (Review)",
        "Core_Anatomy": "Os penis.",
        "Pathogenesis_Immediate": "The most common site of obstructive urolithiasis in dogs is just caudal to the os penis.",
        "Pathogenesis_Deep": "Reiterating that this is the point where the distensible urethra enters the rigid bony groove of the os penis.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    4009: {
        "topic": "Tonometry - Glaucoma Diagnosis",
        "Core_Anatomy": "Eye (Anterior chamber).",
        "Pathogenesis_Immediate": "Increased intraocular pressure (IOP), which is diagnostic for Glaucoma, is best measured using Tonometry.",
        "Pathogenesis_Deep": "Glaucoma is characterized by impaired drainage of aqueous humor, leading to elevated IOP (>25 mmHg in dogs). Chronic elevation compresses the retina and optic nerve, leading to rapid, irreversible blindness. A Tonometer (such as the Tono-Pen or TonoVet rebound tonometer) measures the force required to indent or flatten the cornea, giving an accurate IOP reading.",
        "Why_Not": "The cotton ball test is a simple test of visual tracking (vision), not pressure.",
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
print(f"Batch 4/5 DONE: Updated {updated} questions.")
