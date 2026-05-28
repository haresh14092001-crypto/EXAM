import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3102: {
        "topic": "Multiple Choice Questions Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of the multiple-choice section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3103: {
        "topic": "Golden Period of Wound Healing",
        "Core_Anatomy": "Skin and soft tissues.",
        "Pathogenesis_Immediate": "The ideal period to suture a fresh, contaminated wound (Primary Closure) is <6 hours.",
        "Pathogenesis_Deep": "This is known in surgery as the 'Golden Period'. For the first 6 hours after a traumatic injury, the contaminating bacteria are merely sitting on the surface of the tissue. They have not yet multiplied significantly or invaded deep into the tissue planes. During this window, the surgeon can aggressively lavage and debride the wound, effectively converting it from a contaminated wound back into a clean wound, and suture it closed safely (Primary Intention).",
        "Why_Not": "If the wound is sutured AFTER 6-8 hours, the bacteria have invaded. Closing the skin over them will guarantee a massive, enclosed abscess (dehiscence).",
        "Wow_Approach": "If a wound is >8 hours old, it must be managed open (Delayed Primary Closure or Secondary Intention) until a healthy bed of granulation tissue forms to fight off the established infection."
    },
    3104: {
        "topic": "Golden Period - Distractor Options",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "This line represents the time-based options (<6, <12, <24, <36 hrs) for the Golden Period question.",
        "Pathogenesis_Deep": "Reinforces the <6 hour rule for primary closure of traumatic wounds.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3105: {
        "topic": "Auriculopalpebral Nerve Block - Eyelid Paralysis",
        "Core_Anatomy": "Orbicularis oculi muscle.",
        "Pathogenesis_Immediate": "The Auriculopalpebral nerve block paralyzes the eyelids, preventing blinking (blepharospasm) and allowing examination.",
        "Pathogenesis_Deep": "While true 'ptosis' (drooping) is caused by Oculomotor nerve (CN III) damage, the auriculopalpebral block (a branch of the Facial nerve, CN VII) paralyzes the orbicularis oculi muscle. This causes the upper eyelid to droop slightly and completely abolishes the animal's ability to forcefully squeeze the eye shut. This is mandatory before examining a painful equine eye, otherwise, the horse will forcefully close its eye and the veterinarian will be unable to open it.",
        "Why_Not": "Cornual block is for horns. Infra-trochlear block is a sensory block for the medial canthus.",
        "Wow_Approach": "Because the horse cannot blink after this block, the cornea will rapidly dry out and ulcerate. The veterinarian MUST apply artificial tear ointment constantly until the block wears off (usually 1-2 hours)."
    },
    3107: {
        "topic": "Pharmacology Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options representing common veterinary sedatives (Acepromazine, Xylazine, Diazepam) and an opioid (Tramadol).",
        "Pathogenesis_Deep": "Structural artifact from scanning.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3108: {
        "topic": "Horn Injury - Punctured/Penetrating Wound",
        "Core_Anatomy": "Thoracic or abdominal wall.",
        "Pathogenesis_Immediate": "A horn injury (goring) in cattle or horses results in a deep Punctured or Penetrating Wound.",
        "Pathogenesis_Deep": "A horn thrust carries immense force, driving a dirty, bacteria-laden object deep into the victim's tissues. The surface wound is often small (punctured), but the underlying tissue damage and dead space are massive. This creates the perfect anaerobic environment (no oxygen) for Clostridium tetani (Tetanus) or Clostridium septicum (Malignant Edema) to proliferate.",
        "Why_Not": "It is not a simple laceration (a slicing cut) or an abrasion (a scrape). It is a deep puncture.",
        "Wow_Approach": "Never just suture the small skin hole of a horn gore closed. The massive dead space underneath will instantly form a life-threatening abscess. The wound must be opened, aggressively debrided, and flushed, often requiring a Penrose drain."
    },
    3109: {
        "topic": "Gamma Rays vs X-Rays",
        "Core_Anatomy": "Atomic physics.",
        "Pathogenesis_Immediate": "The liberation of energy (photons) from an UNSTABLE NUCLEUS of a radioactive atom results in the production of Gamma Rays.",
        "Pathogenesis_Deep": "This is the fundamental physical difference between X-rays and Gamma rays. Both are highly energetic, ionizing electromagnetic radiation that behave identically in tissue. However, X-rays are produced MAN-MADE in an X-ray tube when electrons hit a tungsten target (originating from the electron cloud). Gamma rays are produced NATURALLY by the spontaneous decay of radioactive isotopes (like Cobalt-60 or Technetium-99m), originating directly from the unstable nucleus of the atom.",
        "Why_Not": "Alpha and Beta particles are physical matter (helium nuclei and electrons, respectively), not electromagnetic rays.",
        "Wow_Approach": "Because Gamma rays come from constantly decaying radioactive elements, you cannot 'turn them off' like an X-ray machine. Gamma sources (used in equine bone scans) must be stored in massive lead vaults 24/7."
    },
    3110: {
        "topic": "Ketamine Dose - Cattle",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "The dose of ketamine for general anesthesia induction in cattle.",
        "Pathogenesis_Deep": "Similar to horses, adult cattle require profound sedation (usually with Xylazine) before administering Ketamine to prevent violent excitement. The standard induction dose of Ketamine in heavily sedated cattle is typically 2.0 to 2.2 mg/kg IV, which will drop the cow within a minute and provide 10-20 minutes of surgical anesthesia.",
        "Why_Not": "Using Ketamine alone in a cow is contraindicated as it causes severe muscle rigidity, bellowing, and thrashing.",
        "Wow_Approach": "Unlike horses, cattle heavily salivate under Ketamine anesthesia. This massive volume of saliva can easily pool in the pharynx and be aspirated into the lungs, so the cow's head must always be positioned downhill during surgery to allow the saliva to drain out of the mouth."
    },
    3111: {
        "topic": "Ketamine Dose Options - 1.1 mg/kg",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Distractor option for the Ketamine dose.",
        "Pathogenesis_Deep": "1.1 mg/kg is the standard IV induction dose for Xylazine in horses, not Ketamine.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3112: {
        "topic": "Ketamine Dose Options - 2.2 mg/kg",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "The correct option (2.2 mg/kg) for the Ketamine induction dose in large animals.",
        "Pathogenesis_Deep": "This standard 2.2 mg/kg (or 1 mg/lb) rule applies broadly to both equine and bovine IV inductions following adequate alpha-2 premedication.",
        "Why_Not": "5 mg/kg or 12 mg/kg IV would cause massive overdose, prolonged, violent recoveries, and potentially fatal cardiovascular strain in an adult ruminant.",
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
print(f"Batch 2/5 DONE: Updated {updated} questions.")
