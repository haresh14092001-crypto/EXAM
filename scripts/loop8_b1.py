import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    839: {
        "topic": "History of AI - First Successful AI in the Bitch",
        "Core_Anatomy": "Vaginal vault, cervix, and the canine uterine body.",
        "Pathogenesis_Immediate": "The first scientifically recorded successful artificial insemination (AI) was performed in the Bitch (dog) by the Italian physiologist Lazzaro Spallanzani in 1780.",
        "Pathogenesis_Deep": "Spallanzani collected semen from a male dog, successfully deposited it transcervically into the vaginal vault of a receptive bitch, and achieved the birth of three healthy puppies 62 days later. This historic experiment laid the foundations for mammalian reproductive biotechnology, proving that sperm cells carry the complete paternal genetic contribution and can fertilize ova outside of natural copulation. AI was subsequently expanded to horses by Repiquet (1890) and cattle by Ivanoff (1899) in Russia.",
        "Why_Not": "While cattle (cows) and sheep (ewes) are today the most commercially significant species for AI, the original proof-of-concept success was achieved in the dog, making 'Bitch' the historical milestone answer.",
        "Wow_Approach": "Spallanzani also conducted the first experiments on freezing sperm: he placed canine spermatozoa in snow and observed that they became immotile, but resumed active progressive motility upon warming. This was the first primitive documentation of cryo-survival."
    },
    840: {
        "topic": "Semen Collection Hygiene - Latex Sterilization Methods",
        "Core_Anatomy": "Artificial Vagina (AV) latex liner, semen collection cone, and spermatid cell membranes.",
        "Pathogenesis_Immediate": "Latex parts of reproductive equipment (AV liners, collection cones) are sterilized using Ethylene Oxide (Gaseous sterilization) or Autoclaving, with ethylene oxide being preferred to prevent rubber degradation.",
        "Pathogenesis_Deep": "Latex and rubber components of artificial vaginas are highly sensitive to heat and moisture. Repeated autoclaving (121°C at 15 psi) or dry heat causes progressive vulcanization breakdown, cracking, and sticky degradation of the latex. Gaseous sterilization with Ethylene Oxide (EtO) at low temperatures (37-55°C) is highly effective and preserves latex elasticity. However, EtO is highly toxic and residues must be fully aerated for 24-48 hours before use, as residual gas is highly spermatotoxic and causes immediate membrane lysis.",
        "Why_Not": "Dry heat (160°C) melts latex completely. UV radiation only sterilizes the immediate surface and does not penetrate folds or internal tube lumens, leaving pathogens behind.",
        "Wow_Approach": "To check for toxic residues on EtO-sterilized AV liners: perform a sperm contact test. Place a droplet of fresh, high-motility bull semen directly on the liner for 1 minute, then check motility. If motility drops >10% compared to a glass control, the liner requires further aeration."
    },
    841: {
        "topic": "Semen Quality Control - Test Freezing",
        "Core_Anatomy": "Sperm cell plasma membrane, acrosomal integrity, and post-thaw vascular compartment.",
        "Pathogenesis_Immediate": "Test freezing (or post-thaw evaluation) refers to the quality control procedure of freezing and thawing a single straw from a newly processed semen batch to assess post-thaw progressive motility and acrosome integrity before releasing the batch for commercial use.",
        "Pathogenesis_Deep": "Cryopreservation induces severe osmotic and thermal stress on spermatozoa. During the freezing process (using liquid nitrogen vapor at -196°C), up to 50% of the viable sperm pool is damaged. Test freezing ensures that the specific diluent formulation, glycerol equilibration time, and freezing curve achieved adequate cryoprotection for that individual ejaculate. The test straw is thawed at 37°C for 30 seconds, and must show a minimum of 30-35% progressive forward motility to pass standard QA criteria.",
        "Why_Not": "Testing neat semen before dilution evaluates initial concentration and motility, but cannot predict cryo-survival. Testing neat semen after dilution evaluates pre-freeze quality. Test freezing is strictly the post-thaw assessment.",
        "Wow_Approach": "Perform the Host (Hypo-Osmotic Swelling Test) on the test-frozen sample. Placing sperm in a 150 mOsm/L fructose-citrate solution causes intact membranes to swell and curl at the tail. This confirms functional membrane integrity, which correlates better with field fertility than visual motility."
    },
    842: {
        "topic": "Semen Packaging - Polyvinyl Chloride (PVC) Straws",
        "Core_Anatomy": "Sperm membrane, cryoprotectant medium, and liquid nitrogen environment.",
        "Pathogenesis_Immediate": "The primary material used for manufacturing semen packaging straws is Polyvinyl Chloride (PVC) or Polypropylene.",
        "Pathogenesis_Deep": "Semen packaging requires materials that are biochemically inert (non-spermatotoxic), transparent (allowing visual inspection of semen and printed labeling), and highly resistant to extreme temperature shifts (from room temperature to liquid nitrogen at -196°C). Polyvinyl chloride (PVC) possesses these properties. PVC French straws (0.25 ml and 0.5 ml) are sealed at one end with a polyvinyl alcohol (PVA) powder plug that gels upon contact with fluid, and the other end is crimped or sealed with heat.",
        "Why_Not": "Polyvinyl alcohol is used exclusively as the powder plug sealant, not as the structural plastic of the straw body. Propylene glycerol is a cryoprotectant liquid, not a solid packaging plastic.",
        "Wow_Approach": "French straws (invented by Robert Cassou) revolutionized AI: the 0.25 ml mini-straw allows highly efficient storage (up to 2,000 doses per canister) and has a highly uniform freezing/thawing rate compared to old glass ampoules, reducing cryo-injury by 20%."
    },
    843: {
        "topic": "Bovine Artificial Insemination - AI Sheath and Catheter Length",
        "Core_Anatomy": "Vaginal canal, cervix (interlocking rings), and the uterine body.",
        "Pathogenesis_Immediate": "The standard length of a bovine artificial insemination (AI) sheath and catheter is 40 to 45 cm (typically 45 cm or 18 inches) to ensure safe transcervical deposition.",
        "Pathogenesis_Deep": "The bovine reproductive tract is long and suspended: the vagina is 25-30 cm long, and the cervix is 8-10 cm. To perform the rectovaginal AI technique, the clinician must pass the catheter through the vulva, advance it through the vaginal vault, and manipulate the cervix over the catheter tip. The 45 cm length provides sufficient length for the operator's external hand to guide the catheter while the internal hand stabilizes the cervix rectally, placing the tip exactly at the internal cervical os.",
        "Why_Not": "A 10-15 cm sheath is too short, failing to even reach the external cervix. A 60-75 cm sheath is excessively long and flexible, making cervical manipulation difficult and increasing the risk of uterine wall puncture.",
        "Wow_Approach": "Deposition site rule: deposit the semen exactly in the uterine body (just past the final cervical ring). Depositing semen too deep in one uterine horn ('deep horn AI') can be done for low-dose sexed semen, but standard AI requires uterine body deposition to ensure equal sperm distribution to both oviducts."
    },
    844: {
        "topic": "Eunuchoidism - Congenital Androgen Insufficiency",
        "Core_Anatomy": "Testes, Leydig cells, pituitary gonadotrophs, and secondary sex characteristics.",
        "Pathogenesis_Immediate": "The clinical term 'Eunuchoidism' denotes a pathologic state of androgen deficiency (hypogonadism) in the male, characterized by a lack of secondary sex characteristics, reduced libido, and infantile external genitalia.",
        "Pathogenesis_Deep": "Eunuchoidism is caused by: (1) Primary hypogonadism (testicular failure due to hypoplasia or trauma, where Leydig cells fail to secrete testosterone). (2) Secondary hypogonadism (hypothalamic/pituitary failure, where a lack of LH secretion prevents Leydig cell stimulation). Affected males have a feminine body conformation, delayed closure of epiphyseal cartilage (leading to abnormally long limbs), lack of sexual desire (libido), and hypoplastic accessory sex glands.",
        "Why_Not": "Overt sexual behavior (nymphomania equivalent) is erotomania, not eunuchoidism. A complete lack of thyroid hormone is cretinism or myxedema. Eunuchoidism specifically relates to testicular androgen insufficiency.",
        "Wow_Approach": "In rams, eunuchoidism presents with 'kid-like' horns and a fine, soft wool coat. The scrotal circumference remains immature, and testosterone is baseline (<0.2 ng/ml). These males fail to display the Flehmen reaction when exposed to estrous ewes."
    },
    845: {
        "topic": "Canine Artificial Insemination - Minimum Sperm Count per Insemination",
        "Core_Anatomy": "Vaginal vault, cervix, and the canine uterine lumen.",
        "Pathogenesis_Immediate": "The minimum recommended number of progressively motile spermatozoa required per breeding or artificial insemination in the Bitch is 150 to 200 million (or 100-200 million depending on breed size).",
        "Pathogenesis_Deep": "Successful fertilization in the bitch requires a critical mass of sperm to overcome the long vaginal barrier and achieve transcervical migration. A standard normal ejaculate from a stud dog contains 200-1000 million sperm. When performing AI (especially using chilled or frozen semen), depositing fewer than 150 million progressively motile sperm results in a significant drop in conception rates and smaller litter sizes. If frozen semen is used, the minimum dose is often increased because cryopreserved sperm have a shorter lifespan in the female tract.",
        "Why_Not": "A dose of 20 million is typical for bovine AI (using highly fertile frozen semen), but is far too low for dogs, where natural vaginal deposition requires much larger numbers due to the absence of the uterine body deposition achieved in cattle.",
        "Wow_Approach": "To optimize success with low-dose or poor-quality stud semen: perform Transcervical Insemination (TCI) using a rigid endoscope (TCI camera) to deposit the semen directly into the uterine body. This allows successful pregnancy with only 50-80 million motile sperm."
    },
    846: {
        "topic": "Coital Lock in Bitches - Bulbous Glandis and Constrictor Vulvae",
        "Core_Anatomy": "Male glans penis (bulbous glandis), female vestibular sphincter, and constrictor vulvae muscle.",
        "Pathogenesis_Immediate": "The characteristic 'coital lock' (or tie) in dogs occurs due to the rapid engorgement of the male's Bulbous Glandis coupled with the active contraction of the female's Constrictor Vulvae muscle.",
        "Pathogenesis_Deep": "The canine coital lock is a unique physiological mechanism: (1) The male's penis contains an os penis (bone) that allows intromission before full erection. (2) Post-intromission, the bulbous glandis (a vascular ring at the base of the glans) engorges rapidly with blood, swelling to 2-3x its flaccid diameter. (3) The female's vestibular sphincter and constrictor vulvae muscles contract tightly behind the swollen bulbous glandis, locking the penis inside the vagina. The lock lasts 10-30 minutes, during which the male ejaculates the prostatic fraction (third fraction) of semen.",
        "Why_Not": "The os penis facilitates initial penetration but does not cause the lock (tie). A corkscrew-type penis is unique to the boar, which does not have a coital lock. The lock is strictly driven by the swollen bulbous glandis held by the constrictor vulvae.",
        "Wow_Approach": "Ejaculate Fractions: The dog ejaculates in three distinct fractions. Fraction 1 (pre-spermal, clear fluid) occurs during intromission. Fraction 2 (sperm-rich, milky fluid) occurs immediately after intromission. Fraction 3 (prostatic fluid, large volume) occurs exclusively during the coital lock, flushing the sperm forward."
    },
    847: {
        "topic": "Ventral Phimosis - Persistent Frenulum in Young Bulls",
        "Core_Anatomy": "Penile raphe, prepuce, and the glans penis.",
        "Pathogenesis_Immediate": "Ventral deviation of the penis (causing the penis to curve ventrally at erection, preventing intromission) is most commonly caused by a Persistent Frenulum in young bulls.",
        "Pathogenesis_Deep": "During fetal development, the penis and prepuce are fused along the ventral midline. Shortly before puberty (typically at 8-11 months in bulls), testosterone drives the active separation of these tissues. A persistent frenulum occurs when a band of collagenous connective tissue fails to rupture, leaving the ventral glans penis bound to the prepuce. At erection, the bound tissue acts as a tether, pulling the penis downward in a ventral arc ('rainbow' penis) that makes natural service impossible.",
        "Why_Not": "A short penile shaft causes inability to protrude (phimosis), but not focal ventral curvature. Penile hematoma results from rupture of the tunica albuginea, causing a swelling cranial to the scrotum, not a congenital tether.",
        "Wow_Approach": "Surgical correction: under local infiltration (or pudendal nerve block), exteriorize the penis, clamp the persistent frenulum close to the glans and prepuce, cut the tissue band, and place a single absorbable suture at the mucosal edges. The bull can return to service in 3-4 weeks."
    },
    848: {
        "topic": "Semen Terminology - Asthenozoospermia and Teratozoospermia",
        "Core_Anatomy": "Sperm mitochondria (middle piece), flagellum, and plasma membrane.",
        "Pathogenesis_Immediate": "The scientific terminology used to denote reduced or sub-optimal sperm motility in an ejaculate is Asthenozoospermia.",
        "Pathogenesis_Deep": "Comparative semen pathology terms: (1) Asthenozoospermia: <30% progressive motility. (2) Oligozoospermia: abnormally low sperm concentration (sperm count). (3) Teratozoospermia: high percentage of morphologically abnormal sperm (>30% abnormal). (4) Azoospermia: complete absence of spermatozoa in the ejaculate. (5) Aspermia: complete lack of ejaculate volume (failure of emission/ejaculation). Asthenozoospermia is often associated with mitochondrial damage in the middle piece or structural defects in the axoneme (flagellum).",
        "Why_Not": "Oligozoospermia relates to sperm count, not motility. Hypospermia relates to abnormally low ejaculate volume. Teratozoospermia relates to morphologic defects.",
        "Wow_Approach": "To diagnose asthenozoospermia accurately, perform Computer-Assisted Sperm Analysis (CASA). CASA measures specific kinetic parameters: VAP (average path velocity), VSL (straight-line velocity), and ALH (amplitude of lateral head displacement), delivering objective motility scores."
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
