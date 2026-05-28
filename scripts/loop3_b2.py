import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    204: {
        "topic": "VGO - Veterinary Gynaecology and Obstetrics Overview",
        "Core_Anatomy": "The female reproductive tract: ovaries, oviducts, uterine horns, uterine body, cervix, vagina, vulva; and the feto-placental unit.",
        "Pathogenesis_Immediate": "Veterinary Gynaecology and Obstetrics (VGO) encompasses the study of the female reproductive system, pregnancy, parturition, and obstetrical complications in domestic animals.",
        "Pathogenesis_Deep": "Key VGO examination areas: Ovarian pathology (follicular cysts, luteal cysts, ovarian hypoplasia), uterine pathology (pyometra, endometritis, uterine torsion), obstetrical emergencies (dystocia, uterine prolapse, retained placenta), reproductive biotechnology (AI, ET, IVF), and species-specific reproductive physiology (estrus cycles, gestation lengths, parturition mechanisms).",
        "Why_Not": "VGO is distinct from Andrology (male reproduction) and from Reproductive Pharmacology (hormone therapy). However, comprehensive VGO practice integrates all three — a complete reproductive herd health programme addresses both male and female reproductive efficiency simultaneously.",
        "Wow_Approach": "Top 5 most exam-tested VGO topics by frequency: (1) Freemartinism, (2) Uterine Torsion correction methods, (3) Retained Placenta management, (4) Estrus synchronization protocols, (5) Pyometra in small animals. Master these 5 topics first for maximum exam marks."
    },
    205: {
        "topic": "Seasonal Reproductive Patterns in Domestic Animals",
        "Core_Anatomy": "The pineal gland (melatonin production), the hypothalamic GnRH neurons, and the anterior pituitary gonadotrophs.",
        "Pathogenesis_Immediate": "Seasonal breeding in animals is controlled by photoperiod via pineal melatonin secretion. Short-day breeders (sheep, goats, deer) become reproductively active in autumn/winter. Long-day breeders (horses, ferrets) become active in spring/summer.",
        "Pathogenesis_Deep": "Melatonin is produced by the pineal gland exclusively during darkness. In short-day breeders, increasing duration of nocturnal melatonin secretion (as nights lengthen in autumn) stimulates GnRH pulse frequency, initiating the breeding season. In long-day breeders (horses), increasing daylight inhibits melatonin and stimulates reproductive activity. Cattle are essentially non-seasonal breeders, though tropical breeds show subtle seasonal anoestrus under extreme heat.",
        "Why_Not": "Dairy cattle and water buffaloes show year-round cycling but reduced conception rates in peak summer due to heat stress — this is NOT seasonal anoestrus but thermally-induced suboestrus. True seasonal anoestrus in sheep/goats is a photoperiod-driven complete cessation of reproductive activity for 6+ months.",
        "Wow_Approach": "Practical application: Advance the breeding season in sheep by 6-8 weeks using artificial long-night photoperiod (16h dark) for 6-8 weeks, followed by RAM introduction. In horses, use 16-hour artificial lighting from 1 December to advance first ovulation to February-March, optimizing the January 1st universal birth date system used in thoroughbred racing."
    },
    207: {
        "topic": "VGO Objective Questions - True/False Diagnostic Framework",
        "Core_Anatomy": "Female reproductive tract physiology across bovine, equine, ovine, caprine, porcine, and canine species.",
        "Pathogenesis_Immediate": "Key True/False facts in VGO: Silent oestrus in buffaloes is characterized by anovulation — FALSE (silent oestrus involves ovulation without behavioural signs; anovulatory oestrus has behaviour without ovulation). LH deficiency causes delayed ovulation in buffaloes — TRUE.",
        "Pathogenesis_Deep": "Critical VGO True/False facts: Cattle are induced ovulators — FALSE (spontaneous ovulators). Cats are induced ovulators — TRUE. The right ovary is more active in cattle — TRUE (approximately 60% of ovulations from right ovary). Freemartins are sterile — TRUE (bilateral, in 92% of female co-twins with males). IFN-tau prevents luteolysis — TRUE. The horse's placenta is endotheliochorial — FALSE (epitheliochorial, diffuse microcotyledonary).",
        "Why_Not": "Common misconceptions: Cats and rabbits are reflex (induced) ovulators — ovulation triggered by coitus, not spontaneous LH surge. Buffaloes, cattle, sheep, goats, horses, and pigs are all spontaneous ovulators. This distinction is critical for determining AI timing and breeding management.",
        "Wow_Approach": "Memorize induced ovulators as 'CR-BF': Cats, Rabbits, Bears, Ferrets. All farm animal species (cattle, buffalo, sheep, goat, horse, pig) are spontaneous ovulators with predictable estrus-ovulation timing, allowing systematic AI programmes."
    },
    208: {
        "topic": "VGO True/False - Reproductive Physiology Statements",
        "Core_Anatomy": "The endometrium, the corpus luteum, the placenta, and the fetal membranes across species.",
        "Pathogenesis_Immediate": "Key reproductive physiology True/False facts: Ballottement is a technique used to detect floating viscera or masses in the abdominal cavity — TRUE (also used to detect fetal parts in mid-gestation in large animals). Hyperthermia is simple elevation of temperature past the critical point as in heat stroke — TRUE (distinguished from fever/pyrexia which is endogenous pyrogen-mediated).",
        "Pathogenesis_Deep": "Fever (Pyrexia) vs Hyperthermia: Fever = elevation of the hypothalamic set-point by endogenous pyrogens (IL-1, IL-6, TNF-alpha, PGE2) — the body defends the elevated temperature. Hyperthermia = body temperature exceeds thermoregulatory capacity (heat stroke, malignant hyperthermia under anaesthesia) without set-point elevation — the body attempts to cool but fails. Antipyretics (NSAIDs) block PGE2 synthesis and are effective for fever but NOT for hyperthermia.",
        "Why_Not": "Antipyretics (aspirin, flunixin meglumine) effectively reduce fever by blocking the PGE2-mediated set-point elevation in the hypothalamus. They are ineffective in heat stroke hyperthermia because the set-point remains normal — the animal simply cannot dissipate heat fast enough. Treatment for heat stroke is active cooling (cold water, ice packs, fans), not antipyretics.",
        "Wow_Approach": "Ballottement technique in cattle pregnancy diagnosis: Place palm of hand firmly against the right flank (Day 90-150 of pregnancy). Give a sharp push inward and feel for the rebound of the fetal mass against the hand. The fetus floats in amniotic fluid and 'ballots' (bounces) back against the palm — a positive test confirms fetal presence in mid-gestation."
    },
    224: {
        "topic": "VGO Fill-in-the-Blank - Key Reproductive Terms",
        "Core_Anatomy": "The bovine reproductive tract and comparative reproductive physiology across species.",
        "Pathogenesis_Immediate": "Key VGO fill-in terms: Gestation period of cattle = 280 days (9 months 10 days). Gestation of horse = 335-340 days (11 months). Sheep = 147-150 days (5 months). Goat = 145-150 days. Pig = 114 days (3 months 3 weeks 3 days rule). Dog = 63 days. Cat = 63-65 days.",
        "Pathogenesis_Deep": "Critical VGO blanks: Oestrus duration in cattle = 12-18 hours. Oestrus in mare = 4-7 days. Oestrus in ewe = 24-36 hours. Oestrus cycle length in cattle = 21 days. Cycle in mare = 21 days. Cycle in ewe = 17 days. Cycle in sow = 21 days. Normal litter size in sow = 10-14 piglets. Normal litter in bitch = 6-8 puppies. Twining rate in cattle = 1-4%.",
        "Why_Not": "Memorize gestation periods using the 'Three rules' for pigs (3-3-3: 3 months, 3 weeks, 3 days = 114 days). For horses, remember '11 months' as a minimum guide. These figures are tested extensively in fill-in-the-blank questions across all VGO examination papers.",
        "Wow_Approach": "Practical application: A cow inseminated on Day 1, expected to calve on Day 280. Count 280 days from AI date = expected calving date. Use the '9 months + 7 days' shortcut: Add 9 months and 7 days to the breeding date to estimate the calving date quickly in the field."
    },
    239: {
        "topic": "Freemartinism in Cattle - XX/XY Chimerism",
        "Core_Anatomy": "The chorionic vascular anastomoses between twin placentas, the Müllerian duct system, and the gonadal primordium.",
        "Pathogenesis_Immediate": "Freemartinism is a naturally occurring intersex condition in cattle where a female born co-twin with a male calf is sterile in approximately 92% of cases, caused by the exchange of blood (and sex hormones) through placental vascular anastomoses between the twins.",
        "Pathogenesis_Deep": "In bovine twins, chorionic vascular anastomoses form between the two placentas by Day 30-40 of gestation. The male twin's testes develop earlier and produce testosterone and anti-Müllerian hormone (AMH). AMH circulates via the shared vasculature into the female twin, suppressing her Müllerian duct (uterus/cervix/vagina) development and masculinizing her gonads. The female twin is born with rudimentary gonads (streak gonads), hypoplastic/absent uterus, and a blind vaginal pouch.",
        "Why_Not": "Male co-twins are not affected (their fully developed testes are unresponsive to the smaller quantity of hormones circulating from the female). The freemartin female appears externally normal (vulva present) but the vagina ends blindly at 5-10 cm depth. The Whiteside test (modified milk whiteside test for SCC) is irrelevant — use vaginal probe (>10 cm vaginal depth = normal female; <10 cm = probable freemartin).",
        "Wow_Approach": "Confirm freemartinism by: (1) Vaginal probe test (<10 cm depth = freemartin). (2) Karyotyping: Shows XX/XY chimerism (mixture of male and female cells in blood). (3) Blood chimerism test (flow cytometry). Any female calf born co-twin with a male should be tested before purchase — 92% are sterile freemartins, worthless for breeding."
    },
    247: {
        "topic": "Obstetrical Correction Methods - Mutation, Retropulsion, Rotation, Version",
        "Core_Anatomy": "The fetal body (head, limbs, pelvis), the uterine cavity, the cervix, and the maternal pelvic canal.",
        "Pathogenesis_Immediate": "The four obstetrical correction manoeuvres used to correct malpresentations/malpositons/malpostures in dystocia: Mutation (general term), Retropulsion (pushing fetus back), Rotation (rotating fetus), and Version (converting presentation).",
        "Pathogenesis_Deep": "Definitions: Retropulsion — pushing the fetus back into the uterine horn to create space for correction (requires uterine relaxation with Isoxsuprine/Clenbuterol). Rotation — rotating the fetus around its long axis to correct malposition (e.g., converting from ventral to dorsal position). Version — converting a posterior (breech) presentation to anterior presentation or vice versa. Mutation — a general term encompassing all corrective manoeuvres of fetal extremities (extension/flexion of limbs, correction of head/neck deviations).",
        "Why_Not": "Episiotomy is a surgical incision of the vulva/perineum to enlarge the birth canal opening (not a fetal correction manoeuvre). Caslick's operation is a surgical procedure suturing the dorsal vulva to prevent pneumovagina/urovagina in mares (not an obstetrical manoeuvre). Reefing operation is a technique for reducing uterine prolapse.",
        "Wow_Approach": "Always lubricate the birth canal generously (warm soap solution, methylcellulose gel) before any obstetrical correction. Apply epidural anaesthesia (5-10 ml 2% Lignocaine at Co1-Co2) to eliminate straining. In prolonged dystocia, fetal viability is assessed by corneal reflex and swallowing response — a live calf must be delivered with maximum care to avoid CNS injury."
    },
    248: {
        "topic": "Oxytocin for Uterine Inertia - Dosing and Indications in Bitches",
        "Core_Anatomy": "The myometrium of the uterine horns, the oxytocin receptor (OXTR) system, and calcium-dependent uterine smooth muscle contraction.",
        "Pathogenesis_Immediate": "Oxytocin is the drug of choice for treating primary uterine inertia in bitches (confirmed open birth canal with live pup at pelvic inlet), administered at 0.5-2.0 IU intramuscularly to stimulate myometrial contractions and facilitate pup delivery.",
        "Pathogenesis_Deep": "Oxytocin binds uterine OXTR, activating Gq protein → phospholipase C → IP3 → sarcoplasmic reticulum calcium release → myosin light chain kinase activation → actin-myosin cross-bridge formation → uterine contraction. In primary inertia, the uterus has failed to initiate coordinated contractions despite a term fetus at the pelvic inlet. Precede oxytocin with IV calcium gluconate (10 ml of 10% solution) to sensitize the myometrium and improve oxytocin responsiveness.",
        "Why_Not": "Buserelin (GnRH analog) stimulates endogenous LH/FSH release — useful for superovulation induction and delayed ovulation treatment, NOT for uterine inertia. Tiaprost (PGF2alpha analog) causes luteolysis and cervical dilation but is too slow for emergency inertia management. Progesterone suppresses uterine contractions and would worsen inertia.",
        "Wow_Approach": "Low-dose oxytocin protocol in bitches: 0.5-1.0 IU IM every 20-30 minutes, maximum 3 doses. If no pup delivered after 3 doses, proceed immediately to C-section. Never give more than 3 doses — repeated high doses cause tetanic uterine contraction that can rupture the uterus or cause fetal hypoxia from placental compression."
    },
    249: {
        "topic": "Schaffer's Method for Uterine Torsion Correction in Cattle",
        "Core_Anatomy": "The gravid uterus, the mesometrium (broad ligaments), and the maternal abdominal wall musculature.",
        "Pathogenesis_Immediate": "Schaffer's Plank (Rolling) Method is the primary non-surgical technique for correcting post-cervical uterine torsion in cows and buffaloes, using a 12-foot wooden plank pressed against the flank to stabilize the gravid uterus while the cow's body is rolled in the direction of the torsion.",
        "Pathogenesis_Deep": "Technique: (1) Cast the cow on the side of the torsion (if right-sided torsion, cast on right side). (2) Place the plank across her upper abdomen (covering the flank region over the uterus). An assistant stands on the plank applying firm pressure to the flank, immobilizing the uterus. (3) Pull the legs firmly and roll the cow rapidly to the opposite side (rolling to the right for right torsion). The uterus, held by the plank pressure, stays stationary while the cow's body rotates around it — untwisting the torsion. (4) Verify detorsion by rectal palpation and vaginal examination.",
        "Why_Not": "Caslick's Operation is a perineal surgery to suture the dorsal vulva in mares to prevent pneumovagina — completely unrelated to uterine torsion. Episiotomy is a dorsal vulvar incision to enlarge the birth canal. The Reefing method is used to reduce uterine prolapse (not torsion). Schaffer's rolling method is uniquely designed for torsion correction.",
        "Wow_Approach": "Success rate of Schaffer's method: 70-85% for torsions <180°. For torsions >270°, the broad ligaments are severely compressed, and Schaffer's method fails — laparotomy (left flank approach, manual detorsion through the uterine wall) is required. After detorsion, always perform a vaginal examination to confirm cervical dilation and fetal viability before proceeding with delivery."
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
