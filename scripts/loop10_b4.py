import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1167: {
        "topic": "Canine Artificial Insemination - Sperm Dosage (Repeated MCQ)",
        "Core_Anatomy": "Vaginal vault, cervix, and canine uterine lumen.",
        "Pathogenesis_Immediate": "The minimum recommended progressively motile sperm dosage required per breeding in the Bitch for optimum conception rate is 150 to 200 million.",
        "Pathogenesis_Deep": "Successful fertilization in the bitch requires a high critical mass of sperm to traverse the vaginal vault. Ejaculates normally contain 200-1000 million. When using chilled or frozen semen, depositing fewer than 150 million results in a significant drop in conception rates and litter sizes.",
        "Why_Not": "A dose of 20 million is typical for bovine AI (using highly fertile frozen semen), but is far too low for dogs, where natural vaginal deposition requires much larger numbers due to the absence of the uterine body deposition achieved in cattle.",
        "Wow_Approach": "To optimize success with low-dose or poor-quality stud semen: perform Transcervical Insemination (TCI) using a rigid endoscope to deposit the semen directly into the uterine body."
    },
    1168: {
        "topic": "Coital Lock in Bitches - Bulbous Glandis and Constrictor Vulvae (Repeated MCQ)",
        "Core_Anatomy": "Male glans penis (bulbous glandis) and female vestibular sphincter.",
        "Pathogenesis_Immediate": "The characteristic coital lock in dogs occurs due to the rapid engorgement of the male's Bulbous Glandis coupled with the contraction of the female's Constrictor Vulvae muscle.",
        "Pathogenesis_Deep": "Post-intromission, the bulbous glandis swells to 2-3x its flaccid diameter. The female's vestibular sphincter and constrictor vulvae contract tightly behind it, locking the penis inside the vagina. This lock lasts 10-30 minutes, during which the male ejaculates the prostatic fraction.",
        "Why_Not": "The os penis facilitates initial penetration but does not cause the lock. A corkscrew-type penis is unique to the boar. The lock is strictly driven by the swollen bulbous glandis held by the constrictor vulvae.",
        "Wow_Approach": "The prostatic third fraction of canine semen is ejaculated exclusively during the coital lock, serving to flush the sperm-rich second fraction forward into the uterine body."
    },
    1169: {
        "topic": "Ventral Phimosis - Persistent Frenulum in Bulls (Repeated MCQ)",
        "Core_Anatomy": "Penile raphe, prepuce, and glans penis.",
        "Pathogenesis_Immediate": "Ventral deviation of the penis is most commonly caused by a Persistent Frenulum in young bulls.",
        "Pathogenesis_Deep": "Shortly before puberty, testosterone drives the active separation of prepuce and penis. A persistent frenulum occurs when a band of collagenous connective tissue fails to rupture, leaving the ventral glans bound. At erection, this tethers the penis downward in a ventral arc ('rainbow' penis).",
        "Why_Not": "A short penile shaft causes inability to protrude, but not focal ventral curvature. Penile hematoma results from rupture of the tunica albuginea, causing a swelling cranial to the scrotum.",
        "Wow_Approach": "Surgical correction is highly straightforward: under local infiltration, exteriorize the penis, clamp and cut the persistent frenulum, and place a single absorbable suture at the mucosal edges."
    },
    1170: {
        "topic": "Semen Terminology - Asthenozoospermia and Sperm Motility (Repeated MCQ)",
        "Core_Anatomy": "Sperm middle piece (mitochondria) and flagellum.",
        "Pathogenesis_Immediate": "The scientific terminology used to denote reduced or sub-optimal sperm motility in an ejaculate is Asthenozoospermia.",
        "Pathogenesis_Deep": "Asthenozoospermia is defined as <30% progressive motility, often associated with mitochondrial damage in the middle piece or structural defects in the axoneme. In contrast, oligozoospermia refers to low sperm count, and teratozoospermia refers to high morphologic defects.",
        "Why_Not": "Oligozoospermia relates to sperm count, not motility. Hypospermia relates to abnormally low ejaculate volume. Teratozoospermia relates to morphologic defects.",
        "Wow_Approach": "Use Computer-Assisted Sperm Analysis (CASA) to get objective motility scores, measuring average path velocity (VAP) and straight-line velocity (VSL)."
    },
    1171: {
        "topic": "Reproductive Anatomy Fill-In - Efferent Ducts and Boar Penis",
        "Core_Anatomy": "Rete testis, efferent ductules, epididymal duct, and the porcine penis.",
        "Pathogenesis_Immediate": "The efferent ducts (vasa efferentia) in the mammalian testis converge at the caput region into a single, highly convoluted duct called the Epididymis (epididymal duct). The pathognomonic 'corkscrew' type of penis is seen in the Boar (swine).",
        "Pathogenesis_Deep": "These anatomical structures represent key mammalian adaptations: (1) The vasa efferentia (12-15 small tubes) absorb up to 90% of the fluid leaving the rete testis, concentrating sperm before converging into the single epididymal duct (which is up to 50-80 meters long when uncoiled). (2) The boar possesses a fibroelastic penis with a distinct, counter-clockwise spiral or 'corkscrew' tip. During copulation, the spiral tip locks mechanically into the interlocking cervical rings (pulvini cervicales) of the sow, allowing high-pressure deposition of the massive ejaculate volume.",
        "Why_Not": "Efferent ducts do not lead directly into the vas deferens, which is strictly the exit continuation of the epididymal tail. Bulls and rams have a straight glans penis tip with a urethral process, not a spiral corkscrew.",
        "Wow_Approach": "Because the boar's penis corkscrews into the cervix, porcine AI catheters are designed with a spiral or 'corkscrew' rubber tip. The technician must rotate the catheter counter-clockwise during insertion to mimic the natural locking mechanism."
    },
    1178: {
        "topic": "Andrology Matching - Male Reproductive Structures and Pathology (Repeated)",
        "Core_Anatomy": "Comparative male reproductive systems across species.",
        "Pathogenesis_Immediate": "Key matching pairs in Andrology: Boar matches to the preputial diverticulum; Stallion matches to vascular penis; Cavernous bodies match to erection of penis; Artificial Vagina matches to thermal/mechanical semen collection stimulation; Benign Prostatic Hyperplasia matches to Dihydrotestosterone.",
        "Pathogenesis_Deep": "These pairs cover male reproductive adaptations: (1) The boar possesses a preputial diverticulum, a dorsal pouch that accumulates urine and degenerated cells, producing the characteristic foul odor of boars. (2) The stallion has a vascular penis with highly distensible cavernous tissue, which increases massively in length and diameter during erection. (3) BPH in older dogs is driven by DHT (dihydrotestosterone), which stimulates glandular cell hypertrophy.",
        "Why_Not": "Ruminants (bulls, rams) have a fibroelastic penis with a sigmoid flexure that does not increase in diameter during erection, relying on the retractor penis muscle. Prostatitis is marked by white blood cells in semen, not by vascular penis changes.",
        "Wow_Approach": "During breeding soundness exams in boars: the preputial diverticulum must be regularly checked for accumulation of fluid or calculi, which can harbor pathogens like Pseudomonas or Actinobacillus. Emptying the diverticulum manually before natural mating reduces bacterial contamination of the sow."
    },
    1179: {
        "topic": "Boar Reproduction - Preputial Diverticulum and Semen Gel Fraction",
        "Core_Anatomy": "Porcine prepuce, preputial diverticulum, and Cowper's glands.",
        "Pathogenesis_Immediate": "The Boar possesses a dorsal Preputial Diverticulum (a bilateral pouch within the dorsal wall of the prepuce) and ejaculates a massive volume of semen (150-300 ml) containing a thick gel fraction.",
        "Pathogenesis_Deep": "The boar's preputial diverticulum accumulates a mixture of urine, semen residues, and desquamated epithelial cells, which undergoes anaerobic bacterial fermentation. This produces a strong, pungent pheromonal odor (containing androstenone and copulins) that acts as a powerful sexual stimulant for the sow. However, it is also a major reservoir for pathogens. During collection, this fluid must be expressed manually to prevent semen contamination. The gel fraction (tapioca-like substance) is secreted by the massive Cowper's glands, serving to plug the cervix after mating.",
        "Why_Not": "Bulls, rams, and stallions do not possess a preputial diverticulum. The stallion's gel fraction is secreted by the seminal vesicles, whereas in the boar it is strictly bulbourethral (Cowper's) in origin.",
        "Wow_Approach": "AI centers use a double-gloved hand technique for boar semen collection: the technician wears an outer glove to express the dirty preputial fluid, discards it, and then uses the sterile inner glove to grip the spiral penis tip, mimicking cervical pressure to trigger ejaculation."
    },
    1180: {
        "topic": "Stallion Reproduction - Vascular Penis and High-Volume Ejaculation (Repeated)",
        "Core_Anatomy": "Equine glans penis and musculocavernous tissue.",
        "Pathogenesis_Immediate": "The Stallion has a vascular (musculocavernous) penis that expands dramatically in length and diameter during erection, and ejaculates 50-150 ml of semen directly transcervically.",
        "Pathogenesis_Deep": "In the stallion's musculocavernous penis, parasympathetic nitric oxide release triggers massive vasodilation of the helicine arteries, flooding the cavernous spaces. Ejaculation is multi-phasic: the sperm-rich fraction is expelled in 5-8 jets directly into the uterine body, followed by a gel-like vesicular fraction.",
        "Why_Not": "Bulls, rams, and boars have a fibroelastic penis with minimal cavernous space and a rigid sigmoid flexure. Sows have a long, twisted cervix that accommodates the corkscrew boar penis.",
        "Wow_Approach": "Because the stallion ejaculates transcervically, equine AI requires depositing the semen into the uterine body using a flexible pipet to maximize fertility."
    },
    1181: {
        "topic": "Sperm Morphology - Detached Heads as Secondary Defects (Repeated)",
        "Core_Anatomy": "Sperm head, implantation fossa, and capitulum.",
        "Pathogenesis_Immediate": "A detached head (separation of the sperm head from the tail) is classified as a secondary sperm abnormality, arising primarily during epididymal transit or sample collection/handling.",
        "Pathogenesis_Deep": "Detached heads occur due to fragility at the capitulum (implantation fossa) where the tail attaches to the head, often triggered by rough handling, agitation, or temperature shocks during semen processing. In contrast, primary defects arise in the testes.",
        "Why_Not": "Primary defects indicate severe testicular dysfunction or degeneration, whereas secondary defects are often manageable by improving semen handling techniques, reducing collection frequency, or treating epididymal sub-acute inflammation.",
        "Wow_Approach": "A detached head count >20% indicates 'decapitated sperm defect' (a genetic fragility of the basal plate seen in Hereford bulls) or severe chronic epididymitis, both causing sterility."
    },
    1182: {
        "topic": "Corpora Cavernosa - Erection Mechanics in Males (Repeated)",
        "Core_Anatomy": "Corpus cavernosum and tunica albuginea.",
        "Pathogenesis_Immediate": "The corpora cavernosa are the main erectile tissue structures of the penis, responsible for providing the mechanical rigidity and expansion required for Erection.",
        "Pathogenesis_Deep": "During erection, nitric oxide (NO) stimulates cGMP-mediated arterial relaxation. In vascular penises, blood floods the cavernous bodies, expanding the tissue. In fibroelastic penises, blood fills the cavernous spaces under extremely high pressure (>1,000 mmHg), straightening the sigmoid flexure.",
        "Why_Not": "The corpus spongiosum serves to keep the urethral lumen open during ejaculation, whereas the corpora cavernosa are high-pressure vascular compartments specifically designed for mechanical rigidity.",
        "Wow_Approach": "In the bull, rupture of the thick tunica albuginea surrounding the cavernous bodies under the extreme pressure of mounting causes 'penile hematoma' ('broken penis'), a major breeding emergency."
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
