import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    955: {
        "topic": "VGO-511 Andrology MCQ Section - Sperm Biology and Diagnostic Standards",
        "Core_Anatomy": "Male reproductive system and processing laboratory.",
        "Pathogenesis_Immediate": "The objective MCQ section of VGO-511 tests core biophysical constants of spermatozoa: enzyme locations (acrosome), optimal thawing temperatures (37°C), discovery history, testicular descent, and specific sperm defects.",
        "Pathogenesis_Deep": "These questions evaluate clinical knowledge of: (1) Sperm ultrastructure (the acrosomal cap containing proteolytic enzymes). (2) Cryobiology (thawing speed to prevent ice recrystallization). (3) Developmental biology (testicular descent timing). (4) Semen pathology (BPH therapies and packaging history).",
        "Why_Not": "These precise facts represent critical safety gates in AI centers; incorrect thawing or misdiagnosing BPH leads to direct herd fertility failures.",
        "Wow_Approach": "To ensure maximum academic success: structure study sheets by species, grouping testicular descent ages, normal semen volumes, and packaging parameters side-by-side."
    },
    956: {
        "topic": "Acrosomal Enzymes - Hyaluronidase and Acrosin in Sperm Head",
        "Core_Anatomy": "Sperm head, outer and inner acrosomal membranes, and the oocyte cumulus oophorus.",
        "Pathogenesis_Immediate": "Hyaluronidase enzyme is present in the sperm Head, specifically localized within the membrane-bound acrosomal vesicle (acrosome) covering the anterior two-thirds of the sperm nucleus.",
        "Pathogenesis_Deep": "The acrosome is a highly specialized lysosome-like organelle. Hyaluronidase is a key enzyme stored inside: (1) During the acrosome reaction, the outer acrosomal membrane fuses with the sperm plasma membrane. (2) Hyaluronidase is released by exocytosis. (3) It digests hyaluronic acid, the primary glycosaminoglycan matrix holding the follicular cells (cumulus oophorus) together around the oocyte. This allows the sperm to penetrate the cumulus mass and reach the zona pellucida, where the second acrosomal enzyme, acrosin, digests a path through the zona.",
        "Why_Not": "The midpiece contains mitochondria for energy production. The tail contains the axoneme (9+2 microtubule structure) for flagellar propulsion. Neither contains acrosomal enzymes like hyaluronidase.",
        "Wow_Approach": "Acrosomal Integrity Test: Stain a semen smear with Giemsa or Coomassie Blue. Intact acrosomes stain dark blue as a distinct cap on the sperm head. A high percentage of unstained or damaged heads (>15%) indicates acrosomal damage, rendering the sperm unable to digest the cumulus mass even if motile."
    },
    959: {
        "topic": "Semen Straw Thawing - Optimal 37°C Rapid Protocol",
        "Core_Anatomy": "Sperm membrane lipids, intracellular water, and thawing water bath.",
        "Pathogenesis_Immediate": "The optimal thawing temperature for a frozen semen straw (0.25 ml or 0.5 ml French straw) is 37°C (rapid thawing in a water bath for 30 seconds).",
        "Pathogenesis_Deep": "During thawing, sperm cells face severe recrystallization risk. If thawed slowly (e.g., at room temperature or 5°C), the micro-crystals of ice formed during freezing melt slowly and coalesce into larger, lethal ice crystals that lacerate the plasma and acrosomal membranes. Rapid thawing at 37°C for 30 seconds ensures the fastest transition through the critical recrystallization temperature zone (-60°C to 0°C), minimizing osmotic stress and maximizing the recovery of progressively motile sperm.",
        "Why_Not": "Thawing at 5°C is too slow and causes recrystallization. Thawing at 25°C is an intermediate rate that yields substandard motility. Thawing above 40°C is highly toxic, causing rapid heat denaturation of sperm proteins.",
        "Wow_Approach": "AMH/IETS Rule: Keep the thawing water bath at exactly 37°C. After removing the straw from liquid nitrogen with forceps, shake it rapidly to remove residual nitrogen, plunge it into the water bath for 30 seconds, wipe it completely dry (as water is highly spermicidal), cut the sealed tip, and load into the warm AI gun."
    },
    962: {
        "topic": "Discovery of Spermatozoa - Antonie van Leeuwenhoek (1677)",
        "Core_Anatomy": "Sperm head and flagellum under micro-optics.",
        "Pathogenesis_Immediate": "Spermatozoa were first discovered and described by the Dutch microscopist Antonie van Leeuwenhoek in 1677, using his hand-crafted high-power single-lens microscopes.",
        "Pathogenesis_Deep": "Leeuwenhoek examined canine, human, and rabbit semen, identifying billions of highly active, swimming microscopic structures which he named 'animalcules' (little animals). He described their distinct head and undulating tail movement, proving they were living biological units. This discovery laid the foundation for reproductive biology, although it took another two centuries to prove that a single 'animalcule' must fuse with an oocyte to achieve fertilization.",
        "Why_Not": "Salisbury and Lagerlof are famous 20th-century veterinary andrologists who established semen cryopreservation and pathology standards. Heape (1890) performed the first successful embryo transfer in rabbits, not the discovery of sperm.",
        "Wow_Approach": "Leeuwenhoek originally hypothesized that the sperm head contained a fully formed, pre-packaged miniature organism ('homunculus') that simply expanded inside the female uterus, a theory known as preformationism that dominated science for a century."
    },
    963: {
        "topic": "Canine Testicular Descent - Post-Natal Completion at 30-40 Days",
        "Core_Anatomy": "Inguinal canal, vaginal process, gubernaculum testis, and the scrotum.",
        "Pathogenesis_Immediate": "The complete descent of both testes into the scrotum in the Dog (puppy) typically takes place at 30 to 40 days after birth (post-natally), though they can be palpated near the inguinal ring by 10-14 days.",
        "Pathogenesis_Deep": "Testicular descent in dogs occurs in three distinct phases: (1) Transabdominal migration: occurs in utero, where the gubernaculum (mesenchymal cord) expands, anchoring the testis near the inguinal ring. (2) Inguinal passage: occurs shortly after birth (Days 2-5). (3) Scrotal entry: the gubernaculum undergoes regression and collagenization under testosterone influence, pulling the testis through the inguinal canal into the scrotum. The inguinal rings contract behind the testes by Day 40, finalizing scrotal positioning. A dog is clinically diagnosed as cryptorchid if both testes are not palpable in the scrotum by 6 months of age.",
        "Why_Not": "In bulls, rams, and stallions, testicular descent is completed in utero before birth, allowing them to be born with fully scrotal testes. Only in dogs and tomcats is the descent completed post-natally.",
        "Wow_Approach": "To differentiate a prepubertal normal puppy from a cryptorchid: do not make a final diagnosis before 6 months. High sympathetic stress during veterinary handling can cause the active cremaster muscle to temporarily retract the small testes back into the inguinal canal (retractile testes)."
    },
    964: {
        "topic": "Dag Defect - Genetic Sperm Midpiece and Tail Abnormality",
        "Core_Anatomy": "Sperm axoneme (microtubules), outer dense fibers, and the mitochondrial sheath.",
        "Pathogenesis_Immediate": "The 'Dag defect' is a severe, hereditary morphological abnormality of spermatozoa characterized by splitting, tight coiling, or folding of the Midpiece and Tail.",
        "Pathogenesis_Deep": "The Dag defect is a genetic (autosomal recessive) condition originally discovered in Jersey bulls (and named after the index bull 'Dag'). The defect involves: (1) Complete deletion or disruption of the central pair of microtubules (9+0 instead of 9+2) or outer dense fibers in the axoneme. (2) The mitochondrial sheath of the midpiece is disorganized and split. (3) The tail is tightly coiled or folded back on itself within the cell membrane. Ejaculates from affected bulls contain >70-80% Dag-defective sperm, presenting with extremely low progressive motility (asthenozoospermia) and causing complete sterility.",
        "Why_Not": "The acrosome and nuclear cap are head structures. The Dag defect is strictly a structural axonemal defect of the midpiece and tail, leaving the sperm head morphology entirely normal under light microscopy.",
        "Wow_Approach": "Under eosin-nigrosin staining, Dag-defective sperm appear as highly coiled structures resembling 'curly cues'. Because it is a genetic axonemal deletion, it cannot be treated, and affected bulls must be culled immediately to prevent spreading the recessive gene."
    },
    971: {
        "topic": "Benign Prostatic Hyperplasia Therapy - Castration as Gold Standard",
        "Core_Anatomy": "Canine prostate gland, Leydig cells, and systemic androgen receptors.",
        "Pathogenesis_Immediate": "The absolute most effective, definitive treatment for Benign Prostatic Hyperplasia (BPH) in the dog is bilateral Castration (orchiectomy).",
        "Pathogenesis_Deep": "BPH is a 100% testosterone (specifically Dihydrotestosterone / DHT) dependent process. Testosterone produced by the Leydig cells is converted to DHT inside the prostate. DHT drives glandular hypertrophy. Performing a bilateral castration removes the primary source of testosterone (95% reduction in systemic levels). Within 7-10 days post-castration, the prostate begins to atrophy rapidly; by 4-6 weeks, the gland shrinks by >70% to an infantile size, completely resolving clinical signs like tenesmus and hematuria.",
        "Why_Not": "Vasectomy only cuts the vas deferens to prevent sperm transit, leaving the Leydig cells and testosterone secretion completely intact, which has zero effect on BPH. Medical drugs (like Finasteride) are effective but require lifelong daily therapy, making castration the definitive clinical choice.",
        "Wow_Approach": "For valuable stud dogs where fertility must be preserved: use Finasteride (5-alpha-reductase inhibitor) or Deslorelin (GnRH implant). Castration remains the absolute gold standard for pet dogs, as it also eliminates the risk of future prostatic abscesses, perineal hernias, and testicular tumors."
    },
    975: {
        "topic": "Semen Packaging Standards - The French Mini Straw (0.25 ml)",
        "Core_Anatomy": "Sperm cell density, extender volume, and cryogenic storage rack.",
        "Pathogenesis_Immediate": "The most widely used and popular semen packaging straw across the globe is the French Mini Straw (0.25 ml).",
        "Pathogenesis_Deep": "Semen straws are manufactured in two standard French sizes: (1) French Medium (0.5 ml): historically popular, but requires more storage space. (2) French Mini (0.25 ml): today's global standard. The mini straw is highly preferred because: (1) It occupies half the cryogenic storage space, allowing liquid nitrogen tanks to hold double the number of doses. (2) The smaller diameter ensures a highly uniform freezing and thawing rate across the entire cross-section of the straw, reducing thermal shock and improving post-thaw progressive motility by 5-10% compared to medium straws.",
        "Why_Not": "French medium straws are still used for certain horse or dog semen doses but have been largely replaced by mini straws in cattle AI. Pellets are frozen directly on dry ice without straws, which are difficult to label and automate. German straws are structurally similar but less globally standardized.",
        "Wow_Approach": "French mini straws require specialized AI guns (e.g., universal AI guns that can accommodate both 0.25 ml and 0.5 ml straws). The clinician must ensure the straw is loaded with the polyvinyl alcohol (PVA) factory plug facing backward, serving as the plunger contact."
    },
    981: {
        "topic": "Functions of the Epididymis - Maturation and Storage",
        "Core_Anatomy": "Caput (head), corpus (body), and cauda (tail) epididymis.",
        "Pathogenesis_Immediate": "The four primary physiological functions of the epididymis are: Transport of sperm, Concentration of sperm (fluid absorption), Maturation of sperm, and Storage of mature sperm.",
        "Pathogenesis_Deep": "Each region of the epididymis is highly specialized: (1) Transport: sperm are moved from the testis to the vas deferens via hydrostatic pressure and peristaltic contractions of the epididymal smooth muscle (taking 9-14 days). (2) Concentration: the caput absorbs >90% of the testicular fluid, concentrating sperm from 100 million/ml to >4 billion/ml. (3) Maturation: in the corpus, sperm acquire progressive motility and fertilizing capacity through membrane lipid remodeling and the addition of forward-motility glycoproteins. (4) Storage: the cauda serves as the primary reservoir, keeping sperm quiescent in a cool, low-pH environment.",
        "Why_Not": "The epididymis does not produce or synthesize spermatozoa (which is strictly a testicular function of the seminiferous tubules). It does not secrete seminal plasma proteins associated with the accessory glands (e.g., riboflavin or fructose).",
        "Wow_Approach": "To check for complete epididymal obstruction in a sterile ram with normal semen volume: measure seminal plasma L-carnitine or alpha-glucosidase. These biomarkers are synthesized exclusively by the epididymis; their absence in semen confirms complete bilateral epididymal blockage."
    },
    984: {
        "topic": "Structure of the Epididymis - Anatomical Segments",
        "Core_Anatomy": "Caput epididymis, corpus epididymis, cauda epididymis, and efferent ductules.",
        "Pathogenesis_Immediate": "The epididymis is an elongated, single highly convoluted duct divided anatomically into three segments: Caput (head), Corpus (body), and Cauda (tail).",
        "Pathogenesis_Deep": "The anatomical structures are highly distinct: (1) Caput (head): closely adhered to the dorsal pole of the testis, receiving sperm from the efferent ductules. It has a high epithelial height and abundant stereocilia for fluid absorption. (2) Corpus (body): runs down the posterolateral border of the testis, serving as the site of intensive cellular maturation. (3) Cauda (tail): a prominent, bulbous structure at the ventral pole of the testis, which transitions directly into the vas deferens. The cauda is highly muscular, contracting during ejaculation.",
        "Why_Not": "The vas deferens is the exit duct leading to the urethra, not a segment of the epididymis. The efferent ducts connect the rete testis to the caput, serving as the anatomical transition rather than an epididymal segment.",
        "Wow_Approach": "Scrotal palpation: the cauda epididymis should feel firm and distinct. In rams, a soft, flabby, or enlarged cauda indicates Brucella ovis infection (infectious epididymitis), which causes severe fibrosis and obstruction, leading to permanent sterility."
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
