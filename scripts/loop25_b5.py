import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2934: {
        "topic": "Out-pouching - Diverticulum",
        "Core_Anatomy": "Hollow organs (Oesophagus, Bladder, Intestine).",
        "Pathogenesis_Immediate": "An abnormal out-pouching of a hollow organ wall is clinically defined as a Diverticulum.",
        "Pathogenesis_Deep": "Diverticula can be congenital or acquired. Pulsion diverticula occur due to increased intraluminal pressure pushing the mucosa through a weakness in the muscularis layer. Traction diverticula occur when external scar tissue (e.g., from severe periesophageal inflammation) pulls the full thickness of the wall outward. Both types create a dead-end sac that traps ingesta/urine, leading to chronic localized infection.",
        "Why_Not": "A hernia is an out-pouching of an organ through a body wall. A diverticulum is an out-pouching of the organ wall itself.",
        "Wow_Approach": "N/A"
    },
    2935: {
        "topic": "Synthetic Monofilament Absorbable Suture - PDS",
        "Core_Anatomy": "Surgical tissue closure.",
        "Pathogenesis_Immediate": "Header indicating a question identifying a Synthetic Monofilament Absorbable suture.",
        "Pathogenesis_Deep": "Understanding suture classifications is critical. (1) Natural: Catgut (absorbable, multifilament), Silk (non-absorbable, multifilament). (2) Synthetic Multifilament Absorbable: Polyglycolic acid (Dexon), Polyglactin 910 (Vicryl). (3) Synthetic Monofilament Absorbable: Polydioxanone (PDS), Poliglecaprone 25 (Monocryl). (4) Synthetic Monofilament Non-Absorbable: Polypropylene (Prolene), Polyamide (Nylon).",
        "Why_Not": "Multifilament sutures (Vicryl) harbor bacteria in their braids and should not be used in infected wounds. Monofilaments (PDS) are safe for infected wounds.",
        "Wow_Approach": "PDS takes roughly 180 days to be completely absorbed by hydrolysis, making it the ideal suture for tissues that heal slowly (like the linea alba or bladder)."
    },
    2936: {
        "topic": "Polydioxanone (PDS)",
        "Core_Anatomy": "Surgical tissue closure.",
        "Pathogenesis_Immediate": "Polydioxanone (PDS) is the correct answer for a Synthetic Monofilament Absorbable suture.",
        "Pathogenesis_Deep": "PDS provides prolonged tensile strength. It retains 50% of its strength at 4 weeks post-surgery. This is massively superior to Catgut, which loses its strength in just a few days in infected or enzyme-rich environments (like the stomach). Because PDS is a monofilament, it passes smoothly through tissue with zero drag and does not wick bacteria.",
        "Why_Not": "Polyglycolic acid (Dexon) is synthetic and absorbable, but it is MULTIFILAMENT (braided). Polyamide (Nylon) is a monofilament but is NON-ABSORBABLE. Catgut is NATURAL.",
        "Wow_Approach": "PDS is degraded by non-enzymatic hydrolysis (water molecules slowly breaking the polymer chain). Therefore, its absorption rate is highly predictable, regardless of the patient's immune status or the presence of infection."
    },
    2937: {
        "topic": "Normal Urine Output - Dogs",
        "Core_Anatomy": "Kidneys.",
        "Pathogenesis_Immediate": "Normal urine output in a healthy dog is 1-2 ml/kg/hr.",
        "Pathogenesis_Deep": "Monitoring urine output is the gold standard for assessing renal perfusion and cardiovascular status in a critically ill or anaesthetized patient. A closed urinary catheter collection system is used. If the output drops below 1 ml/kg/hr (Oliguria), the kidneys are not receiving enough blood flow, usually due to hypotension, hypovolemia, or acute kidney injury. If it hits 0 ml/kg/hr (Anuria), the situation is dire.",
        "Why_Not": "4-10 ml/kg/hr is massive polyuria (seen with IV fluid diuresis, diabetes, or chronic renal failure).",
        "Wow_Approach": "During shock resuscitation, if you are giving aggressive IV fluids but the urine output remains <1 ml/kg/hr, you must assume the kidneys have shut down (Acute Tubular Necrosis) or the bladder has ruptured."
    },
    2938: {
        "topic": "0.9% Normal Saline - Isotonicity",
        "Core_Anatomy": "Intravascular fluid compartment.",
        "Pathogenesis_Immediate": "0.9% Normal Saline (NaCl) is an Isotonic crystalloid solution.",
        "Pathogenesis_Deep": "Tonicity compares the osmotic pressure of a fluid to normal blood plasma. Isotonic fluids (like 0.9% NaCl, Ringer's Lactate, and Plasmalyte-A) have the same osmolarity (~300 mOsm/L) as plasma. When administered IV, they rapidly expand the intravascular volume without causing water to shift into or out of the red blood cells. Hypertonic fluids (like 7% NaCl) pull water OUT of the tissues into the vessels. Hypotonic fluids (like 0.45% NaCl) push water OUT of the vessels into the cells.",
        "Why_Not": "If you gave a patient sterile pure water IV (highly hypotonic), the water would instantly rush into the red blood cells, causing them to explode (massive fatal hemolysis).",
        "Wow_Approach": "0.9% NaCl is called 'Normal' Saline, but it is actually highly abnormal compared to plasma. It contains 154 mEq/L of Chloride (plasma only has ~110 mEq/L). Giving massive volumes of Normal Saline causes Hyperchloremic Metabolic Acidosis."
    },
    2939: {
        "topic": "Fluid of Choice - Vomiting (Normal Saline)",
        "Core_Anatomy": "Stomach (gastric acid) and systemic acid-base balance.",
        "Pathogenesis_Immediate": "The fluid of choice in cases of severe gastric vomiting (e.g., pyloric obstruction) is 0.9% Normal Saline.",
        "Pathogenesis_Deep": "When an animal vomits profusely, it loses massive amounts of Hydrochloric Acid (HCl) from the stomach. This loss of Hydrogen (acid) and Chloride results in a profound Hypochloremic Metabolic Alkalosis. To correct this specific acid-base imbalance, the patient requires a fluid that is high in Chloride and lacks alkalizing buffers. 0.9% Normal Saline (which contains 154 mEq/L of Chloride and zero buffers) is the perfect physiological antidote.",
        "Why_Not": "Ringer's Lactate is buffered (lactate converts to bicarbonate in the liver). Giving a buffered fluid to a patient that is ALREADY alkalotic will make the alkalosis worse and potentially cause fatal hypokalemia.",
        "Wow_Approach": "If the vomiting is from the LOWER GI tract (diarrhea or intestinal obstruction), the patient loses bicarbonate and becomes Acidotic. In this case, Ringer's Lactate (a buffered fluid) becomes the fluid of choice."
    },
    2940: {
        "topic": "Wound Healing - Maturation/Contraction",
        "Core_Anatomy": "Skin (Myofibroblasts and Collagen).",
        "Pathogenesis_Immediate": "The last stage of wound healing involves Wound Contraction and Tissue Remodeling (Maturation).",
        "Pathogenesis_Deep": "Wound healing occurs in four overlapping phases: (1) Hemostasis/Inflammation (Days 1-3). (2) Debridement (Days 2-5). (3) Repair/Proliferation (Days 4-21)—This includes Fibroplasia (collagen deposition), Angiogenesis (new blood vessels), Epithelialization (skin migrating across the surface), and Wound Contraction (myofibroblasts pulling the wound edges together). (4) Maturation/Remodeling (Months to Years)—The final stage where disorganized Type III collagen is slowly replaced by strong, organized Type I collagen, and the scar tissue strengthens.",
        "Why_Not": "Vasodilation is the very first step (inflammation). Fibroplasia happens in the middle.",
        "Wow_Approach": "In horses, the 'Repair' phase often goes completely out of control, resulting in 'Exuberant Granulation Tissue' (Proud Flesh). This massive fleshy tumor-like growth physically blocks epithelialization and wound contraction from occurring."
    },
    2941: {
        "topic": "Common Hematoma Site - Dogs",
        "Core_Anatomy": "Auricular cartilage (Pinna).",
        "Pathogenesis_Immediate": "The most common anatomical site for a hematoma in dogs is the Ear (Aural Hematoma).",
        "Pathogenesis_Deep": "As covered in a previous batch, violent head shaking causes the centrifugal force to rupture the delicate blood vessels traversing the cartilage of the pinna. The space between the skin and cartilage fills with blood.",
        "Why_Not": "While hematomas can occur anywhere post-trauma, the ear flap is by far the most statistically common, naturally occurring presentation in canine practice.",
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
