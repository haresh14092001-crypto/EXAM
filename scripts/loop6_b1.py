import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    540: {
        "topic": "Terminology - Infertility vs Sterility vs Nymphomania",
        "Core_Anatomy": "Hypothalamic-pituitary-ovarian axis, follicles, and endometrial tissue.",
        "Pathogenesis_Immediate": "Infertility refers to a temporary or reversible reduction in reproductive efficiency, whereas sterility denotes an absolute, permanent, and irreversible inability to produce offspring. Nymphomania is a condition of persistent, continuous, or frequent oestrus behaviour caused by follicular cysts.",
        "Pathogenesis_Deep": "The key physiological distinction is reversibility: infertile animals (e.g., those with endometritis or luteal phase dysfunction) can be restored to normal fertility with therapy (intrauterine infusions, hormone regimens), while sterile animals (e.g., bilateral cryptorchids, freemartins, or those with severe sclerotic metritis) have permanent anatomical or physiological defects that preclude conception. Nymphomania arises due to an absence of luteinizing hormone (LH) surge, leading to persistent large thin-walled anovulatory follicles that continually secrete estrogen.",
        "Why_Not": "Sterility is permanent and untreatable. Pseudopregnancy (false pregnancy) is a transient condition common in bitches where a persistent corpus luteum simulates pregnancy but does not denote a permanent reduction in fertility. Nymphomania is a behavioral manifestation of ovarian dysfunction, not a broad classification of reduced fertility.",
        "Wow_Approach": "To differentiate clinical cases, measure systemic progesterone: nymphomaniac cows consistently show progesterone <1 ng/ml with multiple fluctuant structures >2.5 cm on rectal palpation, whereas sub-active or anoestrus ovaries show minimal structure or a persistent luteal cyst with progesterone >1.5 ng/ml."
    },
    544: {
        "topic": "Intercornual Ligament - Bovine Specific Anatomy",
        "Core_Anatomy": "Intercornual ligament (dorsal and ventral), uterine horns, and uterine body.",
        "Pathogenesis_Immediate": "The intercornual ligament is a distinctive fibrous band connecting the two uterine horns at their bifurcation point, uniquely present in cows. It is absent in mares, sows, and bitches.",
        "Pathogenesis_Deep": "Anatomically, the bovine uterus is bicornuate with a short body and long horns that are curled ventrally. The dorsal and ventral intercornual ligaments secure the horns at their caudal junction, preventing excessive displacement. This structure is a vital tactile landmark during transrectal palpation to stabilize and retract the uterus, allowing the examiner to trace both horns from the bifurcation to the ovaries.",
        "Why_Not": "Mares have a T-shaped bicornuate uterus with a long uterine body and relatively straight horns without a connecting ligament. Sows have extremely long, convoluted uterine horns resembling small intestines, lacking an intercornual ligament. Bitches have a long Y-shaped uterus suited for litter-bearing, also without this ligament.",
        "Wow_Approach": "Retraction technique: Hook the index finger under the dorsal intercornual ligament and pull the uterus dorsally and caudally into the pelvic cavity. This facilitates deep palpation of the horns for early pregnancy diagnosis (fluid fluctuance, slip of fetal membranes at Day 30-35) or detecting pathological fluid."
    },
    575: {
        "topic": "Obstetrics Matching - Uterine Involution, Caslick, and Reflexes",
        "Core_Anatomy": "The cervix, vagina, vulva, broad ligaments, and the hypothalamo-neurohypophyseal axis.",
        "Pathogenesis_Immediate": "Key matching concepts: Caslick's operation corrects pneumovagina in mares; Ferguson's reflex triggers oxytocin release via vaginal/cervical stretch; a fistulous tract is an abnormal epithelial-lined communication (e.g., rectovaginal fistula); uterine involution is the physiological return of the gravid uterus to its non-pregnant size.",
        "Pathogenesis_Deep": "Uterine involution involves progressive myometrial cell size reduction (autolysis), caruncular sloughing, and endometrial regeneration. Ferguson's reflex represents a classic neuroendocrine positive-feedback loop where stretch receptors in the cervix send signals to the hypothalamus, causing oxytocin secretion, which stimulates further myometrial contractions and forces the fetus further into the cervix.",
        "Why_Not": "A fistulous tract is an abnormal tunnel, whereas a sinus is a blind pouch. Sclerotic metritis is a pathological, irreversible chronic fibrosis, not a normal physiological involution. Caslick's operation is strictly indicated for vulvar conformational defects, not vaginal prolapse.",
        "Wow_Approach": "To monitor post-partum uterine involution in dairy cattle: the uterus should be fully retractable into the pelvic canal by Day 25-30. If it remains deep in the abdomen with thickened walls past Day 35, suspect subclinical endometritis or metritis, and initiate prostaglandin therapy."
    },
    578: {
        "topic": "Caslick Operation - Pneumovagina Treatment in Mares",
        "Core_Anatomy": "The vulva, vestibulo-vaginal sphincter, and anus in the mare.",
        "Pathogenesis_Immediate": "Caslick's operation is the surgical procedure used to treat pneumovagina ('wind-sucking') in mares, preventing the aspiration of air, faeces, and pathogens into the vagina by suturing the upper lips of the vulva together.",
        "Pathogenesis_Deep": "Pneumovagina is caused by poor perineal conformation, often seen in aged, thin, or multiparous mares, where the anus sinks cranially, tilting the vulva horizontally. The vestibulovaginal sphincter loses its seal, causing air aspiration. This leads to vaginitis, cervicitis, and chronic endometritis, which are major causes of infertility. The Caslick operation involves removing a thin strip of mucosa (2-3 mm) from the dorsal two-thirds of the vulvar lips and suturing them together to form a permanent tissue bridge.",
        "Why_Not": "Uterine involution is a physiological healing process, not a surgical correction. Cervicotomy is the incision of the cervix for stenosis. Episiotomy is the surgical incision of the vulva to enlarge the opening during active dystocia. Caslick's is a reconstructive closure to reduce the vulvar aperture.",
        "Wow_Approach": "Crucial clinical rule: A pregnant mare that has undergone a Caslick operation MUST have the vulvar bridge surgically opened (episiotomy or 'de-Caslick') approximately 2-4 weeks before her expected foaling date, or immediately upon the onset of Stage 2 labor, to prevent severe perineal tearing."
    },
    595: {
        "topic": "Progesterone Profiling - Ovulation Timing in the Bitch",
        "Core_Anatomy": "Preovulatory follicles, granulosa cells, and the canine systemic vascular compartment.",
        "Pathogenesis_Immediate": "The bitch is unique because luteinization of the preovulatory follicle begins before ovulation, causing a preovulatory rise in progesterone. The progesterone level at the time of the LH surge is 1-2 ng/ml, and at the time of ovulation, it reaches 2-4 ng/ml.",
        "Pathogenesis_Deep": "Unlike most domestic species where progesterone remains <0.5 ng/ml until the CL forms post-ovulation, canine granulosa cells luteinize under the influence of the LH surge before follicular rupture. Ovulation of primary (immature) oocytes occurs at a progesterone concentration of 2-4 ng/ml. The oocytes require an additional 48-72 hours in the oviduct to mature into fertilizable secondary oocytes. Progesterone levels then exceed 5 ng/ml, confirming ovulation.",
        "Why_Not": "Progesterone levels of 20-30 ng/ml are characteristic of fully mature corpora lutea during mid-diestrus, not the ovulation window. Baseline levels of 0.5-1.0 ng/ml are seen during proestrus before the preovulatory LH surge.",
        "Wow_Approach": "AI Scheduling Protocol: Test serum progesterone every 48 hours starting on day 5 of proestrus. When progesterone rises to 2-4 ng/ml (ovulation day), schedule breeding with fresh or chilled semen 48 hours later (when oocytes are mature) to maximize the conception rate and litter size."
    },
    606: {
        "topic": "Progesterone Threshold - Bovine Luteal Activity and Pregnancy",
        "Core_Anatomy": "The mature corpus luteum, endometrial glands, and maternal circulation.",
        "Pathogenesis_Immediate": "A peripheral serum progesterone concentration of >1 ng/ml is the established threshold indicating active luteal function (a functional corpus luteum) and is the minimum level required to maintain pregnancy in cows.",
        "Pathogenesis_Deep": "Progesterone (P4) is secreted by the large and small luteal cells of the CL. During estrus and the follicular phase, levels are baseline (<0.5 ng/ml). By Day 5 of the oestrous cycle, P4 rises above 1 ng/ml as the CL matures, peaking at 5-10 ng/ml during mid-diestrus (Days 10-14). If fertilisation occurs, the CL persists and must maintain P4 >1 ng/ml to suppress myometrial contractility and stimulate endometrial gland secretion (histotroph).",
        "Why_Not": "A threshold of =1 ng/ml is a borderline zone that does not reliably confirm functional luteal phase. Levels <0.5 ng/ml indicate absence of a functional CL (e.g., during oestrus, anoestrus, or post-luteolysis). There is no requirement for levels >10 ng/ml for basic pregnancy maintenance.",
        "Wow_Approach": "Milk Progesterone Test: Collecting milk on Day 21 post-AI and finding progesterone <1 ng/ml has a 100% negative predictive value for pregnancy (the cow is definitely not pregnant and has returned to estrus). A value >3 ng/ml indicates a active CL, with a 75-80% positive predictive value for pregnancy."
    },
    607: {
        "topic": "Programmed Breeding - Hormone Combinations in Cattle",
        "Core_Anatomy": "Hypothalamus (GnRH), anterior pituitary (LH/FSH receptors), corpus luteum, and ovarian follicles.",
        "Pathogenesis_Immediate": "Programmed breeding (synchronization of ovulation) in dairy cattle is most effectively achieved using a combination of GnRH and Prostaglandin F2-alpha (PGF2alpha), which is the basis of the classic Ovsynch protocol.",
        "Pathogenesis_Deep": "The Ovsynch protocol works by coordinating both follicular waves and luteal lifespan: (1) First GnRH injection (Day 0) ovulates or luteinizes the dominant follicle and initiates a new follicular wave. (2) PGF2alpha injection (Day 7) regresses any active or induced CL, causing a rapid drop in progesterone. (3) Second GnRH injection (Day 9) forces a synchronized LH surge, ovulating the new dominant follicle. Fixed-time AI (FTAI) is performed 16-20 hours later.",
        "Why_Not": "Estrogen and progesterone combinations are used for estrus synchronization but are less precise for fixed-time ovulation synchronization due to variable follicle regression rates. Prostaglandin and FSH combinations are used for superovulation, not standard programmed breeding protocols.",
        "Wow_Approach": "To optimize Ovsynch in dairy herds, introduce a Presynch protocol (two PGF2alpha injections 14 days apart, with the second injection given 12 days before starting Ovsynch). This ensures that 70-80% of the cows are on Days 5-12 of their cycle when the first GnRH is given, increasing the conception rate by 10%."
    },
    608: {
        "topic": "Bovine Oestrous Cycle - Follicular Wave Dynamics",
        "Core_Anatomy": "Ovarian cortex, primordial follicle pool, dominant preovulatory follicle, and subordinate follicles.",
        "Pathogenesis_Immediate": "The majority of dairy cattle exhibit either 2 or 3 follicular waves during a normal 21-day oestrous cycle. A wave involves the recruitment, selection, deviation, and dominance of a group of antral follicles.",
        "Pathogenesis_Deep": "A wave starts with a small rise in FSH, stimulating a cohort of 3-6 small follicles (2-4 mm). One follicle is selected as dominant due to acquiring LH receptors on its granulosa cells, while the others (subordinates) undergo atresia. In a 2-wave cycle, the dominant follicle of the first wave undergoes atresia due to high progesterone from the active CL; the second wave's follicle ovulates after luteolysis. In a 3-wave cycle, the third wave's follicle ovulates.",
        "Why_Not": "Single-wave cycles (0-1) are pathological, usually resulting in persistent follicles or anovulatory cysts. Cycles with 4-5 waves are extremely rare in cattle but can occur in prolonged cycles or under certain dietary stresses.",
        "Wow_Approach": "Heifers typically have 3-wave oestrous cycles (interovulatory interval ~22-23 days), whereas mature dairy cows more commonly show 2-wave cycles (interval ~19-21 days). Recognizing this wave pattern is critical when design custom synchronization protocols for heifers vs lactating cows."
    },
    609: {
        "topic": "Indomethacin - Blocking Ovulation via PGE2 Suppression",
        "Core_Anatomy": "Follicular apex, granulosa cells, theca externa, and the follicular vascular bed.",
        "Pathogenesis_Immediate": "Administration of indomethacin (a potent non-selective cyclooxygenase inhibitor) blocks ovulation in cows by suppressing the synthesis of prostaglandins (PGE2 and PGF2alpha), which are essential mediators of follicular rupture.",
        "Pathogenesis_Deep": "Ovulation is a specialized inflammatory process. The preovulatory LH surge triggers a massive up-regulation of COX-2 (cyclooxygenase-2) in granulosa cells, producing PGE2 and PGF2alpha. PGE2 increases follicular hyperaemia, vascular permeability, and plasminogen activator expression. PGF2alpha stimulates the release of lysosomal enzymes and the contraction of theca externa smooth muscle cells, causing digestion and rupture of the follicular apex (stigma). Indomethacin blocks this pathway, leaving the follicle intact.",
        "Why_Not": "Indomethacin does not block FSH or LH release from the pituitary, nor does it inhibit estrogen synthesis. It acts locally within the preovulatory follicle as a COX inhibitor, demonstrating that prostaglandins are the final obligatory intra-follicular triggers for physical rupture.",
        "Wow_Approach": "In bovine clinical research, indomethacin-induced block of ovulation is used to study the 'Luteinized Unruptured Follicle' (LUF) syndrome, a cause of infertility where the follicle fails to rupture but undergoes luteinization, producing normal progesterone cycles without releasing an oocyte."
    },
    616: {
        "topic": "Lithopedions - Fetal Calcification in Ectopic Pregnancy",
        "Core_Anatomy": "The peritoneal cavity, omentum, fetal membranes, and the skeletal/soft tissue compartments of the dead fetus.",
        "Pathogenesis_Immediate": "A Lithopedion ('stone baby') is a dead, extra-uterine (ectopic or abdominal) fetus that has become progressively mummified and calcified over time, representing an end-stage outcome of abdominal pregnancy.",
        "Pathogenesis_Deep": "When an embryo or fetus escapes the uterine cavity (e.g., via uterine rupture) and implants or survives within the peritoneal cavity (abdominal pregnancy), it eventually dies due to inadequate vascularization. In a sterile environment, rather than undergoing maceration (which requires bacterial entry from an open cervix), the fetal tissues lose fluid (desiccation). Over months or years, the maternal body deposits calcium salts into the desiccated fetal membranes and soft tissues, walling it off.",
        "Why_Not": "A macerated fetus is liquefied in the presence of bacteria, leading to bone fragmentation and purulent metritis. A mummified fetus occurs inside an intact, sterile uterus. A lithopedion is strictly extra-uterine and mineralized.",
        "Wow_Approach": "Incidental Slaughterhouse Finding: Lithopedions are most frequently diagnosed as incidental findings during necropsy or slaughter in cows. They present as extremely hard, stone-like abdominal masses that are encapsulated by fibrous omental adhesions, often showing intact skeletal lines on radiography."
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
