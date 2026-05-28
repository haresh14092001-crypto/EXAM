import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    849: {
        "topic": "Andrology Fill-In - Spermatogenic Dynamics and Semen Preservation",
        "Core_Anatomy": "Testicular parenchyma, seminiferous epithelium, and sperm storage compartments.",
        "Pathogenesis_Immediate": "Key Andrology fill-in parameters: The primary intracellular cryoprotectant used in freezing is Glycerol; the site of sperm maturation is the Epididymis; the yellow color of bull semen is due to Riboflavin; semen diluent buffer standard is Tris-Citric-Egg Yolk.",
        "Pathogenesis_Deep": "These fill-ins test core physical and biochemical parameters: (1) Glycerol protects sperm by binding water molecules, preventing intracellular ice crystal formation that would lacerate membranes. (2) Riboflavin (Vitamin B2) secreted by the seminal vesicles is responsible for the normal yellowish tinge of bull semen, which must be distinguished from purulent or urine-contaminated yellowing. (3) The epididymis provides the specialized microenvironment (low pH, high K⁺, proteins) where sperm acquire motility.",
        "Why_Not": "Intracellular cryoprotectants must penetrate the sperm membrane (like glycerol or DMSO), whereas extracellular cryoprotectants (like egg yolk or milk proteins) remain outside, protecting against cold shock. Confusing these two classes of protective agents leads to poor cryo-survival.",
        "Wow_Approach": "To formulate a standard Tris-Citric-Egg Yolk extender: combine Tris (hydroxymethyl) aminomethane (buffer), citric acid (pH adjuster), fructose (energy source), 20% egg yolk (cold shock protection), and 7% glycerol (cryoprotectant), maintaining pH at 6.8 and osmolarity at 300 mOsm/L."
    },
    854: {
        "topic": "Andrology Matching - Male Reproductive Structures and Pathology",
        "Core_Anatomy": "Comparative male reproductive systems across species.",
        "Pathogenesis_Immediate": "Key matching pairs in Andrology: Boar matches to the preputial diverticulum; Stallion matches to vascular penis; Cavernous bodies match to erection of penis; Artificial Vagina matches to thermal/mechanical semen collection stimulation; Benign Prostatic Hyperplasia matches to Dihydrotestosterone.",
        "Pathogenesis_Deep": "These pairs cover male reproductive adaptations: (1) The boar possesses a preputial diverticulum, a dorsal pouch that accumulates urine and degenerated cells, producing the characteristic foul odor of boars. (2) The stallion has a vascular penis with highly distensible cavernous tissue, which increases massively in length and diameter during erection. (3) BPH in older dogs is driven by DHT (dihydrotestosterone), which stimulates glandular cell hypertrophy.",
        "Why_Not": "Ruminants (bulls, rams) have a fibroelastic penis with a sigmoid flexure that does not increase in diameter during erection, relying on the retractor penis muscle. Prostatitis is marked by white blood cells in semen, not by vascular penis changes.",
        "Wow_Approach": "During breeding soundness exams in boars: the preputial diverticulum must be regularly checked for accumulation of fluid or calculi, which can harbor pathogens like Pseudomonas or Actinobacillus. Emptying the diverticulum manually before natural mating reduces bacterial contamination of the sow."
    },
    855: {
        "topic": "Stallion Reproduction - Vascular Penis and Semen Ejaculation",
        "Core_Anatomy": "Equine glans penis, corpus cavernosum, and corpus spongiosum.",
        "Pathogenesis_Immediate": "The Stallion possesses a vascular (musculocavernous) penis characterized by large blood-filled cavernous spaces that expand dramatically in both length and diameter during erection, and ejaculates a large volume of semen (50-150 ml) directly into the cervix.",
        "Pathogenesis_Deep": "In the musculocavernous penis of the stallion: (1) The corpus cavernosum contains highly distensible trabecular spaces. (2) During erection, parasympathetic-mediated nitric oxide release induces vasodilation of the helicine arteries, flooding the cavernous spaces with blood and compressing the venous outflow, causing a massive increase in volume. (3) Ejaculation is multi-phasic: the sperm-rich fraction is expelled in 5-8 jets directly through the dilated cervix into the uterine body, followed by a gel-like fraction from the seminal vesicles that seals the cervix.",
        "Why_Not": "Bulls, rams, and boars have a fibroelastic penis containing minimal cavernous space and a rigid connective tissue sheath; their erection involves straightening the sigmoid flexure without an increase in diameter. Sows have a long, twisted cervix that accommodates the corkscrew boar penis.",
        "Wow_Approach": "Because the stallion ejaculates directly into the uterine body, equine AI requires depositing the semen transcervically. If using frozen semen, deposit the dose deep in the uterine horn on the side of the ovulating follicle using a flexible pipet to maximize fertility."
    },
    856: {
        "topic": "Sperm Morphology - Detached Heads as Secondary Defects",
        "Core_Anatomy": "Sperm head, implantation fossa, capitulum, and flagellum.",
        "Pathogenesis_Immediate": "A detached head (separation of the sperm head from the tail) is classified as a secondary sperm abnormality, arising primarily during epididymal transit or sample collection/handling.",
        "Pathogenesis_Deep": "Sperm morphological defects are divided into: (1) Primary abnormalities: arise during active spermatogenesis in the testes (e.g., pyriform heads, double heads, microcephalic heads, tight coiled tails). (2) Secondary abnormalities: arise after sperm leave the seminiferous tubules, during transit through the epididymis or during handling (e.g., detached heads, distal droplets, bent tails). (3) Tertiary abnormalities: arise due to cold shock or osmotic stress post-collection. Detached heads occur due to fragility at the capitulum (implantation fossa) where the tail attaches to the head, often triggered by rough handling, agitation, or temperature shocks during semen processing.",
        "Why_Not": "Primary defects indicate severe testicular dysfunction or degeneration, whereas secondary defects are often manageable by improving semen handling techniques, reducing collection frequency, or treating epididymal sub-acute inflammation.",
        "Wow_Approach": "To determine if detached heads are pathological: perform a differential morphologic count on 200 sperms stained with eosin-nigrosin. A detached head count >20% indicates 'decapitated sperm defect' (a genetic fragility of the basal plate seen in Hereford bulls) or severe chronic epididymitis, both causing sterility."
    },
    857: {
        "topic": "Corpora Cavernosa - Erection Mechanics in Males",
        "Core_Anatomy": "Corpus cavernosum (bilateral dorsal erectile bodies), corpus spongiosum (ventral body surrounding the urethra), and the tunica albuginea.",
        "Pathogenesis_Immediate": "The corpora cavernosa (cavernous bodies) are the main erectile tissue structures of the penis, responsible for providing the mechanical rigidity and expansion required for Erection and copulation.",
        "Pathogenesis_Deep": "Erection physiology: (1) Sensory or psychic stimuli trigger parasympathetic signals via the pelvic nerve. (2) Non-adrenergic non-cholinergic (NANC) nerve endings release nitric oxide (NO). (3) NO activates guanylyl cyclase in the vascular smooth muscle, increasing cGMP, which drives calcium uptake and arterial relaxation. (4) In vascular penises, blood floods the cavernous bodies, expanding the tissue. In fibroelastic penises, the blood fills the cavernous spaces under extremely high pressure (>1,000 mmHg), which overcomes the retractor penis muscle tension, straightening the sigmoid flexure.",
        "Why_Not": "The corpus spongiosum is less distensible and serves to keep the urethral lumen open during ejaculation, whereas the corpora cavernosa are high-pressure vascular compartments specifically designed for mechanical rigidity.",
        "Wow_Approach": "In the bull, the dorsal canal of the corpus cavernosum penis is the site where venous occlusion occurs during erection. Rupture of the thick tunica albuginea surrounding the cavernous bodies under the extreme pressure of mounting causes 'penile hematoma' ('broken penis'), a major breeding emergency."
    },
    858: {
        "topic": "Artificial Vagina - Thermal and Mechanical Stimulation",
        "Core_Anatomy": "Bovine, equine, or porcine external genitalia and the pelvic urethra.",
        "Pathogenesis_Immediate": "The Artificial Vagina (AV) is the standard device used for semen collection, designed to mimic the natural vagina by providing the optimal combination of temperature (thermal) and pressure (mechanical) stimulation.",
        "Pathogenesis_Deep": "Semen collection using an AV requires careful calibration: (1) Temperature: must be maintained at 42-45°C for bulls, 45-48°C for stallions, and 38-40°C for boars. (2) Pressure: achieved by blowing air into the double-walled jacket. The warmth and mechanical pressure on the glans penis trigger the spinal ejaculation reflex (pudendal nerve pathway), inducing rapid emission and ejaculation into a graduated tube. If the AV is too cold (<40°C for bulls), the bull will refuse to ejaculate; if too hot (>50°C), it causes severe thermal injury and sperm shock.",
        "Why_Not": "Electroejaculation uses electrical stimulation of the pelvic sympathetic and parasympathetic nerves, bypasses the need for libido or physical mount, and is used when bulls are injured or wild. The AV is strictly a physiological simulator requiring a mount partner or dummy.",
        "Wow_Approach": "To ensure maximum semen quality and volume from a bull: perform 'active preparation'. Allow the bull to make two false mounts (mounting the teaser without intromission) and restrain him for 1 minute before collection. This triggers oxytocin release, increasing the sperm concentration per ejaculate by 40%."
    },
    860: {
        "topic": "Prostatitis - Leukocytospermia and Canine Prostatic Disease",
        "Core_Anatomy": "Canine prostate gland (encircling the proximal urethra), prostatic ducts, and semen.",
        "Pathogenesis_Immediate": "Prostatitis (inflammation of the prostate gland) is characterized clinically by the presence of abundant white blood cells (Leucocytes) in the semen (leukocytospermia) and is most common in older intact male dogs.",
        "Pathogenesis_Deep": "The prostate is the only accessory sex gland in the dog. Prostatitis often arises secondary to benign prostatic hyperplasia (BPH) when ascending bacteria (E. coli, Proteus, Staphylococcus) colonize the hyperplastic glandular tissue. The inflammation leads to: (1) Breakdown of the blood-prostate barrier. (2) Infiltration of neutrophils into the prostatic fluid. (3) Pain during ejaculation, hematuria, tenesmus (due to rectal compression), and infertility. Semen evaluation reveals a turbid, yellow-tinged third fraction containing >5-10 WBCs per high-power field.",
        "Why_Not": "Detached heads indicate a maturational or handling defect. Distal droplets indicate epididymal transit issues. Vascular penis changes relate to horse anatomy. Prostatitis is strictly an inflammatory infectious process presenting with white cells.",
        "Wow_Approach": "To diagnose canine prostatitis: collect the third fraction of the ejaculate (prostatic fraction) or perform a prostatic massage with fine-needle aspiration. Culturing the third fraction has a high diagnostic correlation with direct prostatic tissue biopsy, helping select the correct lipid-soluble antibiotic (e.g., Enrofloxacin or Trimethoprim-Sulfa) that can penetrate the blood-prostate barrier."
    },
    861: {
        "topic": "Semen Extenders - Preventing Sperm Agglutination",
        "Core_Anatomy": "Sperm membrane glycoproteins, head-to-head agglutination, and extender buffers.",
        "Pathogenesis_Immediate": "Semen extenders are formulated to dilute and preserve semen, containing specific proteins and buffers that prevent the head-to-head or tail-to-tail agglutination of spermatozoa during storage.",
        "Pathogenesis_Deep": "Sperm agglutination (clumping of cells) occurs due to: (1) Changes in the net negative surface charge of sperm membranes post-ejaculation. (2) Release of intracellular enzymes from damaged cells. (3) Presence of agglutinins in the seminal plasma. Extenders (specifically those containing tris, citric acid, and low concentrations of egg yolk or milk proteins) coat the sperm membrane, maintaining the negative membrane charge that keeps sperm repelled from one another. Extenders also provide: fructose (energy), sodium citrate (buffer), and antibiotics (tylosin, gentamicin, spectinomycin) to control pathogens.",
        "Why_Not": "Cryoprotectants (like glycerol) protect cells from freezing damage but do not prevent active room-temperature agglutination. Semen extenders serve primarily to preserve individual, free-swimming viability and prevent early cell clumping.",
        "Wow_Approach": "If head-to-head agglutination is observed under the microscope: check the pH and osmolarity of the extender. A drop in pH (<6.5) or hypertonic conditions will neutralize sperm surface charges, causing rapid clumping. Correct by replacing the extender batch."
    },
    862: {
        "topic": "Distal Cytoplasmic Droplet - Maturational Semen Defect",
        "Core_Anatomy": "Sperm midpiece, neck, cytoplasmic droplet, and epididymal cauda.",
        "Pathogenesis_Immediate": "The distal cytoplasmic droplet is a normal morphological structure of maturing sperm that should be shed during epididymal transit. Its persistence in ejaculated semen is classified as a maturational secondary defect.",
        "Pathogenesis_Deep": "During spermiogenesis in the testes, the developing spermatozoon retains a droplet of cytoplasm around its neck (proximal droplet). As the sperm travels through the caput and corpus epididymis, the droplet moves distally along the midpiece (distal droplet) and is normally shed into the cauda epididymis before ejaculation. The persistence of distal droplets on >15-20% of ejaculated sperm indicates: (1) Immature semen (overuse of the bull/stallion with rapid depletion of cauda stores). (2) Epididymal dysfunction (failure of the shedding mechanism).",
        "Why_Not": "Proximal cytoplasmic droplets (located at the neck) represent a more severe testicular maturational defect and are classified as primary abnormalities. Distal droplets represent a milder, epididymal transit issue and are secondary defects.",
        "Wow_Approach": "To correct high distal droplet percentages in a young stud bull: provide a 2-week sexual rest period. This allows cauda epididymal stores to replenish and ensures proper transit time, leading to normal cytoplasmic shedding and improved fertility on the subsequent collection."
    },
    863: {
        "topic": "Benign Prostatic Hyperplasia - Dihydrotestosterone (DHT) in Dogs",
        "Core_Anatomy": "Canine prostate gland, prostatic epithelial and stromal cells, and systemic androgen receptors.",
        "Pathogenesis_Immediate": "Benign Prostatic Hyperplasia (BPH) is a spontaneous, age-related condition in intact male dogs, driven by the active androgen Dihydrotestosterone (DHT).",
        "Pathogenesis_Deep": "BPH pathogenesis: (1) With aging, the ratio of estrogen to testosterone in the dog changes, sensitizing the prostatic cells to androgen stimulation. (2) Testosterone is converted to the more potent Dihydrotestosterone (DHT) by the enzyme 5-alpha-reductase inside the prostatic stromal and epithelial cells. (3) DHT binds androgen receptors, driving hyperplasia of the glandular epithelium and hypertrophy of the stroma. The prostate enlarges symmetrically, leading to tenesmus, hematuria, and ribbon-like feces.",
        "Why_Not": "BPH is not driven by estrogen alone (which causes squamous metaplasia, not hyperplasia) or progesterone. It is strictly a DHT-dependent process. BPH is benign; it is distinct from prostatic adenocarcinoma (which is highly malignant and not hormone-dependent).",
        "Wow_Approach": "Medical management of BPH: administer Finasteride (0.1-0.5 mg/kg orally once daily). Finasteride is a selective 5-alpha-reductase inhibitor that blocks the conversion of testosterone to DHT, causing the prostate to shrink by up to 50% within 4 weeks while preserving semen quality and fertility."
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
