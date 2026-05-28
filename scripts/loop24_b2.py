import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2734: {
        "topic": "Thoracic Oesophagus - Surgical Approach",
        "Core_Anatomy": "Thorax (intercostal spaces).",
        "Pathogenesis_Immediate": "The surgical approach to the thoracic oesophagus depends on the location of the lesion (e.g., foreign body).",
        "Pathogenesis_Deep": "Anatomically, the oesophagus shifts as it travels down the neck and through the thorax. In the cervical region, it lies on the LEFT side of the trachea. As it enters the cranial thorax, it shifts slightly to the RIGHT. Therefore, the cranial thoracic oesophagus (base of the heart) is approached via a Right 3rd, 4th, or 5th intercostal thoracotomy. As it passes the heart and heads to the diaphragm, it shifts back to the midline/left. Thus, the caudal thoracic oesophagus (near the diaphragm) is approached via a Left 7th, 8th, or 9th intercostal thoracotomy.",
        "Why_Not": "Approaching from the wrong side means the surgeon will have to wrestle the heart, aorta, or lungs out of the way to reach the oesophagus.",
        "Wow_Approach": "Most oesophageal foreign bodies in dogs (bones) lodge either at the thoracic inlet, the base of the heart, or just cranial to the diaphragm (the three anatomical narrow points). Endoscopic removal is always attempted first, as opening the thorax carries massive morbidity."
    },
    2736: {
        "topic": "Liver Enzyme Marker - ALT",
        "Core_Anatomy": "Hepatocytes.",
        "Pathogenesis_Immediate": "ALT (Alanine Aminotransferase) is a highly specific enzyme marker for hepatocellular damage in dogs and cats.",
        "Pathogenesis_Deep": "ALT is a cytosolic enzyme found in high concentrations within the hepatocytes of small animals. When hepatocytes are damaged or die (necrosis, severe inflammation, toxins), their cell membranes rupture, leaking ALT directly into the bloodstream. Therefore, an elevated serum ALT is a sensitive and specific indicator of active liver cell damage in dogs and cats. (Note: It is not useful in large animals like horses/cattle, where SDH or GLDH are used instead).",
        "Why_Not": "Calcium and Sodium are electrolytes. Glucose is a metabolite. ALT specifically flags liver cell rupture.",
        "Wow_Approach": "ALT measures DAMAGE, not FUNCTION. A dog with end-stage cirrhosis might have a completely normal ALT because there are no healthy hepatocytes left to burst and leak the enzyme. Liver function is measured by Bile Acids or Ammonia tolerance."
    },
    2737: {
        "topic": "Urethral Calculi - Urethral Process",
        "Core_Anatomy": "Urethral process (vermiform appendage) of the penis.",
        "Pathogenesis_Immediate": "The most common site of urethral calculi obstruction in sheep and goats is the Urethral process.",
        "Pathogenesis_Deep": "Small ruminant males (rams and bucks) possess a unique, narrow, worm-like extension of the urethra at the tip of the penis called the urethral process. Because the lumen suddenly narrows here, urinary calculi (stones) passing down from the bladder almost always lodge at this exact point, causing complete obstruction. The second most common site is the sigmoid flexure.",
        "Why_Not": "Obstruction can occur at the sigmoid flexure, but the urethral process is the primary, most frequent site in small ruminants.",
        "Wow_Approach": "As noted previously, the immediate field treatment is simply snipping off the urethral process with scissors. This often dislodges the stone and saves the animal's life without requiring abdominal surgery."
    },
    2738: {
        "topic": "Vesicocele - Bladder Hernia",
        "Core_Anatomy": "Urinary bladder and abdominal wall defect.",
        "Pathogenesis_Immediate": "A hernia in which the Urinary Bladder is the herniated organ is termed a Vesicocele.",
        "Pathogenesis_Deep": "Medical terminology for hernias uses suffixes attached to the organ involved. 'Vesico-' refers to the bladder; '-cele' refers to a hernia or swelling. A vesicocele (or cystocele) occurs when the bladder herniates through a defect (e.g., an inguinal ring, perineal hernia, or abdominal wall tear). In dogs, perineal hernias frequently contain the retroflexed bladder, causing sudden urinary obstruction—a surgical emergency.",
        "Why_Not": "Uterus hernia = hysterocele. Cecum hernia = typhlocele. Scrotal hernia = oscheocele. Vesicocele strictly means the bladder.",
        "Wow_Approach": "If a male dog with a perineal hernia suddenly becomes anuric (cannot pee) and systemically sick, assume the bladder has retroflexed into the hernia sac and the urethra is kinked. Emergency cystocentesis to drain the bladder and unkink the urethra is required before surgical repair."
    },
    2739: {
        "topic": "Intussusception Definition",
        "Core_Anatomy": "Intestinal tract.",
        "Pathogenesis_Immediate": "Telescoping of one part of the intestine into an adjacent part is called Intussusception.",
        "Pathogenesis_Deep": "The proximal segment (intussusceptum) usually telescopes into the distal segment (intussuscipiens), propelled by hypermotility. The trapped segment's mesenteric blood vessels are immediately compressed, leading to venous congestion, edema, and eventually arterial occlusion (ischemic necrosis). It causes a complete mechanical obstruction and sloughing of the intestinal mucosa (resulting in classic 'currant jelly' bloody diarrhea).",
        "Why_Not": "Torsion is twisting on the long axis. Volvulus is twisting of the bowel on its mesenteric axis (cutting off blood supply). Typhlitis is inflammation of the cecum. Telescoping is uniquely intussusception.",
        "Wow_Approach": "During surgery, manual reduction of an intussusception must be done by gently SQUEEZING the distal segment to push the trapped bowel out. NEVER PULL the proximal segment—the necrotic bowel will tear instantly, spilling feces into the abdomen."
    },
    2751: {
        "topic": "Essay - Surgical Treatment of Abscess",
        "Core_Anatomy": "Skin and subcutaneous tissue.",
        "Pathogenesis_Immediate": "Essay prompt regarding abscess management.",
        "Pathogenesis_Deep": "Key points required for the essay: (1) Wait for maturation (pointing) using hot fomentation. (2) Clip and aseptically prepare the site. (3) Incise vertically at the lowest dependent point for gravity drainage. (4) Evacuate pus. (5) Flush the cavity with 0.1% KMnO4 or weak Povidone-Iodine. (6) Leave open to heal by second intention. (7) Apply systemic antibiotics if the animal is febrile.",
        "Why_Not": "Never suture a drained abscess closed—it will instantly reform.",
        "Wow_Approach": "For deep abscesses, inserting a Penrose drain or a gauze wick soaked in hypertonic saline/honey encourages continuous drainage while the cavity granulates from the inside out."
    },
    2755: {
        "topic": "Essay Section Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header instructing students to write essays on two topics.",
        "Pathogenesis_Deep": "Tests comprehensive surgical understanding rather than isolated facts.",
        "Why_Not": "Structural marker.",
        "Wow_Approach": "N/A"
    },
    2768: {
        "topic": "VSR Module Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper I.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2769: {
        "topic": "VSR Module Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper I.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2770: {
        "topic": "Exam Instruction - Time Limit",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction allocating 1 hour for the objective section.",
        "Pathogenesis_Deep": "Tests speed and automaticity of knowledge recall.",
        "Why_Not": "Structural marker.",
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
