import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    734: {
        "topic": "Homology of Gonadal Cells - Granulosa and Sertoli Cells",
        "Core_Anatomy": "Ovarian follicles (granulosa layer) and testicular seminiferous tubules (Sertoli cells).",
        "Pathogenesis_Immediate": "Granulosa cells in the female are embryologically homologous and physiologically similar to Sertoli cells in the male; both express FSH receptors, secrete inhibin, and synthesize estrogens under FSH stimulation.",
        "Pathogenesis_Deep": "During sexual differentiation, the bipotential gonad develops into either testes or ovaries. The coelomic epithelium gives rise to: (1) Sertoli cells in males, which surround developing germ cells. (2) Granulosa cells in females, which surround the oocyte. Physiologically, both cells are stimulated by FSH to convert androgens (produced by Leydig or Theca interna cells under LH stimulation) into estrogens using the aromatase enzyme, and both secrete inhibin to selectively inhibit pituitary FSH secretion via a negative feedback loop.",
        "Why_Not": "LH receptors are expressed primarily on Theca interna cells in the female and Leydig cells in the male (although mature preovulatory granulosa cells do acquire LH receptors shortly before ovulation). cAMP levels are highly elevated in both cells in response to FSH stimulation, as the FSH receptor is Gs-protein coupled.",
        "Wow_Approach": "This homologue relationship explains why tumors of these cells (Granulosa-Theca cell tumors in mares and Sertoli cell tumors in dogs) exhibit similar endocrine patterns, both producing elevated levels of inhibin and estrogens, which suppress pituitary gonadotropins and cause feminization or nymphomania."
    },
    735: {
        "topic": "Puberty Definition - First Estrus with Ovulation",
        "Core_Anatomy": "Hypothalamus (GnRH tonic and surge centers), pituitary gland, and ovarian follicles.",
        "Pathogenesis_Immediate": "Puberty in the female is formally defined as the age at which the animal first expresses behavioral estrus accompanied by standing heat and a successful ovulation.",
        "Pathogenesis_Deep": "The onset of puberty requires the maturation of the hypothalamic GnRH pulse generator. Prepubertally, the hypothalamus is highly sensitive to the negative feedback of low estrogen levels. As puberty approaches, this sensitivity decreases, allowing GnRH pulse frequency to rise. This stimulates pituitary LH and FSH release, driving follicular growth to preovulatory size. The resulting high estrogen levels trigger a positive feedback LH surge, culminating in behavioral estrus and the first ovulation.",
        "Why_Not": "Sexual maturity refers to the age at which the animal achieves maximum reproductive efficiency and can carry a pregnancy to term without impairing its own growth. Fertility is a general index of reproductive capacity, while pregnancy is the post-conception gestational state.",
        "Wow_Approach": "The very first ovulation in prepubertal heifers or lambs is often a 'silent ovulation' — it occurs without behavioral standing heat because the brain has not been primed by progesterone from a previous corpus luteum. Puberty is officially established on the subsequent cycle when behavioral estrus is observed."
    },
    736: {
        "topic": "Luteal Cyst Therapy - PGF2alpha as Drug of Choice",
        "Core_Anatomy": "Thick-walled luteal cyst on the ovary and the systemic circulation.",
        "Pathogenesis_Immediate": "The statement 'The drug of choice for luteal cyst in cows is PGF2alpha' is TRUE. PGF2alpha binds receptors on the luteinized cyst wall, inducing rapid luteolysis.",
        "Pathogenesis_Deep": "Luteal cysts are thick-walled, fluid-filled structures >2.5 cm that secrete progesterone, keeping the cow in a state of persistent anoestrus. Because the wall consists of functional, luteinized tissue expressing FP (prostaglandin) receptors, administering a luteolytic dose of PGF2alpha (e.g., 25 mg Dinoprost or 500 mcg Cloprostenol) causes rapid regression of the luteal tissue. Progesterone drops precipitously, allowing a new follicular wave to progress, and the cow returns to normal estrus within 3-5 days.",
        "Why_Not": "GnRH or hCG are the drugs of choice for thin-walled follicular cysts (to induce luteinization). Giving GnRH to a luteal cyst is redundant and ineffective, as the cyst is already luteinized and secreting progesterone; PGF2alpha is the primary therapy.",
        "Wow_Approach": "To ensure maximum efficacy, perform B-mode ultrasonography to verify cyst wall thickness. A wall thickness >3 mm indicates a luteal cyst, confirming that PGF2alpha will yield a >90% success rate in inducing regression and returning the cow to cycle."
    },
    744: {
        "topic": "Theriogenology Core Matching - Gynaecological Pathology",
        "Core_Anatomy": "Vaginal vestibule, uterine lumen, and the broad ligaments.",
        "Pathogenesis_Immediate": "Key VGO matching concepts: Gartner's duct cysts are vestigial remnants of the Wolffian duct on the vaginal floor; Fincher's test is used to diagnose uterine torsion; persistent hymen causes mucometra or hydrometra; pyometra presents with a closed cervix and purulent fluid.",
        "Pathogenesis_Deep": "These matching pairs cover common gynaecological abnormalities. Gartner's cysts are benign, fluid-filled vestigial remnants of the mesonephric ducts found on the ventrolateral wall of the vagina in cows, often diagnosed incidentally. Uterine torsion is a rotation of the gravid uterus, diagnosed vaginally by spiral vaginal folds and rectally by checking broad ligament tension (Fincher's test).",
        "Why_Not": "Gartner's duct is a male vestigial structure, not a Müllerian remnant (which would form the cervix/uterus). Persistent hymen is a failure of the urogenital sinus membrane to rupture, unrelated to Wolffian ducts.",
        "Wow_Approach": "Gartner's cysts are typically left untreated as they are benign and do not interfere with fertility. However, if they enlarge and cause tenesmus or block natural mating, they can be treated by aspiration or surgical marsupialization."
    },
    752: {
        "topic": "Embryo Recovery in Buffaloes - Day 7 Flushing Limitations",
        "Core_Anatomy": "Uterine cervix, uterine horns, and the water buffalo endometrium.",
        "Pathogenesis_Immediate": "If a water buffalo (Bubalus bubalis) is flushed 7 days after insemination, the embryo recovery rate is typically reduced (often <30%) compared to cattle due to poor superovulatory response, low embryo yield, and anatomical cervix tortuosity.",
        "Pathogenesis_Deep": "Embryo transfer technology (ET) in buffaloes faces significant physiological challenges: (1) Buffaloes have a smaller primordial follicle pool and lower superovulatory response to FSH (yielding only 1-3 transferable embryos vs 5-10 in cattle). (2) The cervix in buffaloes is highly tortuous, rigid, and has prominent, tightly interlocking cervical rings, making the passage of a standard embryo flushing catheter difficult and causing endometrial trauma. (3) Poor luteal support postpartum reduces early embryo survival.",
        "Why_Not": "Flushing on Day 7 is the correct biological timing (the embryo is a free-floating blastocyst in the uterus). The low recovery is not due to incorrect timing, but rather to species-specific anatomical and physiological limitations of the buffalo.",
        "Wow_Approach": "To improve embryo recovery in buffaloes: use a specialized, flexible cervical stylet under epidural anesthesia, administer a tocolytic (clenbuterol) to relax the uterine wall, and use a closed, gravity-flow flushing system with Modified PBS."
    },
    757: {
        "topic": "VGO Short Notes - High-Yield Gynaecological Pathology",
        "Core_Anatomy": "Comparative female reproductive tract.",
        "Pathogenesis_Immediate": "Short-note topics in VGO-I focus on specific pathological conditions: Salpingitis, Hydrometra, Pyometra, Freemartinism, and Retained Fetal Membranes.",
        "Pathogenesis_Deep": "These essays require detailed, structured explanations of: (1) Definition and etiology. (2) Pathogenesis and tissue changes. (3) Clinical findings on rectal palpation and ultrasound. (4) Treatment protocols. For example, Pyometra in cows is defined as purulent uterine accumulation accompanied by a persistent CL and anoestrus, treated with PGF2alpha, whereas in bitches it is an active progesterone-driven bacterial infection treated with ovariohysterectomy.",
        "Why_Not": "Simple bulleted summaries are insufficient for short notes; the candidate must demonstrate an understanding of the pathological mechanism (e.g., how the persistent CL maintains pyometra by suppressing uterine immune defenses).",
        "Wow_Approach": "When writing on Freemartinism, always include a diagram showing the vascular anastomoses between twin chorions, explain the role of AMH from the male co-twin in suppressing the female's Müllerian ducts, and outline the vaginal probe diagnostic test."
    },
    768: {
        "topic": "VGO-I Curriculum - Gynaecology and AI Overview",
        "Core_Anatomy": "Female reproductive system and semen processing.",
        "Pathogenesis_Immediate": "VGO-I syllabus comprises female reproductive anatomy, endocrinology of the cycle, estrus synchronization, artificial insemination, and non-gravid reproductive tract pathologies.",
        "Pathogenesis_Deep": "Key components involve: (1) Understanding the hormonal cascades regulating recruitment, selection, and deviation of follicular waves. (2) semen collection techniques (artificial vagina), semen evaluation (motility, morphology), diluents (egg yolk citrate, tris-buffered glycerol), cryopreservation in liquid nitrogen (-196°C), and AI techniques (rectovaginal method in cattle, transcervical in sheep).",
        "Why_Not": "Pregnancy diagnosis after Day 40, normal parturition, dystocia management, fetotomy, and caesarean section are taught in VGO-II, leaving VGO-I focused on cycling animals and the early pre-implantation phase.",
        "Wow_Approach": "Integrate semen cryopreservation physics into study: glycerol acts as an intracellular cryoprotectant, preventing ice crystal formation that would otherwise lacerate the sperm membrane during the rapid freezing process."
    },
    770: {
        "topic": "Uterine Anatomy - Bipartite and T-Shaped Uterus in Mares",
        "Core_Anatomy": "Equine cervical canal, elongated uterine body, and short uterine horns.",
        "Pathogenesis_Immediate": "The uterus of the mare is classified anatomically as bipartite, characterized by a long, prominent uterine body and two relatively short uterine horns that branch off in a T-shape configuration.",
        "Pathogenesis_Deep": "In the bipartite equine uterus: (1) The uterine body is exceptionally large (15-20 cm long) compared to the horns (10-12 cm). (2) There is no intercornual ligament, and the horns diverge at right angles. (3) The cervix is highly flaccid during estrus and tightly closed during diestrus. This anatomical configuration is suited for early embryonic migration, where the equine conceptus must travel continuously throughout the uterine body and both horns from Day 7 to Day 16 to achieve maternal recognition.",
        "Why_Not": "Cattle have a Y-shaped bicornuate uterus with a short body (2-3 cm) and long horns connected by an intercornual ligament. Sows have extremely long, convoluted horns resembling intestines. Bitches have a Y-shaped uterus with long, parallel horns suited for multi-fetal litters.",
        "Wow_Approach": "Because the equine embryo migrates continuously throughout the entire bipartite cavity to signal pregnancy, any localized endometrial scar tissue or endometrial cysts that block embryonic passage will prevent MRP, leading to early pregnancy loss."
    },
    781: {
        "topic": "Oxytocin Half-Life - Rapid 2-Minute Clearance",
        "Core_Anatomy": "Posterior pituitary gland, systemic blood circulation, and hepatic/renal peptidase clearance.",
        "Pathogenesis_Immediate": "The biological half-life of oxytocin in the circulation of domestic animals is exceptionally short, averaging approximately 2 minutes (range of 1-3 minutes).",
        "Pathogenesis_Deep": "Oxytocin is a peptide octapeptide synthesized in the paraventricular and supraoptic nuclei of the hypothalamus and stored in the posterior pituitary. Upon release (e.g., stimulated by milking or vaginal stretch), it enters the bloodstream. Because it is a small peptide, it is rapidly degraded by circulating aminopeptidases (oxytocinases) and cleared by hepatic filtration and renal excretion. This short half-life ensures that its actions (myometrial or mammary myoepithelial contraction) are transient and tightly regulated.",
        "Why_Not": "A half-life of 1-2 seconds is physically too short for a hormone to travel from the pituitary to the target organs (mammary gland/uterus). A 30-minute half-life would cause prolonged, dangerous uterine tetany during parturition, risking fetal hypoxia.",
        "Wow_Approach": "Due to the 2-minute half-life, when administering oxytocin to treat uterine inertia in a bitch or cow, give repeated small doses (or a continuous low-dose IV infusion) rather than a single large bolus, which could cause receptor down-regulation and uterine spasm."
    },
    782: {
        "topic": "GnRH Dosage - 10-20 mcg Buserelin for Ovarian Cysts",
        "Core_Anatomy": "Anterior pituitary gonadotrophs, GnRH receptors, and the preovulatory follicle/cyst.",
        "Pathogenesis_Immediate": "The standard therapeutic dose of GnRH (specifically the potent analogue Buserelin acetate) used to treat follicular cysts in dairy cattle is 10-20 mcg (typically 10 mcg, equivalent to 2.5 ml of Receptal).",
        "Pathogenesis_Deep": "Follicular cysts are fluid-filled structures >2.5 cm that persist due to a lack of an LH surge. Administering 10 mcg of Buserelin (a highly stable GnRH agonist) binds pituitary GnRH receptors, triggering a rapid release of endogenous LH and FSH within 2-4 hours. This induced LH surge acts on the granulosa cells of the cyst wall, causing them to luteinize. The cyst is converted into a progesterone-producing luteal cyst, which can then be regressed using PGF2alpha 9-11 days later to restore cycling.",
        "Why_Not": "A 5 mcg dose of Buserelin is too low and may fail to induce a reliable LH surge in large, dairy-breed cows. A 50-100 mcg dose is typical of native GnRH (Gonadorelin), not the synthetic, potent Buserelin analogue.",
        "Wow_Approach": "When treating cystic ovaries: combine the 10 mcg Buserelin injection with the insertion of a CIDR device. Progesterone from the CIDR primes the hypothalamus, while the GnRH luteinizes the cyst, resulting in a higher pregnancy rate on the subsequent synchronized estrus."
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
