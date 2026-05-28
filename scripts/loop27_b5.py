import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3171: {
        "topic": "Cancelled Questions Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a cancelled section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3172: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for fill-in-the-blanks.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3193: {
        "topic": "Multiple Choice Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3194: {
        "topic": "Blepharitis - Eyelid Inflammation",
        "Core_Anatomy": "Eyelids (Palpebrae).",
        "Pathogenesis_Immediate": "Inflammation of the eyelids is clinically termed Blepharitis.",
        "Pathogenesis_Deep": "Blepharitis is a generalized inflammation of the eyelid margins. It often involves the Meibomian (tarsal) glands and is frequently immune-mediated (e.g., puppy strangles/juvenile cellulitis) or parasitic (Demodex mites). The eyelids become severely swollen, alopecic, and crusty.",
        "Why_Not": "Keratitis affects the cornea. Coloboma is a congenital defect (hole) in the eyelid or iris. Keratoma is a horn tumor.",
        "Wow_Approach": "If a young puppy presents with severe, bilateral blepharitis and swollen submandibular lymph nodes, suspect Juvenile Cellulitis. Do NOT treat with antibiotics; it is sterile and immune-mediated, requiring aggressive corticosteroid therapy."
    },
    3195: {
        "topic": "Glaucoma - High IOP",
        "Core_Anatomy": "Anterior chamber.",
        "Pathogenesis_Immediate": "Increased intraocular pressure is called Glaucoma.",
        "Pathogenesis_Deep": "As reviewed, failure of aqueous humor drainage causes a massive spike in IOP, leading to optic nerve crush and rapid blindness.",
        "Why_Not": "Chemosis is swelling of the conjunctiva.",
        "Wow_Approach": "N/A"
    },
    3196: {
        "topic": "Hyphema - Anterior Chamber Hemorrhage",
        "Core_Anatomy": "Anterior chamber and Uvea.",
        "Pathogenesis_Immediate": "Hemorrhage (blood) pooling in the anterior chamber of the eye is termed Hyphema.",
        "Pathogenesis_Deep": "Hyphema usually results from severe blunt force trauma to the globe (e.g., hit by car) tearing the highly vascular iris or ciliary body. It can also be a sign of severe systemic coagulopathy (like rodenticide poisoning) or tick-borne diseases (Ehrlichia). The blood physically blocks vision and can clot in the iridocorneal angle, causing secondary glaucoma.",
        "Why_Not": "Hypopyon is PUS in the anterior chamber. Hemopion and Hydropion are nonsense distractors.",
        "Wow_Approach": "Never treat an eye with hyphema using Atropine drops. Atropine dilates the pupil, which folds the iris tissue back and can restart the bleeding from the torn vessels."
    },
    3197: {
        "topic": "Eye Cancer - Squamous Cell Carcinoma",
        "Core_Anatomy": "Corneoscleral limbus and conjunctiva.",
        "Pathogenesis_Immediate": "Histologically, the classic 'Eye Cancer' of cattle is a Squamous Cell Carcinoma (SCC).",
        "Pathogenesis_Deep": "Bovine Ocular Squamous Cell Carcinoma (Cancer Eye) is the most common neoplasm of cattle. It is strongly linked to UV radiation (sunlight) and a lack of circumocular pigmentation (white-faced Herefords are highly predisposed). The tumor typically starts at the corneoscleral limbus as a small plaque and grows into a massive, necrotic, bleeding cauliflower-like mass that destroys the globe.",
        "Why_Not": "Dermoid is a benign congenital hair/skin defect on the cornea. Keloid is an exaggerated scar.",
        "Wow_Approach": "Early, small SCC lesions can be treated by cryotherapy (freezing) or radiofrequency hyperthermia. Advanced cases require radical extirpation of the entire eye (enucleation or exenteration)."
    },
    3198: {
        "topic": "Czerny Suture Pattern",
        "Core_Anatomy": "Intestinal wall.",
        "Pathogenesis_Immediate": "A specific double-layer intestinal closure (often historically described as an inner Connell/Schmieden and an outer Lembert) is associated with the Czerny suture technique.",
        "Pathogenesis_Deep": "The classic Czerny-Lembert technique is a two-layer closure for the intestine. The 'Czerny' part is an inner, simple continuous or interrupted pattern that penetrates the mucosa (to provide strength and hemostasis). It is then immediately buried by an outer 'Lembert' pattern (an inverting pattern that only grabs the seromuscular layer), ensuring serosa-to-serosa contact for perfect healing.",
        "Why_Not": "Connell penetrates the lumen. Cushing goes down to the submucosa but NOT the lumen. The Czerny is explicitly the inner layer of a double-layer closure.",
        "Wow_Approach": "Modern veterinary surgery rarely uses two-layer intestinal closures because they narrow the lumen too much, predisposing the animal to strictures. A single-layer, simple continuous appositional pattern (using PDS) is the modern gold standard."
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
