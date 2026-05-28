import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1336: {
        "topic": "Pharmacology - Standard Dosages MCQ",
        "Core_Anatomy": "Systemic circulation.",
        "Pathogenesis_Immediate": "Standard high-dose options (e.g., 1.0 to 1.25 mg/kg) often represent macro-dosing for antibiotics or less potent sedatives.",
        "Pathogenesis_Deep": "In veterinary board exams, recognizing the magnitude of the dosage is a fast way to eliminate distractors. Highly potent hormones (prostaglandins, GnRH) are dosed in micrograms. Sedatives (xylazine, acepromazine) are dosed in fractions of a milligram (0.05 - 0.25 mg/kg). Antibiotics and induction agents (ketamine, propofol) are dosed in full milligrams (1.0 - 5.0+ mg/kg).",
        "Why_Not": "Administering a macro-dose (1 mg/kg) of a micro-dosed drug (like cloprostenol) will cause massive, potentially fatal smooth muscle spasms.",
        "Wow_Approach": "Always double-check the drug class before selecting a dosage option to prevent lethal iatrogenic errors."
    },
    1337: {
        "topic": "Sertoli Cells - The Nursing Cells (Repeated MCQ)",
        "Core_Anatomy": "Seminiferous tubules and germ cells.",
        "Pathogenesis_Immediate": "The 'nursing cells' of the seminiferous tubules are the Sertoli cells (Sustentacular cells).",
        "Pathogenesis_Deep": "Sertoli cells provide critical structural, nutritional, and endocrine support to developing germ cells. They span from the basement membrane to the lumen, enveloping the spermatogonia, spermatocytes, and spermatids. They secrete fluid to transport spermatozoa to the rete testis, synthesize androgen-binding protein (ABP) to concentrate testosterone locally, and form the blood-testis barrier.",
        "Why_Not": "Leydig cells secrete testosterone. Spermatogonia are the stem cells being nursed. Myoid cells contract the tubule.",
        "Wow_Approach": "Because Sertoli cells do not replicate after puberty, a bull's maximum sperm-producing capacity is permanently fixed early in life."
    },
    1338: {
        "topic": "Scrotal Circumference - Adult Bull Baseline (Repeated MCQ)",
        "Core_Anatomy": "Testicular parenchyma and scrotum.",
        "Pathogenesis_Immediate": "The normal, highly acceptable scrotal circumference in a mature adult breeding bull (e.g., >2 years old) is approximately 38 cm (standardly >34 cm).",
        "Pathogenesis_Deep": "Scrotal circumference (SC) is a highly heritable trait directly correlated with daily sperm production (DSP) and the age of puberty in the bull's female offspring. A mature Bos taurus bull should have an SC >34 cm, with 38-40 cm being excellent. An SC <30 cm in a mature bull is grounds for failure due to testicular hypoplasia.",
        "Why_Not": "25 cm is diagnostic of severe hypoplasia in adults. 55 cm indicates severe pathology (orchitis, hydrocele, or massive tumors).",
        "Wow_Approach": "Use a specialized scrotal tape. Pull it snugly around the widest part of the testicles, ensuring both testicles are pushed fully down into the bottom of the scrotum for an accurate reading."
    },
    1339: {
        "topic": "Accessory Sex Gland Pathology - MCQ Options",
        "Core_Anatomy": "Male accessory sex glands.",
        "Pathogenesis_Immediate": "The inflammatory diseases of the accessory glands include Seminal Vesiculitis, Prostatitis, Ampullitis, and Epididymitis.",
        "Pathogenesis_Deep": "Seminal vesiculitis is the most common accessory gland infection in the bull (often caused by Brucella abortus or Trueperella pyogenes). It causes the gland to become enlarged, firm, and painful on rectal palpation, and pollutes the semen with massive numbers of neutrophils. Prostatitis is the most common in the dog.",
        "Why_Not": "These conditions are highly species-specific due to anatomical differences (e.g., dogs cannot get seminal vesiculitis because they lack seminal vesicles).",
        "Wow_Approach": "In bulls, seminal vesiculitis is a major reason for failing a Breeding Soundness Exam (BSE). The presence of pus in the ejaculate destroys sperm viability upon freezing."
    },
    1340: {
        "topic": "Persistent Frenulum - Ventral Deviation (Repeated MCQ)",
        "Core_Anatomy": "Penile raphe and ventral glans.",
        "Pathogenesis_Immediate": "A persistent penile frenulum in a bull will specifically result in a Ventral deviation of the penis.",
        "Pathogenesis_Deep": "The frenulum is a band of connective tissue joining the prepuce to the ventral glans. Failure to rupture before puberty tethers the penis downward during erection, creating a 'rainbow' curve that prevents intromission.",
        "Why_Not": "Lateral or spiral deviations are caused by the slipping of the apical ligament. A persistent frenulum is strictly a ventral tether.",
        "Wow_Approach": "Surgical correction involves simple clamping, ligation, and transection of the band under local anesthesia, restoring immediate breeding function."
    },
    1341: {
        "topic": "Artificial Insemination Timing - Bovine (Repeated MCQ)",
        "Core_Anatomy": "Female reproductive tract, sperm capacitation, and ovulation.",
        "Pathogenesis_Immediate": "The optimum time for Artificial Insemination (A.I.) in the cow is Mid to Late Estrus.",
        "Pathogenesis_Deep": "This timing aligns with the 'AM/PM Rule'. Because the cow uniquely ovulates 10-14 hours AFTER the end of behavioral estrus, inseminating during mid-to-late estrus ensures that sperm have sufficient time (6-8 hours) to undergo capacitation in the oviduct, making them fully fertile exactly when the oocyte arrives.",
        "Why_Not": "Inseminating before estrus provides aged, dead sperm. Inseminating after ovulation means the oocyte ages rapidly before the new sperm can capacitate.",
        "Wow_Approach": "To maximize conception: inseminate 12 hours after the first observed standing heat."
    },
    1342: {
        "topic": "Knobbed Sperm Defect - Primary Acrosomal Abnormality",
        "Core_Anatomy": "Sperm head acrosome and anterior nuclear pole.",
        "Pathogenesis_Immediate": "The 'Knobbed sperm defect' is a primary morphological abnormality of the sperm head, characterized by a thickened, folded, or cystic acrosomal apex.",
        "Pathogenesis_Deep": "The knobbed defect originates during the Golgi/Cap phases of spermiogenesis in the testis. The acrosomal vesicle fails to spread evenly over the nucleus, instead folding back on itself to form a cyst or 'knob' at the apex. This structurally prevents the sperm from binding to the zona pellucida, causing complete fertilization failure.",
        "Why_Not": "Diadem defect involves nuclear membrane invaginations. Dag defect involves tail coiling. Corkscrew defect involves the midpiece. The Knobbed defect is strictly an apical acrosomal head defect.",
        "Wow_Approach": "Because this is a primary defect of testicular origin, finding >15-20% knobbed sperm indicates a severe disturbance in spermatogenesis (often genetic or due to acute heat stress) and warrants a poor prognosis for fertility."
    },
    1343: {
        "topic": "Sustentacular Cells - Spermatid Nourishment (Repeated MCQ)",
        "Core_Anatomy": "Seminiferous tubules and germ cells.",
        "Pathogenesis_Immediate": "In the seminiferous tubule, developing sperms are nourished by the Sustentacular cells (Sertoli cells).",
        "Pathogenesis_Deep": "Sustentacular cells act as the physiological 'nurse' cells. They regulate the precise microenvironment required for meiosis and spermiogenesis, shielding the germ cells behind the blood-testis barrier and providing metabolic substrates.",
        "Why_Not": "Leydig cells reside outside the tubules and synthesize testosterone. The germinal epithelium refers to the dividing germ cells themselves.",
        "Wow_Approach": "Sustentacular cell function is directly stimulated by FSH from the anterior pituitary."
    },
    1344: {
        "topic": "Testicular Insulation - Inducing Degeneration (Repeated MCQ)",
        "Core_Anatomy": "Scrotal thermoregulation and seminiferous epithelium.",
        "Pathogenesis_Immediate": "Insulation of the testicles for a longer duration artificially raises the core scrotal temperature, rapidly inducing Testicular Degeneration.",
        "Pathogenesis_Deep": "Mammalian spermatogenesis requires a temperature 2-4°C below core body temperature. Artificial insulation (or severe fever) causes rapid heat stress, triggering massive apoptosis of primary spermatocytes and early spermatids. This manifests as severe teratozoospermia (high primary defects) and oligozoospermia.",
        "Why_Not": "Testicular hypoplasia is a congenital underdevelopment, not an acquired heat-induced degeneration. Hyperplasia (tumor formation) requires chronic retention (cryptorchidism), not acute insulation.",
        "Wow_Approach": "To differentiate acquired degeneration from congenital hypoplasia: check breeding records. A previously fertile bull that becomes infertile has acquired degeneration."
    },
    1345: {
        "topic": "Semen Thawing - Optimal Protocol (Repeated MCQ)",
        "Core_Anatomy": "Sperm membrane lipids and water bath.",
        "Pathogenesis_Immediate": "The standard, optimal protocol for thawing frozen bovine semen is immersing the straw in a water bath at 37°C for 30 seconds.",
        "Pathogenesis_Deep": "Rapid thawing at 37°C ensures the sperm rapidly transit through the critical recrystallization temperature zone (-60°C to 0°C), preventing the formation of lethal intracellular ice crystals that shear the plasma membrane.",
        "Why_Not": "Thawing at 25°C is too slow, allowing ice crystals to coalesce and lyse the cell. Thawing above 40°C denatures structural proteins.",
        "Wow_Approach": "After 30 seconds at 37°C, the straw must be meticulously dried, as any contact with water is instantly spermicidal due to severe osmotic shock."
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
