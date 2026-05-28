import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3038: {
        "topic": "Antrum Empyema - Maxillary Sinus",
        "Core_Anatomy": "Maxillary sinus.",
        "Pathogenesis_Immediate": "Pus in the 'antrum' (specifically the antrum of Highmore) refers to Empyema of the Maxillary sinus.",
        "Pathogenesis_Deep": "As reviewed previously, maxillary sinusitis/empyema in dogs is almost universally caused by a periapical tooth root abscess of the 4th maxillary premolar (the carnassial tooth). In horses, it can be caused by fractures or infections of the upper cheek teeth (premolars/molars) whose roots extend directly into the maxillary sinus.",
        "Why_Not": "Frontal sinusitis is associated with dehorning in cattle. The term 'antrum' historically specifically designates the maxillary sinus.",
        "Wow_Approach": "N/A"
    },
    3039: {
        "topic": "Glaucoma - Elevated IOP",
        "Core_Anatomy": "Anterior chamber and Iridocorneal angle.",
        "Pathogenesis_Immediate": "The disease condition of the eye marked by a pathological rise in intraocular pressure (IOP) is Glaucoma.",
        "Pathogenesis_Deep": "Glaucoma occurs when the production of aqueous humor (by the ciliary body) exceeds its drainage (through the iridocorneal angle and trabecular meshwork). The fluid builds up, drastically increasing the pressure inside the rigid globe of the eye (normal dog IOP is 15-25 mmHg; glaucoma is often >40-60 mmHg). This massive pressure physically crushes the optic nerve and retinal ganglion cells, causing rapid, irreversible blindness within 24-48 hours if left untreated.",
        "Why_Not": "Cataract is opacity of the lens. Strabismus is a misaligned eye. Keratitis is corneal inflammation.",
        "Wow_Approach": "A dog presenting with a sudden 'red, cloudy, painful eye' is a dire emergency. You must instantly measure the IOP with a Schiotz or Tono-Pen. If it is glaucoma, emergency treatment with IV Mannitol (an osmotic diuretic) is required to literally suck the water out of the eye and save the retina."
    },
    3040: {
        "topic": "Hordeolum (Stye)",
        "Core_Anatomy": "Eyelid margin (Zeis/Moll glands).",
        "Pathogenesis_Immediate": "A localized, acute purulent inflammation of an eyelash hair follicle or its associated sebaceous gland is called a Hordeolum (or Stye).",
        "Pathogenesis_Deep": "A hordeolum is a classic, acute, painful bacterial (usually Staphylococcal) abscess of the eyelash follicles (glands of Zeis or Moll). It points toward the skin surface of the eyelid.",
        "Why_Not": "A Chalazion (meibomian cyst) is a CHRONIC, non-painful, sterile granulomatous inflammation of the Meibomian (tarsal) gland deep inside the eyelid, caused by retained sebaceous secretions, not an acute bacterial follicle infection. Blepharitis is generalized inflammation of the entire eyelid.",
        "Wow_Approach": "While a hordeolum often ruptures and heals on its own with warm compresses, a chalazion usually requires surgical lancing and curettage from the inside (conjunctival surface) of the eyelid."
    },
    3041: {
        "topic": "Keratitis - Corneal Inflammation",
        "Core_Anatomy": "Cornea.",
        "Pathogenesis_Immediate": "Inflammation specifically of the cornea is termed Keratitis.",
        "Pathogenesis_Deep": "Keratitis presents with corneal edema (blue/cloudy appearance), neovascularization (blood vessels growing into the normally clear cornea), and cellular infiltration. It is most commonly caused by corneal ulceration (bacterial/viral/traumatic) or by dry eye (Keratoconjunctivitis Sicca).",
        "Why_Not": "Uveitis is inflammation of the iris, ciliary body, and choroid (the middle layer of the eye).",
        "Wow_Approach": "If a dog has chronic superficial keratitis (Pannus)—a specific immune-mediated disease common in German Shepherds—the cornea becomes infiltrated with pink fleshy granulation tissue and dark pigment, eventually causing blindness. It is treated with lifelong topical cyclosporine or steroids."
    },
    3042: {
        "topic": "Bulla Osteotomy - Middle Ear Disease",
        "Core_Anatomy": "Tympanic bulla (Middle ear).",
        "Pathogenesis_Immediate": "A Bulla Osteotomy is a surgical operation performed to treat severe, chronic diseases of the Middle Ear.",
        "Pathogenesis_Deep": "When chronic otitis externa (outer ear infection) ruptures the tympanic membrane (eardrum), bacteria invade the tympanic bulla, causing Otitis Media. The bulla acts like a closed bony cave, filling with pus and inflammatory polyps that antibiotics cannot clear. A Bulla Osteotomy involves surgically drilling a hole into the ventral aspect of the tympanic bulla (accessed through the ventral neck in cats/dogs) to physically curette out the pus, necrotic bone, and polyps, providing permanent drainage.",
        "Why_Not": "The external ear is treated with a Total Ear Canal Ablation (TECA). The internal ear is rarely operated on directly. The bulla osteotomy specifically targets the middle ear chamber.",
        "Wow_Approach": "In cats, inflammatory nasopharyngeal polyps originate in the middle ear and grow down the eustachian tube. A Ventral Bulla Osteotomy is required to remove the root of the polyp; simply pulling the polyp out of the throat guarantees it will grow back."
    },
    3043: {
        "topic": "Vitamin C - Collagen Maturation",
        "Core_Anatomy": "Extracellular matrix (Fibroblasts).",
        "Pathogenesis_Immediate": "The statement 'Vitamin C plays a major role in maturation of pre-collagen' is TRUE.",
        "Pathogenesis_Deep": "Vitamin C (Ascorbic acid) is an absolute, non-negotiable co-factor for the enzymes prolyl hydroxylase and lysyl hydroxylase. These enzymes are responsible for hydroxylating proline and lysine residues on the pre-collagen molecule inside the fibroblast. This hydroxylation is required for the collagen triple helix to cross-link and form strong, stable fibers. Without Vitamin C, the collagen produced is structurally weak and defective.",
        "Why_Not": "This is the exact pathophysiology of Scurvy in humans and guinea pigs: without Vitamin C, old collagen breaks down and cannot be replaced by strong new collagen, leading to spontaneous hemorrhage, tooth loss, and the catastrophic failure of surgical wounds to heal (dehiscence).",
        "Wow_Approach": "Unlike humans and guinea pigs (who lack the enzyme L-gulonolactone oxidase), dogs and cats can synthesize their own Vitamin C from glucose in their liver. Therefore, they do not get scurvy and do not require Vitamin C supplementation for wound healing."
    },
    3049: {
        "topic": "Brachycephalic Airway Syndrome",
        "Core_Anatomy": "Upper respiratory tract (Larynx and Pharynx).",
        "Pathogenesis_Immediate": "The statement 'Brachycephalic breeds are prone to airway obstruction during general anaesthesia' is strongly TRUE.",
        "Pathogenesis_Deep": "Brachycephalic dogs (Pugs, Bulldogs) suffer from Brachycephalic Airway Syndrome (BAS), characterized by an elongated soft palate, stenotic nares, everted laryngeal saccules, and a hypoplastic trachea. They rely entirely on active, forceful muscular effort to keep their severely narrowed airway open. The moment an induction anaesthetic (like Propofol) relaxes these pharyngeal muscles, the heavy soft palate collapses over the glottis, causing instant, total airway obstruction and rapid asphyxiation.",
        "Why_Not": "They are the highest-risk anaesthetic patients in veterinary medicine.",
        "Wow_Approach": "Rule of thumb for Brachycephalics: NEVER extubate them (remove the breathing tube) until they are fully awake, actively chewing on the tube, and able to lift their own head. If you extubate them while they are still sleepy, their airway will instantly collapse."
    },
    3050: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting a matching question block.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
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
