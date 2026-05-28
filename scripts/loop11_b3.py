import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1245: {
        "topic": "Obstetrical Hooks - Traction Instruments",
        "Core_Anatomy": "Fetal orbits (eye sockets), inner medial canthus, and maternal pelvic canal.",
        "Pathogenesis_Immediate": "The obstetrical hook (eye hook) is used exclusively for applying Traction to the fetal head during forced extraction, not for retropulsion, rotation, or version.",
        "Pathogenesis_Deep": "Obstetrical hooks are blunt or sharp metal hooks designed to secure the fetal head. They are placed into the medial canthus of the fetal orbits (eye sockets) to apply direct linear traction, guiding the head into the maternal pelvis. Retropulsion uses a crutch; rotation twists the fetus on its long axis; version turns the fetus on its transverse axis. Hooks are strictly for pulling (traction).",
        "Why_Not": "Retropulsion pushes the calf back into the uterus to create space. Version converts a transverse presentation to longitudinal. Rotation corrects a dorso-ilial position to dorso-sacral.",
        "Wow_Approach": "Only use sharp eye hooks on a dead fetus. For a live fetus, use blunt eye hooks and place them very carefully in the medial canthus to avoid destroying the globe of the eye, applying only gentle guiding traction."
    },
    1246: {
        "topic": "Induction of Parturition - Bovine Protocol",
        "Core_Anatomy": "Maternal corpus luteum, placenta, and myometrium.",
        "Pathogenesis_Immediate": "The most effective and reliable protocol for the induction of parturition in the near-term Cow is a combination of both PGF2-alpha and Corticosteroids (e.g., Dexamethasone).",
        "Pathogenesis_Deep": "Bovine pregnancy maintenance at term relies on BOTH the corpus luteum and the placental secretion of progesterone. (1) PGF2-alpha is a potent luteolysin that rapidly destroys the corpus luteum. (2) Corticosteroids (Dexamethasone) mimic the fetal cortisol surge, inducing placental 17-alpha-hydroxylase to convert placental progesterone into estrogen. Using both drugs simultaneously guarantees complete progesterone withdrawal and sensitizes the myometrium to oxytocin, ensuring calving within 24-48 hours.",
        "Why_Not": "Using PGF2-alpha alone may fail if the placental progesterone output is high. Using Corticosteroids alone has a high failure rate in certain cows and takes longer. The combination is the gold standard.",
        "Wow_Approach": "A major side effect of artificially inducing parturition in cattle (even with the combination protocol) is a high incidence of Retained Fetal Membranes (RFM), often exceeding 50%."
    },
    1247: {
        "topic": "Obstetrical Version - Correcting Presentation",
        "Core_Anatomy": "Fetal transverse axis and maternal longitudinal axis.",
        "Pathogenesis_Immediate": "In veterinary obstetrics, 'Version' refers specifically to the correction of a Transverse presentation into a normal longitudinal presentation.",
        "Pathogenesis_Deep": "Version is the turning of the fetus on its transverse axis. If a calf or foal is lying completely sideways across the pelvic inlet (transverse presentation), the clinician must reach in, repel one half of the body while applying traction to the other half, swinging the fetus 90 degrees to align its long axis with the mother's long axis (longitudinal presentation).",
        "Why_Not": "Correcting a longitudinal position (e.g., dorso-ilial to dorso-sacral) is termed 'Rotation'. Correcting a flexed limb (posture) is termed 'Mutation'.",
        "Wow_Approach": "Transverse presentations are extremely rare in cattle and horses but occur occasionally in mares (the 'dog-sitting' or transverse ventral presentation), representing a severe emergency that often requires heavy epidural anesthesia to correct."
    },
    1256: {
        "topic": "Obstetrical Matching - Hydroallantois and Version",
        "Core_Anatomy": "Placental membranes (allantois) and fetal alignment.",
        "Pathogenesis_Immediate": "Key matching concepts: Hydroallantois matches to diseased placenta; Version matches to the correction of transverse presentation; Paraplegia matches to post-partum nerve paralysis.",
        "Pathogenesis_Deep": "Hydrops conditions: (1) Hydroallantois (dropsy of the allantois) is caused by a diseased placenta (fewer, enlarged caruncles) leading to a massive, rapid accumulation of watery transudate (up to 200 liters) in the allantoic sac in late gestation. It presents as a sudden, severe barrel-shaped abdominal distension in the cow. (2) Hydroamnios is caused by a fetal anomaly (e.g., cleft palate preventing swallowing of amniotic fluid), accumulating slowly.",
        "Why_Not": "Hydroamnios is fetal in origin; Hydroallantois is strictly placental in origin. Mutation corrects posture; Version corrects presentation.",
        "Wow_Approach": "When treating Hydroallantois, NEVER drain the 200 liters of fluid rapidly. Sudden decompression of the abdomen causes massive splanchnic blood pooling, leading to acute hypovolemic shock and death of the cow. Drain slowly over hours."
    },
    1257: {
        "topic": "Breech Presentation - Retained Hindlimbs",
        "Core_Anatomy": "Fetal pelvic limbs (hips and stifles) and maternal pelvic inlet.",
        "Pathogenesis_Immediate": "Breech presentation matches to a posterior longitudinal presentation with bilateral flexion of the hips, causing the fetal buttocks to lodge at the pelvic inlet.",
        "Pathogenesis_Deep": "In a normal posterior presentation, the fetal hindlimbs extend backward into the vagina. In a true breech, the hindlimbs are retained deep in the uterus alongside the fetal abdomen. The blunt surface of the tail and buttocks presses against the cervix, often failing to stimulate adequate Ferguson reflex (oxytocin release), leading to weak uterine contractions.",
        "Why_Not": "Nape presentation involves the head. A 'dog-sitting' posture involves retained forelimbs. Breech specifically denotes the tail/buttocks presenting first.",
        "Wow_Approach": "To differentiate a posterior presentation from an anterior one in the birth canal: palpate the joints. If the first two joints bend in OPPOSITE directions (fetlock and hock), it is a hindlimb. If they bend in the SAME direction (fetlock and carpus), it is a forelimb."
    },
    1258: {
        "topic": "Secondary Uterine Inertia - Myometrial Exhaustion",
        "Core_Anatomy": "Maternal myometrium, calcium channels, and fetal obstruction.",
        "Pathogenesis_Immediate": "Secondary uterine inertia matches to myometrial exhaustion resulting from a prolonged, uncorrected physical obstruction (dystocia) in the birth canal.",
        "Pathogenesis_Deep": "Uterine inertia is the failure of the myometrium to contract. (1) Primary uterine inertia occurs when the uterus fails to begin contracting at all (often due to hypocalcemia/milk fever, lack of oxytocin receptors, or small litter size). (2) Secondary uterine inertia occurs AFTER normal labor has begun. A physical blockage (e.g., fetal oversize, breech) prevents delivery. The uterus contracts violently against the blockage until the smooth muscle completely depletes its ATP and calcium reserves, becoming totally flaccid (exhausted).",
        "Why_Not": "Administering oxytocin to a cow with secondary uterine inertia (while the obstruction is still present) is strictly contraindicated—it will cause violent tetanic spasms and uterine rupture.",
        "Wow_Approach": "In secondary inertia, you must physically remove the obstruction (via mutation, traction, or C-section). Once the blockage is clear, you can administer calcium and oxytocin to restore uterine tone and expel the placenta."
    },
    1271: {
        "topic": "VGO Short Notes - Definitions and Explanations",
        "Core_Anatomy": "Reproductive pathology and pharmacology.",
        "Pathogenesis_Immediate": "The 'Define/Explain' short notes section evaluates concise definitions of obstetrical and gynaecological pathologies, such as lochia, version, pelvimetry, and inertia.",
        "Pathogenesis_Deep": "To score full marks on definitions: (1) State the exact anatomical structure involved. (2) State the physiological or pathological mechanism. (3) Provide a clinical example (e.g., 'Version is the turning of the fetus on its transverse axis to correct a transverse presentation in the mare').",
        "Why_Not": "Vague answers lacking anatomical precision (e.g., 'turning the calf') will not receive full credit.",
        "Wow_Approach": "Always include the species in which the condition is most common (e.g., Uterine torsion in the Buffalo, Endometrial cups in the Mare) to demonstrate clinical awareness."
    },
    1285: {
        "topic": "VGO-II Syllabus - Applied Obstetrics and Andrology",
        "Core_Anatomy": "Maternal pelvis, gravid uterus, and male reproductive tract.",
        "Pathogenesis_Immediate": "VGO-II focuses heavily on late-stage gestation, the mechanics of parturition, dystocia resolution, and male breeding soundness.",
        "Pathogenesis_Deep": "The integration of these topics ensures the clinician can manage the entire reproductive pipeline. Key interventions include: epidural anesthesia for mutation, fetotomy wire techniques for dead fetuses, and the biochemistry of semen extenders for genetic preservation.",
        "Why_Not": "VGO-I covers non-pregnant estrous cycles and AI timing. VGO-II covers the pregnant female and the breeding male.",
        "Wow_Approach": "Mastery of VGO-II requires understanding the spatial geometry of the maternal pelvis relative to fetal joint flexion."
    },
    1286: {
        "topic": "VGO-II Advanced Modules - Clinical Integration",
        "Core_Anatomy": "Feto-maternal unit and diagnostic laboratory.",
        "Pathogenesis_Immediate": "VGO-II requires the practical application of theoretical endocrinology to resolve clinical emergencies like milk fever, retained placenta, and fetal mummification.",
        "Pathogenesis_Deep": "Understanding that fetal stress triggers parturition (via cortisol) explains why a dead or mummified fetus often fails to initiate labor, requiring exogenous prostaglandins or surgery.",
        "Why_Not": "Isolated endocrinology is taught in physiology; VGO applies it to direct pharmacological interventions (e.g., using Dexamethasone for induction).",
        "Wow_Approach": "Always verify fetal viability (e.g., checking the withdrawal reflex of the hoof or the swallowing reflex) before deciding between a live extraction (traction/C-section) and a destructive extraction (fetotomy)."
    },
    1287: {
        "topic": "Exam Guidelines - VGO Part-A Strict Timing",
        "Core_Anatomy": "N/A - Academic Administration.",
        "Pathogenesis_Immediate": "The objective Part-A paper is strictly timed (30-60 minutes) to evaluate immediate factual recall without secondary reference to Part-B essay clues.",
        "Pathogenesis_Deep": "This testing format evaluates 'system 1' rapid clinical thinking, which is essential in obstetrical emergencies where decisions (e.g., diagnosing a breech vs anterior presentation based on joint flexion) must be made in seconds.",
        "Why_Not": "Delayed decision-making during a dystocia increases the risk of fetal hypoxia and maternal exhaustion.",
        "Wow_Approach": "Treat the objective exam like an emergency triage: rapidly identify the correct physiological constants and move on."
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
