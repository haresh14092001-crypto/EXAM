import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1441: {
        "topic": "VGO Objective Section Header - Fill in the Blanks",
        "Core_Anatomy": "Veterinary clinical pathology.",
        "Pathogenesis_Immediate": "Fill-in-the-blanks evaluate exact clinical constants (e.g., gestation days, hours to cervical closure, exact drug dosages).",
        "Pathogenesis_Deep": "This format demands high recall accuracy without the benefit of elimination via MCQ distractors.",
        "Why_Not": "Guessing is heavily penalized as there are no provided options.",
        "Wow_Approach": "Always double check the unit required (e.g., days vs months, mg vs ml) before finalizing the answer."
    },
    1456: {
        "topic": "Hydroallantois - Rapid Abdominal Enlargement",
        "Core_Anatomy": "Allantoic sac and maternal abdomen.",
        "Pathogenesis_Immediate": "In dropsy of the fetal membranes, a massive and rapid abdominal enlargement developing within just 5 to 20 days in late gestation is pathognomonic for Hydroallantois.",
        "Pathogenesis_Deep": "Hydroallantois is a placental dysfunction characterized by a drastic reduction in the number of functional caruncles, with the remaining caruncles becoming adventitious and highly permeable. This causes a sudden, rapid transudation of fluid (up to 200 liters) into the allantoic sac over a period of 1-3 weeks. The cow rapidly becomes barrel-shaped, dyspneic, and recumbent due to the massive weight.",
        "Why_Not": "Hydroamnios develops very slowly over several months and is rarely life-threatening to the dam prior to parturition.",
        "Wow_Approach": "Because it develops so rapidly, the maternal abdominal muscles often cannot stretch fast enough and may rupture, causing a catastrophic ventral hernia."
    },
    1457: {
        "topic": "Dropsical Conditions - Hydroallantois vs Hydroamnios",
        "Core_Anatomy": "Placental membranes (allantois and amnion).",
        "Pathogenesis_Immediate": "Hydroallantois (rapid, placental origin) vs Hydroamnios (slow, fetal origin).",
        "Pathogenesis_Deep": "On rectal palpation, Hydroallantois feels like a highly tense, fluid-filled balloon; you cannot palpate the fetus or the placentomes because the uterus is stretched completely tight. In contrast, in Hydroamnios, the uterus is flaccid and doughy, and you can easily palpate the fetus and placentomes through the fluid.",
        "Why_Not": "Hydrocephalus is fluid inside the fetal brain cavity, not the placental membranes.",
        "Wow_Approach": "Hydroallantois accounts for 85-90% of all dropsical conditions in cattle, making it the primary differential for any sudden late-gestation bloat."
    },
    1458: {
        "topic": "Gestation Length - Porcine (Sow) (Repeated MCQ)",
        "Core_Anatomy": "Porcine uterus and fetal HPA axis.",
        "Pathogenesis_Immediate": "The normal gestation length of swine is approximately 111-114 days.",
        "Pathogenesis_Deep": "Often memorized as '3 months, 3 weeks, 3 days' (114 days). Sows rely entirely on the primary corpora lutea for progesterone maintenance throughout the entire gestation. If all CLs are lysed (e.g., via PGF2-alpha administration) at any point, the sow will abort within 24-36 hours.",
        "Why_Not": "222 days is non-physiological. 333 days is the gestation of a mare.",
        "Wow_Approach": "Because sows have litters, parturition is triggered by a collective signal. A minimum of 2-4 viable fetuses is required to maintain pregnancy; if the litter drops below this threshold early on, the pregnancy will fail."
    },
    1459: {
        "topic": "Endometrial Cups - Unique Equine Placenta (Repeated MCQ)",
        "Core_Anatomy": "Maternal endometrium and fetal chorionic girdle.",
        "Pathogenesis_Immediate": "Endometrial cups are unique, transient placental structures present exclusively in the Mare.",
        "Pathogenesis_Deep": "Forming around day 35, they secrete eCG (PMSG) which luteinizes secondary follicles in the mare's ovary to maintain progesterone levels. They naturally regress via maternal immune rejection by day 120-150.",
        "Why_Not": "Cows rely on the primary CL and later placental progesterone (via binucleate giant cells), lacking endometrial cups entirely.",
        "Wow_Approach": "The presence of endometrial cups makes it impossible to 'short cycle' a mare with prostaglandins if she has lost a pregnancy between days 35-120."
    },
    1460: {
        "topic": "Equine Parturition - Patchy Sweating (Foaling Sign)",
        "Core_Anatomy": "Maternal sweat glands and sympathetic nervous system.",
        "Pathogenesis_Immediate": "Patchy sweating, particularly behind the elbows and on the flanks, is a classic, imminent sign of Stage 1 labor seen in the Mare.",
        "Pathogenesis_Deep": "As the mare enters Stage 1 labor (cervical dilation and fetal repositioning), she experiences intense, colicky visceral pain from the initial myometrial contractions. This pain triggers a massive sympathetic response (epinephrine release), causing characteristic patchy sweating, restlessness, pacing, and frequent posturing to urinate. This stage lasts 1-4 hours and ends precisely when the chorioallantoic membrane ruptures ('water breaks').",
        "Why_Not": "Cows exhibit restlessness but rarely sweat profusely. Sows build nests. Only the mare exhibits this distinct, intense patchy sweating prior to foaling.",
        "Wow_Approach": "If you see a mare sweating behind the elbows, prepare immediately. Once her 'water breaks', Stage 2 labor in the mare is explosive and should be completed within 20-30 minutes; any delay beyond 30 minutes is a critical emergency."
    },
    1461: {
        "topic": "PGF2-alpha Synthesis - Endometrial Origin",
        "Core_Anatomy": "Maternal endometrium and arachidonic acid cascade.",
        "Pathogenesis_Immediate": "During the initiation of parturition, PGF2-alpha is synthesized massively in the Endometrium.",
        "Pathogenesis_Deep": "The maternal endometrium is the primary site of PGF2-alpha production in domestic animals. At term, the surge of fetal cortisol drives placental estrogen production. This high estrogen upregulates oxytocin receptors on the endometrium. When oxytocin binds to these receptors, it stimulates the endometrial cells to rapidly synthesize and release PGF2-alpha. This prostaglandin then diffuses locally (or via counter-current exchange) to lyse the corpus luteum and stimulate powerful myometrial contractions.",
        "Why_Not": "The myometrium contracts in response to PGF2-alpha, but does not synthesize the bulk of it. The perimetrium is just the outer serosal layer.",
        "Wow_Approach": "In cattle, this is why a severe endometrial infection (endometritis) can cause premature PGF2-alpha release, leading to early embryonic death or abortion by lysing the CL."
    },
    1462: {
        "topic": "Chronic Metritis - Endometrial Destruction",
        "Core_Anatomy": "Uterine endometrium, myometrium, and fibroblasts.",
        "Pathogenesis_Immediate": "A severe, chronic metritis can result in the complete destruction of the functional endometrium and widespread fibrotic (scar tissue) changes.",
        "Pathogenesis_Deep": "When an acute bacterial infection (often post-partum) invades deeply past the mucosal layer into the myometrium, it is termed 'metritis'. If it becomes chronic, the highly specialized glandular epithelium of the endometrium is destroyed by chronic suppurative inflammation. Fibroblasts invade the area, replacing the functional glands with dense, non-functional scar tissue (fibrosis). Without endometrial glands, the uterus can no longer secrete histotroph (uterine milk) to nourish an embryo, rendering the animal permanently sterile.",
        "Why_Not": "Simple endometritis only involves the superficial mucosa and usually heals without scarring. True chronic metritis with fibrosis is an irreversible end-stage disease.",
        "Wow_Approach": "This severe fibrotic change is often palpated rectally as a thick, heavy, 'leathery' or 'meaty' uterus that lacks normal tone."
    },
    1463: {
        "topic": "Transverse Ventral Presentation - Equine Dystocia (Repeated MCQ)",
        "Core_Anatomy": "Equine uterus, maternal pelvic inlet, and fetal long axis.",
        "Pathogenesis_Immediate": "The transverse ventral presentation (the 'dog-sitting' or sideways presentation where all four feet are directed towards the birth canal) is most common in the Mare.",
        "Pathogenesis_Deep": "Because the equine fetus has exceptionally long limbs and the uterine body is spherical, the fetus can become trapped transversely. In a transverse ventral presentation, the foal's belly and all four limbs face the pelvic inlet, while the head and back are jammed against the uterine wall. This is a catastrophic presentation requiring immediate heavy epidural anesthesia and surgical/manual version.",
        "Why_Not": "Ruminants have long, narrow uterine horns that naturally force the fetus into a longitudinal (anterior or posterior) alignment, making transverse presentations extremely rare.",
        "Wow_Approach": "Never try to pull all four legs! You must repel the hindquarters and perform a version to convert it into a normal anterior longitudinal presentation before traction."
    },
    1464: {
        "topic": "Cervical Closure - Post-Partum Involution Timing",
        "Core_Anatomy": "Maternal cervix, cervical rings, and collagenous stroma.",
        "Pathogenesis_Immediate": "In cows, following normal calving, the cervix rapidly constricts, making it almost impossible to insert a hand completely through the cervix within 24 to 48 hours (often significantly tightening within 10-12 hours).",
        "Pathogenesis_Deep": "The bovine cervix is composed of dense collagenous tissue arranged in distinct annular rings. During parturition, relaxin and estrogen cause massive collagen depolymerization, allowing the cervix to dilate widely (Stage 1 labor). Immediately after the calf passes, the removal of physical pressure and a drop in estrogen causes the collagen to rapidly re-crosslink. Within 10-12 hours, the cervix has tightened significantly, and by 24-48 hours, it is usually closed so tightly that a human hand cannot pass, sealing the uterus from ascending environmental bacteria.",
        "Why_Not": "If the cervix remains open enough to pass a hand for 3-4 days, it is a clinical sign of uterine atony, hypocalcemia, or retained fetal membranes blocking the canal.",
        "Wow_Approach": "This rapid closure is why a retained placenta must be addressed carefully; if the membranes are trapped when the cervix closes, the cow will develop a severe necrotic metritis."
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
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
