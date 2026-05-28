import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    652: {
        "topic": "Induced Ovulators - Cat, Rabbit, and Ferrets",
        "Core_Anatomy": "Vaginal sensory mechanoreceptors, pelvic nerve, and hypothalamic GnRH neurosecretory cells.",
        "Pathogenesis_Immediate": "Spontaneous ovulation does not occur in induced (reflex) ovulators such as cats, rabbits, and ferrets. In these species, physical coitus is required to stimulate the neuroendocrine reflex that triggers the preovulatory LH surge.",
        "Pathogenesis_Deep": "Unlike spontaneous ovulators (cows, ewes, mares) where rising estrogen reaches a threshold that triggers the GnRH/LH surge, induced ovulators require sensory vaginal stimulation. The mechanical stimulus activates pelvic sensory afferents, which transmit signals through the spinal cord to the GnRH surge center in the hypothalamus. This induces a GnRH pulse, causing an LH surge. Without mating, mature follicles fail to ovulate and instead degenerate into anovulatory follicular waves.",
        "Why_Not": "Cats, rabbits, and ferrets are all classic induced ovulators. None of them undergo spontaneous ovulation under normal physiological conditions, meaning 'All of the above' is the correct answer.",
        "Wow_Approach": "To induce ovulation artificially in laboratory or breeding settings for these species, administer a GnRH analogue (e.g., 2.5 mcg Buserelin) or hCG (100-250 IU), or use a sterile glass rod to mechanically stimulate the vagina."
    },
    654: {
        "topic": "Luteotropic Hormones - LH and Prolactin",
        "Core_Anatomy": "Pituitary gland, luteal cells, and corpus luteum receptors.",
        "Pathogenesis_Immediate": "Luteinizing Hormone (LH) is the primary luteotropic hormone in most domestic species, responsible for maintaining the corpus luteum (CL) and stimulating progesterone secretion.",
        "Pathogenesis_Deep": "Luteotropic support varies by species: (1) In cows and ewes, LH is the primary luteotropin, acting through cAMP-mediated pathways to stimulate progesterone synthesis in luteal cells. (2) In bitches and rodents, prolactin acts synergistically with LH to maintain the CL. (3) In mares, LH support is critical, and during mid-gestation, eCG provides additional LH-like luteotropic support to maintain accessory corpora lutea.",
        "Why_Not": "FSH stimulates follicular recruitment and growth, not the CL. Oxytocin is luteolytic in ruminants (via endometrial PGF2alpha stimulation) and acts as a uterotonic, not a luteotropic hormone.",
        "Wow_Approach": "hCG has potent LH-like activity in domestic animals due to binding the same LH receptor. It is clinically used as an exogenous luteotropic agent post-AI to support CL function and prevent early embryonic death."
    },
    655: {
        "topic": "Fertilization Failure - Etiology in Domestic Animals",
        "Core_Anatomy": "Oviductal ampulla, infundibulum, spermatozoa, and the cumulus-oocyte complex.",
        "Pathogenesis_Immediate": "Failure of fertilization can be caused by multiple factors, including ovulatory failure, anatomical oviductal blockage (salpingitis), or poor quality/non-viable semen.",
        "Pathogenesis_Deep": "The fertilization process requires: (1) Release of a viable oocyte (ovulation). (2) Capture of the oocyte by the infundibulum. (3) Transport of healthy, capacitated sperm to the ampullary-isthmic junction. (4) Penetration of the zona pellucida. Failure at any of these steps prevents zygote formation. Common causes include: delayed ovulation (oocyte ages before sperm arrive), salpingitis or oviductal adhesions (physically blocking sperm/oocyte transport), and substandard semen (low motility or high morphological defects).",
        "Why_Not": "Fertilization failure is rarely due to a single isolated factor. An ovulatory failure, oviductal blockage, or poor semen quality can individually cause complete failure, making 'Any one of the above' the correct etiology.",
        "Wow_Approach": "To distinguish fertilization failure from early embryonic death (EED) in repeat-breeding cows: perform non-surgical uterine flushing on Day 7 post-AI. Finding an unfertilized oocyte (UFO) confirms fertilization failure, whereas finding a degenerate or retarded embryo indicates early embryonic death."
    },
    656: {
        "topic": "Pseudocyesis - Canine Pseudopregnancy",
        "Core_Anatomy": "Mammary glands, hypothalamic prolactin-secreting lactotrophs, and persistent corpora lutea.",
        "Pathogenesis_Immediate": "Pseudocyesis (pseudopregnancy or false pregnancy) with prominent milk secretion and maternal behavior is a common physiological condition in the bitch.",
        "Pathogenesis_Deep": "Canine pseudopregnancy is unique because the non-pregnant bitch maintains functional corpora lutea and elevated progesterone levels for 60-70 days post-estrus, which is identical to the gestation period of a pregnant bitch. As the CL regresses at the end of diestrus, progesterone drops, and the pituitary releases prolactin. In sensitive bitches, this prolactin surge triggers mammary gland development, milk synthesis (lactogenesis), and nesting/maternal behavior, even in the absence of fetuses.",
        "Why_Not": "Cows, sows, and ewes do not routinely exhibit overt clinical pseudocyesis with lactation because their oestrous cycles are short (17-21 days) due to active luteolysis in non-pregnant cycles, preventing prolonged progesterone exposure.",
        "Wow_Approach": "Treatment of severe pseudocyesis: Administer a dopamine agonist such as Cabergoline (5 mcg/kg orally once daily for 5-7 days). Dopamine inhibits pituitary prolactin secretion, rapidly resolving lactation and behavioral signs. Avoid physical stripping of mammary glands, as tactile stimulation triggers further prolactin release."
    },
    657: {
        "topic": "Prolactin - Initiation and Maintenance of Lactation",
        "Core_Anatomy": "Pituitary gland (anterior lobe lactotrophs), mammary alveolar epithelial cells, and JAK/STAT pathways.",
        "Pathogenesis_Immediate": "Prolactin is the primary pituitary hormone responsible for the initiation (lactogenesis) and maintenance (galactopoiesis) of lactation in domestic species.",
        "Pathogenesis_Deep": "Lactation regulation involves a complex endocrine cascade: (1) Prolactin binds receptors on mammary alveolar epithelial cells, activating the JAK2/STAT5 signaling pathway to upregulate milk protein gene transcription (casein, alpha-lactalbumin). (2) In ruminants, Growth Hormone (GH/Somatotropin) is more critical for the maintenance of lactation (galactopoiesis) than prolactin, acting by partitioning nutrients toward the mammary gland. (3) In monogastric species (bitches, sows), prolactin remains the key hormone for both initiation and maintenance.",
        "Why_Not": "FSH and LH regulate ovarian follicular growth and ovulation, having no direct role in mammary lactogenesis. Estrogen stimulates mammary duct development during puberty and pregnancy but inhibits active milk synthesis when present in high concentrations.",
        "Wow_Approach": "Recombinant bovine somatotropin (rBST) is used in dairy cattle to increase milk yield by 10-15% by enhancing nutrient partitioning toward the mammary gland, whereas prolactin inhibitors are used in small animals to treat pseudopregnancy."
    },
    658: {
        "topic": "Progesterone - Secretion by the Corpus Luteum",
        "Core_Anatomy": "Corpus luteum, large and small luteal cells, and mitochondria.",
        "Pathogenesis_Immediate": "The corpus luteum (CL) is the primary endocrine gland responsible for the secretion of progesterone, which is essential for establishing and maintaining pregnancy.",
        "Pathogenesis_Deep": "Following ovulation, the remnants of the Graafian follicle undergo luteinization under the influence of LH: (1) Theca interna cells differentiate into small luteal cells. (2) Granulosa cells differentiate into large luteal cells. These cells actively convert cholesterol to pregnenolone inside the mitochondria, which is then converted to progesterone in the smooth endoplasmic reticulum. Progesterone acts on the endometrium to stimulate histotroph secretion and induces myometrial quiescence.",
        "Why_Not": "Prolactin is a pituitary peptide hormone, not a steroid secreted by the CL. PGF2alpha is a uterine-derived fatty acid that regresses the CL. Pregnenolone is an intermediate precursor, not the primary secreted hormone.",
        "Wow_Approach": "A functional CL is the sole source of progesterone during early gestation in all domestic species. In cows, goats, and sows, the CL is required throughout the entire pregnancy; in mares and ewes, the placenta takes over progesterone production by mid-gestation."
    },
    659: {
        "topic": "Bovine Ovulation - Timing Post-Oestrus End (Repeated High-Yield)",
        "Core_Anatomy": "Preovulatory Graafian follicle, follicular apex, and theca externa.",
        "Pathogenesis_Immediate": "Ovulation in the cow occurs on average 10-12 hours (or 8-10 hours) after the end of standing oestrus, making the cow a post-oestrus ovulator.",
        "Pathogenesis_Deep": "Cattle are unique among domestic farm animals because ovulation occurs after the cow has gone out of heat. High estradiol during oestrus triggers the GnRH and LH surges. The LH surge initiates a cascade of inflammatory changes, proteolysis of the follicular wall, and contraction of theca externa cells. Because this physical rupture takes ~30 hours from the LH surge, it occurs after standing oestrus behavior has ceased, during early metoestrus.",
        "Why_Not": "Mares ovulate 24-48 hours before the end of oestrus (ovulating during heat). Ewes ovulate near the end of oestrus. Ovulating in mid-oestrus is typical of sows. The post-oestrus timing is a bovine-specific feature.",
        "Wow_Approach": "AM-PM Rule: Inseminate cows approximately 12 hours after the onset of standing oestrus. This ensures that a population of viable, capacitated sperm is present in the oviduct when ovulation occurs 10-12 hours after heat ends."
    },
    660: {
        "topic": "Equine Oestrus - Average Duration of 6 Days",
        "Core_Anatomy": "Preovulatory follicles, endometrial mucosa, and the vagina/cervix in mares.",
        "Pathogenesis_Immediate": "The average duration of oestrus (heat) in the mare is 6 days (range of 4-8 days), which is significantly longer than in other domestic farm animals.",
        "Pathogenesis_Deep": "The mare's prolonged oestrus is characterized by slow follicular maturation and a gradual, prolonged LH surge. During this time, the cervix is relaxed and vascular, vaginal secretions are abundant, and the mare shows behavioral signs of receptivity (winking, tail raising, squatting, urinating). Ovulation occurs 24-48 hours before the end of oestrus, after which the mare rapidly goes out of heat due to the rise in progesterone from the newly forming CL.",
        "Why_Not": "Cows exhibit a short oestrus of 12-18 hours. Ewes show a heat of 24-36 hours. Sows are in heat for 2-3 days. A 10-12 day heat in the mare is pathological, indicating follicular cysts or prolonged transitional estrus.",
        "Wow_Approach": "Because mares have a long oestrus with variable ovulation timing, perform ultrasound examinations every 24-48 hours starting on Day 2 of heat. Breed the mare when a dominant follicle reaches >35 mm and uterine edema shows a characteristic 'wheel-spoke' pattern."
    },
    661: {
        "topic": "Gonadotropins - Glycoprotein Classification of FSH and LH",
        "Core_Anatomy": "Anterior pituitary gonadotrophs, cell membranes, and extracellular receptors.",
        "Pathogenesis_Immediate": "Follicle-Stimulating Hormone (FSH) and Luteinizing Hormone (LH) are biochemical glycoproteins consisting of two non-covalently associated peptide subunits (alpha and beta).",
        "Pathogenesis_Deep": "The alpha (α) subunit is identical among FSH, LH, and TSH within a species. The beta (β) subunit is unique and confers hormone-specific receptor binding. The carbohydrate (glycan) side chains are essential for stabilizing the tertiary structure, maintaining solubility, and determining the metabolic half-life in circulation. Their glycoprotein structure means they must bind to G-protein coupled receptors (GPCRs) on the cell membrane, acting via second messengers (cAMP).",
        "Why_Not": "FSH and LH are not simple proteins (which lack carbohydrate chains) or steroids (which are cholesterol-derived lipid-soluble molecules, like estrogen/progesterone). They are not fatty acids (like prostaglandins).",
        "Wow_Approach": "The half-life of gonadotropins is directly related to their sialic acid content: eCG has a high sialic acid content, giving it a half-life of several days, whereas pituitary FSH has a half-life of only 2-5 hours."
    },
    662: {
        "topic": "Bovine Embryogenesis - Day 7-8 Blastocyst Stage",
        "Core_Anatomy": "Preimplantation embryo, blastocoel cavity, inner cell mass, and trophoblast.",
        "Pathogenesis_Immediate": "The blastocyst stage of the preimplantation embryo in cattle is achieved on Days 7-8 post-fertilization.",
        "Pathogenesis_Deep": "Bovine embryonic development schedule: Day 1 = 2-cell stage; Day 3 = 8-cell stage; Days 5-6 = Morula (compaction of blastomeres); Days 7-8 = Blastocyst (formation of a fluid-filled blastocoel cavity, dividing cells into the inner cell mass and trophoblast); Days 8-9 = Expanded Blastocyst; Days 9-11 = Hatched Blastocyst (digestion of the zona pellucida). This timeline is crucial for embryo transfer technology, as non-surgical flushing is performed on Day 7 to collect morulae or early blastocysts.",
        "Why_Not": "The 3-day stage represents early cleavage (8-16 cells) in the oviduct. The 5-day stage is the compact morula, which has not yet developed a blastocoel cavity.",
        "Wow_Approach": "For embryo transfer, collect embryos on Day 7 when they are at the compact morula or early blastocyst stage. These stages are robust and survive cryopreservation (freezing in ethylene glycol) much better than earlier or later stages."
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
