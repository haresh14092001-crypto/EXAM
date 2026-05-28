import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    412: {
        "topic": "Hydrocephalus and Genetic Defects Causing Fetal Dystocia",
        "Core_Anatomy": "The fetal skull (cranial vault, fontanelles), the choroid plexus, and the ventricular system of the brain.",
        "Pathogenesis_Immediate": "Hydrocephalus (abnormal accumulation of CSF within the cerebral ventricles, causing massive skull enlargement) is the most common genetic/developmental defect causing fetal dystocia in cattle, because the enlarged fetal head cannot pass through the maternal pelvic canal.",
        "Pathogenesis_Deep": "Hydrocephalus is caused by obstruction of CSF flow (aqueductal stenosis) or impaired CSF reabsorption by the arachnoid villi. Excess CSF accumulates in the lateral and third ventricles, causing progressive expansion of the calvarium. In bovine calves, the affected head may be 3-4x normal size, making vaginal delivery impossible. Genetic origin: autosomal recessive mutations are the most common cause in cattle; environmental teratogen exposure (Akabane virus, BVD virus) is also implicated.",
        "Why_Not": "Ascites (fetal hydrops abdominalis) is fluid in the fetal peritoneal cavity, causing abdominal enlargement — less common cause of dystocia. Wry neck causes head malpresentation but normal skull size. Hydrocephalus specifically causes an oversized, dome-shaped, translucent cranium that is immediately recognizable on vaginal examination.",
        "Wow_Approach": "Emergency management of hydrocephalus dystocia: Relieve the intracranial pressure by inserting a large-bore needle (10G) into the largest fontanelle and draining the CSF. After decompression, the collapsed skull allows delivery. This fetotomy-sparing technique must be attempted before proceeding to cranial fetotomy (bisecting the skull with a fetatome wire)."
    },
    414: {
        "topic": "Clenbuterol - Beta-2 Agonist Tocolytic for Uterine Relaxation",
        "Core_Anatomy": "The myometrial smooth muscle (beta-2 adrenergic receptors), the uterine wall, and the cervix.",
        "Pathogenesis_Immediate": "Clenbuterol (a selective beta-2 adrenergic agonist) is the drug of choice for uterine relaxation (tocolysis) during obstetrical correction of dystocia — it relaxes myometrial contractions, creating the space needed for fetal repositioning.",
        "Pathogenesis_Deep": "Clenbuterol binds beta-2 adrenergic receptors on uterine smooth muscle → activates adenylyl cyclase → increases intracellular cAMP → activates PKA → phosphorylates myosin light chain kinase → reduces myosin-actin interaction → smooth muscle relaxation. This completely inhibits uterine contractions for 30-90 minutes, providing a 'quiet uterus' that allows the obstetrician to perform retropulsion, rotation, and version without fighting against powerful straining.",
        "Why_Not": "Cloprostenol (PGF2alpha analogue) causes uterine contractions and cervical dilation — opposite effect to tocolysis. Tiaprost tromethamol is also a PGF2alpha analogue — uterotonic. Carpoprost is another PGF2alpha analogue. Oxytocin is the classic uterotonic. Clenbuterol is uniquely the tocolytic in this group, used specifically to STOP contractions.",
        "Wow_Approach": "Clenbuterol dose in cattle: 0.3 mcg/kg IV (300 mcg total for a 500 kg cow) given slowly over 2 minutes. Effect onset: 2-5 minutes. Duration: 30-60 minutes. Side effects: tachycardia, sweating, mild tremors (all beta-2 mediated). Contraindicated in cardiac arrhythmias. Always have atropine available to counteract bradycardia if vagal-mediated cardiovascular effects occur."
    },
    416: {
        "topic": "Stage 2 Labour - Shortest Duration in Equine (Repeated for emphasis)",
        "Core_Anatomy": "The equine cervix, vaginal canal, the vulvar opening, and the foal's presenting parts (forelimbs + head).",
        "Pathogenesis_Immediate": "The shortest duration of Stage 2 labour (active fetal expulsion) among domestic species is in the Equine (Mare) — typically 20-30 minutes. This rapid delivery is essential because the diffuse epitheliochorial placenta detaches from the entire uterine surface immediately after delivery, cutting off fetal oxygen supply.",
        "Pathogenesis_Deep": "Equine Stage 2 physiology: The foal's forelimbs and head engage the pelvic canal (anterior presentation, dorsal position). The allantochorion ruptures (red bag delivery if not ruptured = emergency — cut the bag immediately). Myometrial contractions combined with abdominal press expel the foal in 15-30 minutes. The foal's hindlimbs remain in the vaginal canal for 1-5 minutes post-delivery — the dam should not be disturbed during this period as the umbilical cord continues to transfer blood.",
        "Why_Not": "Canine Stage 2 lasts 2-4 hours for the full litter with individual pups born 15-60 minutes apart. Bovine Stage 2 lasts 0.5-4 hours. Ovine Stage 2 lasts 0.5-2 hours for each lamb. Only the mare has a Stage 2 so rapid that any delay beyond 30 minutes is classified as an emergency requiring immediate obstetrical intervention.",
        "Wow_Approach": "Red Bag Delivery (premature placental separation) in mares: If the allantochorion (deep red/purple bag) presents at the vulva WITHOUT rupture, cut it IMMEDIATELY with scissors. A foal born with intact membranes covering the head asphyxiates within 2-3 minutes. This is the single most time-critical equine parturition emergency."
    },
    417: {
        "topic": "Fetotomy - Indication for Dead Calves Not Deliverable by Traction",
        "Core_Anatomy": "The fetal skeleton, skin, and soft tissues; the fetotome (Thygesen's or Harms' wire saw instrument).",
        "Pathogenesis_Immediate": "Fetotomy (surgical amputation/bisection of the dead fetus in utero) is indicated when a dead calf cannot be delivered by mutation (repositioning) and forced traction alone, and when the birth canal is inadequate for Caesarean section to be practical.",
        "Pathogenesis_Deep": "Fetotomy indications: (1) Dead emphysematous fetus (gas-distended, rigid — cannot be repositioned). (2) Hydrocephalus after CSF drainage fails. (3) Anasarca (generalised fetal oedema — too large to deliver). (4) Partial correction of malpresentation failed. Fetotomy technique: A stainless steel wire saw (fetatome) is threaded around the fetal part to be removed (usually a limb or the head) and the wire is sawed to sever the part. The operation is performed trans-vaginally under epidural anaesthesia.",
        "Why_Not": "Embryotomy (embryotomy wire/saw) is functionally the same as fetotomy but the term historically referred to earlier-stage fetal dissection. In modern usage, Fetotomy is used for all in-utero fetal sectioning. Episiotomy (enlarging the vulvar opening) assists delivery of the intact fetus — not of a fetus requiring dissection.",
        "Wow_Approach": "The maximum number of fetotomy cuts recommended is 6 in cattle (to minimize maternal trauma and uterine rupture risk). Complete fetotomy (total fetal dismemberment) is associated with a 50-70% chance of subsequent fertility in cows. Partial fetotomy (removal of one limb or the head only) preserves 80-90% subsequent fertility."
    },
    418: {
        "topic": "Episiotomy - Vulvar Incision to Enlarge Birth Canal",
        "Core_Anatomy": "The vulva (labia majora and minora), the perineal body, and the vestibular constrictor muscles.",
        "Pathogenesis_Immediate": "Episiotomy is a surgical incision made in the vulva (specifically the dorsal commissure of the vulvar lips and perineal body) to enlarge the birth canal opening, facilitating delivery of a large fetus or an oversized fetal part that cannot pass through the undilated vulvar opening.",
        "Pathogenesis_Deep": "Episiotomy technique: With the animal under epidural anaesthesia (caudal epidural, 5-10 ml 2% Lignocaine at Co1-Co2), a 3-5 cm dorsal incision is made at the 12 o'clock position of the vulvar opening using straight scissors or a scalpel. This prevents tearing (which creates irregular, poorly healing wounds) and provides controlled enlargement of the vulvar opening. After delivery, the wound is closed in two layers (mucosa + skin) with absorbable sutures.",
        "Why_Not": "Caslick's Operation involves suturing the dorsal vulva CLOSED (opposite of episiotomy) — used to prevent pneumovagina in mares. Reefing operation reduces uterine prolapse. Cesarean section is reserved for cases where vaginal delivery is completely impossible. Episiotomy is specifically a vulvar enlargement procedure used as an adjunct to assisted vaginal delivery.",
        "Wow_Approach": "Episiotomy is more commonly performed in mares (where the vulvar constrictor is tight) and bitches (where the vulvar opening is proportionally small relative to the fetal heads). In cattle, the vulva is usually sufficiently dilated by the time stage 2 labour begins — episiotomy in cattle is reserved for primipara heifers or for delivery of oversized calves."
    },
    419: {
        "topic": "Critical Period for Developmental Anomalies - Period of the Embryo",
        "Core_Anatomy": "The embryonic germ layers (ectoderm, mesoderm, endoderm), the organogenetic period (Days 17-60 in cattle), and the fetal organ systems.",
        "Pathogenesis_Immediate": "Most developmental anomalies (teratogenic malformations) occur during the Period of the Embryo (organogenesis, Days 14-45 in cattle, equivalent to the first trimester in humans) — when organ systems are being differentiated from germ layers and are maximally susceptible to teratogens.",
        "Pathogenesis_Deep": "Developmental periods: Period of Ovum (Days 0-14) = pre-implantation; teratogens cause all-or-nothing effect (death or normal development). Period of Embryo (Days 14-60) = organogenesis; each organ has a specific critical window of susceptibility — exposure to teratogens during a specific organ's differentiation causes that organ's malformation. Period of Fetus (Day 60 to term) = growth phase; teratogens cause growth retardation or functional impairment, rarely structural malformations.",
        "Why_Not": "During the Period of the Fetus, organ structure is established but functional maturation continues. Teratogen exposure during this period causes functional defects (hearing loss, CNS impairment) rather than gross structural malformations. The Period of the Ovum is actually the SAFEST period — the embryo has not yet differentiated, so damage causes complete death rather than partial malformation.",
        "Wow_Approach": "Key veterinary teratogens and their specific organ targets in the embryonic period: Akabane virus (Day 30-50 in cattle): cerebellar hypoplasia, arthrogryposis. BVD virus (Day 40-125): cerebellum, immune system (PI calves). Vitamin A excess (Day 14-45): neural tube defects. Locoweed alkaloids (Days 20-60): hydrocephalus, arthrogryposis."
    },
    420: {
        "topic": "Clenbuterol Contraindicated for Uterine Inertia - Tocolytic vs Uterotonic",
        "Core_Anatomy": "The uterine myometrial smooth muscle (beta-2 and oxytocin receptors), the fetal-placental unit.",
        "Pathogenesis_Immediate": "Clenbuterol (beta-2 agonist tocolytic) CANNOT treat uterine inertia — it causes uterine relaxation (REDUCES contractions). To treat uterine inertia, you need uterotonics: Calcium (sensitizes myometrium), Oxytocin (triggers myometrial contraction), or PGF2alpha (stimulates labour).",
        "Pathogenesis_Deep": "Uterine inertia (primary or secondary failure of uterine contractions): Primary inertia = failure to initiate coordinated contractions despite term pregnancy (hypocalcaemia, exhaustion, myometrial fatigue). Secondary inertia = cessation of contractions after prolonged effort (exhaustion). Treatment: Calcium gluconate IV (corrects hypocalcaemia, sensitizes myometrium to oxytocin) → Oxytocin 20-40 IU IM (stimulates coordinated contractions). Clenbuterol would worsen inertia by further relaxing the already-inert myometrium.",
        "Why_Not": "Clenbuterol is the drug used for the OPPOSITE situation — uterine hypertonia during obstetrical correction where excessive contractions prevent fetal repositioning. These two scenarios are the reverse of each other: inertia = too few contractions (needs uterotonics); hypertonia = too many contractions (needs tocolytics).",
        "Wow_Approach": "Sequential approach to uterine inertia: (1) 400 ml 40% Calcium Borogluconate IV (slow, 15 min). (2) Wait 15 minutes — if contractions resume, deliver naturally. (3) If no improvement: Oxytocin 40 IU IM. (4) If still no progress in 30 min: assisted delivery or C-section. Never exceed 3 doses of oxytocin — risk of uterine tetany and fetal hypoxia."
    },
    421: {
        "topic": "Vaginal Prolapse in Dogs - Oestrus-Associated Hyperplasia",
        "Core_Anatomy": "The vaginal mucosa, the vestibulo-vaginal junction, and the estrogenic sensitivity of the vaginal epithelium.",
        "Pathogenesis_Immediate": "Vaginal prolapse (vaginal hyperplasia/type I-III prolapse) in dogs occurs specifically during Proestrus and Oestrus — the period of peak estrogen stimulation — when estrogenic sensitivity of the vaginal submucosa causes exaggerated oedematous hyperplasia and folding that protrudes through the vulva.",
        "Pathogenesis_Deep": "Estrogen causes profound vaginal mucosal proliferation and submucosal oedema during proestrus. In predisposed breeds (Mastiff, Boxer, Labrador, Saint Bernard, Bulldog), the vaginal floor cranial to the urethral tubercle hypertrophies massively under estrogen stimulation, forming a pink, tongue-like mass protruding from the vulva. If not reduced, the exposed mucosa desiccates, ulcerates, and necroses.",
        "Why_Not": "Uterine prolapse is the eversion of the entire uterus through the cervix and vulva — most commonly post-parturition when the cervix is still dilated. Vaginal prolapse occurs during oestrus WITHOUT parturition. Perineal hernia is the displacement of the rectum or bladder through the perineal musculature — not vaginal tissue eversion.",
        "Wow_Approach": "Management: (1) Reduce the prolapse manually under sedation and epidural anaesthesia. (2) Clean, lubricate, and replace the tissue. (3) Place a vulvar retention suture to prevent recurrence until oestrogen levels drop. (4) Spay at the earliest opportunity — the condition recurs with every oestrus until ovariohysterectomy removes the estrogenic stimulus permanently."
    },
    423: {
        "topic": "Obstetrical Instruments - Snare, Concealed Palm Knife, and Fetotomy Tools",
        "Core_Anatomy": "The fetal head, jaw, and limbs; the maternal birth canal.",
        "Pathogenesis_Immediate": "Key obstetrical instruments: Snare (wire or rope loop around a fetal part for traction), Concealed Palm Knife (hooked blade concealed in the palm of the hand for in-utero incisions without maternal injury), Fetatome (Thygesen's tube with wire saw for fetotomy).",
        "Pathogenesis_Deep": "Snare application: A braided wire or rope loop is placed around the fetal lower jaw (for head retraction), a limb (for traction), or the neck (for dead fetus extraction). The snare converts pulling force to a point source, enabling controlled directional traction. Concealed Palm Knife: Used to incise the fetal skin during subcutaneous fetotomy or to enlarge the vulvar opening (episiotomy) from inside the birth canal, minimizing maternal mucosal trauma by keeping the blade hidden within the palm.",
        "Why_Not": "The Kuhn's fetotome is a metal tube through which the wire saw is threaded — protecting the maternal reproductive tract from wire laceration. The Ostertag embryotome is a similar design. These are distinct from simple wire snares (which only apply traction, not cutting force).",
        "Wow_Approach": "Golden rules of obstetrical assistance: (1) Never pull a living calf without confirming the presentation, position, and posture are correctable. (2) Use copious lubrication (methylcellulose gel, warm soapy water) before any correction. (3) Maximum traction force: Two people pulling on a calf jack = equivalent to 250 kg force — never exceed this without fetotomy. (4) Epidural anaesthesia first, always."
    },
    431: {
        "topic": "Retropulsion as an Obstetrical Correction Manoeuvre",
        "Core_Anatomy": "The fetal presenting parts, the uterine cavity, and the amniotic/allantoic fluid cushion.",
        "Pathogenesis_Immediate": "Retropulsion is the obstetrical manoeuvre of pushing the fetus back (cranially) into the uterine cavity to create space for correcting malpresentations, malpositions, or malpostures before applying traction for delivery.",
        "Pathogenesis_Deep": "Retropulsion is always the FIRST step in any obstetrical correction — before attempting to reposition a flexed limb or a deviated head, the fetus must be pushed back to decompress the presenting parts from the pelvic inlet. This requires: (1) Clenbuterol injection (0.3 mcg/kg IV) to relax uterine contractions. (2) Generous lubrication of the birth canal. (3) The obstetrician's palm placed against the fetal chest or rump and firm, steady pressure cranially between contractions. Once the fetus floats back into the uterine space, the malposture (flexed knee, deviated head) can be corrected.",
        "Why_Not": "Retropulsion without tocolysis (clenbuterol) is extremely difficult — the cow/mare's uterine contractions actively work against the obstetrician's corrective push. The combination of retropulsion + clenbuterol + copious lubrication is the standard of care for any obstetrical correction before forced extraction.",
        "Wow_Approach": "Retropulsion is most critical in equine dystocia where the mare's extremely powerful abdominal contractions expel the foal rapidly — the narrow equine pelvic canal combined with vigorous contractions makes correction of a malpresented foal extremely difficult. Administer 1 mg romifidine IV (deep sedation + analgesia) to safely retropulse an equine foal."
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
