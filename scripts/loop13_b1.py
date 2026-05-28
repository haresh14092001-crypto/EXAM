import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1465: {
        "topic": "Pelvic Inlet Geometry - Species Differences",
        "Core_Anatomy": "Maternal bony pelvis (ilium, ischium, pubis).",
        "Pathogenesis_Immediate": "The pelvic inlet is NOT oval-shaped in the Mare (it is nearly circular).",
        "Pathogenesis_Deep": "The shape of the pelvic inlet (the entrance to the birth canal) dictates the mechanics of parturition. In the cow and ewe, the inlet is elliptical (oval), meaning it is taller (vertical diameter) than it is wide (transverse diameter). In the mare, the pelvic inlet is nearly perfectly circular (round) and massive. This circular shape, combined with the mare's extremely powerful abdominal contractions, allows for the explosive, rapid delivery of the foal in Stage 2 labor.",
        "Why_Not": "Because the cow's pelvis is oval, the calf must enter it in a very specific dorso-sacral orientation to fit through the narrow transverse diameter. The mare's circular pelvis is much more forgiving of minor positional deviations.",
        "Wow_Approach": "In the sow, the pelvic axis is almost a straight line, which perfectly accommodates the rapid, sequential expulsion of the litter."
    },
    1466: {
        "topic": "Premature Viability - Bovine Gestation Limits",
        "Core_Anatomy": "Fetal lungs (surfactant) and gravid uterus.",
        "Pathogenesis_Immediate": "Premature birth of a potentially viable calf can occur in the cow between days 260 and 270.",
        "Pathogenesis_Deep": "Normal bovine gestation is 280-285 days. A calf born before 260 days is considered an abortion because the fetal type II pneumocytes have not produced sufficient surfactant. The lungs cannot expand, leading to fatal respiratory distress syndrome (hyaline membrane disease). Between days 260-270, the calf is premature but potentially viable with intensive neonatal care. A calf born between 270 and 280 days is considered 'early term' and is usually fully viable.",
        "Why_Not": "Births before 260 days result in absolute non-viability. 270-280 is essentially term in some early-maturing breeds like Jerseys.",
        "Wow_Approach": "If parturition must be induced prematurely to save the cow (e.g., due to severe hydrops), always administer Dexamethasone at least 24-48 hours prior to delivery to artificially stimulate fetal lung surfactant production."
    },
    1467: {
        "topic": "Testicular Orientation - Horizontal Axis in the Stallion",
        "Core_Anatomy": "Scrotum, spermatic cord, and testicular long axis.",
        "Pathogenesis_Immediate": "The long axis of the testes is nearly horizontal in the Stallion.",
        "Pathogenesis_Deep": "Testicular orientation varies drastically by species, dictating the method of clinical palpation and castration: (1) Stallion: Horizontal. The epididymis lies along the dorsal border. (2) Bull and Ram: Vertical. The epididymis runs down the medial/caudal border, with the cauda firmly at the ventral pole. (3) Boar and Dog: Oblique (tilted upwards and backwards toward the anus).",
        "Why_Not": "Attempting to castrate a stallion using the same scrotal incision orientation as a bull can result in severe hemorrhage and inadequate drainage.",
        "Wow_Approach": "When performing a Breeding Soundness Exam on a stallion, always palpate the tail of the epididymis at the caudal pole of the horizontal testis to check for sperm granulomas or epididymitis."
    },
    1468: {
        "topic": "Testicular Orientation - Oblique Axis in the Boar",
        "Core_Anatomy": "Perineal scrotum and testicular long axis.",
        "Pathogenesis_Immediate": "In contrast to the horizontal testes of the stallion and the vertical testes of the bull, the long axis of the testes in the Boar is Oblique.",
        "Pathogenesis_Deep": "The boar's scrotum is not pendulous; it is situated high up in the perineal region, just below the anus. The testicles are massive and tilted obliquely upwards and backwards. This tight perineal location protects the testicles from mechanical trauma during fighting but limits the efficiency of counter-current heat exchange compared to the pendulous scrotum of the bull or ram.",
        "Why_Not": "Heat stress in boars is a major cause of summer infertility precisely because their non-pendulous, oblique scrotal anatomy is less efficient at dissipating body heat.",
        "Wow_Approach": "Boar castration requires a perineal approach, incising directly over the testicles below the anus, rather than a ventral scrotal approach."
    },
    1469: {
        "topic": "Ram Penile Anatomy - The Urethral Process",
        "Core_Anatomy": "Glans penis and distal urethra.",
        "Pathogenesis_Immediate": "The penis of the ram (and buck) is distinctly characterized by a long, free-ending Urethral Process (processus urethralis).",
        "Pathogenesis_Deep": "The ram and buck have a fibroelastic penis with a sigmoid flexure. At the glans, the urethra extends 2 to 4 cm beyond the tip of the penis as a narrow, freely mobile tube. During ejaculation, this vermiform (worm-like) process whips in a rapid circular motion, spraying semen in a 360-degree arc completely over the external os of the ewe's cervix, maximizing fertilization chances.",
        "Why_Not": "Bulls have a very short urethral process that does not extend freely. Boars have a corkscrew tip. Stallions have a vascular bell-shaped glans.",
        "Wow_Approach": "The urethral process is the absolute most common site for urolith (bladder stone) impaction in small ruminants. In an emergency block, the process can simply be amputated with scissors to restore urine flow without affecting the ram's fertility."
    },
    1470: {
        "topic": "Semen Concentration - Bull Averages",
        "Core_Anatomy": "Cauda epididymis and ejaculate volume.",
        "Pathogenesis_Immediate": "The average spermatozoan concentration in a normal bull ejaculate is approximately 1200 million (1.2 billion) sperm per milliliter.",
        "Pathogenesis_Deep": "Bulls produce a relatively small volume of semen (5-8 ml) but at a highly concentrated density (1-2 billion sperm/ml). In contrast, the boar produces a massive volume (200-300 ml) at a much lower concentration (200-300 million/ml). The stallion produces moderate volume (50-100 ml) at low-to-moderate concentration (150-300 million/ml).",
        "Why_Not": "120 million/ml is characteristic of a stallion or boar. 12 million/ml is severe oligozoospermia in any species.",
        "Wow_Approach": "Because bull semen is so highly concentrated, a single 5 ml ejaculate (containing 6 billion sperm) can be extended and packaged into hundreds of 0.25 ml French straws (each requiring only 15-20 million viable sperm for AI)."
    },
    1471: {
        "topic": "Cryptorchidism Terminology - The 'Ridgling'",
        "Core_Anatomy": "Inguinal canal, scrotum, and retained testis.",
        "Pathogenesis_Immediate": "A cryptorchid animal is colloquially and historically spoken of as a 'Ridgling' (or 'Rig') specifically in the Stallion/Horse.",
        "Pathogenesis_Deep": "In equine practice, a stallion with one or both testes retained in the abdomen or inguinal canal is called a 'rig'. Because testicular descent in the horse occurs very late in gestation (or even shortly after birth), the inguinal rings remain relatively large. Rigs often exhibit unpredictable, aggressive, and dangerous stallion-like behavior despite appearing to be geldings (if one testicle was previously removed and the retained one ignored).",
        "Why_Not": "In cattle, pigs, and sheep, the term cryptorchid is used formally. 'Ridgling' is deeply rooted in equine equestrian terminology.",
        "Wow_Approach": "Never castrate just the descended testicle in a unilateral cryptorchid horse. Doing so removes the easily accessible testis but leaves the abdominal one, creating a 'false gelding' that cannot be easily diagnosed without hormonal assays (Anti-Mullerian Hormone or Estrone Sulfate)."
    },
    1472: {
        "topic": "Endocrinology Matching - Leydig Cells",
        "Core_Anatomy": "Testicular interstitium and LH receptors.",
        "Pathogenesis_Immediate": "Leydig cells (interstitial cells) are the primary endocrine cells responsible for producing Testosterone in the male.",
        "Pathogenesis_Deep": "Leydig cells reside in the interstitial connective tissue OUTSIDE the seminiferous tubules. They are rich in smooth endoplasmic reticulum and lipid droplets (cholesterol). When Luteinizing Hormone (LH) from the anterior pituitary binds to Leydig cell receptors, it activates adenylate cyclase, converting cholesterol into testosterone. This testosterone then diffuses into the adjacent tubules to drive spermatogenesis.",
        "Why_Not": "Sertoli cells respond to FSH and produce inhibin/ABP. Spermatocytes are the germ cells undergoing meiosis. Myoid cells contract the tubule.",
        "Wow_Approach": "Because Leydig cells are highly resistant to heat, a bilaterally cryptorchid male (with core-temperature testicles) is completely sterile (azoospermic) but still produces normal levels of testosterone, retaining all secondary male sex characteristics and libido."
    },
    1473: {
        "topic": "Canine Semen Fractions - Prostatic Fluid",
        "Core_Anatomy": "Canine prostate gland and pelvic urethra.",
        "Pathogenesis_Immediate": "The third fraction of dog semen is produced exclusively by the Prostate gland.",
        "Pathogenesis_Deep": "The canine ejaculate is collected in three distinct fractions: (1) First fraction (pre-sperm): A small volume (0.5-2 ml) of clear fluid from the prostate, cleaning the urethra. (2) Second fraction (sperm-rich): A milky, highly concentrated fluid (1-3 ml) originating from the epididymis. (3) Third fraction (prostatic fluid): A massive volume (up to 20-30 ml) of clear fluid forcefully ejected from the prostate during the prolonged 'tie' (copulatory lock). This final fraction pushes the sperm-rich fraction deep into the bitch's uterus.",
        "Why_Not": "The dog lacks seminal vesicles and bulbourethral glands entirely. The prostate is the ONLY accessory sex gland in the canine.",
        "Wow_Approach": "During manual semen collection in the dog, the collector usually stops collecting once the milky second fraction turns clear, as adding too much of the third prostatic fraction dilutes the semen unnecessarily for artificial insemination."
    },
    1474: {
        "topic": "Sertoli Cells - Sustentacular Synonym (Repeated MCQ)",
        "Core_Anatomy": "Seminiferous tubule epithelium.",
        "Pathogenesis_Immediate": "The sustentacular cell is otherwise commonly called the Sertoli cell.",
        "Pathogenesis_Deep": "Sertoli cells form the absolute structural foundation of the seminiferous tubule. They are connected to each other by tight junctions (zonula occludens) near the basement membrane, forming the impenetrable blood-testis barrier. This barrier prevents the male's own immune system (lymphocytes) from recognizing and destroying the haploid sperm cells, which are genetically unique and would otherwise trigger an autoimmune attack.",
        "Why_Not": "Leydig cells are interstitial. Spermatogonia are germ cells.",
        "Wow_Approach": "Damage to the Sertoli cell tight junctions (e.g., from severe trauma or biopsy) leads to the production of anti-sperm antibodies, causing autoimmune sperm agglutination and permanent sterility."
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
