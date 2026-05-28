import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    621: {
        "topic": "Reproductive Matching - CIDR, Metestrual Bleeding, and Placental Structures",
        "Core_Anatomy": "Endometrium, vulva, placenta, and caudal vertebral canal.",
        "Pathogenesis_Immediate": "Key matching concepts: CIDR is a progesterone-releasing device; metestrual bleeding occurs due to estrogen withdrawal in cows; cervical star is the avascular area of the equine placenta; caudal epidural anaesthesia is performed at the Co1-Co2 space.",
        "Pathogenesis_Deep": "This matching sequence tests core diagnostics and physiological indicators. Caudal epidural anaesthesia blocks the caudal pelvic nerves, relaxing the vagina and rectum for obstetrical handling. The cervical star represents the part of the equine placenta that lies directly over the internal cervical os, lacking microcotyledons, and is where the allantochorion breaks at birth.",
        "Why_Not": "PGF2alpha is a luteolytic hormone, not a device like CIDR. Metestrual bleeding does not occur in mares or sows, only in heifers and cows. Cervical star is an equine placental feature, never found in cows.",
        "Wow_Approach": "In equine obstetrics, examine the expelled placenta: locate the 'cervical star' and ensure it has ruptured cleanly. If the cervical star did not rupture and instead presented at the vulva, it indicates 'red bag' delivery, requiring immediate manual intervention."
    },
    622: {
        "topic": "CIDR - Controlled Internal Drug Release",
        "Core_Anatomy": "Vaginal mucosal epithelium, submucosal capillaries, and the hypothalamic-pituitary axis.",
        "Pathogenesis_Immediate": "Controlled Internal Drug Release (CIDR) is a silicone-moulded intravaginal device containing progesterone, used for estrus synchronization and treating anoestrus in ruminants by delivering a steady release of progesterone.",
        "Pathogenesis_Deep": "CIDR insertion delivers exogenous progesterone (1.38 g in bovine, 0.3 g in ovine/caprine) that is rapidly absorbed across the vaginal mucosal epithelium into the systemic circulation. Systemic progesterone simulates an artificial luteal phase, suppressing hypothalamic GnRH release, which blocks LH pulses and prevents ovulation. Upon device removal (typically after 7 days), progesterone drops rapidly, mimicking luteolysis and inducing synchronized estrus within 48-72 hours.",
        "Why_Not": "CIDR does not contain estrogen or prostaglandins. Prostaglandin injections (e.g., Cloprostenol) cause luteolysis of an active CL, whereas CIDR acts as a progesterone source to synchronize animals regardless of the presence of an active CL (especially useful in anestrous cows).",
        "Wow_Approach": "To treat postpartum anestrus in dairy cows, combine a CIDR with a GnRH injection on Day 0 (insertion) and a PGF2alpha injection on Day 7 (removal). This 'Co-Synch + CIDR' protocol induces ovulation in up to 75% of anovulatory cows."
    },
    623: {
        "topic": "Metestrual Bleeding - Estrogen Withdrawal in Cows",
        "Core_Anatomy": "Endometrial capillaries, uterine lumen, and the vulva.",
        "Pathogenesis_Immediate": "Metestrual bleeding is a physiological phenomenon in heifers and cows occurring 1-3 days after the end of oestrus, caused by diapedesis of erythrocytes from endometrial capillaries following rapid estrogen withdrawal.",
        "Pathogenesis_Deep": "During proestrus and oestrus, peak levels of estradiol-17beta cause intense vascular congestion and hyperaemia of the endometrium. Following ovulation, estrogen levels drop precipitously. This abrupt hormone withdrawal leads to vasoconstriction, capillary fragility, and diapedesis of red blood cells into the uterine lumen. The blood mixes with mucus, presenting as a bloody vulvar discharge. It is normal and indicates that the animal was in estrus 1-3 days prior.",
        "Why_Not": "Metestrual bleeding is not a sign of menstruation (which involves shedding of the endometrium and occurs in primates). It does not indicate conception failure; pregnant and non-pregnant heifers can exhibit metestrual bleeding, meaning it cannot be used as an early pregnancy test.",
        "Wow_Approach": "If a dairy cow is seen with metestrual bleeding and was not bred, it is a retrospective indicator of a missed estrus. Record this date as Day 1-2 of the cycle and schedule intense estrus detection 18-20 days later to ensure she is bred on the next cycle."
    },
    624: {
        "topic": "Cervical Star - Equine Placental Anatomy",
        "Core_Anatomy": "Allantochorion, cervix (internal os), and uterine body.",
        "Pathogenesis_Immediate": "The cervical star is the avascular, pale, star-shaped region on the mare's allantochorion that corresponds to the area of the placenta positioned over the internal cervical os, where microcotyledons do not develop.",
        "Pathogenesis_Deep": "In the equine diffuse placenta, microcotyledons cover almost the entire chorionic surface to maximize nutrient exchange. However, where the chorion contacts the internal opening of the cervix (cervical os), there is no endometrial contact, preventing microcotyledon development. This leaves a smooth, avascular, pale area resembling a star. During Stage 2 labor, the advancing foal's feet and head push the amnion against this weakened cervical star, causing it to rupture.",
        "Why_Not": "The cervical star is unique to equids. In ruminants, the cotyledonary placenta has discrete placentomes, and there is no comparable structure. Rupture elsewhere on the equine placenta (e.g., at the horns) represents an abnormal separation.",
        "Wow_Approach": "Post-foaling examination: Spread the expelled placenta in a 'F' or 'Y' shape. Find the cervical star. It should be white, torn, and have clean edges. A velvety red, unruptured cervical star indicates 'red bag' (premature placental separation), which is an obstetric emergency."
    },
    638: {
        "topic": "VGO-I Course - Core Gynaecological Curriculum",
        "Core_Anatomy": "Hypothalamic-pituitary-gonadal axis and female reproductive organs.",
        "Pathogenesis_Immediate": "VGO-I (Veterinary Gynaecology and Obstetrics I) focuses on the physiological processes of reproduction, puberty, the estrous cycle, fertilization, pregnancy, and gynaecological disorders in domestic animals.",
        "Pathogenesis_Deep": "The curriculum covers comparative reproductive anatomy, endocrinology, the manipulation of oestrous cycles, semen collection and processing, artificial insemination, embryo transfer, and pathologies of non-pregnant female organs. Understanding these foundational topics is required to solve clinical cases in both beef/dairy herds and small animals.",
        "Why_Not": "VGO-II deals with obstetrics, dystocia, neonatology, and post-partum complications. VGO-I focuses strictly on the non-gravid animal's reproductive health, cycle management, and the early embryonic phase up to maternal recognition.",
        "Wow_Approach": "To excel in VGO-I, map the oestrous cycles of cows, mares, bitches, and queens side-by-side, noting the dominant hormones (estrogen vs progesterone), the mechanism of ovulation (spontaneous vs induced), and the site of semen deposition."
    },
    639: {
        "topic": "Academic Regulations - Veterinary Examination Procedures",
        "Core_Anatomy": "N/A - Regulatory and institutional protocols.",
        "Pathogenesis_Immediate": "Examination procedures for BVSc & AH final exams require that Part-A (objective questions) must be completed within the first 30 minutes and handed over to the Hall Superintendent before proceeding to Part-B.",
        "Pathogenesis_Deep": "Academic integrity and standard testing protocols are strictly enforced in professional veterinary programs. Separating Part-A (MCQs, fill-in-the-blanks, true/false) ensures rapid testing of core factual knowledge without access to descriptive sheets or references. This builds rapid-recall skills needed for high-pressure clinical and licensing exams.",
        "Why_Not": "Part-B contains subjective, descriptive, and clinical case-based questions that require more writing time and cannot be completed in 30 minutes.",
        "Wow_Approach": "When revising, practice answering objective questions under a 15-minute time limit. Rapid recall of biological values (e.g., gestation lengths, normal heart rates, hormone dosages) is a hallmark of an expert clinician."
    },
    640: {
        "topic": "Theriogenology Objectives - Core Biological Standards",
        "Core_Anatomy": "Ovary, uterus, cervix, and hypophysis.",
        "Pathogenesis_Immediate": "Objective questions in Theriogenology test species-specific values: minimum sperm concentration, gestation lengths, hormone biochemical classes, and diagnostic thresholds.",
        "Pathogenesis_Deep": "Key standards include: minimum progressive motility for frozen semen (>35% post-thaw), glycoprotein class of gonadotropins (LH, FSH), steroid class of ovarian hormones (estradiol, progesterone), and the typical anatomical positions of reproductive organs (e.g., ovaries are retroperitoneal/intraperitoneal, suspended by the mesovarium).",
        "Why_Not": "Subjective essays test therapeutic management, whereas objective sections strictly test exact diagnostic figures, drug classes, and numerical parameters.",
        "Wow_Approach": "Create a pocket-sized reference table of all reproductive parameters (oestrus length, ovulation timing, gestation period, placental type, and puberty age) for cow, mare, ewe, doe, sow, and bitch for last-minute review."
    },
    649: {
        "topic": "Bovine Ovulation - Metoestrus Timing",
        "Core_Anatomy": "The mature Graafian follicle, LH receptors on granulosa cells, and the follicular apex.",
        "Pathogenesis_Immediate": "Ovulation in the cow occurs during the metoestrus phase of the oestrous cycle, approximately 10-15 hours after the end of standing oestrus (or 24-30 hours after the LH surge).",
        "Pathogenesis_Deep": "Cattle are unique because they ovulate after behavioral oestrus (standing heat) has completely ceased. During oestrus (estrus phase), high estradiol induces standing behavior and triggers the LH surge. The LH surge initiates the inflammatory cascade within the preovulatory follicle, but the physical rupture of the follicle (ovulation) takes 24-30 hours, by which time the cow has entered metoestrus. The metoestrus phase (Days 1-5) is characterized by the early development of the corpus luteum from the ruptured follicle.",
        "Why_Not": "Ovulation does not occur during estrus in the cow (unlike mares and ewes, which ovulate during active heat). It does not occur during dioestrus (when progesterone from the mature CL blocks follicular maturation).",
        "Wow_Approach": "Practical Breeding Rule: Because ovulation occurs in early metoestrus, breed cows 12 hours after the first observation of standing heat (AM-PM rule). Insemination during oestrus ensures that capacitated sperm are waiting in the oviduct when the follicle ruptures in metoestrus."
    },
    650: {
        "topic": "Programmed Breeding in Buffaloes - PGF2alpha and Progesterone",
        "Core_Anatomy": "The corpus luteum, dominant follicle, and the hypothalamo-pituitary-gonadal axis in buffaloes.",
        "Pathogenesis_Immediate": "Programmed breeding in water buffaloes (Bubalus bubalis) can be accomplished using PGF2alpha alone, progesterone devices (CIDR/PRID) alone, or a combination of both (CIDR + PGF2alpha + GnRH).",
        "Pathogenesis_Deep": "Buffaloes show a high incidence of silent heat (suboestrus), especially during hot summer months. Programmed breeding bypasses the need for estrus detection. A single or double PGF2alpha regimen (11 days apart) works well if a functional CL is present. In anestrous or summer-stressed buffaloes, combining an intravaginal progesterone device (CIDR) for 7 days with a PGF2alpha injection on Day 7 and GnRH or eCG at device removal ensures synchronized follicular development and ovulation.",
        "Why_Not": "PGF2alpha alone is ineffective in anestrous buffaloes that lack a functional corpus luteum, making progesterone priming or GnRH combinations necessary for a reliable response in non-cycling herds.",
        "Wow_Approach": "To maximize fertility in summer buffaloes, use the 'Ovsynch + CIDR' protocol: Insert a CIDR and inject GnRH on Day 0, inject PGF2alpha and remove CIDR on Day 7, inject GnRH on Day 9, and perform fixed-time AI 16-20 hours later. This protocol achieves pregnancy rates of 45-50% during summer."
    },
    651: {
        "topic": "Cystic Ovarian Degeneration - Lack of LH Surge in Bovines",
        "Core_Anatomy": "Hypothalamic GnRH surge center, pituitary gonadotrophs, preovulatory follicle, and granulosa cells.",
        "Pathogenesis_Immediate": "Cystic ovarian degeneration (COD) in bovines is primarily caused by a lack of an adequate luteinizing hormone (LH) surge (or hypothalamic dysfunction), preventing ovulation of the dominant follicle.",
        "Pathogenesis_Deep": "A follicular cyst develops when a dominant follicle reaches preovulatory size (>2.5 cm) but fails to ovulate, persisting on the ovary for more than 10 days. The primary pathology is a failure of the hypothalamic-pituitary axis: either the hypothalamus fails to release a GnRH surge in response to estrogen (due to stress, high cortisol, or negative energy balance), or the anterior pituitary gonadotrophs fail to release an LH surge of sufficient amplitude. The follicle continues to grow, and the granulosa cells may eventually degenerate or become partially luteinized.",
        "Why_Not": "COD is not caused by hypocalcaemia or hypokalemia (which cause metabolic paresis or downer cow syndrome). It is not due to cholesterol excess. It is specifically an endocrine failure of the LH surge mechanism.",
        "Wow_Approach": "Treatment of Follicular Cysts: Inject 10-20 mcg Buserelin (GnRH analogue) or 3,000-5,000 IU hCG IM. This forces LH release (or mimics LH) to luteinize the cyst wall. Follow with a PGF2alpha injection 9-11 days later to regress the luteinized cyst, bringing the cow back into normal estrus."
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
