import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    986: {
        "topic": "Seasonal Breeding in Males - Photoperiodic Regulation",
        "Core_Anatomy": "Retinohypothalamic tract, pineal gland, and the hypothalamic-pituitary-testicular (HPT) axis.",
        "Pathogenesis_Immediate": "Breeding season in males of seasonal species (rams, stallions, bucks) is characterized by seasonal changes in testicular size, spermatogenic output, and libido, regulated by photoperiod and pineal melatonin.",
        "Pathogenesis_Deep": "The seasonal male reproductive cycle mirrors the female: (1) In seasonal short-day males (rams, bucks), decreasing day length in autumn triggers prolonged melatonin secretion, which stimulates pulsatile GnRH, LH, and FSH release. This leads to testicular hypertrophy, maximum daily sperm production, high testosterone, and intense libido (the 'rut'). (2) In seasonal long-day males (stallions), increasing day length in spring suppresses melatonin, removing HPT axis inhibition to maximize fertility.",
        "Why_Not": "Bulls, boars, and stud dogs are year-round (continuous) breeders and do not undergo complete seasonal testicular regression, although high ambient summer temperatures can temporarily reduce semen quality.",
        "Wow_Approach": "To induce out-of-season breeding in a flock of sheep: expose the rams to melatonin implants or artificial photoperiods alongside the ewes. This ensures that when the ewes are induced to cycle, the rams possess optimal sperm concentration, progressive motility, and strong libido to achieve high conception rates."
    },
    994: {
        "topic": "Factors Affecting Semen Quality - Environmental and Systemic Drivers",
        "Core_Anatomy": "Testicular parenchyma, seminiferous tubules, and epididymal duct.",
        "Pathogenesis_Immediate": "The primary factors affecting semen quality in domestic animals are: Ambient temperature (heat stress), Nutrition (energy/protein/trace minerals), Frequency of collection (overuse), Age, and Systemic diseases.",
        "Pathogenesis_Deep": "Each factor acts via specific pathways: (1) Heat stress (due to fever or high ambient temp) disrupts testicular thermoregulation, causing apoptosis of primary spermatocytes and high morphologic defects (primary abnormalities). (2) Overuse (too frequent semen collection) depletes cauda epididymal stores, leading to low sperm concentration and a high percentage of immature sperm with distal cytoplasmic droplets. (3) Zinc and Selenium deficiencies impair sperm membrane stability and chromatin condensation.",
        "Why_Not": "Minor changes in exercise or light do not directly alter semen quality in year-round breeders like bulls, but severe thermal, nutritional, or collection frequency shocks will immediately crash fertility parameters.",
        "Wow_Approach": "When assessing a sudden drop in bull semen quality: always check the farm treatment records from 60 days prior. Because spermatogenesis requires ~61 days in the bull, a febrile episode (e.g., due to an injection or subclinical infection) two months ago is the typical cause of current poor semen parameters."
    },
    998: {
        "topic": "VGO-II Core Study - Obstetrics and Male Reproduction Overview",
        "Core_Anatomy": "Comparative male and female reproductive tracts.",
        "Pathogenesis_Immediate": "VGO-II is gynaecology's sister course, providing standard clinical instructions on male breeding soundness (Andrology) and obstetrical emergencies (dystocia, fetotomy, uterine prolapse).",
        "Pathogenesis_Deep": "The gynaecological curriculum requires complete integration of: (1) Testicular and accessory gland physiology. (2) Semen preservation chemistry. (3) Parturition mechanics (endocrine induction via fetal ACTH and cortisol). (4) Dystocia resolution (mutation, traction, fetotomy, caesarean). It is the definitive clinical framework for field veterinary gynaecologists.",
        "Why_Not": "Female oestrous cycles, non-pregnant diagnostics, and artificial insemination logistics are taught in VGO-I, while VGO-II focuses strictly on mature male fertility and periparturient female gynaecology.",
        "Wow_Approach": "In clinical practice, treat Andrology and Obstetrics as the beginning and end of the reproductive production line: Andrology ensures high-quality genetics are successfully seeded, while Obstetrics ensures the viable harvest of the fetus at term."
    },
    1000: {
        "topic": "VGO-511 Andrology Objective parameters",
        "Core_Anatomy": "Testicular and accessory sex gland compartment.",
        "Pathogenesis_Immediate": "This objective paper tests exact quantitative constants: duration of spermatogenesis, sperm production rates, sperm enzyme sites, and standard semen freezing parameters.",
        "Pathogenesis_Deep": "Key parameters tested: Flehmen's reflex is absent in boars; semen riboflavin causes yellowing; pampiniform counter-current heat exchange; optimal vapor freeze grill height is 4 cm. Precise recall of these values is tested to build diagnostic speed and prevent cryopreservation errors.",
        "Why_Not": "Subjective questions evaluate clinical or surgical techniques, while the objective section focuses exclusively on these biological and mechanical constants.",
        "Wow_Approach": "Compile a comparison matrix of sperm biology values (e.g., bull 61 days spermatogenesis, ram 49 days, boar 34 days) to quickly eliminate distractors in multiple-choice exams."
    },
    1001: {
        "topic": "Flehmen's Reflex - Absence in the Boar",
        "Core_Anatomy": "Vomeronasal organ (VNO), nasopalatine ducts, and the olfactory bulb.",
        "Pathogenesis_Immediate": "The Flehmen's reflex (curling of the upper lip to facilitate pheromone transport to the vomeronasal organ) is observed in bulls, rams, stallions, and bucks, but is completely absent in the Boar.",
        "Pathogenesis_Deep": "The Flehmen's reflex is a sensory behavioral display: (1) The male investigates female urine or vaginal discharge. (2) He curls his upper lip and inhales, closing the nostrils. (3) This creates a negative pressure that draws the fluid/pheromones through the nasopalatine ducts into the Vomeronasal Organ (VNO), which analyzes the non-volatile pheromones to detect oestrus. Boars do not display Flehmen because their vomeronasal organ is structurally different, and they rely instead on direct tactile snout-to-snout contact and salivary pheromones (androstenone) to assess female receptivity.",
        "Why_Not": "Bulls, stallions, rams, and bucks are classic exhibitors of the Flehmen reflex, using it as their primary olfactory tool to verify standing heat in females.",
        "Wow_Approach": "To trigger Flehmen in a breeding stallion: present a cloth soaked in estrous mare urine. The stallion will immediately lift his head, curl his upper lip, and remain rigid for 10-15 seconds, confirming active olfactory processing through the VNO."
    },
    1018: {
        "topic": "VGO Andrology MCQ - Diagnostic Case Solving",
        "Core_Anatomy": "Comparative male reproductive anatomy.",
        "Pathogenesis_Immediate": "This MCQ section evaluates clinical problem-solving: identifying the causes of impotence, specific hormone therapies for BPH, acrosomal origins, and semen cryopreservation physics.",
        "Pathogenesis_Deep": "Topics include: (1) Impotentia coeundi (inability to copulate, e.g., due to gonitis or persistent frenulum). (2) Acrosome origin from the Golgi apparatus during spermiogenesis. (3) BPH treatment using 5-alpha-reductase inhibitors or castration. (4) Sperm membrane protection using egg yolk extenders.",
        "Why_Not": "Descriptive essays allow for general explanations, whereas the MCQ section demands precise, singular correct answers to verify diagnostic accuracy in clinical veterinary medicine.",
        "Wow_Approach": "When answering MCQs on impotence: always distinguish 'impotentia coeundi' (mechanical/behavioral mounting failure) from 'impotentia generandi' (normal copulation but poor semen quality leading to fertilization failure). This distinction dictates the prognosis."
    },
    1019: {
        "topic": "Gonitis - Stifle Joint Inflammation in Bulls (Repeated MCQ)",
        "Core_Anatomy": "Stifle joint, joint capsule, femoropatellar and femorotibial joint compartments.",
        "Pathogenesis_Immediate": "Gonitis is the clinical term for the distention, inflammation, and pathological enlargement of the Stifle joint capsule, leading to severe hindlimb lameness in breeding bulls.",
        "Pathogenesis_Deep": "The stifle joint is the primary weight-bearing joint during mounting. During natural mating, a bull must rear up and support his entire massive body weight on his hindlimbs. Gonitis causes severe pain and mechanical instability of the stifle joint, preventing the bull from mounting females or artificial vaginas. It is a major cause of secondary impotentia coeundi.",
        "Why_Not": "Gonitis does not involve the shoulder joint (forelimb), hip joint (coxofemoral), or knee joint (carpus). It is strictly localized to the stifle joint.",
        "Wow_Approach": "A breeding bull with gonitis should be placed on immediate, complete sexual rest for at least 4-8 weeks, supplemented with systemic NSAIDs (e.g., Flunixin Meglumine) and soft bedding to prevent joint capsule fibrosis."
    },
    1020: {
        "topic": "Buck Seminal Plasma - Cowper's Gland EYCE Secretion (Repeated MCQ)",
        "Core_Anatomy": "Caprine bulbourethral (Cowper's) glands, pelvic urethra, and semen.",
        "Pathogenesis_Immediate": "The Bulbourethral (Cowper's) gland in the buck secretes Egg Yolk Coagulating Enzyme (EYCE / phospholipase A2) into the seminal plasma, which causes severe toxicity in egg yolk extenders.",
        "Pathogenesis_Deep": "EYCE reacts with lecithin in egg yolk to produce lysolecithin, a highly toxic surfactant that lyses sperm cell membranes. Because the bulbourethral gland is the sole source of this enzyme, buck semen must either be washed by centrifugation to remove seminal plasma or diluted in alternative extenders (like skim milk or soy lecithin).",
        "Why_Not": "The prostate gland, seminal vesicles, and ampullary glands do not synthesize or secrete EYCE, having no direct role in egg yolk coagulation in goats.",
        "Wow_Approach": "Using skim milk extenders is the most cost-effective field method for freezing buck semen, as casein micelles in milk naturally bind and block EYCE, bypassing the need for centrifugation which can damage fragile sperm membranes."
    },
    1021: {
        "topic": "Semen Cryopreservation - Vapor Freezing Grill Height (Repeated MCQ)",
        "Core_Anatomy": "Semen straws, liquid nitrogen vapor, and freezing rack.",
        "Pathogenesis_Immediate": "During the deep-freezing of semen, the optimal distance between the liquid nitrogen level and the straw rack is 4 cm to achieve a uniform cooling rate of -10°C to -20°C/min.",
        "Pathogenesis_Deep": "At 4 cm above the liquid nitrogen level, the vapor phase temperature is stable between -80°C and -120°C. Exposing the semen straws on the rack at this height for 7-10 minutes allows optimal dehydration of sperm cells, preventing the lethal formation of intracellular ice crystals before final plunging into liquid nitrogen (-196°C).",
        "Why_Not": "Placing straws at 10 cm is too warm and slows the freezing rate, causing osmotic cell death. Placing straws directly on the liquid (<1 cm) causes instantaneous, uneven freezing that traps water inside, rupturing membranes.",
        "Wow_Approach": "To ensure maximum quality, use a digital thermocouple to verify that the rack temperature is exactly -120°C. Plunge the straws rapidly into the liquid nitrogen after exactly 9 minutes of vapor exposure."
    },
    1022: {
        "topic": "Impotentia Coeundi - Inability to Copulate",
        "Core_Anatomy": "Sigmoid flexure, dorsal apical ligament, stifle joints, and prepuce.",
        "Pathogenesis_Immediate": "A reduced to complete lack of sexual desire (libido) or mechanical ability to copulate (mount and achieve intromission) in the male is defined clinically as Impotentia Coeundi.",
        "Pathogenesis_Deep": "Male breeding failure is divided into two primary clinical syndromes: (1) Impotentia coeundi: the bull/stallion is unable to physically perform the act of copulation. Causes include: poor libido, musculoskeletal pain (gonitis, spondylosis), penile deviation (persistent frenulum, corkscrew penis), prepuce injury, or penile hematoma. (2) Impotentia generandi: the male copulates normally, but fertilizing capacity is lost due to poor semen quality (azoospermia, high abnormalities).",
        "Why_Not": "Phimosis is a mechanical inability to protrude the penis from the prepuce, which is only one specific cause of impotentia coeundi. Impotentia generandi refers to fertilization failure, not copulation failure.",
        "Wow_Approach": "During breeding soundness evaluations, first verify potentia coeundi by observing the bull mount a teaser. If he mounts, achieves erection, thrusts, and retracts normally, he possesses potentia coeundi. Then, evaluate semen to assess potentia generandi."
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
