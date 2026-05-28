import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2789: {
        "topic": "Xylazine Premedication - Barbiturate Sparing Effect",
        "Core_Anatomy": "Central nervous system (sedation synergy).",
        "Pathogenesis_Immediate": "Xylazine premedication allows the surgeon to Decrease the dose of barbiturates required for induction.",
        "Pathogenesis_Deep": "As a potent alpha-2 agonist, Xylazine depresses the CNS significantly. When followed by an induction agent like Thiopental, the required dose of the barbiturate is reduced by 50-75% (the 'dose-sparing' effect). This is critical because barbiturates have a very narrow therapeutic index and cause severe respiratory and cardiovascular depression at high doses.",
        "Why_Not": "Failing to reduce the barbiturate dose after heavy premedication will result in a massive overdose, leading to profound apnea and potential cardiac arrest.",
        "Wow_Approach": "This is the core concept of 'Balanced Anaesthesia': combining smaller doses of multiple drugs with different mechanisms (sedative + analgesic + induction agent) to achieve surgical anaesthesia with far fewer side effects than a massive dose of a single drug."
    },
    2790: {
        "topic": "Inhalant Anaesthesia - Recovery Time",
        "Core_Anatomy": "Pulmonary alveoli (gas exchange).",
        "Pathogenesis_Immediate": "Recovery is significantly faster in Inhalant anaesthesia compared to injectable agents.",
        "Pathogenesis_Deep": "Inhalant agents (Isoflurane, Sevoflurane) rely on the lungs for both uptake and elimination. Because they have very low blood-gas solubility, they do not accumulate heavily in the body's fat stores. The moment the vaporizer is turned off and the animal breathes pure oxygen, the concentration gradient reverses, and the drug is rapidly exhaled. Recovery is complete within minutes.",
        "Why_Not": "Intravenous agents (like ketamine or barbiturates) must be metabolised by the liver or excreted by the kidneys, which takes hours.",
        "Wow_Approach": "If a patient on inhalant anaesthesia crashes, the anaesthetist can instantly turn off the drug and aggressively ventilate the lungs with pure oxygen to literally 'breathe the anaesthetic out' of the patient."
    },
    2791: {
        "topic": "Potassium Permanganate - Wound Lavage",
        "Core_Anatomy": "Wound surface (bacterial flora).",
        "Pathogenesis_Immediate": "The correct concentration of Potassium Permanganate (KMnO4) for wound lavage is 1%.",
        "Pathogenesis_Deep": "At a 1% concentration (1 in 1000), Potassium Permanganate is an effective oxidizing antiseptic, releasing nascent oxygen that destroys bacterial membranes (especially effective against strict anaerobes). At this low concentration, it is relatively non-toxic to the healing fibroblasts and epithelial cells of the wound bed.",
        "Why_Not": "Concentrations of 5% or 10% are strongly caustic and will cause severe chemical burns to the wound tissue, delaying healing and creating more necrotic debris for bacteria to feed on.",
        "Wow_Approach": "KMnO4 is rarely used in modern small animal surgery (having been replaced by 0.05% Chlorhexidine or 1% Povidone-Iodine), but it remains a cheap, effective, and heavily tested staple of large animal field surgery."
    },
    2792: {
        "topic": "X-ray Film Storage",
        "Core_Anatomy": "Silver halide emulsion.",
        "Pathogenesis_Immediate": "Unexposed X-ray films must be stored in a Cool and Dry location.",
        "Pathogenesis_Deep": "The gelatin emulsion of an X-ray film is highly sensitive to environmental factors. Heat provides activation energy that causes the silver halide crystals to slowly reduce to metallic silver without X-ray exposure, creating 'chemical fog' (a greyish background that degrades image contrast). Moisture causes the gelatin to swell, making the films stick together and ruining the emulsion surface.",
        "Why_Not": "Hot and humid conditions will destroy a box of unexposed X-ray film within weeks.",
        "Wow_Approach": "Films must also be stored vertically (like books on a shelf), NEVER stacked flat on top of each other. The physical pressure from stacking also causes pressure artifacts (fogging) on the bottom films in the box."
    },
    2793: {
        "topic": "Double Contrast Radiography",
        "Core_Anatomy": "Hollow organs (stomach, colon, bladder).",
        "Pathogenesis_Immediate": "To study both the lumen size AND the mucosal contour of an organ, Double contrast radiography is employed.",
        "Pathogenesis_Deep": "Using only positive contrast (Barium) fills the lumen and shows the overall organ size, but it is so dense (white) that it hides small mucosal lesions (like early ulcers or polyps) inside the pool of contrast. Double contrast involves coating the mucosa with a small amount of positive contrast (Barium/Iodine) and then inflating the lumen with a negative contrast gas (Air/CO2). The air distends the lumen, and the white contrast perfectly outlines the mucosal folds against the black air background.",
        "Why_Not": "Single contrast techniques (either positive or negative alone) provide incomplete information regarding mucosal detail.",
        "Wow_Approach": "In the bladder, double contrast cystography is the gold standard for identifying radiolucent stones (urate/cystine). The stones appear as black 'filling defects' outlined by a thin rim of white iodine, floating in a pool of black air."
    },
    2794: {
        "topic": "Hypovolemic Shock - Ringer's Lactate",
        "Core_Anatomy": "Intravascular and Interstitial fluid compartments.",
        "Pathogenesis_Immediate": "The most versatile crystalloid solution for treating hypovolemic shock is Ringer's Lactate.",
        "Pathogenesis_Deep": "Ringer's Lactate is a balanced, isotonic, replacement crystalloid. It contains sodium, potassium, calcium, and chloride in concentrations very similar to normal blood plasma. It also contains lactate, which the liver metabolizes into bicarbonate to buffer the metabolic acidosis universally present in shock patients. It expands the intravascular volume rapidly without causing the hyperchloremic acidosis associated with Normal Saline.",
        "Why_Not": "Dextrose (5% in water) is technically isotonic in the bag, but the glucose is instantly metabolized, leaving free water which rapidly diffuses out of the blood vessels into the cells. It provides almost ZERO intravascular volume expansion.",
        "Wow_Approach": "A 'shock dose' of Ringer's Lactate in a dog is 90 mL/kg/hour (roughly equivalent to their entire blood volume). In a 30kg dog, this means administering almost 3 Liters of fluid in one hour to save its life."
    },
    2795: {
        "topic": "Tamponade Plugging",
        "Core_Anatomy": "Body cavities (Abdomen, Thorax, Nasal).",
        "Pathogenesis_Immediate": "Tamponade plugging is matched with: Control bleeding from cavities.",
        "Pathogenesis_Deep": "When surgical hemorrhage occurs from a diffuse area rather than a single identifiable vessel (e.g., severe liver lobe laceration, nasal turbinate trauma), individual ligation is impossible. Tamponade involves packing the cavity tightly with sterile gauze or specialized hemostatic sponges (Gelfoam). This applies continuous, direct mechanical pressure to the bleeding surface, allowing the intrinsic clotting cascade to seal the microvasculature.",
        "Why_Not": "It is a mechanical hemostatic technique, unrelated to radiation or primary healing.",
        "Wow_Approach": "If standard gauze is used for tamponade, it must be removed very carefully 24-48 hours later. Yanking it out will rip off the newly formed fibrin clots and immediately restart the hemorrhage. It should be soaked with warm saline before gentle removal."
    },
    2796: {
        "topic": "Roentgen - Radiation Unit",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "Roentgen (R) is the classic unit of X-ray exposure.",
        "Pathogenesis_Deep": "While the Roentgen (R) measures the amount of ionizing radiation in the air, veterinary safety monitoring relies on the Sievert (Sv), which measures the biological effect of that radiation absorbed by human tissue. Radiographers must wear lead aprons (0.5mm lead equivalent) because scatter radiation (measured in R) bounces off the patient and hits the staff.",
        "Why_Not": "The Roentgen is a measure of exposure, not absorption (Gray) or equivalent dose (Sievert).",
        "Wow_Approach": "Lead aprons do NOT protect against the primary X-ray beam. If you put your gloved hand directly under the X-ray tube to hold an animal, the primary beam will easily penetrate the lead and expose your hand. The lead is only designed to stop low-energy scattered radiation."
    },
    2797: {
        "topic": "Closed Wound - Primary Healing",
        "Core_Anatomy": "Skin and soft tissues.",
        "Pathogenesis_Immediate": "A surgically closed wound is intended to heal via Primary Healing (First Intention Healing).",
        "Pathogenesis_Deep": "Primary intention healing occurs when the edges of a clean, uninfected surgical incision are brought together (apposed) with sutures. Because there is no tissue loss and no infection, the wound heals rapidly with minimal granulation tissue and minimal scarring. The fibrin clot acts as a scaffold for epithelial cells to bridge the gap within 48 hours.",
        "Why_Not": "Secondary healing occurs in open, contaminated wounds with tissue loss, requiring extensive granulation tissue to fill the defect from the bottom up.",
        "Wow_Approach": "If a surgeon ties the sutures too tightly, it causes ischemic necrosis of the wound edges. This destroys the primary healing process, causing the wound to break open (dehiscence) and forcing it to heal by the much slower secondary intention."
    },
    2798: {
        "topic": "Potter-Bucky Diaphragm - Scatter Radiation",
        "Core_Anatomy": "X-ray table mechanics.",
        "Pathogenesis_Immediate": "The Potter-Bucky diaphragm is designed to Absorb secondary (scatter) radiation.",
        "Pathogenesis_Deep": "Located just under the X-ray table surface, the Bucky mechanism holds the lead grid and oscillates it rapidly back and forth during the exposure. This movement prevents the lead strips of the grid from casting a shadow (grid lines) on the final image, while still allowing the lead to absorb the multi-directional scatter radiation coming from the patient.",
        "Why_Not": "It does not produce X-rays or control bleeding. Its sole function is to clean up the image by removing scatter.",
        "Wow_Approach": "If you hear a loud buzzing or vibrating sound from the X-ray table right before the 'beep' of the exposure, that is the Bucky mechanism motor engaging to move the grid."
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
