import json
import re
from pathlib import Path

def run_direct_enrichment():
    db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
    
    if not db_path.exists():
        print(f"Error: {db_path} not found.")
        return
        
    with open(db_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract the JSON array
    json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
    json_str = json_str.rsplit(';', 1)[0].strip()
    data = json.loads(json_str)
    
    # Pre-formulated clinical content dictionary mapped by Question ID
    enrichment_data = {
        # BATCH 1: IDs 261, 267, 268, 269, 270, 271, 279, 285, 287, 299 (Already formulated in chat)
        261: {
            "subject": "Theriogenology",
            "topic": "The Corpus Luteum and Luteotrophic Support in Cows",
            "Core_Anatomy": "Ovarian cortex, the ruptured Graafian follicle cavity (ovulation site), and the newly formed luteal parenchyma (Yellow Body).",
            "Pathogenesis_Immediate": "Following ovulation, the granulosa and theca cells of the follicle undergo morphological and biochemical luteinization to form the Corpus Luteum (CL). The CL secretes progesterone, supported by systemic luteotrophic hormones, to maintain early pregnancy.",
            "Pathogenesis_Deep": "Luteinization is driven by luteinizing hormone (LH). Granulosa cells hypertrophy to become Large Luteal Cells (LLCs), and theca cells divide to form Small Luteal Cells (SLCs). In cows, LH is the principal luteotrophic hormone, stimulating basal progesterone secretion via the cAMP pathway. Progesterone acts on the endometrium to stimulate histotroph ('uterine milk') secretion and suppress myometrial contractility.",
            "Why_Not": "In the ewe, prolactin combined with LH forms the luteotrophic complex. In the cow, LH alone is the principal luteotrophic driver, and prolactin plays a minor role in maintaining the CL, whereas in primates, hCG acts as the primary luteotrophic signal of pregnancy to prevent luteolysis.",
            "Wow_Approach": "The bovine CL is highly vascularized; blood flow to the CL is greater per unit tissue than to any other organ in the body. Clinically, transrectal ultrasonography is used to evaluate CL diameter and the presence of a fluid-filled cavity (cavitary CL), which is a normal variation and secretes normal levels of progesterone."
        },
        267: {
            "subject": "Theriogenology",
            "topic": "Ecbolic Drugs in Veterinary Practice",
            "Core_Anatomy": "Myometrial smooth muscle cells of the uterine horns and the cervix.",
            "Pathogenesis_Immediate": "Ecbolic drugs (uterine contractants like Oxytocin, Cloprostenol, and Ergot alkaloids) are administered to induce myometrial contractions, helping expel retained placenta, uterine exudates (pyometra), or a dead fetus, or to treat uterine inertia.",
            "Pathogenesis_Deep": "Oxytocin binds to G-protein coupled oxytocin receptors on the myometrium, activating phospholipase C. This generates IP3 (inositol trisphosphate), releasing calcium from the sarcoplasmic reticulum, causing rapid, rhythmic myometrial contractions. In contrast, PGF2alpha (Cloprostenol) causes direct calcium influx and luteolysis, dropping progesterone and dilating the cervix, while causing sustained, tonic contractions.",
            "Why_Not": "Oxytocin is highly effective for immediate, rhythmic contractions when the cervix is already dilated. Prostaglandin F2alpha (Cloprostenol) is the drug of choice when the cervix is closed and luteolysis is required first, as oxytocin cannot dilate a rigid, progesterone-primed cervix.",
            "Wow_Approach": "Always ensure the cervix is fully dilated before administering oxytocin. Administering oxytocin in a cow with an un-dilated cervix or a malpresentation can cause fatal uterine rupture."
        },
        268: {
            "subject": "Theriogenology",
            "topic": "Semen Volume Abnormalities (Hyperspermia)",
            "Core_Anatomy": "The accessory sex glands (seminal vesicles, prostate, bulbourethral glands) and the pelvic urethra.",
            "Pathogenesis_Immediate": "Hyperspermia is a condition characterized by abnormally high ejaculate volume, which dilutes sperm concentration, lowering fertilization rates unless the semen is concentrated or carefully evaluated.",
            "Pathogenesis_Deep": "Ejaculate volume is determined by the secretory activity of the accessory glands. Hyperspermia is caused by hyper-secretion of the seminal vesicles or prostate due to subclinical inflammation (seminal vesiculitis) or over-stimulation during collection. The high fluid volume increases the distance sperm must travel and decreases the concentration of protective seminal proteins per unit volume.",
            "Why_Not": "Hypospermia (abnormally low semen volume) is typically caused by incomplete collection, retrograde ejaculation, or accessory sex gland hypoplasia. Hyperspermia represents a true hyper-secretory event that dilutes sperm density.",
            "Wow_Approach": "During breeding soundness evaluations, if a bull exhibits hyperspermia with extremely low concentration and excessive inflammatory cells (neutrophils), perform transrectal palpation of the seminal vesicles to diagnose and treat seminal vesiculitis."
        },
        269: {
            "subject": "Theriogenology",
            "topic": "Sperm Concentration Pathology (Oligozoospermia)",
            "Core_Anatomy": "The seminiferous epithelium of the testes, Sertoli cells, and Leydig cells.",
            "Pathogenesis_Immediate": "Oligozoospermia (abnormally low concentration of spermatozoa in the ejaculate) reduces the fertile capacity of the male, caused by testicular degeneration, testicular hypoplasia, or high heat stress.",
            "Pathogenesis_Deep": "Spermatogenesis requires a low scrotal temperature and high local testosterone. Under heat stress (fever, high ambient temperature), Sertoli cell function is disrupted, causing apoptosis of developing spermatids. This reduces the daily sperm production, resulting in a low concentration of sperm in the semen.",
            "Why_Not": "Azoospermia is the *complete absence* of spermatozoa in the ejaculate (often due to ductal occlusion). Oligozoospermia is a quantitative reduction in sperm count, indicating a compromised but functional spermatogenic cycle.",
            "Wow_Approach": "If a bull displays oligozoospermia, measure the scrotal circumference and evaluate for signs of testicular degeneration (soft, spongy testes). Treat with sexual rest for at least 60 days (the length of one full spermatogenic cycle) and evaluate again."
        },
        270: {
            "subject": "Theriogenology",
            "topic": "Sperm Absence (Azoospermia) in Bulls",
            "Core_Anatomy": "The epididymis (head, body, tail), ductus deferens, and the efferent ductules.",
            "Pathogenesis_Immediate": "Azoospermia is the complete absence of spermatozoa in the ejaculate, rendering the bull sterile, caused by complete testicular arrest (bilateral testicular hypoplasia) or physical blockage of the excurrent ducts (bilateral epididymitis).",
            "Pathogenesis_Deep": "Bilateral epididymal occlusion (often due to chronic infection with *Brucella abortus* or *Actinobacillus seminis*) blocks the transit of sperm from the testes to the pelvic urethra. The ejaculate consists entirely of accessory sex gland fluids. If caused by testicular hypoplasia, the seminiferous tubules lack germ cells (Sertoli-cell-only syndrome), failing to produce any sperm.",
            "Why_Not": "Aspermia is the *complete lack of ejaculation* (failure of emission or ejaculation due to nerve damage). Azoospermia is a normal volume ejaculate that is completely devoid of spermatozoa.",
            "Wow_Approach": "Differentiate obstructive azoospermia from testicular failure by measuring seminal fructose and alkaline phosphatase (ALP). High ALP in the semen indicates the epididymal ducts are patent, as ALP is primarily produced in the epididymis; low ALP confirms bilateral ductal obstruction."
        },
        271: {
            "subject": "Theriogenology",
            "topic": "Sperm Viability Pathology (Necrozoospermia)",
            "Core_Anatomy": "The sperm plasma membrane, mitochondria in the midpiece, and the epididymal environment.",
            "Pathogenesis_Immediate": "Necrozoospermia is a condition characterized by a high percentage of dead, immotile spermatozoa in the ejaculate, causing complete sterility despite normal sperm concentration.",
            "Pathogenesis_Deep": "Spermatozoa die due to structural membrane disruption or severe oxidative stress. High levels of Reactive Oxygen Species (ROS) oxidize the polyunsaturated fatty acids in the sperm plasma membrane, causing lipid peroxidation. This destroys membrane integrity, halts mitochondrial ATP production, and causes cell death. Chronic epididymitis can also produce a hostile, hyper-acidic environment that kills sperm during storage.",
            "Why_Not": "Asthenozoospermia refers to sperm that are *alive but immotile* (due to structural defects in the axoneme like the Dag defect). Necrozoospermia refers to sperm that are dead, confirmed by membrane dye uptake.",
            "Wow_Approach": "Verify necrozoospermia using live-dead vital staining (Eosin-Nigrosin stain). Live sperm exclude the eosin dye and remain white; dead sperm have damaged membranes, absorb the pink dye, and appear pink against the dark nigrosin background."
        },
        279: {
            "subject": "Theriogenology",
            "topic": "Testicular Degeneration in Bulls",
            "Core_Anatomy": "The seminiferous tubules, Leydig cells, Sertoli cells, and the blood-testis barrier.",
            "Pathogenesis_Immediate": "Testicular degeneration is the progressive loss of spermatogenic function in a previously fertile male, caused by heat stress, local trauma, systemic infections, or aging, leading to severe subfertility or sterility.",
            "Pathogenesis_Deep": "Degeneration begins with vacuolization of Sertoli cells and loss of the highly specialized blood-testis barrier. The primary and secondary spermatocytes undergo apoptotic pyknosis and desquamation into the tubular lumen. This leads to collapse of the seminiferous tubules, interstitial fibrosis, and replacement of spermatogenic tissue with fibrous scar tissue, macroscopically presenting as small, firm, calcified testes.",
            "Why_Not": "Testicular hypoplasia is a congenital, hereditary defect (commonly associated with the XXY karyotype in Swedish Red-and-White bulls) where the testes *never* developed normally. Testicular degeneration is an acquired pathology in a previously fertile bull.",
            "Wow_Approach": "Clinically, early degeneration is reversible if the primary cause (e.g., local scrotal inflammation, scabies, or fever) is treated. Provide at least 60-70 days of sexual rest to allow a new wave of spermatids to mature before conducting a repeat Breeding Soundness Evaluation."
        },
        285: {
            "subject": "Theriogenology",
            "topic": "Superfetation vs Superfecundation",
            "Core_Anatomy": "The gravid uterine horn, the functioning corpus luteum, the cervix, and the ovaries.",
            "Pathogenesis_Immediate": "Superfetation is the fertilization and development of a second oocyte when a fetus is already present in the uterus. Superfecundation is the fertilization of two or more oocytes from the same ovulation cycle by sperm from different matings/sires.",
            "Pathogenesis_Deep": "In superfetation, a pregnant animal must ovulate, the cervix must allow sperm transit despite a thick progesterone-induced mucus plug, and the second embryo must implant successfully beside the existing gravid horn. In superfecundation, the female ovulates multiple eggs during a single heat, and mates with different males, resulting in a multi-sired litter.",
            "Why_Not": "Superfecundation is highly common in litter-bearing animals (dogs, cats) that mate with multiple males during estrus. Superfetation is extremely rare and considered pathological in farm animals because progesterone from the existing CL normally suppresses GnRH, blocking ovulation.",
            "Wow_Approach": "Superfecundation is easily verified in dogs using DNA paternity testing of the litter. Superfetation in cows typically results in the birth of a full-term calf alongside a severely premature or aborted second fetus when parturition triggers luteolysis."
        },
        287: {
            "subject": "Theriogenology",
            "topic": "Superovulation and Embryo Transfer Technology (ETT)",
            "Core_Anatomy": "Ovarian follicular waves, the dominant follicle, the uterine horns, and the cervix.",
            "Pathogenesis_Immediate": "Superovulation is the administration of exogenous gonadotropins (FSH or eCG) to rescue antral follicles from atresia, inducing the development and ovulation of multiple dominant follicles in a high-genetic-value donor cow for subsequent non-surgical embryo recovery and transfer to recipients.",
            "Pathogenesis_Deep": "A donor cow is treated with twice-daily intramuscular injections of Follicle-Stimulating Hormone (FSH) for 4 days during the mid-luteal phase (days 9-12 of the cycle) to bypass dominant follicle selection. On the 3rd day of FSH, PGF2alpha is injected to regress the CL, inducing estrus. The donor is bred, and the multiple ovulated ova are fertilized. On Day 7 post-insemination, the blastocysts are recovered non-surgically using a Foley catheter to flush the uterine horns.",
            "Why_Not": "While eCG (equine Chorionic Gonadotropin) can also be used, its long half-life (days) causes persistent ovarian stimulation and abnormal follicular development. FSH has a short half-life (hours), providing highly controlled stimulation when administered twice daily.",
            "Wow_Approach": "Day 7 embryos are graded microscopically (Stage: morula/blastocyst; Quality: Grade 1, 2, 3) before being transferred directly into synchronized recipients (Day 7 post-estrus) using an embryo transfer gun, or cryopreserved in liquid nitrogen using ethylene glycol."
        },
        299: {
            "subject": "Theriogenology",
            "topic": "Fetal Mummification vs Fetal Maceration in Cows",
            "Core_Anatomy": "The gravid uterus, maternal cervix, and the uterine microenvironment.",
            "Pathogenesis_Immediate": "Fetal mummification is the death of the fetus during mid-gestation (3-8 months) in a sterile uterine environment with a closed cervix, leading to fluid absorption and the formation of a dry, leathery, bone-hard mass. Fetal maceration is fetal death accompanied by bacterial invasion through an open cervix, causing autolysis and liquefaction of soft tissues, leaving loose bones trapped in a purulent uterine cavity.",
            "Pathogenesis_Deep": "In mummification (commonly caused by BVDV, Leptospira, or genetic defects), the fetus dies, but the CL persists (no luteolysis). The closed cervix prevents bacterial contamination. The maternal uterine wall absorbs the amniotic and allantoic fluids, compressing the fetus into a dry, brown-black mass coated with hematic pigment (hematic mummification). In maceration, pyogenic bacteria enter the uterus, liquefying the fetus, while chronic endometritis thickens the uterine wall, permanently damaging the endometrium.",
            "Why_Not": "Mummification is a sterile process that preserves the future fertility of the cow once the mummy is expelled. Maceration is an inflammatory, septic process that causes severe, irreversible endometritis, rendering the cow permanently sterile.",
            "Wow_Approach": "Treat fetal mummification by administering a single intramuscular dose of PGF2alpha (Dinoprost or Cloprostenol). This regresses the persistent CL, dilates the cervix, and leads to the expulsive delivery of the mummy within 24 to 72 hours. Macerated cows have a hopeless prognosis and should be culled."
        },

        # BATCH 2: IDs 300 - 310
        300: {
            "subject": "Theriogenology",
            "topic": "Equine Chorionic Gonadotropin (eCG) / PMSG Biosynthesis",
            "Core_Anatomy": "Fetal chorionic girdle cells and maternal endometrial cups in the pregnant mare's uterine horns.",
            "Pathogenesis_Immediate": "Pregnant Mare Serum Gonadotropin (PMSG), now known as eCG, is secreted by transient endometrial cups between days 40 and 120 of equine gestation, acting to luteinize or ovulate secondary follicles to support early pregnancy.",
            "Pathogenesis_Deep": "Around Day 37 of gestation, specialized binucleate cells from the fetal chorionic girdle invade the maternal endometrium to form the endometrial cups. These cups secrete eCG, a highly glycosylated gonadotropin with a long half-life. eCG enters maternal circulation, exhibiting strong LH and FSH-like activities in non-equine species, but strictly luteotrophic/LH-like activity in mares, inducing accessory corpora lutea to maintain high progesterone.",
            "Why_Not": "In humans, hCG is produced by synctiotrophoblasts throughout gestation and exhibits strictly LH-like activity to support the primary CL. In mares, eCG is produced only temporarily by endometrial cups and has both LH and FSH-like activities in other species, but functions as a pure luteotrophic agent in the horse.",
            "Wow_Approach": "Endometrial cups have a fixed lifespan and are immunologically rejected and sloughed by Day 120, after which the placenta takes over progesterone synthesis. eCG is highly useful in synchronization protocols in sheep and cattle to stimulate follicular development due to its dual FSH/LH action."
        },
        301: {
            "subject": "Theriogenology",
            "topic": "Vibrionic Abortion (Campylobacteriosis) in Cattle",
            "Core_Anatomy": "Endometrium, cervical canal, and the fetal cotyledons of the placentome.",
            "Pathogenesis_Immediate": "Venereal transmission of *Campylobacter fetus subsp. venerealis* by infected bulls during coitus leads to subacute endometritis, fertilization failure, and early embryonic death (EED) or abortion in cows.",
            "Pathogenesis_Deep": "The bacteria colonize the vagina, cervix, and uterus. The local inflammatory response (neutrophilic and lymphocytic endometritis) creates a hostile environment that kills the developing blastocyst prior to maternal recognition of pregnancy, causing repeat breeding. In late-gestation, it infects the placentome, causing cotyledonary necrosis and expulsive abortion.",
            "Why_Not": "Unlike Trichomoniasis (caused by the protozoan *Tritrichomonas foetus*) which also causes EED and post-coital pyometra, Campylobacteriosis is a bacterial infection that rarely causes post-coital pyometra, presenting primarily as irregular estrus cycles and early abortions.",
            "Wow_Approach": "Eradicate venereal spread by using artificial insemination exclusively with semen treated with antibiotics (Dihydrostreptomycin). Annual vaccination of both bulls and cows with oil-adjuvant bacterins provides highly effective systemic and mucosal secretory IgA protection."
        },
        303: {
            "subject": "Theriogenology",
            "topic": "Gestation Length and Factors Affecting Pregnancy Duration in Cattle",
            "Core_Anatomy": "The feto-placental unit, maternal placentomes, and the maternal pelvic space.",
            "Pathogenesis_Immediate": "Gestation length in dairy cattle averages 280-285 days. Variations in gestation duration are influenced by fetal genotype (breed), sire, sex of the fetus (male calves are carried longer), and fetal number (twins have shorter gestation).",
            "Pathogenesis_Deep": "The timing of parturition is dictated by the maturation of the fetal hypothalamic-pituitary-adrenal (HPA) axis. When the fetus reaches developmental maturity, physical space limitations in the uterus trigger fetal stress, leading to cortisol release. Fetal cortisol alters placental steroidogenesis, initiating labor. If the HPA axis is delayed (e.g., in fetal anomalies or prolonged gestation), calving fails to initiate, leading to oversized fetuses.",
            "Why_Not": "In equines, gestation length is highly variable (330-345 days) and highly influenced by seasonal photoperiod. In bovines, gestation length is genetically highly conserved, and deviations exceeding 10 days typically indicate fetal pathology or impending dystocia.",
            "Wow_Approach": "Clinically, precise records of artificial insemination are crucial. If gestation exceeds 290 days, monitor the cow closely via transrectal palpation for fetal viability. Induce calving using Dexamethasone combined with Cloprostenol to prevent massive fetal oversize and dystocia."
        },
        304: {
            "subject": "Theriogenology",
            "topic": "Silent Estrus (Suboestrus) in Water Buffaloes",
            "Core_Anatomy": "Hypothalamic GnRH neurons, anterior pituitary gonadotrophs, and the uterine/cervical estrogen receptors.",
            "Pathogenesis_Immediate": "Failure of water buffaloes (*Bubalus bubalis*) to exhibit external signs of heat (standing behavior, vulvar swelling) despite normal follicular development and ovulation, leading to a high rate of missed inseminations.",
            "Pathogenesis_Deep": "Buffaloes have a highly sensitive hypothalamic-pituitary-ovarian axis. During warm, humid summer months (seasonal anestrus/suboestrus), high ambient heat triggers elevated plasma cortisol and prolactin. Cortisol suppresses LH pulse frequency. Although estrogen is produced by the dominant follicle to induce ovulation, its levels are insufficient to trigger behavioral centers in the brain, resulting in silent heat.",
            "Why_Not": "In cows, estrus signs are highly prominent, including mounting and standing behaviors. In buffaloes, standing estrus is rarely observed; heat detection relies on subtle signs like slight vulvar edema, clear mucus string, and frequent urination.",
            "Wow_Approach": "Overcome silent heat by using a teaser bull (which utilizes olfactory pheromones to detect suboestrus females) or implementing a scheduled timed artificial insemination protocol (like Ovsynch) combined with wallowing facilities to reduce summer thermal stress."
        },
        305: {
            "subject": "Theriogenology",
            "topic": "Progesterone Profile during the Bovine Estrus Cycle",
            "Core_Anatomy": "Ovarian luteal tissue (corpus luteum) and the systemic capillary network.",
            "Pathogenesis_Immediate": "Progesterone (P4) is the dominant hormone of the luteal phase (metestrus and diestrus), rising from near-zero post-ovulation to peak levels (>5 ng/ml) by Day 10, maintaining uterine quietness until luteolysis on Day 17.",
            "Pathogenesis_Deep": "Following ovulation, small and large luteal cells synthesize progesterone from cholesterol via the steroidogenic pathway (StAR protein, cytochrome P450scc, 3-beta-HSD). High progesterone exerts negative feedback on the hypothalamus, suppressing GnRH pulse frequency and preventing the pre-ovulatory LH surge. If pregnancy does not occur, PGF2a from the uterus regresses the CL, causing P4 to plunge by Day 19, allowing a new follicular wave to ovulate.",
            "Why_Not": "In non-pregnant bitches, the luteal phase (diestrus) persists for 60-70 days regardless of pregnancy status, showing a slow, natural decline in progesterone. In cows, the luteal phase is strictly regulated by uterine-derived PGF2a, returning the cow to cycle in 21 days if non-pregnant.",
            "Wow_Approach": "Progesterone monitoring is a powerful diagnostic tool. A plasma P4 level of >1 ng/ml confirms the presence of a functional CL, while a P4 level of <1 ng/ml on Day 21 post-AI is a 100% accurate indicator of non-pregnancy (early pregnancy diagnosis)."
        },
        306: {
            "subject": "Theriogenology",
            "topic": "Somatic Cell Nuclear Transfer (SCNT) and Animal Cloning",
            "Core_Anatomy": "Donor cell nucleus (somatic cell) and the recipient oocyte cytoplasm (enucleated MII oocyte).",
            "Pathogenesis_Immediate": "Somatic Cell Nuclear Transfer (SCNT) involves transferring a diploid nucleus from a donor somatic cell into an enucleated metaphase II (MII) oocyte, followed by artificial activation and embryo transfer, creating a genetic clone.",
            "Pathogenesis_Deep": "First, the genetic material of the recipient oocyte is removed (enucleation). The donor somatic cell (e.g., mammary epithelial cell, as in Dolly the sheep) is fused with the enucleated oocyte using electrical pulses. The fused cell is chemically activated (using ionomycin/DMAP) to mimic sperm fertilization, initiating embryonic cleavage and development into a blastocyst.",
            "Why_Not": "Natural fertilization involves the fusion of haploid gametes (sperm and egg) and immediate maternal-to-zygotic transition. SCNT requires the artificial reprogramming of a fully differentiated somatic cell nucleus back to a totipotent embryonic state, a process prone to epigenetic errors.",
            "Wow_Approach": "SCNT is highly inefficient (~1-5% success rate). Epigenetic failures lead to 'Large Offspring Syndrome' (LOS), characterized by placental abnormalities, fetal giantism, respiratory failure, and umbilical hernia. Enforcing precise donor cell starvation (inducing G0 quiescence) is critical to optimize nuclear reprogramming."
        },
        307: {
            "subject": "Theriogenology",
            "topic": "Epigenetic Reprogramming and Donor Cell Selection in SCNT",
            "Core_Anatomy": "Chromatin structure, histones, and DNA methylation pathways of the donor nucleus.",
            "Pathogenesis_Immediate": "The success of somatic cell cloning depends on complete chromatin remodeling and DNA methylation reprogramming of the donor diploid somatic nucleus by the recipient oocyte's cytoplasmic factors.",
            "Pathogenesis_Deep": "Differentiated somatic cells have highly restricted gene expression due to dense chromatin packing (heterochromatin) and extensive DNA methylation. Upon transfer, the oocyte's cytoplast must rapidly de-condense the donor chromatin, remove somatic-specific histone modifications (like H3K9me3), and demethylate developmental pluripotency genes (Oct4, Nanog) to allow embryo development.",
            "Why_Not": "Embryos produced via IVF undergo normal, programmed epigenetic clearing and maternal imprinting. SCNT embryos must accomplish this reprograming in a highly compressed timeframe without sperm-derived factors, leading to frequent transcription failures.",
            "Wow_Approach": "Select donor cells that are less differentiated (e.g., fetal fibroblasts or adult stem cells) and synchronize them into the G0 phase of the cell cycle by serum starvation. This chromatin configuration is highly receptive to the remodeling factors present in the oocyte cytoplasm."
        },
        308: {
            "subject": "Theriogenology",
            "topic": "Non-Permeable Cryoprotectants in Embryo/Semen Freezing",
            "Core_Anatomy": "The cell membrane (lipid bilayer) and the extracellular hydration shell of embryos/spermatozoa.",
            "Pathogenesis_Immediate": "Cryopreservation requires protecting cells from extracellular ice crystal damage. Non-permeating cryoprotective agents (like Sucrose, Trehalose, or Raffinose) do not cross the membrane; instead, they act extracellularly by drawing water out of the cell.",
            "Pathogenesis_Deep": "Non-permeating sugars increase the extracellular osmolarity, establishing an osmotic gradient that dehydrates the cell prior to freezing. This reduces intracellular water content, minimizing the substrate available for intracellular ice crystallization. Additionally, they interact with membrane phospholipids, stabilizing the liquid-crystalline phase during extreme cooling.",
            "Why_Not": "Permeable cryoprotectants (Glycerol, Ethylene Glycol) enter the cell to prevent internal ice formation and protect organelles. Non-permeable agents remain strictly in the extracellular fluid and are primarily used during vitrification (ultra-rapid freezing) and thawing/rehydration protocols to prevent osmotic shock.",
            "Wow_Approach": "In embryo vitrification, Sucrose is the absolute standard in the dilution/thawing media. It acts as an osmotic buffer, preventing the rapid, lethal influx of water into the embryo as the highly concentrated intracellular cryoprotectant is washed out."
        },
        309: {
            "subject": "Theriogenology",
            "topic": "Fincher's Test for Uterine Torsion in Buffaloes",
            "Core_Anatomy": "Vaginal canal, cervix, and the broad ligaments (mesometrium).",
            "Pathogenesis_Immediate": "Uterine torsion is a major cause of dystocia in water buffaloes. Fincher's test is a specialized transrectal/transvaginal palpation method used to determine the exact direction and degree of the uterine twist.",
            "Pathogenesis_Deep": "In a normal pregnant animal, the vaginal canal is straight, and the broad ligaments are felt rectally descending vertically on both sides of the uterus. In uterine torsion, rectal palpation reveals one broad ligament pulled tightly across the top of the uterus to the opposite side, while the other ligament descends vertically. Transvaginally, the vaginal wall is twisted into spiraling folds resembling a corkscrew, preventing access to the cervix.",
            "Why_Not": "Unlike standard rectal examinations for pregnancy diagnosis which focus on identifying the fetus or placentomes, Fincher's test focuses strictly on the spatial orientation of the broad ligaments and the vaginal spirals to plan the detorsion strategy.",
            "Wow_Approach": "In Fincher's test: if the right broad ligament is pulled tightly over the dorsal surface of the uterus to the left, it is a right-side (clockwise) torsion. Cast the buffalo on her right side and roll her to the right using Schaffer's method to correct the twist."
        },
        310: {
            "subject": "Theriogenology",
            "topic": "White Heifer Disease (Segmental Aplasia of Mullerian Ducts)",
            "Core_Anatomy": "The Mullerian (paramesonephric) duct derivatives: uterine horns, cervix, and anterior vagina.",
            "Pathogenesis_Immediate": "White Heifer Disease is a congenital, hereditary developmental defect in cattle characterized by segmental aplasia of the Mullerian ducts, leading to sterile, blind-ending uterine horns and fluid accumulation (mucometra/hydrometra).",
            "Pathogenesis_Deep": "During embryonic development, the Mullerian ducts must canalize and fuse to form the female reproductive tract. In affected animals (most commonly Shorthorn heifers with a white coat color, linked to a recessive gene), the canalization process fails segmentally. The ovaries develop normally (as they originate from the germinal ridge), but the uterus consists of isolated, blind pouches that accumulate endometrial secretions, preventing conception.",
            "Why_Not": "Unlike Freemartinism, which is a non-hereditary intersex condition caused by male hormones crossing through chorionic vascular fusion in twins, White Heifer Disease is a strictly genetic, hereditary structural malformation occurring in single-born heifers with normal female karyotypes.",
            "Wow_Approach": "Affected heifers display normal estrus cycles and are often presented as repeat breeders. Transrectal palpation reveals a fluid-distended, fluctuant uterine horn that can be mistaken for pregnancy; however, the absence of a corpus luteum, membrane slip, or placentomes confirms mucometra secondary to segmental aplasia. Cull affected animals."
        },

        # BATCH 3: IDs 311 - 323
        311: {
            "subject": "Theriogenology",
            "topic": "Anovulatory Estrus vs Silent Heat in Water Buffaloes",
            "Core_Anatomy": "The dominant Graafian follicle, granulosa cells, and the hypothalamic GnRH surge center.",
            "Pathogenesis_Immediate": "True silent estrus involves normal follicular development and ovulation without behavioral signs. In contrast, anovulatory estrus is characterized by behavioral signs of heat (estrus) but a complete failure of the follicle to rupture and release an oocyte.",
            "Pathogenesis_Deep": "Anovulatory estrus is common in heifers and during the transitional seasonal breeding phase in buffaloes. The dominant follicle secretes sufficient estrogen to trigger the behavioral estrus center in the brain, but due to hypothalamic fatigue or low LH stores, the pre-ovulatory LH surge is absent. The follicle fails to ovulate, either regressing or forming an anovulatory follicular cyst.",
            "Why_Not": "In silent heat, the cow is fertile but displays no behavior; insemination at the correct time leads to pregnancy. In anovulatory estrus, the cow displays clear heat behavior but is completely sterile for that cycle due to the absence of an oocyte.",
            "Wow_Approach": "Confirm ovulation by performing transrectal ultrasound 48 hours post-estrus to verify the disappearance of the dominant follicle and the subsequent formation of the corpus hemorrhagicum. Treat recurrent anovulatory cycles with GnRH at the start of estrus."
        },
        314: {
            "subject": "Theriogenology",
            "topic": "LH Deficiency and Ovarian Dysfunction in Water Buffaloes",
            "Core_Anatomy": "The anterior pituitary gland (gonadotrophic cells), hypothalamic GnRH neurons, and the dominant follicle.",
            "Pathogenesis_Immediate": "Deficiency in the secretion or pulsatility of Luteinizing Hormone (LH) in buffaloes prevents ovulation of the mature dominant follicle, leading to delayed ovulation, follicular cysts, or persistent anestrus.",
            "Pathogenesis_Deep": "LH secretion is regulated by pulsatile GnRH. Under thermal or nutritional stress (common in tropical buffaloes), elevated cortisol and ACTH block the GnRH pulse generator. This lowers the basal LH pulse frequency, which is essential for dominant follicle stimulation, and prevents the massive LH surge required to activate follicular wall proteolysis, arresting the follicle in a pre-ovulatory state.",
            "Why_Not": "FSH deficiency primarily halts early follicular recruitment and wave development, leading to completely static, inactive ovaries. LH deficiency allows the follicle to grow to a mature dominant stage but prevents its rupture or luteinization.",
            "Wow_Approach": "To bypass LH deficiency and induce ovulation in anestrus or delayed-ovulating buffaloes, administer 10-20 mcg of Buserelin (GnRH analog) or 1500-3000 IU of hCG. This directly triggers follicular rupture within 24-30 hours, improving timed-AI success."
        },
        319: {
            "subject": "Theriogenology",
            "topic": "Maternal Recognition of Pregnancy (MRP) in Pigs and Horses",
            "Core_Anatomy": "The fetal blastocyst membrane and the maternal endometrial epithelium.",
            "Pathogenesis_Immediate": "Each mammalian species has a unique maternal recognition of pregnancy (MRP) signal to prevent luteolysis. In swine, it is mediated by embryonic estrogen; in equines, it is mediated by physical embryonic migration.",
            "Pathogenesis_Deep": "In pigs, the blastocysts secrete estradiol-17-beta between days 11 and 12 of pregnancy. This estrogen redirects PGF2alpha secretion by the endometrium from an endocrine path (into the uterine veins) to an exocrine path (into the uterine lumen), where it is enzymatically inactivated, protecting the CL. At least two conceptuses per horn are required to prevent luteolysis. In horses, the unattached spherical embryo must physically migrate throughout both uterine horns 12-14 times a day to mechanically inhibit PGF2a release.",
            "Why_Not": "Ruminants use Interferon-tau (IFN-t) to biochemically silence endometrial oxytocin receptors. Swine use Estrogen to redirect PGF2a flow, and equines use mechanical migration to inhibit PGF2a synthesis, showcasing diverse evolutionary adaptations.",
            "Wow_Approach": "In pigs, if a sow has fewer than 4 embryos total (less than 2 per horn), the estrogen signal is insufficient to redirect PGF2a, resulting in luteolysis and early pregnancy loss. Enforce high fertilization rates in swine through precise multi-dose insemination."
        },
        320: {
            "subject": "Theriogenology",
            "topic": "Two-Cell Two-Gonadotropin Model of Ovarian Steroidogenesis",
            "Core_Anatomy": "The follicular theca interna cells, granulosa cells, and the basement membrane of the Graafian follicle.",
            "Pathogenesis_Immediate": "Estradiol synthesis by the Graafian follicle requires the cooperative action of two distinct cell types (theca and granulosa) and two gonadotropins (LH and FSH).",
            "Pathogenesis_Deep": "Theca interna cells bind LH, activating the cAMP pathway to convert cholesterol into androgens (androstenedione and testosterone). These lipophilic androgens diffuse across the follicular basement membrane into the granulosa cells. Granulosa cells bind FSH, activating the aromatase enzyme system which aromatizes the theca-derived androgens into estradiol-17-beta, the dominant hormone of estrus.",
            "Why_Not": "Theca cells lack the aromatase enzyme and cannot produce estrogen directly. Granulosa cells lack the enzymes (specifically 17-alpha-hydroxylase) to convert progesterone to androgens and must rely on theca cells for substrate, making the two-cell model mandatory.",
            "Wow_Approach": "During follicular cysts, this cooperative model is disrupted. Granulosa cells lose their FSH receptors and degenerate, while theca cells may undergo partial luteinization, shifting hormone production from estradiol to progesterone or abnormal androgens."
        },
        321: {
            "subject": "Theriogenology",
            "topic": "Interferon-tau Biosynthesis and Luteostatic Action in Ruminants",
            "Core_Anatomy": "The fetal trophectoderm and the maternal endometrial luminal epithelium.",
            "Pathogenesis_Immediate": "Interferon-tau (IFN-t) is a novel type I interferon secreted by the ruminant blastocyst during elongation (days 15-17 in cows) that acts as the maternal recognition signal to prevent luteolysis and maintain the CL.",
            "Pathogenesis_Deep": "Between Days 15 and 17 post-estrus, the conceptus elongates rapidly into a thread-like structure. Trophectoderm cells produce massive quantities of IFN-t. IFN-t binds to type I interferon receptors on the endometrial epithelium, suppressing the transcription of estrogen receptor-alpha (ER-a). Lacking ER-a, the endometrium cannot express oxytocin receptors (OTR). Without OTR, oxytocin cannot stimulate the pulsatile release of PGF2alpha, preserving the CL.",
            "Why_Not": "Unlike other type I interferons (like Interferon-alpha) which have high systemic antiviral toxicity, IFN-tau is strictly localized in the uterine lumen, exerting its luteostatic action without triggering maternal systemic immune or inflammatory responses.",
            "Wow_Approach": "Early embryonic death (EED) before Day 16 results in a failure of IFN-tau signaling. The maternal system fails to recognize the pregnancy, PGF2a is released, and the cow returns to heat. Maximizing early embryonic survival via post-breeding progesterone therapy is a key clinical strategy."
        },
        322: {
            "subject": "Theriogenology",
            "topic": "Buller Cow Syndrome (Nymphomania/Adrenal Virilism)",
            "Core_Anatomy": "The hypothalamic-pituitary-adrenal axis, ovarian cortex, and the external genitalia.",
            "Pathogenesis_Immediate": "Buller Cow Syndrome (Nymphomania) is a behavioral disorder in dairy cows characterized by persistent, abnormal estrus behavior, where the cow stands to be mounted constantly by other cows, leading to physical injury and exhaustion.",
            "Pathogenesis_Deep": "The condition is primarily caused by Cystic Ovarian Disease (follicular cysts) or chronic adrenal cortex hyperplasia (adrenal virilism). Follicular cysts secrete high, unregulated levels of estradiol. In adrenal virilism, the adrenal cortex secretes excessive androgens (testosterone and androstenedione). These hormones act continuously on the hypothalamic estrus center, abolishing the normal 21-day cycling and inducing constant sexual receptivity.",
            "Why_Not": "Normal estrus behavior is a transient event lasting 12-18 hours, triggered by a coordinated pre-ovulatory estrogen peak. Buller Cow Syndrome is a chronic, pathological state of hormonal dominance where negative feedback is lost, leading to permanent behavioral disruption.",
            "Wow_Approach": "Affected cows develop a masculine appearance, including a thick neck, raised tailhead, and deep voice ('steer-ish' behavior). Treat immediately with GnRH (to luteinize the ovarian cysts) or isolate the animal to prevent pelvic fractures and muscle trauma from constant mounting."
        },
        323: {
            "subject": "Theriogenology",
            "topic": "Pheromonal Primer Effects (Whitten, Bruce, and Ram Effects)",
            "Core_Anatomy": "The vomeronasal organ (VNO), accessory olfactory bulb, and the hypothalamic GnRH surge center.",
            "Pathogenesis_Immediate": "Pheromones are volatile chemical signals excreted in male urine/sebum that act on the female's olfactory system to synchronize estrus (Whitten effect), induce ovulation (Ram effect), or terminate pregnancy (Bruce effect).",
            "Pathogenesis_Deep": "In the Whitten effect (primarily studied in mice, but analogous to the buck/ram effect in small ruminants), exposing anestrus females to male pheromones (e.g., 6-methyl-5-hepten-2-one) stimulates receptors in the vomeronasal organ. Signals travel via the accessory olfactory bulb to the medial amygdala, stimulating pulsatile GnRH release from the hypothalamus. This triggers a synchronized wave of LH secretion, bringing the herd into estrus within 48-72 hours.",
            "Why_Not": "Visual or auditory cues from males can stimulate sexual interest, but only chemical pheromones acting on the vomeronasal organ can trigger the neuroendocrine cascade required to actively break seasonal anestrus or synchronize ovulation.",
            "Wow_Approach": "The 'Ram Effect' is a highly practical management tool in sheep husbandry. Introduce a vigorous ram to a flock of seasonally anestrus ewes that have been isolated from males for at least 3-4 weeks. This triggers sudden, highly synchronized ovulation in the ewes without exogenous hormones."
        },

        # BATCH 4: IDs 325 - 336
        325: {
            "subject": "Theriogenology",
            "topic": "Etiology and Predisposing Factors of Uterine Torsion in Ruminants",
            "Core_Anatomy": "Gravid uterus, mesometrium (broad ligaments), and the pelvic and abdominal cavities.",
            "Pathogenesis_Immediate": "Uterine torsion (rotation of the gravid uterus along its longitudinal axis) occurs primarily during the late first stage of labor, driven by unstable fetal movements, a lax mesometrium, and sudden maternal physical shifts.",
            "Pathogenesis_Deep": "During late gestation, the gravid bovine uterus lies primarily on the abdominal floor, unsupported by the pelvis. Predisposing anatomical factors include a long, lax mesometrium (highly pronounced in buffaloes) and a low volume of allantoic fluid. When the fetus begins active movement to assume the presentation posture at the start of labor, and the cow rolling or slipping suddenly, the uterus pivots around the cervix, twisting the vagina and blocking fetal exit.",
            "Why_Not": "In small ruminants (sheep/goats), uterine torsion is extremely rare because the gravid uterus is small, highly compact, and frequently carries multiple fetuses that wedge the uterus, preventing rotational torque. In large, deep-bellied dairy cows and buffaloes, the large single fetus acts as a pendulum, facilitating torsion.",
            "Wow_Approach": "Uterine torsion is a major veterinary emergency. Always check for uterine torsion in any cow or buffalo showing prolonged first-stage labor (straining without fetal presentation). Correct promptly using Schaffer's rolling plank method to avoid fetal death."
        },
        331: {
            "subject": "Theriogenology",
            "topic": "Semen Extenders and Diluent Formulation for AI",
            "Core_Anatomy": "The sperm plasma membrane, acrosomal enzymes, and the flagellar motor apparatus.",
            "Pathogenesis_Immediate": "Semen extenders are specialized liquid media added to collected ejaculates to preserve sperm viability, buffer toxic metabolic byproducts, and protect against cold shock during storage and freezing.",
            "Pathogenesis_Deep": "A highly functional extender must contain: 1. A buffer (Tris, Citrate, or Phosphate) to maintain optimal pH (6.7-6.9) and counteract lactic acid. 2. A cryoprotectant (Glycerol) to prevent ice crystallization. 3. Nutrients (Fructose or Glucose) for ATP production. 4. A membrane stabilizer (Egg yolk lipoprotein or milk lecithin) to protect against cold shock. 5. Antibiotics (Tylosin, Gentamicin) to control bacterial growth.",
            "Why_Not": "Standard saline or simple glucose solutions can temporarily dilute semen, but they lack buffering capacity and cryoprotectants. Diluting semen in saline leads to rapid osmotic swelling, membrane rupture, and complete loss of motility within hours.",
            "Wow_Approach": "Tris-buffered egg yolk glycerol extender is the global standard for bovine semen cryopreservation. Semen must be cooled slowly (equilibration phase at 4°C for 4 hours) to allow glycerol permeation and membrane lipid stabilization before plunging into liquid nitrogen."
        },
        332: {
            "subject": "Theriogenology",
            "topic": "Bovine Birth Canal Mechanics (Fetal Arc of Presentation)",
            "Core_Anatomy": "Maternal pelvic inlet, sacrosciatic ligaments, and the fetus in anterior presentation.",
            "Pathogenesis_Immediate": "During normal parturition in uniparous animals, the fetus must traverse the birth canal along an upward and outward curved path ('Arc of Presentation'), conforming to the shape of the maternal pelvic cavity.",
            "Pathogenesis_Deep": "The maternal pelvic canal is not a straight pipe; it has a dorsal curve dictated by the sacrum and a bony floor formed by the pubis and ischium. To pass successfully, the fetus must enter in anterior presentation, dorsal position, and extended posture. As the uterine contractions push the fetus, the head and forelimbs act as a wedge, dilating the cervix. The fetus must bend its neck and spine slightly, sliding along the curve of the pelvic inlet (arc form) to clear the vulva.",
            "Why_Not": "In multiparous animals (pigs/dogs), the fetuses are small and easily slide out without complex rotational alignment. In uniparous cattle, the fetopelvic ratio is highly tight; if the fetus enters in a rigid, straight line without conforming to the pelvic arc, it jams, causing obstructive dystocia.",
            "Wow_Approach": "When assisting a difficult calving, do not pull in a straight line. Apply traction downwards and outwards, mimicking the natural pelvic arc. Pulling horizontally or upwards jams the fetal pelvis against the maternal sacrum (hip-lock); pulling downwards clears the pelvic brim."
        },
        333: {
            "subject": "Theriogenology",
            "topic": "Pelvimetry and Pelvic Area Assessment in Heifers",
            "Core_Anatomy": "Bony pelvis (pubis, ilium, sacrum), vaginal vault, and the fetal head diameter.",
            "Pathogenesis_Immediate": "Fetopelvic disproportion is a major cause of dystocia, especially in heifers. Measuring the maternal pelvic area (pelvimetry) pre-breeding allows the selection of heifers with adequate birth canals to reduce dystocia.",
            "Pathogenesis_Deep": "Pelvimetry is conducted transrectally using a Rice Pelvimeter. Measure the vertical diameter (from the sacrum to the pubic symphysis) and horizontal diameter (widest distance between the shafts of the ilia). Calculate pelvic area (Vertical x Horizontal). Heifers with a pelvic area of <200 cm² at breeding have a 4-fold higher risk of severe dystocia when bred to standard bulls.",
            "Why_Not": "While choosing low-birth-weight bulls is the most common management tool, it is incomplete. If the maternal heifer has a congenitally narrow or stenotic pelvis (e.g., due to prior fracture or breed variation), she will experience dystocia even with small calves, making maternal pelvimetry crucial.",
            "Wow_Approach": "Screen replacement heifers at 12-13 months of age. Cull any heifer with a pelvic area below 140 cm² at yearling stage, and ensure selected heifers are bred to sires with highly rated Calving Ease (CE) EPDs."
        },
        334: {
            "subject": "Theriogenology",
            "topic": "Fetal Emphysema (Septic Putrefaction of Fetus) in Ruminants",
            "Core_Anatomy": "The gravid uterus, fetal subcutaneous tissues, and the maternal cervix.",
            "Pathogenesis_Immediate": "Fetal emphysema is the post-mortem bacterial putrefaction of a dead fetus retained in the uterus in the presence of an open cervix, characterized by severe gas accumulation in the fetal tissues and maternal toxemia.",
            "Pathogenesis_Deep": "Following fetal death during late gestation or delayed parturition, the cervix dilates slightly, allowing anaerobic gas-producing bacteria (primarily *Clostridium perfringens* and *Escherichia coli*) to ascend from the vagina into the uterus. These bacteria ferment fetal tissue proteins and glycogen, producing foul-smelling gas that distends the fetal subcutaneous tissues. This double-sized, crepitant fetus jams in the birth canal, while toxic bacterial byproducts are absorbed by the maternal endometrium, causing fatal maternal septicemia.",
            "Why_Not": "Fetal mummification is a sterile, closed-cervix process where fluids are absorbed, producing a dry, clean mummy. Fetal emphysema is a highly septic, open-cervix process characterized by gas accumulation, liquefactive necrosis, and severe maternal toxemia.",
            "Wow_Approach": "Fetal emphysema is a life-threatening veterinary emergency. Never attempt a C-section if the uterus is highly contaminated, as this leaks toxic fluids into the peritoneal cavity, causing fatal peritonitis. Perform a careful fetotomy to extract the gas-distended fetus, and treat the dam with aggressive systemic antibiotics and fluids."
        },
        335: {
            "subject": "Theriogenology",
            "topic": "Tocolytic Agents (Isoxsuprine) in Veterinary Obstetrics",
            "Core_Anatomy": "Myometrial smooth muscle cells and beta-2 adrenergic receptors.",
            "Pathogenesis_Immediate": "Tocolytics are pharmacological agents used to suppress myometrial contractions (uterine relaxants). In veterinary medicine, Isoxsuprine is the beta-2 adrenergic agonist of choice to temporarily arrest labor.",
            "Pathogenesis_Deep": "Isoxsuprine binds to beta-2 adrenergic receptors on the myometrial cell membranes. This activates adenylate cyclase, increasing intracellular cAMP. Elevated cAMP activates protein kinase A, which phosphorylates myosin light chain kinase (MLCK), inactivating it. Without active MLCK, myosin cannot bind to actin, arresting uterine contractions and causing complete myometrial relaxation.",
            "Why_Not": "Ecbolic drugs (like Oxytocin) stimulate uterine contractions by increasing intracellular calcium. Tocolytic drugs (like Isoxsuprine or Clenbuterol) relax the uterus by activating cAMP-mediated phosphorylation, serving as direct pharmacological opposites.",
            "Wow_Approach": "Isoxsuprine is highly useful during uterine torsion correction, surgical embryo transfer, or when correcting difficult fetal malpresentations. Relaxing the uterus prevents straining, providing the veterinarian with maximum space to manipulate the fetus safely."
        },
        336: {
            "subject": "Theriogenology",
            "topic": "Retained Fetal Membranes (Retained Placenta) in Cattle",
            "Core_Anatomy": "The placentome (consisting of maternal caruncle and fetal cotyledon) and the uterine caruncular crypts.",
            "Pathogenesis_Immediate": "Failure of the fetal membranes (placenta) to be expelled within 8-12 hours post-parturition, caused by a failure of cotyledonary-caruncular detent, leading to uterine infection and reduced future fertility.",
            "Pathogenesis_Deep": "Normally, post-calving, a sharp drop in progesterone combined with uterine contractions and local collagenase activity digests the cellular bridges (collagen fibers) connecting the fetal cotyledonary villi to the maternal caruncular crypts. In Retained Fetal Membranes (RFM), a lack of local matrix metalloproteinases, hypocalcemia (uterine inertia), or placentitis (due to Brucellosis) prevents this cellular dissociation, locking the placenta in place.",
            "Why_Not": "In mares, RFM is a hyper-acute medical emergency; if not expelled within 3 hours, bacterial endotoxins are absorbed, causing fatal laminitis and metritis. In cows, RFM is tolerated relatively well; the placenta slowly putrefies and sloughs over 7-10 days, presenting primarily as a hygiene and fertility risk.",
            "Wow_Approach": "Never manually pull or tear a retained placenta in cows, as this damages the caruncles and introduces bacteria deep into the endometrium. Manage conservatively by monitoring body temperature; administer systemic antibiotics (ceftiofur) only if the cow develops a fever (septic metritis)."
        },

        # BATCH 5: IDs 337 - 383
        337: {
            "subject": "Theriogenology",
            "topic": "Diffuse Microcotyledonary Placentation in the Mare",
            "Core_Anatomy": "The maternal endometrium and the fetal chorion of the equine placenta.",
            "Pathogenesis_Immediate": "The mare possesses a diffuse, microcotyledonary, epitheliochorial placenta, where placental attachment is spread uniformly across the entire uterine surface via microscopic structures called microcotyledons.",
            "Pathogenesis_Deep": "The outer surface of the equine chorion is covered by thousands of microscopic tufts of chorionic villi called microcotyledons. These villi fit precisely into corresponding microscopic crypts in the maternal endometrial epithelium. This diffuse arrangement provides a massive surface area for nutrient exchange, compensating for the thick, non-invasive epitheliochorial barrier (6 tissue layers separating maternal and fetal blood).",
            "Why_Not": "In ruminants, placentation is cotyledonary, restricted to 70-120 large placentomes. In dogs, it is zonary (a band around the middle of the chorionic sac). In the mare, it is diffuse; if any large segment of the endometrium is scarred (e.g., due to endometritis), the placenta cannot compensate, leading to fetal growth restriction or abortion.",
            "Wow_Approach": "Because the diffuse placenta must utilize almost the entire uterine surface to sustain a fetus, twin pregnancies are highly dangerous in mares. The two placentas compete for surface area, leading to placental insufficiency and the abortion of both fetuses in 90% of twin gestations. Always pinch out one embryonic vesicle if twins are detected via early ultrasound."
        },
        338: {
            "subject": "Theriogenology",
            "topic": "Rectovaginal Fistula and Third-Degree Perineal Laceration in the Mare",
            "Core_Anatomy": "The rectovaginal septum, the dorsal vaginal wall, the ventral rectal wall, and the perineal body.",
            "Pathogenesis_Immediate": "During dystocia in mares, a fetal foot (typically the forefoot) is forced upward, penetrating the dorsal vaginal wall and entering the rectum. If the foal is delivered with the foot in this position, it tears the rectovaginal septum, creating a permanent rectovaginal fistula.",
            "Pathogenesis_Deep": "If the tear extends completely through the external anal sphincter and vulva, it is classified as a Third-Degree Perineal Laceration, converting the rectum and vagina into a single, common opening (cloaca). This leads to constant fecal contamination of the vagina (pneumovagina and urovagina), causing severe, chronic endometritis and permanent sterility unless surgically corrected.",
            "Why_Not": "First-degree perineal lacerations involve only the mucosal lining of the vulva. Second-degree lacerations involve the muscular layers of the vulvar sphincter but do not tear the rectovaginal septum. Third-degree lacerations completely destroy the tissue boundary separating the gastrointestinal and reproductive tracts.",
            "Wow_Approach": "Surgical repair (using the Aanes or McKinnon technique) is highly successful but must *never* be attempted immediately post-injury. Wait 4 to 6 weeks to allow the intense inflammatory edema to subside and scar tissue to form. Keep the mare on a highly laxative diet (pasture/bran) to prevent hard feces from rupturing the surgical repair."
        },
        339: {
            "subject": "Theriogenology",
            "topic": "Hanging Drop Technique for Caudal Epidural Anesthesia in Cattle",
            "Core_Anatomy": "The epidural space, the ligamentum flavum, the coccygeal vertebrae (Co1-Co2 space), and the spinal cord canal.",
            "Pathogenesis_Immediate": "Caudal epidural anesthesia is utilized in large animals to anesthetize the perineum, vulva, and rectum to facilitate uterine detorsion, obstetrical manipulations, or repair of perineal tears. The 'hanging drop' technique confirms correct needle placement.",
            "Pathogenesis_Deep": "The epidural space possesses a sub-atmospheric (negative) pressure due to the bellows-like action of the dural sheath and abdominal movements. To perform the block, a needle is inserted through the Co1-Co2 intervertebral space. A drop of anesthetic solution is placed in the hub of the needle. As the needle penetrates the tough ligamentum flavum and enters the epidural space, the negative pressure sucks the drop of fluid down the needle shaft ('hanging drop' sign), confirming correct placement.",
            "Why_Not": "If the needle enters the subarachnoid space (spinal block), cerebral spinal fluid (CSF) will flow *outward* under positive pressure, pushing the drop out. The sucking inward of the drop is unique to the negative pressure of the epidural space.",
            "Wow_Approach": "Administer 5-10 ml of 2% Lignocaine epidurally. This provides complete desensitization of the vulva and anus within 10 minutes and halts straining (tenesmus) completely, while keeping the cow standing safely, as the motor nerves to the hindlegs (lumbar region) are unaffected."
        },
        340: {
            "subject": "Theriogenology",
            "topic": "Brucellosis (Contagious Bovine Abortion) and Placentitis",
            "Core_Anatomy": "The maternal caruncles, fetal cotyledons, and the trophoblast cells of the placenta.",
            "Pathogenesis_Immediate": "Ingestion of *Brucella abortus* bacteria leads to systemic infection, localization in the gravid uterus, and severe necrotic placentitis, causing contagious abortion in cattle during the third trimester (7-9 months).",
            "Pathogenesis_Deep": "*Brucella abortus* has a high affinity for erythritol, a sugar alcohol produced in high concentrations by the bovine placenta. The bacteria multiply inside the chorionic trophoblast cells, causing cell lysis and local vasculitis. This triggers extensive necrosis of the cotyledons and severe intercotyledonary edema, presenting macroscopically as a thickened, dry, 'leathery' placenta, starving the fetus and triggering premature expulsive labor.",
            "Why_Not": "While Trichomoniasis causes early embryonic death (EED) and post-coital pyometra in the first trimester, Brucellosis strictly targets the late-gestation placenta due to erythritol expression, presenting exclusively as late-term abortions and retained placenta.",
            "Wow_Approach": "Brucellosis is a highly dangerous, zoonotic disease causing Undulant Fever in humans. Enforce strict biosecurity: isolate aborting cows immediately, incinerate aborted fetuses and placenta, and immunize female calves between 4-8 months of age with the Brucella abortus Strain 19 or RB51 live vaccine."
        },
        362: {
            "subject": "Theriogenology",
            "topic": "Post-partum Endometritis and Metritis Complex in Dairy Cows",
            "Core_Anatomy": "The endometrium (mucosa), myometrium (muscularis), and perimetrium (serosa) of the uterine horns.",
            "Pathogenesis_Immediate": "Bacterial contamination of the uterus post-calving (most commonly by *Escherichia coli* followed by *Trueperella pyogenes*) causes severe metritis (involving all tissue layers) or endometritis (restricted to the mucosa), reducing pregnancy rates.",
            "Pathogenesis_Deep": "Post-calving, the cervix is dilated, and the uterine lumen contains lochia, creating a perfect culture medium. If the cow has low immunity (due to hypocalcemia or ketosis) or experienced dystocia, *E. coli* replicates rapidly, releasing endotoxins. *E. coli* infection damage allows *T. pyogenes* to colonize the endometrium later, releasing pyolysin (PLO) which destroys endometrial cells, leading to chronic purulent endometritis and repeat breeding.",
            "Why_Not": "Metritis is an acute, systemic disease occurring within 10 days post-calving, presenting with fever, foul-smelling red-brown discharge, and toxemia. Endometritis is a subacute/chronic localized mucosal disease occurring after 21 days, presenting without systemic signs, only purulent vaginal discharge.",
            "Wow_Approach": "Treat acute metritis with systemic antibiotics (Ceftiofur, which does not require milk discard) and supportive fluids. Treat chronic endometritis with intrauterine infusion of warm, dilute Lugol's iodine or administration of PGF2alpha to induce luteolysis, which flushes the uterus via estrus-mediated contractions."
        },
        363: {
            "subject": "Theriogenology",
            "topic": "Pyometra in Bitches (Cystic Endometrial Hyperplasia - Pyometra Complex)",
            "Core_Anatomy": "The endometrium, endometrial glands, myometrium, and the cervix of the bitch.",
            "Pathogenesis_Immediate": "Cystic Endometrial Hyperplasia (CEH) induced by prolonged progesterone exposure, followed by ascending bacterial infection (primarily *E. coli*), leads to massive accumulation of pus in the uterine horns, causing severe systemic toxemia.",
            "Pathogenesis_Deep": "Bitches have a prolonged luteal phase (60-70 days) dominated by progesterone. Progesterone stimulates endometrial gland hyperplasia and secretion, while suppressing myometrial contractions and closing the cervix. This fluid-filled uterus is highly susceptible to bacteria ascending from the vagina during estrus. *E. coli* colonizes the hyperplastic endometrium, and its endotoxins enter the circulation, causing systemic inflammatory response syndrome (SIRS).",
            "Why_Not": "In cows, pyometra is a localized uterine infection associated with a persistent CL, but it rarely causes systemic illness. In bitches, pyometra is a life-threatening, acute medical emergency due to the high sensitivity of the canine kidney to *E. coli* endotoxins, leading to glomerulonephritis and renal failure.",
            "Wow_Approach": "Bitches present with polydipsia, polyuria, purulent vaginal discharge (if open pyometra), and severe leukocytosis. The gold-standard treatment is immediate emergency Ovariohysterectomy (spay) combined with aggressive intravenous fluid therapy and bactericidal antibiotics."
        },
        364: {
            "subject": "Theriogenology",
            "topic": "Ovarian Hypoplasia in Cattle",
            "Core_Anatomy": "The ovarian cortex, primordial follicles, and the hypothalamic-pituitary-ovarian pathway.",
            "Pathogenesis_Immediate": "Ovarian hypoplasia is a congenital, hereditary developmental defect in heifers characterized by a complete or partial lack of primordial germ cells in the ovarian cortex, resulting in infantile ovaries, a lack of estrus cycles, and permanent sterility.",
            "Pathogenesis_Deep": "During embryonic migration, primordial germ cells fail to colonize the gonadal ridge. The ovary develops as a small, thin, flat 'streak' of fibrous tissue devoid of Graafian follicles or corpora lutea. The lack of ovarian estrogen prevents the normal development of the uterus, cervix, and secondary sex characteristics, leaving the heifer with an infantile reproductive tract.",
            "Why_Not": "Ovarian anestrus is an acquired physiological suppression of activity in normal, fully developed ovaries due to poor nutrition or NEB. Ovarian hypoplasia is a congenital structural absence of germ tissue; the ovaries can never be stimulated to produce follicles.",
            "Wow_Approach": "Ovarian hypoplasia is highly heritable (associated with a single autosomal recessive gene with incomplete penetrance in Swedish Red-and-White cattle). Clinically, transrectal palpation reveals tiny, hard, pea-sized ovaries without any structures. Affected heifers must be culled; never use their parents for breeding."
        },
        365: {
            "subject": "Theriogenology",
            "topic": "Persistent Corpus Luteum (Persistent CL) in Dairy Cows",
            "Core_Anatomy": "The corpus luteum on the ovary and the uterine endometrium.",
            "Pathogenesis_Immediate": "Failure of the non-pregnant uterus to secrete luteolytic PGF2alpha at the end of the estrus cycle extends the lifespan of the corpus luteum (persistent CL), locking the cow in anestrus.",
            "Pathogenesis_Deep": "Luteolysis requires pulsatile PGF2a release from a healthy, functional endometrium. If the endometrium is severely damaged (due to chronic pyometra, mucometra, or endometrial segment aplasia), or if there is a dead, mummified fetus in the uterus, the endometrial cells cannot synthesize or release PGF2a. Progesterone remains elevated, suppressing GnRH pulses and preventing the cow from returning to heat.",
            "Why_Not": "A normal CL regresses on Day 17 of the cycle. A persistent CL continues to produce high progesterone for months, presenting as a structural cause of anestrus, whereas nutritional anestrus involves inactive ovaries *without* any CL.",
            "Wow_Approach": "Confirm the diagnosis of a persistent CL via two ultrasound checks spaced 10 days apart showing the same luteal structure. Treat by administering a single intramuscular dose of PGF2alpha (Dinoprost or Cloprostenol), which regresses the CL and induces estrus within 72 hours."
        },
        366: {
            "subject": "Theriogenology",
            "topic": "Hydrosalpinx and Salpingitis in Cattle",
            "Core_Anatomy": "The fallopian tubes (oviducts; consisting of infundibulum, ampulla, and isthmus) and the mesosalpinx.",
            "Pathogenesis_Immediate": "Chronic ascending bacterial infection from the uterus leads to inflammation of the fallopian tubes (salpingitis). If the ends of the tube become occluded, the fluid accumulates, ballooning the tube (hydrosalpinx) and causing permanent sterility.",
            "Pathogenesis_Deep": "Pathogens (such as *Mycoplasma* spp., *T. pyogenes*, or *Ureaplasma*) ascend from a metritic uterus into the oviduct. The inflammatory response destroys the highly specialized ciliated epithelial cells that propel the oocyte. The tubal lumen becomes blocked by inflammatory debris. Endometrial/tubal secretions accumulate, distending the thin-walled tube into a fluid-filled, fluctuant structure, preventing sperm-oocyte transit.",
            "Why_Not": "Salpingitis is the active, cellular inflammatory stage of the oviduct. Hydrosalpinx is the chronic, non-inflammatory end-stage fluid distension resulting from prior tubal occlusion. Both prevent fertilization, but hydrosalpinx is structurally irreversible.",
            "Wow_Approach": "Salpingitis and early hydrosalpinx are diagnosed via transrectal palpation as thick, firm, coiled cords near the ovary, or via ultrasound. Bilateral hydrosalpinx carries a hopeless prognosis for breeding; affected cows are permanently sterile and should be culled."
        },
        375: {
            "subject": "Theriogenology",
            "topic": "Asymmetry of Ovarian Function in Cattle",
            "Core_Anatomy": "The left and right ovaries, the uterine horns, and the local vascular networks in cattle.",
            "Pathogenesis_Immediate": "In cattle, the right ovary is physiologically significantly more active than the left ovary, accounting for approximately 60% of all ovulations and subsequent pregnancies.",
            "Pathogenesis_Deep": "This physiological asymmetry is primarily anatomical. The right ovary has a superior vascular supply compared to the left, as the right ovarian artery is larger and has a more direct angle of origin from the aorta. Additionally, the rumen occupies the left side of the abdominal cavity, physically compressing and displacing the left ovary, slightly reducing local perfusion and follicular development compared to the right side.",
            "Why_Not": "In sheep and goats, ovarian function is symmetric, with both ovaries ovulating equally. In the mare, ovulation is also symmetric. In the queen and bitch, both ovaries function equally to support multi-fetal litters.",
            "Wow_Approach": "Clinically, when performing rectally guided artificial insemination or embryo transfer, always palpate both ovaries. Confirming a mature CL on the right ovary is a highly common finding, and transferring the embryo to the uterine horn ipsilateral to the CL (most commonly the right horn) is critical to optimize pregnancy rates."
        },
        376: {
            "subject": "Theriogenology",
            "topic": "Luteal Cavities and Cavitary CLs in Cows",
            "Core_Anatomy": "Ovarian corpus luteum and the central luteal cavity.",
            "Pathogenesis_Immediate": "Following ovulation, the central cavity of the developing corpus luteum may fail to fill completely with luteal tissue, leaving a fluid-filled center (cavitary CL) that is a normal, non-pathological variation.",
            "Pathogenesis_Deep": "During luteinization, the granulosa and theca cells migrate inward to fill the blood clot cavity (corpus hemorrhagicum). In about 30% of cycles, a central fluid cavity (>2mm in diameter) persists. Granulosa-derived large luteal cells line the outer wall of the cavity, synthesizing normal, high levels of progesterone. The fluid in the cavity contains high concentrations of progesterone and follicular proteins.",
            "Why_Not": "A luteal cyst is a pathological structure (>20mm in diameter) characterized by a thin layer of luteal tissue and a large fluid cavity, secreting high progesterone and causing persistent anestrus. A cavitary CL is normal in size (<20mm), cycles normally, and does *not* impair fertility.",
            "Wow_Approach": "Cavitary CLs are easily diagnosed via ultrasound as a hypoechoic circular area inside the hyperechoic luteal tissue. Do not mistake a cavitary CL for a pathological ovarian cyst; they require zero treatment and have normal conception rates."
        },
        378: {
            "subject": "Theriogenology",
            "topic": "Bovine Ovulation Physiology and Timing",
            "Core_Anatomy": "The mature Graafian follicle, the follicular apex (stigma), and the ovarian tunic.",
            "Pathogenesis_Immediate": "Unlike most domestic species, the cow ovulates post-estrus, approximately 10-12 hours *after* the behavioral signs of heat have ceased, demanding precise timing for successful insemination.",
            "Pathogenesis_Deep": "Ovulation is triggered by the LH surge (which occurs at the start of estrus). LH activates the local synthesis of progesterone and prostaglandins in the follicle. Prostaglandin F2alpha stimulates lysosomal enzymes to degrade the collagen matrix of the follicular wall at the stigma. Concurrently, smooth muscle cells in the ovarian tunic contract, gently forcing the oocyte-cumulus complex out of the ruptured follicle into the infundibulum.",
            "Why_Not": "Mares, sows, and ewes ovulate *during* active estrus. Cows ovulate *metestrus* (after estrus has ended). Inseminating a cow during active standing estrus ensures that sperm undergo the 4-6 hour capacitation process in the uterus and are ready in the oviduct when the egg is released 12 hours later.",
            "Wow_Approach": "This delayed ovulation physiology is the basis of the classic AM-PM Rule. Inseminating too early leads to sperm death before ovulation; inseminating too late (after the egg has aged) leads to fertilization failure."
        },
        380: {
            "subject": "Theriogenology",
            "topic": "Ovarian Anatomy and Folliculogenesis in the Sow",
            "Core_Anatomy": "Ovarian cortex, multiple dominant follicles, and multiple corpora lutea in the sow.",
            "Pathogenesis_Immediate": "The ovary of the sow is mulberry-shaped (lobulated) due to the simultaneous development of multiple large follicles or corpora lutea, reflecting her high prolificacy (litter-bearing nature).",
            "Pathogenesis_Deep": "Sows are polytocous (litter-bearing) animals, ovulating 15 to 25 oocytes per estrus cycle. During proestrus, a wave of multiple dominant follicles develops simultaneously, distending the ovarian surface. Post-ovulation, these follicles form multiple corpora lutea that resemble a bunch of grapes or a mulberry. This lobulated structure is essential to synthesize the massive progesterone levels required to sustain multiple developing fetuses.",
            "Why_Not": "In uniparous cattle and horses, the ovary is smooth, oval, or kidney-shaped, typically developing only a single dominant follicle or CL per cycle. The lobulated, grape-like ovary is unique to polytocous sows and bitches.",
            "Wow_Approach": "Sow fertility is measured by litter size. Optimizing nutrition during the pre-breeding phase (flushing: feeding high-energy diets for 10-14 days prior to breeding) maximizes the ovulation rate, increasing the number of active follicles on the mulberry-shaped ovary."
        },
        381: {
            "subject": "Theriogenology",
            "topic": "Silent Heat and Estrus Detection in Swine",
            "Core_Anatomy": "The hypothalamus, the olfactory bulb, and behavioral centers of the brain in the sow.",
            "Pathogenesis_Immediate": "Silent heat (anovulatory or ovulatory suboestrus) in swine leads to a complete failure of the sow to display the classic standing reflex, causing massive breeding delays.",
            "Pathogenesis_Deep": "Estrus detection in swine relies on the 'standing reflex' (immobilization response). When the sow is in heat, pressure applied to her back causes her to stand completely rigid with erect ears. This reflex is highly facilitated by the presence of a boar, specifically the pheromones (androstenone) present in his saliva. In silent heat (common under high ambient heat or group stress), cortisol suppresses the behavioral response, and the sow refuses to stand despite follicular maturation.",
            "Why_Not": "In cattle, estrus is detected by mounting behavior. In swine, estrus is detected strictly by the immobilization standing reflex under back pressure, which is highly dependent on boar pheromone priming.",
            "Wow_Approach": "To resolve silent heat in swine, always conduct heat checks twice daily in the direct presence of a mature, salivary-foaming boar. Apply firm back pressure and check for the rigid standing reflex. Use synthetic androstenone aerosol sprays if a live boar is unavailable."
        },
        382: {
            "subject": "Theriogenology",
            "topic": "Estrus Detection and Synchronization in Ewes",
            "Core_Anatomy": "Hypothalamic GnRH neurons, the pineal gland (melatonin pathway), and the vomeronasal organ.",
            "Pathogenesis_Immediate": "Ewes are seasonally polyestrus (short-day breeders). Estrus signs are extremely subtle and virtually impossible to detect visually without the presence of a teaser ram, requiring specialized synchronization and detection protocols.",
            "Pathogenesis_Deep": "As daylight shortens, the pineal gland increases melatonin secretion, which stimulates hypothalamic GnRH and initiates cycling. Ewes in heat do not mount other females; they merely stand quietly near the ram, wag their tails, and rub against him. In silent heat (common at the start of the breeding season), ovulation occurs without these subtle behavioral signs due to a lack of prior progesterone priming of the brain.",
            "Why_Not": "In dairy cattle, visual heat detection is highly effective. In sheep, visual heat detection is completely ineffective; rams use olfactory cues and pheromones to locate ewes in heat, making a teaser ram mandatory for detection.",
            "Wow_Approach": "Synchronize ewes during the breeding season using intravaginal progesterone-releasing sponges (CIDR) left in place for 12-14 days, followed by an injection of eCG (PMSG) at sponge withdrawal. Use a color-marked raddle harness on a vasectomized ram to identify synchronized ewes in heat."
        },
        383: {
            "subject": "Theriogenology",
            "topic": "Fecundity and Litter Size Optimization in Swine and Sheep",
            "Core_Anatomy": "The ovarian cortex, uterine endometrial capacity, and early embryonic survival pathways.",
            "Pathogenesis_Immediate": "Fecundity refers to the physiological capacity of a female to produce a large number of viable offspring (litter size), which is determined by ovulation rate, fertilization rate, and embryonic survival.",
            "Pathogenesis_Deep": "Litter size is regulated at three critical checkpoints: 1. Ovulation Rate: The number of oocytes released per cycle (maximized by high-energy 'flushing' nutrition). 2. Fertilization Rate: The percentage of eggs fertilized (maximized by precise timing of AI). 3. Embryonic Survival: The percentage of embryos that survive maternal recognition of pregnancy (maximized by avoiding crowding and providing optimal progesterone support).",
            "Why_Not": "Fertility is the simple qualitative ability to conceive and produce offspring. Fecundity is the quantitative measure of the *number* of offspring produced per birth, which is highly developed in polytocous species (swine, dogs) but highly restricted in uniparous ruminants.",
            "Wow_Approach": "In swine, embryonic mortality typically occurs between Days 12 and 18 post-breeding due to physical space limitations and uterine crowding in the horns. Enforce strict nutrient management post-breeding: feed *low* energy levels for the first 30 days of gestation to reduce progesterone clearance and optimize embryonic survival."
        }
    }
    
    # Process data and inject clinical fields
    updated_count = 0
    for q in data:
        qid = q.get("id")
        if qid in enrichment_data:
            q.update(enrichment_data[qid])
            updated_count += 1
            
    # Write back to database.js
    with open(db_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated Hybrid Exam Database\n")
        f.write("const examData = ")
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write(";\n")
        
    print(f"Direct Enrichment Complete: Updated {updated_count} high-yield questions directly in database.js.")

if __name__ == "__main__":
    run_direct_enrichment()
