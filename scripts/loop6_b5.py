import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    691: {
        "topic": "Reproductive Pathology - Metritis, Endometritis, and Salpingitis",
        "Core_Anatomy": "Endometrium, myometrium, oviductal mucosa, and pelvic peritoneum.",
        "Pathogenesis_Immediate": "Definitions of key inflammatory conditions in Theriogenology: Metritis is inflammation of all layers of the uterine wall (endometrium, myometrium, and serosa); endometritis is inflammation limited to the endometrium; salpingitis is inflammation of the oviduct.",
        "Pathogenesis_Deep": "These conditions represent progressive stages of reproductive tract infections. Metritis typically occurs postpartum (Stage 1-2 weeks), is acute, systemic (fever, toxemia), and involves gas-producing pathogens (Clostridium, Fusobacterium). Endometritis is chronic, subclinical or clinical, limited to the mucosa, and does not cause systemic disease but impairs embryonic survival. Salpingitis often arises secondary to ascending uterine infections, causing mucosal adhesions that block sperm/oocyte transport, leading to permanent sterility.",
        "Why_Not": "Vaginitis is inflammation of the vagina, which rarely affects fertility unless severe. Cervicitis is inflammation of the cervix. Neither of these causes systemic disease or direct mechanical blockage of fertilization like metritis or salpingitis do.",
        "Wow_Approach": "To diagnose subclinical endometritis in dairy cows at Day 30-40 postpartum, perform endometrial cytology using a Cytobrush. A neutrophil count >5% confirms subclinical endometritis, indicating the need for intrauterine therapies such as metricure (cephapirin) or prostaglandin injection."
    },
    699: {
        "topic": "VGO-I Course Syllabus - Female Infertility and Diagnostics",
        "Core_Anatomy": "Ovary, oviduct, uterus, cervix, and vagina.",
        "Pathogenesis_Immediate": "VGO-I covers the physiology of the female reproductive system and clinical diagnostics for non-pregnant female infertility.",
        "Pathogenesis_Deep": "The curriculum details clinical investigations of repeat breeding, ovarian cysts, anestrus, and repeat-breeder syndromic management. Practical sessions emphasize semen collection, transrectal palpation, B-mode ultrasonography of the reproductive tract, and therapeutic protocols for postpartum infections. Mastery of these fields is crucial for cattle and equine herd management.",
        "Why_Not": "Obstetrical techniques, fetal malpresentations, dystocia, fetotomy, and neonatal care are covered under VGO-II (Obstetrics), whereas VGO-I is strictly limited to female reproductive physiology, cyclic management, and gynaecological pathologies.",
        "Wow_Approach": "In the clinical examination, combine rectal palpation with real-time B-mode ultrasonography. Palpation identifies gross organ changes (size, symmetry, tone), while ultrasound identifies microstructures (follicle sizes, luteal cavities, subclinical uterine fluid), providing a comprehensive diagnosis."
    },
    700: {
        "topic": "VGO-I Subject - Core Reproductive Physiology Principles",
        "Core_Anatomy": "Hypothalamus, pituitary gland, ovary, and uterus.",
        "Pathogenesis_Immediate": "VGO-I introduces students to comparative reproductive biology, including the endocrine control of puberty, oestrous cycles, and early embryonic development in domestic animals.",
        "Pathogenesis_Deep": "Physiological principles include: (1) The dual-hormone control of the follicular phase (LH and FSH). (2) The negative and positive feedback mechanisms of estradiol on the hypothalamus. (3) The biochemical processes of luteolysis (PGF2alpha-mediated). (4) The mechanisms of maternal recognition of pregnancy (IFN-tau in ruminants, estrogens in pigs). These principles form the basis for artificial insemination and synchronization technologies.",
        "Why_Not": "Pathological parturition, dystocia handling, and uterine prolapse are taught in VGO-II, while VGO-I focuses strictly on establishing and maintaining the non-gravid physiological cycle and early embryonic phases.",
        "Wow_Approach": "To memorize species-specific features: group animals by cycle type. Ruminants and mares are spontaneous ovulators with short follicular phases, whereas queens and rabbits are induced ovulators with coitus-dependent LH surges. This simplifies clinical endocrinology."
    },
    701: {
        "topic": "TANUVAS Academic Regulations - Final Examination Guidelines",
        "Core_Anatomy": "N/A - Examination Protocols.",
        "Pathogenesis_Immediate": "TANUVAS guidelines dictate that Part-A (objective questions) must be completed within 30 minutes and handed over to the invigilator, with no descriptive answers allowed in this section.",
        "Pathogenesis_Deep": "This testing structure ensures a rapid, independent evaluation of factual recall in Theriogenology. Separating Part-A ensures that core knowledge of physiological values, gestation periods, hormone classes, and anatomical features is assessed without the use of descriptive cues from subsequent sections.",
        "Why_Not": "Part-B contains essays and short-answer clinical case questions, which are graded separately and require descriptive, structured answers over the remaining 2.5 hours of the exam.",
        "Wow_Approach": "When studying, practice rapid retrieval of core facts using flashcards. Developing immediate recall of normal reproductive values (e.g., canine proestrus length, equine follicle sizes) is essential for rapid diagnosis in busy veterinary hospitals."
    },
    702: {
        "topic": "Theriogenology Core Values - Reference Ranges in Farm Animals",
        "Core_Anatomy": "Comparative female reproductive tract.",
        "Pathogenesis_Immediate": "This section tests the normal reference ranges for the oestrous cycle, gestation, ovulation, and semen parameters across farm animals.",
        "Pathogenesis_Deep": "Key parameters include: (1) Gestation length: cow = 280 days, mare = 340 days, ewe/doe = 150 days, sow = 114 days, bitch = 63 days. (2) Oestrous cycle length: cow, mare, sow = 21 days; ewe = 17 days. (3) Semen parameters: minimum progressively motile sperm required for freezing in bulls is 30-35%. These values serve as the biological baseline for identifying pathology.",
        "Why_Not": "Pathological values (e.g., prolonged gestation or persistent cysts) cannot be correctly identified without first establishing these normal biological reference ranges for each species.",
        "Wow_Approach": "Apply the 'rule of thumb' for small ruminant gestation: 5 months (150 days). For sows: 3 months, 3 weeks, 3 days (114 days). This facilitates rapid clinical calculations during farm visits."
    },
    719: {
        "topic": "VGO Objective Section - Objective Examination Pattern",
        "Core_Anatomy": "HPG Axis and Female Organs.",
        "Pathogenesis_Immediate": "The objective section of VGO papers tests factual details: hormone biochemical structures, specific synchronization schedules, breed susceptibilities, and anatomical coordinates.",
        "Pathogenesis_Deep": "Topics tested include: the counter-current vascular transfer of PGF2alpha in ruminants, the site of fertilization (ampulla), the specific hormones responsible for maternal recognition (IFN-tau), and the exact cells producing progesterone (luteal cells). Rapid, precise recall is required to complete this section within the 30-minute exam window.",
        "Why_Not": "The descriptive section evaluates clinical therapeutics and procedural details (e.g., how to perform a C-section or correct a uterine torsion), whereas the objective section focus exclusively on basic biological facts.",
        "Wow_Approach": "Keep a high-yield study sheet listing the exact mechanism of action of common reproductive drugs (e.g., Cloprostenol as luteolytic, Buserelin as GnRH agonist, Dinoprost as myometrial stimulant) to quickly answer MCQ choices."
    },
    720: {
        "topic": "Maternal Recognition of Pregnancy (MRP) - IFN-tau in cows (Day 15-17)",
        "Core_Anatomy": "Trophectoderm (blastocyst), endometrial luminal epithelium, and corpus luteum.",
        "Pathogenesis_Immediate": "In the cow, maternal recognition of pregnancy (MRP) occurs between Days 15 and 17 post-ovulation, mediated by Interferon-tau (IFN-tau) secreted by the embryonic trophectoderm.",
        "Pathogenesis_Deep": "MRP prevents luteolysis to maintain the CL. Between Days 15 and 17, the elongated bovine blastocyst's trophectoderm secretes IFN-tau. IFN-tau binds receptors on the endometrial luminal epithelium, suppressing the transcription of oxytocin receptors (OTR). Without OTR, the pulsatile oxytocin from the CL cannot stimulate endometrial PGF2alpha release. The CL persists, and progesterone remains high, maintaining pregnancy. If this signal fails or is delayed, luteolysis occurs, and the embryo dies.",
        "Why_Not": "MRP does not occur on Day 20-21 (which is too late, as luteolysis would have already occurred on Day 16-17, resulting in estrus). In ewes, MRP occurs earlier (Days 12-14); in mares, it occurs on Days 12-16 via physical embryo migration.",
        "Wow_Approach": "Interferon-tau is a unique Type I interferon that lacks systemic antiviral toxicity but possesses potent immunosuppressive and anti-luteolytic properties. It is a key target in research aiming to reduce early embryonic death in high-producing dairy cows."
    },
    721: {
        "topic": "Blastocyst Hatching - Day 9-11 Post-Ovulation in Cows",
        "Core_Anatomy": "Blastocyst, trophectoderm cells, and the zona pellucida.",
        "Pathogenesis_Immediate": "In cattle, the blastocyst escapes (hatches) from the zona pellucida between Days 9 and 11 post-ovulation, allowing direct contact between the trophectoderm and the endometrial epithelium.",
        "Pathogenesis_Deep": "Hatching involves: (1) Upregulation of fluid accumulation in the blastocoel cavity, causing the blastocyst to expand and thinning the zona pellucida. (2) Secretion of trypsin-like proteolytic enzymes (plasminogen activators) by the trophoblast cells to digest the inner surface of the zona. (3) Rhythmic contractions of the blastocyst. The blastocyst eventually ruptures the weakened zona and emerges. Once hatched, it undergoes rapid elongation, growing from a 1 mm sphere to a 10-20 cm filamentous thread by Day 15.",
        "Why_Not": "Hatching does not occur on Day 2-4 (when the embryo is still in early cleavage in the oviduct). It does not occur on Day 5-6 (morula stage). The zona pellucida must remain intact until the embryo enters the uterus and reaches the expanded blastocyst stage on Day 8.",
        "Wow_Approach": "Hatching is a critical checkpoint for in-vitro embryo production (IVP). In-vitro embryos often show delayed or failed hatching due to a hardened zona pellucida caused by culture media. Assisted hatching using a laser or acid Tyrode's solution is sometimes used to improve pregnancy rates."
    },
    722: {
        "topic": "Fincher's Test - Diagnostic for Uterine Torsion in Cows",
        "Core_Anatomy": "Vagina, cervix, broad ligaments (mesometrium), and uterine body.",
        "Pathogenesis_Immediate": "Fincher's test is a transrectal and transvaginal palpation method used to diagnose Uterine Torsion in cows by identifying the characteristic twisting and tension on the broad ligaments.",
        "Pathogenesis_Deep": "Uterine torsion involves a rotation of the gravid uterus around its longitudinal axis. During rectal or vaginal palpation, Fincher's test reveals: (1) In a right-sided torsion (clockwise), the left broad ligament is pulled tightly across the dorsal aspect of the uterus toward the right, while the right ligament is under extreme tension and pulled ventrally. (2) The vagina shows spiral folds running in the direction of the torsion. Correct diagnosis of the torsion direction is required before attempting Schaffer's rolling method or surgical detorsion.",
        "Why_Not": "Fincher's test is not used to diagnose freemartinism (diagnosed using a vaginal probe or XX/XY karyotyping), cystic ovaries (diagnosed by rectal palpation/ultrasound showing structures >2.5 cm), or Gartner's cysts (palpable fluid-filled vestigial ducts in the vaginal floor).",
        "Wow_Approach": "To perform Fincher's test: insert a hand rectally and locate the broad ligaments. The ligament that is pulled tightly across the top of the uterus like a taut rope indicates the direction of the torsion (e.g., if the left ligament is pulled over the top toward the right, it is a right-sided torsion)."
    },
    723: {
        "topic": "Oviductal Fluid Regulation - Estrogen Domination",
        "Core_Anatomy": "Oviductal mucosa (ciliated and secretory cells) and the infundibulum/ampulla.",
        "Pathogenesis_Immediate": "The secretory activity and ciliary beat frequency of the oviductal epithelium are highly upregulated under the influence of Estrogen during the follicular phase (proestrus and oestrus).",
        "Pathogenesis_Deep": "Estrogen binds to receptors on oviductal cells, stimulating: (1) Secretory cells (peg cells) to produce oviductal fluid rich in glycoproteins, lactate, and pyruvate, which nourish the oocytes and spermatozoa. (2) Ciliated cells to increase ciliary beat frequency toward the uterus, facilitating gamete transport. (3) Hyperaemia and smooth muscle contractions of the oviduct wall. This optimal environment supports sperm capacitation, fertilization, and early zygote cleavage.",
        "Why_Not": "Progesterone dominates the luteal phase and pregnancy, reducing oviductal secretory activity and slowing ciliary transport, which is suboptimal for fertilization. Prostaglandin and inhibin do not directly regulate the trophic secretory activity of the oviduct.",
        "Wow_Approach": "Oviduct-specific glycoprotein 1 (OVGP1), also known as oviductin, is an estrogen-dependent protein that coats the oocyte and sperm, enhancing sperm binding to the zona pellucida and facilitating fertilization. Adding recombinant OVGP1 to IVF media significantly improves blastocyst yield."
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

# Database validation
with open(db_path, "r", encoding="utf-8") as f:
    c2 = f.read()
d2 = json.loads(re.sub(r'^.*?const examData = ', '', c2, flags=re.DOTALL).rsplit(';',1)[0].strip())
empty2 = [x for x in d2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]

print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
