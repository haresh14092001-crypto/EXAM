import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2597: {
        "topic": "Hare Lip - Cheiloplasty",
        "Core_Anatomy": "Lips and maxilla (primary palate).",
        "Pathogenesis_Immediate": "Hare lip (cleft lip / cheiloschisis) is surgically corrected via Cheiloplasty.",
        "Pathogenesis_Deep": "Hare lip is a congenital defect where the embryonic maxillary and medial nasal processes fail to fuse, leaving a fissure in the upper lip. It often occurs concurrently with a cleft palate (palatoschisis). The surgical repair is termed Cheiloplasty. The procedure involves carefully excising the epithelialized margins of the cleft to expose healthy vascular connective tissue, then reconstructing the lip in three layers (mucosa, muscle/orbicularis oris, and skin) to ensure functional sphincter competence and a cosmetic result.",
        "Why_Not": "V-Y plasty is for ectropion. Saculectomy is for anal glands. Cheiloplasty specifically refers to reconstructive surgery of the lip ('cheilo-' = lip).",
        "Wow_Approach": "Because puppies with hare lip and cleft palate cannot create negative suction to nurse, they must be tube-fed until they are old enough (usually 8-12 weeks) to safely undergo surgical correction."
    },
    2598: {
        "topic": "Ectropion - V-Y Plasty",
        "Core_Anatomy": "Eyelid margin (palpebral conjunctiva).",
        "Pathogenesis_Immediate": "Ectropion (outward rolling of the eyelid) is surgically corrected using a V-Y Plasty.",
        "Pathogenesis_Deep": "Ectropion exposes the palpebral conjunctiva to environmental drying and irritation, causing chronic conjunctivitis. It is common in breeds with excessive facial skin (Bloodhounds, St. Bernards). When ectropion is caused by cicatricial scarring (scar tissue pulling the eyelid downward), the gold standard repair is the V-Y Plasty. A V-shaped incision is made below the eyelid, the skin is undermined and pushed upward to relieve the tension and roll the eyelid back against the cornea, and the defect is sutured closed in a Y-shape.",
        "Why_Not": "Entropion (inward rolling of the eyelid causing corneal scratching) is typically treated with a Hotz-Celsus procedure (removing a crescent of skin). V-Y plasty specifically pushes skin TOWARDS the defect to fix Ectropion.",
        "Wow_Approach": "Ophthalmic surgeries require extreme precision; the eyelid margin must be perfectly aligned during closure using a 'Figure-of-8' suture to prevent a 'step defect' which would permanently irritate the cornea."
    },
    2611: {
        "topic": "Veterinary Surgery and Radiology Module Header",
        "Core_Anatomy": "Systemic surgical principles.",
        "Pathogenesis_Immediate": "Header denoting the start of a new Veterinary Surgery and Radiology (VSR) exam paper.",
        "Pathogenesis_Deep": "VSR exams integrate applied anatomy, pathophysiology, pharmacology (anaesthetics), and physics (radiology).",
        "Why_Not": "This is a structural header, not a clinical question.",
        "Wow_Approach": "The foundational triad of veterinary surgery: Asepsis (Halsted's principles), Haemostasis, and atraumatic tissue handling."
    },
    2612: {
        "topic": "Veterinary Surgery and Radiology Module Header",
        "Core_Anatomy": "Systemic surgical principles.",
        "Pathogenesis_Immediate": "Continuation of the VSR module header.",
        "Pathogenesis_Deep": "This section evaluates the clinician's ability to apply surgical theory to clinical case scenarios.",
        "Why_Not": "Structural header.",
        "Wow_Approach": "Surgery is the ultimate integration of all veterinary preclinical sciences."
    },
    2613: {
        "topic": "Exam Instructions - Hall Superintendent",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Standard examination protocol instruction regarding the submission of the objective paper.",
        "Pathogenesis_Deep": "Strict time management is essential for board exams; the objective portion must be completed rapidly to allow sufficient time for the descriptive/essay section.",
        "Why_Not": "Structural instruction.",
        "Wow_Approach": "If you don't know an MCQ answer immediately, skip it and return later; do not burn time on a 1-mark question at the expense of a 10-mark essay."
    },
    2614: {
        "topic": "Objective Type Questions Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for the objective section (20 half-mark questions).",
        "Pathogenesis_Deep": "These high-speed questions test rapid recall of exact definitions, surgical terms, and anatomical landmarks.",
        "Why_Not": "Structural header.",
        "Wow_Approach": "In surgical MCQs, the most 'conservative' effective treatment is often the correct answer, unless it's an absolute emergency (like a GDV)."
    },
    2615: {
        "topic": "Choose the Correct Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of the multiple-choice section.",
        "Pathogenesis_Deep": "Surgical MCQs often present four viable options where only one is technically optimal for the specific condition described.",
        "Why_Not": "Structural header.",
        "Wow_Approach": "Look for defining keywords in the stem: 'acute' vs 'chronic', 'clean' vs 'contaminated'—these dictate the surgical approach."
    },
    2616: {
        "topic": "Abscess - Abnormal Cavity with Pus",
        "Core_Anatomy": "Subcutaneous or deep tissue pyogenic membrane.",
        "Pathogenesis_Immediate": "An abnormal cavity containing pus is defined as an Abscess.",
        "Pathogenesis_Deep": "An abscess is a localized collection of purulent exudate (pus) formed by tissue necrosis, liquefied by neutrophil enzymes (proteases). Critically, it is surrounded by a newly formed fibrous capsule called a 'pyogenic membrane.' This membrane walls off the infection from the rest of the body, which is a successful immune response, but it also completely blocks systemic antibiotics from penetrating into the cavity. Therefore, the definitive treatment for a mature abscess is always surgical: incision, complete drainage, and copious flushing.",
        "Why_Not": "A cyst is a normal or abnormal epithelium-lined sac containing fluid, not pus. A hematoma contains blood. A tumor is a solid tissue neoplasm. Only an abscess is an abnormal cavity specifically filled with pus.",
        "Wow_Approach": "The classic surgical maxim: 'Ubi pus, ibi evacua' (Where there is pus, let it out). Antibiotics alone will never cure a mature abscess."
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
