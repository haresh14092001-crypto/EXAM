import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    452: {
        "topic": "Veterinary Gynaecology and Obstetrics I - Subject Overview",
        "Core_Anatomy": "The bovine, equine, ovine, caprine, porcine, and canine female reproductive tracts.",
        "Pathogenesis_Immediate": "VGO-I covers core reproductive physiology: oestrous cycle regulation, folliculogenesis, ovulation, fertilization, embryonic development, implantation, placentation, and endocrine control of pregnancy in domestic animals.",
        "Pathogenesis_Deep": "VGO-I examinations test: Species-specific oestrous cycle lengths (cattle 21d, horse 21d, sheep 17d, pig 21d, dog 7 months anestrus), gestation lengths, placentation types, methods of pregnancy diagnosis (rectal palpation, ultrasonography, progesterone assay, Cuboni test for mares), and reproductive failure causes (repeat breeding, anovulatory oestrus, silent heat).",
        "Why_Not": "VGO-II covers obstetrics (parturition, dystocia, fetal membrane pathology), while VGO-I covers gynaecology (non-obstetrical reproductive tract pathology: ovarian cysts, endometritis, pyometra, metritis, uterine torsion). Understanding this division helps focus examination preparation on the correct paper.",
        "Wow_Approach": "Top high-yield VGO-I topics by examination frequency: (1) Freemartinism diagnosis and mechanism. (2) IFN-tau and maternal recognition of pregnancy. (3) Ovarian cyst types and treatment. (4) Embryo transfer recipient synchronization. (5) Oestrus detection methods and efficiency calculations."
    },
    454: {
        "topic": "Embryo Transfer Recipient Synchronization Requirements",
        "Core_Anatomy": "The corpus luteum of the recipient cow (Days 5-7 post-ovulation), the uterine endometrium, and the progesterone-primed uterine environment.",
        "Pathogenesis_Immediate": "In embryo transfer (ET), the recipient cow's oestrous cycle must be synchronized within ±1 day of the donor's cycle, ensuring the recipient's uterine environment (progesterone-primed endometrium) matches the developmental stage of the transferred embryo.",
        "Pathogenesis_Deep": "Embryo transfer timing: Day 0 = oestrus. Day 6-8 = embryo collection from donor. The collected embryo (typically a morula or early blastocyst) is non-surgically transferred into the recipient's uterine horn ipsilateral to a CL of equivalent age. The recipient CL must be Days 5-8 post-ovulation (progesterone peak) to create the optimal uterine microenvironment matching the embryo's developmental stage. A ±24-hour cycle discrepancy reduces pregnancy rates significantly.",
        "Why_Not": "If the recipient's CL is too young (Days 1-4), progesterone levels are insufficient for embryo support — pregnancy fails. If the recipient's CL is too old (Days 10+), the luteolytic process is already initiated — the CL will regress before the embryo can produce IFN-tau. Precise synchronization (via two-injection PGF2alpha protocol, Days 0 and 11) is critical.",
        "Wow_Approach": "Modern non-surgical ET pregnancy rates: 60-65% per transfer using a good quality (Grade 1-2) fresh morula/blastocyst. Frozen-thawed embryo transfer rates: 50-55%. Superovulation protocol for donors: FSH injections twice daily for 4 days (declining dose: 50-40-30-20 mg) starting Day 9-11 of cycle, followed by PGF2alpha on Day 11 to synchronize luteolysis."
    },
    455: {
        "topic": "Embryo Transfer Recipient Selection and Synchronization Protocol",
        "Core_Anatomy": "The bovine corpus luteum, the uterine endometrium, and the cervix.",
        "Pathogenesis_Immediate": "For optimal results in embryo transfer, the recipient cow should have: (1) A corpus luteum of equivalent age (within 24 hours) to the donor. (2) Body condition score 3.0-3.5. (3) Negative history of reproductive disease. (4) Normal uterine tone and cervical patency on rectal palpation.",
        "Pathogenesis_Deep": "Recipient selection criteria: Age 2-5 years (young uterine environment, optimal endometrial receptivity). BCS 3.0-3.5 (neither thin nor fat). At least 45 days post-partum (uterine involution complete). No history of metritis, endometritis, or repeat breeding. Rectal palpation Day 6-8 post-oestrus: firm CL palpable on one ovary (confirms luteal phase). Progesterone >2 ng/ml on Day 7 confirms adequate CL function.",
        "Why_Not": "Recipients with BCS <2.5 (thin) have poor uterine blood flow and endometrial thickness, reducing embryo implantation. Recipients with BCS >4.0 (fat) have fatty uterine degeneration and reduced uterine contractility. Thin cows also have inadequate progesterone production to maintain early pregnancy.",
        "Wow_Approach": "Recipients are typically cross-bred or lower-genetic-value cows that are synchronized at the same time as donors but NOT superovulated. In commercial ET, 10-15 recipients are synchronized for every donor to ensure adequate numbers with appropriate CL stages on collection day. Recipients failing the CL check on Day 7 are excluded."
    },
    467: {
        "topic": "Signet Ring Appearance - Early Blastocyst Stage Embryo",
        "Core_Anatomy": "The blastocyst (trophoblast + inner cell mass + blastocoel cavity) of the bovine preimplantation embryo.",
        "Pathogenesis_Immediate": "The 'Signet Ring' appearance of a bovine embryo on light microscopy describes the Early Blastocyst stage — where the blastocoel cavity (fluid-filled space) enlarges to one side, pushing the inner cell mass (embryoblast) to the periphery, creating the appearance of a ring with a gem (the ICM).",
        "Pathogenesis_Deep": "Bovine embryo development timeline post-fertilization: Day 1 = zygote. Day 2 = 2-cell. Day 3 = 4-8 cell (compaction begins). Day 4-5 = Morula (compact ball of cells, no cavity). Day 5-6 = Early Blastocyst (blastocoel begins forming, signet ring appearance). Day 7 = Blastocyst (distinct ICM and trophoblast). Day 8-9 = Expanded Blastocyst (zona pellucida thinning). Day 9-10 = Hatched Blastocyst (zona dissolved, ICM expanding).",
        "Why_Not": "The Compact Morula has no cavity — all cells are undifferentiated blastomeres in tight junctions. The signet ring appearance is uniquely associated with EARLY BLASTOCYST when the blastocoel begins forming asymmetrically before it fills the entire embryo. This embryo stage (Grade 2 early blastocyst) is routinely recovered and successfully transferred or frozen.",
        "Wow_Approach": "IETS (International Embryo Transfer Society) morphological grading: Grade 1 = Excellent/Good (tight, uniform, >85% viable cells). Grade 2 = Fair (minor defects, 50-85% viable). Grade 3 = Poor (major defects, <50% viable). Grade 4 = Dead/Degenerate. Only Grade 1 and 2 embryos are transferred or frozen — Grade 3 and 4 are discarded."
    },
    468: {
        "topic": "Oviduct Regions and Secretory Cells - Ampulla",
        "Core_Anatomy": "The ampulla of the oviduct (the widest, most convoluted segment), lined by ciliated and secretory (non-ciliated) epithelial cells.",
        "Pathogenesis_Immediate": "The Ampulla contains the largest number of secretory (non-ciliated, peg) epithelial cells in the oviduct, producing the tubular fluid that nourishes the zona-enclosed embryo during its transit from the site of fertilization (ampullary-isthmic junction) toward the uterus.",
        "Pathogenesis_Deep": "Oviduct segments (proximal to distal): Infundibulum → Ampulla → Isthmus → Uterotubal Junction. The Ampulla: (1) Is the site of fertilization (ampullary-isthmic junction). (2) Has the highest proportion of secretory cells, producing albumin, oviductin (glycoprotein), transferrin, and growth factors. (3) The embryo spends Days 0-3 here. The Isthmus: High proportion of ciliated cells, stores capacitated sperm in the sperm reservoir. The Infundibulum: Ciliated cells capture the released oocyte at ovulation.",
        "Why_Not": "The Isthmus primarily stores sperm and transports the embryo via ciliary beat. The Infundibulum captures the COC (cumulus-oocyte complex) and has mostly ciliated cells for directional transport. Only the Ampulla has the high secretory cell density essential for early embryo nutrition and zona pellucida modification.",
        "Wow_Approach": "Oviductin (bovine oviduct-specific glycoprotein, BSP-30) secreted by ampullary cells binds the zona pellucida and sperm surface, enhancing sperm-zona recognition and fertilization rates. This is why in vitro fertilization (IVF) systems supplement culture media with oviductal fluid or oviductin protein to improve fertilization and early cleavage rates."
    },
    469: {
        "topic": "Maternal Recognition of Pregnancy in Cows - Days 16-19",
        "Core_Anatomy": "The elongating trophectoderm of the bovine conceptus (Days 14-21), the uterine luminal epithelium, and the corpus luteum.",
        "Pathogenesis_Immediate": "In cattle, maternal recognition of pregnancy (MRP) occurs between Days 16 and 19 of gestation, when the elongating bovine trophectoderm produces IFN-tau in sufficient quantities to block endometrial PGF2alpha release and prevent luteolysis.",
        "Pathogenesis_Deep": "IFN-tau peak production corresponds with maximal trophectoderm elongation (the filamentous bovine conceptus reaches >100 mm length by Day 16-17). IFN-tau acts in a paracrine manner on the endometrial luminal epithelium, suppressing ER-alpha expression and blocking the estrogen-induced OTR upregulation. Without OTRs, oxytocin pulses from the CL cannot initiate the luteolytic PGF2alpha cascade, the CL is preserved, and progesterone maintains pregnancy.",
        "Why_Not": "In sheep, MRP occurs slightly earlier (Days 12-14). In pigs, MRP requires estrogen produced by the conceptus (Days 11-12). In horses, the embryo's physical presence (mechanoreceptor stimulation of the endometrium during migration Days 10-16) prevents PGF2alpha release. Only in ruminants is IFN-tau the specific molecular signal.",
        "Wow_Approach": "If IFN-tau production is inadequate (due to embryo stress, heat, or poor conceptus development), the CL regresses normally on Days 16-18 and early embryonic death occurs. This is the most common cause of repeat breeding in cattle — embryonic death between Days 8-16. Progesterone supplementation (CIDR, Day 5-18) can 'rescue' borderline pregnancies by improving uterine receptivity."
    },
    470: {
        "topic": "Unfertilized Ova Retained in Oviduct - Species-Specific Embryo Transport",
        "Core_Anatomy": "The uterotubal junction (sphincter), the oviductal isthmus, and the cilia of the oviductal epithelium.",
        "Pathogenesis_Immediate": "In Mares (horses), only embryos are transported from the oviduct into the uterus — unfertilized ova are retained in the oviduct indefinitely. This is the only domestic species with this selective embryo-transport mechanism.",
        "Pathogenesis_Deep": "The equine uterotubal junction acts as a molecular filter: embryo-produced PGF2alpha and PGE2 relax the uterotubal sphincter (progesterone and estrogen sensitive), allowing the embryo's passage around Days 5-6 post-ovulation. Unfertilized oocytes lack this paracrine signalling capacity and are retained in the isthmus for months without entering the uterus. This mechanism prevents uterine accumulation of non-viable embryos and protects the uterine environment.",
        "Why_Not": "In cattle, both fertilized AND unfertilized ova are transported into the uterus within 3-4 days post-ovulation via ciliary and smooth muscle activity. In bitches, both ova and embryos pass into the uterus. Only the mare has species-unique embryo-selective transport — a key MCQ fact that is frequently tested.",
        "Wow_Approach": "Practical implication: In equine embryo recovery (ET), flushing begins on Day 7-8 post-ovulation (when the embryo has just entered the uterus). If flushing is performed too early (Day 5), the embryo is still in the oviduct and cannot be collected non-surgically. Surgical (laparoscopic) oviductal flushing is required for Day 5 embryo collection in mares."
    },
    471: {
        "topic": "Blastocyst Hatching in Cows - Days Post-Ovulation",
        "Core_Anatomy": "The zona pellucida (glycoprotein shell surrounding the embryo), the trophectoderm, and the blastocoel cavity.",
        "Pathogenesis_Immediate": "In cattle, blastocyst hatching from the zona pellucida occurs between Days 8-11 post-ovulation (approximately Days 8-9 in practice), as the expanding blastocoel pressure and embryonic protease (strypsin) activity digest and rupture the zona pellucida.",
        "Pathogenesis_Deep": "Zona pellucida hatching process: As the blastocyst expands, intraluminal pressure from the growing blastocoel stretches the zona pellucida thin. Simultaneously, the trophectoderm cells secrete strypsin (a trypsin-like protease) that digests a point in the zona pellucida. The blastocyst 'pips' through (similar to a chick hatching from an egg) and rapidly expands to form the elongating trophoblast. Hatching is a prerequisite for implantation in all species (attachment occurs only after zona removal).",
        "Why_Not": "Option 2-4 days is the 2-cell to 8-cell cleavage period — too early. Option 4-8 days is morula formation. Option 8-11 days is the correct blastocyst hatching window. In mice, hatching occurs on Day 4-5; in humans, Day 5-6; in cattle, Days 8-11 (the slowest among domestic species due to longer conceptus development time).",
        "Wow_Approach": "In IVF/ICSI programmes, hatching can be artificially assisted using: (1) Laser-assisted hatching (drilling a precise 10-15 μm hole in the zona using a 1.48 μm infrared diode laser). (2) Chemical hatching (brief exposure to Tyrode's Acid solution). (3) Mechanical hatching (micropipette pressure). Assisted hatching improves embryo transfer pregnancy rates by 10-15% in embryos with thickened zonae."
    },
    472: {
        "topic": "Intercornual Ligament - Species-Specific Anatomical Feature in Cows",
        "Core_Anatomy": "The intercornual ligament (a fibrous band connecting the two uterine horns ventrally at their junction with the uterine body) — present in Cows, absent in mares.",
        "Pathogenesis_Immediate": "The Intercornual Ligament is a distinct anatomical structure present in COWS (Bos taurus), connecting the two uterine horns at the bifurcation point. It is absent in mares, bitches, and sows. It is palpable rectally as a transverse fibrous band between the two uterine horns.",
        "Pathogenesis_Deep": "The intercornual ligament in cattle: Located at the bifurcation of the uterine horns from the uterine body. Can be felt as a firm ridge ('intercornual groove') between the two horn bases during rectal pregnancy diagnosis. In early pregnancy (Days 25-35), the pregnant horn is larger, softer, and fluctuant compared to the non-pregnant horn — the intercornual ligament provides a reference point for comparing horn sizes during rectal examination.",
        "Why_Not": "The mare's uterus has a T-shaped ('bicornuate simplex') configuration with a short uterine body and long uterine horns but NO intercornual ligament — the horns join directly at the body without a discrete fibrous connection. This is an important anatomical distinguishing feature in comparative reproductive anatomy examinations.",
        "Wow_Approach": "The intercornual ligament is also used as an anatomical landmark during C-section in cattle: the incision is made in the greater curvature of the pregnant uterine horn (identified by palpating the fetal parts and tracing back to the intercornual bifurcation). The uterine incision avoids the intercornual ligament to prevent haemorrhage from the uterine branch vessels running within it."
    },
    475: {
        "topic": "Bovine Ovulation Timing - 24-48 Hours Post-Oestrus End",
        "Core_Anatomy": "The preovulatory follicle (Graafian follicle), the LH surge, and the cumulus-oocyte complex (COC).",
        "Pathogenesis_Immediate": "In cattle, ovulation occurs on average 24-30 hours after the END of oestrus (or approximately 30-35 hours after the LH surge peak), making it the LAST event of the reproductive cycle — oestrus ends BEFORE ovulation.",
        "Pathogenesis_Deep": "Bovine LH surge: begins 2-4 hours before the onset of standing oestrus, peaks at the midpoint of oestrus, and the preovulatory follicle ruptures 24-30 hours after oestrus end. This is the physiological basis for the AM-PM rule: cows seen in oestrus in the morning (AM) are inseminated in the evening (PM) of the same day; cows seen in oestrus in the evening (PM) are inseminated the following morning (AM). This timing maximizes sperm presence at the ampullary-isthmic junction at the time of ovulation.",
        "Why_Not": "In mares, ovulation occurs 24-48 hours BEFORE the end of oestrus (opposite to cattle — the mare's oestrus ends AFTER ovulation). In sheep, ovulation occurs 24-30 hours after oestrus onset. Understanding species-specific ovulation timing relative to oestrus is critical for optimizing AI timing in each species.",
        "Wow_Approach": "The bovine ovulation timing was established definitively by Trimberger (1948): AI performed 12-18 hours before ovulation achieves maximum conception rates (allowing sperm capacitation time + ensuring viable sperm at ovulation site). AI performed after ovulation results in dramatically reduced conception as the oocyte rapidly ages and becomes non-fertilizable within 6-8 hours post-ovulation."
    },
    476: {
        "topic": "Fincher's Test for Uterine Torsion Diagnosis",
        "Core_Anatomy": "The broad ligaments (mesometrium), the vaginal walls, and the cervix in cases of uterine torsion.",
        "Pathogenesis_Immediate": "Fincher's Test is the vaginal examination technique for diagnosing uterine torsion in cattle, based on palpation of: (1) the twisted broad ligaments (mesometrial folds visible as spiralling bands crossing the vaginal roof), and (2) deviation of the cervix from the midline.",
        "Pathogenesis_Deep": "Technique: Insert a gloved arm into the vagina (after epidural anaesthesia). Feel the vaginal walls — in uterine torsion, one broad ligament runs diagonally across the vaginal roof from upper left to lower right (or vice versa) creating a characteristic 'twist' or 'corkscrew' sensation. The cervix is pulled laterally toward the side of the torsion. Degree of torsion determines vaginal accessibility: <180° torsion — can reach cervix. >270° torsion — vagina ends blindly.",
        "Why_Not": "Cystic ovary diagnosis requires rectal palpation (follicular cysts are soft, >2.5 cm; luteal cysts are firm, thick-walled). Freemartinism diagnosis uses the vaginal probe test + karyotyping. Paraovarian cyst diagnosis uses rectal palpation and ultrasonography. Fincher's test is uniquely the vaginal examination for TORSION.",
        "Wow_Approach": "Determine torsion direction during Fincher's test: If the right broad ligament crosses from upper-left to lower-right (dorsal-to-ventral when viewed from behind), the torsion is clockwise (right-sided). This determines the rolling direction for Schaffer's method: roll the cow to the LEFT (counter-clockwise) to untwist a right-sided clockwise torsion."
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
