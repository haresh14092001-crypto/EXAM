import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1023: {
        "topic": "Etiology of Male Infertility - Testicular Pathology Spectrum",
        "Core_Anatomy": "Testicular parenchyma, seminiferous tubules, and the scrotal sac.",
        "Pathogenesis_Immediate": "The primary organic causes of male infertility and semen quality collapse include Testicular Hypoplasia, Testicular Degeneration, and Cryptorchidism (making 'All of the above' the correct etiology).",
        "Pathogenesis_Deep": "These conditions cover the spectrum of testicular pathology: (1) Testicular hypoplasia is a congenital, hereditary failure of the seminiferous tubules to develop. (2) Testicular degeneration is an acquired, progressive loss of active germ cells caused by heat, fever, toxins, or age, leading to tubular calcification. (3) Cryptorchidism is the failure of the testes to descend, exposing them to core body temperature which suppresses spermatogenesis. All three lead to azoospermia or severe teratozoospermia, causing infertility.",
        "Why_Not": "These conditions cannot be grouped separately under standard clinical breeding examinations; all three represent major, irreversible (or slowly reversible in degeneration) testicular pathologies that warrant immediate culling or medical exclusion.",
        "Wow_Approach": "To differentiate hypoplasia from degeneration: check historical breeding records. A bull that was previously highly fertile but suddenly crashes has testicular degeneration. A young bull that was never fertile and presents with small, firm testes has testicular hypoplasia."
    },
    1024: {
        "topic": "BPH Endocrinology - DHT and Estrogen Synergism (Repeated MCQ)",
        "Core_Anatomy": "Canine prostate gland, epithelial cells, and intracellular 5-alpha-reductase.",
        "Pathogenesis_Immediate": "Prostatic hyperplasia (BPH) in dogs is caused primarily by the excess intraprostatic conversion and activity of the androgen Dihydrotestosterone (DHT), synergized by age-related increases in Estrogen.",
        "Pathogenesis_Deep": "Testosterone secreted by the Leydig cells is converted into Dihydrotestosterone (DHT) inside the prostate by the enzyme 5-alpha-reductase. DHT is 5-10 times more potent than testosterone and is the primary driver of prostatic glandular hypertrophy. With aging, the dog's estrogen levels rise relative to testosterone. Estrogen upregulates the transcription of androgen receptors on the prostatic cells, making the gland hyper-sensitive to even normal circulating levels of DHT, accelerating hyperplasia.",
        "Why_Not": "Progesterone has no direct hyperplastic effect on the prostate. Estrogen alone causes squamous metaplasia (which can cause cystic changes but is distinct from standard glandular BPH). DHT remains the mandatory driver.",
        "Wow_Approach": "CPSE (Canine Prostate Specific Esterase) is a major blood biomarker secreted by hyperplastic prostatic epithelial cells. A high CPSE level (>15 ng/ml) in an intact dog is 95% diagnostic of BPH, allowing detection before clinical signs develop."
    },
    1025: {
        "topic": "Dystrophia Adiposogenitalis - Pituitary Chromophobe Tumor in Dogs",
        "Core_Anatomy": "Hypothalamus, anterior pituitary gland, third ventricle, and the infundibular stalk.",
        "Pathogenesis_Immediate": "Dystrophia Adiposogenitalis (Fröhlich's syndrome) in dogs is caused by a space-occupying tumor (typically a chromophobe adenoma) of the Anterior Pituitary gland that compresses the adjacent hypothalamic centers.",
        "Pathogenesis_Deep": "The pathophysiology involves dual compression: (1) The growing pituitary tumor compresses the hypothalamic satiety center, causing extreme obesity (dystrophia adiposa). (2) The tumor destroys the gonadotrophs in the anterior pituitary and compresses the GnRH-releasing neurosecretory stalk, causing a complete lack of FSH and LH. Without gonadotropins, the testes undergo profound atrophy (infantile genitalia) and libido is lost (genitalis hypoplasia). It presents as an obese, sluggish male dog with infantile external genitalia.",
        "Why_Not": "Sertoli cell tumors cause feminization syndrome (alopecia, gynecomastia, pendulous prepuce) due to direct estrogen secretion, but do not cause hypothalamic obesity (Dystrophia Adiposogenitalis). Leydig cell tumors are typically benign and hormonally silent.",
        "Wow_Approach": "To diagnose Dystrophia Adiposogenitalis clinically: perform an MRI or CT of the brain to visualize the pituitary mass. Urinalysis will show diabetes insipidus signs if the tumor compresses the adjacent supraoptic-hypophyseal tract, blocking ADH release."
    },
    1026: {
        "topic": "Semen Chemistry - Prevention of Sperm Agglutination by Albumin",
        "Core_Anatomy": "Sperm cell outer membrane, seminal plasma glycoproteins, and calcium channels.",
        "Pathogenesis_Immediate": "Semen extenders utilize Albumin (bovine serum albumin or egg yolk proteins) to coat the sperm membrane and prevent the spontaneous head-to-head agglutination of spermatozoa.",
        "Pathogenesis_Deep": "Sperm agglutination is an immunologic or biophysical clumping that reduces progressive motility. Albumin acts as a protective macromolecule: (1) It binds to the sperm plasma membrane, stabilizing the negative surface charge (zeta potential). (2) This keeps the sperm cells mutually repelled. (3) Albumin acts as a potent scavenger of reactive oxygen species (ROS) and toxic lipid peroxides that would otherwise damage membrane lipids, exposing agglutination-triggering antigens.",
        "Why_Not": "Gelatin is a gelling agent used to thicken extenders (e.g., in boar semen transport), but does not prevent membrane agglutination. Arginine is an amino acid that supports sperm metabolism but lacks macromolecular protective properties.",
        "Wow_Approach": "In semen extender formulation, Bovine Serum Albumin (BSA) is added at a concentration of 0.1-1.0%. BSA supplementation is particularly crucial for sex-sorted semen, which is highly fragile due to laser-induced membrane stress and prone to rapid clumping."
    },
    1027: {
        "topic": "Acrosomal Enzymes - Acrosin and Hyaluronidase for Egg Penetration",
        "Core_Anatomy": "Sperm head acrosomal vesicle, inner acrosomal membrane, and the oocyte zona pellucida.",
        "Pathogenesis_Immediate": "The primary proteolytic enzyme secreted by the acrosome that digests a path through the oocyte's zona pellucida is Acrosin, working alongside Hyaluronidase.",
        "Pathogenesis_Deep": "Sperm penetration is a dual-enzyme process: (1) Hyaluronidase is released first to digest the hyaluronic acid matrix of the cumulus oophorus cells. (2) Upon contact with the zona pellucida glycoprotein ZP3, the sperm undergoes the acrosome reaction, exposing the inner acrosomal membrane. (3) Acrosin (a trypsin-like serine protease bound to the inner acrosomal membrane) is activated. Acrosin digests a highly localized tunnel through the zona pellucida, allowing the hyperactivated sperm tail to push the sperm head through into the perivitelline space.",
        "Why_Not": "Proteases, peptidases, and lipases are general cellular enzymes. Acrosin is a highly specialized, sperm-specific serine protease designed exclusively to bind and digest the zona pellucida matrix.",
        "Wow_Approach": "Acrosin is stored in the acrosome as an inactive zymogen, proacrosin. This prevents premature self-digestion of the acrosomal membrane. It is only converted to active acrosin during the calcium-dependent acrosome reaction upon contact with the zona."
    },
    1028: {
        "topic": "Spermiogenesis - Golgi Apparatus Origin of the Acrosome",
        "Core_Anatomy": "Round spermatid cytoplasm, Golgi apparatus, and the anterior nuclear pole.",
        "Pathogenesis_Immediate": "During spermiogenesis (the morphological differentiation phase of spermatogenesis), the acrosome originates directly from the Golgi apparatus of the round spermatid.",
        "Pathogenesis_Deep": "The acrosomal vesicle is synthesized in three distinct phases: (1) Golgi Phase: the Golgi apparatus of the round spermatid produces proacrosomal granules rich in glycoproteins. These granules coalesce to form a single large acrosomal vesicle. (2) Cap Phase: the acrosomal vesicle spreads out and flattens over the anterior two-thirds of the condensing sperm nucleus, forming the acrosomal cap. (3) Acrosome Phase: the vesicle undergoes compaction, and the Golgi residues migrate to the caudal pole of the cell to be shed as residual cytoplasm (residual bodies).",
        "Why_Not": "Mitochondria migrate to the base of the flagellum and align spirally around the middle piece to form the mitochondrial sheath. The nucleus condenses to form the sperm head. Lysozymes are general organelles, not the specific source of the acrosome.",
        "Wow_Approach": "Understanding the Golgi origin explains the high glycoprotein content of the acrosome. Staining techniques like PAS (Periodic Acid-Schiff) specifically target these Golgi-derived carbohydrates, allowing the clinician to evaluate acrosome formation under light microscopy."
    },
    1040: {
        "topic": "Sustentacular Cells - Sertoli Cells of the Testis",
        "Core_Anatomy": "Seminiferous tubules, Sertoli cells, germ cells, and the basement membrane.",
        "Pathogenesis_Immediate": "Sustentacular cells (otherwise known as Sertoli cells) are the large, somatic structural cells lining the seminiferous tubules that provide physical and nutritional support to developing germ cells.",
        "Pathogenesis_Deep": "Sertoli cells are homologous to ovarian granulosa cells. They have three primary functions: (1) Structural support: they span the entire height of the seminiferous epithelium from the basement membrane to the lumen, anchoring the developing germ cells. (2) Blood-Testis Barrier: tight junctions between adjacent Sertoli cells divide the tubule into basal and adluminal compartments, preventing immunogenic haploid spermatids from contacting the host immune system. (3) Endocrine: they secrete androgen-binding protein (ABP) to concentrate testosterone, inhibin to suppress FSH, and AMH in the fetus.",
        "Why_Not": "Leydig cells are located in the interstitium outside the tubules and secrete testosterone, not serving a direct structural support role for germ cells. Myoid cells are contractile muscle cells of the tubule wall.",
        "Wow_Approach": "Because Sertoli cells have a fixed population size determined prepubertally, the total number of Sertoli cells per testis dictates the maximum spermatogenic capacity of the bull. High-quality early nutrition maximizes Sertoli cell mitosis, ensuring superior adult fertility."
    },
    1041: {
        "topic": "Antioxidants in Semen - SOD and Catalase Protection",
        "Core_Anatomy": "Sperm plasma membrane (rich in polyunsaturated fatty acids) and seminal plasma.",
        "Pathogenesis_Immediate": "Superoxide Dismutase (SOD) and Catalase are key enzymatic antioxidants present in seminal plasma that protect spermatozoa from oxidative stress and lipid peroxidation.",
        "Pathogenesis_Deep": "Sperm membranes are highly vulnerable to reactive oxygen species (ROS) due to high concentrations of polyunsaturated fatty acids. (1) Superoxide dismutase (SOD) catalyzes the conversion of highly reactive superoxide radicals (O2•⁻) into hydrogen peroxide (H2O2) and oxygen. (2) Catalase then converts the toxic H2O2 into water and oxygen. Without this dual enzymatic protection, ROS causes rapid lipid peroxidation of the sperm membrane, leading to membrane lysis, loss of motility (asthenozoospermia), and DNA fragmentation.",
        "Why_Not": "Glycerol is a physical cryoprotectant, not an enzymatic antioxidant scavenger. Proteases digest proteins, which would damage sperm rather than protect them from oxygen radicals.",
        "Wow_Approach": "During semen cryopreservation, the native seminal plasma is diluted, reducing SOD and Catalase concentrations. Adding exogenous antioxidants (e.g., Vitamin E, Vitamin C, or recombinant SOD) to the extender significantly improves post-thaw progressive motility and fertility."
    },
    1042: {
        "topic": "Blood-Testis Barrier - Immunological Isolation of Spermatids",
        "Core_Anatomy": "Sertoli cell tight junctions (zonula occludens) and the seminiferous epithelium.",
        "Pathogenesis_Immediate": "The Blood-Testis Barrier (BTB) is formed by specialized tight junctions (zonula occludens) between adjacent Sertoli cells, physically isolating haploid germ cells from the host immune system.",
        "Pathogenesis_Deep": "The BTB divides the seminiferous tubule into: (1) Basal compartment: contains diploid spermatogonia which are exposed to systemic blood and lymph. (2) Adluminal compartment: contains haploid spermatids and spermatozoa. Because meiosis generates unique, non-self antigens on haploid cells, the immune system would recognize them as foreign. The tight junctions of the BTB prevent immune cells and immunoglobulins from entering the adluminal compartment, preventing autoimmune orchitis and the formation of anti-sperm antibodies.",
        "Why_Not": "The basement membrane is porous and does not block immune cells. Leydig cells reside in the interstitium and have no tight junctions. The BTB is strictly a Sertoli-to-Sertoli cell tight junction system.",
        "Wow_Approach": "Clinical correlation: Any trauma, biopsy, or severe infection (such as Brucellosis) that ruptures the Blood-Testis Barrier will expose the haploid spermatids to systemic circulation. The immune system immediately forms anti-sperm antibodies, leading to autoimmune testicular degeneration and permanent sterility."
    },
    1043: {
        "topic": "Calcium Ionophore A23187 - Inducer of In-Vitro Acrosome Reaction",
        "Core_Anatomy": "Sperm plasma membrane, intracellular calcium pools, and acrosomal vesicle.",
        "Pathogenesis_Immediate": "Calcium Ionophore A23187 is a highly potent lipophilic chemical agent used in reproductive laboratories to artificially induce the Acrosome Reaction in spermatozoa in-vitro.",
        "Pathogenesis_Deep": "The physiological acrosome reaction requires an influx of extracellular calcium into the sperm head, triggered by binding to the zona pellucida ZP3 glycoprotein. Calcium Ionophore A23187 acts as a mobile carrier: (1) It inserts into the lipid bilayer of the sperm membrane. (2) It binds extracellular calcium ions and transports them directly across the membrane down the concentration gradient. (3) This rapid increase in intracellular calcium activates phospholipase C and raises pH, triggering immediate fusion and vesiculation of the outer acrosomal membrane with the plasma membrane, achieving a >90% acrosome reaction in-vitro.",
        "Why_Not": "Heparin is used to induce capacitation (cholesterol removal), not the final acrosome reaction. Prostaglandins have no direct ionophore activity. Trypsin is a protease, not a membrane calcium transporter.",
        "Wow_Approach": "The Calcium Ionophore assay is used in breeding soundness labs to evaluate a stallion's or bull's 'acrosome responsiveness'. Sperm that fail to undergo the acrosome reaction when exposed to A23187 are functionally incompetent, as they lack the intracellular machinery required for fertilization."
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
