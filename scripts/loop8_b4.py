import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    884: {
        "topic": "VGO-511 Andrology Course Syllabus - Key Reproductive Parameters",
        "Core_Anatomy": "Male HPG axis, testes, epididymis, accessory sex glands, and semen.",
        "Pathogenesis_Immediate": "VGO-511 covers the biology of male reproduction, clinical semen evaluation, cryopreservation technology, and diagnostic breeding soundness evaluations.",
        "Pathogenesis_Deep": "The syllabus details the mechanisms of spermatogenesis, hormonal regulation of testosterone, accessory sex gland secretions, semen diluent chemical functions, and liquid nitrogen cryopreservation mechanics. It builds clinical skills for identifying male infertility (e.g., orchitis, epididymitis, BPH, preputial vices) and managing artificial insemination centers.",
        "Why_Not": "Obstetrical maneuvers, fetal dystocias, and postpartum female pathologies are covered in other courses, keeping VGO-511 focused exclusively on the male reproducer and processing technology.",
        "Wow_Approach": "To ensure maximum academic readiness: integrate physical exam findings (testicular palpation, scrotal circumference) with precise physiological constants (spermatogenic wave duration) to formulate accurate diagnoses."
    },
    897: {
        "topic": "Leydig Cells - Testosterone Secretion and LH Stimulation",
        "Core_Anatomy": "Testicular interstitium, Leydig cells, LH receptors, and mitochondria.",
        "Pathogenesis_Immediate": "The primary male sex hormone, testosterone, is synthesized and secreted by the interstitial Leydig cells (interstitial cells of Leydig) under the direct stimulation of Luteinizing Hormone (LH).",
        "Pathogenesis_Deep": "Leydig cells are located in the connective tissue interstitium between the seminiferous tubules: (1) LH from the anterior pituitary binds G-protein coupled LH receptors on the Leydig cell membrane. (2) This activates adenylate cyclase, increasing intracellular cAMP. (3) cAMP stimulates the StAR (steroidogenic acute regulatory) protein to transport cholesterol across the mitochondrial membranes. (4) Cholesterol is converted to pregnenolone, which is then converted to testosterone in the smooth endoplasmic reticulum. Testosterone is essential for spermatogenesis, accessory gland function, and male libido.",
        "Why_Not": "Sertoli cells are located inside the seminiferous tubules and respond to FSH, producing androgen-binding protein (ABP) and inhibin, but not testosterone. Myoid cells are contractile cells that form the tubular wall.",
        "Wow_Approach": "Because testosterone is lipid-soluble, it cannot be stored in vesicles. Leydig cells must synthesize it de novo in response to pulsatile LH releases. This results in highly pulsatile systemic testosterone levels, peaking 3-5 times daily in mature bulls."
    },
    898: {
        "topic": "Gonitis - Stifle Joint Inflammation in Breeding Bulls",
        "Core_Anatomy": "Stifle joint (femorotibial and femoropatellar joints), cruciate ligaments, and joint capsule.",
        "Pathogenesis_Immediate": "Gonitis is the clinical term denoting the distention, inflammation, and enlargement of the joint capsule of the Stifle joint, which is a major cause of mounting failure in breeding bulls.",
        "Pathogenesis_Deep": "The stifle joint is the largest and most complex joint in the hindlimb, corresponding to the human knee. Gonitis in bulls often arises due to: (1) Trauma or sprain during mounting (sudden twisting or slipping). (2) Degenerative joint disease (osteoarthritis) in heavy, older bulls. (3) Infectious arthritis (Mycoplasma, Brucella). The inflammation causes severe pain, distention of the femoropatellar joint capsule (visible as a fluctuant swelling on the cranial aspect of the stifle), and mechanical lameness. Affected bulls cannot bear weight on their hindlimbs, preventing them from mounting females or artificial vaginas.",
        "Why_Not": "Gonitis does not involve the knee joint (which corresponds to the carpus in animals) or the hip joint (coxofemoral joint). It is strictly and pathognomonically localized to the stifle joint.",
        "Wow_Approach": "To clinically verify gonitis in a lame bull: perform palpation of the stifle joint capsule. If distended, perform arthrocentesis. Finding turbid joint fluid with highly elevated protein (>4.5 g/dL) and abundant neutrophils confirms active gonitis, requiring sexual rest and intra-articular NSAID therapy."
    },
    899: {
        "topic": "Sperm Abnormalities - Primary Defects Arising in the Testes",
        "Core_Anatomy": "Seminiferous tubules, germ cells (spermatogonia, spermatids), and the blood-testis barrier.",
        "Pathogenesis_Immediate": "Primary sperm abnormalities (morphological defects like double heads, pyriform heads, microcephalic heads, or tight coiled tails) arise exclusively during active spermatogenesis in the Testes.",
        "Pathogenesis_Deep": "Sperm defects are classified by their site of origin: (1) Primary abnormalities: arise due to disturbances in spermiogenesis or meiosis within the seminiferous epithelium of the testes (e.g., severe nuclear or head shapes, structural axonemal deletions). They represent true testicular dysfunction. (2) Secondary abnormalities: arise during transit or maturation in the epididymis (e.g., detached heads, distal cytoplasmic droplets, simple bent tails). (3) Tertiary abnormalities: arise due to poor handling, cold shock, or osmotic stress post-ejaculation (e.g., coiled tails in hypotonic media).",
        "Why_Not": "The epididymis and vas deferens are transit ducts where secondary maturation and transport occur; they do not generate primary nuclear or head shape abnormalities, which are determined during chromatin condensation in the testis.",
        "Wow_Approach": "If a bull has >15-20% primary sperm abnormalities (e.g., pyriform heads): it indicates chronic testicular degeneration or severe heat stress. Because these defects arise in the testes, the bull will require a minimum of 60 days (one complete spermatogenic cycle) of sexual rest to show any potential improvement in semen quality."
    },
    900: {
        "topic": "Bull Semen Evaluation - Minimum Volume and Concentration",
        "Core_Anatomy": "Testicular output, epididymal reserve, and accessory sex gland fluid.",
        "Pathogenesis_Immediate": "The minimum physiological volume and sperm concentration required to process an ejaculate for commercial deep-freezing in dairy bulls is a volume of 2.5 to 3.0 ml and a concentration of 500 million/ml.",
        "Pathogenesis_Deep": "For an ejaculate to be economically and biologically viable for cryopreservation, it must meet standard QA thresholds: (1) Volume: must be at least 2.5 ml. An abnormally low volume indicates incomplete ejaculation or accessory gland dysfunction. (2) Concentration: must be at least 500 million sperm per ml (measured by spectrophotometer or hemocytometer). This ensures that after the massive dilution required (typically 1:10 to 1:20 to achieve 20 million sperm per 0.25 ml straw), the extender retains sufficient cryoprotective properties and the post-thaw dose is highly fertile.",
        "Why_Not": "A 10 ml volume with 1,200 million concentration is an excellent, premium ejaculate, but is not the minimum processing threshold. A 3 ml volume with only 100 million concentration is too dilute and cannot be processed for deep-freezing, as the dilution factor would be too low to allow proper cryoprotection.",
        "Wow_Approach": "If a valuable bull consistently produces low-concentration ejaculates: implement a pre-collection preparation protocol (two false mounts + 1 minute restraint). This stimulates oxytocin release, which triggers contractions of the epididymal tail and vas deferens, increasing the sperm concentration by up to 50%."
    },
    901: {
        "topic": "Bovine Semen Processing - Minimal Quality Thresholds (Repeated MCQ)",
        "Core_Anatomy": "Bull ejaculatory tract and processing laboratory.",
        "Pathogenesis_Immediate": "Standard commercial AI centers require a minimum raw ejaculate volume of 2.5 ml and a concentration of 500 million/ml to justify the dilution and freezing protocol.",
        "Pathogenesis_Deep": "Processing semen is highly resource-intensive. Diluting an ejaculate that falls below the 500 million/ml threshold is economically unviable because it yields too few straws per batch. Biologically, low-concentration ejaculates often contain a higher percentage of abnormal sperm and are highly susceptible to lipid peroxidation due to a lack of protective seminal plasma proteins.",
        "Why_Not": "Processing highly dilute semen (e.g., 100 million/ml) results in poor post-thaw progressive motility because the low density of sperm cells increases their vulnerability to ice crystal damage during the rapid freezing process.",
        "Wow_Approach": "To ensure maximum quality, the AI center uses a CASA system to verify that the raw semen also has a minimum of 70% progressive motility and less than 15% total morphological abnormalities before processing."
    },
    902: {
        "topic": "Buck Seminal Plasma - Bulbourethral Gland Egg Yolk Coagulating Enzyme",
        "Core_Anatomy": "Caprine bulbourethral (Cowper's) glands, urethral lumen, and semen.",
        "Pathogenesis_Immediate": "The Bulbourethral (Cowper's) gland in the Buck (male goat) secretes a specific enzyme into the seminal plasma that causes severe coagulation and toxicity when egg yolk-based extenders are added.",
        "Pathogenesis_Deep": "The caprine bulbourethral gland secretes a glycoprotein enzyme called Egg Yolk Coagulating Enzyme (EYCE), which has phospholipase A2 activity. When buck semen is diluted with traditional egg yolk-buffered extenders: (1) EYCE hydrolyzes the lecithin (phosphatidylcholine) present in egg yolk. (2) This hydrolysis reaction produces fatty acids and lysolecithin. (3) Lysolecithin is highly toxic to spermatozoa, causing immediate disruption of the plasma membrane, loss of motility, and cell death. For this reason, buck semen must be handled differently than bull semen.",
        "Why_Not": "The prostate gland, seminal vesicles, and ampullary glands do not secrete EYCE. While the seminal vesicles secrete other proteins, the bulbourethral gland is the sole source of this specific egg yolk-toxic coagulant.",
        "Wow_Approach": "To successfully freeze buck semen: either wash the spermatozoa (centrifuge at 600g for 10 minutes in PBS to remove the seminal plasma containing EYCE before diluting with egg yolk extender), or use egg yolk-free extenders based on skim milk or chemically defined soybean lecithin (e.g., Bioxcell)."
    },
    903: {
        "topic": "EYCE Phospholipase A2 - Caprine Bulbourethral Secretion (Repeated MCQ)",
        "Core_Anatomy": "Bulbourethral gland secretory epithelium and the sperm membrane.",
        "Pathogenesis_Immediate": "The specific enzyme responsible for coagulating egg yolk in buck semen diluents is Egg Yolk Coagulating Enzyme (EYCE), a phospholipase A2 secreted by the bulbourethral (Cowper's) glands.",
        "Pathogenesis_Deep": "EYCE's phospholipase action targets the outer lipid bilayer of the sperm membrane. The resulting byproduct, lysolecithin, acts as a potent detergent that solubilizes the membrane lipids. This leads to: rapid calcium influx, loss of mitochondrial membrane potential, and immediate asthenozoospermia. This caprine-specific incompatibility requires either semen washing or alternative extender formulations.",
        "Why_Not": "Citric acid, fructose, and ergothioneine are normal, non-toxic components of seminal plasma that support sperm viability, and do not cause egg yolk coagulation or toxicity.",
        "Wow_Approach": "Skim milk extenders work exceptionally well for bucks because milk proteins (specifically casein micelles) bind and inactivate small amounts of EYCE, preventing the enzymatic reaction and protecting the sperm without the need for centrifugation."
    },
    904: {
        "topic": "Semen Cryopreservation - Vapor Freezing Grill Distance",
        "Core_Anatomy": "Semen straws, liquid nitrogen level, and the vapor freezing compartment.",
        "Pathogenesis_Immediate": "During the deep-freezing of semen straws in liquid nitrogen vapor, the optimal distance between the liquid nitrogen level (grill) and the straw rack is 4 cm (or approximately 1.5 to 2 inches).",
        "Pathogenesis_Deep": "Semen cryopreservation relies on a precise cooling curve: (1) Straws must be cooled from 4°C to -130°C in the vapor phase before direct immersion into the liquid nitrogen (-196°C). (2) At 4 cm above the liquid level, the nitrogen vapor temperature is consistently between -80°C and -120°C. (3) Placing the straws on the rack at this exact height for 7-10 minutes achieves a rapid, uniform cooling rate of approximately -10°C to -20°C per minute. This rate is critical to allow cellular water to escape, preventing intracellular ice crystallization while minimizing osmotic shock.",
        "Why_Not": "Placing straws at 10 cm above the liquid is too warm, leading to a slow cooling rate that causes severe osmotic cell damage (solution effect). Placing straws directly on the liquid level (<1 cm) causes instantaneous, uneven freezing, trapping water inside and rupturing the sperm membranes.",
        "Wow_Approach": "To verify the vapor phase temperature: place a digital thermocouple on the freezing rack. When the liquid nitrogen level is stable and the rack is at 4 cm, the sensor should register exactly -120°C. Expose the straws for 9 minutes, then plunge them rapidly into the liquid nitrogen."
    },
    905: {
        "topic": "Accessory Sex Glands - Canine Lack of Seminal Vesicles",
        "Core_Anatomy": "Male reproductive tract, pelvic urethra, prostate gland, and seminal vesicles (vesicular glands).",
        "Pathogenesis_Immediate": "The Seminal Vesicles (vesicular glands) are completely absent in the Dog (bitch/male dog) and Cat, where the prostate gland is the sole functional accessory sex gland.",
        "Pathogenesis_Deep": "Accessory sex gland anatomy varies significantly among domestic males: (1) Bulls, stallions, and boars have a complete set of glands: ampullary glands, seminal vesicles, prostate, and bulbourethral glands. (2) Goats and rams also have all four glands. (3) Dogs only possess a highly developed Prostate Gland that encircles the pelvic urethra; they have no seminal vesicles or bulbourethral glands. (4) Cats have a prostate and bulbourethral glands, but no seminal vesicles. The absence of seminal vesicles means canine semen lacks fructose and citric acid, relying instead on prostatic secretions rich in cholesterol and lactate.",
        "Why_Not": "Bulls have large, lobulated seminal vesicles that produce a significant portion of the ejaculate volume. Boars have extremely massive seminal vesicles that secrete the gel fraction. Stallions have piriform vesicular glands. Only the dog completely lacks these glands.",
        "Wow_Approach": "Because the dog only has a prostate gland, any prostatic pathology (like BPH, prostatitis, or prostatic cysts) will immediately affect all three fractions of the ejaculate. Measuring prostatic specific esterase (CPSE) in canine blood is a highly sensitive diagnostic for these conditions."
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
