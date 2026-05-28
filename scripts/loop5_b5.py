import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

# Fill remaining of the list from next50.txt that weren't yet enriched
enrichment = {
    525: {
        "topic": "VGO-I Overview - Gynaecology Paper Structure",
        "Core_Anatomy": "Female reproductive tract: ovaries, oviducts, uterus, cervix, vagina, vulva across bovine, equine, ovine, caprine, porcine, and canine species.",
        "Pathogenesis_Immediate": "VGO-I (Veterinary Gynaecology — VGO 411) covers: reproductive anatomy, oestrous cycle physiology, puberty, mating, fertilization, early embryonic development, maternal recognition of pregnancy, and gynaecological diseases (ovarian cysts, endometritis, pyometra, uterine torsion).",
        "Pathogenesis_Deep": "High-yield VGO-I topics by examination frequency: (1) Follicular cysts vs Luteal cysts — distinguishing signs (nymphomania vs anestrus), hormones, treatment. (2) Freemartinism mechanism and diagnosis. (3) IFN-tau and MRP in ruminants. (4) Embryo transfer recipient synchronization. (5) Oestrus detection methods and efficiency. (6) Placentation types across species.",
        "Why_Not": "VGO-II (Obstetrics — VGO 421) covers parturition, dystocia, obstetrical techniques, and post-partum complications. Understanding which subject covers which topic prevents confusion during paper analysis. Both papers appear in the TANUVAS final BVSc examination as separate papers with equal marks allocation.",
        "Wow_Approach": "VGO-I examination strategy: The MCQ section tests specific values (gestation lengths, oestrous cycle parameters, caruncle counts, progesterone thresholds). The short-answer section tests mechanisms (IFN-tau, cortical granule block to polyspermy, luteolysis cascade). The essay section tests clinical problem-solving (repeat breeding investigation protocol, pyometra management in the bitch, PCOS treatment in mares)."
    },
    526: {
        "topic": "VGO-I Paper — Key Examination Areas",
        "Core_Anatomy": "Comparative reproductive physiology, ovarian dynamics, and uterine biology across domestic animal species.",
        "Pathogenesis_Immediate": "Key areas tested in VGO 411 papers include: Fill-in-the-blank (reproductive physiology values), MCQ (breed/species associations, drug actions), True/False (species-specific physiology), Matching (hormones, conditions, procedures), Short answers (mechanisms, definitions), and Essays (clinical management protocols).",
        "Pathogenesis_Deep": "Core topics appearing in 3+ consecutive year question papers: (1) Follicular wave dynamics in cattle. (2) Oestrus detection methods (efficiency, false positive rate). (3) Pyometra classification (open vs closed cervix), diagnosis, and management. (4) Embryo transfer procedure in cattle. (5) Uterine torsion — Schaffer's method, laparotomy. (6) Freemartinism — mechanism, diagnosis, economic importance.",
        "Why_Not": "Less frequently tested VGO-I areas (appear once in 3-5 years): Sperm capacitation biochemistry, zona pellucida composition (ZP1/ZP2/ZP3), embryo cryopreservation protocols, in-vitro fertilization media composition. Focus the majority of preparation time on the high-frequency core topics.",
        "Wow_Approach": "Previous year pattern analysis for TANUVAS VGO 411: True/False section consistently tests 'induced vs spontaneous ovulators'. MCQ section always includes at least one question on the Intercornual Ligament species and one on oestrous cycle duration values. Be prepared to differentiate anoestrus from silent heat and cystic ovary from luteal cyst in every examination."
    },
    400: {
        "topic": "VGO Short Definitions - Superfecundation, Superfetation, Dystocia",
        "Core_Anatomy": "The uterus, placenta, and ovarian cycle; reproductive anatomy of polytocous species.",
        "Pathogenesis_Immediate": "Short definitions for VGO 411 short-answer section: Superfecundation = fertilization of two ova from the same oestrus by different males. Superfetation = fertilization of an ovum during an established pregnancy. Dystocia = difficult parturition requiring obstetrical assistance. Eutocia = normal unassisted parturition.",
        "Pathogenesis_Deep": "Additional critical definitions: Nymphomania = continuous, uninterrupted signs of oestrus in cattle (caused by follicular cysts). Anaphrodisia/Anoestrus = complete absence of oestrus cycles. Repeat breeding = failure to conceive after 3+ inseminations in a structurally normal cow. Sub-oestrus = oestrus with reduced or absent behavioural signs (common in buffaloes during summer). Phymosis = inability to retract the penis. Infertility = reduced reproductive efficiency (reversible). Sterility = complete permanent inability to reproduce.",
        "Why_Not": "These definition questions appear in 1-mark (fill-in) and 2-mark (define) formats. The key for 1-mark answers is precision: 'Superfecundation = fertilization of two eggs from the same heat by different sires' is the complete 1-mark answer. For 2-mark answers, add the species most commonly affected and the clinical significance.",
        "Wow_Approach": "Memory shortcut for Super- terms: Super-FECUNDATION = two SIRES, same heat (Fe = fertilization twice by different sires). Super-FETATION = pregnancy during pregnancy (Fe-FETUS already present). This Latin root distinction prevents confusion between these two rarely occurring but frequently examined reproductive phenomena."
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
