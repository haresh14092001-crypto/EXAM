import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    400: {
        "topic": "VGO Short Answer Definitions - Superfetation, Superfecundation, Freemartinism",
        "Core_Anatomy": "The uterus, placenta, and ovarian cycle; multiple paternity genetics.",
        "Pathogenesis_Immediate": "Key VGO short-answer definitions: Superfecundation = fertilization of two ova from the same oestrus by two different males (different sires). Superfetation = fertilization of a new ovum during an established pregnancy (extremely rare, requires oestrus during pregnancy). Freemartinism = sterile female co-twin with a male due to placental vascular chimerism.",
        "Pathogenesis_Deep": "Superfecundation is common in dogs and cats (polyovulatory species where multiple eggs from one oestrus can be fertilized by different sires from multiple matings). DNA parentage testing can identify multiple sires in a single litter. Superfetation is biologically prevented in most species by progesterone suppression of oestrus, cervical mucus plug formation, and implantation-blocking mechanisms — it is only documented in a few species (horses rarely, humans extremely rarely).",
        "Why_Not": "Superovulation (multiple ovulation induced by FSH/eCG treatment) is a controlled biotechnological technique used in ET programmes — distinct from natural superfecundation. Superfetation would require both ovulation (despite pregnancy) AND fertilization AND implantation — three simultaneous obstacles that are almost never overcome naturally.",
        "Wow_Approach": "Superfecundation forensic case example: A Labrador bitch mated with both a Labrador and a German Shepherd in the same oestrus can produce a litter of mixed pups from two sires. This is legally significant in pedigree dog breeding and requires microsatellite DNA parentage testing for each pup to correctly register purebred vs mixed-breed offspring."
    },
    405: {
        "topic": "VGO Obstetrics Fill-in-the-Blank Key Values",
        "Core_Anatomy": "The bovine and equine birth canal, fetal membranes, and myometrial physiology.",
        "Pathogenesis_Immediate": "Key VGO 421 (Veterinary Obstetrics) fill-in values: Normal Stage 1 labour duration (cattle) = 2-6 hours. Normal Stage 2 duration (cattle) = 30 min to 2 hours. Normal Stage 3 (placental expulsion) cattle = within 12 hours. Retained Fetal Membranes (RFM) in cattle = failure to expel placenta within 12 hours.",
        "Pathogenesis_Deep": "Critical obstetrics fill-ins: Maximum allowable birth canal traction force in cattle = equivalent of 2 people pulling. Epidural anaesthesia dose = 5-10 ml of 2% Lignocaine at Co1-Co2 junction. Clenbuterol dose for uterine relaxation = 0.3 mcg/kg IV. Oxytocin dose for inertia = 20-40 IU IM. C-section indications: irreducible dystocia, absolute fetal oversize, irreducible uterine torsion (>360°), fetal monstrosities.",
        "Why_Not": "Stage 3 retention in horses = failure to expel fetal membranes within 3 hours (much shorter than cattle's 12 hours). This is because retained membranes in mares cause rapid laminitis (within 12-24 hours) due to endotoxin absorption — a true emergency requiring immediate manual removal in mares.",
        "Wow_Approach": "RFM in cattle management: Do NOT manually remove bovine retained placentas forcibly (causes endometritis from torn caruncle epithelium). Instead, administer Oxytocin (50-100 IU IM) to stimulate CL-independent myometrial contractions. Use intrauterine antibiotics (oxytetracycline pessaries). Most bovine RFM shed spontaneously within 7-10 days without manual intervention."
    },
    409: {
        "topic": "VGO Multiple Choice - Obstetrics Core MCQs",
        "Core_Anatomy": "Fetal membrane anatomy, maternal pelvic canal, and the myometrial contraction system.",
        "Pathogenesis_Immediate": "Core VGO Obstetrics MCQ facts: Most common dropsy of fetal membranes in bovines = Hydroallantois (>90% of cases). Shortest Stage 2 labour = Mare. Dystocia due to wry neck = most common in Sow. Drug for uterine relaxation = Clenbuterol. Episiotomy target = Vulva.",
        "Pathogenesis_Deep": "VGO-421 high-frequency MCQ answers: Hydroallantois > Hydroamnion in prevalence (ratio 10:1). Hydroallantois = rapid onset (days-weeks), massive fluid (up to 200L), poor prognosis for dam. Hydroamnion = slow onset (months), moderate fluid (20-50L), better prognosis. Wry neck frequency: Sow > Cow > Mare. Stage 2 duration: Mare (20-30 min) < Ewe (30-60 min) < Cow (30-120 min) < Bitch (hours).",
        "Why_Not": "Developmental anomalies peak during the embryonic period (organogenesis, Days 14-60 in cattle) — this is the most tested teratology fact. Uterine inertia is treated with Calcium + Oxytocin; Clenbuterol CANNOT treat inertia (it would worsen it). Vaginal prolapse in dogs occurs in Proestrus/Oestrus (high estrogen). These four MCQ pairs are frequently tested together.",
        "Wow_Approach": "VGO exam strategy: For any 'which species' MCQ (shortest stage 2, most susceptible to a condition, etc.), default answers by frequency: Mare = shortest stage 2. Sow = most wry neck dystocia. Bitch = most vaginal prolapse during oestrus. Buffalo = most silent heat. Cow = most RFM. Ewe = most pregnancy toxaemia (twins)."
    },
    415: {
        "topic": "Carpoprost - PGF2alpha Analogue for Uterine Contraction",
        "Core_Anatomy": "The uterine myometrium (FP prostaglandin receptors), the cervix (softening), and the corpus luteum (luteolysis).",
        "Pathogenesis_Immediate": "Carpoprost (15-methyl-PGF2alpha) is a synthetic analogue of PGF2alpha used for uterine contractions, luteolysis, and management of postpartum haemorrhage in large animals — it is more potent and longer-acting than natural dinoprost.",
        "Pathogenesis_Deep": "PGF2alpha analogues used in veterinary practice: Dinoprost tromethamine (natural PGF2alpha — Lutalyse®): standard dose 25 mg IM in cattle. Cloprostenol (ICI-80996 — Estrumate®): 0.5 mg IM, 100x more potent. Tiaprost tromethamol (Iliren®): similar potency to Cloprostenol. Carpoprost (15-methyl-PGF2alpha): higher potency and resistance to enzymatic breakdown in the lung (longer plasma half-life). All cause luteolysis, cervical softening, and myometrial contractions.",
        "Why_Not": "Clenbuterol (option D in the MCQ) is the opposite — a beta-2 agonist TOCOLYTIC that RELAXES the uterus. This is the most important distinction: all PGF2alpha analogues (Dinoprost, Cloprostenol, Tiaprost, Carpoprost) are uterotonicS; Clenbuterol is the uterine relaxant. The MCQ is testing whether you know Clenbuterol is the odd-one-out.",
        "Wow_Approach": "PGF2alpha contraindications in veterinary practice: NEVER in pregnant animals (causes abortion). NEVER in animals with bronchospasm or respiratory disease. NEVER handle by pregnant women (potent abortifacient if absorbed through skin). Always wear protective gloves and eyewear when handling prostaglandin products."
    },
    422: {
        "topic": "Vaginal Prolapse in Dogs - Proestrus and Oestrus Association",
        "Core_Anatomy": "The vaginal submucosa, the vestibulovaginal sphincter, and the vaginal floor mucosa.",
        "Pathogenesis_Immediate": "Vaginal hyperplasia/prolapse in dogs occurs exclusively during Proestrus and Oestrus — the high-estrogen phases of the cycle — when estrogenic hypertrophy and submucosal oedema cause the vaginal floor mucosa to prolapse through the vulvar opening.",
        "Pathogenesis_Deep": "Three grades of canine vaginal hyperplasia: Grade I (Type 1): Folding of vaginal mucosa within the vaginal vault — visible only on speculum examination. Grade II (Type 2): Protrusion through the vulvar lips (the classic 'donut' or 'tongue' of pink tissue at the vulva). Grade III (Type 3): Complete circumferential eversion of the vaginal vault through the vulva. Grades I-II resolve spontaneously at the end of oestrus (when estrogen falls). Grade III requires manual reduction.",
        "Why_Not": "Metestrus and anestrus are LOW-estrogen phases — vaginal prolapse does not occur. Vaginal prolapse in the cat is extremely rare (feline vaginal submucosa is less responsive to estrogen). Only during the high-estrogen proestrus/oestrus window is the canine vaginal submucosa sufficiently oedematous to prolapse.",
        "Wow_Approach": "Breed predisposition: Mastiff, Boxer, Saint Bernard, English Bulldog, Labrador. If breeding is desired from affected females, use AI (the prolapse prevents natural mating), then perform OHE after the litter is weaned to prevent recurrence. OHE is the only permanent cure."
    },
    424: {
        "topic": "Fetal Ascites as Obstetrical Complication Requiring Snare/Paracentesis",
        "Core_Anatomy": "The fetal peritoneal cavity, the umbilical vessels, the abdominal wall, and the birth canal.",
        "Pathogenesis_Immediate": "Fetal ascites (hydrops abdominalis) — excessive fluid in the fetal peritoneal cavity causing massive abdominal enlargement — is an obstetrical complication requiring drainage (paracentesis using a concealed palm knife or trocar) before delivery can proceed.",
        "Pathogenesis_Deep": "Fetal ascites causes: congenital heart failure, hepatic failure, lymphatic obstruction, haemolytic disease, or chromosomal abnormality. The massively distended fetal abdomen engages the maternal pelvic inlet but cannot pass through the birth canal. Emergency management: Insert a trocar or concealed palm knife through the fetal abdominal wall (guided by the palm inside the birth canal) and drain the ascitic fluid. Once abdominal circumference is reduced, complete the delivery by traction.",
        "Why_Not": "A snare (wire loop) is used to apply traction to a fetal limb or jaw — it does not drain fluid. A concealed palm knife is used for incision (fluid drainage, subcutaneous fetotomy). Isoxsuprine is a uterine relaxant (tocolytic used for retropulsion). Each instrument has a specific obstetrical application that must be matched to the clinical situation.",
        "Wow_Approach": "Surgical rule for fetal ascites drainage: Never drain more than 50-60% of the fluid volume rapidly — sudden decompression of the fetal abdomen causes umbilical vessel torsion and rapid fetal death if the fetus is still alive. Drain slowly and simultaneously apply gentle traction to guide delivery."
    },
    425: {
        "topic": "Third Stage of Labour - Expulsion of Fetal Membranes",
        "Core_Anatomy": "The placentomes (caruncles + cotyledons in ruminants), the chorionic villi, and the uterine contractions of Stage 3.",
        "Pathogenesis_Immediate": "The third stage of labour is the expulsion of the fetal membranes (placenta + fetal membranes) following delivery of the fetus. In cattle, this normally occurs within 12 hours post-delivery via uterine contractions and placental separation from the caruncles.",
        "Pathogenesis_Deep": "Stage 3 mechanism in cattle: After fetal delivery, oxytocin release continues (Ferguson reflex from the birth canal) maintaining uterine contractions. These contractions invert the caruncular crypts, loosening the cotyledonary-caruncular interlocking. Placentomal separation is facilitated by collagenase activity (breaking down the connective tissue between caruncle and cotyledon) and neutrophil infiltration of the caruncular epithelium. The chorioallantois is then expelled as a continuous sheet.",
        "Why_Not": "Stage 1 = cervical dilation + early myometrial contractions (2-6 hours in cattle). Stage 2 = fetal delivery (30 min to 2 hours in cattle). Stage 3 = placental expulsion (within 12 hours in cattle, within 3 hours in mares). A Stage 3 lasting >12 hours in cows = RFM requiring veterinary intervention.",
        "Wow_Approach": "RFM risk factors in cattle: Selenium deficiency (impaired neutrophil chemotaxis at the placentome). Hypocalcaemia (reduced uterine contractility). Dystocia (exhausted myometrium). Hydrops allantois (uterine over-distension). BVD virus infection (placentitis). Premature birth/abortion. Address these risk factors peripartum to reduce RFM incidence."
    },
    426: {
        "topic": "Forced Extraction and Isoxsuprine in Obstetrics",
        "Core_Anatomy": "The fetal hindlimbs, the pelvic canal, and the uterine smooth muscle.",
        "Pathogenesis_Immediate": "Forced Extraction is the obstetrical technique of applying mechanical traction (using obstetrical chains, ropes, or a calf puller/calving aid) to the fetal limbs and head to deliver the fetus when voluntary expulsive efforts are insufficient. Isoxsuprine is a beta-adrenergic agonist tocolytic used to relax the uterus during difficult obstetrical correction.",
        "Pathogenesis_Deep": "Forced extraction is indicated when: (1) The fetus is correctly presented, positioned, and postured. (2) The birth canal is adequately dilated. (3) The pelvic dimensions are sufficient. (4) Maternal expulsive efforts are failing (secondary uterine inertia). Obstetrical chains are applied above the fetlock (pastern loop) with a half-hitch below to distribute traction evenly. Maximum traction = two people or one person + mechanical calf puller (Calving-aid/Hip-lock).",
        "Why_Not": "Isoxsuprine (Duvadilan®) is a beta-2 agonist tocolytic used for uterine relaxation during obstetrical correction. It is functionally equivalent to Clenbuterol but with longer plasma half-life and less selectivity. The key matching: Forced Extraction = delivery traction technique. Isoxsuprine = tocolytic for uterine relaxation during correction.",
        "Wow_Approach": "Calving aid (mechanical calf puller / 'Dystocia Handle'): Allows controlled, measured force application with a ratchet mechanism. Provides up to 400-500 kg of force if used incorrectly — causing fatal uterine rupture and maternal death. ALWAYS use with a load-limiting mechanism and NEVER exceed the force two people can apply manually. Correct obstetrical assistance = gentle, intermittent, direction-matched traction during uterine contractions."
    },
    473: {
        "topic": "Dolly the Sheep - Somatic Cell Nuclear Transfer (SCNT) Donor Cell",
        "Core_Anatomy": "The mammary gland epithelial cell nucleus (donor), the enucleated oocyte (recipient), and the reconstructed embryo.",
        "Pathogenesis_Immediate": "Dolly (the sheep, born 1996) was the first mammal cloned from an adult somatic cell using Somatic Cell Nuclear Transfer (SCNT). The donor cell was a Mammary Gland Cell (udder/mammary epithelial cell) from a 6-year-old Finn Dorset ewe.",
        "Pathogenesis_Deep": "SCNT procedure (Ian Wilmut, Roslin Institute, 1996): (1) A mammary gland cell nucleus from a 6-year-old Finn Dorset ewe was isolated. (2) The donor cell was arrested in G0 phase by serum starvation (to synchronize cell cycle for nuclear reprogramming). (3) The nucleus was inserted into an enucleated oocyte from a Scottish Blackface ewe by electrofusion. (4) The reconstructed embryo developed in vitro and was transferred to a surrogate Scottish Blackface ewe. (5) Dolly was born with the exact nuclear genome of the Finn Dorset mammary donor.",
        "Why_Not": "Dolly was NOT cloned from: an embryonic cell (that would be embryo splitting / identical twin production), a skin fibroblast (used in subsequent SCNT experiments), or a fetal cell (Dolly used adult somatic cell reprogramming — the breakthrough was proving that adult differentiated cells could be reprogrammed). Dolly's mitochondrial DNA was from the enucleated oocyte donor.",
        "Wow_Approach": "Dolly demonstrated that differentiated adult somatic cell nuclei can be completely reprogrammed to a totipotent state by the oocyte cytoplasm — a revolution that later led to Yamanaka's discovery of induced pluripotent stem cells (iPSCs, 2006). Dolly lived only 6 years (normal sheep lifespan = 10-12 years) and suffered premature arthritis and lung disease, raising questions about epigenetic ageing in clones."
    },
    501: {
        "topic": "Ergotamine - Uterine Contraction Drug for Postpartum Haemorrhage",
        "Core_Anatomy": "The uterine myometrium (alpha-adrenergic and serotonin receptors), the spiral uterine arteries, and the postpartum uterus.",
        "Pathogenesis_Immediate": "Ergotamine (an ergot alkaloid) causes sustained uterine smooth muscle contraction via alpha-adrenergic and serotonin receptor agonism, used for treating postpartum haemorrhage by compressing uterine blood vessels and preventing/stopping uterine bleeding.",
        "Pathogenesis_Deep": "Ergotamine acts on uterine alpha-1 adrenergic receptors and 5-HT2 serotonin receptors → sustained tonic contraction of the uterine body and cervix → mechanical compression of uterine spiral arteries → haemostasis. Unlike oxytocin (which causes rhythmic contractions), ergotamine produces a sustained tonic contraction, making it more effective for haemostasis but contraindicated for stimulating labour (the sustained tone would compromise fetal oxygenation).",
        "Why_Not": "Progesterone suppresses uterine contractions (promotes uterine quiescence during pregnancy). Estrogen increases uterine sensitivity to oxytocin. Isoxsuprine is a beta-2 agonist tocolytic (relaxes uterus). Ergotamine is uniquely the sustained uterotonic used specifically for postpartum haemorrhage — NOT for labour induction.",
        "Wow_Approach": "Ergotamine/Ergometrine contraindications: NEVER use during active labour (causes tetanic uterine contractions causing fetal asphyxia). NEVER in hypertensive animals (causes vasoconstriction + hypertension). Use ONLY AFTER delivery of the placenta is confirmed. Standard postpartum haemorrhage protocol: Oxytocin (immediate) → Ergotamine (sustained) → PGF2alpha (if both fail)."
    },
    502: {
        "topic": "Episiotomy for Vulval Stenosis During Parturition",
        "Core_Anatomy": "The vulvar commissure, the perineal body, and the vestibulovaginal junction.",
        "Pathogenesis_Immediate": "Vulval stenosis (abnormal narrowing of the vulvar opening) is corrected during parturition by Episiotomy — a surgical incision of the vulvar commissure (typically the dorsal commissure) to enlarge the birth canal opening and allow delivery of the fetus.",
        "Pathogenesis_Deep": "Episiotomy specifically for vulval stenosis: Most commonly required in: (1) Mares with prior Caslick's suture that was not removed before foaling (the sutured vulvar commissure tears catastrophically if not opened). (2) Heifers with underdeveloped vulva relative to fetal size. (3) Animals with post-traumatic vulvar scarring/adhesions. The incision is made with scissors at the 12 o'clock position, extending 3-5 cm dorsally through the vulvar commissure and perineal skin.",
        "Why_Not": "Cervicotomy (incision of the cervix) is used to enlarge a stenotic cervix that prevents fetal passage — distinct from vulval stenosis. Laparotomy is abdominal surgery (C-section approach). Tubectomy is surgical occlusion of the fallopian tubes. Only Episiotomy addresses vulvar/vestibular stenosis.",
        "Wow_Approach": "Critical Caslick's rule: Any mare with a previous Caslick's operation MUST have the suture opened (Episiotomy) at least 4-6 weeks before the expected foaling date, or as an emergency at the onset of Stage 2 labour if forgotten. A closed Caslick's suture during Stage 2 labour causes perineal tearing from Stage 2 pressure — a preventable, devastating complication."
    },
    503: {
        "topic": "Species with Silent Estrus - Buffalo as the Classic Example",
        "Core_Anatomy": "The hypothalamus (GnRH pulse generator), the limbic system (behavioural response to estrogen), and the GnRH-LH axis.",
        "Pathogenesis_Immediate": "Buffalo (Bubalus bubalis) is the species most classically associated with Silent Estrus (suboestrus) — where ovulation occurs without overt behavioural signs of estrus, causing missed breeding opportunities especially during summer months.",
        "Pathogenesis_Deep": "Silent estrus in buffaloes: The buffalo's hypothalamic GnRH pulse generator and limbic system are more sensitive to thermal stress and negative energy balance than cattle. In summer (>35°C), heat stress suppresses hypothalamic estrogen receptor expression, reducing the behavioral response to the pre-ovulatory estrogen surge despite normal follicular development and LH surge. The result is ovulation (confirmed by progesterone rise) without any observable standing behavior.",
        "Why_Not": "While silent estrus occurs in all species under stress, it is MOST prevalent and most clinically important in buffaloes during summer. Dairy cows can also show silent estrus (up to 20% of cycles), but cows show secondary signs (clear cervical mucus, vulvar swelling) more reliably than buffaloes. The buffalo's naturally shorter estrus duration (12-18 hours vs 18-24 hours in cattle) further reduces detection opportunity.",
        "Wow_Approach": "Buffalo estrus detection methods: (1) Teaser bull (vasectomized or semen-diverted): 90-minute morning and evening observation periods. (2) Progesterone ELISA from milk: confirms luteal phase by Day 7 post-AI. (3) Ultrasonography: follicle >12 mm = dominant follicle ready for ovulation. (4) GnRH-based ovulation synchronization (Ovsynch protocol adapted for buffaloes) eliminates the need for estrus detection entirely."
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

# Final validation
with open(db_path, "r", encoding="utf-8") as f:
    c2 = f.read()
d2 = json.loads(re.sub(r'^.*?const examData = ', '', c2, flags=re.DOTALL).rsplit(';',1)[0].strip())
empty2 = [x for x in d2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries. {len(empty2)} high-yield questions still empty.")
