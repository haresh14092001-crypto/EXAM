import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1044: {
        "topic": "Os Penis - The Baculum of Canine Anatomy",
        "Core_Anatomy": "Glans penis, penile urethra, urethral groove, and the baculum bone.",
        "Pathogenesis_Immediate": "The Os Penis (baculum) is a heterotopic skeletal bone found within the glans penis of dogs (canines) and other carnivores, providing the structural rigidity required for initial intromission before full erection.",
        "Pathogenesis_Deep": "The canine os penis: (1) Lies dorsal to the urethra. (2) Has a deep, ventral urethral groove that houses and protects the urethra from compression. (3) Originates from mesenchymal ossification. The presence of the bone ensures that the male dog can achieve mechanical intromission into the receptive bitch's vagina immediately upon mounting. Erection of the vascular bulbous glandis occurs *after* intromission, locking the dog in place (the tie).",
        "Why_Not": "Bulls, rams, and boars have a fibroelastic penis with no penile bone (os penis), relying strictly on high-pressure straightening of the sigmoid flexure. Stallions have a vascular penis but lack a baculum.",
        "Wow_Approach": "Because the urethra runs through the narrow, rigid urethral groove of the os penis, this groove is the primary site where urinary calculi (uroliths) lodge in male dogs. The clinician must perform a urethrotomy just caudal to the os penis to relieve such obstructions."
    },
    1054: {
        "topic": "VGO Andrology Exam - Final Objective Structure (Repeated MCQ)",
        "Core_Anatomy": "Male reproductive system and processing laboratory.",
        "Pathogenesis_Immediate": "The objective section of Andrology evaluates core facts: cryopreservation chemistry (glycerol, riboflavin), semen density, and sperm maturation kinetics.",
        "Pathogenesis_Deep": "University guidelines emphasize testing quantitative baselines to ensure diagnostic safety. Topics include: (1) Liquid carbon dioxide storage at -79°C. (2) Fructose concentration (highest in bulls/ruminants). (3) Pathological agents of orchitis (Brucella abortus).",
        "Why_Not": "Descriptive short notes assess surgical or procedural expertise, while the objective section focuses strictly on these bio-mechanical parameters.",
        "Wow_Approach": "To ensure maximum scores, create comparative summaries of semen parameters (volume, concentration, cryoprotectant rates) across domestic species."
    },
    1055: {
        "topic": "Glycerol - Semen Freezing Cryoprotection (Repeated MCQ)",
        "Core_Anatomy": "Sperm plasma membrane and intracellular cytoplasm.",
        "Pathogenesis_Immediate": "Glycerol is the universally used intracellular cryoprotectant in the deep-freezing of mammalian spermatozoa, maintaining membrane stability during freezing.",
        "Pathogenesis_Deep": "Glycerol penetrates the cell membrane, binding water molecules to lower the freezing point. This suppresses ice crystal growth, protecting the fragile acrosomal and plasma membranes from mechanical lysis. It is standardly added at 6-8% in Tris-citric-egg yolk extenders.",
        "Why_Not": "DMSO and ethylene glycol are primary cryoprotectants for embryos, but are highly spermatotoxic to spermatozoa at standard processing temperatures, making glycerol the exclusive standard.",
        "Wow_Approach": "Always allow an equilibration period of 2-4 hours at 4°C after adding glycerol-containing extenders. This gives glycerol sufficient time to fully penetrate the membrane before freezing."
    },
    1056: {
        "topic": "Riboflavin - Physiological Yellow Semen Pigment (Repeated MCQ)",
        "Core_Anatomy": "Seminal vesicles and semen.",
        "Pathogenesis_Immediate": "The physiological yellow color of normal bull semen is due to Riboflavin (Vitamin B2) secreted by the seminal vesicles.",
        "Pathogenesis_Deep": "Bovine seminal vesicles synthesize and secrete high concentrations of free and protein-bound Riboflavin. During ejaculation, this fluid mixes with the sperm, giving the semen a yellowish-creamy appearance that indicates active, normal accessory gland function.",
        "Why_Not": "Lutein is an ovarian luteal pigment. Purulent yellowing (pus) is pathological and accompanied by abundant neutrophils and odor, which are absent in physiological riboflavin-pigmented semen.",
        "Wow_Approach": "Perform a rapid microscopic exam: if sperm progressive motility is >70% and no leucocytes are found, the yellow color is physiological riboflavin and completely normal."
    },
    1060: {
        "topic": "Semen Density - Ruminant Milky Whitish Ejaculates (Repeated MCQ)",
        "Core_Anatomy": "Sperm concentration and seminal plasma.",
        "Pathogenesis_Immediate": "A milky-whitish color of semen is characteristic of Ruminant species (Bulls, Rams, and Bucks) due to their exceptionally high sperm concentration.",
        "Pathogenesis_Deep": "Ruminants produce highly concentrated ejaculates (>1-3 billion sperm/ml) in small-to-moderate volumes, giving the semen a dense, milky-white to creamy appearance. In contrast, stallions and boars produce large-volume, highly dilute ejaculates that appear grayish-watery.",
        "Why_Not": "A watery or grayish color in a bull or ram ejaculate is pathological, indicating severe oligospermia or testicular degeneration, as their normal baseline is always dense and milky.",
        "Wow_Approach": "Use a visual density grading scale (0-5) in the field to rapidly estimate sperm concentration before spectrophotometer verification."
    },
    1061: {
        "topic": "Dry Ice Storage - Historically Significant -79°C Semen Storage (Repeated MCQ)",
        "Core_Anatomy": "Sperm metabolism and dry ice cooling.",
        "Pathogenesis_Immediate": "Historically, frozen semen was stored at -79°C using Solid Carbon Dioxide (Dry Ice) and alcohol mixtures before liquid nitrogen became available.",
        "Pathogenesis_Deep": "At -79°C (the sublimation temperature of solid CO2), sperm cell metabolism is significantly slowed but not completely suspended. This limited the storage lifespan of frozen semen to 1-2 years due to progressive enzymatic and membrane degradation, whereas liquid nitrogen (-196°C) suspends metabolism indefinitely.",
        "Why_Not": "Liquid nitrogen maintains -196°C. Standard freezers maintain -20°C or -80°C. The temperature of solid CO2 is specifically -79°C.",
        "Wow_Approach": "Dry ice storage is still a valuable historical and backup transport reference. Straws must be packed in insulated dry ice containers and used immediately upon arrival."
    },
    1064: {
        "topic": "Semen Chemistry - Fructose Dominance in Ruminants (Repeated MCQ)",
        "Core_Anatomy": "Seminal vesicles and sperm mitochondria.",
        "Pathogenesis_Immediate": "The concentration of fructose (the primary glycolytic energy substrate for sperm) is exceptionally high in Ruminant species (Bulls, Rams, and Bucks), synthesized and secreted by their highly developed seminal vesicles.",
        "Pathogenesis_Deep": "In ruminants, seminal plasma fructose serves as the mandatory anaerobic energy source for spermatozoa, converted to lactic acid via fructolysis to fuel mitochondrial ATP synthesis for flagellar motility. Additionally, Brucella abortus is the primary intracellular bacterial pathogen involved in orchitis, epididymitis, and seminal vesiculitis in bulls due to its potent tissue tropism for reproductive tract erythritol and fructose.",
        "Why_Not": "Dogs completely lack seminal vesicles and have zero fructose in their semen, relying instead on prostatic lactate. Boars and stallions have moderate fructose but much higher volumes of dilute fluid.",
        "Wow_Approach": "Measuring the Fructolysis Index (the rate of fructose disappearance per billion sperm per hour at 37°C) is a highly sensitive historical test for verifying active, metabolically viable sperm cells."
    },
    1067: {
        "topic": "Objective MCQ Section - Andrology Final (Repeated MCQ)",
        "Core_Anatomy": "Male urogenital system.",
        "Pathogenesis_Immediate": "The objective section of Andrology evaluates core facts: sperm enzymes (hyaluronidase in head), optimal thawing temperatures (37°C), discovery history, and developmental descent.",
        "Pathogenesis_Deep": "This testing structure ensures a rapid, independent evaluation of factual recall in Andrology. Topics include the acrosome origin from the Golgi apparatus, BPH castrative therapies, and semen packaging history.",
        "Why_Not": "Subjective essays allow for general explanations, whereas the MCQ section demands precise, singular correct answers to verify diagnostic accuracy in clinical veterinary medicine.",
        "Wow_Approach": "Familiarize yourself with the exact grading weight: Part-A carries 60 marks of highly granular factual questions."
    },
    1068: {
        "topic": "Acrosomal Enzymes - Hyaluronidase in Sperm Head (Repeated MCQ)",
        "Core_Anatomy": "Sperm head acrosome.",
        "Pathogenesis_Immediate": "Hyaluronidase enzyme is present in the sperm Head, specifically localized within the membrane-bound acrosomal vesicle covering the anterior two-thirds of the nucleus.",
        "Pathogenesis_Deep": "Hyaluronidase is released during the acrosome reaction, digesting the hyaluronic acid matrix of the cumulus oophorus cells surrounding the oocyte. This allows the sperm to penetrate the cumulus mass and reach the zona pellucida, where acrosin digests a path through the zona.",
        "Why_Not": "The midpiece contains mitochondria for energy production. The tail contains the axoneme (9+2 microtubule structure) for flagellar propulsion. Neither contains acrosomal enzymes.",
        "Wow_Approach": "Stain a semen smear with Giemsa: intact acrosomes stain dark blue as a distinct cap. Damaged acrosomes remain unstained, indicating a loss of fertility."
    },
    1070: {
        "topic": "Semen Straw Thawing - Optimal 37°C Protocol (Repeated MCQ)",
        "Core_Anatomy": "Sperm membrane lipids and thawing bath.",
        "Pathogenesis_Immediate": "The optimal thawing temperature for a frozen semen straw is 37°C (rapid thawing in a water bath for 30 seconds).",
        "Pathogenesis_Deep": "Rapid thawing at 37°C ensures the fastest transition through the critical recrystallization temperature zone (-60°C to 0°C), preventing the lethal coalescence of ice crystals that would otherwise lacerate the sperm membranes.",
        "Why_Not": "Thawing at 5°C or 25°C is too slow and causes membrane damage. Thawing above 40°C is highly toxic, causing rapid heat denaturation of sperm proteins.",
        "Wow_Approach": "Always wipe the straw completely dry after thawing, as water is highly spermicidal. Cut the sealed tip and load into the warm AI gun immediately."
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
