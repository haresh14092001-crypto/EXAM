import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1402: {
        "topic": "Semen Equilibration - 4°C Constant",
        "Core_Anatomy": "Sperm plasma membrane and intracellular cytoplasm.",
        "Pathogenesis_Immediate": "The standard equilibration temperature for processing and freezing bull semen is 4°C.",
        "Pathogenesis_Deep": "After raw semen is diluted with a warm (37°C) glycerol-containing extender, it is slowly cooled to 4°C over 2 hours. Once at 4°C, it must undergo 'equilibration' for an additional 2 to 4 hours. At this specific temperature (4°C), cellular metabolism is drastically reduced (saving energy), but the membrane remains just fluid enough to allow the large glycerol molecules to slowly penetrate the cell and bind intracellular water, preparing the sperm for deep-freezing.",
        "Why_Not": "-10°C or -4°C would freeze the extracellular water before glycerol has penetrated, causing fatal osmotic shock. 10°C leaves metabolism too high, burning through fructose reserves.",
        "Wow_Approach": "Skipping the 4°C equilibration period is the most common technician error leading to total post-thaw mortality in an otherwise healthy ejaculate."
    },
    1403: {
        "topic": "Oxidative Stress - Loss of Sperm Motility",
        "Core_Anatomy": "Sperm midpiece (mitochondria) and axoneme.",
        "Pathogenesis_Immediate": "The first, most immediate, and most powerful clinical impact of oxidative stress (ROS) on spermatozoa is the profound Loss of Motility.",
        "Pathogenesis_Deep": "Sperm motility is driven by ATP generated in the mitochondria located in the midpiece. Reactive Oxygen Species (ROS) rapidly initiate lipid peroxidation of the highly unsaturated mitochondrial membranes. This destroys the electron transport chain, immediately halting ATP production. Without ATP, the axoneme (the 9+2 microtubule structure of the tail) cannot beat. Thus, motility ceases long before the acrosome is damaged or the DNA fragments.",
        "Why_Not": "Exocytosis (acrosome reaction) requires calcium influx, not ROS. DNA fragmentation occurs later in the oxidative cascade. The absolute first visible sign is the sperm stopping.",
        "Wow_Approach": "When evaluating chilled semen that has been shipped overnight, a sudden drop from 70% motility down to 10% indicates severe oxidative stress or cold shock during transit."
    },
    1404: {
        "topic": "Puerperal Involution - Cervix vs Uterus",
        "Core_Anatomy": "Maternal cervix and uterine myometrium.",
        "Pathogenesis_Immediate": "The statement 'Involution of the cervix is slower than that of the uterus' is TRUE in the cow.",
        "Pathogenesis_Deep": "Following parturition, the massive bovine uterus shrinks rapidly (macroscopic involution is complete by day 25-30) due to intense myometrial contractions and lochial discharge. However, the cervix—which is composed primarily of dense, avascular collagenous connective tissue—remodels much more slowly. The cervical os closes quickly (within 2-3 days) to prevent infection, but the physical mass of the cervix remains enlarged and palpable for up to 45-60 days.",
        "Why_Not": "Assuming the cervix involutes faster would lead a clinician to falsely diagnose a normal, mildly enlarged post-partum cervix as 'cervicitis'.",
        "Wow_Approach": "On a 30-day post-partum rectal palpation in a dairy cow, finding a uterus that has returned to the pelvic brim but a cervix that feels 'thicker than normal' is physiological, not pathological."
    },
    1411: {
        "topic": "Cold Shock - Rapid Temperature Drop (Repeated MCQ)",
        "Core_Anatomy": "Sperm plasma membrane lipid bilayer.",
        "Pathogenesis_Immediate": "The statement 'The stress response shown by spermatozoa as a reaction to a rapid drop in temperature is known as Cold shock' is TRUE.",
        "Pathogenesis_Deep": "Cold shock occurs when semen is cooled too rapidly (e.g., dropping from 37°C to 4°C in less than 30 minutes). The rapid chilling causes the membrane phospholipids to undergo a violent phase transition from fluid to rigid-gel state. This forces membrane proteins out of alignment, creating massive pores. The sperm loses its selective permeability, leaks ATP and enzymes, and dies instantly with a characteristic 'coiled tail' or bent midpiece.",
        "Why_Not": "Cold shock is specifically the damage caused by RAPID chilling above freezing. Frost damage or ice-crystal formation happens below 0°C.",
        "Wow_Approach": "To prevent cold shock, semen extenders always include lipoproteins (like Egg Yolk or Milk Casein), which coat the outside of the sperm membrane and buffer the lipid phase transition during cooling."
    },
    1412: {
        "topic": "Sustentacular Cells - Andrology Matching",
        "Core_Anatomy": "Seminiferous tubules and blood-testis barrier.",
        "Pathogenesis_Immediate": "Sustentacular cells (Sertoli cells) match to 'Nursing cells' or 'Inhibin production'.",
        "Pathogenesis_Deep": "Sertoli cells are the somatic pillars of the seminiferous tubule. They secrete Inhibin (which negatively feeds back on the pituitary to suppress FSH), secrete Androgen-Binding Protein (ABP), and phagocytize the residual bodies cast off by elongating spermatids. They are the ultimate 'nurses' of the male reproductive tract.",
        "Why_Not": "Leydig cells secrete testosterone (stimulated by LH), not inhibin. The fistulous tract is a pathology, unrelated to normal histology.",
        "Wow_Approach": "Sertoli cell tumors in dogs secrete massive amounts of estrogen (and inhibin), leading to a feminizing syndrome (gynecomastia, pendulous prepuce, and bilateral alopecia) and severe bone marrow suppression."
    },
    1413: {
        "topic": "Caslick Operation - Pneumovagina Treatment",
        "Core_Anatomy": "Equine vulva, vestibulo-vaginal sphincter, and perineum.",
        "Pathogenesis_Immediate": "The Caslick operation (vulvoplasty) matches to the treatment of Pneumovagina ('windsucking') in the Mare.",
        "Pathogenesis_Deep": "Older, multiparous mares often suffer from perineal conformational changes where the anus sinks cranially, pulling the dorsal commissure of the vulva into a horizontal plane. This breaks the vestibular seal. When the mare trots, air (pneumovagina) and feces (urovagina) are sucked directly into the reproductive tract, causing severe, chronic endometritis and absolute infertility. The Caslick operation involves removing a thin strip of mucosa from the dorsal lips of the vulva and suturing them together to surgically restore the seal.",
        "Why_Not": "It is not used in cows or sows because their vulvar anatomy and tail placement naturally prevent windsucking.",
        "Wow_Approach": "You MUST open (episiotomy) a Caslick suture line 2 weeks before the mare foals. If you forget, the foal's head will violently tear the vulva and perineum during delivery, creating a catastrophic 3rd-degree perineal laceration."
    },
    1420: {
        "topic": "Fetal Anasarca - Bloated Bull Frog Appearance",
        "Core_Anatomy": "Fetal subcutaneous tissues and lymphatic system.",
        "Pathogenesis_Immediate": "A severe congenital anomaly characterized by massive generalized edema, giving the fetus a 'Bloated Bull Frog' appearance, is known as Fetal Anasarca (Water Calf).",
        "Pathogenesis_Deep": "Fetal anasarca is an autosomal recessive genetic defect (common in Bulldog calves of Dexter cattle and some canine breeds like Bulldogs). The fetal lymphatic system fails to develop properly, leading to the massive accumulation of transudate in the subcutaneous tissues. The fetus becomes a giant, bloated, water-filled sphere. This massive fetopelvic disproportion always results in severe dystocia.",
        "Why_Not": "Hydroallantois is fluid in the placental sac, not inside the fetus. Fetal emphysema is gas accumulation post-mortem due to putrefaction, not genetic fluid edema.",
        "Wow_Approach": "Because the 'water calf' is essentially a giant fluid balloon, forced traction will often rupture the fetal skin, causing a massive explosion of fluid into the operator's face. Delivery often requires multiple deep incisions into the fetal skin to drain the edema before traction."
    },
    1423: {
        "topic": "VGO Short Notes - Pathology Synthesis",
        "Core_Anatomy": "Integrated reproductive systems.",
        "Pathogenesis_Immediate": "The 'Short Notes' section evaluates the ability to synthesize the etiology, clinical signs, and treatment of complex syndromes like fetal anasarca, cold shock, or pneumovagina.",
        "Pathogenesis_Deep": "To excel: always define the core defect (e.g., lymphatic failure in anasarca), the clinical consequence (dystocia), and the veterinary intervention (episiotomy for Caslick, or fetotomy/drainage for anasarca).",
        "Why_Not": "Providing only a definition without the clinical intervention loses marks in VGO-II, which is an applied clinical subject.",
        "Wow_Approach": "Use diagrams where applicable (e.g., drawing the suture line for a Caslick operation) to secure maximum points."
    },
    1437: {
        "topic": "VGO-II Core Objectives - Obstetrics and Dystocia",
        "Core_Anatomy": "Feto-maternal pelvic axis.",
        "Pathogenesis_Immediate": "VGO-II is primarily dedicated to Veterinary Obstetrics—the management of pregnancy, parturition, and the puerperium.",
        "Pathogenesis_Deep": "This module transitions students from the physiology of getting an animal pregnant (VGO-I) to the mechanics of delivering the fetus. It focuses heavily on applied biomechanics: predicting dystocia via pelvimetry, resolving it via mutation (correcting posture/presentation), and managing postpartum crises like uterine prolapse or retained placenta.",
        "Why_Not": "Andrology focuses on the male; VGO-II focuses intensely on the female birth canal and neonatal survival.",
        "Wow_Approach": "The ultimate rule of VGO-II: Never pull on a calf until you have positively identified the presentation, position, and posture, and fully corrected any deviations."
    },
    1438: {
        "topic": "VGO-II Advanced Interventions - Surgery",
        "Core_Anatomy": "Maternal abdomen and birth canal.",
        "Pathogenesis_Immediate": "Beyond manual extraction, VGO-II mandates proficiency in obstetrical surgeries, specifically the Caesarean Section and Fetotomy.",
        "Pathogenesis_Deep": "When manual mutation fails (due to a bloated water calf, a narrow 120 cm² pelvis, or a true breech), the clinician must pivot immediately to surgery. Fetotomy is used strictly for dead fetuses to save the dam. C-section is used for live fetuses (or recently dead fetuses where the uterus is still healthy) via the left paralumbar fossa in cattle.",
        "Why_Not": "Delaying the decision to cut (C-section) while fruitlessly pulling on a stuck calf for hours guarantees the death of the calf and severe nerve paralysis (obturator nerve) for the cow.",
        "Wow_Approach": "The decision to perform a C-section should ideally be made within 15 minutes of assessing a dystocia that cannot be manually corrected."
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
