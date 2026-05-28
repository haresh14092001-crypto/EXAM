import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1202: {
        "topic": "Semen Cryopreservation - Indefinite Lifespan (Repeated)",
        "Core_Anatomy": "Sperm cell cytoplasm and cryogenic storage.",
        "Pathogenesis_Immediate": "The statement 'The life span of frozen semen is five years' is FALSE. When properly stored in liquid nitrogen at -196°C, the life span of frozen semen is theoretically indefinite.",
        "Pathogenesis_Deep": "At -196°C, all metabolic and enzymatic activities of the spermatozoon are completely suspended. There is no biochemical degradation or DNA damage. Sperm cells can remain viable in this cryogenic state for decades. Successful conceptions have been achieved using bovine semen frozen for over 40-50 years.",
        "Why_Not": "A 5-year limit is a logistical shelf-life recommendation for certain registries, but possesses no biological basis under proper liquid nitrogen storage.",
        "Wow_Approach": "To prevent accidental damage during storage: never lift semen straws above the 'frost line' for more than 5 seconds to avoid ice recrystallization."
    },
    1203: {
        "topic": "Libido Assessment - Reaction Time (Repeated)",
        "Core_Anatomy": "Hypothalamus and pelvic motor pathways.",
        "Pathogenesis_Immediate": "The statement 'Libido of the bull can be assessed by the reaction time' is TRUE.",
        "Pathogenesis_Deep": "Libido is the sexual desire of the male, independent of semen quality. In BSE, libido is assessed by placing the bull in a pen with a teaser animal and measuring the 'reaction time'—the time interval from introduction to the first active mount. A highly fertile bull with strong libido should have a reaction time under 2-3 minutes.",
        "Why_Not": "Evaluating semen volume or motility evaluates testicular/accessory gland function, not the central nervous system drive.",
        "Wow_Approach": "Bulls are graded on a scale of 0 to 10. A score of 9-10 indicates active courtship and mounting within 1 minute."
    },
    1212: {
        "topic": "Exam Guidelines - VGO Objective Section Time Limit",
        "Core_Anatomy": "N/A - Examination Rules.",
        "Pathogenesis_Immediate": "University regulations dictate that the objective Part-A paper must be completed in the first 30 to 60 minutes and handed over to the Hall Superintendent.",
        "Pathogenesis_Deep": "This testing structure isolates direct factual recall of reproductive physiology, preventing the use of descriptive cues from essays in Part-B. Evaluated topics include: semen packaging materials, epididymal transit times, and hormonal parameters.",
        "Why_Not": "Part-B contains descriptive clinical essays and surgical procedures which require structured problem-solving.",
        "Wow_Approach": "Rapid-fire recall of quantitative constants is essential for passing the objective section."
    },
    1213: {
        "topic": "Pelvimetry - Measurement of Pelvic Dimensions",
        "Core_Anatomy": "Maternal bony pelvis (ilium, ischium, pubis) and pelvic canal.",
        "Pathogenesis_Immediate": "Pelvimetry is the clinical procedure that deals with the measurement of different internal dimensions of the maternal bony pelvis to predict dystocia.",
        "Pathogenesis_Deep": "Pelvimetry is primarily used in heifers to determine if the pelvic area is sufficient to deliver a normal-sized calf. A Rice pelvimeter is inserted rectally to measure: (1) Vertical diameter (sacrum to pubic symphysis). (2) Transverse diameter (widest point between the shafts of the ilia). Multiplying these gives the Pelvic Area (in cm²). If the pelvic area is too small relative to the expected calf birth weight (fetopelvic disproportion), the heifer is culled or scheduled for elective caesarean.",
        "Why_Not": "Fetometry is the measurement of the fetus. Pelvimetry strictly refers to measuring the maternal birth canal.",
        "Wow_Approach": "A yearling beef heifer should have a minimum pelvic area of 140-150 cm² before breeding to minimize the risk of severe dystocia at calving."
    },
    1229: {
        "topic": "Breech Presentation - Posterior Longitudinal Presentation",
        "Core_Anatomy": "Fetal pelvic limbs, maternal pelvic canal, and fetal buttocks.",
        "Pathogenesis_Immediate": "A presentation where the fetal buttocks or tail is presented at the pelvic inlet with the hindlimbs retained (flexed at the hip joints) is termed a Breech presentation.",
        "Pathogenesis_Deep": "Breech presentation is a specific, severe form of posterior longitudinal presentation. Normally in a posterior presentation, the fetal hindlimbs are extended into the birth canal (plantar surfaces facing dorsally). In a true breech, there is bilateral flexion of the hips (and usually extension of the stifles), causing the blunt mass of the fetal buttocks and tail to lodge firmly against the maternal pelvic inlet, making vaginal delivery impossible without intervention.",
        "Why_Not": "Nape presentation involves the back of the neck. Transverse/lateral involves the fetal side or back. Standard posterior presentation has the hindlimbs extended. Breech strictly implies retained hindlimbs.",
        "Wow_Approach": "To correct a breech: administer epidural anesthesia to stop maternal straining. Repel the fetal buttocks into the uterus, then systematically hook and extend the hindlimbs one by one into the pelvic canal before applying traction."
    },
    1230: {
        "topic": "Equine and Human Chorionic Gonadotropins - Placental Origin",
        "Core_Anatomy": "Fetal trophectoderm, endometrial cups (mare), and syncytiotrophoblast (human).",
        "Pathogenesis_Immediate": "The hormones eCG (equine Chorionic Gonadotropin) and hCG (human Chorionic Gonadotropin) are secreted directly by the fetal Placenta (specifically the chorionic tissues), not by the pituitary gland.",
        "Pathogenesis_Deep": "These are powerful luteotrophic hormones: (1) eCG (formerly PMSG) is produced by the endometrial cups (derived from fetal chorionic girdle cells) in the pregnant mare from day 35 to 120. It possesses massive FSH-like activity in other species (used for superovulation). (2) hCG is produced by the human syncytiotrophoblast, possesses massive LH-like activity, and is used to trigger ovulation of mature follicles in veterinary medicine.",
        "Why_Not": "The anterior pituitary secretes endogenous FSH and LH. The hypothalamus secretes GnRH. Only chorionic gonadotropins are uniquely synthesized by the fetal placental tissues to hijack the maternal ovaries.",
        "Wow_Approach": "For superovulation protocols in cows: inject 2500 IU of eCG (PMSG) intramuscularly. Because eCG is heavily glycosylated, its half-life in the cow is extremely long (several days), allowing a single injection to drive a massive follicular wave."
    },
    1231: {
        "topic": "Obstetrical Terminology - Fetal Posture",
        "Core_Anatomy": "Fetal head, neck, and limbs relative to its own body.",
        "Pathogenesis_Immediate": "The obstetrical term that defines the relation of the extremities (head, neck, and limbs) to the body of the fetus itself is termed Posture.",
        "Pathogenesis_Deep": "Veterinary obstetrics relies on three specific definitions to describe fetal alignment: (1) Presentation: the relation of the long axis of the fetus to the long axis of the mother (longitudinal vs transverse). (2) Position: the relation of the dorsum of the fetus to the quadrants of the maternal pelvis (e.g., dorso-sacral is normal). (3) Posture: the anatomical disposition of the fetal appendages (limbs, head, neck) relative to its own body (e.g., extended, flexed, retained). A normal posture is 'head resting on extended forelimbs'.",
        "Why_Not": "Presentation defines the fetal-maternal axis. Position defines fetal back relative to maternal pelvis. Posture strictly refers to the internal folding or extension of the fetal limbs and head.",
        "Wow_Approach": "Most dystocias in cattle are due to abnormalities in posture (e.g., carpal flexion or lateral deviation of the head). Correction (mutation) always involves correcting posture first before attempting to extract the calf."
    },
    1232: {
        "topic": "Reproductive Timelines - Attachment or Transit Parameters",
        "Core_Anatomy": "Maternal endometrium and fetal trophoblast.",
        "Pathogenesis_Immediate": "In reproductive timelines, the period of 20-25 days often correlates with embryonic attachment or maternal recognition events depending on the species.",
        "Pathogenesis_Deep": "This parameter evaluates knowledge of key chronological events in embryology. For example, in cattle, maternal recognition of pregnancy (via IFN-tau) occurs around days 15-17, and definitive chorioallantoic attachment begins around days 20-25. In the mare, the embryo remains spherical and mobile until fixation at day 16, with endometrial cup formation beginning around day 35.",
        "Why_Not": "Timelines like 9-12 days reflect early blastocyst stages or oviductal transit, whereas 40 days reflects established placentation or specific milestones like canine testicular descent.",
        "Wow_Approach": "Always correlate days of gestation with the structural changes visible on transrectal ultrasound (e.g., embryonic heartbeat visible at day 24-28 in cows)."
    },
    1233: {
        "topic": "Bicornuate Uterus Anatomy - Sow (Highly Developed Horns)",
        "Core_Anatomy": "Uterine horns (cornua), uterine body, and cervix.",
        "Pathogenesis_Immediate": "A highly developed Bicornuate type of uterus (with extremely long, folded uterine horns and a small uterine body) is characteristically found in litter-bearing species like the Sow.",
        "Pathogenesis_Deep": "Uterine classification is based on the degree of fusion of the Mullerian ducts: (1) Bipartite uterus (cow, ewe): has a prominent septum separating the two horns for part of their length, with moderate horn length. (2) Bicornuate uterus (sow, bitch): the horns are extremely long (up to 1 meter in sows) and convoluted to accommodate multiple fetuses (litters) spaced along the endometrium. The uterine body is very short. (3) Bipartite/Cruciate (mare): has short horns and a large, prominent uterine body. (4) Simplex (primates): no horns, just a large single body.",
        "Why_Not": "The cow and ewe are technically bipartite (though often loosely termed bicornuate in general biology, the sow is the absolute classic example of a highly developed bicornuate uterus designed for litters).",
        "Wow_Approach": "Because the sow has 1-meter-long uterine horns, intrauterine migration of embryos is essential. Between days 8-12, the porcine embryos migrate freely between the two horns to ensure perfectly equal spacing and nutrient distribution before attachment."
    },
    1234: {
        "topic": "Bovine Ovulation Timing - Post-Estrus Ovulation",
        "Core_Anatomy": "Ovarian Graafian follicle, LH surge, and the infundibulum.",
        "Pathogenesis_Immediate": "In the cow, ovulation is unique because it occurs 10 to 14 hours (typically 8-12 hours) AFTER the end of behavioral estrus.",
        "Pathogenesis_Deep": "The cow is unique among domestic species in her ovulation timing. Behavioral estrus (standing heat) lasts 12-18 hours. The massive preovulatory LH surge occurs near the onset of estrus. However, the enzymatic breakdown of the follicular wall (via collagenase and prostaglandins) is exceptionally slow, taking ~28-30 hours from the LH surge. This causes the follicle to rupture 10-14 hours after the cow has completely gone out of heat.",
        "Why_Not": "In the mare and sow, ovulation occurs during the mid-to-late phase of estrus, while the female is still highly receptive. Only in the cow does ovulation consistently occur post-estrus.",
        "Wow_Approach": "This timing dictates the 'AM/PM Rule' for cattle artificial insemination: if a cow is seen in standing heat in the morning (AM), inseminate her in the evening (PM) to ensure capacitated sperm are waiting in the oviduct when the oocyte is finally released post-estrus."
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
