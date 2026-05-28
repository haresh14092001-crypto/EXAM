import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    477: {
        "topic": "Estrogen Role in Oviductal Sperm Transport",
        "Core_Anatomy": "The oviductal isthmic sperm reservoir, the cilia of the oviductal epithelium, and the smooth muscle of the oviductal wall.",
        "Pathogenesis_Immediate": "Estrogen (not progesterone, PGF2alpha, or inhibin) is the primary hormone regulating sperm transport through the oviduct at the time of oestrus, enhancing ciliary beat frequency and smooth muscle peristalsis to facilitate rapid sperm movement from the uterus to the fertilization site.",
        "Pathogenesis_Deep": "At oestrus, peak estradiol-17β stimulates: (1) Increased ciliary beat frequency toward the infundibulum (opposing direction to embryo transport). (2) Increased oviductal smooth muscle contractility — rhythmic contractions mix and propel luminal contents. (3) Upregulation of estrogen receptors on oviductal epithelial cells, amplifying estrogenic responsiveness. (4) Modulation of the sperm reservoir at the isthmus — releasing capacitated sperm in a controlled manner toward the ampulla at the time of ovulation.",
        "Why_Not": "Progesterone (dominant in the luteal phase, Days 5-17) REDUCES oviductal motility and increases the sperm reservoir retention time — slowing transport. This is the physiological basis for progesterone-based sperm selection in the isthmus (only the best-quality capacitated sperm are released). Inhibin is a gonadal hormone that feeds back to suppress FSH — unrelated to oviductal transport.",
        "Wow_Approach": "The oviductal sperm reservoir at the isthmic-ampullary junction stores 10,000-100,000 sperm for up to 24-30 hours post-mating. Sperm are bound to oviductal epithelial cells via carbohydrate-lectin interactions, maintaining viability and preventing premature capacitation. This reservoir explains why AI timing can succeed even when insemination precedes ovulation by 12-18 hours."
    },
    480: {
        "topic": "Sheep as a Short-Day Breeder - Photoperiod and Melatonin",
        "Core_Anatomy": "The pineal gland (melatonin production), the hypothalamic kisspeptin neurons, and the pars tuberalis of the pituitary.",
        "Pathogenesis_Immediate": "Sheep are short-day breeders — they become sexually active as daylength decreases (autumn/winter in the Northern Hemisphere, corresponding to increasing duration of nocturnal melatonin secretion).",
        "Pathogenesis_Deep": "As nights lengthen in autumn, the duration of melatonin secretion from the pineal gland increases (melatonin is secreted only in darkness). Extended melatonin signal activates kisspeptin neurons in the hypothalamus, which stimulate GnRH pulse frequency. Increased GnRH → increased LH pulsatility → follicular development and oestrus initiation. The first oestrus of the season is typically preceded by a 'silent ovulation' (ovulation without behavioural signs).",
        "Why_Not": "Horses are long-day breeders (breeding season = spring/summer, when days lengthen). Cattle are essentially non-seasonal (year-round breeders). Only sheep, goats, deer, and some other species are strict short-day breeders. Melatonin implants (Regulin® implants containing 18 mg melatonin) can be used to advance the breeding season in sheep by 6-8 weeks by artificially simulating long-night photoperiod.",
        "Wow_Approach": "RAM effect: Introduction of a ram (male) to anovulatory ewes in late anoestrus advances the onset of the breeding season by triggering a surge of LH within 2 hours of ram introduction (the Whitten Effect in sheep). This pheromone-mediated neuroendocrine response causes the first 'silent ovulation' of the season, followed by fertile oestrus in the next cycle (17 days later)."
    },
    485: {
        "topic": "VGO Matching - Reproductive Hormones and Physiological Effects",
        "Core_Anatomy": "The hypothalamus (GnRH, kisspeptin), anterior pituitary (FSH, LH), ovary (estradiol, progesterone, inhibin), uterus (PGF2alpha, oxytocin receptors), and fetal trophoblast (IFN-tau).",
        "Pathogenesis_Immediate": "Key VGO matching pairs: IFN-tau → maternal recognition of pregnancy (ruminants). Melatonin → seasonal breeding regulation (short-day and long-day breeders). PGF2alpha → luteolysis. Inhibin → negative feedback on FSH. Whitten effect → male pheromone-induced oestrus advancement in rodents and ewes.",
        "Pathogenesis_Deep": "Hormone-effect matching summary: IFN-tau (bovine/ovine trophoblast) → inhibits endometrial OTR expression → prevents PGF2alpha luteolytic cascade → CL preserved. Melatonin (pineal gland) → modulates GnRH pulse frequency → controls seasonality. Progesterone (CL) → maintains pregnancy, inhibits oestrus behaviour, promotes uteroglobin secretion (early embryo nutrition). Inhibin (granulosa cells) → negative feedback → suppresses pituitary FSH → controls follicle numbers recruited.",
        "Why_Not": "Estrogen (granulosa cells of dominant follicle) → positive feedback at mid-cycle LH surge. Oxytocin (CL + posterior pituitary) → stimulates endometrial PGF2alpha release (luteolytic cascade) + stimulates myometrial contractions at parturition. Each hormone's role is precisely timed within the oestrous cycle.",
        "Wow_Approach": "The Whitten Effect (named after Dr. W.K. Whitten, 1956): Introduction of male mice to group-housed female mice synchronizes their oestrous cycles to a 3-day cycle within 72 hours. The mechanism is male preputial gland pheromones (MHC-peptide volatiles) acting on the vomeronasal organ → olfactory bulb → GnRH neurons. Applied in sheep as the 'Ram Effect' for low-cost oestrus synchronization."
    },
    486: {
        "topic": "IFN-tau - Specific Pregnancy Signal in Ruminants",
        "Core_Anatomy": "The bovine elongating trophectoderm (Day 14-21 conceptus), the uterine luminal epithelium (IFN-tau target), and the corpus luteum (protected from luteolysis).",
        "Pathogenesis_Immediate": "Interferon-tau (IFN-tau) is the specific molecular signal produced exclusively by the ruminant trophectoderm to achieve maternal recognition of pregnancy — it is unique to cattle, sheep, goats, and deer among domestic animals.",
        "Pathogenesis_Deep": "IFN-tau production peak: Days 14-25 in cows (peak Days 16-17). IFN-tau is a type I interferon but uniquely lacks the antiviral potency of conventional interferons — it is primarily immunomodulatory and antiluteolytic. Signal mechanism: IFN-tau → JAK1/TYK2 phosphorylation → STAT1/STAT2 activation → ISG15/Mx1/2-5OAS gene expression → suppression of ER-alpha and PGHS-2 → no PGF2alpha production by luminal epithelium → CL maintained.",
        "Why_Not": "In pigs, the trophoblast-derived pregnancy signal is ESTROGEN (estrone/estradiol), not IFN-tau. In horses, there is no specific molecular signal — physical embryo mobility prevents PGF2alpha release. IFN-tau is strictly a ruminant-specific anti-luteolytic protein with no equivalent in non-ruminant domestic species.",
        "Wow_Approach": "IFN-tau has been investigated as a therapeutic agent: systemic or intrauterine recombinant bovine IFN-tau (rbIFN-tau) administered between Days 15-17 post-AI can rescue CLs in cows that would otherwise experience early embryonic death, potentially reducing repeat breeding rates in high-risk animals."
    },
    488: {
        "topic": "Whitten Effect - Male Pheromone-Induced Oestrus Synchronization",
        "Core_Anatomy": "The vomeronasal organ (Jacobson's organ), the olfactory bulb, the GnRH pulse generator in the hypothalamus.",
        "Pathogenesis_Immediate": "The Whitten Effect is the synchronization of oestrous cycles in female mice (and by extension ewes, does, and gilts) induced by introduction of a male or male-soiled bedding, mediated by volatile male pheromones stimulating GnRH pulsatility via the vomeronasal-olfactory pathway.",
        "Pathogenesis_Deep": "Male preputial gland and urinary pheromones (MHC-peptide complexes, dehydro-exo-brevicomin, 2-sec-butyl-4,5-dihydrothiazole) are detected by the vomeronasal organ (VNO) in females. VNO → accessory olfactory bulb → medial amygdala → bed nucleus stria terminalis → arcuate nucleus kisspeptin neurons → GnRH pulse frequency increases → LH surge → ovulation. This neuroendocrine reflex occurs within 2-4 hours of male introduction.",
        "Why_Not": "The Bruce Effect (also pheromone-mediated) is block of pregnancy by exposure to a strange male's urine — causes CL regression in mice during the pre-implantation period. The Lee-Boot Effect is spontaneous prolongation of the dioestrus phase in all-female groups. The Whitten Effect specifically causes cycle synchronization in response to male introduction.",
        "Wow_Approach": "Applied Whitten Effect in livestock: Ram Effect in sheep — introduce rams 15-30 days before desired mating season start. Boar Effect in pigs — boar contact with gilts accelerates puberty onset by 15-30 days. Buck Effect in goats — same principle. These male-introduction methods are cost-free alternatives to hormone synchronization in small-holder farming."
    },
    489: {
        "topic": "Embryo Transport in the Oviduct - Melatonin Role in Seasonal Breeding",
        "Core_Anatomy": "The oviductal isthmus, the smooth muscle layers, and the ciliated epithelium transport system.",
        "Pathogenesis_Immediate": "Embryo transport through the oviduct is regulated by: (1) ciliary beat (toward the uterus), (2) oviductal smooth muscle peristalsis, and (3) luminal fluid flow — all modulated by the local estrogen/progesterone balance. Melatonin regulates the timing of the breeding season (not direct embryo transport).",
        "Pathogenesis_Deep": "Transit times: Bovine embryo takes 3-4 days to traverse the oviduct (infundibulum → ampulla → isthmus → uterus). During this time: Days 0-2 = cleavage in the ampulla. Days 2-4 = morula formation in the isthmus. Day 4-5 = entry into uterus (early blastocyst stage). The uterotubal junction (UTJ) sphincter controls entry timing — progesterone maintains UTJ closure, while embryo-produced PGE2 relaxes it. In mares, only embryos (not unfertilized ova) can produce sufficient PGE2 to open the UTJ.",
        "Why_Not": "Melatonin controls the seasonal timing of reproduction (when the breeding season begins and ends) via the pineal gland-GnRH axis — it does not directly influence oviductal embryo transport speed or direction.",
        "Wow_Approach": "Oviductal embryo co-culture: In IVF, early bovine embryos (Day 1-5) cultured alongside bovine oviductal epithelial cells (BOECs) or conditioned medium develop to blastocyst at higher rates than embryos in standard synthetic media, because BOECs secrete the exact cocktail of oviductin, EGF, and IGF-1 that the embryo requires for optimal early development."
    },
    491: {
        "topic": "VGO Fill-in Key Reproductive Parameters",
        "Core_Anatomy": "Comparative reproductive physiology — species-specific values for key parameters.",
        "Pathogenesis_Immediate": "Critical fill-in values for VGO examination: Semen collection frequency in bulls = 2x/week. Normal semen volume in bulls = 4-8 ml. Normal sperm motility for AI release = ≥70% progressive motility (fresh). Normal sperm morphology = ≥70% normal forms. Minimum sperm concentration for AI = 15-25 million progressively motile sperm per straw.",
        "Pathogenesis_Deep": "Key VGO fill-ins tested annually: Normal estrous cycle: Cow 21 days (range 17-25). Mare 21 days. Ewe 17 days (range 14-20). Sow 21 days. Normal gestation: Cow 280d. Mare 335-340d. Ewe 147d. Sow 114d. Bitch 63d. Cat 63-65d. Duration of oestrus: Cow 12-18h. Mare 4-7d. Ewe 24-36h. Sow 24-72h. Time of ovulation: Cow 24-30h after oestrus end. Mare 24-48h before oestrus end. Ewe 24-30h after oestrus onset.",
        "Why_Not": "These values differ significantly between species and must be memorized precisely — even small errors (e.g., writing 17 days for the bovine oestrous cycle instead of 21 days) constitute incorrect answers in multiple-choice format. Create a species-parameter matrix table for last-minute revision.",
        "Wow_Approach": "Memory shortcut for gestation periods: '280 - 335 - 147 - 114 - 63' → Cow - Horse - Sheep - Pig - Dog. Cow is '9 months + 10 days'. Horse is 'almost 11 months'. Sheep is 'exactly 5 months'. Pig is '3-3-3 rule'. Dog is '63 days = 9 weeks'. These mnemonics enable rapid recall under examination stress."
    },
    498: {
        "topic": "VGO Choose the Best Answer - Obstetrics Overview",
        "Core_Anatomy": "Comparative obstetrical anatomy across bovine, equine, ovine, porcine, and canine species.",
        "Pathogenesis_Immediate": "Key obstetrical answer choices tested in VGO MCQs: Normal presentation in all species = anterior (forelimbs + head presented first). Normal position = dorsal (fetal spine toward maternal dorsum). Normal posture = extended (limbs and head extended). ANY deviation = malpresentation, malposition, or malposture = dystocia.",
        "Pathogenesis_Deep": "Obstetrical terminology: Presentation = which part of the fetus enters the pelvic inlet first (anterior = forelimbs+head; posterior = hindlimbs; transverse = lateral or dorsoventral). Position = relationship of fetal dorsum to maternal dorsum (dorsal position = normal; ventral/lateral = abnormal). Posture = flexion/extension state of fetal limbs and head (extended = normal; various flexions = malposture).",
        "Why_Not": "Posterior presentation (breech or hindlimb-first) is abnormal in cattle and horses but is NORMAL in dogs/cats/pigs (where up to 40% of pups/piglets are born hindlimb-first without dystocia). This species difference is frequently tested — a 'posterior presentation' MCQ answer depends entirely on the species in the question.",
        "Wow_Approach": "Incidence of dystocia by species: Horse = 4-8% (most serious, highest foal mortality). Cattle = 3-8% (heifers much higher, up to 15%). Pigs = 2-5%. Sheep = 3-5%. Dogs = breed-dependent (brachycephalic breeds up to 80%). Cats = <1% (exceptional natural deliverers). Equine dystocia is the highest-risk emergency due to rapid Stage 2 and placental separation."
    },
    499: {
        "topic": "Version - Conversion of Fetal Presentation in Obstetrics",
        "Core_Anatomy": "The fetal body axis, the uterine cavity, and the maternal pelvic inlet.",
        "Pathogenesis_Immediate": "Version is the obstetrical manoeuvre of rotating the fetus on its TRANSVERSE axis to convert it from one PRESENTATION to another (anterior ↔ posterior). This is distinct from Rotation (rotating on the LONG axis to change POSITION).",
        "Pathogenesis_Deep": "Four obstetrical correction manoeuvres: (1) Version = transverse axis rotation → changes PRESENTATION (anterior to posterior or vice versa). (2) Rotation = long axis rotation → changes POSITION (dorsal to ventral or lateral). (3) Extension = correcting a flexed limb or head from flexion to full extension. (4) Retropulsion = pushing the fetus cranially into the uterus to create space for correction. All four may be required in combination for a complex malpresentation.",
        "Why_Not": "Episiotomy changes the birth canal (maternal anatomy), not the fetal presentation. Fetotomy removes fetal parts to allow delivery — not a repositioning manoeuvre. Version is specifically a presentation-changing manoeuvre — converting from transverse to anterior presentation by rotating the entire fetal body 90° around its transverse axis.",
        "Wow_Approach": "Version to posterior presentation (hindlimb-first delivery) is preferable to version to anterior if the fetus is in the caudal half of the uterus — it is faster and requires less manipulation. Posterior delivery requires: hocks and stifles extended (extended hindlimb presentation), NOT the hock-flexed 'breech' which is the most dangerous malpresentation in cattle."
    },
    500: {
        "topic": "Caesarean Section Approach - Right Upper Flank (Paralumbar) in Cattle",
        "Core_Anatomy": "The right paralumbar fossa, the peritoneal cavity, the gravid uterus (abomasum on the right side of the abdomen in cattle), and the linea alba.",
        "Pathogenesis_Immediate": "Abdominal contamination during C-section is most completely avoidable with the Right Upper Flank (Right Paralumbar Fossa) approach, because the gravid uterine horn can be exteriorized through this incision before opening the uterus — preventing spillage of uterine contents (fetal fluids, lochia) into the peritoneal cavity.",
        "Pathogenesis_Deep": "C-section approaches in cattle: (1) Right Paralumbar Fossa (Standing, Right flank) — preferred: uterus is exteriorized before opening, contamination minimal, cow is standing (reduces anaesthetic risk). (2) Left Paralumbar Fossa — used when uterus is on left side (rare) or in conjunction with LDA correction. (3) Ventral Midline (Linea Alba) — most peritoneal contamination risk (gravity-assisted spillage) but excellent exposure. (4) Paramedian — intermediate contamination risk.",
        "Why_Not": "The left flank approach is used in LDA correction (abomasopexy) but not preferred for C-section as the gravid horn is typically right-sided and harder to exteriorize through the left flank. Ventral approaches cause peritonitis risk and cannot be performed in a standing cow.",
        "Wow_Approach": "Right paralumbar fossa C-section procedure: Inverted-L proximal paravertebral block (T13, L1, L2 intercostal nerves) + local infiltration. 30 cm vertical incision through skin, external/internal oblique, transversus abdominis, and peritoneum. Bring gravid uterine horn to the incision. Pack off peritoneum with wet drapes. Open uterus through greater curvature. Deliver calf. Close uterus with Lembert continuous sutures. Post-op: systemic antibiotics 5 days + NSAIDs."
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
