import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1392: {
        "topic": "Pre-Parturition Endocrinology - Progesterone Withdrawal",
        "Core_Anatomy": "Maternal corpus luteum, placenta, and systemic blood.",
        "Pathogenesis_Immediate": "Prior to parturition, the blood progesterone level must plummet to baseline to remove the 'progesterone block' on the myometrium, allowing uterine contractions to begin.",
        "Pathogenesis_Deep": "Progesterone hyperpolarizes the myometrial smooth muscle cells, keeping the uterus quiescent throughout pregnancy. For parturition to occur, fetal cortisol stimulates placental enzymes to convert progesterone into estrogen (and stimulates PGF2-alpha to lyse the CL). The rapid drop in progesterone and the simultaneous spike in estrogen upregulates oxytocin receptors and gap junctions in the myometrium, shifting it from a quiescent state to an actively contracting state.",
        "Why_Not": "If blood progesterone remains elevated (e.g., due to a persistent CL or exogenous administration), the female cannot go into labor, resulting in a prolonged gestation and fetal giantism.",
        "Wow_Approach": "To predict calving in a cow within 24 hours: take a blood sample or measure rectal temperature. A sudden drop in rectal temperature (by 0.5-1°C) corresponds directly with the systemic luteolytic drop in progesterone."
    },
    1393: {
        "topic": "Uterine Torsion - Post-Cervical Twist (Repeated MCQ)",
        "Core_Anatomy": "Gravid uterine horn, cervix, and anterior vagina.",
        "Pathogenesis_Immediate": "The most common anatomical location for the twist in bovine uterine torsion is Post-Cervical (involving the anterior vagina).",
        "Pathogenesis_Deep": "In the cow, the broad ligaments do not attach to the cervix or vagina. When the massive, heavy gravid uterine horn flips over itself, the twisting force is transmitted caudally. Because the cervix is relatively rigid but unattached, the twist typically occurs just caudal to the cervix, in the highly elastic anterior vagina. This is termed a 'post-cervical' torsion.",
        "Why_Not": "Pre-cervical torsion (cranial to the cervix) occurs occasionally in cows but is much rarer. Post-cervical is the textbook standard for bovines.",
        "Wow_Approach": "You can easily diagnose a post-cervical torsion without even touching the uterus: simply insert a hand into the vagina. If the vaginal walls form a tight, spiraling corkscrew cone that blocks your hand from reaching the cervix, you have a post-cervical torsion."
    },
    1394: {
        "topic": "Transverse Presentation Dystocia - The Mare",
        "Core_Anatomy": "Equine uterus, maternal pelvic inlet, and fetal long axis.",
        "Pathogenesis_Immediate": "Dystocia due to a Transverse presentation is most commonly seen in the Mare compared to other large domestic species.",
        "Pathogenesis_Deep": "The equine fetus has extremely long limbs and neck. Unlike the cow (where the fetus normally aligns longitudinally early on), the equine fetus remains highly mobile in the large, spherical body of the uterus until late gestation. If the foal fails to orient longitudinally before the powerful Stage 2 contractions begin, it can become jammed sideways (transverse) across the pelvic inlet. This is a catastrophic dystocia because the mare's explosive abdominal contractions will quickly crush the foal or rupture the uterus.",
        "Why_Not": "Cows and buffaloes have long, narrow uterine horns that naturally force the fetus into a longitudinal presentation. Transverse presentations in ruminants are exceptionally rare.",
        "Wow_Approach": "Correcting a transverse presentation in a mare is an absolute emergency. Administer heavy sedation and epidural anesthesia to stop her violent straining, then perform a Version (turning the fetus on its transverse axis) to align the head and forelimbs with the canal."
    },
    1395: {
        "topic": "Semen Antioxidants - Melatonin Supplementation",
        "Core_Anatomy": "Sperm plasma membrane and seminal extender.",
        "Pathogenesis_Immediate": "The damaging effects of Reactive Oxygen Species (ROS) during semen preservation can be prevented by the addition of potent antioxidants like Melatonin to the extender.",
        "Pathogenesis_Deep": "During cryopreservation, cold shock and osmotic stress cause mitochondria to leak ROS (superoxide, hydrogen peroxide). Because sperm membranes are rich in polyunsaturated fatty acids, ROS rapidly causes lipid peroxidation, destroying motility and DNA integrity. Melatonin is a highly lipophilic, powerful free-radical scavenger that crosses the sperm membrane, neutralizing ROS and upregulating endogenous enzymes like SOD and catalase.",
        "Why_Not": "Prostaglandin causes smooth muscle contraction. Oxytocin triggers milk letdown and myometrial contraction. Neither possesses antioxidant properties to protect sperm cells from oxidative stress.",
        "Wow_Approach": "Adding Melatonin (at 1-2 mM concentrations) to buck or ram semen extenders significantly improves post-thaw progressive motility and acrosome integrity, making it a cutting-edge additive in modern AI centers."
    },
    1396: {
        "topic": "Penetrating Cryoprotectants - Glycerol and DMSO",
        "Core_Anatomy": "Sperm/embryo plasma membrane and intracellular cytoplasm.",
        "Pathogenesis_Immediate": "Examples of penetrating cryoprotectants include Glycerol, DMSO (Dimethyl sulfoxide), and Ethylene glycol.",
        "Pathogenesis_Deep": "Cryoprotectants are classified by their ability to cross the lipid bilayer: (1) Penetrating cryoprotectants (Glycerol, DMSO) have low molecular weights. They enter the cytoplasm, displace water, and lower the freezing point, preventing lethal intracellular ice crystal formation. (2) Non-penetrating cryoprotectants (Sugars like sucrose or trehalose) are large molecules that remain outside the cell, creating an osmotic gradient that actively dehydrates the cell before freezing.",
        "Why_Not": "Ethyl alcohol is a toxic solvent, not a cryoprotectant. Non-penetrating sugars do not enter the cell.",
        "Wow_Approach": "Glycerol is the gold standard for freezing sperm. DMSO is the gold standard for freezing embryos and tissue cultures because it penetrates much faster than glycerol, preventing osmotic shock in large cell masses."
    },
    1397: {
        "topic": "Sperm Abnormalities - Permissible Head Defect Limits",
        "Core_Anatomy": "Sperm head (acrosome and nucleus).",
        "Pathogenesis_Immediate": "In a normal, good quality bovine ejaculate, strict morphological guidelines permit no more than 5 to 10 per cent of severe head abnormalities.",
        "Pathogenesis_Deep": "Morphological defects are strictly quantified during a Breeding Soundness Exam (BSE). Total abnormalities should not exceed 30% (requiring >70% normal sperm). However, primary defects (which originate in the testis and include severe head defects like pyriform, diadem, or knobbed acrosomes) are much more detrimental to fertility than secondary tail defects. Therefore, the threshold for primary head abnormalities is much stricter (typically capping at 5-10%).",
        "Why_Not": "Permitting 20-30% head abnormalities would indicate active testicular degeneration, and the bull would fail the BSE. A limit of 2% is unrealistically strict for a biological system.",
        "Wow_Approach": "To accurately count head defects, you must use a high-magnification (1000x oil immersion) differential interference contrast (DIC) microscope or stain with Eosin-Nigrosin, examining exactly 200 individual sperm cells."
    },
    1398: {
        "topic": "Cryobiology - The Period of Supercooling",
        "Core_Anatomy": "Intracellular water and cryoprotectant medium.",
        "Pathogenesis_Immediate": "During the freezing of semen, the period of supercooling (where water remains liquid below its normal freezing point) occurs approximately between 0°C to -5°C.",
        "Pathogenesis_Deep": "As the semen straw is cooled, the extracellular water does not immediately freeze at 0°C due to the dissolved solutes and cryoprotectants (supercooling). Between -5°C and -15°C, ice nucleation finally begins. This is a critical danger zone because as extracellular ice forms, pure water is removed, leaving behind a hyperosmotic, highly toxic solute brine that severely dehydrates the sperm cell before it finally crosses the glass transition temperature.",
        "Why_Not": "The range of -15°C to -64°C is the critical recrystallization danger zone. Supercooling strictly refers to the initial sub-zero liquid phase before nucleation.",
        "Wow_Approach": "Modern programmable freezers use 'seeding' (a sudden burst of liquid nitrogen vapor) to intentionally force ice nucleation at exactly -5°C, preventing extreme supercooling and subsequent osmotic shock."
    },
    1399: {
        "topic": "Bovine Seminal Plasma (BSP) Proteins - Vesicular Origin",
        "Core_Anatomy": "Seminal vesicles (vesicular glands) and sperm plasma membrane.",
        "Pathogenesis_Immediate": "Bovine seminal plasma proteins (BSP proteins) are synthesized and secreted primarily by the Seminal Vesicles.",
        "Pathogenesis_Deep": "BSP proteins (BSP-A1/A2, BSP-A3, and BSP-30-kDa) constitute the major protein fraction of bull seminal plasma. Upon ejaculation, these proteins bind to choline phospholipids on the sperm membrane. They play a dual role: they protect the sperm during transit, but they also promote cholesterol efflux, meaning they are the primary biochemical triggers for sperm capacitation in the female tract.",
        "Why_Not": "The prostate and cowper's glands secrete minor volumes of cleansing fluid. The epididymis secretes maturation proteins (like forward motility protein), not BSPs.",
        "Wow_Approach": "Because BSP proteins trigger capacitation, prolonged exposure to seminal plasma is actually detrimental to sperm storage. This is why highly concentrated BSPs reduce the freezeability of bull semen, and why semen extenders must heavily dilute the native plasma."
    },
    1400: {
        "topic": "Primary Sperm Abnormalities - Testicular Origin (Repeated)",
        "Core_Anatomy": "Seminiferous tubules and germ cells.",
        "Pathogenesis_Immediate": "Primary sperm abnormalities (such as double heads, pyriform heads, and diadem defects) arise exclusively during spermatogenesis in the Testes.",
        "Pathogenesis_Deep": "Primary abnormalities represent true testicular dysfunction, arising due to mitotic or meiotic disturbances in the seminiferous epithelium. Secondary abnormalities arise during transit in the epididymis (detached heads, distal droplets), while tertiary defects are handling-induced (cold shock).",
        "Why_Not": "The epididymis and vas deferens are transport ducts; they do not determine head shape or nuclear abnormalities, which are fixed during chromatin condensation in the testis.",
        "Wow_Approach": "If a bull has >15% primary defects, it indicates testicular degeneration or heat stress. Because they arise in the testes, a minimum of 60 days of sexual rest is required for any potential improvement."
    },
    1401: {
        "topic": "Gamete Aging - Fertilization Failure Combinations",
        "Core_Anatomy": "Oocyte vitelline membrane, zona pellucida, and sperm chromatin.",
        "Pathogenesis_Immediate": "The worst outcomes in fertilization (embryonic death, polyspermy) occur when the combination involves an 'Aged egg and fresh sperm' or 'Fresh egg and aged sperm'.",
        "Pathogenesis_Deep": "Gametes have a strictly limited viable lifespan. (1) Oocytes are viable for only 8-12 hours post-ovulation. If fertilization is delayed (Aged egg), the zona pellucida hardens, and the cortical granules prematurely discharge. When a fresh sperm finally penetrates, the block to polyspermy fails, leading to triploidy and early embryonic death. (2) Sperm are viable for 24-48 hours. Aged sperm suffer lipid peroxidation and DNA fragmentation, failing to decondense properly inside the fresh oocyte.",
        "Why_Not": "The only acceptable, fertile combination is a Freshly ovulated egg meeting Freshly capacitated sperm in the ampulla.",
        "Wow_Approach": "This is why AI timing is so critical in cattle: inseminating too late (after ovulation) guarantees the sperm will meet an Aged Egg, resulting in an immediate drop in conception rates from 60% down to 20%."
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
