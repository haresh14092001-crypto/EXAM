import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    663: {
        "topic": "Ovarian Bursa - Complete Encapsulation in the Bitch",
        "Core_Anatomy": "Ovary, infundibulum, mesosalpinx, and ovarian bursa.",
        "Pathogenesis_Immediate": "The ovaries are almost completely enclosed within a well-developed ovarian bursa (bursa ovarica) in the bitch, which prevents surgical or transvaginal access without incising the bursal wall.",
        "Pathogenesis_Deep": "The ovarian bursa is a peritoneal pouch formed by the mesosalpinx and mesovarium. In the bitch, it has a narrow, slit-like opening and contains a large amount of adipose tissue. This complete encapsulation ensures that when ovulation occurs, the oocyte is directly captured and guided into the infundibulum of the oviduct. In contrast, cows and mares have a highly open ovarian bursa, exposing the ovarian surface directly to the peritoneal cavity.",
        "Why_Not": "Cows have an open bursa where the ovary is easily accessible for rectal palpation or transvaginal aspiration. Sows have a partially open bursa. Mares have a unique ovarian bursa that only covers the ovulation fossa.",
        "Wow_Approach": "During canine ovariohysterectomy (OHE), the suspensory ligament must be broken to exteriorize the ovary. Identify the fatty ovarian bursa; the ovary lies completely within it. The clinician must check the bursa to confirm that the entire ovary, including the proper ligament, has been removed to prevent ovarian remnant syndrome."
    },
    664: {
        "topic": "Intercornual Ligament - Bovine Anatomy (Repeated MCQ)",
        "Core_Anatomy": "Uterine horns (cornua uteri), uterine body, and the intercornual ligament.",
        "Pathogenesis_Immediate": "The intercornual ligament is a key anatomical structure located at the bifurcation of the uterine horns, present only in the Cow.",
        "Pathogenesis_Deep": "In cows, the two uterine horns are held together caudally by a dorsal and a ventral intercornual ligament. The dorsal ligament is thicker and more prominent. These ligaments prevent the divergence of the uterine horns, maintaining their coiled shape. During rectogenital examination, the intercornual ligament serves as the primary anchor point for retracting the uterus.",
        "Why_Not": "Sows have long, free-floating, convoluted uterine horns without any connecting ligament. Bitches have long Y-shaped horns suited for litters, which are not bound together. Mares have T-shaped horns that branch off at right angles, lacking an intercornual ligament.",
        "Wow_Approach": "Palpating the intercornual ligament is the first step in bovine transrectal uterine retraction. Stabilization of the ligament allows the examiner to slide their fingers along the greater curvature of each horn to check for pregnancy or pathologies."
    },
    665: {
        "topic": "Short-Day Breeders - Sheep Seasonal Reproduction",
        "Core_Anatomy": "Retina, pineal gland, kisspeptin neurons, and GnRH surge center.",
        "Pathogenesis_Immediate": "Sheep are classic short-day breeders, entering their active breeding season during autumn and winter when day length decreases.",
        "Pathogenesis_Deep": "The photoperiodic mechanism relies on melatonin secretion by the pineal gland, which occurs exclusively during darkness. As day length shortens in autumn, the duration of nightly melatonin release increases. This prolonged melatonin signal acts on the hypothalamic kisspeptin neurons, stimulating pulsatile GnRH release. GnRH stimulates the pituitary to release LH and FSH, initiating follicular development and regular oestrous cycles.",
        "Why_Not": "Mares are long-day breeders that cycle in spring and summer. Sows are polytocous and cycle year-round. Cats are seasonal long-day breeders (cycling in spring/summer) and are induced ovulators.",
        "Wow_Approach": "To advance the lambing season, insert a melatonin implant (e.g., Regulin) subcutaneously in early summer. This simulates short days, triggering GnRH pulsatility and inducing oestrus 6-8 weeks earlier than the natural autumn breeding season."
    },
    666: {
        "topic": "Puberty in Buffaloes - Delayed Onset at 24-28 Months",
        "Core_Anatomy": "Hypothalamus, pituitary gland, ovaries, and adipose tissue.",
        "Pathogenesis_Immediate": "The age of puberty in the water buffalo (Bubalus bubalis) is typically 24-28 months under standard farm management, which is significantly later than in dairy cattle.",
        "Pathogenesis_Deep": "The delay in buffalo puberty is due to slower somatic growth rates, a higher sensitivity of the GnRH pulse generator to negative feedback from estradiol during prepubertal development, and seasonal heat stress. Puberty is reached when the animal achieves approximately 55-60% of mature body weight (typically 250-300 kg in buffaloes), allowing leptin from adipose tissue to stimulate the kisspeptin-GnRH-gonadotropin axis.",
        "Why_Not": "Dairy cattle reach puberty at 8-12 months. Sheep and goats reach puberty at 6-8 months. A 3-4 month range is typical of rodents or rabbits, not large ruminants.",
        "Wow_Approach": "Improve prepubertal heifer nutrition by feeding a high-protein, high-energy ration ('flushing') to accelerate daily weight gain. This allows buffalo heifers to reach the threshold weight and enter puberty by 18-20 months of age."
    },
    667: {
        "topic": "Klinefelter's Syndrome - XXY Chromosomal Aneuploidy",
        "Core_Anatomy": "Germ cells, seminiferous tubules, Leydig cells, and sex chromosomes.",
        "Pathogenesis_Immediate": "The XXY sex chromosome constitution is associated with Klinefelter's syndrome, leading to testicular hypoplasia and sterility in affected males.",
        "Pathogenesis_Deep": "Klinefelter's syndrome (47,XXY in humans, equivalent aneuploidy in animals) occurs due to non-disjunction of sex chromosomes during parental gametogenesis. Affected males have an extra X chromosome. Anatomically, they present with: small, firm hypoplastic testes, absence of spermatogenesis (sterility), and occasionally mild gynaecomastia. Leydig cells are abnormal, leading to low testosterone levels. It is documented in dogs, bulls, rams, and tricolor male cats.",
        "Why_Not": "Turner's syndrome is associated with a single X chromosome (XO), causing gonadal dysgenesis in females. Downer cow syndrome is a metabolic/musculoskeletal disorder, not a chromosomal abnormality.",
        "Wow_Approach": "In tricolor (calico or tortoiseshell) male cats, the XXY karyotype explains their unique coat pattern. The gene for orange/black coat color is X-linked; a male cat requires two X chromosomes (XXY) to express both colors, and these males are almost always sterile."
    },
    668: {
        "topic": "Biologic Half-Life of FSH - 2-5 Hours",
        "Core_Anatomy": "Pituitary gland, circulating plasma compartment, and hepatic/renal clearance pathways.",
        "Pathogenesis_Immediate": "The statement 'Biologic half-life of FSH is about 2-5 hours' is TRUE. FSH is rapidly cleared from the circulation compared to other gonadotropins.",
        "Pathogenesis_Deep": "Follicle-Stimulating Hormone (FSH) is a pituitary glycoprotein. Its metabolic half-life in cattle and sheep is short (2-5 hours) due to rapid hepatic clearance and renal excretion. This necessitates twice-daily injections when using pituitary-derived FSH extracts (e.g., Folltropin) for superovulation protocols. In contrast, equine Chorionic Gonadotropin (eCG), which has FSH-like activity in cattle, has a high sialic acid content that prevents rapid clearance, giving it a half-life of 20-26 hours.",
        "Why_Not": "If FSH had a longer half-life (like eCG), a single injection would suffice for superovulation. Its short half-life requires a twice-daily, declining 4-day injection protocol to maintain continuous follicular stimulation.",
        "Wow_Approach": "Superovulation Protocol: Inject pituitary FSH IM twice daily for 4 days in a declining dose (e.g., 50, 40, 30, 20 mg). This maintains elevated circulating FSH levels, preventing dominant follicle deviation and recruiting multiple preovulatory follicles."
    },
    673: {
        "topic": "Superovulation - Pituitary FSH as the Choice Hormone",
        "Core_Anatomy": "Ovarian follicles, granulosa cells, and pituitary FSH receptors.",
        "Pathogenesis_Immediate": "The statement 'The choice of hormone for superovulation is GnRH' is FALSE. The primary hormone of choice for superovulation in cattle embryo transfer programs is Follicle-Stimulating Hormone (FSH) or eCG.",
        "Pathogenesis_Deep": "Superovulation requires sustaining elevated levels of follicle-stimulating activity to rescue multiple subordinate follicles from atresia. Pituitary-derived FSH (or eCG) acts directly on FSH receptors on granulosa cells, stimulating the growth of multiple follicles. GnRH, on the other hand, causes a brief endogenous surge of LH and FSH to induce ovulation or luteinization of a single dominant follicle. It cannot stimulate multiple follicular growth waves.",
        "Why_Not": "GnRH is used to synchronize or induce ovulation at the end of a superovulation protocol, but FSH (or eCG) is the obligatory hormone used to recruit and grow the multiple follicles.",
        "Wow_Approach": "To superovulate a donor cow, administer pituitary FSH twice daily for 4 days starting on Day 9-11 of the estrous cycle. Inject PGF2alpha on the 3rd day of the FSH protocol to regress the corpus luteum, allowing the multiple follicles to mature and ovulate."
    },
    674: {
        "topic": "Chemical Pregnancy Tests - Cuboni and Amoroso Tests",
        "Core_Anatomy": "Placenta, maternal urinary system, and estrogen metabolites.",
        "Pathogenesis_Immediate": "Chemical tests for pregnancy rely on detecting specific hormone metabolites in body fluids. The Cuboni test is a chemical test used to diagnose pregnancy in mares by detecting elevated estrogen metabolites in urine.",
        "Pathogenesis_Deep": "In pregnant mares, the fetal gonads produce large amounts of dehydroepiandrosterone (DHEA), which the placenta converts into estrogens (estrone, equilin, equilenin). These estrogens are excreted in maternal urine starting around Day 120 of gestation. The Cuboni test involves adding concentrated hydrochloric acid and benzene to a urine sample, heating it, and observing under UV light. A green fluorescence indicates a positive result.",
        "Why_Not": "Progesterone assays are immunologic or competitive binding tests, not simple chemical reaction tests. B-mode ultrasonography is an imaging modality. PGF2alpha is a luteolytic hormone, not a diagnostic test.",
        "Wow_Approach": "The Cuboni test is highly reliable in mares from Day 120 to term. It is a cost-effective, simple laboratory method for verifying pregnancy in performance or draft horses where rectal palpation is difficult or risky."
    },
    675: {
        "topic": "Biologic Pregnancy Tests - Aschheim-Zondek and Galli-Mainini Tests",
        "Core_Anatomy": "Gonadotropin receptors, ovaries, and testes of laboratory animals.",
        "Pathogenesis_Immediate": "Biologic tests for pregnancy involve injecting animal serum or urine into immature or male laboratory animals (mice, rabbits, frogs) and observing gonadotropin-induced gonadal changes.",
        "Pathogenesis_Deep": "Historically significant biologic tests include: (1) The Aschheim-Zondek (A-Z) test: Inject patient urine into immature female mice; gonadotropins (hCG or eCG) induce follicular growth, luteinization, or ovulation. (2) The Friedman test: Uses immature female rabbits. (3) The Galli-Mainini test: Inject serum/urine into male frogs; gonadotropins cause rapid sperm release. These tests demonstrate the cross-species bioactivity of placental gonadotropins (eCG and hCG) on gonadal tissue.",
        "Why_Not": "Chemical tests (like Cuboni) rely on direct chemical reactions with estrogen metabolites, not biological tissue responses. ELISA and RIA are modern immunologic tests that utilize monoclonal antibodies, bypassing the need for live laboratory animals.",
        "Wow_Approach": "Biological assays paved the way for discovering gonadotropins. Today, they are replaced by rapid lateral-flow immunochromatographic assays (using anti-eCG or anti-PAG antibodies) that deliver highly accurate results in 10 minutes."
    },
    688: {
        "topic": "VGO-I Essay Guidelines - Clinical Problem Solving",
        "Core_Anatomy": "Reproductive organs, endocrine axes, and systemic health parameters.",
        "Pathogenesis_Immediate": "Descriptive and essay questions in VGO-I require detailed, structured clinical protocols covering repeat breeding, postpartum anestrus, cystic ovarian degeneration, and embryo transfer.",
        "Pathogenesis_Deep": "Final veterinary examinations require candidates to demonstrate deep clinical reasoning. For essays, structure answers systematically: (1) Etiology and pathophysiology. (2) Clinical signs and physical/rectal findings. (3) Diagnostic tools (rectal palpation, ultrasound, hormone profiles). (4) Treatment protocols (specific drugs, dosages, and administration schedules). (5) Prevention and herd-level management strategies.",
        "Why_Not": "Descriptive essays cannot be solved with simple bullet points or definitions. They require integrating anatomy, endocrinology, pathology, and therapeutics to formulate comprehensive herd health plans.",
        "Wow_Approach": "When writing an essay on Repeat Breeding: divide the etiology into fertilization failure vs early embryonic death, outline a diagnostic plan (vaginal discharge check, uterine biopsy, rectal ultrasound), and detail specific hormone therapies (GnRH at AI, progesterone CIDR post-AI)."
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
