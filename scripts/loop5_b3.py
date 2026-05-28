import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    566: {
        "topic": "Fetal Glucocorticoid (Cortisol) Role in Initiating Parturition",
        "Core_Anatomy": "The fetal adrenal cortex (zona fasciculata), the fetoplacental steroidogenic enzymes, and the maternal myometrium.",
        "Pathogenesis_Immediate": "In most domestic species (cattle, sheep, goats), rising fetal cortisol production by the maturing fetal adrenal gland is the primary trigger that initiates parturition by converting the fetoplacental unit from progesterone to estrogen production, leading to PGF2alpha release and myometrial contractions.",
        "Pathogenesis_Deep": "Fetal cortisol cascade in sheep (classic model): Mature fetal hypothalamus-pituitary-adrenal axis → cortisol surge in the last 2 weeks → cortisol induces placental 17α-hydroxylase enzyme → placenta converts progesterone → estrogen (instead of maintaining progesterone). Estrogen surge → endometrial PGF2alpha release → CL regression in ewes (CLs are still functional at term in sheep). PGF2alpha + estrogen → myometrial OTR upregulation → oxytocin-driven contractions → parturition.",
        "Why_Not": "In the mare, the fetoplacental unit controls parturition primarily through estrogen (from fetal gonads, which are massively developed in horses) and PGF2alpha, with cortisol playing a secondary role. In pigs, progesterone withdrawal from the CL (driven by PGF2alpha) is the primary trigger. The cortisol-driven mechanism is specifically well-established in ruminants.",
        "Wow_Approach": "Dexamethasone (synthetic glucocorticoid) induction of parturition: Inject 10-20 mg dexamethasone IM in cattle on Day 265-275 of gestation → mimics the fetal cortisol surge → initiates the parturition cascade. Parturition occurs within 24-72 hours. Used for management convenience but associated with increased RFM rate (immature placentome separation mechanism)."
    },
    569: {
        "topic": "Endometrial Cups and eCG Production in Mares - Day 36-120",
        "Core_Anatomy": "The chorionic girdle cells (equine trophoblast), the endometrial stroma (invasion site), and the maternal immune system (tolerance mechanism).",
        "Pathogenesis_Immediate": "Endometrial Cups in mares form between Days 36-40 of gestation when chorionic girdle cells from the equine conceptus invade the uterine endometrial stroma, forming discrete cup-shaped structures that produce eCG (Equine Chorionic Gonadotropin, formerly PMSG) from Days 40-120.",
        "Pathogenesis_Deep": "eCG function: Has both FSH-like and LH-like activity in the mare. FSH-like activity → secondary follicle development → accessory CLs form. LH-like activity → maintains primary and accessory CLs → progesterone maintained until the fetoplacental unit takes over at Day 100-120. After Day 120, the endometrial cups are rejected by the maternal immune system (despite the unique immune tolerance mechanism earlier), and eCG production ceases. The cups persist as necrotic scars for several weeks.",
        "Why_Not": "eCG (PMSG) production is UNIQUE to equids — no other domestic species produces a gonadotropin from the placenta. In cattle, the trophoblast produces bCSP (bovine Chorionic Somatomammotropin Protein) which has weak prolactin-like activity — completely different from eCG. The endometrial cups are also unique to Equidae — no equivalent in ruminants or other domestic species.",
        "Wow_Approach": "eCG (Pregnant Mare Serum Gonadotropin — PMSG) is commercially extracted from the serum of pregnant mares (Days 55-90) and used widely in veterinary reproductive biotechnology: superovulation induction in sheep, goats, and cattle; synchronization of cyclic and non-cyclic ewes for ET programs; puberty advancement in gilts. The animal welfare of collection mares is regulated under EU Directive 2010/63/EU."
    },
    571: {
        "topic": "Post-Cervical Uterine Torsion - Parts Involved",
        "Core_Anatomy": "The uterine body, the uterine horns (both), the broad ligaments, and the cervix.",
        "Pathogenesis_Immediate": "Post-cervical uterine torsion in cattle involves BOTH the Uterus AND Cervix — the torsion point is at or cranial to the cervix, causing the entire uterine body + cervix to rotate as a unit. This is the most common type of uterine torsion in cattle (>90% of cases).",
        "Pathogenesis_Deep": "Classification of uterine torsion by location: (1) Post-cervical (supra-cervical) torsion — twist at or cranial to the cervix; involves uterus + cervix. Most common in cattle. (2) Pre-cervical (infra-cervical) torsion — twist between the cervix and the vagina; involves the vagina. Less common. Degree: <180°, 180°, 270°, 360° rotations. Most bovine torsions are 180-270° post-cervical, confirmed by Fincher's test (twisted broad ligaments palpable vaginally).",
        "Why_Not": "Post-cervical torsion involves BOTH uterus and cervix (not uterus alone, not cervix alone). The broad ligaments rotate with the uterus, compressing the utero-ovarian vasculature and causing progressive uterine ischaemia. The longer the torsion goes uncorrected, the greater the vascular compromise and the lower the survival rate for both dam and fetus.",
        "Wow_Approach": "Time-sensitivity: Uterine torsion > 12 hours without correction causes fetal death (hypoxia). Torsion > 24 hours causes uterine wall necrosis. Attempt Schaffer's Rolling Method first (success in 70-85% of <180° torsions). If rolling fails after 2 attempts, proceed immediately to laparotomy (left or right paralumbar fossa approach, manual detorsion through the uterine wall)."
    },
    572: {
        "topic": "Merged Stage 2 and Stage 3 Labour in Polytocous Animals",
        "Core_Anatomy": "The multiple fetuses, multiple placentas (or single zonary/diffuse placenta), and the multi-phasic uterine contraction pattern.",
        "Pathogenesis_Immediate": "In polytocous animals (pigs, dogs, cats, rabbits), Stage 2 (fetal expulsion) and Stage 3 (placental expulsion) are merged — individual placentas are expelled either immediately after each neonate or in clusters between neonates, rather than in a distinct third stage after ALL fetuses are delivered.",
        "Pathogenesis_Deep": "Polytocous parturition pattern: Each fetus is usually expelled with its own placenta (born within the fetal membranes or immediately followed by them). In pigs: a placentas may be delivered in groups of 2-3, interleaved with piglet deliveries. In dogs: placenta typically follows each pup within 5-15 minutes of birth. In cats: similar to dogs. Total Stage 3 duration: merges with Stage 2, extending over the entire multi-hour delivery period.",
        "Why_Not": "Monotocous animals (cattle, horses, sheep, goats — single offspring species) have distinct sequential stages: Stage 2 (single fetus delivery) is complete before Stage 3 (single placenta expulsion) begins. In cattle: Stage 2 ends, then Stage 3 takes 2-12 hours. The merged Stage 2/3 in polytocous species is why RFM is assessed differently — all placentas must be passed within 4 hours post-last-pup in bitches.",
        "Wow_Approach": "Assess placental completeness in polytocous delivery: Count neonates + count placentas. If neonate count > placenta count, a retained placenta is present. In bitches, some dams consume placentas immediately — keep the dam from consuming placentas during observation to allow accurate counting. Retained placenta in bitches: administer oxytocin 2-5 IU IM + refer for ultrasonography to confirm."
    },
    573: {
        "topic": "Fetal Cadavers - Maceration and Mummification Definitions",
        "Core_Anatomy": "The fetal integument, bones, and soft tissues; the uterine environment (sterile vs infected).",
        "Pathogenesis_Immediate": "Fetal cadavers in utero undergo two distinct pathological processes: (1) Maceration — fetal death followed by bacterial contamination (open cervix allows ascending infection), causing liquefaction and softening of fetal tissues with putrid fluid accumulation. (2) Mummification — fetal death in a sterile, closed-cervix environment, causing progressive dehydration and preservation.",
        "Pathogenesis_Deep": "Macerated fetus (open cervix): Ascending bacteria (E. coli, Streptococcus, Clostridia) enter the uterus after fetal death. Bacterial proteases and lipases liquefy soft tissues, leaving bones and skin fragments in a fluid-filled uterus. Clinical sign: mucopurulent vulvar discharge, maternal anorexia, fever. Manage with oxytocin + cervical dilators (estrogen) + manual removal of fetal remnants. Mummified fetus (closed cervix): No bacterial entry → fetal tissues dehydrate → compact, firm, leather-like mummification. No clinical signs until persistent anoestrus detected.",
        "Why_Not": "An emphysematous fetus is caused by gas-producing bacteria (Clostridia) invading a dead fetus in utero — the carcass swells with gas (subcutaneous emphysema), feeling crepitant on palpation. This is distinct from both maceration (liquid putrefaction) and mummification (dry preservation). Emphysematous fetuses are extremely difficult to deliver without fetotomy.",
        "Wow_Approach": "Mummification diagnosis: Rectal palpation reveals a hard, firm, compact uterine mass (the mummified fetus) without any fluid fluctuation. The uterus is small relative to the expected gestational age because the fluid has been reabsorbed. Ultrasonography: highly echogenic fetal parts without amniotic fluid. Induce cervical dilation with estrogen (5-10 mg estradiol cypionate IM) + oxytocin 24-48 hours later to facilitate expulsion."
    },
    574: {
        "topic": "Wry Neck Dystocia - Most Common in Sows (Repeated High-Yield)",
        "Core_Anatomy": "The fetal cervical vertebrae (torticollis), the pelvic canal of the sow, and the intrinsic narrowness of the porcine birth canal.",
        "Pathogenesis_Immediate": "Dystocia due to Wry Neck (torticollis — lateral deviation of the fetal neck and head) is most common in SOWS (pigs) due to the narrow, tubular porcine birth canal combined with the high prevalence of congenital vertebral column anomalies in pigs.",
        "Pathogenesis_Deep": "Wry neck pathogenesis in pigs: Congenital cervical vertebral malformation (genetic, or teratogenic) causes permanent lateral deviation of the fetal head. When the sow delivers in anterior presentation, the rotated head prevents the shoulder from entering the pelvic inlet — the shoulder impacts while the deviated head blocks the contralateral side. Correction: lubricate generously, introduce the arm into the vagina, palpate the deviated chin, manually straighten the neck, advance the muzzle onto the forelimbs, apply gentle traction.",
        "Why_Not": "In mares, the large single foal usually presents in normal anterior presentation. Equine dystocia from wry neck occurs (carpal flexion and poll-head deviation are more common in horses). In cows, head and neck deviations occur but the larger bovine birth canal allows more room for correction. Only in sows does the combination of narrow canal + high congenital defect prevalence make wry neck the leading cause of malpresentation dystocia.",
        "Wow_Approach": "In commercial swine operations, >80% of farrowing is unassisted. However, when assistance is needed, porcine obstetrics is challenging: the sow's vulva is small, the vaginal canal is narrow, and the multiple piglets mean that one stuck piglet blocks all subsequent deliveries. A stuck piglet for >30 minutes causes uterine tetany and death of all remaining piglets. Time is critical — act immediately."
    },
    576: {
        "topic": "Fistulous Tract - Tubular Abnormal Communication in Reproductive Tract",
        "Core_Anatomy": "The perineal body, the rectal wall, the vaginal wall, and the uterovesical junction.",
        "Pathogenesis_Immediate": "A Fistulous Tract is an abnormal tubular communication between two organs or between an organ and the body surface, lined by epithelium (distinguishing it from a sinus, which is a blind-ended track). In veterinary obstetrics, the most common is the rectovaginal fistula (perineal laceration during parturition creating a fistula between rectum and vagina).",
        "Pathogenesis_Deep": "Rectovaginal fistula formation: During Stage 2 labour (especially in mares), if the fetal hooves puncture the dorsal vaginal wall instead of the perineal body, the hoof tip enters the rectum and tears through the rectovaginal septum. The resulting tear connects the rectal lumen to the vaginal vault. Clinical consequence: faecal contamination of the vagina → ascending endometritis → infertility → permanent if untreated.",
        "Why_Not": "Open cervix with dead fetus indicates pyometra (open-cervix type) or maceration — not fistulous tract. Sclerotic metritis is associated with leathery placenta. Uterine involution is associated with the post-partum uterine recovery period. Fistulous tract is matched to the abnormal communication/tunnel between two compartments.",
        "Wow_Approach": "Rectovaginal fistula repair in mares: Allow the tear to heal as fibrous tissue for 4-6 weeks before surgical repair (the fresh tear edges are too inflamed to hold sutures). Surgery: retrovaginal sphincteroplasty — reconstruct the rectovaginal septum and perineal body in two stages. Success rate: 70-80% with a skilled surgical approach. Prevention: Caslick's operation reduces perineal damage risk; proper obstetrical assistance avoids fistula formation."
    },
    577: {
        "topic": "Ferguson's Reflex and Uterine Involution Matching",
        "Core_Anatomy": "The myometrium, the endometrium, and the post-partum uterine remodelling system.",
        "Pathogenesis_Immediate": "Matching: Ferguson's Reflex → Oxytocin release (reflex triggered by cervicovaginal distension causing pituitary oxytocin release). Caslick's Operation → Pneumovagina correction. Fistulous Tract → Open communication between body cavities. Uterine Involution → the post-partum reduction of the uterus to its pre-pregnancy size.",
        "Pathogenesis_Deep": "Uterine involution: After calving in cattle, the uterus involutes from 8-10 kg (gravid) to 0.5-1 kg (non-pregnant) over 25-35 days. Process: (1) Myometrial autolysis (PGF2alpha-driven contraction and myocyte reduction). (2) Caruncular autolysis (necrosis and sloughing of post-partum caruncles — the basis of lochia). (3) Cervical involution (closing over 4-5 days). (4) Endometrial regeneration (luminal epithelium restored by Day 25-35). Complete uterine involution is required before conception — minimum voluntary waiting period after calving = 40-60 days.",
        "Why_Not": "Sclerotic Metritis → Leathery Placenta (irreversible fibrosis — NOT uterine involution). Uterine involution is a NORMAL physiological post-partum process. Sclerotic metritis is a PATHOLOGICAL outcome of repeated infections. These two must be sharply distinguished in matching questions.",
        "Wow_Approach": "Uterine involution assessment by rectal palpation: Week 1 = uterus extends into pelvic cavity, asymmetric (gravid horn larger). Week 2 = both horns equal in size, still in pelvic cavity. Week 3 = uterus fully returned to abdominal position, symmetrical, reduced. Week 4-5 = complete involution, uterus feels like a non-pregnant cow. Delayed involution (still enlarged at Day 35+) indicates subclinical endometritis — check for cervical discharge."
    },
    589: {
        "topic": "Dropsy of Amniotic Sac - Hydroamnion Associated with Defective Swallowing",
        "Core_Anatomy": "The amniotic cavity, the fetal oral cavity and pharynx (swallowing mechanism), the fetal oesophagus, and the amniotic fluid dynamics.",
        "Pathogenesis_Immediate": "Dropsy of the Amniotic Sac (Hydroamnion) is associated with defective fetal swallowing — when the fetus cannot swallow amniotic fluid (due to neural defects, oesophageal atresia, or palatoschisis), the fluid accumulates excessively in the amniotic cavity.",
        "Pathogenesis_Deep": "Normal amniotic fluid balance: The fetus continuously swallows amniotic fluid (200-500 ml/day at term in cattle) and excretes it via the fetal kidneys into the allantoic cavity. Fetal lung fluid also contributes to amniotic fluid. If swallowing is impaired (lower brainstem defect, oesophageal atresia, cleft palate), amniotic fluid accumulates → hydroamnion. Conversely, hydroallantois results from RENAL problems (excess urine production) or placental dysfunction — not swallowing defects.",
        "Why_Not": "Hydroallantois (dropsy of the allantoic sac) is caused by PLACENTAL dysfunction (failure of allantoic fluid reabsorption) or fetal renal abnormalities — not swallowing defects. The key differential: Hydroamnion = fetal SWALLOWING defect (amniotic fluid not processed). Hydroallantois = PLACENTAL/RENAL problem (allantoic fluid overproduced or not reabsorbed). This distinction is the most commonly tested MCQ in VGO dropsy questions.",
        "Wow_Approach": "Ultrasonographic differentiation: Hydroamnion — fluid is immediately surrounding the fetus (amniotic cavity expansion visible around fetal body); fetus visible in the centre of the fluid. Hydroallantois — massive fluid fills the entire abdominal cavity (allantoic compartment), pushing the fetus to one side; the fluid appears uniformly distributed throughout the entire uterus."
    },
    592: {
        "topic": "Stage 1 Labour - Cervical Dilation and Preparatory Contractions",
        "Core_Anatomy": "The uterine cervix (collagen remodelling, prostaglandin-mediated), the uterine circular and longitudinal myometrium, and the fetal membranes.",
        "Pathogenesis_Immediate": "Stage 1 of labour comprises cervical dilation (ripening) and the beginning of uterine myometrial contractions — in cattle, Stage 1 lasts 2-6 hours and ends when the cervix is fully dilated (10+ cm) to allow fetal passage.",
        "Pathogenesis_Deep": "Stage 1 events: (1) Rising PGF2alpha and relaxin causes cervical collagen remodelling (loosening of collagen cross-links → cervix softens and dilates). (2) Oxytocin from the posterior pituitary (Ferguson's reflex from early fetal pressure) initiates irregular uterine contractions. (3) The allantochorion ('first water bag') moves toward the cervix, acting as a hydraulic dilator. (4) Restlessness, pawing, flank watching, frequent urination, dropping of milk ('bagging up' in dairy cattle).",
        "Why_Not": "Stage 2 (active fetal expulsion) begins when the cervix is fully dilated AND the fetus is engaged in the pelvic canal. Stage 3 (placental expulsion) begins after fetal delivery. Stage 1 is specifically the preparatory phase — no fetal parts are visible at the vulva, only the water bag (allantochorion). In heifers, Stage 1 can last 6-12 hours due to a tighter cervix.",
        "Wow_Approach": "Clinical assessment during Stage 1: Check cervical dilation every 30-60 minutes. A cervix dilating from 1 finger (2 cm) to 4-5 fingers (10+ cm) over 2-4 hours is progressing normally. A cervix dilating slower than 1 cm/hour indicates primary cervical inertia — administer estrogen (to ripen the cervix) + oxytocin (to stimulate contractions) and monitor closely."
    },
    593: {
        "topic": "Post-Cervical Uterine Torsion - Uterus and Cervix Both Involved",
        "Core_Anatomy": "The uterine body, the cervix, and the broad ligaments in post-cervical torsion.",
        "Pathogenesis_Immediate": "In post-cervical uterine torsion (the most common type in cattle), both the Uterus AND Cervix are involved — the torsion point is at the level of or cranial to the cervix, causing both organs to rotate as a single unit.",
        "Pathogenesis_Deep": "Post-cervical torsion (most common in cattle — 90%+): The gravid uterine horn rotates around the cervico-vaginal axis. Both the uterus and cervix rotate together. The broad ligaments twist and compress. Fincher's test reveals broad ligament twisting visible in the vagina. Treatment: Schaffer's rolling method (>70% success for <180° torsions). If failed: laparotomy through the left or right paralumbar fossa, manual detorsion through the uterine wall.",
        "Why_Not": "Pre-cervical (vaginal) torsion involves the vagina between the cervix and vulva — extremely rare in cattle. A torsion involving the uterus ALONE without cervical rotation is not possible anatomically — the cervix is the pivot point of the entire torsion, so it must be involved in post-cervical torsion.",
        "Wow_Approach": "Laparotomy for failed Schaffer's: Under epidural + paralumbar block, make a right flank incision. Identify the twisted uterus — the direction of the broadligament torsion confirms the rotation direction. Place both hands around the uterus and rotate it in the CORRECTION direction (opposite to torsion). Monitor fetal viability by checking for fetal heartbeat with hand on uterine wall. Post-correction: deliver calf vaginally or proceed to C-section."
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
