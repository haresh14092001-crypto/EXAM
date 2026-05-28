import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    547: {
        "topic": "Diffuse Epitheliochorial Placentation in Mares",
        "Core_Anatomy": "The equine allantochorion (diffuse microvilli surface), the endometrial cup region, and the uterine luminal epithelium.",
        "Pathogenesis_Immediate": "The mare has a Diffuse (non-deciduate) Epitheliochorial placentation — microvilli from the chorioallantois interdigitate with endometrial microvilli over the ENTIRE chorionic surface (diffuse = no localized attachment zones).",
        "Pathogenesis_Deep": "Equine placentation characteristics: (1) Diffuse distribution — microvilli cover the entire chorioallantoic surface. (2) Epitheliochorial — trophoblast contacts maternal uterine epithelium directly; no invasion of maternal vessels. (3) Non-deciduate — no maternal decidual reaction; the uterine epithelium is NOT shed at parturition. (4) Endometrial cups — unique equine structures (Days 36-120) invade the endometrium to produce eCG (equine Chorionic Gonadotropin) for maintaining accessory CLs.",
        "Why_Not": "Cattle have Synepitheliochorial (modified epitheliochorial) placentation — cotyledonary. Carnivores (dogs, cats) have Endotheliochorial — zonary pattern. Rodents and humans have Haemochorial — the most invasive, with direct maternal blood contact. The mare's diffuse epitheliochorial is the least invasive after primates.",
        "Wow_Approach": "Endometrial Cups (unique to Equidae): Formed by primary trophoblast cells (chorionic girdle cells) that invade the endometrial stroma between Days 36-40. These cups produce eCG (Pregnant Mare Serum Gonadotropin — PMSG) from Days 40-120 of pregnancy. eCG has both FSH-like and LH-like activity, stimulating accessory CL formation in the mare (critical because the primary CL regresses by Day 60, and accessory CLs maintain progesterone until the placenta takes over progesterone production at Day 80-100)."
    },
    548: {
        "topic": "Cardinal Sign of Luteal Cyst - Anoestrus",
        "Core_Anatomy": "The corpus luteum (luteal cyst variant), the hypothalamic-pituitary-ovarian axis, and the uterine endometrium.",
        "Pathogenesis_Immediate": "Anoestrus (absence of oestrus cycles) is the cardinal clinical sign of Luteal Cysts in cattle — the thick-walled, progesterone-secreting cyst maintains persistently elevated progesterone, suppressing hypothalamic GnRH pulsatility and preventing follicular development and oestrus behaviour.",
        "Pathogenesis_Deep": "Luteal cysts (also called luteinized follicular cysts, thick-walled cysts >2.5 cm): Formed by incomplete luteinization of an anovulatory follicle — the follicular wall luteinizes partially but the cavity persists, producing progesterone. Elevated progesterone: (1) Suppresses GnRH pulse frequency (hypothalamic negative feedback). (2) Suppresses behavioural oestrus. (3) Promotes endometrial gland secretion but prevents follicular LH surge. Result: cow appears in permanent dioestrus (anestrous).",
        "Why_Not": "Follicular cysts (thin-walled, >2.5 cm, low progesterone) cause Nymphomania (continuous, persistent oestrus-like behaviour) due to continuous estrogen production without progesterone counter-regulation. Luteal cysts cause ANOESTRUS (opposite). This distinction is the most heavily tested cyst question in VGO.",
        "Wow_Approach": "Differential diagnosis by rectal palpation: Follicular cyst = thin-walled, turgid, fluid-filled, single large structure (fluctuant). Luteal cyst = thick-walled, firm-to-hard, ovoid, progesterone-producing. Confirm with serum progesterone: Follicular cyst = <1 ng/ml. Luteal cyst = >1 ng/ml (often 3-5 ng/ml). Treatment: Luteal cyst = PGF2alpha (to cause CL/cyst regression) → cow returns to oestrus in 3-5 days."
    },
    549: {
        "topic": "VGO True/False - Reproductive Physiology Statements",
        "Core_Anatomy": "Comparative reproductive physiology across species.",
        "Pathogenesis_Immediate": "Key True/False reproductive physiology statements: Sheep is a short-day breeder = TRUE. Cattle are induced ovulators = FALSE (spontaneous ovulators). Cats are induced ovulators = TRUE. Right ovary is more active in cattle = TRUE (approximately 60% of ovulations). Buffalo has the longest postpartum anestrus = TRUE (45-90 days vs 28-45 days in cattle).",
        "Pathogenesis_Deep": "Critical VGO True/False facts: The equine placenta is haemochorial = FALSE (epitheliochorial). Progesterone is required for nidation = TRUE (decidual reaction requires progesterone). Cryptorchid dogs are sterile = FALSE (unilateral cryptorchids are fertile from the descended testis; bilateral cryptorchids are sterile). Freemartin heifers have XX/XY chimerism = TRUE. The placenta produces progesterone in horses after Day 100 = TRUE (fetoplacental unit takes over from ovarian CL).",
        "Why_Not": "Common true/false traps: Boar ejaculate volume is larger than bull's = TRUE (boar = 200-500 ml; bull = 4-8 ml). The interestrus interval in dogs is 7 months = TRUE (proestrus + oestrus + dioestrus + anestrus = 6-9 months total cycle). Cats are polyoestrous in spring/summer = TRUE (long-day breeders).",
        "Wow_Approach": "VGO True/False examination strategy: When in doubt about a statement, apply the 'exception check': most reproductive statements are species-specific and the trap is applying cattle physiology to another species. Always identify the species first, then apply the species-specific parameters."
    },
    552: {
        "topic": "Sheep as Short-Day Breeders - Photoperiod Mechanism",
        "Core_Anatomy": "The retinohypothalamic tract, the suprachiasmatic nucleus (SCN), the pineal gland, and the hypothalamic arcuate nucleus.",
        "Pathogenesis_Immediate": "Sheep are classified as short-day breeders — their breeding season is triggered by decreasing daylength (increasing nighttime melatonin exposure) in autumn, and they enter seasonal anoestrus as days lengthen in spring.",
        "Pathogenesis_Deep": "Photoperiodic transduction: Retina detects daylength → retinohypothalamic tract → SCN (master circadian clock) → superior cervical ganglion → pineal gland. Melatonin synthesis is inhibited by light and stimulated by darkness. As nights lengthen (autumn), melatonin duration increases → activates melatonin receptors (MT1/MT2) on pars tuberalis cells → increases EY/TSHβ expression → activates hypothalamic dio deiodinase type 2 → increases T3 → activates RFRP-3/kisspeptin changes → GnRH activation → reproductive axis activation.",
        "Why_Not": "Horses (long-day breeders) become reproductively active in spring/summer (short nights). The mechanism is the inverse: short melatonin exposure → suppresses the reproductive inhibitory pathway → GnRH pulsatility increases. The fundamental pineal-melatonin mechanism is identical; it's the species-specific response to the melatonin signal duration that determines whether a species is a short-day or long-day breeder.",
        "Wow_Approach": "Artificial manipulation of photoperiod for sheep: (1) Advance breeding season (to August-September instead of October): Expose to 16h artificial light from April to July, then switch to natural short days — simulates an artificially early autumn. (2) Melatonin implants (18 mg subcutaneous Regulin® implant): Applied in June, provides prolonged melatonin signal, advances breeding season by 6-8 weeks."
    },
    555: {
        "topic": "LH Deficiency Causing Delayed Ovulation in Buffaloes",
        "Core_Anatomy": "The anterior pituitary LH-secreting gonadotrophs, the dominant preovulatory follicle (LH receptor), and the hypothalamic GnRH pulse generator.",
        "Pathogenesis_Immediate": "Deficiency of LH (inadequate preovulatory LH surge) is the primary cause of delayed ovulation in buffaloes, especially during the summer months when heat stress suppresses GnRH pulsatility and reduces pituitary LH content.",
        "Pathogenesis_Deep": "Normal ovulation requires a preovulatory LH surge of sufficient amplitude (>50 ng/ml in cattle) and duration (>5 hours). In heat-stressed buffaloes, cortisol (elevated by heat stress) inhibits hypothalamic GnRH pulse amplitude → reduced LH stores in the pituitary → the LH surge is inadequate to fully luteinize the dominant follicle → ovulation is delayed or fails → the follicle either undergoes atresia or luteinizes incompletely (luteal cyst formation).",
        "Why_Not": "FSH deficiency would impair follicular recruitment (anovulation from the beginning of the wave). LH deficiency specifically affects the final stage (ovulation) — follicles develop normally but fail to ovulate at the appropriate time. This is why hCG (LH-like) or GnRH (induces endogenous LH) effectively treats delayed ovulation — they supplement the inadequate endogenous LH signal.",
        "Wow_Approach": "Ovulation synchronization in buffaloes: The Ovsynch protocol (GnRH → 7d → PGF2alpha → 2d → GnRH → AI at 16-20h) has a 55-65% ovulation rate in well-managed buffaloes. Modified Ovsynch using progesterone priming (CIDR + Ovsynch) improves synchrony by ensuring optimal pituitary LH stores before the ovulatory GnRH injection — critical in lactating buffaloes."
    },
    560: {
        "topic": "VGO Matching - Hormones and Physiological Effects",
        "Core_Anatomy": "The corpus luteum (progesterone), the endometrium (fern pattern mucus), the anterior pituitary (FSH for superovulation), and the hypothalamus (GnRH).",
        "Pathogenesis_Immediate": "Key VGO matching pairs: Luteal Phase → Progesterone (dominant hormone). PGF2alpha → Luteolysis (CL regression). Fern Pattern → Cervical Mucus (oestrogen-stimulated mucus ferns on dried slide). Induced Ovulator → Cat/Rabbit (ovulation triggered by coitus). Whitten Effect → Male pheromone-induced cycle synchronization.",
        "Pathogenesis_Deep": "Fern Pattern (arborisation): Oestrogen stimulates high NaCl content in cervical mucus. When dried on a glass slide, the NaCl crystallizes in a distinctive fernlike (arborescent) pattern visible under low-power microscopy. This fern pattern is maximal at oestrus (peak estrogen) and absent during the luteal phase (progesterone reduces NaCl in mucus). Used as a simple, inexpensive oestrus indicator in cattle and mares.",
        "Why_Not": "Spinnbarkeit is a related but different cervical mucus test — it measures the elasticity (thread-forming ability) of mucus, which is also maximal at oestrus. Fern test measures crystallization pattern. Both are peak-oestrus indicators but via different physical properties of the mucus. The fern test requires dried slide preparation; Spinnbarkeit is done fresh on the examination glove.",
        "Wow_Approach": "Superovulation protocol using FSH: Administer declining doses of FSH (50-40-30-20 mg, twice daily) from Day 9-11 of the cycle. This floods the system with FSH → recruits all available follicles → multiple dominant follicles develop simultaneously. If properly timed with PGF2alpha and AI, 5-20 embryos can be collected from a single super-stimulated cow donor — the basis of commercial ET programs."
    },
    561: {
        "topic": "Luteal Phase Matching - Progesterone as Key Hormone",
        "Core_Anatomy": "The corpus luteum (large and small luteal cells), progesterone biosynthesis (LDL cholesterol → pregnenolone → progesterone), and progesterone receptors in the uterus.",
        "Pathogenesis_Immediate": "The Luteal Phase of the oestrous cycle is dominated by Progesterone secreted from the corpus luteum — progesterone suppresses oestrus behavior, promotes uterine secretion (histotroph/uterine milk for early embryo), and inhibits myometrial contractions.",
        "Pathogenesis_Deep": "Progesterone actions during the luteal phase: (1) Negative feedback on GnRH/LH pulse frequency → suppresses oestrus and ovulation. (2) Endometrial gland stimulation → increases uterine secretion of amino acids, energy substrates, and growth factors (uterine milk). (3) Cervical mucus: thick, viscous, impenetrable (mucus plug) → prevents ascending infection. (4) Myometrial quiescence → prevents premature expulsion of conceptus. (5) Downregulation of estrogen receptors (anti-estrogenic effect on behavior).",
        "Why_Not": "Estrogen dominates the follicular phase (proestrus/oestrus). FSH dominates the follicular recruitment phase. Inhibin (from granulosa cells) feeds back to suppress FSH during dominant follicle phase. Only progesterone specifically characterizes and dominates the luteal phase — matching 'Luteal Phase' to 'Progesterone' is a core VGO matching answer.",
        "Wow_Approach": "Progesterone supplementation (CIDR, 1.38 g progesterone intravaginal device) is used to: (1) Suppress oestrus during embryo transfer in recipients not yet in luteal phase. (2) Support early pregnancy in cows with inadequate CL function (short luteal phase). (3) Prime repeat-breeding cows (CIDR + Ovsynch) to ensure adequate pituitary LH stores. CIDR devices can be reused up to 3 times — each reuse releases ~60-70% of first-use progesterone."
    },
    562: {
        "topic": "PGF2alpha - Mechanism as Luteolytic Agent",
        "Core_Anatomy": "The corpus luteum (FP receptor, large luteal cells), the uterine endometrium (PGF2alpha synthesis), and the utero-ovarian counter-current blood transfer.",
        "Pathogenesis_Immediate": "PGF2alpha (Prostaglandin F2-alpha) causes Luteolysis (corpus luteum regression) by binding FP receptors on large luteal cells, causing vasoconstriction of the luteal vasculature and apoptosis of luteal cells, with a precipitous fall in progesterone production.",
        "Pathogenesis_Deep": "Luteolytic mechanism: Endometrial PGF2alpha → absorbed into the uterine venous drainage → counter-current transfer to the ovarian artery via the uteroovarian vascular plexus → reaches the CL in concentrations 100x higher than systemic blood → FP receptor binding → Gq protein activation → IP3-mediated calcium surge → PKC activation → luteal cell vasoconstriction → ischaemic necrosis → CL regression → progesterone collapse within 24-48 hours.",
        "Why_Not": "LH maintains the CL (luteotropic) — exogenous LH or hCG prolongs CL lifespan. Estrogen at the time of oestrus stimulates endometrial OTR (enabling the luteolytic cascade) but is not directly luteolytic. Progesterone from the CL suppresses its own luteolytic cascade (blocks OTR expression) — only when CL progesterone falls can the luteolytic mechanism begin.",
        "Wow_Approach": "The utero-ovarian counter-current vascular transfer of PGF2alpha is the key reason why unilateral hysterectomy (removal of one uterine horn) selectively abolishes the CL on the same side: the ipsilateral CL loses its PGF2alpha supply → persistent ipsilateral CL. This was proven by Wiltbank and Anderson (1958) in the classic bovine experiment that defined the uterine role in CL control."
    },
    563: {
        "topic": "Fern Pattern - Cervical Mucus Oestrus Indicator",
        "Core_Anatomy": "The cervical mucus glands (columnar secretory cells of the cervical canal), NaCl content, and the crystallization physics of NaCl in biological fluid.",
        "Pathogenesis_Immediate": "The Fern Pattern (arborisation) is observed in cervical mucus at oestrus — estrogen-stimulated cervical mucus has high NaCl content that forms characteristic fern-like (arborescent) crystals when a thin film of mucus is spread on a glass slide and allowed to air-dry.",
        "Pathogenesis_Deep": "Fern pattern physiology: At oestrus, peak estradiol → cervical mucus glands increase secretion volume and alter mucus biochemistry (↑NaCl, ↑water content, ↑Cl⁻ concentration, ↓viscosity). The high ionic content causes NaCl crystal formation in a dendritic (fernlike) pattern upon drying. The pattern is most pronounced at peak oestrus and completely absent during the luteal phase (progesterone → high viscosity, low NaCl, no fern pattern).",
        "Why_Not": "The fern pattern is used for oestrus detection in cattle, mares, and women (Billings/natural family planning method). It is NOT a pregnancy test. It is NOT indicative of infection (purulent discharge forms amorphous clumps, not ferns, on dried slides). The test is non-specific for the species — any high-estrogen state produces fern patterns.",
        "Wow_Approach": "Practical technique: Collect 1-2 drops of cervical mucus with a long cotton swab at the cervical os (after speculum insertion). Spread thinly on a glass slide. Allow to air-dry for 10-15 minutes. Examine under 10x microscope objective. Grade: Positive (full fern pattern) = peak oestrus. Intermediate = proestrus or late oestrus. Negative (amorphous) = luteal phase or pregnancy."
    },
    564: {
        "topic": "Induced Ovulators - Cat and Rabbit as Primary Examples",
        "Core_Anatomy": "The vaginal nerve endings (mechanoreceptors), the afferent nerve → hypothalamic GnRH neurons, and the preovulatory LH surge mechanism.",
        "Pathogenesis_Immediate": "Induced (Reflex) Ovulators are species in which ovulation is triggered by copulation (coitus-stimulated LH surge) rather than by a spontaneous, time-dependent LH surge. Primary veterinary examples: Cat (Felis catus) and Rabbit (Oryctolagus cuniculus).",
        "Pathogenesis_Deep": "Mechanism: Vaginal tactile stimulation during copulation → afferent nerve signals → spinal cord → hypothalamus → GnRH burst → pituitary LH surge within 30-120 minutes of mating → follicular rupture (ovulation) 24-30 hours after mating. Without mating (or equivalent stimulation), LH surge does not occur and the dominant follicle undergoes atresia. In cats, multiple matings (minimum 4-5) are needed for a reliable LH surge of sufficient amplitude to trigger ovulation.",
        "Why_Not": "Mnemonic for induced ovulators: 'CR-BF' = Cats, Rabbits, Bears, Ferrets (also mink and other mustelids). All farm animals (cattle, buffaloes, horses, sheep, goats, pigs) are spontaneous ovulators — the LH surge is triggered by the pre-ovulatory estrogen peak, not by mating.",
        "Wow_Approach": "Feline pseudopregnancy: A queen that mates with a vasectomized tom undergoes LH surge and ovulation → CL formation → pseudopregnancy (45-60 days) without conception. This is why vasectomized toms are used in cat breeding management to suppress repeated oestrous cycling and prevent queens from cycling continuously without conception (which predisposes to pyometra in cats)."
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
