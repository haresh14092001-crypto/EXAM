import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    812: {
        "topic": "Proestrual Bleeding - Feline vs Canine Vaginal Physiology",
        "Core_Anatomy": "Vaginal mucosal capillaries and the uterine endometrial vascular bed.",
        "Pathogenesis_Immediate": "Proestrual bleeding is a physiological feature characteristic of the Bitch (due to diapedesis of erythrocytes from endometrial capillaries under estrogen stimulation), but is absent in cows, mares, and queens.",
        "Pathogenesis_Deep": "During canine proestrus, rising estradiol from developing follicles causes intense hyperaemia and vascular engorgement of the endometrium. This is accompanied by an increase in capillary permeability and fragility, leading to diapedesis of red blood cells (RBCs) directly into the uterine lumen. The blood flows cranially through the cervix into the vagina and exits the vulva as a serosanguinous discharge. In contrast, cows exhibit metestrual bleeding (after estrus ends), and queens have no bleeding due to a highly tight mucosal barrier.",
        "Why_Not": "Metestrual bleeding occurs in cows *after* estrus (post-ovulatory), whereas proestrual bleeding in bitches occurs *before* estrus (pre-ovulatory). Queens do not bleed at any stage of their cycle, as their mucosal blood vessels are highly resistant to diapedesis.",
        "Wow_Approach": "To clinically differentiate canine proestrual bleeding from pathological hematuria or cystitis: perform a vaginal smear. Finding a high percentage of intermediate/superficial epithelial cells alongside RBCs confirms physiological proestrual discharge, whereas a high neutrophil and bacterial count indicates pathology."
    },
    821: {
        "topic": "Theriogenology Definitions - Capacitation, Decapacitation, and Acrosome Reaction",
        "Core_Anatomy": "Sperm cell membrane (plasma membrane), acrosomal membrane, and oviductal fluid.",
        "Pathogenesis_Immediate": "Key sperm biological milestones: Capacitation is the physiological priming of the sperm membrane in the female tract; Decapacitation is the stabilization of sperm membranes by seminal plasma proteins; Acrosome reaction is the fusion and vesiculation of the outer acrosomal membrane with the sperm plasma membrane.",
        "Pathogenesis_Deep": "These processes are obligatory for fertilization: (1) Ejaculated sperm are covered by decapacitation factors (seminal proteins) that stabilize the membrane. (2) In the uterus and oviduct, these factors are washed off, and cholesterol is removed from the sperm plasma membrane (Capacitation). This increases calcium permeability and hyperactivates motility. (3) When capacitated sperm bind the zona glycoprotein ZP3, it triggers the Acrosome Reaction. Calcium influx causes the outer acrosomal membrane to fuse with the overlying plasma membrane, releasing acrosin and hyaluronidase to digest a path through the zona.",
        "Why_Not": "Without capacitation, sperm cannot undergo the acrosome reaction, even if they physically contact the zona pellucida. The acrosome reaction is a one-time, irreversible exocytotic event; capacitation is a reversible priming phase.",
        "Wow_Approach": "In IVF, semen must be chemically capacitated in-vitro. This is achieved by washing sperm in media containing heparin or methyl-beta-cyclodextrin (which extracts cholesterol from the sperm membrane), simulating the uterine/oviductal fluid environment."
    },
    830: {
        "topic": "VGO-II Syllabus - Andrology, AI, and Veterinary Obstetrics",
        "Core_Anatomy": "Male reproductive tract, testis, epididymis, semen, and the birth canal.",
        "Pathogenesis_Immediate": "VGO-II focuses on Andrology (male reproduction), Semen Processing, Artificial Insemination (AI), Veterinary Obstetrics (parturition, dystocia), and Neonatology.",
        "Pathogenesis_Deep": "The curriculum covers: (1) Spermatogenesis kinetics, spermatogenic wave, and epididymal transit. (2) Semen collection, evaluation, and cryopreservation technologies. (3) The endocrinology of parturition, stages of labor, and maternal/fetal dystocia etiologies. (4) Obstetrical maneuvers (mutations, traction, fetotomy) and surgical interventions (caesarean section). (5) Neonatal resuscitation and colostrum management. This forms the clinical toolkit for high-yield food animal and equine practices.",
        "Why_Not": "Ovarian cycling, oestrus synchronization, repeat breeding, and non-gravid female reproductive tract pathologies are covered under VGO-I, leaving VGO-II focused on the male reproductive axis and the periparturient phase.",
        "Wow_Approach": "When reviewing VGO-II, treat Andrology and Obstetrics as complementary: Andrology ensures optimal fertility and semen quality to establish pregnancy, while Obstetrics ensures the safe, viable delivery of the genetic outcome at term."
    },
    831: {
        "topic": "VGO-II Course Overview - Male Fertility and Parturition",
        "Core_Anatomy": "Comparative male and female reproductive tracts.",
        "Pathogenesis_Immediate": "VGO-II provides the theoretical and practical framework for managing male breeding soundness, semen preservation, and obstetrical emergencies.",
        "Pathogenesis_Deep": "Key components involve: (1) Breeding Soundness Evaluation (BSE) in bulls and stallions (measuring scrotal circumference, libido, progressive motility, morphology). (2) Diluent formulation (tris-citric-egg yolk, skim milk) and cryoprotectants (glycerol). (3) Dystocia correction protocols (manipulation of head, neck, and limb flexions, fetotomy wire technique, and epidural anesthesia). (4) Retained Fetal Membranes (RFM) and uterine prolapse therapeutics.",
        "Why_Not": "The study of silent heat, cystic ovaries, and early embryonic death is the domain of VGO-I, whereas VGO-II begins at the level of the mature male gamete and the late-stage gravid female.",
        "Wow_Approach": "In the obstetrical clinic, always apply the 'rule of two: check for the presence of two joints (fetlock and carpus/hock) and ensure they flex in the correct direction to distinguish anterior (forelimb) from posterior (hindlimb) presentation before applying traction."
    },
    833: {
        "topic": "VGO-II Objective Section - Andrology and Obstetrics Focus",
        "Core_Anatomy": "Testicular parenchyma, epididymis, and maternal pelvic canal.",
        "Pathogenesis_Immediate": "The objective section of VGO-II tests precise numerical parameters: duration of spermatogenesis, epididymal transit time, sperm production rates, and standard obstetrical coordinates.",
        "Pathogenesis_Deep": "Key parameters include: (1) Sperm production rates: ~10,000 sperm per second in mammals. (2) Spermatogenesis duration: bull = 61 days, ram = 49 days, boar = 34 days, stallion = 57 days. (3) Epididymal transit: 9-14 days in bulls. (4) Normal fetal presentations (anterior longitudinal, dorso-sacral, head and forelimbs extended). Accurate recall of these numbers is tested to build diagnostic precision.",
        "Why_Not": "Subjective essays evaluate surgical technique (e.g., how to perform a caesarean), while the objective section focuses strictly on these precise biological constants.",
        "Wow_Approach": "Create a comparative table of male spermatogenic parameters (duration of cycle, total spermatogenesis length, and daily sperm production per gram of testis) for bull, ram, stallion, and boar for quick reference."
    },
    834: {
        "topic": "Objective Andrology - Sperm Production and Maturation Kinetics",
        "Core_Anatomy": "Seminiferous tubules, Leydig cells, and epididymal duct.",
        "Pathogenesis_Immediate": "The objective portion of Andrology tests biological constants: the site of sperm maturation (epididymis), the hormone stimulating Leydig cells (LH), and the cellular site of blood-testis barrier (Sertoli cell tight junctions).",
        "Pathogenesis_Deep": "Important concepts: (1) The Blood-Testis Barrier (BTB) is formed by tight junctions between Sertoli cells, dividing the seminiferous epithelium into basal and adluminal compartments to protect immunogenic haploid spermatids from the host immune system. (2) Sperm acquire progressive motility and fertilizing capacity during their transit through the corpus and cauda epididymis. (3) Daily Sperm Production (DSP) is highly correlated with scrotal circumference and testicular weight.",
        "Why_Not": "The accessory sex glands (prostate, seminal vesicles) produce seminal plasma to transport sperm, but do not contribute to sperm production or maturation kinetics, which are strictly testicular and epididymal processes.",
        "Wow_Approach": "Scrotal circumference is the single most important physical indicator of fertility in young bulls. A scrotal circumference <30 cm at 12 months of age is a direct indicator of small testicular mass and poor daily sperm production, warranting culling."
    },
    835: {
        "topic": "Rate of Sperm Production - Mammalian Testicular Capacity",
        "Core_Anatomy": "Testicular parenchyma, seminiferous epithelium, and germ cells.",
        "Pathogenesis_Immediate": "The rate of sperm production in mammals is exceptionally high, averaging approximately 10,000 spermatozoa per second (range of 5,000-15,000/sec depending on species and testicular mass).",
        "Pathogenesis_Deep": "Mammalian spermatogenesis is a continuous, highly productive process. In the seminiferous tubules, spermatogonia undergo continuous mitotic divisions to replenish the stem cell pool and produce primary spermatocytes. This is followed by meiosis and spermiogenesis. A mature bull with 500 g of testicular parenchyma produces ~5-6 billion sperm per day (which translates to ~60,000 sperm/second). This continuous high production is required to support the massive numbers of sperm required per ejaculate (typically 4-8 billion in bulls) to overcome maternal tract defenses.",
        "Why_Not": "A rate of 1,000/sec is too low to sustain the massive daily sperm output of domestic livestock. A rate of 35,000/sec is an overestimate for average mammals but can be achieved in hyper-fertile boars with exceptionally large testes (>800 g).",
        "Wow_Approach": "Boars have the highest daily sperm production among domestic animals, producing ~15-20 billion sperm per day, which is why a single boar ejaculate contains 200-500 ml of fluid containing 50-100 billion sperm."
    },
    836: {
        "topic": "Duration of Spermatogenesis in the Bull - 61 Days",
        "Core_Anatomy": "Seminiferous tubules, type A spermatogonia, and mature spermatids.",
        "Pathogenesis_Immediate": "The complete duration of spermatogenesis (from type A spermatogonium division to the release of mature spermatozoa into the lumen) in the bull is 61 days (approximately 8.5 weeks).",
        "Pathogenesis_Deep": "Spermatogenesis is a highly coordinated, species-specific process: (1) It consists of four complete cycles of the seminiferous epithelium, with each cycle lasting 13.5 days in the bull (13.5 × 4.5 cycles = ~61 days). (2) Stage I: Mitotic proliferation (spermatocytogenesis) to produce spermatocytes (~21 days). (3) Stage II: Meiosis I and II to produce haploid round spermatids (~21 days). (4) Stage III: Spermiogenesis (cellular remodeling: flagellum formation, nuclear condensation, acrosome cap formation) to produce elongated spermatozoa (~19 days). Any toxic insult or heat stress to the testis will present as poor semen quality exactly 6-8 weeks later.",
        "Why_Not": "Spermatogenesis takes 49 days in the ram, 34 days in the boar, and 57 days in the stallion. The 61-day duration is a specific, heavily tested biological constant for the bull (Bos taurus).",
        "Wow_Approach": "Clinical correlation: If a breeding bull suffers from a high fever (e.g., due to Ephemeral Fever or Foot-and-Mouth disease) on Day 0, the heat will damage the developing spermatids. The resulting poor semen quality (high morphologic abnormalities, low motility) will appear in the ejaculate 60 days later and persist for another 30-40 days."
    },
    837: {
        "topic": "Epididymal Transit - 9-14 Day Sperm Maturation and Transport",
        "Core_Anatomy": "Caput epididymis (head), corpus epididymis (body), and cauda epididymis (tail).",
        "Pathogenesis_Immediate": "The transport of spermatozoa through the epididymis in the bull requires 9 to 14 days, during which the sperm undergo essential maturation processes.",
        "Pathogenesis_Deep": "When sperm are released from the seminiferous tubules (spermiation), they are immotile and incapable of fertilization. They travel through the efferent ducts into the epididymis: (1) Caput (head): fluid absorption concentrates the sperm. (2) Corpus (body): sperm undergo biochemical changes, including membrane lipid modification and glycoprotein coating. They acquire the capacity for progressive motility. (3) Cauda (tail): serves as the primary storage site for mature, fertile sperm. The transit through these segments takes 9-14 days, regulated by regular contractions of the epididymal smooth muscle.",
        "Why_Not": "A 1-2 day transit is too rapid, as sperm would be expelled while still immature and infertile. A 20-30 day transit is typical of sexual exhaustion or low emission rates, but is not the normal physiological transit range.",
        "Wow_Approach": "Sperm stored in the cauda epididymis are kept in a quiescent, highly concentrated state due to low pH (6.5), high potassium levels, and low oxygen. Upon ejaculation, they mix with alkaline fluids from the accessory sex glands, which activates their motility."
    },
    838: {
        "topic": "Spermatogenesis Genetic Diversity - Meiosis I Crossing Over",
        "Core_Anatomy": "Primary spermatocytes, sister chromatids, and the synaptonemal complex.",
        "Pathogenesis_Immediate": "During spermatogenesis, genetic diversity of the spermatozoa is guaranteed during the Meiotic Division I (specifically during the prophase I stage of meiosis).",
        "Pathogenesis_Deep": "Genetic diversity is achieved via two key meiotic mechanisms: (1) Crossing Over (homologous recombination): during the pachytene stage of prophase I, homologous maternal and paternal chromosomes pair up (synapsis) and exchange segments of DNA. This creates completely unique recombinant chromatids. (2) Independent Assortment: during metaphase I and anaphase I, the maternal and paternal chromosomes align and segregate randomly into the secondary spermatocytes. This ensures that every single spermatozoon carries a unique genetic combination.",
        "Why_Not": "The mitotic phase involves simple clonal expansion of type A spermatogonia, ensuring genetic identity. The differentiation phase (spermiogenesis) is strictly morphological remodeling (no cell division or DNA replication occurs).",
        "Wow_Approach": "Because crossing over occurs during the prolonged prophase I (specifically in pachytene), primary spermatocytes are highly sensitive to mutagens, radiation, and heat stress during this phase, which can disrupt chromosome synapsis and lead to chromosomal aberrations in the sperm."
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
