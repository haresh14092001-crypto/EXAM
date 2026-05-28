import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    250: {
        "topic": "History of Artificial Insemination - Ivanoff and Cattle AI",
        "Core_Anatomy": "The bovine cervix, uterine body, and the artificial vagina (AV) collection apparatus.",
        "Pathogenesis_Immediate": "The first successful Artificial Insemination (AI) in cattle was performed by Russian physiologist Elias Ivanoff in the early 20th century, establishing the systematic scientific foundation for large-scale cattle AI programs worldwide.",
        "Pathogenesis_Deep": "Ivanoff (1899-1930s) developed the artificial vagina for semen collection, basic dilution extenders, and cervical/vaginal insemination techniques for horses and cattle. His work was expanded by Milovanov (USSR) who introduced rubber artificial vaginas and glycerol cryoprotection. The first AI organisation for cattle was established in Denmark (1936). India established its first AI centre in 1942 at Allahabad.",
        "Why_Not": "Lazzaro Spallanzani (1780) performed the first documented AI in a dog. Polge (1949) discovered glycerol as the first successful cryoprotectant for semen — enabling the global frozen semen industry. Salisbury developed practical AI protocols for dairy cattle in the USA. Ivanoff uniquely established the physiological protocols for commercial-scale cattle AI.",
        "Wow_Approach": "Modern cattle AI uses deep cornual insemination (placing the semen directly into the uterine horn ipsilateral to the dominant follicle using recto-vaginal technique). This targets 15-20 million progressively motile sperm per straw to maximize fertilization rates at the uterotubal junction."
    },
    251: {
        "topic": "Glycerol Concentration in Bull Semen Cryopreservation Extenders",
        "Core_Anatomy": "The sperm plasma membrane phospholipid bilayer, the acrosomal cap, and the mitochondrial sheath.",
        "Pathogenesis_Immediate": "The optimal final concentration of glycerol in Tris-egg yolk extenders for bovine semen cryopreservation is 7% (6-7%). This provides maximum cryoprotection against ice crystal formation without glycerol-induced cytotoxicity.",
        "Pathogenesis_Deep": "Glycerol (a triol alcohol) diffuses across the sperm plasma membrane due to its small molecular size. Inside the cell, it replaces intracellular water, reducing the amount available to freeze into damaging ice crystals. Externally, glycerol raises the osmolality of the extender, drawing additional water out of the cell (cryodehydration), further reducing intracellular ice formation during the freezing process to -196°C in liquid nitrogen.",
        "Why_Not": "At <5% glycerol: insufficient intracellular cryoprotection — ice crystals form inside the cell, rupturing the plasma membrane and acrosome. At >8% glycerol: direct cytotoxicity from osmotic shock and chemical membrane perturbation — sperm motility is chemically impaired. The 6-7% range is the narrow therapeutic window for optimal cryoprotection.",
        "Wow_Approach": "The equilibration time after adding glycerol is critical: Allow 4 hours at 4°C before freezing. This allows complete glycerol permeation into all sperm cells. Rush-freezing without equilibration causes patchy cryoprotection with high post-thaw mortality. Post-thaw quality standard: >35% progressive motility for release of a semen batch for field use."
    },
    252: {
        "topic": "Internal Pudendal Nerve Block for Penile Examination in Bulls",
        "Core_Anatomy": "The internal pudendal nerve, the retractor penis muscle, and the sigmoid flexure of the bull's penis.",
        "Pathogenesis_Immediate": "The Pudendal Nerve Block (Internal Pudendal Block) is the nerve block technique adopted for detailed examination of the penis in bulls, causing complete relaxation of the retractor penis muscle and protrusion of the penis without recumbency.",
        "Pathogenesis_Deep": "The internal pudendal nerve exits the sacral plexus through the greater sciatic foramen, curves around the sacrosciatic ligament, and passes through the lesser sciatic foramen to supply the penis and perineum. Injection of 20-30 ml of 2% Lignocaine through the ischiorectal fossa with a 14-gauge 18cm needle, guided rectally, blocks this nerve. Full penile protrusion occurs within 20-30 minutes, allowing examination for penile deviations, hematomas, persistent frenulum, and preputial adhesions.",
        "Why_Not": "Sciatic nerve block causes hindlimb motor paralysis and collapse — dangerous in standing bulls. Obturator nerve block prevents adduction of the hindlimb (useful for hip surgery, not penile examination). Sacral epidural block causes tail/perineal anaesthesia but less reliable penile protrusion than the targeted pudendal block.",
        "Wow_Approach": "A simpler field alternative: Acepromazine (0.05-0.1 mg/kg IM) causes penile relaxation by blocking alpha-1 adrenergic receptors of the retractor penis muscle smooth muscle — but without analgesia. The pudendal block provides both relaxation AND complete penile anaesthesia, allowing surgical intervention on the penis without general anaesthesia."
    },
    253: {
        "topic": "Phallocampsis - Penile Deviation Classification",
        "Core_Anatomy": "The corpus cavernosum penis, the tunica albuginea, and the dorsal apical ligament of the bull penis.",
        "Pathogenesis_Immediate": "Phallocampsis is the general term for any abnormal curvature or deviation of the erect penis. The most clinically important form is spiral deviation (corkscrew penis) in bulls, caused by failure of the dorsal apical ligament to maintain the penis in the straight position during erection.",
        "Pathogenesis_Deep": "During erection, the corpus cavernosum fills with blood under pressures exceeding 14,000 mmHg. Normally the dorsal apical ligament (DAL) limits differential expansion of the corpus cavernosum, maintaining straightness. When the DAL is congenitally weak or slips to the left side of the penile apex, the penis spirals left during full erection. Ventral deviation results from congenitally shortened DAL. In-Sheath deviation results from preputial adhesions restricting normal protrusion.",
        "Why_Not": "Phimosis = inability to protrude the penis from the prepuce (due to preputial stenosis). Paraphimosis = inability to retract the penis back into the prepuce (due to penile oedema or preputial ring swelling). Phallocampsis = abnormal direction of an already protruded, erect penis.",
        "Wow_Approach": "Spiral deviation is highly heritable (polygenic) — affected bulls should be permanently culled from natural service. Surgical correction success rate is moderate (50-60% return to fertility). Collect semen by electroejaculation for AI use while the bull undergoes surgical assessment — maximizes genetic value even if natural service is compromised."
    },
    255: {
        "topic": "Anton Van Leeuwenhoek - First Observation of Spermatozoa (1677)",
        "Core_Anatomy": "Basic mammalian sperm cell structure: head (nucleus + acrosome), midpiece (mitochondria), and flagellum (axoneme 9+2 microtubule arrangement).",
        "Pathogenesis_Immediate": "Anton Van Leeuwenhoek first observed and described spermatozoa from human and canine semen in 1677 using his hand-crafted single-lens microscopes (magnification up to 270x), calling them 'animalcules' and correctly identifying their motility.",
        "Pathogenesis_Deep": "Leeuwenhoek ground his own biconvex glass lenses to achieve unprecedented magnifications. He described the sperm head and tail accurately in his letters to the Royal Society of London. His observations disproved the prevailing preformationist theory that semen was merely a vaporous spirit. However, the role of sperm in fertilization was only proven by Spallanzani (1780) through filtration experiments showing that filtered seminal fluid (no spermatozoa) was infertile.",
        "Why_Not": "William Harvey (1628) described the circulation of the blood. Charles Darwin (1859) proposed the theory of evolution by natural selection. Neither was involved in the discovery of spermatozoa. Spallanzani (1729-1799) proved spermatozoa were necessary for fertilization — a different milestone from Leeuwenhoek's first observation.",
        "Wow_Approach": "Leeuwenhoek's microscopy also revealed bacteria ('animalcules' in dental plaque), protozoa, and red blood cells. His discovery of spermatozoa initiated the study of andrology. Today, Computer-Assisted Semen Analysis (CASA) tracks individual sperm cells at 60+ frames/second, analysing the same structures Leeuwenhoek sketched by hand 350 years ago."
    },
    256: {
        "topic": "Scrotal Circumference Standards in Breeding Soundness Evaluation",
        "Core_Anatomy": "The testicular parenchyma (seminiferous tubules + interstitium), epididymis, and scrotal skin and thermoregulatory structures.",
        "Pathogenesis_Immediate": "Normal scrotal circumference (SC) for an adult bull (>24 months) is a minimum of 34 cm, measured at the widest point using a standardised scrotal tape. SC directly correlates with daily sperm production and sire fertility.",
        "Pathogenesis_Deep": "Scrotal circumference is the single most objective and heritable parameter in Breeding Soundness Evaluation (BSE). Each 1 cm increase in SC correlates with approximately 2 million additional sperm produced per day. Heifers sired by large-scrotal bulls reach puberty 15-20 days earlier (h² for this trait = 0.50) — SC is a marker for reproductive efficiency across generations.",
        "Why_Not": "A 28 cm SC indicates testicular hypoplasia or early degeneration — this bull should fail the BSE minimum SC standards for his age class (<30 cm at 12-14 months, <31 cm at 15-17 months, <32 cm at 18-20 months, <34 cm at >24 months — Society for Theriogenology standards). An 18 cm SC is grossly abnormal indicating severe testicular pathology.",
        "Wow_Approach": "Always measure SC using a spring-loaded scrotal tape (not a rigid ruler), measuring the widest circumference of both testes together inside the scrotum. Pull the testes firmly downward into the scrotum before measuring to exclude scrotal skin folds. Re-measure twice and use the mean of three measurements for accuracy."
    },
    257: {
        "topic": "Testicular Descent in Dogs - Timing and Cryptorchidism",
        "Core_Anatomy": "The inguinal canal (inguinal rings, cremaster muscle), gubernaculum testis, and the scrotum.",
        "Pathogenesis_Immediate": "In dogs, the testes normally descend from the abdominal cavity through the inguinal canal into the scrotum within 1 month after birth (by 6-8 weeks post-partum). Failure to descend by 8 weeks of age = cryptorchidism.",
        "Pathogenesis_Deep": "Testicular descent is controlled by the gubernaculum (guided by INSL3 and testosterone). In dogs, testes are in the abdominal cavity at birth, pass through the inguinal canal in the first 2 weeks, and reach the scrotum by 4-8 weeks. Cryptorchid testes trapped in the abdomen (40-75°C higher temperature) fail to produce viable sperm (spermatogenic arrest at primary spermatocyte stage) but continue producing testosterone (so the dog has normal libido and secondary sexual characteristics).",
        "Why_Not": "In bulls and rams, testicular descent is complete by mid-gestation in utero — calves and lambs are born with testes already in the scrotum. In horses (colts), testes descend into the scrotum shortly before birth. In dogs uniquely, descent is post-natal and can be monitored during the puppy examination period.",
        "Wow_Approach": "Cryptorchid dogs have a 10-14x higher risk of developing testicular cancer (primarily Sertoli Cell Tumour causing feminization syndrome, and Seminoma). The retained testis should be surgically removed even if unilateral (the descended contralateral testis can be used for breeding but the cryptorchid gene must NOT be propagated). Bilateral cryptorchids are sterile."
    },
    259: {
        "topic": "IFN-tau and Luteolysis Prevention in Ruminant Pregnancy",
        "Core_Anatomy": "The fetal trophectoderm cells, the uterine luminal and glandular epithelium, and the corpus luteum.",
        "Pathogenesis_Immediate": "Interferon-tau (IFN-tau) is the trophoblastic signal produced by the ruminant conceptus (Days 15-17 in cows) that prevents luteolysis by blocking endometrial PGF2alpha release, maintaining the corpus luteum and progesterone production for pregnancy.",
        "Pathogenesis_Deep": "The elongating trophoblast produces IFN-tau in massive quantities. IFN-tau acts on type I interferon receptors on the luminal endometrial epithelium, activating JAK-STAT signalling and suppressing estrogen receptor (ER-alpha) expression. Without ER-alpha, the endometrium cannot respond to estrogen to upregulate oxytocin receptors (OTR). Without OTR, the pulsatile oxytocin-PGF2alpha cycle cannot initiate, so the CL is preserved and progesterone levels remain high, sustaining the pregnant state.",
        "Why_Not": "In pigs, MRP is mediated by trophoblastic estrogen redirecting PGF2alpha secretion luminally. In horses, the spherical embryonic vesicle physically migrates throughout the uterine horns to prevent PGF2alpha release mechanically. In ruminants, IFN-tau is the specific molecular signal — a uniquely elegant biochemical mechanism.",
        "Wow_Approach": "IFN-tau has been investigated therapeutically: intrauterine infusion of recombinant bovine IFN-tau around Day 15-17 post-AI in repeat-breeding cows may extend CL lifespan and reduce early embryonic death rates. Early results are promising for improving conception rates in high-producing dairy cattle."
    },
    260: {
        "topic": "Luteolysis and the Bovine Estrous Cycle Hormonal Events",
        "Core_Anatomy": "The corpus luteum (CL), the uterine endometrium, and the counter-current vascular exchange between uterine vein and ovarian artery.",
        "Pathogenesis_Immediate": "Luteolysis (regression of the corpus luteum) in cows occurs on Days 16-17 of the estrous cycle, triggered by pulsatile PGF2alpha release from the endometrium, causing a precipitous drop in progesterone and return to follicular phase.",
        "Pathogenesis_Deep": "The luteolytic cascade: Late diestrus oxytocin (from the CL) binds endometrial OTR → activates phospholipase A2 → releases arachidonic acid → COX-2 converts to PGF2alpha → PGF2alpha passes via counter-current exchange from the uterine vein to the ovarian artery → reaches the CL → binds FP receptors on luteal cells → intracellular calcium surge → luteal cell apoptosis → progesterone collapses to baseline.",
        "Why_Not": "Counter-current exchange between the uterine vein and ovarian artery is UNIQUE to ruminants, allowing locally produced PGF2alpha to reach the CL in concentrations 100x higher than systemic blood. This system fails in horses (no counter-current exchange) — equine PGF2alpha must reach the CL via systemic circulation. This is why much higher doses of exogenous PGF2alpha are needed in horses vs cattle.",
        "Wow_Approach": "Clinical implication: Hysterectomy in cattle permanently prevents luteolysis — the CL persists for months (Persistent CL syndrome) without the uterine PGF2alpha signal. This definitively proves that the uterus controls luteal lifespan in ruminants — the classic Wiltbank and Anderson (1958) experiment that transformed reproductive biology."
    },
    384: {
        "topic": "Ovarian Morphology During Anestrus in Cattle and Buffaloes",
        "Core_Anatomy": "The ovarian cortex, the absence of follicular or luteal structures, and the fibrous ovarian stroma.",
        "Pathogenesis_Immediate": "During anestrus (reproductive inactivity), the ovaries are small, smooth, and flaccid — containing no developing follicles, no dominant follicle, and no corpus luteum, because GnRH pulse frequency is insufficient to drive follicular wave development.",
        "Pathogenesis_Deep": "In anestrus (caused by negative energy balance, lactational suppression, seasonal photoperiod, or pathological causes), the hypothalamic GnRH pulse generator operates at low frequency (<1 pulse/hour). Without adequate LH pulsatility, follicular waves either fail to initiate or fail to produce a dominant follicle. The ovary remains small (2-3 cm in cattle), smooth-surfaced, and firm-to-flaccid in consistency — no palpable structures on rectal examination.",
        "Why_Not": "Cystic Ovarian Disease (follicular or luteal cysts) presents with large (>2.5 cm), turgid, fluid-filled structures palpable rectally. Persistent CL presents with a firm, rubbery structure on the ovary. Anestrus ovaries are specifically smooth AND flaccid — no structures at all.",
        "Wow_Approach": "Differentiate anestrus from quiet heat by two rectal examinations 10-14 days apart: in anestrus, both examinations show inactive smooth ovaries; in quiet heat, the second exam shows a CL from a missed silent ovulation. Treat nutritional anestrus with a steaming-up diet (increased concentrate feeding 2-3 weeks before service)."
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
