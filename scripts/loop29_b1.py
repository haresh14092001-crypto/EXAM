import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3284: {
        "topic": "Empyema of Frontal Sinus (Review)",
        "Core_Anatomy": "Frontal Sinus.",
        "Pathogenesis_Immediate": "Empyema of the frontal sinus is a classic complication due to Dehorning.",
        "Pathogenesis_Deep": "As reviewed extensively, opening the cornual diverticulum during adult dehorning exposes the frontal sinus to environmental pathogens, leading to severe purulent sinusitis.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3285: {
        "topic": "Empyema - Horn Affection",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Confirmation that frontal sinus empyema is specifically caused by a 'Horn affection' (Dehorning).",
        "Pathogenesis_Deep": "N/A",
        "Why_Not": "Tooth affections cause Maxillary sinusitis, not Frontal sinusitis.",
        "Wow_Approach": "N/A"
    },
    3286: {
        "topic": "Cherry Eye - 3rd Eyelid",
        "Core_Anatomy": "Nictitating membrane.",
        "Pathogenesis_Immediate": "Cherry eye specifically involves the 3rd Eyelid (Nictitating membrane).",
        "Pathogenesis_Deep": "It is the prolapse of the gland of the third eyelid, appearing as a red, swollen mass at the medial canthus.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3287: {
        "topic": "Viborg's Triangle - Guttural Pouch (Review)",
        "Core_Anatomy": "Equine Head and Neck.",
        "Pathogenesis_Immediate": "The Viborg's triangle approach is used exclusively to access the Guttural pouch.",
        "Pathogenesis_Deep": "As reviewed, this surgical window avoids the carotid arteries and jugular vein.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3288: {
        "topic": "Approach to Cranial Thoracic Oesophagus",
        "Core_Anatomy": "Thorax (Intercostal spaces).",
        "Pathogenesis_Immediate": "The surgical approach to the cranial thoracic oesophagus is typically via the Left 3rd or 4th intercostal space.",
        "Pathogenesis_Deep": "When an esophageal foreign body (like a bone) is lodged at the base of the heart, it must be removed via a thoracotomy. The cranial thoracic esophagus is usually accessed from the LEFT side (3rd/4th ICS). Conversely, the caudal thoracic esophagus (near the diaphragm) is best accessed from the RIGHT or LEFT 8th/9th ICS depending on the exact location of the mass/stricture.",
        "Why_Not": "Accessing the wrong side or wrong intercostal space means the heart, aorta, or lungs will completely block your view of the esophagus.",
        "Wow_Approach": "Thoracic surgery requires a ventilator. The moment you open the chest cavity, the negative pressure is lost, the lungs collapse, and the animal will die within minutes without positive pressure ventilation."
    },
    3289: {
        "topic": "Paraneoplastic Syndrome - Hypercalcemia",
        "Core_Anatomy": "Systemic circulation (Calcium metabolism).",
        "Pathogenesis_Immediate": "A common paraneoplastic syndrome in veterinary medicine involves severe elevation in blood Calcium levels (Hypercalcemia of malignancy).",
        "Pathogenesis_Deep": "Certain tumors—most classically Apocrine Gland Anal Sac Adenocarcinoma (AGASACA) and Lymphoma in dogs—secrete Parathyroid Hormone-related Protein (PTHrP). This fake hormone perfectly mimics real PTH. It signals the bones to constantly release calcium and the kidneys to stop excreting it. This results in massive, life-threatening hypercalcemia, causing PU/PD, severe vomiting, and ultimately soft tissue mineralization and acute renal failure.",
        "Why_Not": "Tumors rarely cause generalized hypernatremia (high sodium) or primary elevations in ALT unless they are directly destroying the liver.",
        "Wow_Approach": "If an older dog presents with unexplained severe hypercalcemia, the very first thing you must do is perform a digital rectal exam to check for an anal sac mass."
    },
    3290: {
        "topic": "Urethral Calculi - Sheep/Goat",
        "Core_Anatomy": "Urethral process (Vermiform appendage).",
        "Pathogenesis_Immediate": "The most common site of urethral calculi obstruction in male sheep and goats is the Urethral Process (Vermiform appendage), followed by the sigmoid flexure.",
        "Pathogenesis_Deep": "Male small ruminants have a very long, narrow urethra that makes a sharp S-curve (the sigmoid flexure) and terminates in a tiny, hair-like extension at the tip of the penis called the urethral process. Phosphatic calculi (from high-grain diets) almost universally lodge in this tiny terminal process, causing complete urinary blockage and eventual bladder rupture.",
        "Why_Not": "In dogs, stones lodge at the base of the os penis. In cattle, they lodge at the distal sigmoid flexure. In small ruminants, the urethral process is the absolute bottleneck.",
        "Wow_Approach": "The immediate, life-saving field treatment for a blocked wether/buck is to simply amputate the urethral process with scissors. It has no vital function, and snipping it off often immediately relieves the obstruction."
    },
    3291: {
        "topic": "Vesicocele - Bladder (Review)",
        "Core_Anatomy": "Urinary bladder.",
        "Pathogenesis_Immediate": "A Vesicocele is the herniation of the Bladder.",
        "Pathogenesis_Deep": "Reiterating that this is a surgical emergency, typically seen in perineal hernias.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3292: {
        "topic": "Intussusception",
        "Core_Anatomy": "Gastrointestinal tract.",
        "Pathogenesis_Immediate": "The telescoping of one part of the intestine into an adjacent part is called an Intussusception.",
        "Pathogenesis_Deep": "This usually occurs secondary to severe hypermotility (e.g., from Parvovirus or heavy roundworm burdens in puppies). A proximal segment of bowel (the intussusceptum) is violently pushed INSIDE the lumen of the distal segment (the intussuscipiens). This immediately cuts off the venous drainage of the trapped segment, causing it to rapidly swell, turn black, and die (ischemic necrosis), while also completely obstructing the passage of food.",
        "Why_Not": "Volvulus is the twisting of the bowel on its mesenteric axis. Torsion is twisting on its longitudinal axis. Intussusception is strictly telescoping.",
        "Wow_Approach": "On a physical exam, a fresh intussusception feels exactly like a firm sausage in the puppy's abdomen. On ultrasound, it pathognomonically appears as a 'Target Sign' (multiple concentric rings of bowel wall)."
    },
    3293: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
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
print(f"Batch 1/5 DONE: Updated {updated} questions.")
