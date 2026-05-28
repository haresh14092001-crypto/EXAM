import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    243: {
        "topic": "hCG for Treatment of Delayed Ovulation in Cattle and Buffaloes",
        "Core_Anatomy": "The dominant preovulatory follicle, the granulosa and theca cells, and the LH receptor system.",
        "Pathogenesis_Immediate": "hCG (human Chorionic Gonadotropin) is the drug of choice for treating delayed ovulation in cattle and buffaloes because it mimics the LH surge, binding LH receptors on the dominant preovulatory follicle to trigger ovulation within 24-48 hours of injection.",
        "Pathogenesis_Deep": "Delayed ovulation occurs when the endogenous LH surge is insufficient to trigger ovulation of the dominant follicle (common in buffaloes in summer and in high-producing early-lactation dairy cows). hCG (3,000-5,000 IU IV/IM) provides a supraphysiological LH-like stimulus that overcomes the LH deficiency, triggering follicular rupture, ovulation, and CL formation. The resulting CL produces progesterone, supporting pregnancy if AI was performed at or before the ovulation-inducing injection.",
        "Why_Not": "GnRH (Gonadorelin/Buserelin) also induces LH release and ovulation but acts indirectly (via the pituitary), requiring 30-60 minutes to generate adequate LH levels. hCG acts directly on the follicular LH receptors with immediate effect. PGF2alpha causes CL regression (luteolysis) — it would be used if there is a persistent CL, not for delayed ovulation of a mature follicle.",
        "Wow_Approach": "The Ovsynch protocol (GnRH Day 0 → PGF2alpha Day 7 → GnRH Day 9 → AI Day 10) uses GnRH twice to synchronize ovulation precisely. In buffaloes with high incidence of delayed ovulation in summer, substituting the second GnRH with hCG (5,000 IU) improves ovulation synchrony and conception rates by 8-12% compared to GnRH alone."
    },
    244: {
        "topic": "Cloprostenol - Synthetic Prostaglandin Analogue for Luteolysis",
        "Core_Anatomy": "The corpus luteum (FP prostaglandin receptor), the smooth muscle of the uterus and broad ligament vasculature.",
        "Pathogenesis_Immediate": "Cloprostenol (ICI-80996) is a synthetic analogue of PGF2alpha used for luteolysis (CL regression), estrus synchronization, and treatment of pyometra/luteal cysts in cattle. It is 100-300x more potent than natural dinoprost (PGF2alpha tromethamine).",
        "Pathogenesis_Deep": "Cloprostenol binds the FP (F-prostanoid) receptor on luteal cells with higher affinity and longer duration than natural PGF2alpha. Receptor binding activates Gq protein → phospholipase C → IP3-mediated calcium release → luteal cell vasoconstriction → ischaemic necrosis of luteal tissue → progesterone collapse within 48-72 hours. The cow returns to oestrus 48-96 hours post-injection.",
        "Why_Not": "Dinoprost (PGF2alpha tromethamine = natural PGF2alpha) is effective but requires higher doses (25-35 mg IM) vs Cloprostenol (0.5-1.0 mg IM). Gonadorelin (GnRH) triggers LH release causing ovulation — not luteolysis. Buserelin is also a GnRH analogue — used for ovulation induction, not CL regression.",
        "Wow_Approach": "Safety alert: Prostaglandin analogues (Cloprostenol, Dinoprost) are ABORTIFACIENT and cause potent bronchoconstriction. NEVER handle in pregnant women or asthmatics. Wear gloves; wash hands immediately if skin contact occurs. Accidental injection into humans causes intense abdominal cramping and bronchospasm requiring emergency hospital treatment."
    },
    245: {
        "topic": "Optimum Service-Per-Conception Ratio in Dairy Cattle",
        "Core_Anatomy": "The bovine cervix, uterine horns, and the spermatozoa-ovum fertilization site (ampullary-isthmic junction of the oviduct).",
        "Pathogenesis_Immediate": "The optimum Service-Per-Conception (SPC) ratio in a well-managed dairy cattle herd is 1.5–1.7. This means on average 1.5 to 1.7 inseminations are required for each successful pregnancy, reflecting a 60-67% first-service conception rate.",
        "Pathogenesis_Deep": "SPC = Total number of services ÷ Total number of conceptions. An ideal dairy herd targets: First-service conception rate (FSCR) of 55-65%, overall conception rate of 60%+, and SPC <1.7. Factors increasing SPC (worsening fertility): poor oestrus detection (<50% efficiency), poor AI technique, semen quality failures, heat stress, and subclinical endometritis reducing uterine receptivity.",
        "Why_Not": "An SPC of 2.0-2.2 indicates poor reproductive performance (conception rate ~45-50%), costing each repeat service approximately Rs.500-2000 in semen + labour + extended calving interval losses. An SPC >3.0 indicates a herd reproductive emergency requiring investigation of male fertility, semen quality, oestrus detection, or infectious disease.",
        "Wow_Approach": "Monitor herd fertility with three key performance indicators (KPIs): (1) Submission Rate (% of eligible cows inseminated in first 21 days of breeding). (2) Conception Rate (% of services resulting in pregnancy). (3) Pregnancy Rate = Submission Rate × Conception Rate. Target Pregnancy Rate >20% per 21-day cycle for optimal calving distribution."
    },
    246: {
        "topic": "Bovine Sperm Concentration Standards for AI",
        "Core_Anatomy": "The testicular seminiferous tubule (spermatogenic epithelium), the epididymis (sperm maturation and storage), and the accessory sex glands (sperm dilution).",
        "Pathogenesis_Immediate": "The standard sperm concentration in a frozen bull semen straw prepared for AI is 100 million sperm per ml (or 20-25 million progressively motile sperm per 0.5 ml straw after thawing), based on the minimum threshold for reliably achieving fertilization at the oviductal level.",
        "Pathogenesis_Deep": "Bull ejaculate concentration at collection: 800-1200 million sperm/ml. After dilution with Tris-egg yolk-glycerol extender, the final concentration per 0.5 ml straw is adjusted to 20-40 million total sperm (10-15 million progressively motile). Post-thaw quality criteria for commercial release: Progressive motility ≥35%, Morphologically normal sperm ≥70%, Acrosomal integrity ≥80%.",
        "Why_Not": "10,000 million/ml is the raw ejaculate concentration of some high-producing bulls — this is the pre-dilution concentration, not the AI-ready concentration. Diluting to 100 million/ml for AI allows a single ejaculate (5-10 ml) to yield 80-200 straws, maximising the genetic impact of a superior bull.",
        "Wow_Approach": "National Dairy Development Board (NDDB) AI Centre, Anand (Gujarat) processes over 60 million semen doses annually — the largest bovine semen production facility in Asia. NDDB has been instrumental in cross-breeding India's indigenous cattle with Holsteins and Jerseys through AI, revolutionising Indian dairy productivity."
    },
    254: {
        "topic": "National Dairy Research Institute (NDRI) - Location and Semen Production",
        "Core_Anatomy": "N/A — Institutional and regulatory knowledge for Indian veterinary science.",
        "Pathogenesis_Immediate": "The National Dairy Research Institute (NDRI), India's premier dairy research institution, is located in Karnal, Haryana. It conducts research in dairy science, animal breeding, nutrition, and reproductive biotechnology.",
        "Pathogenesis_Deep": "NDRI Karnal conducts research in: (1) AI and reproductive biotechnology (frozen semen production, embryo transfer, IVF). (2) Dairy cattle breeding (development of Karan Fries, Karan Swiss crossbreeds). (3) Milk processing and product development. (4) Animal nutrition and feed technology. NDRI has produced over 500 PhDs and is rated among the world's top dairy research institutions.",
        "Why_Not": "IVRI (Indian Veterinary Research Institute) is located in Izatnagar, Bareilly, UP — focuses on animal disease research and vaccine production. CIRG (Central Institute for Research on Goats) is in Makhdoom, Mathura. CSWRI (Central Sheep and Wool Research Institute) is in Avikanagar, Rajasthan. Each has a specific research mandate.",
        "Wow_Approach": "Key NDRI contributions to Indian dairy: Development of Karan Fries (HF × Tharparkar) and Karan Swiss (Brown Swiss × Sahiwal) crossbreeds optimized for Indian tropical conditions. NDRI's milk processing research gave India the shelf-stable UHT milk technology and Shrikhand process standardization. NDRI's bull semen bank stores frozen semen from >200 proven bulls."
    },
    391: {
        "topic": "Hippomanes - Allantoic Bodies in Equine Fetal Membranes",
        "Core_Anatomy": "The allantoic cavity, the allantochorion, and the allantoic fluid in equine pregnancy.",
        "Pathogenesis_Immediate": "Hippomanes are brownish, soft, rubbery, oval bodies (2-10 cm) found floating in the allantoic fluid of equine (and bovine) fetuses, composed of desquamated cells, mucus, and mineral deposits — a normal finding with no pathological significance.",
        "Pathogenesis_Deep": "Hippomanes form throughout gestation from the accumulation of fetal cellular debris, allantoin crystals, and mucoproteins shed from the allantoic and amniotic epithelium. In horses, they are consistently present (1-3 per fetus). The name 'hippomanes' comes from Greek (hippo = horse, mania = madness) — ancient Greeks incorrectly believed these bodies caused sexual frenzy in mares. The mare placenta expels hippomanes along with allantoic fluid at parturition.",
        "Why_Not": "Cystic ovary in cattle is an ovarian pathology, not a fetal membrane finding. Lithopedion is a calcified fetus (stone baby) from an ectopic/extra-uterine pregnancy — extremely rare. Hippomanes are strictly intra-allantoic, are soft (not calcified), and have no clinical significance when found at post-mortem or parturition examination.",
        "Wow_Approach": "When assisting equine parturition, identification of hippomanes expelled with the allantoic fluid confirms intact allantochorion passage. After equine delivery, always examine the expelled fetal membranes for completeness — weigh them (normal: 4-6 kg for a TB mare). If total weight is significantly less than expected, retained fetal membranes (RFM) are present."
    },
    392: {
        "topic": "Extra-Uterine (Ectopic) Pregnancy and Lithopedion Formation",
        "Core_Anatomy": "The peritoneal cavity, the abdominal organs (omentum, intestine, body wall), and the calcification process in dead fetal tissue.",
        "Pathogenesis_Immediate": "Extra-uterine (ectopic/abdominal) pregnancy occurs when a fertilized ovum implants outside the uterus (on peritoneum, omentum, or intestinal serosa) and the fetus dies, becoming mummified and calcified over time to form a Lithopedion (stone baby).",
        "Pathogenesis_Deep": "Ectopic pregnancy in domestic animals (rare, reported in cattle, sheep, horses): The fertilized egg escapes through a uterine rupture or migrates through the fallopian tube into the peritoneal cavity. The conceptus implants on the omentum or intestinal surface and may survive for several months before dying (no proper placentome formation). The dead fetus undergoes saponification and progressive calcium deposition over months to years, eventually forming a hard, mineralized mass (lithopedion) that can persist for years without clinical signs.",
        "Why_Not": "Mummification occurs within an intact uterus in a sterile environment. Lithopedion formation requires extra-uterine location where peritoneal calcium deposition can occur on the dead fetal body. Ascites is fluid accumulation in the peritoneal cavity — not related to ectopic pregnancy formation.",
        "Wow_Approach": "Clinical detection: Lithopedions are often incidental findings at necropsy or slaughter. In living animals, hard abdominal masses detectable on deep palpation or radiography should prompt differential for lithopedion vs intestinal neoplasia vs abscess. Ultrasound shows a highly echogenic mass with acoustic shadowing (calcification artifact)."
    },
    393: {
        "topic": "Gartner's Ducts - Embryological Remnant and Cyst Formation",
        "Core_Anatomy": "The Wolffian (Mesonephric) duct remnants in the lateral walls of the bovine vagina and uterus.",
        "Pathogenesis_Immediate": "Gartner's Ducts (Ductus Gartneriani) are paired vestigial remnants of the mesonephric (Wolffian) ducts in female domestic animals, running along the ventrolateral walls of the vagina. They normally regress completely but can persist as Gartner's Duct Cysts.",
        "Pathogenesis_Deep": "Embryological origin: In females, the Müllerian ducts form the uterus, cervix, and vagina. The Wolffian ducts (which form the male epididymis, vas deferens, and seminal vesicles) normally regress in the absence of testosterone. Incomplete regression leaves Gartner's Duct remnants in the lateral vaginal walls. These can fill with secretions to form Gartner's Duct Cysts — palpable on vaginal examination as soft, fluid-filled structures in the lateral vaginal walls.",
        "Why_Not": "Paramesonephric (Müllerian) duct remnants cause ovarian bursal cysts and periovarian cysts. Paraovarian cysts are derived from rete ovarii. Gartner's duct cysts are strictly mesonephric in origin and strictly located in the LATERAL VAGINAL WALL — a key anatomical distinguishing fact for exam MCQs.",
        "Wow_Approach": "Gartner's duct cysts in cattle are typically 2-5 cm, fluid-filled, thin-walled, and located 5-10 cm cranial to the vulvar commissure on the vaginal floor/lateral walls. They are usually asymptomatic but can occasionally cause dysuria or dystocia if very large. Treatment is marsupialization (creating a permanent opening) or surgical excision."
    },
    410: {
        "topic": "Hydroallantois vs Hydroamnion - Dropsy of Fetal Membranes in Bovines",
        "Core_Anatomy": "The allantochorion (allantoic cavity) and the amnion (amniotic cavity) of the bovine placenta.",
        "Pathogenesis_Immediate": "Hydroallantois (excessive accumulation of allantoic fluid, >100 litres) is the most common type of dropsy of fetal membranes in bovines, causing rapid abdominal distension over 2-4 weeks. Hydroamnion (excessive amniotic fluid, >20 litres) is rarer and accumulates more slowly.",
        "Pathogenesis_Deep": "Normal allantoic fluid volume in cattle at term: 8-15 litres. In hydroallantois, the volume can reach 100-200 litres. Pathogenesis: Placentomal dysfunction (failure of fluid reabsorption), allantochorion inflammation, or fetal renal agenesis causing excessive urinary output. The massive fluid accumulation causes: ventral abdominal distension, dyspnoea (diaphragm compression), anorexia, sternal recumbency, and limb oedema from pressure on abdominal vessels.",
        "Why_Not": "Hydroamnion is caused by failure of fetal swallowing (neural defects, oesophageal atresia) — the fetus cannot ingest amniotic fluid, causing progressive accumulation. In hydroallantois, the allantochorion is diseased; in hydroamnion, the fetal swallowing mechanism is defective. The two can be distinguished by transrectal ultrasonography: allantoic fluid is hypoechoic and uniformly distributed; amniotic fluid is around the fetus and normally slightly echogenic from fetal debris.",
        "Wow_Approach": "Emergency treatment for hydroallantois causing respiratory distress: slow, controlled tapping of the allantoic fluid by inserting a large-bore trocar through the vagina into the allantochorion. Release fluid SLOWLY (1 litre/minute) — rapid release causes acute cardiovascular collapse from sudden loss of intra-abdominal pressure. Follow immediately with an oxytocin drip to initiate labour."
    },
    411: {
        "topic": "Wry Neck (Torticollis) Dystocia - Most Common Species",
        "Core_Anatomy": "The fetal cervical vertebrae, the sternocleidomastoid and splenius muscles, and the birth canal.",
        "Pathogenesis_Immediate": "Wry Neck (torticollis/lateral deviation of the head and neck) dystocia occurs most frequently in SOWS (pigs), due to the combination of narrow pelvic dimensions, polytocous litter delivery, and the high incidence of congenital vertebral anomalies in pigs.",
        "Pathogenesis_Deep": "Wry Neck is a fetal malpresentation where the head is laterally flexed (deviated to one side), preventing entry into the birth canal because the fetal nose cannot be positioned on the forelimbs (normal anterior presentation). In anterior presentation with wry neck, the shoulder engages the pelvic inlet but the head blocks further descent. Correction: retropulsion (push fetus back), palpate and manually extend the neck, bring the muzzle forward onto the forelimbs, then apply traction.",
        "Why_Not": "Wry neck occurs in all species but is most commonly reported and most problematic in sows due to the small fetal pigs' propensity for congenital vertebral malformations and the narrow tubular porcine birth canal. In mares, wry neck is rarer because the single large foal usually presents in normal anterior position.",
        "Wow_Approach": "Wry neck in pigs is often bilateral ('snub-nosed' presentation where both the head AND legs are retained). Porcine obstetrical assistance requires a gloved arm introduced through the vulva — the sow's narrow vagina limits manipulation. Forceps delivery or careful traction with a snare around the lower jaw may be required for irreducible wry neck."
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
