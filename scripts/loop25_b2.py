import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2829: {
        "topic": "Eye Worm - Thelazia / Setaria",
        "Core_Anatomy": "Anterior chamber and conjunctival sac of the eye.",
        "Pathogenesis_Immediate": "The 'Eye worm' is matched with Setaria Spp. (or Thelazia spp.).",
        "Pathogenesis_Deep": "Two major parasites affect the eye in large animals. (1) Thelazia (true eyeworm) lives in the conjunctival sac and lacrimal ducts, causing severe conjunctivitis and corneal ulceration. (2) Setaria digitata / Setaria equina: Normally, these are harmless filarial nematodes living in the peritoneal cavity. However, they can undergo erratic migration. If they migrate into the anterior chamber of the eye (Equine Ocular Setariasis), the large, white worm can literally be seen swimming in the aqueous humor, causing severe uveitis and corneal edema.",
        "Why_Not": "Habronema causes 'summer sores' on the conjunctiva but is not a swimming worm. Setaria and Thelazia are the primary ophthalmic nematodes.",
        "Wow_Approach": "To remove a Setaria worm from the anterior chamber, a paracentesis (small stab incision) is made at the limbus (corneal margin). The sudden rush of aqueous humor leaving the eye often flushes the worm completely out onto the surgical drape."
    },
    2830: {
        "topic": "Esophagus Matching - Choke",
        "Core_Anatomy": "Cervical and thoracic oesophagus.",
        "Pathogenesis_Immediate": "Esophagus is clinically matched with Choke (oesophageal obstruction).",
        "Pathogenesis_Deep": "As reviewed earlier, 'Choke' is the clinical term for an oesophageal obstruction. In horses, it is almost always caused by dry, unsoaked feed (pellets or beet pulp) expanding and impacted in the cervical oesophagus. In dogs, it is usually a sharp bone stuck at the base of the heart. The cardinal signs of choke in a horse are copious bilateral, feed-tinged nasal discharge, neck stretching, and repeated, anxious swallowing attempts.",
        "Why_Not": "Choke in veterinary medicine NEVER means a tracheal (airway) obstruction. A horse with choke can breathe perfectly fine; it just cannot swallow.",
        "Wow_Approach": "Passing a stomach tube in a choking horse must be done very gently with copious amounts of water to soften the feed impaction. Forcible pushing with the tube will easily rupture the oesophagus, causing fatal mediastinitis."
    },
    2833: {
        "topic": "Recurrent Bloat - Rumen Fistula",
        "Core_Anatomy": "Rumen and Left Paralumbar Fossa.",
        "Pathogenesis_Immediate": "Recurrent bloat in cattle is surgically managed by creating a Rumen Fistula (Rumenostomy).",
        "Pathogenesis_Deep": "When a cow suffers from chronic, intractable, recurrent ruminal tympany (bloat)—often due to chronic vagal indigestion or tetanus—conservative treatment (passing a stomach tube) becomes impractical. A permanent or temporary rumen fistula is created. The surgeon incises the left paralumbar fossa, pulls the rumen wall out, and sutures the rumen mucosa directly to the skin, leaving a permanent hole. This allows ruminal gases to vent continuously into the atmosphere, saving the cow's life from asphyxiation.",
        "Why_Not": "Spaying (ovariohysterectomy) is for reproduction control/pyometra, completely unrelated to the digestive tract.",
        "Wow_Approach": "Rumen fistulas are also created in healthy 'donor' cattle at veterinary teaching hospitals to provide a continuous, accessible supply of healthy rumen fluid (transfaunation) for sick, acidotic cattle."
    },
    2837: {
        "topic": "Definitions Section Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a short-answer definition section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2845: {
        "topic": "Exam Instruction - Time Limit",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating Part-A (objective section) must be completed in one hour.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2846: {
        "topic": "VSR 411 - General Surgery Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the objective questions for General Veterinary Surgery (VSR 411).",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2847: {
        "topic": "Father of Antiseptic Surgery - Joseph Lister",
        "Core_Anatomy": "Surgical operating environment.",
        "Pathogenesis_Immediate": "Joseph Lister introduced the principles of Antiseptic sterilization to surgery.",
        "Pathogenesis_Deep": "In the 1860s, British surgeon Joseph Lister, applying Louis Pasteur's germ theory, pioneered the use of carbolic acid (phenol) to sterilize surgical instruments and clean wounds. This drastically reduced the incidence of fatal postoperative gangrene. While modern surgery relies on Asepsis (preventing bacteria from entering the wound via autoclaves and drapes), Lister's introduction of chemical Antisepsis was the critical turning point in surgical history.",
        "Why_Not": "Halsted introduced aseptic principles (gloves, gentle tissue handling). Pasteur proved germs exist. Lister specifically applied chemicals to sterilize the surgical field.",
        "Wow_Approach": "The popular mouthwash 'Listerine' was named directly in honor of Joseph Lister's pioneering work in antisepsis."
    },
    2857: {
        "topic": "True or False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of the True/False section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2858: {
        "topic": "Shock Pathophysiology - Sympathoadrenal System",
        "Core_Anatomy": "Systemic vasculature and Adrenal medulla.",
        "Pathogenesis_Immediate": "The statement 'In shock, stimulation of the PARA-sympathoadrenal system leads to vasoconstriction' is FALSE. (It is the SYMPATHO-adrenal system).",
        "Pathogenesis_Deep": "In the early, compensatory phase of shock (e.g., severe hemorrhage), the baroreceptors sense a drop in blood pressure. They trigger a massive SYMPATHETIC nervous system response, causing the adrenal medulla to release Epinephrine and Norepinephrine. This sympathoadrenal surge causes profound peripheral vasoconstriction (pale mucous membranes, cold extremities) to shunt the remaining blood volume exclusively to the vital organs (heart and brain) to keep the animal alive.",
        "Why_Not": "The Parasympathetic system ('rest and digest') causes vasodilation and bradycardia. Activating it during shock would instantly kill the animal.",
        "Wow_Approach": "This intense sympathetic vasoconstriction is why finding a vein for an IV catheter in a shocky patient is extremely difficult; the peripheral veins are completely collapsed."
    },
    2866: {
        "topic": "Auriculopalpebral Nerve Block - Motor Only",
        "Core_Anatomy": "Facial nerve (CN VII) and orbicularis oculi muscle.",
        "Pathogenesis_Immediate": "The statement 'Auriculopalpebral nerve block is a sensory nerve block' is FALSE.",
        "Pathogenesis_Deep": "The Auriculopalpebral nerve is a branch of the Facial Nerve (Cranial Nerve VII), which is purely a MOTOR nerve. Blocking it over the zygomatic arch paralyses the orbicularis oculi muscle, preventing the horse or cow from blinking (abolishing blepharospasm). It provides ABSOLUTELY ZERO analgesia (pain relief) to the eye.",
        "Why_Not": "To provide pain relief for ocular surgery, you must block the sensory nerves (the Ophthalmic division of the Trigeminal Nerve, CN V) using a retrobulbar block or topical tetracaine drops.",
        "Wow_Approach": "If you perform a standing enucleation on a cow with ONLY an auriculopalpebral block, the cow will violently resist the moment you cut the conjunctiva, because you have only paralyzed its eyelid, not numbed its eye."
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
