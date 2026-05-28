import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3265: {
        "topic": "Iohexol - Non-Ionic Contrast",
        "Core_Anatomy": "Spinal cord (Subarachnoid space).",
        "Pathogenesis_Immediate": "Iohexol is a modern, non-ionic, water-soluble iodinated contrast agent.",
        "Pathogenesis_Deep": "Iohexol (Omnipaque) is vastly superior to older ionic contrast agents (like Diatrizoate) because it is non-ionic and has low osmolarity. It is the ONLY safe contrast agent to inject into the subarachnoid space for a Myelogram. Older ionic agents are highly neurotoxic; injecting them into the spine causes massive, fatal seizures.",
        "Why_Not": "Barium is never injected anywhere except the GI tract.",
        "Wow_Approach": "Iohexol is also the contrast of choice if you suspect a ruptured bladder or ruptured GI tract. If barium leaks into the abdomen, it causes fatal peritonitis. If Iohexol leaks into the abdomen, it is safely absorbed by the peritoneum and excreted by the kidneys with no tissue reaction."
    },
    3266: {
        "topic": "Succinylcholine - Neuromuscular Blocker",
        "Core_Anatomy": "Neuromuscular junction (Motor end plate).",
        "Pathogenesis_Immediate": "Succinylcholine is a depolarizing peripheral muscle relaxant (neuromuscular blocking agent).",
        "Pathogenesis_Deep": "It binds to nicotinic acetylcholine receptors at the neuromuscular junction, initially causing muscle fasciculations (depolarization), followed immediately by profound, flaccid paralysis. It was historically used in veterinary medicine to paralyze animals for surgery or capture.",
        "Why_Not": "It is NOT centrally acting (like Guaifenesin or Diazepam). It works exclusively at the peripheral neuromuscular junction.",
        "Wow_Approach": "Succinylcholine provides ABSOLUTELY ZERO analgesia or sedation. If you give this drug to a conscious animal, the animal will be fully awake, completely terrified, and feeling every ounce of surgical pain, but completely paralyzed and unable to move or breathe. Its use without general anaesthesia is considered extreme animal abuse."
    },
    3267: {
        "topic": "Fixer Solution - Sodium Thiosulphate",
        "Core_Anatomy": "Radiographic chemistry.",
        "Pathogenesis_Immediate": "The primary active ingredient in the X-ray Fixer solution is Sodium Thiosulphate.",
        "Pathogenesis_Deep": "After the developer turns the X-ray-exposed silver halide crystals into black metallic silver, the film is placed in the Fixer. The Sodium Thiosulphate ('hypo') acts as a clearing agent. It chemically dissolves and washes away all the remaining UNEXPOSED, unreduced silver halide crystals from the emulsion. This leaves the transparent/white areas of the film and makes the image permanent.",
        "Why_Not": "If you don't fix the film, the unexposed crystals will remain. When you turn on the room lights, those remaining crystals will expose and turn black, completely ruining the image.",
        "Wow_Approach": "The fixer solution is highly valuable because over time, it becomes completely saturated with dissolved silver. Clinics sell their exhausted fixer solution to silver reclamation companies."
    },
    3268: {
        "topic": "Autoclave Biological Indicator",
        "Core_Anatomy": "Sterilization assurance.",
        "Pathogenesis_Immediate": "Steam sterilization (Autoclaving) efficacy is definitively tested using the biological indicator Bacillus stearothermophilus.",
        "Pathogenesis_Deep": "Chemical indicator tape (which turns black) only proves that the outside of the surgical pack got hot. It does not prove that the steam penetrated deep into the pack to kill the bacteria. To prove actual sterility, a vial containing the highly heat-resistant spores of Geobacillus stearothermophilus is placed deep inside the heaviest surgical pack. If the autoclave successfully kills these extremely tough spores, it is guaranteed to have killed every other pathogen.",
        "Why_Not": "Bacillus subtilis is used as the biological indicator for Ethylene Oxide gas sterilization, not steam.",
        "Wow_Approach": "N/A"
    },
    3274: {
        "topic": "Glyceryl Guaiacolate (Guaifenesin)",
        "Core_Anatomy": "Central nervous system (Spinal cord internuncial neurons).",
        "Pathogenesis_Immediate": "Glyceryl Guaiacolate (Guaifenesin / GG) is a Centrally acting muscle relaxant used primarily in equine anaesthesia.",
        "Pathogenesis_Deep": "Unlike Succinylcholine (which paralyzes the peripheral muscles and stops breathing), GG works centrally by depressing nerve impulse transmission at the internuncial neurons of the spinal cord and brainstem. It provides profound relaxation of the skeletal muscles without paralyzing the diaphragm, so the horse continues to breathe normally.",
        "Why_Not": "It provides no analgesia or anaesthesia; it must be combined with Ketamine and Xylazine (the classic 'Triple Drip' for equine field anaesthesia).",
        "Wow_Approach": "In human medicine, Guaifenesin is commonly found in over-the-counter cough syrups (like Mucinex) as an expectorant, but in veterinary medicine, it is bought by the liter as an IV muscle relaxant for 500kg horses."
    },
    3275: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3276: {
        "topic": "Aural Hematoma Definition",
        "Core_Anatomy": "Auricular cartilage (Pinna).",
        "Pathogenesis_Immediate": "The collection of blood within the ear cartilage is called an Aural Hematoma.",
        "Pathogenesis_Deep": "Caused by the centrifugal force of violent head shaking (due to otitis externa), which shears the cartilage plates apart and ruptures the traversing blood vessels.",
        "Why_Not": "N/A",
        "Wow_Approach": "Surgical repair requires mattress sutures placed completely through the ear flap, parallel to the blood vessels, to obliterate the dead space and allow the cartilage plates to scar back together."
    },
    3283: {
        "topic": "Atheroma - False Nostril Cyst",
        "Core_Anatomy": "Equine nasal diverticulum (False nostril).",
        "Pathogenesis_Immediate": "A sebaceous cyst (abscess/collection of atheromatous material) located in the false nostril of a horse is called an Atheroma.",
        "Pathogenesis_Deep": "The equine nasal diverticulum (false nostril) is a blind-ending cutaneous pouch located in the dorsal angle of the nostril. An atheroma is a painless, spherical epidermal inclusion cyst that develops here, filled with thick, grey, caseous sebaceous material. While it is usually just a cosmetic blemish, a very large atheroma can mechanically obstruct airflow, causing respiratory noise (stridor) in racehorses.",
        "Why_Not": "It is not an infection of the true nasal passage or the guttural pouch.",
        "Wow_Approach": "Attempting to drain an atheroma with a needle is futile because the sebaceous material is as thick as toothpaste. It must be surgically excised in its entirety; leaving any part of the cyst lining behind guarantees it will reform."
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
