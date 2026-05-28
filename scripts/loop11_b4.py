import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1288: {
        "topic": "VGO-511 Andrology & Reproductive Techniques",
        "Core_Anatomy": "Male reproductive system and artificial insemination.",
        "Pathogenesis_Immediate": "The objective section of VGO-511 systematically evaluates clinical male reproductive pathology, semen handling, and nerve block techniques.",
        "Pathogenesis_Deep": "This testing framework validates theoretical competency before field practice. It encompasses: diagnosing penile deviations (phallocampsis), administering pudendal nerve blocks for penile exteriorization, and evaluating the endocrinology of spermatogenesis.",
        "Why_Not": "General obstetrics (dystocia) is assessed in VGO-512, whereas VGO-511 is strictly focused on male fertility and reproductive biotechnology.",
        "Wow_Approach": "Success in this module requires linking anatomical knowledge (e.g., retractor penis muscle) directly to clinical pharmacology (e.g., pudendal nerve block to relax it)."
    },
    1289: {
        "topic": "Cryptorchidism Fertility - Unilateral vs Bilateral",
        "Core_Anatomy": "Testicular parenchyma, scrotum, and abdominal cavity.",
        "Pathogenesis_Immediate": "The statement 'All types of cryptorchids are sterile' is FALSE.",
        "Pathogenesis_Deep": "Cryptorchidism can be unilateral (one testis retained, one in the scrotum) or bilateral (both retained). (1) In a bilateral cryptorchid, both testes are exposed to core body temperature, which destroys the germinal epithelium, resulting in complete azoospermia and sterility. (2) In a unilateral cryptorchid (monorchid), the single descended testis functions normally at scrotal temperature, producing sufficient spermatozoa to render the male completely fertile.",
        "Why_Not": "Claiming all are sterile ignores the functional capacity of the descended testis in unilateral cases.",
        "Wow_Approach": "Because cryptorchidism is a hereditary polygenic trait, a fertile unilateral cryptorchid male must NEVER be used for breeding, as he will pass the genetic defect to his offspring."
    },
    1308: {
        "topic": "Penile Deviation Terminology - Phallocampsis",
        "Core_Anatomy": "Glans penis, penile shaft, and apical ligament.",
        "Pathogenesis_Immediate": "Ventral deviation (or any structural curvature) of the penis during erection is clinically referred to as Phallocampsis.",
        "Pathogenesis_Deep": "Phallocampsis denotes a curved or deviated penis. In bulls, it most commonly presents as a ventral deviation ('rainbow penis') due to a persistent frenulum pulling the ventral aspect of the glans backward, or as a spiral deviation (corkscrew penis) due to premature slipping of the apical ligament of the penis during intromission.",
        "Why_Not": "Phimosis is the inability to exteriorize the penis. Paraphimosis is the inability to retract it. Phallocampsis strictly describes the physical bending or deviation of the shaft.",
        "Wow_Approach": "Spiral deviation of the bull's penis is normal AFTER intromission into the cow's vagina (to distribute semen). It is only considered a pathological phallocampsis if it spirals prematurely BEFORE intromission, preventing entry."
    },
    1329: {
        "topic": "Bovine Penile Erection - Cavernosal Engorgement",
        "Core_Anatomy": "Corpus cavernosum, tunica albuginea, and retractor penis muscle.",
        "Pathogenesis_Immediate": "In the bull, the erection of the penis occurs primarily due to the high-pressure vascular engorgement of the Corpus Cavernosum, synchronized with the relaxation of the retractor penis muscles.",
        "Pathogenesis_Deep": "The bull possesses a fibroelastic penis with a massive, unyielding tunica albuginea. During sexual arousal, blood is pumped into the corpus cavernosum via the contraction of the ischiocavernosus muscle against a closed venous outflow. The pressure inside the cavernosal tissue skyrockets to over 1,000-1,700 mmHg (the highest blood pressure in the mammalian body). This extreme pressure straightens the sigmoid flexure, protruding the penis.",
        "Why_Not": "The corpus spongiosum (surrounding the urethra) only engorges slightly to keep the urethral lumen open for ejaculation; it does not provide the rigid structural straightening power of the corpus cavernosum.",
        "Wow_Approach": "Because the tunica albuginea is inelastic, the bull's penis does not increase significantly in diameter during erection (unlike the stallion's vascular penis). It only increases in length as the sigmoid flexure straightens."
    },
    1330: {
        "topic": "Penile Hematoma - 'Broken Penis' in Bulls",
        "Core_Anatomy": "Tunica albuginea, corpus cavernosum, and dorsal aspect of the distal sigmoid flexure.",
        "Pathogenesis_Immediate": "A massive, sudden swelling cranial to the scrotum due to the rupture of the tunica albuginea during copulation is colloquially termed a 'Broken Penis' (Penile Hematoma).",
        "Pathogenesis_Deep": "During a normal mount, the cavernosal pressure exceeds 1,000 mmHg. If the bull's penis misses the cow's vulva and strikes her bony pelvis (ischium) during the explosive thrust, the extreme compressive force causes the tunica albuginea to rupture, almost always at its weakest point (the dorsal aspect of the distal sigmoid flexure). Blood violently escapes into the peripenile tissue, forming a massive hematoma and immediately terminating the erection.",
        "Why_Not": "Phallocampsis is a curvature, not a rupture. Fractured penis is an anatomical misnomer, as bulls lack an os penis (bone) to fracture; 'Broken penis' is the accepted clinical colloquialism for hematoma.",
        "Wow_Approach": "Do not attempt surgery immediately! Wait 5 to 7 days for the active hemorrhage to clot and the collateral vascular network to stabilize before performing surgical evacuation and suturing of the tunica albuginea."
    },
    1331: {
        "topic": "Pudendal Nerve Block - Penile Examination",
        "Core_Anatomy": "Pudendal nerve, ischiorectal fossa, and retractor penis muscle.",
        "Pathogenesis_Immediate": "The specific nerve block technique adopted for the detailed examination of the penis (to achieve complete relaxation and analgesia) in the bull is the Pudendal Nerve Block.",
        "Pathogenesis_Deep": "The pudendal nerve (derived from S3-S4 roots) supplies both sensory innervation to the glans penis and prepuce, and motor innervation to the retractor penis muscle. Injecting local anesthetic bilaterally at the ischiorectal fossa blocks the nerve. This completely paralyses the retractor penis muscles, causing the penis to passively drop out of the prepuce (prolapse) and providing total analgesia for surgical procedures (like removing fibropapillomas or repairing lacerations).",
        "Why_Not": "A sciatic nerve block would paralyze the hindlimbs, causing the bull to collapse. An epidural block (at C1-C2) affects the tail and perineum but often fails to fully relax the retractor penis muscles.",
        "Wow_Approach": "An alternative to the pudendal block is the administration of a systemic tranquilizer (like Xylazine or Acepromazine), which also relaxes the retractor penis muscles but does not provide local surgical analgesia."
    },
    1332: {
        "topic": "Phallocampsis Definition - Penile Deviation",
        "Core_Anatomy": "Penile shaft, apical ligament, and tunica albuginea.",
        "Pathogenesis_Immediate": "The clinical term 'Phallocampsis' literally translates to and means Deviation (or curvature) of the penis.",
        "Pathogenesis_Deep": "Phallocampsis categorizes any structural bending of the erect penis that interferes with normal intromission. It includes: (1) Ventral deviation (rainbow penis) often due to a persistent frenulum or short ventral tunica albuginea. (2) Spiral deviation (corkscrew penis) due to premature rolling of the apical ligament. (3) S-shaped deviation due to inadequate length of the preputial lining.",
        "Why_Not": "Broken penis is a hematoma (rupture). Double penis is diphallia (a congenital duplication). Phallocampsis strictly denotes deviation.",
        "Wow_Approach": "Spiral deviation is the most common form of phallocampsis in polled beef breeds. It can only be accurately diagnosed during a test mating or via electroejaculation, as the penis may appear perfectly straight when flaccid."
    },
    1333: {
        "topic": "White Side Test - Detecting Pus in Reproductive Fluids",
        "Core_Anatomy": "Uterine endometrium, cervical mucus, and polymorphonuclear leukocytes (PMNs).",
        "Pathogenesis_Immediate": "The White Side Test is a rapid, cow-side biochemical test used to detect the presence of subclinical purulent inflammation (pus / leukocytes) in cervical mucus or semen.",
        "Pathogenesis_Deep": "The test detects the enzyme peroxidase, which is abundant in the granules of neutrophils (PMNs). When cervical mucus from a cow with subclinical endometritis is boiled with 5% sodium hydroxide (NaOH), the leukocyte peroxidases react, causing the fluid to turn distinctively yellow (positive). Normal, healthy estrual mucus remains clear (negative).",
        "Why_Not": "PSP (Phenolsulfonphthalein) dye test is used for evaluating fallopian tube patency. The Cuboni test evaluates urinary estrogens for pregnancy diagnosis in mares. Only the White Side test is designed for leukocyte detection.",
        "Wow_Approach": "The White Side test is highly valuable for screening repeat-breeder cows where the estrual mucus appears visually clear, but actually contains microscopic levels of spermicidal neutrophils."
    },
    1334: {
        "topic": "Pharmacological Dosages in Andrology - Low Dose MCQ",
        "Core_Anatomy": "Systemic circulation and specific drug receptors.",
        "Pathogenesis_Immediate": "Objective exams often present standard dosage options (like 0.25 mg/kg) to evaluate the precise clinical administration of potent reproductive or anesthetic drugs.",
        "Pathogenesis_Deep": "For example, 0.25 mg/kg is a common dosage for specific tranquilizers (like Acepromazine) or hormones used in reproductive protocols. Mastery of precise mg/kg dosing is critical to prevent toxicity or therapeutic failure in large animal practice.",
        "Why_Not": "Using a generic 1 mg/kg for all drugs leads to lethal overdoses with potent sedatives (like Xylazine, which is dosed at 0.05 - 0.1 mg/kg in cattle).",
        "Wow_Approach": "Always memorize the 'species-specific sensitivity'—cattle require only 1/10th the dose of xylazine compared to horses to achieve the same level of sedation."
    },
    1335: {
        "topic": "Micro-dosing in Reproduction - Ultra-Low Dose MCQ",
        "Core_Anatomy": "Systemic circulation and specific drug receptors.",
        "Pathogenesis_Immediate": "Ultra-low dosages such as 0.025 mg/kg represent the therapeutic range for highly potent pharmacological agents, such as specific prostaglandins or alpha-2 agonists in sensitive species.",
        "Pathogenesis_Deep": "For example, standard dinoprost (natural PGF2-alpha) is dosed at 25 mg total per cow, whereas synthetic analogues like cloprostenol are highly potent and dosed at only 500 micrograms total per cow. Confusing the micro-dosing of synthetics with natural hormones results in massive overdosing.",
        "Why_Not": "Administering a macro-dose of a micro-dosed drug causes severe systemic side effects, such as violent smooth muscle spasms, sweating, and respiratory distress.",
        "Wow_Approach": "When reading pharmacology questions, pay strict attention to the units (mg vs. micrograms) and the specific drug derivative (natural vs. synthetic) to accurately select the correct dose."
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
