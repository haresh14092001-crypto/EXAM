import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

# Find next empty HY IDs after 384
empty = [x for x in data if x.get('is_high_yield') and not x.get('Core_Anatomy')]
print(f"Empty remaining: {len(empty)}")
next_ids = [x['id'] for x in empty[:15]]
print("Next IDs:", next_ids)

enrichment = {
    385: {
        "topic": "Ovarian Consistency During Anestrus - Hard vs Firm vs Flaccid",
        "Core_Anatomy": "The ovarian cortex stroma (fibrous connective tissue) and the absence of follicular/luteal structures.",
        "Pathogenesis_Immediate": "During anestrus, bovine ovaries are described as smooth and flaccid — the flaccid (soft, compressible) texture reflects the absence of any turgid follicles or firm corpus luteum structures.",
        "Pathogenesis_Deep": "Ovarian texture correlation with hormonal status: Firm/hard = active corpus luteum (days 5-16 of estrous cycle) — progesterone-secreting luteal tissue is dense and firm. Soft/Flaccid = anestrus or early post-partum — no follicular or luteal structures. Turgid/Cystic = follicular cyst (fluid under high pressure, >2.5 cm, walls thin). Rubbery/Firm = luteal cyst (thick-walled, progesterone-secreting). Knowing these textures by rectal palpation is the cornerstone of bovine reproductive examination.",
        "Why_Not": "Hard ovaries are normal in the mid-luteal phase (Days 8-14 post-ovulation). Flaccid ovaries during this period indicate luteal insufficiency or failure of ovulation. Distinguish true anestrus (flaccid, smooth, small ovaries on TWO examinations 14 days apart) from the inter-wave anovulatory period (transient smoothness between follicular waves).",
        "Wow_Approach": "Develop a systematic rectal palpation approach for ovaries: (1) Locate the cervix (hard, cartilaginous). (2) Move cranially along the uterine horn (dorsal, medial). (3) At the tip of the horn, sweep laterally to find the ovary (attached to broad ligament). (4) Gently roll the ovary between thumb and forefinger. (5) Describe: size, shape, surface texture, and any palpable structures."
    },
    386: {
        "topic": "Second Stage of Labour - Species Comparison and Duration",
        "Core_Anatomy": "The birth canal (cervix, vagina, vulva), the fetal presenting part (head/forelimbs or hindlimbs), and the myometrial contraction forces.",
        "Pathogenesis_Immediate": "The shortest duration of Stage 2 labour (from cervical dilation to fetal expulsion) is observed in the Mare (Equine). Stage 2 in mares lasts only 20-30 minutes — the fastest of all domestic species due to the intense myometrial contractions of the horse.",
        "Pathogenesis_Deep": "Stage 2 labour durations by species: Mare = 20-30 minutes (fastest — intense contractions, large fetus, rapid delivery essential for placental separation preventing fetal hypoxia). Cow = 30 minutes to 2 hours. Ewe = 30 minutes to 1 hour. Bitch = up to 2-4 hours total for entire litter (individual pup delivery 15-60 minutes apart). The mare's placenta separates rapidly after delivery — any delay >30 minutes in Stage 2 indicates an emergency requiring immediate obstetrical assistance.",
        "Why_Not": "Dystocia threshold: Intervention is indicated if Stage 2 exceeds 30 minutes in mares, 4 hours in cows (if no progress), 2 hours between puppies in bitches. The mare's short Stage 2 window means that any delay is immediately life-threatening to the foal — hypoxia begins within 10-15 minutes of umbilical compression.",
        "Wow_Approach": "The mare's foal is most vulnerable to hypoxia because the diffuse epitheliochorial placenta separates from the entire uterine surface simultaneously at parturition, unlike the cotyledonary cattle placenta which separates sequentially. Once the allantochorion ruptures, the foal must be born within 30 minutes or faces severe hypoxic encephalopathy."
    },
    387: {
        "topic": "PSP Dye Test for Oviductal Patency in Cattle",
        "Core_Anatomy": "The oviduct (infundibulum, ampulla, isthmus), the uterus, and the vagina.",
        "Pathogenesis_Immediate": "The PSP (Phenolsulfonphthalein) Dye Test is used to detect blockage (occlusion) of the fallopian tubes (oviducts) in cattle. The dye is injected into the uterus; passage into the peritoneal cavity (visible on laparoscopy or via peritoneal lavage) confirms oviductal patency.",
        "Pathogenesis_Deep": "Technique: Inject 5 ml of 0.5% PSP dye solution through the cervix into the uterine horns using an AI gun. If oviducts are patent, the dye passes through the infundibulum into the peritoneal cavity. Peritoneal lavage samples collected by paracentesis, or direct laparoscopic visualization of dye at the fimbriae, confirm patency. Absence of dye in the peritoneum indicates unilateral or bilateral oviductal occlusion (hydrosalpinx, adhesions, or salpingitis).",
        "Why_Not": "Cuboni Test detects estrogens in mare urine as a pregnancy test (not oviductal patency). White Side Test is a milk test for subclinical mastitis (SCC elevation). Spinnbarkeit test measures the elasticity of cervical mucus during estrus in cattle (degree of ferning and thread formation).",
        "Wow_Approach": "Oviductal occlusion in cattle is most commonly caused by ascending *Tritrichomonas foetus* or *Ureaplasma* infections causing salpingitis, or adhesions from prior peritonitis. Affected cows repeatedly conceive but lose early embryos at the point of oviductal transit. Diagnosis by PSP test guides the decision for unilateral vs bilateral salpingectomy or culling."
    },
    388: {
        "topic": "Allantoic Cavity - Storage of Fetal Urinary Waste Products",
        "Core_Anatomy": "The allantois (endodermal outgrowth from the cloaca), the allantoic cavity, the urachus, and the amniotic cavity.",
        "Pathogenesis_Immediate": "The waste products of fetal kidney (fetal urine) are stored in the Allantoic cavity (not amniotic). The allantois collects fetal urine throughout gestation via the urachus, and this fluid forms the allantoic fluid (largest volume fluid surrounding the fetus in cattle).",
        "Pathogenesis_Deep": "Fetal membrane compartments: Amniotic cavity — directly surrounds the fetus; contains amniotic fluid (from fetal skin transudation, lung fluid, and fetal swallowing); clear, viscous. Allantoic cavity — between chorioallantois and amnion; contains allantoic fluid (primarily fetal urine); larger volume; straw-coloured, watery. In cattle, allantois can hold 8-10 litres of fluid. The urachus is the tubular connection between the fetal bladder and the allantoic cavity.",
        "Why_Not": "Amniotic fluid is NOT the primary repository for fetal urine — it contains primarily fetal skin transudation, lung fluid, and some oral secretions. The fetus swallows amniotic fluid as part of normal deglutition practice. If the fetus cannot swallow (due to oesophageal atresia or neural defects), polyhydramnios (excessive amniotic fluid) results.",
        "Wow_Approach": "Diagnosis of fetal membrane rupture type: Clear/viscous fluid first = amnion rupture (water bag breaking). Straw-coloured/watery fluid after = allantochorion rupture (true water breaking). In cattle, the first fluid expelled is allantoic (as the allantochorion ruptures at Stage 1-2 transition), followed by amniotic fluid just before delivery. In horses, the reverse occurs."
    },
    389: {
        "topic": "VGO Matching Pairs - Heifers, Mares, and Reproductive Terms",
        "Core_Anatomy": "Bovine and equine comparative reproductive anatomy and clinical presentations.",
        "Pathogenesis_Immediate": "Key VGO matching pairs: Heifer — Ventral bulging (of the abdomen in late pregnancy due to pendulous uterus resting on the abdominal floor, more pronounced than cows due to weak abdominal musculature). Mare — Epitheliochorial placentation. Freemartin — XX/XY chimerism. Retention of Placenta (RFM) — Collagenase deficiency at placentomal crypts.",
        "Pathogenesis_Deep": "Heifer ventral bulging in late pregnancy: The heifer's abdominal musculature is less developed than a mature cow's. The growing gravid uterus in a heifer causes dramatic ventral abdominal distension visible from the side, creating a classic pendulous abdomen appearance by the 7th month of gestation. This predisposes heifers to uterine torsion (the uterus swings more freely).",
        "Why_Not": "Left-sided abdominal distension in the paralumbar fossa (not ventral) indicates ruminal bloat or LDA. Bilateral distension indicates vagal indigestion. Ventral pendulous abdomen specifically in a heifer at late gestation is physiological and related to the musculoskeletal immaturity of the first-calf heifer.",
        "Wow_Approach": "Heifer calving management: Initiate 24-hour supervised calving monitoring from Day 275 onwards. Heifers have a 5-7x higher dystocia rate than mature cows due to: (1) pelvic immaturity (insufficient pelvic area), (2) lack of obstetric experience, and (3) higher incidence of fetal oversize relative to pelvic dimensions. Pelvimetry (Rice pelvimeter measurement >150 cm² area) predicts calving success."
    },
    390: {
        "topic": "VGO Matching - Reproductive Terminology and Management",
        "Core_Anatomy": "Comparative uterine and fetal membrane anatomy across species.",
        "Pathogenesis_Immediate": "Key reproductive term matching: Dystocia = difficult birth requiring obstetrical assistance. Eutocia = normal, unassisted parturition. Monotocous = species bearing single young (cattle, horses, sheep). Polytocous = species bearing multiple young (pigs, dogs, cats, rabbits). Primipara = a female giving birth for the first time. Multipara = a female having given birth two or more times.",
        "Pathogenesis_Deep": "Placentation types across species: Cattle/Sheep/Goat = Synepitheliochorial (modified epitheliochorial — cotyledonary, semi-invasive). Horse = Epitheliochorial (diffuse microcotyledonary, non-invasive). Dog/Cat = Endotheliochorial (zonary, moderately invasive). Human/Rodents = Haemochorial (most invasive, direct maternal blood contact). Invasiveness correlates inversely with neonatal immunoglobulin transfer — the more invasive the placenta, the more IgG transferred in utero (haemochorial). Less invasive species (cattle, horses) rely entirely on colostral IgG transfer.",
        "Why_Not": "Cattle neonates (calves) are born with essentially no circulating immunoglobulins (agammaglobulinaemic at birth) because the synepitheliochorial placenta prevents maternal IgG transfer. This makes Failure of Passive Transfer (FPT) from delayed or inadequate colostrum consumption a life-threatening emergency in the calf — a critical bovine production medicine concept.",
        "Wow_Approach": "Passive transfer of immunity: Calves must receive 4 litres of high-quality colostrum (IgG >50 g/L) within the first 6 hours of birth (gut closure begins at 12 hours, complete by 24 hours). Test colostrum quality with a Brix refractometer: >22% Brix = adequate quality. Test calf serum IgG at 24-48 hours: >10 g/L = adequate passive transfer."
    },
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
