import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    594: {
        "topic": "Progesterone Level at Ovulation in Bitches - 2-4 ng/ml",
        "Core_Anatomy": "The canine preovulatory follicle (granulosa and theca cells), the peripheral blood progesterone receptor assay (ELISA/RIA).",
        "Pathogenesis_Immediate": "In bitches, ovulation occurs when peripheral serum progesterone reaches 2-4 ng/ml — a uniquely elevated pre-ovulatory progesterone level compared to most other domestic species (where progesterone at ovulation is baseline <0.5 ng/ml).",
        "Pathogenesis_Deep": "Unique canine LH surge/ovulation physiology: In the bitch, the preovulatory LH surge triggers premature luteinization of the preovulatory follicle granulosa cells BEFORE ovulation, causing a rise in progesterone from 0.5 to 2-4 ng/ml. At 2-4 ng/ml (the ovulation progesterone threshold), the follicle ruptures. After ovulation, progesterone continues to rise rapidly to 15-30 ng/ml during diestrus. This pre-ovulatory luteinization is unique to bitches and is why canine oocytes are ovulated as PRIMARY OOCYTES (immature), requiring 48-72 hours of in-oviductal maturation before fertilization.",
        "Why_Not": "In cattle, progesterone at ovulation = <0.5 ng/ml (baseline — the CL hasn't formed yet). In mares, progesterone at ovulation = 0.3-0.8 ng/ml. The 2-4 ng/ml threshold is specifically the canine ovulation window. Sequential progesterone monitoring in bitches (every 2-3 days from proestrus onset): <1 ng/ml = follicular phase, 1-2 ng/ml = approaching LH surge, 2-4 ng/ml = ovulation window, >5 ng/ml = post-ovulatory diestrus.",
        "Wow_Approach": "Practical AI timing in bitches: Test serum progesterone at first sign of oestrus (proestrus). Test every 2 days until progesterone reaches 2-4 ng/ml (ovulation). Perform AI on Day of ovulation (2-4 ng/ml) AND 2 days later (when oocytes have matured). Use chilled extended semen within 24 hours; use frozen semen only at the 4-6 ng/ml window (transcervical or surgical AI for maximum fertility)."
    },
    596: {
        "topic": "Freemartinism - Key True/False Statements",
        "Core_Anatomy": "The bovine twin placenta (vascular anastomoses), the fetal gonadal development, and the Müllerian duct system.",
        "Pathogenesis_Immediate": "Key True/False for Freemartinism: 'Both male and female calves are sterile' = FALSE (only the female co-twin is sterile in 92% of cases; the male is fertile). 'Single-born freemartins can occur' = FALSE (freemartinism requires twin pregnancy with shared placental circulation). 'It is a genetic disorder' = FALSE (it is a developmental/hormonal disorder caused by placental blood chimerism).",
        "Pathogenesis_Deep": "Freemartinism mechanism: Shared placental vasculature (chorionic anastomoses by Day 30-40) allows male twin's testosterone and AMH to circulate into the female twin → suppresses Müllerian duct (uterus/cervix/vagina) development → masculinizes gonads (streak ovaries). The male twin is NOT affected because his gonads are fully developed and unresponsive to the small amount of hormones from the female. It is NOT genetic — it is a paracrine developmental effect.",
        "Why_Not": "Genetic sex (XX karyotype) of the freemartin is normal female — the defect is in phenotypic development, not chromosomal constitution. However, blood chimerism (XX + XY cells in blood) results from the shared placental vasculature. A karyotype from blood will show XX/XY chimerism — but a karyotype from other tissue (skin fibroblasts) will show only XX.",
        "Wow_Approach": "Three rapid freemartin tests: (1) Vaginal probe: <10 cm vaginal depth = freemartin. (2) Blood karyotype: XX/XY chimerism confirms freemartin. (3) AMH (Anti-Müllerian Hormone) serum test: elevated AMH in female co-twin confirms residual gonadal testicular tissue. The vaginal probe test is the fastest and most practical field test — perform on every heifer born co-twin with a bull calf before purchasing."
    },
    597: {
        "topic": "Early Embryonic Death - Less Than 40 Days Gestation in Cattle",
        "Core_Anatomy": "The bovine conceptus (early trophectoderm and embryoblast), the endometrium, and the corpus luteum.",
        "Pathogenesis_Immediate": "Early embryonic death (EED) in cattle is defined as embryonic death occurring before Day 40 of gestation (when the transition from embryonic to fetal period occurs). This accounts for the majority of reproductive failures in repeat-breeding cows.",
        "Pathogenesis_Deep": "EED timeline: Days 1-7 = pre-implantation death (fertilization failure or chromosomal errors — these go undetected, the cow returns to normal oestrus on Day 21). Days 8-16 = conceptus fails to produce adequate IFN-tau → CL regresses normally → cow returns to oestrus on Day 21-24 (slightly delayed). Days 16-40 = post-MRP death, causes delayed return to oestrus (>24 days). The vast majority of EED (60-70%) occurs before Day 16, making it indistinguishable from fertilization failure without intensive investigation.",
        "Why_Not": "Death after Day 40 is classified as Early Fetal Death (the conceptus is now in the fetal period and has established placental attachment). Death in the late fetal period (Days 100-260) is classified as abortion. The clinical distinction matters because: EED causes early returns to oestrus (Days 18-30 post-AI), while abortions require pregnancy diagnosis confirmation and differential testing for abortifacient pathogens.",
        "Wow_Approach": "Causes of EED in order of importance: (1) Genetic/chromosomal errors (natural embryo selection — up to 30% of fertilized eggs have lethal chromosomal abnormalities). (2) Subclinical endometritis (impaired uterine environment). (3) Heat stress (hyperthermia on Days 1-3 post-AI is catastrophic — the pre-implantation embryo is exquisitely sensitive to temperature above 39°C). (4) Luteal insufficiency (inadequate progesterone). Manage by: cool barns in summer, CIDR supplementation, minimizing stress around AI."
    },
    598: {
        "topic": "Maximum Fetotomy Cuts - 6 Cuts in Cattle",
        "Core_Anatomy": "The fetal skeleton, major body regions (head, neck, forelimbs, thorax, hindlimbs, pelvis), and the maternal reproductive tract.",
        "Pathogenesis_Immediate": "The maximum recommended number of fetotomy cuts in cattle is 6 — beyond 6 cuts, the maternal reproductive tract trauma (endometrial lacerations, broad ligament tears, peritoneal contamination) becomes too severe, threatening maternal life. Beyond 6 cuts, C-section is preferred.",
        "Pathogenesis_Deep": "Fetotomy cut sequence (standard complete fetotomy): Cut 1 = forelimb removal at shoulder. Cut 2 = opposite forelimb removal. Cut 3 = head and neck amputation. Cut 4 = thorax bisection. Cut 5 = hindlimb removal. Cut 6 = pelvic bisection. Each cut uses a fetatome (Thygesen's) with a wire saw, performing retropulsion of the remaining trunk between cuts. After each removal, the maternal tract is inspected for lacerations.",
        "Why_Not": "Partial fetotomy (1-3 cuts, e.g., removing one flexed forelimb to correct a malposture) has 90%+ subsequent fertility in the dam. Complete fetotomy (all 6 cuts) has approximately 50-70% subsequent fertility. The decision to proceed beyond 3 cuts is based on: fetal condition (emphysematous vs fresh carcass), maternal tract integrity, and operator skill level.",
        "Wow_Approach": "Fetotomy contraindications: (1) Viable fetus — NEVER perform fetotomy on a living fetus. (2) Inadequate epidural anaesthesia — the dam must be fully relaxed. (3) Insufficient lubrication — always use copious methylcellulose gel. (4) Incomplete cervical dilation — forced fetotomy through an undilated cervix lacerates the maternal tract fatally. When in doubt — C-section is safer for the dam."
    },
    599: {
        "topic": "Interestrus Interval in Bitches - 7 Months",
        "Core_Anatomy": "The canine ovary (CL, follicular phase timing), the hypothalamic-pituitary axis, and the obligatory anestrus period.",
        "Pathogenesis_Immediate": "The inter-oestrous interval in bitches is 6-10 months (average 7 months) — bitches cycle twice yearly (approximately), with an obligatory anestrus phase of 4-5 months between cycles during which the hypothalamic-pituitary axis is refractory to reproductive stimulation.",
        "Pathogenesis_Deep": "Canine reproductive cycle phases: Proestrus (7-10 days) + Oestrus (7-9 days) + Metoestrus/Dioestrus (60-65 days, whether pregnant or not) + Anestrus (60-150 days, breed dependent). Total inter-oestrous interval = 180-300 days (6-10 months). German Shepherd Dogs have shorter intervals (5-6 months). Basenji (uniquely monoestrous — once yearly). Most bitches are biestrous (twice yearly).",
        "Why_Not": "Cats are polyoestrous (continuously cycling seasonal breeders — multiple cycles during the spring/summer long-day breeding season without an obligatory interestrus pause). Cattle cycle every 21 days year-round (essentially polyestrous with continuous cycling). Mares cycle seasonally but within the breeding season, cycle every 21 days. Only the bitch has this unique prolonged obligatory anestrus between cycles.",
        "Wow_Approach": "Suppress canine oestrus pharmacologically: Megestrol acetate (progestogen) — 2.2 mg/kg daily for 32 days starting in proestrus. Delmadinone acetate (progestogen) — single injection in anestrus. Osaterone acetate — used in male dogs for BPH suppression. These hormonal suppressants delay but do not eliminate the oestrous cycle — permanent prevention requires OHE."
    },
    600: {
        "topic": "Zona Reaction - Block to Polyspermy by Enzymes from Cortical Granules",
        "Core_Anatomy": "The zona pellucida (ZP1, ZP2, ZP3 glycoproteins), the oocyte cortical granules (lysosomal granules beneath the plasma membrane), and the acrosomal enzymes of the sperm.",
        "Pathogenesis_Immediate": "Block to polyspermy (prevention of more than one sperm fertilizing an egg) is achieved by enzymes from the oocyte's Cortical Granules — released by exocytosis immediately after the first sperm-oocyte fusion, they modify the zona pellucida to prevent additional sperm penetration.",
        "Pathogenesis_Deep": "Cortical granule exocytosis: First sperm-egg fusion → inositol trisphosphate (IP3)-mediated calcium wave from the perivitelline space → cortical granule (lysosomal) exocytosis throughout the entire oocyte cortex → release of enzymes (ovastacin, N-acetylglucosaminidase, peroxidase) into the perivitelline space → ZP2 cleavage and ZP3 modification (N-glycan removal) → zona pellucida hardens (zona reaction) and becomes impenetrable to additional sperm within 5-10 minutes of first sperm fusion.",
        "Why_Not": "The fast block to polyspermy (electrical block — membrane potential depolarization from +10 mV to -70 mV within seconds of sperm fusion) provides the first, ultra-rapid barrier. The zona reaction (cortical granule exocytosis) provides the slow, permanent block. Together they ensure only ONE sperm fertilizes the oocyte. Polyspermy causes triploid embryos — invariably lethal.",
        "Wow_Approach": "In IVF, polyspermy is a major quality control issue — when sperm concentrations are too high in the fertilization droplet, multiple sperm can penetrate the zona before the zona reaction is complete. This produces triploid (3N) embryos that appear morphologically normal in early cleavage but invariably die before implantation. Reduce polyspermy by optimizing IVF sperm concentration to 1-2 million/ml."
    },
    601: {
        "topic": "Clenbuterol - Tocolytic to Postpone Parturition in Cattle",
        "Core_Anatomy": "The uterine myometrium (beta-2 adrenergic receptors), the placental unit, and the fetal-maternal hormonal axis.",
        "Pathogenesis_Immediate": "Clenbuterol (a selective beta-2 adrenergic agonist) is the drug used especially to postpone (delay) parturition in cattle by suppressing myometrial contractions — useful for delaying imminent calving by 24-48 hours when obstetrical assistance will be required.",
        "Pathogenesis_Deep": "Clenbuterol for parturition delay: 0.3-0.6 mcg/kg IV in cattle delays the onset of active labour (Stage 2) by 4-24 hours by blocking myometrial OTR-mediated contractions. Used clinically when: (1) Calving in the middle of the night with no veterinary assistance available. (2) Calf in an uncorrected malpresentation. (3) Cervix not fully dilated. (4) Fetal emphysema — to gain time for fetotomy preparation. Chronogest (progesterone device) maintains pregnancy long-term; Receptal (GnRH) induces ovulation — neither delays parturition.",
        "Why_Not": "Cloprostenol INDUCES parturition (luteolysis + uterine contractions). Chronogest (progesterone implant) prevents oestrus/ovulation for weeks to months. Receptal (GnRH analogue) induces the LH surge. Only Clenbuterol among these options specifically DELAYS (postpones) parturition by tocolysis.",
        "Wow_Approach": "Clenbuterol parturition delay protocol: Administer 0.3 mcg/kg IV slowly over 2 minutes. Effect onset: 2-5 minutes. Duration: 4-12 hours. Can repeat once after 4 hours if needed. After tocolysis, allow parturition to proceed naturally or perform obstetrical intervention. Never delay beyond 24 hours as uterine exhaustion and fetal hypoxia become critical risks."
    },
    602: {
        "topic": "Day 7 Bovine Embryo Stage - Compact Morula or Early Blastocyst",
        "Core_Anatomy": "The bovine preimplantation embryo at Day 7 post-fertilization.",
        "Pathogenesis_Immediate": "The Day 7 bovine embryo is at the stage of Compact Morula to Early Blastocyst — the IETS (International Embryo Transfer Society) standard morphological stage for commercial embryo transfer collection in cattle.",
        "Pathogenesis_Deep": "Bovine embryo development timeline: Day 1 = zygote. Days 2-3 = 4-8 cell cleavage. Day 4 = early morula (loose blastomere cluster). Day 5 = compact morula (tight junctions formed, blastocoel beginning). Day 6 = early blastocyst (blastocoel visible — signet ring stage). Day 7 = blastocyst (distinct ICM and trophoblast). Day 8 = expanded blastocyst (zona thinning). Day 9-10 = hatched blastocyst. Commercial ET embryo collection is performed on Day 7 because the embryo is accessible within the uterus (not yet attached/implanted) and is at the optimal transferable stage.",
        "Why_Not": "A 16-cell stage is reached on approximately Day 3. Early morula is Day 4-5. The MCQ option 'blastocyst' without qualifier could also be correct for Day 7 — the key distinction is 'Day 7 = compact morula to early blastocyst' (the stage just BEFORE the fully expanded blastocyst). The IETS Grade 1 compact morula collected on Day 7 is the most commonly transferred embryo stage.",
        "Wow_Approach": "Day 7 embryo collection protocol: Flush with 500 ml warm lactated Ringer's solution (or Dulbecco's PBS) flushed through a Foley catheter inflated in the uterine horn. Collect the flushed fluid in an embryo filter (75 μm mesh). Search the filter under a stereomicroscope (10-25x magnification) for the embryo. Grade using IETS criteria (Grade 1-4). Load into a 0.25 ml embryo straw and transfer within 2 hours or cryopreserve in liquid nitrogen."
    },
    603: {
        "topic": "Primary Uterine Inertia - Most Common in Bitch and Cat",
        "Core_Anatomy": "The uterine myometrium (oxytocin receptors, calcium-dependent smooth muscle contraction), the placenta, and the fetal-maternal signalling at term.",
        "Pathogenesis_Immediate": "Primary Uterine Inertia (failure to initiate coordinated uterine contractions at term) is most commonly seen in Bitches and Cats among domestic species, typically associated with: small litter size (insufficient fetal pressure), obesity, old age, or breed-specific myometrial dysfunction.",
        "Pathogenesis_Deep": "Primary inertia mechanism: Despite term pregnancy (gestation complete, fetus in birth canal), the myometrium fails to generate sufficient coordinated contractions for fetal expulsion. Causes: (1) Small litter size (fewer fetuses = less corpus luteum support and less fetal pressure on the cervix for Ferguson's reflex). (2) Hypocalcaemia (reduced ionized calcium = impaired smooth muscle contraction). (3) Progesterone excess (persisting CL preventing myometrial activation). (4) Myometrial exhaustion in large litters.",
        "Why_Not": "Secondary inertia (cessation of contractions after labour began) is most common in large-litter polytocous species (pigs, dogs). Primary inertia (never started) is the bitch/cat-specific problem, whereas secondary inertia can occur in all species. Mares rarely have primary inertia (their powerful myometrial contraction mechanism is rarely deficient at term).",
        "Wow_Approach": "Manage primary inertia in bitches: (1) Confirm fetal viability (Doppler ultrasonography — fetal heart rate >150 bpm = alive). (2) Calcium gluconate 10% solution: 1-2 ml/kg IV slowly over 15 minutes (primes myometrium). (3) Oxytocin 0.5-2 IU IM (do not exceed 3 doses). (4) If no progress in 30 minutes: C-section. Do not delay C-section — fetal hypoxia from failed expulsion is rapidly fatal."
    },
    604: {
        "topic": "Large Superficial Cells Predominant at Oestrus in Canine Vaginal Cytology",
        "Core_Anatomy": "The stratified squamous vaginal epithelium, the differential cell layers (parabasal, intermediate, superficial), and the estrogenic stimulation of the vaginal mucosa.",
        "Pathogenesis_Immediate": "At oestrus in bitches, Large Superficial Cells (also called angular, cornified, or keratinized cells — anuclear or with pyknotic nuclei, angular edges) are the predominant cell type in vaginal cytology, indicating maximum estrogenic stimulation of the vaginal epithelium.",
        "Pathogenesis_Deep": "Canine vaginal cytology cell types and their correlation with cycle stage: Parabasal cells (small, round, large nucleus): Anestrus and early proestrus. Intermediate cells (medium sized, round, nucleus present): Mid-proestrus. Large Superficial (angular/cornified, small pyknotic nucleus): Oestrus (>90% superficial cells = oestrus). Transition back to intermediate/parabasal: Post-oestrus onset of dioestrus (first day >50% intermediate cells after oestrus = 'Day 1 of Dioestrus' = 6 days post-ovulation).",
        "Why_Not": "Neutrophils are absent at oestrus (estrogen suppresses neutrophil migration into the vagina). Neutrophils reappear in early diestrus, marking the end of oestrus. Parabasal cells indicate early proestrus or anestrus — low estrogen state. The appearance of large superficial cells specifically indicates peak estrogenic stimulation.",
        "Wow_Approach": "Vaginal cytology technique: Insert a cotton-tipped swab 3-4 cm cranial to the urethral orifice (no speculum needed). Roll the swab onto a glass slide. Fix with alcohol-based fixative or allow to air-dry. Stain: Diff-Quik (Romanowsky-type) or modified Papanicolaou. Count 100 cells: calculate % superficial. >80% superficial = oestrus confirmed. This inexpensive test can be performed in any small animal clinic."
    },
    605: {
        "topic": "Transverse Ventral Presentation - Most Common in Mares",
        "Core_Anatomy": "The equine uterus (T-shaped, large uterine body), the fetal body orientation in the large uterine cavity, and the pelvic inlet.",
        "Pathogenesis_Immediate": "Transverse Ventral Presentation (the fetal spine directed perpendicular to the birth canal with the ventral surface of the fetus toward the maternal pelvis) is the most common transverse presentation in Mares — due to the large, spacious equine uterine body that allows the long fetal body to rotate to a transverse orientation.",
        "Pathogenesis_Deep": "Equine transverse presentation: In the normal equine anterior presentation (dorsal position), the foal's forelimbs + head engage the pelvic canal. In transverse presentation, the foal lies ACROSS the uterus (spine perpendicular to the birth canal). Ventral transverse = fetal belly faces the cervix. Dorsal transverse = fetal back faces the cervix. Both are insoluble without fetotomy or C-section in most cases. The large equine uterine body provides enough room for the large fetus to adopt a transverse orientation, which is less possible in cattle (smaller uterus relative to fetal size).",
        "Why_Not": "Cows can have transverse presentations but the smaller bovine uterine body relative to fetal size makes this uncommon. In sows, the multiple fetuses in long uterine horns rarely allow transverse presentation. In ewes/queens, the small uterus precludes transverse orientation. Only in mares does the spacious T-shaped uterine body make transverse presentation a recognized clinical entity.",
        "Wow_Approach": "Management of equine transverse presentation: Attempt version (converting to anterior or posterior presentation) under deep sedation (xylazine 1.1 mg/kg IV + butorphanol 0.02 mg/kg IV) with the mare positioned in dorsal recumbency (increases uterine space). Generous intrauterine lubrication. If version fails after two attempts: proceed immediately to C-section (do not attempt partial fetotomy in transverse presentation — risk of uterine rupture is extreme)."
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
