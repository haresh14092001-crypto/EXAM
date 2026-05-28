import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1155: {
        "topic": "VGO Objective Section - Exam Hall Instructions (Repeated)",
        "Core_Anatomy": "Male reproductive system and processing laboratory.",
        "Pathogenesis_Immediate": "TANUVAS exam guidelines require the 60-mark objective section to be completed within 1 hour and handed over.",
        "Pathogenesis_Deep": "This testing structure isolates direct factual recall of reproductive physiology, preventing the use of descriptive cues from essays in Part-B. Evaluated topics include: semen packaging materials, epididymal transit times, and hormonal parameters.",
        "Why_Not": "Subjective essays and case studies are graded separately in Part-B, which is completed over the remaining 2 hours of the exam.",
        "Wow_Approach": "To ensure academic success, practice rapid-fire recall of quantitative constants like sperm transit times and vapor freezing heights."
    },
    1156: {
        "topic": "Sperm Production Kinetics - Mammalian Daily Sperm Output",
        "Core_Anatomy": "Seminiferous epithelium, spermatogonia, Sertoli cells, and testicular parenchyma.",
        "Pathogenesis_Immediate": "The biological rate of sperm production in mature domestic mammals is extremely high, averaging approximately 10,000 spermatozoa produced per second.",
        "Pathogenesis_Deep": "Spermatogenic production is a continuous, highly efficient assembly line: (1) In bulls, the daily sperm production (DSP) is ~5-10 billion sperm. (2) This breaks down mathematically to ~10,000 sperm produced per second across the 5,000 meters of seminiferous tubules. (3) The rate is determined prepubertally by the number of Sertoli cells undergoing mitosis, as each Sertoli cell can support a fixed number of germ cells. High-quality genetics and nutrition maximize this baseline.",
        "Why_Not": "A rate of 10 sperm per second would cause immediate sterility. Ejaculation output represents the accumulated epididymal reserve, whereas sperm production is the continuous testicular meiotic output.",
        "Wow_Approach": "To quantify daily sperm production in a living bull: measure the scrotal circumference. In Holstein bulls, every 1 cm increase in scrotal circumference above 30 cm corresponds to an increase of ~1.2 billion in daily sperm production."
    },
    1157: {
        "topic": "Male Reproductive Tract - Non-Accessory Sex Glands",
        "Core_Anatomy": "Urogenital tract, ampulla, vesicular glands, prostate, and bulbourethral glands.",
        "Pathogenesis_Immediate": "Structures such as the anterior pituitary gland, thyroid, or adrenal glands are endocrine glands, and are not considered accessory sex glands of the male reproductive tract.",
        "Pathogenesis_Deep": "The male accessory sex glands are strictly exocrine glands that secrete fluid directly into the pelvic urethra to form seminal plasma: (1) Ampullary glands (absent in boars). (2) Seminal vesicles (absent in dogs). (3) Prostate gland (only gland in dogs). (4) Bulbourethral (Cowper's) glands (absent in dogs). While the anterior pituitary regulates reproduction via LH and FSH, it is a central endocrine gland, not an accessory urogenital gland.",
        "Why_Not": "Vesicular glands, Cowper's glands, and ampullae are classic, functional accessory sex glands that directly synthesize seminal plasma, whereas systemic endocrine glands do not drain into the urethra.",
        "Wow_Approach": "Identify accessory glands by palpation: rectal palpation in the bull easily identifies the lobulated seminal vesicles lying cranial to the neck of the bladder, flanking the urethra, and the thin, band-like body of the prostate."
    },
    1158: {
        "topic": "Epididymal Transit Time - Ruminant Sperm Transport (Repeated MCQ)",
        "Core_Anatomy": "Caput, corpus, and cauda epididymis.",
        "Pathogenesis_Immediate": "The normal physiological transit time required for spermatozoa to travel from the rete testis through the epididymis to the vas deferens in the bull is 9 to 14 days.",
        "Pathogenesis_Deep": "Transit through the epididymis is driven by hydrostatic pressure from the testes and rhythmic contractions of the epididymal smooth muscle. During this 9-14 day transit, sperm undergo mandatory biochemical maturation, acquiring forward progressive motility and fertilizing capability while being concentrated and stored.",
        "Why_Not": "A 1-2 day transit is too rapid, yielding completely immature, infertile sperm with proximal droplets. A 20-30 day transit represents severe epididymal stasis, leading to sperm senescence and death.",
        "Wow_Approach": "If a bull is over-collected (e.g., 4 collections daily), the epididymal transit time is artificially shortened, leading to ejaculates containing highly immature sperm with high distal cytoplasmic droplets."
    },
    1160: {
        "topic": "Sperm Morphology - Origin Phase of Primary Defects",
        "Core_Anatomy": "Seminiferous epithelium, spermatids, and chromatin.",
        "Pathogenesis_Immediate": "Primary sperm abnormalities (such as double heads, pyriform heads, and tight coiled tails) arise exclusively during the differentiation phase (spermiogenesis) of spermatogenesis in the testes.",
        "Pathogenesis_Deep": "Spermatogenesis has three phases: (1) Mitotic phase (spermatogonial proliferation). (2) Meiotic phase (primary and secondary spermatocytes undergoing genetic division). (3) Differentiation phase (spermiogenesis, where round spermatids transform into elongated spermatozoa). Morphological defects of the head and nuclear chromatin condense during this differentiation phase. Disturbances (like heat stress or fever) during this phase disrupt nuclear packaging and tail assembly, creating primary abnormalities.",
        "Why_Not": "Mitotic division only increases cell numbers. Stem cell renewal maintains the germ pool. While meiosis duplicates DNA, the actual physical molding of the head and flagellum occurs during differentiation.",
        "Wow_Approach": "Because primary defects arise during the 17-day differentiation phase of spermiogenesis, any testicular insult will take ~10-14 days to appear in the ejaculated semen, representing the transit time through the epididymis."
    },
    1161: {
        "topic": "History of AI - First Successful AI in the Bitch (Repeated MCQ)",
        "Core_Anatomy": "Vaginal vault, cervix, and the canine uterus.",
        "Pathogenesis_Immediate": "The first scientifically recorded successful artificial insemination (AI) was performed in the Bitch by Lazzaro Spallanzani in 1780.",
        "Pathogenesis_Deep": "Spallanzani collected semen from a male dog and transcervically deposited it into a receptive bitch, achieving the birth of three healthy puppies 62 days later, proving that sperm carry the complete paternal genetic contribution.",
        "Why_Not": "While cattle and sheep are today the most commercially significant species for AI, the original proof-of-concept success was achieved in the dog, making 'Bitch' the historical milestone answer.",
        "Wow_Approach": "Spallanzani also conducted the first experiments on freezing sperm, showing that canine spermatozoa resume progressive motility upon warming."
    },
    1162: {
        "topic": "Semen Quality Control - Test Freezing (Repeated MCQ)",
        "Core_Anatomy": "Sperm cell plasma membrane and cryopreservation.",
        "Pathogenesis_Immediate": "Test freezing refers to the quality control procedure of freezing and thawing a single straw from a newly processed semen batch to assess post-thaw progressive motility before releasing the batch.",
        "Pathogenesis_Deep": "Cryopreservation induces severe osmotic stress on spermatozoa. Test freezing ensures that the diluent formulation and freezing curve achieved adequate cryoprotection, requiring a minimum of 30-35% progressive post-thaw motility to pass QA.",
        "Why_Not": "Testing neat semen before dilution evaluates initial concentration and motility, but cannot predict cryo-survival. Test freezing is strictly the post-thaw assessment.",
        "Wow_Approach": "Perform the Host (Hypo-Osmotic Swelling Test) on the test-frozen sample to confirm functional membrane integrity, which correlates better with field fertility than visual motility."
    },
    1164: {
        "topic": "Semen Packaging - Polyvinyl Chloride French Straws (Repeated MCQ)",
        "Core_Anatomy": "Sperm membrane and cryoprotectant medium.",
        "Pathogenesis_Immediate": "The primary material used for manufacturing semen packaging straws is Polyvinyl Chloride (PVC) or Polypropylene.",
        "Pathogenesis_Deep": "Semen packaging requires materials that are biochemically inert (non-spermatotoxic), transparent, and highly resistant to extreme temperature shifts (from room temperature to liquid nitrogen at -196°C). PVC French straws possess these cryogenic properties.",
        "Why_Not": "Polyvinyl alcohol is used exclusively as the powder plug sealant, not as the structural plastic of the straw body. Propylene glycerol is a cryoprotectant liquid, not a solid packaging plastic.",
        "Wow_Approach": "French straws (0.25 ml and 0.5 ml) are sealed at one end with a polyvinyl alcohol (PVA) powder plug that gels upon contact with fluid, and the other end is crimped or sealed with heat."
    },
    1165: {
        "topic": "Bovine Penile Anatomy - Normal Bull Penislength",
        "Core_Anatomy": "Sigmoid flexure, glans penis, retractor penis muscle, and prepuce.",
        "Pathogenesis_Immediate": "The normal anatomical length of the non-erect, flaccid penis in mature breeding bulls is approximately 60 to 75 cm.",
        "Pathogenesis_Deep": "Bovine penile anatomy: (1) The bull has a fibroelastic penis that is relatively rigid even when non-erect, containing minimal cavernous tissue. (2) The penis is arranged in an S-shaped curve (sigmoid flexure) inside the prepuce, suspended by the bilateral retractor penis muscles. (3) The total anatomical length from the root to the tip of the glans is 60-75 cm. (4) During erection, relaxation of the retractor penis muscles straightens the sigmoid flexure, causing up to 25-30 cm of the penis to protrude from the sheath for copulation.",
        "Why_Not": "A length of 10-15 cm represents the protrusion length in small ruminants (rams/bucks), but is far too short for the massive anatomy of the bull. A length of 15-20 cm is typical for stallions when flaccid.",
        "Wow_Approach": "Sigmoid flexure clinical check: In bulls with breeding failure, manually palpate the sigmoid flexure just caudal to the scrotum. If the sigmoid cannot be fully straightened due to adhesions or retractor penis muscle fibrosis, the bull will be unable to protrude his penis, presenting with impotentia coeundi."
    },
    1166: {
        "topic": "Eunuchoidism - Congenital Androgen Insufficiency (Repeated MCQ)",
        "Core_Anatomy": "Testes, Leydig cells, and secondary sex characteristics.",
        "Pathogenesis_Immediate": "The clinical term 'Eunuchoidism' denotes a pathologic state of androgen deficiency in the male, characterized by a lack of secondary sex characteristics, reduced libido, and infantile genitalia.",
        "Pathogenesis_Deep": "Eunuchoidism is caused by primary hypogonadism (testicular failure) or secondary hypogonadism (pituitary failure), where a lack of LH secretion prevents Leydig cell stimulation. Affected males have a feminine body conformation and hypoplastic accessory glands.",
        "Why_Not": "Overt sexual behavior is nymphomania. A complete lack of thyroid hormone is cretinism. Eunuchoidism specifically relates to testicular androgen insufficiency.",
        "Wow_Approach": "In rams, eunuchoidism presents with 'kid-like' horns and a fine, soft wool coat. The scrotal circumference remains immature, and testosterone is baseline (<0.2 ng/ml)."
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
