import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1356: {
        "topic": "Endocrinology of Spermatogenesis - HPT Axis",
        "Core_Anatomy": "Hypothalamic-Pituitary-Testicular (HPT) axis and seminiferous tubules.",
        "Pathogenesis_Immediate": "Spermatogenesis is NOT primarily controlled by the hormone Estrogen in the standard veterinary curriculum (making it the correct 'not controlled by' option). It is strictly dependent on FSH, LH, and Testosterone.",
        "Pathogenesis_Deep": "Spermatogenesis requires three mandatory hormones: (1) LH from the anterior pituitary stimulates Leydig cells to produce testosterone. (2) FSH stimulates Sertoli cells to produce Androgen-Binding Protein (ABP). (3) Testosterone (concentrated 100x inside the tubules by ABP) directly drives the meiotic divisions of the germ cells. While trace amounts of estrogen are produced by Sertoli cells (from testosterone via aromatase) and play a minor local role in epididymal fluid resorption, it is not considered a primary regulatory driver of spermatogenesis like the HPT axis hormones.",
        "Why_Not": "Without high intratesticular testosterone, meiosis halts completely. Without FSH, Sertoli cells cannot nurse the germ cells. Without LH, testosterone is absent.",
        "Wow_Approach": "Administering exogenous estrogen or high doses of systemic testosterone to a bull will cause a negative feedback loop, shutting down endogenous LH and FSH, leading to profound testicular atrophy and azoospermia."
    },
    1357: {
        "topic": "Andrology Matching - Embryology and Cryobiology",
        "Core_Anatomy": "Male urogenital tract and semen processing laboratory.",
        "Pathogenesis_Immediate": "Key matching pairs: Genital tubercle matches to glans penis/clitoris development; Corkscrew penis matches to Boar; Glycerol matches to intracellular cryoprotectant.",
        "Pathogenesis_Deep": "These matching pairs evaluate fundamental, distinct concepts in male reproduction: (1) The genital tubercle is the embryonic primordium that develops into the phallus. (2) The boar's corkscrew penis is a unique anatomical adaptation for cervical locking. (3) Glycerol is the universal chemical agent used to prevent intracellular ice crystal formation during deep freezing of semen.",
        "Why_Not": "Matching glycerol to anything other than cryoprotection (e.g., matching it to an energy source like fructose) demonstrates a critical misunderstanding of semen extender chemistry.",
        "Wow_Approach": "To master matching questions, group the terms by discipline: Embryology (Genital tubercle, Wolffian duct), Anatomy (Corkscrew, Os penis), and Chemistry (Glycerol, Tris, Citrate)."
    },
    1358: {
        "topic": "Genital Tubercle - Embryonic Phallus Development",
        "Core_Anatomy": "Embryonic urogenital sinus and the indifferent external genitalia.",
        "Pathogenesis_Immediate": "The Genital Tubercle is the embryonic precursor structure that develops into the Glans Penis in the male and the Clitoris in the female.",
        "Pathogenesis_Deep": "During the indifferent stage of embryonic development, all mammalian fetuses possess a genital tubercle (a small swelling cranial to the urogenital sinus). In the male, under the influence of Dihydrotestosterone (DHT) produced locally from fetal testicular testosterone, the genital tubercle rapidly elongates to form the shaft and glans of the penis. In the absence of DHT (in females), it remains small and becomes the clitoris.",
        "Why_Not": "The Wolffian ducts form the internal plumbing (epididymis/vas deferens). The genital swellings form the scrotum or labia. The genital tubercle specifically forms the phallus.",
        "Wow_Approach": "Freemartin heifers (genetically female but exposed to male twin hormones in utero) often have an enlarged, prominent clitoris due to the partial masculinization of their genital tubercle by the twin's androgens."
    },
    1359: {
        "topic": "Corkscrew Shaped Penis - Porcine Anatomy (Repeated MCQ)",
        "Core_Anatomy": "Porcine glans penis and female cervical rings.",
        "Pathogenesis_Immediate": "The pathognomonic 'Corkscrew' shaped penis is the anatomical hallmark of the Boar.",
        "Pathogenesis_Deep": "The boar possesses a fibroelastic penis with a distinct, counter-clockwise spiral or 'corkscrew' tip. During copulation, the spiral tip locks mechanically into the interlocking cervical rings (pulvini cervicales) of the sow. This perfect anatomical fit allows the boar to deposit the massive ejaculate volume (150-300 ml) under high pressure directly into the cervix and uterine body over a prolonged 5-10 minute ejaculation period.",
        "Why_Not": "Bulls and rams have a straight glans with a urethral process. Stallions have a large, blunt vascular glans that expands into a 'bell' shape.",
        "Wow_Approach": "When performing AI in swine, the technician uses a specialized spiral-tipped catheter and must rotate it counter-clockwise to mimic the boar's penis locking into the sow's cervix."
    },
    1360: {
        "topic": "Glycerol - Semen Freezing Cryoprotection (Repeated MCQ)",
        "Core_Anatomy": "Sperm plasma membrane and intracellular cytoplasm.",
        "Pathogenesis_Immediate": "Glycerol is the universally used intracellular cryoprotectant in the deep-freezing of mammalian spermatozoa, maintaining membrane stability during freezing.",
        "Pathogenesis_Deep": "Glycerol penetrates the cell membrane, binding water molecules to lower the freezing point. This suppresses ice crystal growth, protecting the fragile acrosomal and plasma membranes from mechanical lysis. It is standardly added at 6-8% in Tris-citric-egg yolk extenders.",
        "Why_Not": "DMSO and ethylene glycol are primary cryoprotectants for embryos, but are highly spermatotoxic to spermatozoa at standard processing temperatures, making glycerol the exclusive standard.",
        "Wow_Approach": "Always allow an equilibration period of 2-4 hours at 4°C after adding glycerol-containing extenders. This gives glycerol sufficient time to fully penetrate the membrane before freezing."
    },
    1374: {
        "topic": "Exam Guidelines - VGO Objective Section Time Limit (Repeated)",
        "Core_Anatomy": "N/A - Examination Rules.",
        "Pathogenesis_Immediate": "University regulations dictate that the objective Part-A paper must be completed in the first 30 minutes and handed over to the Hall Superintendent.",
        "Pathogenesis_Deep": "This testing structure isolates direct factual recall of reproductive physiology, preventing the use of descriptive cues from essays in Part-B. Evaluated topics include: semen packaging materials, epididymal transit times, and hormonal parameters.",
        "Why_Not": "Part-B contains descriptive clinical essays and surgical procedures which require structured problem-solving.",
        "Wow_Approach": "Rapid-fire recall of quantitative constants is essential for passing the objective section."
    },
    1375: {
        "topic": "VGO Objective Section Header - General Andrology",
        "Core_Anatomy": "Male reproductive system.",
        "Pathogenesis_Immediate": "This header denotes the start of the high-yield objective section, demanding rapid, singular factual answers regarding semen processing and dystocia.",
        "Pathogenesis_Deep": "Familiarity with the test structure is key. Objective fill-in-the-blanks test exact constants (e.g., pelvic area >200 sq cm, glycerol concentrations, and specific anatomical terms like vertex presentation).",
        "Why_Not": "Subjective answers require paragraphs; this section requires absolute precision in terminology.",
        "Wow_Approach": "Use a mental 'first-thought' approach for these blanks; overthinking often leads to replacing the specific anatomical term with a vague generic one."
    },
    1389: {
        "topic": "Vertex Presentation - Forehead Obstruction",
        "Core_Anatomy": "Fetal cranium, vertex/poll, and maternal pelvic brim.",
        "Pathogenesis_Immediate": "A dystocia where the nose of the fetus is caught at the pelvic brim (pointing downwards) and the forehead/poll is entering the pelvic canal is termed a Vertex Presentation.",
        "Pathogenesis_Deep": "Vertex presentation is a specific downward deviation of the head. In a normal anterior presentation, the muzzle rests on the forelimbs and leads into the canal. In a vertex presentation, the fetal neck is slightly flexed so the chin is tucked, and the top of the skull (vertex) impacts the maternal pubis. The nose gets hooked below the brim of the pelvis, completely halting delivery.",
        "Why_Not": "In a nape presentation, the neck is flexed even further down so the back of the neck enters the canal. A lateral deviation involves the head turned to the side (flank).",
        "Wow_Approach": "Correction is straightforward but requires space: repel the fetal chest to push the vertex back into the uterus, cup the muzzle, and lift the nose upward over the pelvic brim."
    },
    1390: {
        "topic": "Labor Stages - Merging in Polytocous Species",
        "Core_Anatomy": "Uterine myometrium, cervix, and placentas.",
        "Pathogenesis_Immediate": "The second (fetal expulsion) and third (placental expulsion) stages of labor are merged and occur simultaneously/alternatingly in Polytocous (litter-bearing) animals like the Sow and Bitch.",
        "Pathogenesis_Deep": "In monotocous animals (cows, mares), parturition is strictly sequential: Stage 2 (delivery of the single fetus) followed hours later by Stage 3 (expulsion of the fetal membranes). In polytocous species, the delivery of the litter takes several hours. A fetus is expelled, followed almost immediately by its corresponding placenta, then the next fetus, then its placenta. Thus, the stages are functionally merged.",
        "Why_Not": "Pluriparous refers to an animal that has had multiple pregnancies, not necessarily litters. Monotocous animals deliver one offspring at a time and have distinct, separated stages of labor.",
        "Wow_Approach": "In the bitch, do not forcibly pull on a retained placenta between puppies. Wait for the delivery of the next puppy or administer a micro-dose of oxytocin after the last pup is born to clear the remaining membranes."
    },
    1391: {
        "topic": "Bovine Pelvimetry - Protective Pelvic Area Threshold",
        "Core_Anatomy": "Maternal bony pelvis (ilium, ischium, pubis).",
        "Pathogenesis_Immediate": "The incidence of dystocia is significantly less in cows (and particularly heifers) with a measured pelvic area of above 200-240 square cm (cm²).",
        "Pathogenesis_Deep": "Pelvic area is calculated by multiplying the internal vertical diameter by the transverse diameter using a Rice pelvimeter. A pelvic area <140-150 cm² in a yearling heifer almost guarantees fetopelvic disproportion and severe dystocia. An area >200 cm² (up to 240 cm² in mature cows) provides a massive birth canal that easily accommodates the standard 35-45 kg birth weight of beef/dairy calves, reducing dystocia rates to near zero.",
        "Why_Not": "Square millimeters (mm) is anatomically microscopic. The measurement must be in square centimeters (cm²).",
        "Wow_Approach": "Many commercial beef operations aggressively cull replacement heifers with a pelvic area below 150 cm² at 12-14 months of age to eliminate the genetics for narrow pelvises from the herd."
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
