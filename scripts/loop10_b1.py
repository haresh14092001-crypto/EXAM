import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1102: {
        "topic": "VGO-II Syllabus - Clinical Andrology and Reproductive Biotechnology",
        "Core_Anatomy": "Male reproductive tract and molecular gamete interface.",
        "Pathogenesis_Immediate": "VGO-II curriculum provides comprehensive instruction in male reproductive soundness, semen biochemistry, cryopreservation, and advanced biotechnology like embryo transfer.",
        "Pathogenesis_Deep": "The syllabus covers: (1) Testicular physiology, including seminiferous tubule length (up to 5,000 meters in bulls) and HPT endocrine pathways. (2) Semen preservation (tris extenders, glycerol cryoprotection, vapor-phase freezing). (3) Sperm biology, including capacitation (reversible membrane remodeling) and the acrosome reaction (irreversible exocytosis).",
        "Why_Not": "General female estrous cycle regulation is VGO-I, while VGO-II focuses strictly on mature male reproductive pathology, semen banking, and advanced veterinary embryology.",
        "Wow_Approach": "To master the curriculum: always link quantitative cellular constants (e.g., sperm production rates, tubule length) with macroscopic diagnostic criteria (e.g., scrotal circumference) to build clinical accuracy."
    },
    1104: {
        "topic": "VGO-511 Andrology Objective parameters (Repeated MCQ)",
        "Core_Anatomy": "Male reproductive system and processing laboratory.",
        "Pathogenesis_Immediate": "The objective section of VGO-511 evaluates standard quantitative reproductive and semen preservation parameters.",
        "Pathogenesis_Deep": "Topics tested include: seminiferous tubule dimensions, motility criteria, the reversible nature of capacitation, minimum processing volumes for cryopreservation, and seminal plasma composition.",
        "Why_Not": "Clinical essay questions assess surgical or therapeutic interventions, while the objective section focuses on these biological and technical constants.",
        "Wow_Approach": "Compile species-specific reference tables (e.g., bull vs boar tubule length and sperm concentration) to quickly eliminate distractors in multiple-choice exams."
    },
    1119: {
        "topic": "Seminiferous Tubules - Extreme Length in Breeding Bulls",
        "Core_Anatomy": "Testicular parenchyma, seminiferous tubules (convoluted and straight), and the mediastinum testis.",
        "Pathogenesis_Immediate": "The total combined length of the seminiferous tubules in both testes of a single mature breeding bull is approximately 3,000 to 5,000 meters (typically ~5,000 meters total).",
        "Pathogenesis_Deep": "The seminiferous tubules are the highly convoluted tubes where spermatogenesis occurs. (1) In the bull, each testis contains up to 250-400 lobules, and each lobule contains highly coiled tubules that are 10-15 meters long individually. (2) When uncoiled and combined, the total tubular length in a single testis is 2,000-2,500 meters, totaling ~5,000 meters in both testes. This massive length provides an enormous surface area of seminiferous epithelium, allowing the bull to produce up to 5-10 billion spermatozoa daily.",
        "Why_Not": "A length of 10-15 cm represents the physical scrotal length, not the internal tubular length. A length of 50-100 meters represents the epididymis length, which is a single duct but much shorter than the combined seminiferous tubules.",
        "Wow_Approach": "Because the tubular compartment occupies >80% of the testicular mass, measuring Scrotal Circumference is a highly accurate, direct clinical proxy for seminiferous tubule length and daily sperm production capacity in beef and dairy bulls."
    },
    1120: {
        "topic": "Impotentia Coeundi - Inability to Copulate (Repeated MCQ)",
        "Core_Anatomy": "Sigmoid flexure, prepuce, and pelvic limbs.",
        "Pathogenesis_Immediate": "A reduced to complete lack of sexual desire or physical ability to copulate in the male is defined clinically as Impotentia Coeundi.",
        "Pathogenesis_Deep": "Impotentia coeundi involves mechanical or behavioral mounting failure, caused by: musculoskeletal pain (stifle joint gonitis), penile deviation (persistent frenulum), or complete lack of central nervous system libido. It is distinct from impotentia generandi, where copulation is normal but the semen is infertile.",
        "Why_Not": "Phimosis is only one specific cause of impotentia coeundi, representing an inability to protrude the penis. Impotentia generandi refers to fertilization failure, not copulation failure.",
        "Wow_Approach": "Verify potentia coeundi by observing the bull mount a teaser. If he mounts, achieves erection, and thrusts, he possesses potentia coeundi, and the diagnostic focus shifts to semen quality."
    },
    1121: {
        "topic": "Sperm Abnormalities - Primary Defects of Testicular Origin (Repeated MCQ)",
        "Core_Anatomy": "Seminiferous tubules and germ cells.",
        "Pathogenesis_Immediate": "Primary sperm abnormalities (such as double heads, pyriform heads, and microcephalic heads) arise exclusively during spermatogenesis in the Testes.",
        "Pathogenesis_Deep": "Primary abnormalities represent true testicular dysfunction, arising due to mitotic or meiotic disturbances in the seminiferous epithelium. Secondary abnormalities arise during transit in the epididymis (detached heads, distal droplets), while tertiary defects are handling-induced (cold shock).",
        "Why_Not": "The epididymis and vas deferens are transport ducts; they do not determine head shape or nuclear abnormalities, which are fixed during chromatin condensation in the testis.",
        "Wow_Approach": "If a bull has >15% primary defects, it indicates testicular degeneration or heat stress. Because they arise in the testes, a minimum of 60 days of sexual rest is required for any potential improvement."
    },
    1122: {
        "topic": "Leydig Cells - Testosterone Synthesis and LH Regulation (Repeated MCQ)",
        "Core_Anatomy": "Testicular interstitium, Leydig cells, and LH receptors.",
        "Pathogenesis_Immediate": "The primary male sex hormone, testosterone, is synthesized and secreted by the interstitial Leydig cells under the direct stimulation of Luteinizing Hormone (LH).",
        "Pathogenesis_Deep": "LH binds G-protein coupled receptors on Leydig cells, stimulating cAMP-driven transport of cholesterol across mitochondrial membranes via the StAR protein. Cholesterol is then converted to pregnenolone and testosterone in the smooth endoplasmic reticulum, essential for spermatogenesis and libido.",
        "Why_Not": "Sertoli cells respond to FSH and produce androgen-binding protein (ABP) but not testosterone. Myoid cells are contractile cells forming the seminiferous tubule wall.",
        "Wow_Approach": "Because testosterone is lipid-soluble and cannot be stored, Leydig cells synthesize it de novo in response to pulsatile LH, resulting in highly pulsatile systemic levels."
    },
    1123: {
        "topic": "Sperm Motility - Progressive Motility as Fertility Gold Standard",
        "Core_Anatomy": "Sperm flagellum, axoneme (9+2 microtubules), mitochondrial sheath, and cervical mucus.",
        "Pathogenesis_Immediate": "Good quality semen should possess high Progressive Motility, where spermatozoa swim actively in a straight forward direction rather than in circular or reverse paths.",
        "Pathogenesis_Deep": "Sperm motility is divided into: (1) Progressive motility: the cell travels forward in a straight or slightly curved line, which is mandatory to traverse the cervical mucus barrier and swim up the oviduct. (2) Non-progressive motility: the tail beats, but the cell moves in circles (circular motility) or vibrates in place. Circular motility often indicates structural flagellar damage (e.g., bent tails or eccentric mitochondrial sheets) or early cold shock. Good semen requires >70% progressive motility raw, and >30-35% post-thaw.",
        "Why_Not": "Circular or reverse motility prevents sperm from navigating the female reproductive tract, trapping them in the vaginal vault where they undergo rapid phagocytosis by neutrophils.",
        "Wow_Approach": "Use Computer-Assisted Sperm Analysis (CASA) to measure VSL (straight-line velocity) and VAP (average path velocity). A VSL >50 micrometers/second confirms high progressive forward motility, highly correlated with pregnancy rates."
    },
    1124: {
        "topic": "Sperm Capacitation - The Reversible Activation Reaction",
        "Core_Anatomy": "Sperm plasma membrane, cholesterol, glycoproteins, and female uterine fluid.",
        "Pathogenesis_Immediate": "Sperm Capacitation (the biochemical activation process occurring in the female reproductive tract) is a fully Reversible reaction.",
        "Pathogenesis_Deep": "During transit in the female tract (uterus and oviduct), sperm undergo capacitation: (1) Seminal plasma decapacitation factors (glycoproteins coating the sperm) are removed. (2) Cholesterol is effluxed from the sperm membrane, increasing membrane fluidity. (3) This allows calcium channels to open, hyperactivating motility. If capacitated sperm are recovered and placed back into seminal plasma, they bind decapacitation factors again, reversing the capacitation state (re-decapacitation). In contrast, the subsequent Acrosome Reaction is a structural exocytotic fusion of membranes, which is completely irreversible.",
        "Why_Not": "The acrosome reaction involves physical fusion and vesiculation of the outer acrosomal membrane and plasma membrane, resulting in the shedding of the acrosomal cap; once shed, it cannot be rebuilt, making it irreversible. HOS reaction is a physical swelling that is irreversible.",
        "Wow_Approach": "This reversibility is a key evolutionary adaptation: it prevents sperm from undergoing premature activation during storage in the epididymis or during transit, reserving the irreversible acrosome reaction strictly for the immediate vicinity of the oocyte."
    },
    1125: {
        "topic": "Bull Semen Processing - Minimal Quality Thresholds (Repeated MCQ)",
        "Core_Anatomy": "Bull ejaculatory tract and processing laboratory.",
        "Pathogenesis_Immediate": "The minimum raw ejaculate volume and sperm concentration required to process semen for deep-freezing is a volume of 2.5 ml and a concentration of 500 million/ml.",
        "Pathogenesis_Deep": "Diluting an ejaculate that falls below these thresholds is economically unviable and biologically risky. Low concentration increases sperm vulnerability to lipid peroxidation and ice crystal damage, resulting in poor post-thaw recovery.",
        "Why_Not": "A 10 ml volume with 1,200 million concentration is a premium ejaculate, but is not the minimum processing threshold. A 3 ml volume with 100 million is too dilute and cannot be processed.",
        "Wow_Approach": "Always verify that the raw semen also possesses a minimum of 70% progressive motility and less than 15% total morphological abnormalities before initiating dilution."
    },
    1126: {
        "topic": "Bovine Semen Processing - Minimal Quality Option (Repeated MCQ)",
        "Core_Anatomy": "Bull ejaculatory tract and processing laboratory.",
        "Pathogenesis_Immediate": "Standard commercial AI centers require a minimum raw ejaculate volume of 2.5 ml and a concentration of 500 million/ml to justify the dilution and freezing protocol.",
        "Pathogenesis_Deep": "Processing semen is highly resource-intensive. Diluting an ejaculate that falls below the 500 million/ml threshold is economically unviable because it yields too few straws per batch. Biologically, low-concentration ejaculates often contain a higher percentage of abnormal sperm and are highly susceptible to lipid peroxidation due to a lack of protective seminal plasma proteins.",
        "Why_Not": "Processing highly dilute semen (e.g., 100 million/ml) results in poor post-thaw progressive motility because the low density of sperm cells increases their vulnerability to ice crystal damage during the rapid freezing process.",
        "Wow_Approach": "To ensure maximum quality, the AI center uses a CASA system to verify that the raw semen also has a minimum of 70% progressive motility and less than 15% total morphological abnormalities before processing."
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
print(f"Batch 1/5 DONE: Updated {updated} questions.")
