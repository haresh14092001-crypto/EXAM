import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1072: {
        "topic": "Discovery of Spermatozoa - Leeuwenhoek (Repeated MCQ)",
        "Core_Anatomy": "Sperm head and tail under micro-optics.",
        "Pathogenesis_Immediate": "Spermatozoa were first discovered and described by the Dutch microscopist Antonie van Leeuwenhoek in 1677, using his hand-crafted microscopes.",
        "Pathogenesis_Deep": "Leeuwenhoek described these moving cells in semen as 'animalcules' (little animals), documenting their head and tail structure. This proved that semen was a cellular suspension rather than a homogeneous fluid, initiating the study of reproductive biology.",
        "Why_Not": "Salisbury and Lagerlof are famous 20th-century veterinary andrologists who established semen cryopreservation and pathology standards. Heape (1890) performed the first successful embryo transfer in rabbits.",
        "Wow_Approach": "Leeuwenhoek originally hypothesized that the sperm head contained a fully formed, pre-packaged miniature organism ('homunculus') that simply expanded inside the female uterus."
    },
    1073: {
        "topic": "Canine Testicular Descent - Post-Natal Completion (Repeated MCQ)",
        "Core_Anatomy": "Inguinal canal, vaginal process, gubernaculum testis, and the scrotum.",
        "Pathogenesis_Immediate": "The complete descent of both testes into the scrotum in the Dog typically takes place at 30 to 40 days after birth (post-natally).",
        "Pathogenesis_Deep": "testicular descent in dogs involves transabdominal migration in utero, inguinal passage shortly after birth (Days 2-5), and scrotal entry completed by Day 40 under testosterone-driven gubernaculum regression. A dog is clinically cryptorchid if both testes are not in the scrotum by 6 months.",
        "Why_Not": "In bulls, rams, and stallions, testicular descent is completed in utero before birth. Only in dogs and tomcats is the descent completed post-natally.",
        "Wow_Approach": "To differentiate retractile testes from cryptorchidism in young puppies, avoid a final diagnosis before 6 months of age, as stress can cause the cremaster muscle to retract the testes."
    },
    1074: {
        "topic": "Dag Defect - Midpiece and Tail Genetic Abnormality (Repeated MCQ)",
        "Core_Anatomy": "Sperm axoneme, outer dense fibers, and the mitochondrial sheath.",
        "Pathogenesis_Immediate": "The 'Dag defect' is a severe, hereditary morphological abnormality of spermatozoa characterized by splitting, tight coiling, or folding of the Midpiece and Tail.",
        "Pathogenesis_Deep": "The Dag defect is a genetic (autosomal recessive) condition in Jersey bulls. It involves complete deletion of the central pair of microtubules (9+0) in the axoneme and disorganization of the mitochondrial sheath, causing complete loss of progressive motility and sterility.",
        "Why_Not": "The acrosome and nuclear cap are head structures. The Dag defect is strictly a structural axonemal defect of the midpiece and tail, leaving the sperm head morphology entirely normal under light microscopy.",
        "Wow_Approach": "Under eosin-nigrosin staining, Dag-defective sperm appear as tightly coiled structures. Because it is a genetic deletion, it cannot be treated, and affected bulls must be culled."
    },
    1076: {
        "topic": "Benign Prostatic Hyperplasia Therapy - Castration (Repeated MCQ)",
        "Core_Anatomy": "Canine prostate gland and Leydig cells.",
        "Pathogenesis_Immediate": "The absolute most effective, definitive treatment for Benign Prostatic Hyperplasia (BPH) in the dog is bilateral Castration.",
        "Pathogenesis_Deep": "BPH is driven by Dihydrotestosterone (DHT) converted from testosterone in the prostate. Castration removes the testicular Leydig cells (the primary source of testosterone), causing the prostate to atrophy rapidly (shrinking by >70% in 4-6 weeks) and completely resolving clinical signs.",
        "Why_Not": "Vasectomy only cuts the vas deferens, leaving testosterone levels intact, which has zero effect on BPH. Drugs like Finasteride are effective but require lifelong daily therapy.",
        "Wow_Approach": "Castration remains the absolute gold standard for pet dogs, as it also eliminates the risk of future prostatic abscesses, perineal hernias, and testicular tumors."
    },
    1080: {
        "topic": "Semen Packaging Standards - French Mini Straw (Repeated MCQ)",
        "Core_Anatomy": "Sperm cell density and cryogenic storage.",
        "Pathogenesis_Immediate": "The most widely used and popular semen packaging straw across the globe is the French Mini Straw (0.25 ml).",
        "Pathogenesis_Deep": "The 0.25 ml French mini straw is the global standard because it occupies half the cryogenic storage space of medium straws and its smaller diameter ensures a highly uniform freezing and thawing rate, improving post-thaw progressive motility by 5-10%.",
        "Why_Not": "French medium straws (0.5 ml) require double the storage space. Pellets are frozen directly on dry ice without straws, which are difficult to label and automate.",
        "Wow_Approach": "French mini straws require specialized universal AI guns. The clinician must ensure the straw is loaded with the polyvinyl alcohol (PVA) plug facing backward."
    },
    1088: {
        "topic": "Functions of the Epididymis - Maturation and Storage (Repeated)",
        "Core_Anatomy": "Caput, corpus, and cauda epididymis.",
        "Pathogenesis_Immediate": "The four primary physiological functions of the epididymis are: Transport of sperm, Concentration of sperm, Maturation of sperm, and Storage of mature sperm.",
        "Pathogenesis_Deep": "Each region of the epididymis is highly specialized: (1) Transport: sperm are moved via hydrostatic pressure and peristaltic contractions. (2) Concentration: the caput absorbs >90% of the testicular fluid. (3) Maturation: in the corpus, sperm acquire progressive motility and fertilizing capacity. (4) Storage: the cauda serves as the primary reservoir, keeping sperm quiescent in a cool, low-pH environment.",
        "Why_Not": "The epididymis does not produce spermatozoa (which is strictly a testicular function of the seminiferous tubules) or secrete seminal plasma proteins associated with the accessory glands.",
        "Wow_Approach": "Seminal plasma L-carnitine is synthesized exclusively by the epididymis; its absence in semen confirms complete bilateral epididymal blockage."
    },
    1091: {
        "topic": "Structure of the Epididymis - Anatomical Segments (Repeated)",
        "Core_Anatomy": "Caput epididymis, corpus epididymis, cauda epididymis, and efferent ductules.",
        "Pathogenesis_Immediate": "The epididymis is an elongated, single highly convoluted duct divided anatomically into three segments: Caput (head), Corpus (body), and Cauda (tail).",
        "Pathogenesis_Deep": "The anatomical structures are highly distinct: (1) Caput (head): closely adhered to the dorsal pole of the testis. (2) Corpus (body): runs down the posterolateral border of the testis, serving as the site of intensive cellular maturation. (3) Cauda (tail): a prominent, bulbous structure at the ventral pole of the testis, transitioning directly into the vas deferens.",
        "Why_Not": "The vas deferens is the exit duct, not a segment of the epididymis. The efferent ducts connect the rete testis to the caput, serving as the anatomical transition rather than an epididymal segment.",
        "Wow_Approach": "Palpate the cauda epididymis: a soft, flabby, or enlarged cauda indicates Brucella ovis infection (infectious epididymitis), which causes severe fibrosis and obstruction."
    },
    1093: {
        "topic": "Seasonal Breeding in Males - Photoperiodic Regulation (Repeated)",
        "Core_Anatomy": "Retinohypothalamic tract, pineal gland, and the HPT axis.",
        "Pathogenesis_Immediate": "Breeding season in males of seasonal species (rams, stallions, bucks) is characterized by seasonal changes in testicular size, spermatogenic output, and libido, regulated by photoperiod and pineal melatonin.",
        "Pathogenesis_Deep": "The seasonal male reproductive cycle mirrors the female: (1) In seasonal short-day males (rams, bucks), decreasing day length in autumn triggers prolonged melatonin secretion, which stimulates pulsatile GnRH, LH, and FSH release. This leads to testicular hypertrophy, maximum daily sperm production, high testosterone, and intense libido (the 'rut'). (2) In seasonal long-day males (stallions), increasing day length in spring suppresses melatonin, removing HPT axis inhibition to maximize fertility.",
        "Why_Not": "Bulls, boars, and stud dogs are year-round (continuous) breeders and do not undergo complete seasonal testicular regression, although high ambient summer temperatures can temporarily reduce semen quality.",
        "Wow_Approach": "To induce out-of-season breeding in a flock of sheep: expose the rams to melatonin implants or artificial photoperiods alongside the ewes."
    },
    1100: {
        "topic": "Factors Affecting Semen Quality - Environmental Drivers (Repeated)",
        "Core_Anatomy": "Testicular parenchyma, seminiferous tubules, and epididymal duct.",
        "Pathogenesis_Immediate": "The primary factors affecting semen quality in domestic animals are: Ambient temperature (heat stress), Nutrition (energy/protein/trace minerals), Frequency of collection (overuse), Age, and Systemic diseases.",
        "Pathogenesis_Deep": "Each factor acts via specific pathways: (1) Heat stress (due to fever or high ambient temp) disrupts testicular thermoregulation, causing apoptosis of primary spermatocytes and high morphologic defects (primary abnormalities). (2) Overuse (too frequent semen collection) depletes cauda epididymal stores, leading to low sperm concentration and a high percentage of immature sperm with distal cytoplasmic droplets. (3) Zinc and Selenium deficiencies impair sperm membrane stability and chromatin condensation.",
        "Why_Not": "Minor changes in exercise or light do not directly alter semen quality in year-round breeders like bulls, but severe thermal, nutritional, or collection frequency shocks will immediately crash fertility parameters.",
        "Wow_Approach": "Because spermatogenesis requires ~61 days in the bull, a febrile episode (e.g., due to an injection or subclinical infection) two months ago is the typical cause of current poor semen parameters."
    },
    1101: {
        "topic": "VGO-II Subject Syllabus - Male Fertility and Parturition (Repeated)",
        "Core_Anatomy": "Comparative male and female reproductive tracts.",
        "Pathogenesis_Immediate": "VGO-II provides the theoretical and practical framework for managing male breeding soundness, semen preservation, and obstetrical emergencies.",
        "Pathogenesis_Deep": "Key components involve: (1) Breeding Soundness Evaluation (BSE) in bulls and stallions (measuring scrotal circumference, libido, progressive motility, morphology). (2) Diluent formulation (tris-citric-egg yolk, skim milk) and cryoprotectants (glycerol). (3) Dystocia correction protocols (manipulation of head, neck, and limb flexions, fetotomy wire technique, and epidural anesthesia). (4) Retained Fetal Membranes (RFM) and uterine prolapse therapeutics.",
        "Why_Not": "The study of silent heat, cystic ovaries, and early embryonic death is the domain of VGO-I, whereas VGO-II begins at the level of the mature male gamete and the late-stage gravid female.",
        "Wow_Approach": "In the obstetrical clinic, always apply the 'rule of two: check for the presence of two joints (fetlock and carpus/hock) and ensure they flex in the correct direction to distinguish anterior (forelimb) from posterior (hindlimb) presentation before applying traction."
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
