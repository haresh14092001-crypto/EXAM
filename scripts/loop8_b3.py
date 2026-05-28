import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    864: {
        "topic": "Andrology True/False - Testicular Pathology and Breeding Vices",
        "Core_Anatomy": "Testicular parenchyma, HPG axis, and male neural behavior.",
        "Pathogenesis_Immediate": "True/False section covering male reproductive vices, testicular histology, cryptorchid tumor risks, semen cryo-survival limits, and libido assessments.",
        "Pathogenesis_Deep": "These statements evaluate clinical knowledge of: (1) Pathological behaviors (vices like masturbation, coital failure) which are highly correlated with management and confinement. (2) Testicular composition (seminiferous tubules make up >80% of weight, Leydig cells are a minor fraction). (3) Cryptorchidism (highly predisposed to neoplastic transformation). (4) Cryopreservation limits (liquid nitrogen storage is theoretically indefinite, not limited to 5 years).",
        "Why_Not": "These biological constants represent highly critical QA steps in breeding bull management. Misunderstanding semen lifespan or testicular weight distribution leads to poor clinical diagnostics.",
        "Wow_Approach": "To master male breeding soundness exams: always correlate physical parameters (scrotal circumference) with behavioral parameters (libido scored by reaction time) to provide a comprehensive breeding potential index."
    },
    866: {
        "topic": "Breeding Vices in Males - Management and Exercise Prevention",
        "Core_Anatomy": "Central nervous system, hypothalamic reward pathways, and pelvic musculature.",
        "Pathogenesis_Immediate": "The statement 'Proper management and exercise generally prevents development of vices in male animals' is TRUE. Confinement, isolation, and lack of exercise are major etiologies.",
        "Pathogenesis_Deep": "Male breeding vices (e.g., masturbation in stallions, mounting failure in bulls, preputial sucking in boars) are abnormal behaviors that impair breeding efficiency. They often arise due to boredom, high-energy rations combined with close confinement (lack of physical exercise), and sensory isolation from receptive females. Regular exercise (e.g., pasture walking, lunging) increases endorphins, reduces stress, burns excess energy, and improves physical stamina, preventing these destructive behavioral patterns.",
        "Why_Not": "Vices are rarely due to primary organic disease. Hormonal treatments are ineffective and often worsen the behavior. Environmental enrichment and exercise are the primary preventive strategies.",
        "Wow_Approach": "In stallions, masturbation (spontaneous ejaculation or penile rubbing) can be managed by using a stallion ring (a rubber ring placed on the penis that causes mild discomfort during erection), but the most effective treatment remains regular lunging exercise and pasture socialization."
    },
    868: {
        "topic": "Balling Up - Penile Deviation Vice in Bulls",
        "Core_Anatomy": "Sigmoid flexure, retractor penis muscle, prepuce, and penile raphe.",
        "Pathogenesis_Immediate": "The statement ''Balling up' is one of the vices in males that occurs commonly in boars' is FALSE. 'Balling up' is a pathological vice/defect that occurs in Bulls during attempted service.",
        "Pathogenesis_Deep": "In bulls, 'balling up' (also known as penile telescoping or preputial invagination) occurs when the bull attempts to mount a cow but fails to achieve proper penile intromission. As he thrusts, the erect penis presses against the cow's perineum. Instead of penetrating, the penile shaft bends or curls back inside the loose prepuce, forming a loop or 'ball'. The thrusting force is transmitted into the prepuce, causing severe preputial trauma, hematoma, or rupture of the retractor penis muscle. It is common in bulls with poor libido or inexperienced mounting behavior.",
        "Why_Not": "Boars have a corkscrew-type penis tip that locks into the sow's cervix, preventing telescoping or 'balling up'. 'Balling up' is strictly a bovine-specific mechanical failure of intromission.",
        "Wow_Approach": "To prevent 'balling up' in young bulls: provide experienced teaser cows, ensure the breeding pen floor is non-slip, and closely supervise the first 5 matings. Young bulls that develop this habit due to initial failures should be retrained or culled."
    },
    871: {
        "topic": "Testicular Histology - Seminiferous Tubule Dominance",
        "Core_Anatomy": "Testicular parenchyma, seminiferous tubules, Leydig cells, and interstitial space.",
        "Pathogenesis_Immediate": "The statement 'About 80% testicular weight is made up of leydig cells' is FALSE. In mature domestic animals, the seminiferous tubules make up 80-90% of the total testicular weight.",
        "Pathogenesis_Deep": "The testicular parenchyma consists of: (1) The tubular compartment (seminiferous tubules containing Sertoli cells and germ cells undergoing spermatogenesis), which occupies 80-90% of the total testicular volume and weight. (2) The interstitial compartment (containing Leydig cells, blood vessels, lymphatics, and connective tissue), which occupies only 10-20% of the weight. Leydig cells themselves make up only a small fraction (often <5-8%) of the total testicular mass. This is why scrotal circumference is highly correlated with daily sperm production (tubular function), not just testosterone levels (interstitial function).",
        "Why_Not": "If Leydig cells occupied 80% of the weight, the testis would have an extremely small capacity for sperm production, resulting in severe oligozoospermia. The vast majority of the testis must be dedicated to germ cell meiosis.",
        "Wow_Approach": "To diagnose tubular vs. interstitial degeneration in a sterile bull with normal testosterone: perform a scrotal ultrasound. A decrease in testicular size with increased hyperechogenic stromal lines indicates tubular atrophy (loss of the 80% tubular mass) while Leydig cells may remain functional."
    },
    872: {
        "topic": "Testicular Hypoplasia - Age of Diagnosis in Bulls",
        "Core_Anatomy": "Testicular parenchyma, scrotal skin, and epididymis.",
        "Pathogenesis_Immediate": "The statement 'Testicular hypoplasia can be diagnosed at one year of age in bull' is TRUE (or FALSE depending on management, but clinically it is highly reliable by 12-14 months when puberty is fully established).",
        "Pathogenesis_Deep": "Testicular hypoplasia is a congenital, often hereditary (recessive autosomal) defect characterized by a failure of the seminiferous tubules to develop. At 12 months of age (standard puberty age for beef and dairy bulls), the scrotal circumference and testicular size should be fully recorded during Breeding Soundness Evaluation (BSE). A bull with testicular hypoplasia will present with abnormally small, firm testes (<28 cm scrotal circumference at 12 months) and azoospermia or severe oligozoospermia. While transient prepubertal delay is possible, a definitive diagnosis is highly reliable at one year of age.",
        "Why_Not": "Waiting until 2 years of age is uneconomical and risks breeding heifers to a subfertile bull. Diagnosing before 8 months is premature because normal prepubertal testicular growth is still actively progressing.",
        "Wow_Approach": "Testicular hypoplasia was historically linked to the white heifer disease gene in Swedish Red and White cattle. Affected bulls must be culled immediately, as they will transmit the hypoplasia gene to their offspring, causing ovarian hypoplasia in heifers."
    },
    873: {
        "topic": "Cryptorchidism - Neoplastic Predisposition in Retained Testes",
        "Core_Anatomy": "Abdominal cavity, inguinal canal, scrotum, and testicular germ/Sertoli cells.",
        "Pathogenesis_Immediate": "The statement 'Tumours are more common in cryptorchid males' is TRUE. Retained testes have up to a 13-fold higher risk of developing neoplasia.",
        "Pathogenesis_Deep": "Cryptorchidism is the failure of one (unilateral) or both (bilateral) testes to descend into the scrotum. The abdominal or inguinal environment is maintained at core body temperature, which is 2-4°C higher than the scrotum. This chronic elevated temperature suppresses normal spermatogenesis but stimulates the proliferation of Sertoli cells and germ cells. The result is a highly increased risk of neoplastic transformation, particularly: (1) Sertoli cell tumors (which secrete high estrogen, causing feminization syndrome in dogs). (2) Seminomas (germ cell tumors). It is most common in dogs, horses, and boars.",
        "Why_Not": "Normal scrotal testes are protected by thermoregulatory mechanisms (cremaster muscle, dartos, pampiniform plexus), maintaining a cool temperature that suppresses the hyperplastic pathways that lead to tumor formation.",
        "Wow_Approach": "Feminization syndrome in a cryptorchid dog: look for bilateral symmetrical alopecia, hyperpigmentation of the groin, gynecomastia (enlarged mammary glands), pendulous prepuce, and attraction of other male dogs. This confirms an estrogen-secreting Sertoli cell tumor in the retained testis, requiring emergency laparotomy."
    },
    874: {
        "topic": "Semen Cryopreservation - Indefinite Lifespan in Liquid Nitrogen",
        "Core_Anatomy": "Sperm cell cytoplasm, membrane lipids, and cryogenic storage compartment.",
        "Pathogenesis_Immediate": "The statement 'The life span of frozen semen is five years' is FALSE. When properly stored in liquid nitrogen at -196°C, the life span of frozen semen is theoretically indefinite.",
        "Pathogenesis_Deep": "At -196°C, all metabolic and enzymatic activities of the spermatozoon are completely suspended. There is no biochemical degradation, membrane lipid peroxidation, or DNA damage. Sperm cells can remain viable in this cryogenic state for decades. Successful conceptions and healthy offspring have been achieved using bovine semen that was frozen for over 40-50 years. The only limiting factor is the physical maintenance of the liquid nitrogen level in the storage flask; dry-out causes immediate recrystallization and death of all sperm.",
        "Why_Not": "A 5-year limit is a marketing or logistical shelf-life recommendation for certain species, but possesses no biological basis under proper liquid nitrogen storage. The physical suspension of life is complete.",
        "Wow_Approach": "To prevent accidental damage during storage: never lift semen straws above the 'frost line' (neck of the liquid nitrogen tank) for more than 5 seconds. Exposing straws to the warmer neck region (-80 to -120°C) triggers partial ice recrystallization, severely reducing post-thaw progressive motility."
    },
    875: {
        "topic": "Libido Assessment - Reaction Time as a Behavioral Metric",
        "Core_Anatomy": "Hypothalamus, optic and olfactory tracts, and pelvic motor pathways.",
        "Pathogenesis_Immediate": "The statement 'Libido of the bull can be assessed by the reaction time' is TRUE. Reaction time is the standard, quantifiable metric of sexual desire.",
        "Pathogenesis_Deep": "Libido is the sexual desire or drive of the male, which is independent of semen quality. In breeding soundness evaluations, libido is assessed by placing the bull in a pen with a teaser animal (restrained cow) and measuring the 'reaction time'. Reaction time is defined as the time interval (in seconds or minutes) from the moment the bull is introduced to the teaser until he makes the first active mount with attempt at intromission. A highly fertile bull with strong libido should have a reaction time under 2-3 minutes.",
        "Why_Not": "Evaluating semen volume or motility under the microscope evaluates testicular/accessory gland function, not the central nervous system drive. Reaction time is the only direct behavioral measure of libido.",
        "Wow_Approach": "To standardize libido scoring: bulls are graded on a scale of 0 to 10. A score of 9-10 indicates rapid interest, active courtship (nuzzling, Flehmen reaction), and mounting within 1 minute. A score of 0 indicates complete lack of interest after 10 minutes, indicating poor breeding potential."
    },
    877: {
        "topic": "Andrology Short Notes - Core Clinical Concepts",
        "Core_Anatomy": "Male reproductive system and processing laboratory.",
        "Pathogenesis_Immediate": "Descriptive short notes in Andrology focus on: Semen extenders, Cryptorchidism, Electroejaculation, Testicular Biopsy, and Breeding Soundness Evaluation (BSE).",
        "Pathogenesis_Deep": "Each short-note topic requires structured clinical formatting: (1) Semen extenders: discuss composition (buffers, cryoprotectants, nutrients, antibiotics) and freezing steps. (2) Cryptorchidism: discuss inheritance (polygenic recessive), unilateral vs bilateral, tumor risks (Sertoli cell, seminoma), and diagnosis. (3) Electroejaculation: discuss physiological pathway (pelvic nerve stimulation), advantages (injured/wild bulls), and limitations (highly diluted seminal fraction). (4) Testicular Biopsy: discuss techniques (Tru-Cut needle), indications (azoospermia), and complications (hematoma, testicular degeneration due to pressure).",
        "Why_Not": "Vague descriptions without scientific terms (e.g., failing to mention glycerol in extenders or temperature in AVs) will fail final academic grading, as the candidate must demonstrate laboratory and clinical competency.",
        "Wow_Approach": "When writing on Electroejaculation, always explain the safety protocol: use a rectal probe with segmented electrodes, start at 0 volts, gradually increase to a peak of 10-15 volts in rhythmic 3-second pulses, and immediately turn off the current if the bull exhibits tetanic muscle spasms."
    },
    883: {
        "topic": "Veterinary Andrology Exam - Part-A Guidelines",
        "Core_Anatomy": "Male reproductive system parameters.",
        "Pathogenesis_Immediate": "TANUVAS academic regulations state that the objective Part-A paper for Veterinary Andrology (VGO-511) must be completed in the first hour and handed over to the hall superintendent.",
        "Pathogenesis_Deep": "The objective paper assesses factual recall of: normal scrotal circumference minimums, semen diluent chemical formulations, cooling curves (-0.5°C/min down to 4°C), and specific sperm morphological defect classifications. Separating this section ensures that basic science knowledge is tested independently before the student begins descriptive essays in Part-B.",
        "Why_Not": "Part-B evaluates clinical case management and surgical procedures (e.g., correction of penile hematoma or cryptorchidectomy), which require structured, detailed essays.",
        "Wow_Approach": "Familiarize yourself with the exact grading weight: Part-A carries 60 marks of highly granular factual questions. Prioritize memorizing normal physiological values (e.g., stallion gel-free semen volume, boar preputial fluid chemistry) to maximize scores."
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
