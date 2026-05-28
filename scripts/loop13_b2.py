import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1475: {
        "topic": "Sperm Viability - Canine Uterine Survival",
        "Core_Anatomy": "Canine endometrium and sperm plasma membrane.",
        "Pathogenesis_Immediate": "The viability of dog sperms in the reproductive tract of bitches is exceptionally long, lasting for 4 to 7 days.",
        "Pathogenesis_Deep": "Canine reproduction is uniquely adapted for delayed fertilization. The bitch ovulates primary oocytes (which require 2-3 additional days to mature into fertilizable secondary oocytes in the oviduct). To ensure fertilization, canine spermatozoa can survive, remain motile, and retain fertilizing capacity deep within the endometrial crypts for up to 7 days post-mating, slowly releasing to meet the maturing eggs.",
        "Why_Not": "In cattle and horses, sperm only survive 24-48 hours in the female tract. Selecting 1-2 days for a dog completely ignores their unique evolutionary adaptation for prolonged uterine survival.",
        "Wow_Approach": "Because of this 7-day survival, a bitch can be mated by multiple different sires over a week-long period and deliver a single litter with multiple different fathers (superfecundation)."
    },
    1476: {
        "topic": "Seminiferous Tubules - Total Length in Bulls (Repeated MCQ)",
        "Core_Anatomy": "Testicular parenchyma and seminiferous epithelium.",
        "Pathogenesis_Immediate": "The combined total length of the seminiferous tubules in a normal adult bull is approximately 5000 meters (5 km).",
        "Pathogenesis_Deep": "The testis is a massive factory optimized for surface area. The seminiferous tubules are highly convoluted loops that pack tightly into the testicular lobules. If uncoiled and laid end-to-end, the tubules from a single mature bull testis would stretch for several kilometers (3000-5000 meters). This massive surface area is required to support the production of billions of spermatozoa every single day.",
        "Why_Not": "Lengths of 5-10 meters severely underestimate the microscopic convolution required for spermatogenesis.",
        "Wow_Approach": "This total length is directly correlated with Scrotal Circumference. A larger circumference means more tubular length, which mathematically guarantees higher daily sperm production."
    },
    1477: {
        "topic": "Spermatocytogenesis - Bovine Proliferation Phase",
        "Core_Anatomy": "Seminiferous epithelium (basal compartment).",
        "Pathogenesis_Immediate": "Spermatocytogenesis (the mitotic and initial meiotic phases of spermatogenesis) takes approximately 45 days in bulls.",
        "Pathogenesis_Deep": "Spermatogenesis has three phases: (1) Spermatocytogenesis: Mitotic proliferation of spermatogonia into primary spermatocytes, followed by meiosis I to form secondary spermatocytes (~45 days). (2) Spermiogenesis: The morphological differentiation of round spermatids into elongated spermatozoa (~15 days). Total spermatogenesis in the bull takes ~60-61 days.",
        "Why_Not": "25 or 35 days underestimates the time required for the massive mitotic amplification divisions. 55 days is almost the entire duration of total spermatogenesis, not just the cytogenesis phase.",
        "Wow_Approach": "Because the mitotic phase (spermatocytogenesis) is so long and metabolically demanding, it is highly susceptible to heat stress, radiation, and toxins."
    },
    1486: {
        "topic": "Anesthesia Matching - Paravertebral Block",
        "Core_Anatomy": "Thoracolumbar spinal nerves (T13, L1, L2).",
        "Pathogenesis_Immediate": "The Paravertebral block is matched to standing flank laparotomies (e.g., C-sections or rumenotomies) in cattle.",
        "Pathogenesis_Deep": "A paravertebral block desensitizes the dorsal and ventral rami of the spinal nerves T13, L1, and L2 as they exit the intervertebral foramina. This provides complete anesthesia and muscle relaxation of the entire flank from the skin down to the peritoneum. It is the gold standard for standing C-sections because it avoids the toxicity of massive local infiltration (line block) and does not affect the hindlimbs (unlike a high epidural).",
        "Why_Not": "It is not matched to 'rectal copulation'—that is an anatomical anomaly or a behavioral vice, unrelated to flank anesthesia.",
        "Wow_Approach": "A successful paravertebral block causes the cow's spine to physically curve (scoliosis) towards the blocked side due to the unilateral relaxation of the epaxial muscles, confirming the block is working."
    },
    1496: {
        "topic": "VGO-II Syllabus Header - Transition to Obstetrics",
        "Core_Anatomy": "Maternal pelvis and gravid uterus.",
        "Pathogenesis_Immediate": "This header signifies the transition into applied obstetrics, dystocia management, and male breeding soundness.",
        "Pathogenesis_Deep": "Mastery in this section requires the integration of anatomical geometry (pelvimetry), endocrinology (parturition induction), and pharmacology (epidurals and tocolytics).",
        "Why_Not": "VGO-I primarily tests normal estrous cycles and basic AI.",
        "Wow_Approach": "Approach these questions by visualizing the spatial alignment of the fetus relative to the maternal birth canal."
    },
    1498: {
        "topic": "Colpotomy - Vaginal Surgical Approach",
        "Core_Anatomy": "Anterior vagina and peritoneal cavity.",
        "Pathogenesis_Immediate": "Colpotomy is defined as a surgical incision made directly through the wall of the vagina to access the pelvic/abdominal cavity.",
        "Pathogenesis_Deep": "In large animal surgery (primarily equine and bovine), colpotomy is used as a minimally invasive approach to the abdomen, completely avoiding a flank or ventral midline incision. The surgeon incises the dorsal fornix of the anterior vagina to enter the peritoneal cavity. It is classically used for routine ovariectomy (spaying) in mares or for removing small granulosa cell tumors, allowing for rapid recovery with no external skin wounds.",
        "Why_Not": "Episiotomy is an incision of the vulva (to prevent tearing during dystocia). Laparotomy is an incision through the flank/abdominal wall. Colpotomy strictly refers to the vagina.",
        "Wow_Approach": "Strict asepsis is impossible in the vagina. Therefore, colpotomy carries a constant inherent risk of introducing ascending vaginal bacteria directly into the peritoneum, requiring rigorous perioperative antibiotics."
    },
    1505: {
        "topic": "VMD-411 Clinical Medicine - General & Systemic Header",
        "Core_Anatomy": "Multi-systemic veterinary medicine.",
        "Pathogenesis_Immediate": "This header marks the transition from Theriogenology into Veterinary Clinical Medicine (VMD).",
        "Pathogenesis_Deep": "VMD-411 evaluates internal medicine, focusing on systemic diseases, metabolic disorders, and clinical symptomatology across all species. Questions in this section test the ability to match classic clinical signs (e.g., regurgitation, epistaxis, anhidrosis) to their specific systemic etiologies.",
        "Why_Not": "Unlike surgery or obstetrics, internal medicine relies heavily on pathognomonic clinical signs and laboratory diagnostics to localize the lesion.",
        "Wow_Approach": "When answering VMD questions, always differentiate between similar signs: e.g., regurgitation (passive, esophageal) vs. vomiting (active, gastric/systemic)."
    },
    1506: {
        "topic": "Anhidrosis - The Non-Sweating Syndrome",
        "Core_Anatomy": "Equine sweat glands and sympathetic beta-2 receptors.",
        "Pathogenesis_Immediate": "The pathological decrease or complete absence of sweating in response to appropriate physiological stimuli (heat/exercise) is known as Anhidrosis.",
        "Pathogenesis_Deep": "Anhidrosis is a severe, life-threatening metabolic condition most commonly seen in horses imported to hot, humid climates ('Florida Summer' syndrome). Chronic overstimulation of the sweat glands by epinephrine leads to the down-regulation or desensitization of the beta-2 adrenergic receptors on the sweat glands. The horse completely loses the ability to sweat, resulting in hyperthermia (temp >105°F), severe tachypnea (panting like a dog), and exercise intolerance.",
        "Why_Not": "Hyperhidrosis is excessive sweating. Anhidrosis is the cessation of sweating, removing the horse's primary mechanism for thermoregulation.",
        "Wow_Approach": "To definitively diagnose anhidrosis, perform the Terbutaline test: inject serial dilutions of terbutaline (a beta-2 agonist) intradermally. A normal horse will sweat profusely at the injection sites; an anhidrotic horse will not respond."
    },
    1507: {
        "topic": "Megaesophagus - Regurgitation vs Vomiting",
        "Core_Anatomy": "Esophageal smooth/striated muscle and vagus nerve.",
        "Pathogenesis_Immediate": "The most common and pathognomonic clinical sign noticed in megaesophagus in dogs is Regurgitation.",
        "Pathogenesis_Deep": "Megaesophagus is the generalized dilation and severe hypomotility of the esophagus (either congenital or acquired via Myasthenia Gravis or dysautonomia). Because peristalsis fails, food and water passively pool in the flaccid esophageal tube. This leads to Regurgitation: the passive, effortless expulsion of undigested, tube-shaped food covered in mucus, without any abdominal heaving or nausea.",
        "Why_Not": "Vomiting is an active, centrally-mediated reflex involving violent abdominal contractions and nausea, originating from the stomach/intestines. Megaesophagus patients regurgitate; they do not vomit.",
        "Wow_Approach": "Megaesophagus patients almost always die from Aspiration Pneumonia, because the pooled esophageal contents easily spill over the arytenoids into the trachea, especially when the dog is sleeping."
    },
    1508: {
        "topic": "Hemorrhage Terminology - Clinical Manifestations",
        "Core_Anatomy": "Respiratory, gastrointestinal, and nasal mucosa.",
        "Pathogenesis_Immediate": "Clinical terminology for hemorrhage specifies the exact anatomical origin: Haemoptysis (coughing blood), Epistaxis (nosebleed), and Melena (digested blood in stool).",
        "Pathogenesis_Deep": "Precision in terminology localizes the lesion: (1) Haemoptysis indicates bleeding in the lower airways/lungs (e.g., EIPH in racehorses or heartworm disease). (2) Epistaxis indicates bleeding from the nasal cavity (e.g., ethmoid hematoma). (3) Melena indicates upper GI bleeding (stomach/small intestine) where the blood is digested into a black, tarry stool. (4) Hematochezia indicates lower GI bleeding (colon/rectum) where the blood remains bright red.",
        "Why_Not": "Confusing haemoptysis with epistaxis could lead you to scope the lungs when the tumor is actually in the nasal passages.",
        "Wow_Approach": "If a dog presents with severe melena, the two primary differentials are always NSAID-induced gastric ulcers or severe hookworm (Ancylostoma) infestation."
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
