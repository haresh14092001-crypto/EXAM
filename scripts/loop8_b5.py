import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    920: {
        "topic": "Andrology Matching - Thermoregulation and Urogenital Anatomy",
        "Core_Anatomy": "Testicular vascular architecture and the terminal urethra.",
        "Pathogenesis_Immediate": "Key matching pairs in Andrology: Pampiniform plexus matches to thermoregulation (counter-current heat exchange); Urethral process matches to buck/ram (vermiform appendage); Erection matches to pelvic nerve parasympathetic activation.",
        "Pathogenesis_Deep": "These matching pairs cover critical physiological structures: (1) The Pampiniform Plexus is a highly convoluted network of testicular veins that wrap around the testicular artery. Warm arterial blood (39°C) transfers its heat to the cool venous blood (33°C) returning from the scrotal skin, cooling the arterial blood before it enters the testis. (2) The urethral process (vermiform process) is an anatomical projection of the urethra extending past the glans penis in rams and bucks, which sprays semen in a wide arc during ejaculation.",
        "Why_Not": "The prostate gland is the sole accessory gland in the dog, unrelated to pampiniform or urethral processes. In stallions, the urethral process is recessed within the fossa glandis, not forming an elongated vermiform appendage like in small ruminants.",
        "Wow_Approach": "In rams, severe urolithiasis (urinary calculi) almost always lodges at the narrow urethral process. The standard emergency veterinary procedure is a 'urethral process amputation' (snipping the vermiform process), which instantly relieves the urinary obstruction without impairing future fertility."
    },
    921: {
        "topic": "Pampiniform Plexus - Counter-Current Heat Exchanger",
        "Core_Anatomy": "Testicular artery, convoluted testicular vein network, and the spermatic cord.",
        "Pathogenesis_Immediate": "The Pampiniform Plexus is a highly specialized vascular structure in the spermatic cord that acts as a counter-current heat and hormone exchanger, maintaining testicular temperature at 2-6°C below core body temperature.",
        "Pathogenesis_Deep": "Thermoregulation of the testes is mandatory for normal spermatogenesis. The pampiniform plexus consists of: (1) The highly coiled testicular artery, which increases the surface area for vascular contact. (2) A surrounding network of up to 10-12 anastomosing testicular veins. Warm arterial blood (39°C) entering the spermatic cord transfers its heat down the thermal gradient to the cool venous blood (33°C) returning from the scrotal skin. This ensures the testis is maintained at ~34°C. Additionally, it allows local testosterone exchange from venous blood back into the arterial inflow.",
        "Why_Not": "If the pampiniform plexus fails (e.g., due to varicocele or inguinal hernia), the testicular temperature rises to core body temperature, causing immediate arrest of meiosis in primary spermatocytes and permanent testicular degeneration.",
        "Wow_Approach": "The pampiniform plexus also serves as a pressure pulse dampener. The extreme convolution of the testicular artery absorbs the arterial pulse wave, transforming the high-pressure pulsatile flow into a slow, continuous, non-pulsatile micro-circulation by the time blood reaches the testicular parenchyma."
    },
    922: {
        "topic": "Urethral Process - Vermiform Appendage of Small Ruminants",
        "Core_Anatomy": "Distal urethral mucosa, glans penis, and the prepuce.",
        "Pathogenesis_Immediate": "The urethral process (vermiform process or appendage) is a highly prominent, thin, flexible projection of the urethra extending 2-3 cm past the glans penis in the Buck (goat) and Ram (sheep).",
        "Pathogenesis_Deep": "During ejaculation in small ruminants, the rapid muscular contractions of the urethralis muscle force semen out at high velocity. The flexible urethral process rotates rapidly in a whip-like motion, spraying a micro-thin film of semen in a wide 360-degree arc over the external cervical os. This ensures maximum distribution of the small-volume, highly concentrated semen (0.5-1.5 ml containing 3-5 billion sperm/ml) onto the cervix, maximizing the chance of sperm capture.",
        "Why_Not": "Bulls and boars have a simple, blunt urethral opening at the tip of the glans penis with no external process. Stallions have a recessed urethral process located within the fossa glandis, which does not spray semen.",
        "Wow_Approach": "Amputation of the urethral process is highly effective for relieving urolithiasis in pet or meat goats. However, in elite breeding rams, process amputation is avoided if possible, as losing the spraying mechanism can reduce conception rates under natural flock mating conditions."
    },
    941: {
        "topic": "Veterinary Andrology Examination - Comprehensive Objective Section",
        "Core_Anatomy": "Male reproductive system and processing laboratory.",
        "Pathogenesis_Immediate": "The objective section of final Andrology exams carries 60 marks, designed to test a wide spectrum of anatomical, chemical, and biological constants in reproductive technologies.",
        "Pathogenesis_Deep": "The exam structure prioritizes rapid factual recall: (1) Cryobiology (glycerol concentration, cooling rates, nitrogen vapor temps). (2) Sperm biology (spermatogenesis timelines, epididymal transit, daily output). (3) Physical diagnoses (scrotal measurements, lameness, vices). (4) Semen chemistry (seminal vesicles, Cowper's gland toxins, fructose levels). Mastering this section requires high-precision flashcard retrieval.",
        "Why_Not": "Descriptive essays cannot assess this density of clinical facts. The objective section is mandatory to verify that the student has memorized the normal biological baselines required to prevent clinical errors in the field.",
        "Wow_Approach": "When reviewing, compile a 'cheat sheet' of species-specific constants (e.g., bull vs stallion semen volume, ram vs boar spermatogenesis length) to quickly identify correct answers among distractors."
    },
    942: {
        "topic": "Objective Andrology Guidelines - Exam Time Management",
        "Core_Anatomy": "N/A - Exam Protocols.",
        "Pathogenesis_Immediate": "University regulations dictate that the 60-mark objective section must be completed within 1 hour and handed over, with no descriptive answers allowed in this section.",
        "Pathogenesis_Deep": "This testing structure ensures a rapid, independent evaluation of factual recall in Andrology. Separating this section ensures that core knowledge of physiological values, semen dilution rates, and accessory gland profiles is assessed without the use of descriptive cues from subsequent sections.",
        "Why_Not": "Part-B contains essays and short-answer clinical case questions, which are graded separately and require descriptive, structured answers over the remaining 2 hours of the exam.",
        "Wow_Approach": "When practicing, simulate the 1-hour constraint. Developing immediate recall of normal reproductive values (e.g., canine semen fraction details, equine extender protocols) is essential for rapid diagnosis in busy veterinary hospitals."
    },
    943: {
        "topic": "Glycerol - Universal Cryoprotectant in Semen Freezing",
        "Core_Anatomy": "Sperm plasma membrane, intracellular compartment, and extracellular matrix.",
        "Pathogenesis_Immediate": "Glycerol is the universally used intracellular cryoprotectant in the deep-freezing of mammalian spermatozoa, added at a final concentration of 6-8% in bovine semen extenders.",
        "Pathogenesis_Deep": "Glycerol protects sperm cells during the transition through the critical temperature zone (0°C to -60°C) via multiple mechanisms: (1) It easily penetrates the sperm plasma membrane due to its small molecular weight. (2) Inside the cytoplasm, it binds water molecules, dramatically lowering the freezing point and reducing the amount of ice formed. (3) This minimizes cell dehydration and prevents the high concentration of extracellular solutes ('solution effect') that would otherwise denature membrane proteins. (4) It stabilizes the phospholipid bilayer against cold shock.",
        "Why_Not": "DMSO is used for cryopreservation of embryos, but is highly toxic to spermatozoa at standard concentrations. Ethylene glycol is used for direct transfer of embryos. Glycerol remains the absolute gold-standard cryoprotectant for semen.",
        "Wow_Approach": "Equilibration time: after adding the glycerol-containing extender at 4°C, semen must be allowed to 'equilibrate' for 2-4 hours. This allows the glycerol to fully penetrate the sperm membrane and stabilize the lipid matrix before the rapid plunge into nitrogen vapor."
    },
    944: {
        "topic": "Riboflavin - Physiological Yellow Pigment of Bovine Semen",
        "Core_Anatomy": "Bovine seminal vesicles (vesicular glands), urethral lumen, and seminal plasma.",
        "Pathogenesis_Immediate": "The physiological yellow color of normal bull semen is due to Riboflavin (Vitamin B2) secreted by the seminal vesicles.",
        "Pathogenesis_Deep": "Bull seminal plasma contains a high concentration of free and protein-bound Riboflavin. The seminal vesicles actively synthesize and secrete this water-soluble vitamin. When semen is ejaculated, the mixing of vesicular fluid with the sperm-rich ampullary fluid imparts a characteristic creamy-yellowish tinge to the semen. This yellow color is entirely normal and highly correlated with normal accessory gland activity. It must be clinically distinguished from pathological yellowing caused by pyometra/orchitis pus (which is turbid, contains neutrophils) or urine contamination (which has a distinct ammonia odor and low sperm motility).",
        "Why_Not": "Lutein is the carotenoid pigment responsible for the yellow color of the corpus luteum, but is not secreted in semen. Fructose is a colorless sugar. Urea causes yellowing due to urine contamination, which is pathological.",
        "Wow_Approach": "To verify if yellow semen is physiological: perform a microscopic exam. If sperm progressive motility is >70% and no leucocytes are found, the color is physiological riboflavin. If motility is <20% and neutrophils are abundant, it is purulent contamination."
    },
    949: {
        "topic": "Semen Density - Milky Whitish Color of Ruminant Ejaculates",
        "Core_Anatomy": "Sperm cell density, seminal plasma, and comparative male ejaculation.",
        "Pathogenesis_Immediate": "A milky-whitish color of semen is characteristic of Ruminant species (Bulls, Rams, and Bucks) due to their exceptionally high sperm concentration (>1-3 billion sperm/ml).",
        "Pathogenesis_Deep": "The color and consistency of an ejaculate are highly dependent on the concentration of spermatozoa per unit volume: (1) High density (Milky-whitish to creamy-yellow): seen in bulls, rams, and bucks, where the sperm concentration exceeds 1 billion/ml. (2) Moderate density (Opalescent to cloudy-white): seen in dogs and cats (~100-300 million/ml). (3) Low density (Watery or grayish-translucent): seen in stallions and boars (~50-150 million/ml), where the ejaculate volume is very high (50-250 ml) but dilute.",
        "Why_Not": "A watery or grayish color in a bull or ram ejaculate is pathological, indicating severe oligospermia or testicular degeneration, as their normal baseline is always a dense, milky-white.",
        "Wow_Approach": "Visual grading of bull semen: grade semen on a 0-5 scale. A score of 5 represents a thick, creamy-white ejaculate (concentration >1.5 billion/ml), whereas a score of 1 represents a watery-grayish ejaculate (concentration <200 million/ml), allowing rapid field estimation before spectrophotometry."
    },
    950: {
        "topic": "Dry Ice Storage - Historically Significant -79°C Semen Storage",
        "Core_Anatomy": "Sperm cell metabolism, dry ice (solid carbon dioxide) container.",
        "Pathogenesis_Immediate": "Prior to the widespread commercial availability of liquid nitrogen, frozen semen was historically stored at -79°C in Solid Carbon Dioxide (Dry Ice) and alcohol mixtures.",
        "Pathogenesis_Deep": "Cryopreservation history: (1) In 1949, Polge, Smith, and Parkes discovered the cryoprotective properties of glycerol. (2) The first commercial freezing of bull semen was achieved using a mixture of solid carbon dioxide (dry ice) and isopropyl alcohol, which maintains a stable temperature of -79°C. (3) While sperm metabolism is significantly slowed at -79°C, it is not completely suspended, leading to progressive membrane degradation and limiting the semen lifespan to 1-2 years. Today, liquid nitrogen (-196°C) is the absolute standard, suspending metabolism indefinitely.",
        "Why_Not": "Liquid nitrogen maintains a temperature of -196°C. Standard deep-freezers maintain -20°C or -80°C. The specific temperature of solid CO2 (dry ice) sublimation is -79°C, which is the historical value tested.",
        "Wow_Approach": "Dry ice storage is still occasionally used for transport in regions lacking liquid nitrogen infrastructure. The semen straws must be packed in insulated containers filled with crushed dry ice, and must be used immediately upon arrival, as temperature fluctuations rapidly kill the cells."
    },
    952: {
        "topic": "Brucella abortus - High-Yield Agent of Male Reproductive Pathology",
        "Core_Anatomy": "Testicular parenchyma, epididymal tail, seminal vesicles, and the blood-testis barrier.",
        "Pathogenesis_Immediate": "Brucella abortus is the bacterial pathogen most commonly involved in causing acute and chronic Orchitis, Epididymitis, and Seminal Vesiculitis in bulls.",
        "Pathogenesis_Deep": "Brucella abortus has a potent tissue tropism for both the gravid female uterus and the male reproductive tract due to local concentrations of erythritol. In the bull: (1) The bacteria invade via hematogenous or ascending pathways. (2) They colonize the seminal vesicles, causing chronic seminal vesiculitis (seminal plasma contains neutrophils and Brucella). (3) They cross the blood-testis barrier, causing necrotizing orchitis and epididymitis. The testis swells rapidly inside the scrotum, causing pressure necrosis of the seminiferous tubules. Eventually, the testis undergoes fibrous scar tissue replacement or abscessation, causing permanent sterility and serving as a major source of venereal transmission.",
        "Why_Not": "*Campylobacter fetus* causes venereal early embryonic death in cows but does not cause severe necrotizing orchitis or vesiculitis in bulls. *Trichomonas foetus* resides strictly on the prepuce and does not invade the testis parenchyma.",
        "Wow_Approach": "A bull diagnosed with Brucella orchitis or seminal vesiculitis is a major biosecurity hazard. The bacteria are shed in massive numbers in the semen, and natural mating or AI will instantly infect cows. These bulls cannot be treated and must be culled immediately."
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
