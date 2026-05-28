import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1127: {
        "topic": "Accessory Sex Glands - Seminal Vesicle Dominance in Bulls",
        "Core_Anatomy": "Bovine seminal vesicles (vesicular glands), pelvic urethra, and urethralis muscle.",
        "Pathogenesis_Immediate": "The accessory sex gland that contributes the majority of the volume of the seminal plasma (ejaculatory volume) in the Bull is the Seminal Vesicle (vesicular gland), contributing 60-70% of the total volume.",
        "Pathogenesis_Deep": "Bovine accessory gland secretions: (1) Seminal vesicles: large, lobulated glands that secrete a thick, yellowish, protein-rich fluid containing fructose, citric acid, and riboflavin. This fluid makes up 60-70% of the normal 4-8 ml ejaculate. (2) Prostate: contributes only 5-10% of the volume. (3) Ampullae: secrete a small, sperm-rich pre-spermal fraction. (4) Cowper's (bulbourethral) glands: secrete a very small cleansing fraction. The high volume of vesicular fluid serves to dilute, buffer, and provide immediate energy to the sperm during ejaculation.",
        "Why_Not": "In dogs, the prostate gland is the sole accessory gland and contributes 100% of the volume. In bulls, however, the prostate is relatively small, and the seminal vesicles are highly dominant.",
        "Wow_Approach": "To detect active vesicular gland infection (seminal vesiculitis): look for large clumps of neutrophils ('pus cells') in the ejaculate. Affected bulls will also have a sharp drop in seminal pH and fructose concentration, rendering the semen unviable for cryopreservation."
    },
    1128: {
        "topic": "Buck Seminal Plasma - Cowper's Gland EYCE Secretion (Repeated MCQ)",
        "Core_Anatomy": "Caprine bulbourethral (Cowper's) glands, pelvic urethra, and sperm membrane.",
        "Pathogenesis_Immediate": "The Bulbourethral gland in the buck secretes Egg Yolk Coagulating Enzyme (EYCE / phospholipase A2) into the seminal plasma, which causes severe toxicity in egg yolk extenders.",
        "Pathogenesis_Deep": "EYCE reacts with lecithin in egg yolk to produce lysolecithin, a highly toxic surfactant that lyses sperm cell membranes. Because the bulbourethral gland is the sole source of this enzyme, buck semen must either be washed by centrifugation to remove seminal plasma or diluted in alternative extenders (like skim milk or soy lecithin).",
        "Why_Not": "The prostate gland, seminal vesicles, and ampullary glands do not synthesize or secrete EYCE, having no direct role in egg yolk coagulation in goats.",
        "Wow_Approach": "Using skim milk extenders is the most cost-effective field method for freezing buck semen, as casein micelles in milk naturally bind and block EYCE, bypassing the need for centrifugation."
    },
    1129: {
        "topic": "The Diadem Defect - Sperm Nuclear Membrane Invagination",
        "Core_Anatomy": "Sperm head nucleus, chromatin, and the inner nuclear membrane.",
        "Pathogenesis_Immediate": "The 'Diadem defect' is a specific, primary morphological abnormality of spermatozoa characterized by a circular arrangement of invaginations or pouches (craters) along the nuclear membrane.",
        "Pathogenesis_Deep": "The Diadem defect: (1) Originates during active spermiogenesis in the testes. (2) Invaginations of the inner nuclear membrane form a ring of pouches (resembling a crown or 'diadem') at the anterior edge of the post-acrosomal sheath. (3) These pouches trap nucleoplasm and appear as a distinct line of small 'craters' or 'nuclear vacuoles' under differential interference contrast (DIC) microscopy. It is highly correlated with transient heat stress, fever, or administration of dexamethasone, indicating acute testicular stress.",
        "Why_Not": "Microcephalic head refers to a small sperm head due to incomplete chromatin packaging. Pyriform head refers to a pear-shaped head. The diadem defect is strictly a nuclear membrane invagination.",
        "Wow_Approach": "Under standard brightfield microscopy, diadem defects can be easily missed. To verify: use differential interference contrast (DIC) microscopy or stain semen with Giemsa. Finding >15% diadem-defective sperm indicates significant sub-fertility due to compromised chromatin stability."
    },
    1130: {
        "topic": "Andrology True/False - Scrotal Thermoregulation and Hypoplasia (Repeated)",
        "Core_Anatomy": "Scrotal skin, tunica dartos, cremaster muscle, and testicular parenchyma.",
        "Pathogenesis_Immediate": "Key True/False: The principal thermoregulator of the testis is the Scrotum (via tunica dartos, cremaster, and scrotal sweat glands), not the tunica albuginea (making the statement FALSE). Testicular hypoplasia diagnosis at one year of age in bulls is TRUE.",
        "Pathogenesis_Deep": "These statements cover core diagnostic and anatomical facts: (1) The tunica albuginea is a tough, fibrous connective tissue capsule that surrounds the testis to maintain internal pressure and support tubules, but has zero active role in thermoregulation. Thermoregulation is driven by the scrotum's vascular exchange, sweat glands, and muscle-driven distance from the body cavity. (2) Scrotal circumference and semen analysis at 12 months (puberty) reliably identify congenital testicular hypoplasia.",
        "Why_Not": "Attributing thermoregulation to the tunica albuginea is a severe physiological error; the albuginea lacks the sweat glands, thin dermis, and vascular networks present in the scrotum.",
        "Wow_Approach": "To assess scrotal thermoregulation: measure the temperature gradient. The scrotal skin surface should register exactly 2-4°C lower than core body temperature. A higher surface temperature indicates active thermoregulatory failure."
    },
    1139: {
        "topic": "Andrology Matching - Embryonic Development and Tissue Barriers (Repeated)",
        "Core_Anatomy": "Mesonephric (Wolffian) duct and Sertoli cell junctions.",
        "Pathogenesis_Immediate": "Key matching pairs: Wolffian duct matches to epididymis and vas deferens development; Blood-testis barrier matches to Sertoli cell tight junctions; Os penis matches to canine baculum.",
        "Pathogenesis_Deep": "These matching pairs cover essential developmental and physical systems: (1) The Wolffian (mesonephric) duct is the embryonic precursor to the male reproductive plumbing (epididymis, vas deferens, seminal vesicles), stimulated by fetal Leydig cell testosterone. (2) The BTB isolates haploid gametes. (3) The baculum bone facilitates rapid intromission.",
        "Why_Not": "The Mullerian duct is the embryonic precursor to the female reproductive tract (oviduct, uterus, cervix, cranial vagina), which regresses in males under the influence of Sertoli-derived Anti-Mullerian Hormone (AMH).",
        "Wow_Approach": "To remember embryology: the presence of both testosterone (Wolffian driver) and AMH (Mullerian regressor) is mandatory to successfully develop a normal male reproductive tract. An absence of either leads to persistent Mullerian duct syndrome (PMDS)."
    },
    1140: {
        "topic": "Wolffian Duct - Embryonic Origin of Male Plumbing",
        "Core_Anatomy": "Embryonic mesonephros, mesonephric (Wolffian) duct, and fetal Leydig cells.",
        "Pathogenesis_Immediate": "The Wolffian Duct (mesonephric duct) is the embryonic structure that differentiates under testosterone influence to form the Epididymis, Vas Deferens, and Seminal Vesicles.",
        "Pathogenesis_Deep": "Male reproductive tract embryology: (1) Early embryos possess both Wolffian (male) and Mullerian (female) duct systems. (2) The fetal SRY gene triggers testis differentiation. (3) Fetal Sertoli cells secrete Anti-Mullerian Hormone (AMH), causing regression of the Mullerian ducts. (4) Fetal Leydig cells secrete testosterone, which actively stimulates the Wolffian ducts to differentiate into the epididymal head, body, and tail, the vas deferens, and the seminal vesicles.",
        "Why_Not": "The testicular parenchyma and seminiferous tubules develop from the sex cords of the gonadal ridge, not the Wolffian duct. The prostate and bulbourethral glands develop from the embryonic urogenital sinus.",
        "Wow_Approach": "Persistent Mullerian Duct Syndrome (PMDS): In Miniature Schnauzer dogs, a congenital mutation in the AMH receptor causes the Mullerian ducts to persist alongside normal Wolffian structures. Affected males have normal external genitalia but possess a uterus and oviducts inside their abdomen."
    },
    1141: {
        "topic": "Blood-Testis Barrier - Sertoli Cell Tight Junctions (Repeated Matching)",
        "Core_Anatomy": "Sertoli cell tight junctions (zonula occludens) and the seminiferous epithelium.",
        "Pathogenesis_Immediate": "The Blood-Testis Barrier (BTB) is formed by tight junctions between adjacent Sertoli cells, physically isolating haploid germ cells from the host immune system.",
        "Pathogenesis_Deep": "The BTB divides the seminiferous tubule into: (1) Basal compartment: contains diploid spermatogonia exposed to blood. (2) Adluminal compartment: contains haploid spermatids. Because meiosis generates unique, non-self antigens on haploid cells, the tight junctions of the BTB prevent immune cells and immunoglobulins from entering, preventing autoimmune orchitis.",
        "Why_Not": "The basement membrane is porous and does not block immune cells. Leydig cells reside in the interstitium and have no tight junctions. The BTB is strictly a Sertoli-to-Sertoli tight junction system.",
        "Wow_Approach": "Clinical correlation: Any trauma, biopsy, or severe infection (such as Brucellosis) that ruptures the Blood-Testis Barrier will expose the haploid spermatids to systemic circulation, causing autoimmune testicular degeneration."
    },
    1151: {
        "topic": "Andrology Short Notes - Laboratory and Clinical Concepts (Repeated)",
        "Core_Anatomy": "Male reproductive system and processing laboratory.",
        "Pathogenesis_Immediate": "Descriptive short notes in Andrology focus on: Semen extenders, Cryptorchidism, Electroejaculation, Testicular Biopsy, and Breeding Soundness Evaluation (BSE).",
        "Pathogenesis_Deep": "Each short-note topic requires structured clinical formatting: (1) Semen extenders: discuss composition (buffers, cryoprotectants, nutrients, antibiotics) and freezing steps. (2) Cryptorchidism: discuss inheritance (polygenic recessive), unilateral vs bilateral, tumor risks (Sertoli cell, seminoma), and diagnosis. (3) Electroejaculation: discuss physiological pathway (pelvic nerve stimulation), advantages (injured/wild bulls), and limitations.",
        "Why_Not": "Vague descriptions without scientific terms (e.g., failing to mention glycerol in extenders or temperature in AVs) will fail final academic grading, as the candidate must demonstrate laboratory and clinical competency.",
        "Wow_Approach": "When writing on Electroejaculation, always explain the safety protocol: use a rectal probe with segmented electrodes, start at 0 volts, gradually increase to a peak of 10-15 volts in rhythmic 3-second pulses."
    },
    1153: {
        "topic": "VGO-II Course Syllabus - Comprehensive Andrology and Biotechnology (Repeated)",
        "Core_Anatomy": "Male reproductive system and reproductive biotechnology.",
        "Pathogenesis_Immediate": "VGO-II is gynaecology's sister course, providing standard clinical instructions on male breeding soundness (Andrology) and obstetrical emergencies.",
        "Pathogenesis_Deep": "The gynaecological curriculum requires complete integration of: (1) Testicular and accessory gland physiology. (2) Semen preservation chemistry. (3) Parturition mechanics (endocrine induction via fetal ACTH and cortisol). (4) Dystocia resolution (mutation, traction, fetotomy, caesarean). It is the definitive clinical framework for field veterinary gynaecologists.",
        "Why_Not": "Female oestrous cycles, non-pregnant diagnostics, and artificial insemination logistics are taught in VGO-I, while VGO-II focuses strictly on mature male fertility and periparturient female gynaecology.",
        "Wow_Approach": "In clinical practice, treat Andrology and Obstetrics as the beginning and end of the reproductive production line: Andrology ensures high-quality genetics are successfully seeded, while Obstetrics ensures the viable harvest of the fetus at term."
    },
    1154: {
        "topic": "VGO Andrology Objective parameters - Standard Constants (Repeated)",
        "Core_Anatomy": "Male reproductive system.",
        "Pathogenesis_Immediate": "This objective section evaluates core facts: sperm enzymes (hyaluronidase in head), optimal thawing temperatures (37°C), discovery history, and developmental descent.",
        "Pathogenesis_Deep": "This testing structure ensures a rapid, independent evaluation of factual recall in Andrology. Topics include the acrosome origin from the Golgi apparatus, BPH castrative therapies, and semen packaging history.",
        "Why_Not": "Subjective essays allow for general explanations, whereas the MCQ section demands precise, singular correct answers to verify diagnostic accuracy in clinical veterinary medicine.",
        "Wow_Approach": "Familiarize yourself with the exact grading weight: Part-A carries 60 marks of highly granular factual questions."
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
