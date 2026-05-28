import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3209: {
        "topic": "Tail Amputation - Epidural Anaesthesia",
        "Core_Anatomy": "Sacrococcygeal space and Cauda equina.",
        "Pathogenesis_Immediate": "Tail amputation (docking) in cattle can be easily performed under Epidural anesthesia.",
        "Pathogenesis_Deep": "A caudal epidural is performed by injecting local anaesthetic (Lidocaine) into the sacrococcygeal (S5-Co1) or first intercoccygeal (Co1-Co2) space. This blocks the caudal nerve roots (pudendal and coccygeal nerves). It completely desensitizes the tail, perineum, and vulva, allowing for painless tail amputation (usually for severe tail necrosis/gangrene) while the cow remains standing.",
        "Why_Not": "General anaesthesia (inhalant or dissociative) is entirely unnecessary and dangerous for a simple tail amputation. The epidural is cheap, safe, and highly effective.",
        "Wow_Approach": "To ensure you are in the correct epidural space, place a drop of local anaesthetic in the hub of the needle. Because the epidural space has negative pressure, the 'Hanging Drop' will be instantly sucked into the needle when it pierces the ligamentum flavum."
    },
    3210: {
        "topic": "Atropine Contraindications - Horses/Cattle",
        "Core_Anatomy": "Gastrointestinal tract (Parasympathetic innervation).",
        "Pathogenesis_Immediate": "Atropine as a routine pre-anaesthetic is strongly contraindicated in Horses and Cattle.",
        "Pathogenesis_Deep": "Atropine is an anticholinergic (parasympatholytic) drug that blocks acetylcholine at muscarinic receptors. In horses, it completely paralyzes the motility of the cecum and large colon, leading to fatal post-operative ileus and colic. In cattle, it makes the copious ruminal saliva extremely thick and viscid (ropy), increasing the risk of airway obstruction, while also paralyzing the rumen and causing fatal bloat.",
        "Why_Not": "In dogs and cats, Atropine is routinely used to prevent bradycardia. (Note: Rabbits naturally produce an enzyme called 'atropinesterase' that instantly degrades atropine, making the drug totally useless, but not necessarily dangerous).",
        "Wow_Approach": "If a horse develops life-threatening bradycardia or AV block under anaesthesia, you must still give Atropine to save its life, but you must be prepared to aggressively treat the subsequent severe colic that will inevitably follow."
    },
    3211: {
        "topic": "Anaesthetic of Choice in Cats - Ketamine",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "A common, safe, and highly effective injectable anaesthetic choice in cats is Ketamine.",
        "Pathogenesis_Deep": "Unlike dogs (who metabolize ketamine quickly in the liver), cats eliminate a large portion of Ketamine unchanged through their kidneys. This allows for highly reliable, profound intramuscular (IM) sedation/anaesthesia in aggressive or feral cats. A 'Ketamine-combo' (e.g., Ketamine + Xylazine or Ketamine + Dexmedetomidine + Butorphanol, aka 'Kitty Magic') is the gold standard for sedating intractable felines.",
        "Why_Not": "Thiopentone requires an IV catheter, which is impossible to place in a feral, fighting cat. Diazepam provides mild sedation but zero pain control. Ketamine can be darted or squirted IM.",
        "Wow_Approach": "Cats under Ketamine anaesthesia maintain their palpebral (blink) and swallow reflexes, and their eyes remain wide open. You must apply ophthalmic ointment immediately, otherwise the corneas will dry out and ulcerate."
    },
    3212: {
        "topic": "Cystography - Contrast Radiography (Review)",
        "Core_Anatomy": "Urinary bladder.",
        "Pathogenesis_Immediate": "Cystography is a contrast radiographic technique specifically evaluating the Urinary bladder.",
        "Pathogenesis_Deep": "As reviewed previously, iodine or air is instilled via a urinary catheter to outline bladder stones, tumors, or ruptures.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3213: {
        "topic": "Pregnancy Contraindications - Barbiturates",
        "Core_Anatomy": "Placenta and Fetal CNS.",
        "Pathogenesis_Immediate": "Among the options provided, Barbiturates are strongly contraindicated during pregnancy, particularly for Caesarean sections.",
        "Pathogenesis_Deep": "Barbiturates (like Thiopentone) are highly lipophilic and readily cross the placental barrier. Because the fetal liver is too immature to metabolize the drug, the barbiturates heavily depress the fetal central nervous and respiratory systems. If a C-section is performed using barbiturate induction, the puppies/calves will be born completely apneic (not breathing) and profoundly sedated, resulting in massive neonatal mortality.",
        "Why_Not": "Propofol is rapidly cleared and is much safer for C-sections. Diazepam has minimal cardiovascular effects. Xylazine is the primary contraindication in cattle (causes abortion), but barbiturates are universally dangerous for the fetuses at term.",
        "Wow_Approach": "The safest induction protocol for a canine C-section is Propofol or Alfaxalone, followed immediately by Isoflurane, allowing the puppies to wake up and breathe the moment they are delivered."
    },
    3222: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting a matching question block.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3224: {
        "topic": "Jabot - Oesophageal Diverticulum",
        "Core_Anatomy": "Oesophagus.",
        "Pathogenesis_Immediate": "The term 'Jabot' is historically matched with an oesophageal diverticulum (or the crop in birds).",
        "Pathogenesis_Deep": "Jabot is a French term originally referring to the crop of a bird (a muscular pouch near the gullet). In veterinary medicine, it is occasionally used to describe a pathological, sac-like dilation (diverticulum) of the lower oesophagus that traps food and mimics the function of a crop.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3225: {
        "topic": "Pig Eye - Microphthalmia",
        "Core_Anatomy": "Globe (Eye).",
        "Pathogenesis_Immediate": "The term 'Pig eye' is clinically matched with Microphthalmia.",
        "Pathogenesis_Deep": "Microphthalmia is a congenital developmental defect where the entire globe of the eye is abnormally small. Because the eye is too small for the orbit, the third eyelid often protrudes permanently. 'Pig eye' is an older colloquial term for this appearance.",
        "Why_Not": "Macrophthalmia (Buphthalmos) is an enlarged eye, typically due to glaucoma.",
        "Wow_Approach": "Microphthalmia is frequently linked to genetic coat color defects, such as 'Lethal White' foals or double-merle (homozygous merle) breeding in dogs (e.g., Australian Shepherds, Great Danes). These animals are often born deaf and completely blind with tiny, non-functional eyes."
    },
    3226: {
        "topic": "Grid Lines - Potter-Bucky Diaphragm",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "Grid lines are the artifact removed by the Potter-Bucky diaphragm.",
        "Pathogenesis_Deep": "A stationary grid sits directly on top of the film cassette. While it stops scatter, its lead strips cast fine, white shadows (grid lines) directly onto the final radiograph. To eliminate these lines, the Potter-Bucky mechanism physically moves/oscillates the grid during the exposure, blurring the lines out of existence while still absorbing the scatter.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3227: {
        "topic": "Iodine - Positive Contrast",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "Iodine is matched with Positive contrast agent.",
        "Pathogenesis_Deep": "Like Barium, Iodine is a heavy element (high atomic number) that stops X-rays. Water-soluble iodinated contrast media (like Iohexol) are injected intravenously to highlight the kidneys/ureters (IVP), or injected into the spinal canal (myelogram) or joints (arthrogram).",
        "Why_Not": "Barium is also positive contrast, but it can NEVER be injected IV or into the spinal cord, as it is a highly inflammatory heavy metal suspension that will cause fatal granulomas. Barium is strictly for the GI tract.",
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
