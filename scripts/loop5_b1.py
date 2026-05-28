import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    504: {
        "topic": "VGO Matching - Obstetrical Conditions and Procedures",
        "Core_Anatomy": "The vulva, vagina, cervix, uterus, and placental membranes.",
        "Pathogenesis_Immediate": "Key VGO matching pairs: Pneumovagina → Caslick's Operation (treatment). Ferguson's Reflex → Oxytocin release (mechanism of milk let-down and Stage 3 contractions). Leathery placenta → Sclerotic Metritis (chronic uterine fibrosis). Cyclopes → developmental anomaly (fetal eye fusion defect).",
        "Pathogenesis_Deep": "Ferguson's Reflex: Mechanical distension of the cervix and vaginal vault → afferent nerve signals via the pelvic nerve → hypothalamus → posterior pituitary → oxytocin release. This oxytocin surge stimulates myometrial contractions (aiding fetal and placental expulsion) and mammary myoepithelial contraction (milk let-down). This reflex is the basis of the hand-milking stimulus in dairy cows — cervical/vaginal stimulation by the calf's suckling reflex or manual milking triggers oxytocin-mediated milk ejection.",
        "Why_Not": "Cyclops (Cyclopia) is a lethal congenital anomaly where the two orbits fail to separate during embryonic development — the nose (proboscis) sits above the single fused eye. It is caused by teratogens (Veratrum californicum alkaloid cyclopamine in ewes grazing Veratrum on Day 14 of gestation is the classic veterinary cause). Cyclopia = one eye, not associated with Caslick's or Ferguson's.",
        "Wow_Approach": "Veratrum californicum (false hellebore, corn lily) alkaloid cyclopamine blocks the Hedgehog signalling pathway, preventing midface and orbital separation. Ewes grazing Veratrum on Day 14 of gestation produce cycloptic lambs. This plant teratogen was the original discovery that led to understanding the Hedgehog pathway, which is now a cancer therapy target (vismodegib)."
    },
    505: {
        "topic": "Pneumovagina and Caslick's Operation in Mares",
        "Core_Anatomy": "The vulvar labia (conformation), the dorsal vulvar commissure, and the perineal body.",
        "Pathogenesis_Immediate": "Pneumovagina (aspiration of air and faecal contamination into the vagina) is corrected by Caslick's Operation — surgical apposition (suturing) of the dorsal vulvar labia to reduce the vulvar opening to a 4-5 cm slit sufficient only for urine passage.",
        "Pathogenesis_Deep": "Pneumovagina predisposing conformation: Sunken anus (anus tilted forward below the pelvic brim), poor perineal conformation in lean, older multiparous mares. The poorly conformed dorsal vulva lacks the sphincteric seal of normal mares — air, bacteria, and faecal material aspirate into the vagina with each locomotion step. Resulting ascending bacterial contamination causes: endometritis, uterine fibrosis, embryonic death, and infertility. Caslick's corrects the conformational defect.",
        "Why_Not": "Fistulous tract is a tubular epithelial-lined channel connecting two abnormal cavities (e.g., rectovaginal fistula — connecting the rectum to the vagina via a tear in the perineal body, caused by tearing during parturition). This is distinct from Pneumovagina (air entry through the external vulvar opening without fistula).",
        "Wow_Approach": "Caslick's scoring system (perineal body scoring): Score 1 (good) = anus above pelvic brim, vulva vertical. Score 2 (marginal) = anus at brim level. Score 3 (poor) = anus below brim, vulva tilted forward. Score 3 mares should have Caslick's before each breeding season. Grading is done with the mare in a stocks, visual inspection from behind."
    },
    507: {
        "topic": "Ferguson's Reflex - Neuroendocrine Mechanism",
        "Core_Anatomy": "The uterine cervix and vaginal mechanoreceptors, the afferent pelvic nerve, the hypothalamic paraventricular nucleus, and the posterior pituitary gland.",
        "Pathogenesis_Immediate": "Ferguson's Reflex is the neuroendocrine mechanism by which mechanical distension of the uterine cervix and vagina triggers oxytocin release from the posterior pituitary, causing uterine contractions to expel the fetus and then the placenta.",
        "Pathogenesis_Deep": "Reflex pathway: Fetal head pressure against cervix → stretch receptors activated → afferent signals via pelvic/hypogastric nerve → spinal cord → hypothalamic paraventricular nucleus (PVN) → action potentials along the hypothalamo-neurohypophyseal tract → oxytocin release from posterior pituitary → blood-borne oxytocin reaches uterine OTR → myometrial contractions → stronger fetal pressure → more oxytocin → positive feedback amplification. This positive feedback loop drives the explosive Stage 2 contractions needed for delivery.",
        "Why_Not": "Unlike most endocrine systems (which use negative feedback to maintain homeostasis), the Ferguson's Reflex uses POSITIVE feedback — each cycle of contractions increases cervical distension, which increases oxytocin release, which increases contractions, until delivery is complete. This is one of the few physiological positive feedback systems in the body.",
        "Wow_Approach": "Ferguson's Reflex is also the mechanism of milk let-down: Teat stimulation by the calf's suckling → afferent sensory nerve signals → hypothalamic PVN → oxytocin release → mammary myoepithelial cell contraction → alveolar milk ejected into the duct system → let-down. Conditioning (hearing the milking machine or bucket) can stimulate oxytocin release via a conditioned Pavlovian reflex — explaining why stressful milking environments reduce milk yield."
    },
    508: {
        "topic": "Leathery Placenta and Sclerotic Metritis - Chronic Uterine Fibrosis",
        "Core_Anatomy": "The endometrium (uterine mucosa), the myometrium, and the placentomes (in ruminants).",
        "Pathogenesis_Immediate": "Leathery Placenta (sclerotic endometrium) is the end-stage of chronic metritis where repeated uterine infections cause progressive fibrosis of the endometrium and myometrium, producing a thick, firm, inelastic uterine wall that cannot support implantation.",
        "Pathogenesis_Deep": "Sclerotic Metritis progression: Acute metritis (bacterial contamination post-partum) → chronic endometritis (persistent low-grade infection) → fibroblast activation and collagen deposition in the endometrial stroma → progressive loss of uterine glands (glandular fibrosis) → myometrial fibrosis → loss of uterine contractility and expansibility. The resulting 'leathery' uterus cannot expand to accommodate a growing fetus and cannot produce the secretions needed for early embryo nutrition — permanent sterility results.",
        "Why_Not": "Pyometra (closed cervix, purulent uterine content) is an active infection with fluid accumulation — not fibrosis. Hydrometra (fluid in the uterus without infection) causes uterine distension without wall thickening. Sclerotic metritis/leathery placenta is the IRREVERSIBLE fibrotic endpoint of chronic infection.",
        "Wow_Approach": "Diagnosis of sclerotic metritis: Rectal palpation reveals a thick, firm, symmetrically enlarged uterus with poor motility (normally the uterus has a doughy, contractile tone). Ultrasonography shows increased echogenicity and loss of normal endometrial fold pattern. Uterine biopsy (Knudsen biopsy punch) shows Grade III endometritis on histopathology — fibrosis replacing >50% of glandular tissue. These cows should be culled."
    },
    528: {
        "topic": "VGO-I Fill-in Key Gynaecological Parameters",
        "Core_Anatomy": "The bovine, equine, and canine reproductive tracts — comparative anatomy and physiology.",
        "Pathogenesis_Immediate": "Critical VGO-I fill-in facts: Duration of follicular phase in cattle = 4-6 days. Duration of luteal phase in cattle = 14-15 days. Normal CL diameter in cattle = 2-3 cm. Normal dominant follicle diameter at ovulation = 1.5-2.0 cm. Minimum progesterone for luteal phase = 1 ng/ml. Progesterone at mid-luteal phase (Day 10-14) = 5-10 ng/ml.",
        "Pathogenesis_Deep": "Follicular wave dynamics in cattle: 2-3 follicular waves occur per 21-day oestrous cycle. Each wave: Recruitment (5-7 small follicles 2-4mm diameter grow) → Selection (one follicle is selected as dominant) → Dominance (dominant follicle grows to 12-16mm, suppresses subordinates via inhibin B and IGF-1) → Deviation (subordinates undergo atresia). The wave producing the ovulatory follicle begins on Day 15-16 of the previous cycle.",
        "Why_Not": "Single-wave cycles (occasionally seen in cattle) have one large follicular wave with prolonged dominance. The dominant follicle in single-wave cycles undergoes luteinization (without ovulation) if progesterone is still elevated, contributing to follicular cysts. Three-wave cycles (seen in approximately 20% of cattle) have slightly longer inter-ovulatory intervals (23-24 days).",
        "Wow_Approach": "Ovarian ultrasonography (rectal B-mode ultrasound with 5-7.5 MHz probe) allows real-time follicular wave mapping: image the ovary in cross-section, measure every follicle >3mm diameter, plot follicle diameter daily. This folliculogram reveals the wave emergence pattern (Day 1-2, Day 8-10, Day 15-16 in a 3-wave cycle) and identifies the ovulatory follicle."
    },
    539: {
        "topic": "Infertility vs Sterility vs Subfertility - Definitions",
        "Core_Anatomy": "The reproductive axis (HPG axis), the gonads, and the reproductive tract.",
        "Pathogenesis_Immediate": "Infertility = reduced or temporary failure of reproductive performance (reversible — may respond to treatment). Sterility = absolute, permanent inability to reproduce (irreversible — cannot be corrected). Subfertility = below-normal but not absent reproductive efficiency (produces some offspring, but fewer than expected).",
        "Pathogenesis_Deep": "The correct answer for 'denotes reduced fertility' is Infertility (the MCQ answer choice). Infertility is the broad clinical term for any sub-optimal reproductive performance that is potentially correctable. A repeat-breeding cow (3+ services without conception) is infertile but not necessarily sterile. Sterility implies complete absence of reproductive capacity (e.g., cryptorchid bilateral with spermatogenic arrest). Nymphomania is the condition of prolonged, continuous oestrus-like behaviour due to follicular cysts — a cause of infertility but not a synonym for reduced fertility.",
        "Why_Not": "Pseudopregnancy (false pregnancy) is a condition where non-pregnant females show signs of pregnancy (mammary development, nesting behaviour in bitches) due to persistent luteal phase — it is a reproductive abnormality but not classified as infertility per se. Nymphomania (from Greek: nymphe = bride, mania = madness) in cattle is caused by follicular cysts producing continuous estrogen without luteal counter-regulation.",
        "Wow_Approach": "Reproductive efficiency assessment in a cattle herd uses the Pregnancy Rate (PR) formula: PR = Submission Rate × Conception Rate. Target PR >20%/21-day period. Farms below this threshold are classified as having a herd infertility problem. Systematic investigation: CIDR-based synchronization challenge (to distinguish anovulatory vs conception failure), semen testing (to eliminate bull subfertility), and uterine culture (to identify subclinical endometritis)."
    },
    541: {
        "topic": "Age of Puberty in Buffalo - 24-48 Months",
        "Core_Anatomy": "The hypothalamic GnRH pulse generator, the anterior pituitary, and the ovarian follicle-CL system.",
        "Pathogenesis_Immediate": "Age of puberty in the buffalo (Bubalus bubalis) is 24-48 months (2-4 years) — significantly later than cattle (8-12 months). This delayed puberty is due to the buffalo's slower growth rate and higher nutritional requirements relative to its body mass.",
        "Pathogenesis_Deep": "Puberty onset requires: (1) Body weight threshold (critical body mass — approximately 55-60% of mature body weight in buffalo). (2) Hypothalamic kisspeptin-GnRH axis maturation (leptin signalling from adipose tissue to arcuate nucleus kisspeptin neurons triggers GnRH pulsatility). In buffaloes, the body weight threshold is reached at 24-36 months under average management, but poor nutrition can delay puberty to 48+ months.",
        "Why_Not": "Cattle (Bos taurus dairy breeds) reach puberty at 8-12 months at 55-60% of mature body weight. Zebu cattle (Bos indicus) reach puberty at 16-24 months. Sheep/goats reach puberty at 6-8 months. Pigs reach puberty at 5-7 months. Buffalo's 24-48 month puberty is the LATEST among major domestic livestock species.",
        "Wow_Approach": "Accelerate buffalo puberty: Flush feeding (high-energy diet for 60 days pre-mating) + exposure to a fertile bull (pheromone stimulation) can advance puberty by 3-6 months in well-grown heifers. Teasing with a vasectomized bull from 18 months of age is used in commercial buffalo operations to detect first oestrus and confirm reproductive soundness before natural mating."
    },
    542: {
        "topic": "T-Shaped Uterus in the Mare",
        "Core_Anatomy": "The equine uterine body (long), the two short uterine horns (bilateral), and the cervix.",
        "Pathogenesis_Immediate": "The mare's uterus is T-shaped (or Y-shaped depending on the reference) — characterized by a prominent, elongated uterine BODY with two relatively shorter uterine horns branching off at approximately right angles, creating a T-configuration when viewed dorsally.",
        "Pathogenesis_Deep": "Comparative uterine shapes: Mare = T-shaped (long body, short horns — body is the primary uterine chamber). Cow = Y-shaped (two long equal horns, short body). Sow = F/Y-shaped (extremely long, convoluted horns, small body). Bitch = Y-shaped (two long horns proportionate to body). The mare's T-shaped uterus means the developing conceptus lives primarily in the uterine BODY (unlike ruminants where it migrates into the horn). The equine embryo migrates continuously throughout the body from Day 7-16 to achieve MRP.",
        "Why_Not": "In cattle, the uterus is Y-shaped with two long equal horns (10-12 cm) and a short body (2-3 cm). Pregnancy in cattle is exclusively within one uterine horn. The mare's uniquely long uterine body relative to horns is the anatomical basis for the equine embryo's characteristic migration pattern.",
        "Wow_Approach": "Mare uterine body endoscopy (hysteroscopy): Insert a 1-metre fibre-optic scope through the cervix into the uterine body to visualize endometrial folds, lymphatic lacunae, and early embryo attachment sites. This diagnostic technique identifies focal endometrial fibrosis (Kenney Grade III endometritis) — a major cause of infertility in performance mares."
    },
    543: {
        "topic": "Caruncle Count in Bovine Uterus - 70-120 Caruncles",
        "Core_Anatomy": "The uterine caruncles (raised, button-like endometrial projections), the placentomes (caruncle + cotyledon complexes), and the bovine uterine horns.",
        "Pathogenesis_Immediate": "The number of caruncles in the bovine uterus is approximately 70-120 (spread across both uterine horns and the uterine body) — these are the maternal components of the placentomal attachment system, with 70-80 caruncles in the pregnant horn and 30-40 in the non-pregnant horn.",
        "Pathogenesis_Deep": "Bovine placentomal system: Caruncle (maternal C-shaped/cup-shaped endometrial projection, convex surface) + Cotyledon (fetal villous mass that interlocks with the caruncle crypts). Together they form a Placentome — the functional unit of ruminant placentocentesis. Cattle have 4 rows of caruncles (2 per horn = 4 total rows). The caruncle-cotyledon connection is non-invasive (epitheliochorial/synepitheliochorial) — mechanical interdigitation without trophoblast invasion of maternal blood vessels.",
        "Why_Not": "The MCQ option 45-55 is too low. Option 200-250 is too high (sheep have approximately 90-100 placentomes). Cattle typically have 70-120 caruncles. The exact count varies by breed: B. taurus breeds have fewer, larger placentomes; B. indicus breeds have more, smaller ones.",
        "Wow_Approach": "The caruncle is one of the most important anatomical landmarks in bovine reproductive examination: (1) Pregnant horn: Placentomes enlarge to 10-15 cm diameter at term — palpable per rectum as large, soft cotyledonary masses. (2) Non-pregnant horn: Caruncles remain small (2-3 cm), firm. (3) Pyometra: Caruncles are enlarged and spongy; pus fills the lumen. (4) Post-partum RFM: Cotyledonary-caruncular fusion prevents normal placental separation."
    },
    545: {
        "topic": "Ovarian Shape - Bean-Shaped Ovaries in Sows",
        "Core_Anatomy": "The sow's ovary (surface, germinal epithelium, follicles, and corpora lutea).",
        "Pathogenesis_Immediate": "Sow ovaries are uniquely bean-shaped (oblong, indented on one surface — the hilus) and have a distinctive 'mulberry-like' or 'cluster-of-grapes' surface appearance during the luteal phase when multiple large corpora lutea (1.0-1.5 cm diameter) are palpable on the ovarian surface.",
        "Pathogenesis_Deep": "Sow ovarian characteristics: Multiple CL (10-20 per ovary) reflect the highly polytocous nature of pigs (average litter size 10-14). All CL are similar in size (unlike the single dominant CL in cattle). The sow ovary during the luteal phase (Days 3-14 of 21-day cycle) is a massive, irregular, multilobulated structure that can weigh 5-8 g (vs 5-10 g for a bovine CL-containing ovary). Mare ovaries are kidney-shaped (ovulation fossa on the free border — the unique mare ovary feature).",
        "Why_Not": "Mare ovaries are kidney-shaped and OVULATE ONLY from the Ovulation Fossa (a depression on the free border, opposite the hilus). This is unique — all other species can ovulate from any point on the ovarian surface. The Ovulation Fossa is the anatomical basis for non-surgical oocyte recovery in mares (transvaginal follicle aspiration through the fossa).",
        "Wow_Approach": "The mare's ovulation fossa is palpable rectally as a distinct indentation on the cranial free border of the ovary. The preovulatory follicle (>35 mm diameter in mares) feels soft and fluctuant, and is always located adjacent to the fossa. All equine ovulations occur exclusively through this fossa — a fact unique to the horse family (Equidae)."
    },
    546: {
        "topic": "Follicular Phase of Bovine Oestrous Cycle - Proestrus and Oestrus",
        "Core_Anatomy": "The anterior pituitary (FSH, LH), the dominant follicle (estradiol production), and the hypothalamic GnRH pulse generator.",
        "Pathogenesis_Immediate": "The Follicular Phase of the bovine oestrous cycle comprises Proestrus and Oestrus — characterized by rising estradiol from the dominant follicle, declining progesterone (CL regression), and culminating in the preovulatory LH surge and ovulation.",
        "Pathogenesis_Deep": "Bovine follicular phase (Days 17-21 of the 21-day cycle): Day 16-17 = Luteolysis (PGF2alpha causes CL regression, progesterone falls). Day 17-19 = Proestrus (estradiol from dominant follicle rises, uterine tone increases, cervical mucus clears). Day 19-21 = Oestrus (peak estradiol → LH surge → standing oestrus behavior for 12-18 hours). Day 21 = Ovulation (24-30 hours after oestrus end). The follicular phase totals 4-6 days.",
        "Why_Not": "The Luteal Phase (Metoestrus + Dioestrus = Days 1-16) is not part of the Follicular Phase. Metoestrus (Days 1-5) = CL formation. Dioestrus (Days 5-16) = mature CL, peak progesterone. The Follicular Phase (Proestrus + Oestrus) is the short final phase where the dominant follicle takes over hormonal control from the regressing CL.",
        "Wow_Approach": "Progesterone concentration across the bovine oestrous cycle: Day 1 (oestrus): <0.5 ng/ml (baseline). Day 5: 2-3 ng/ml (rising). Day 10-14: 5-10 ng/ml (peak luteal phase). Day 17 (luteolysis): drops rapidly to <0.5 ng/ml. This progesterone profile is the basis for milk progesterone assays (ELISA) used for: early pregnancy diagnosis (elevated on Day 21-23), silent heat detection (elevated during 'missed' oestrus), and CL assessment."
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
