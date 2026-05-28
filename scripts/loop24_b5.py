import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2799: {
        "topic": "Povidone-Iodine - Antiseptic",
        "Core_Anatomy": "Skin and mucous membranes.",
        "Pathogenesis_Immediate": "Povidone-Iodine is classified as an Antiseptic.",
        "Pathogenesis_Deep": "As reviewed, Povidone-Iodine is an iodophor that slowly releases free iodine. It is an antiseptic (used on living tissue) rather than a disinfectant (used on inanimate objects). It has a very broad spectrum of activity against bacteria, fungi, viruses, and some spores. It is particularly valuable in veterinary ophthalmology: a very dilute solution (0.2%) is the ONLY safe antiseptic for preparing the cornea and conjunctiva for eye surgery (Chlorhexidine is strictly contraindicated in the eye as it causes severe corneal ulcers).",
        "Why_Not": "Disinfectants are for tables and floors. Antiseptics are for patient skin preparation.",
        "Wow_Approach": "Povidone-iodine scrub (containing detergent) should never be used in open wounds, as the detergent causes tissue necrosis. Only Povidone-iodine solution (aqueous, no detergent) should be used for wound lavage."
    },
    2800: {
        "topic": "Positive Contrast - Radiopaque",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "Positive contrast media (Barium, Iodine) appear Radiopaque (white) on radiographs.",
        "Pathogenesis_Deep": "These heavy elements absorb X-rays via the photoelectric effect, preventing the rays from reaching the film. The film remains unexposed (white) in these areas.",
        "Why_Not": "Negative contrast (Air) appears black.",
        "Wow_Approach": "N/A"
    },
    2802: {
        "topic": "Frostbite - Exposure to Cold",
        "Core_Anatomy": "Extremities (Ear tips, tail, digits).",
        "Pathogenesis_Immediate": "Frostbite is matched to Exposure to cold.",
        "Pathogenesis_Deep": "Severe peripheral vasoconstriction in sub-zero temperatures shunts blood to the core to preserve life. The resulting profound ischemia, combined with physical intracellular ice crystal formation, causes ischemic coagulative necrosis of the extremities.",
        "Why_Not": "Burns are from heat.",
        "Wow_Approach": "N/A"
    },
    2804: {
        "topic": "Nitrous Oxide Cylinder - Blue Color",
        "Core_Anatomy": "Anaesthetic machine.",
        "Pathogenesis_Immediate": "Medical Nitrous Oxide (N2O) cylinders are universally painted Blue.",
        "Pathogenesis_Deep": "Medical gas cylinders are color-coded to prevent fatal attachment errors. Oxygen is White (or Green in the US). Nitrous Oxide is Blue. Medical Air is Black/White (or Yellow in the US). Carbon Dioxide is Grey. Nitrous oxide provides excellent analgesia (the 'laughing gas' effect) and allows a significant reduction in the required dose of Isoflurane (the 'Second Gas Effect').",
        "Why_Not": "Attaching a blue nitrous cylinder to the oxygen yoke will asphyxiate the patient with 100% N2O. Machines have a 'Pin Index Safety System' (PISS) with uniquely spaced pins to physically prevent this mistake.",
        "Wow_Approach": "Nitrous oxide rapidly diffuses into air-filled spaces in the body. It is absolutely contraindicated in cases of Gastric Dilatation-Volvulus (GDV) or pneumothorax, as it will rapidly enter the gas-filled stomach or chest, massively increasing the pressure and killing the patient."
    },
    2806: {
        "topic": "VSR 421 - Regional Surgery Header",
        "Core_Anatomy": "Regional surgical anatomy.",
        "Pathogenesis_Immediate": "Header denoting the start of the Regional Veterinary Surgery section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2815: {
        "topic": "Apron Keratoplasty - Deep Corneal Ulcers",
        "Core_Anatomy": "Cornea and Bulbar Conjunctiva.",
        "Pathogenesis_Immediate": "An Apron type of keratoplasty (conjunctival pedicle graft) is used in the treatment of deep corneal ulcers or descemetoceles.",
        "Pathogenesis_Deep": "When a corneal ulcer is so deep that it reaches Descemet's membrane (a descemetocele), the eye is at imminent risk of rupturing. The cornea lacks blood vessels, so healing is very slow. A conjunctival 'apron' or pedicle graft involves cutting a strip of the highly vascular bulbar conjunctiva, rotating it over the ulcer, and suturing it directly into the corneal defect. This immediately provides physical support (plugging the hole), a direct blood supply, and serum antiproteases to halt the melting process of the ulcer.",
        "Why_Not": "Superficial ulcers heal with medical management (antibiotic drops/serum). Deep melting ulcers require this surgical graft to save the globe.",
        "Wow_Approach": "Once the cornea has fully healed (often 6-8 weeks later), the base of the conjunctival graft is snipped under local anaesthetic. The piece attached to the cornea will gradually shrink and become more transparent, restoring vision."
    },
    2817: {
        "topic": "Laparotomy Indications",
        "Core_Anatomy": "Abdominal cavity (linea alba).",
        "Pathogenesis_Immediate": "Laparotomy (ventral midline celiotomy) is indicated for intestinal obstruction, diaphragmatic hernia, and Caesarean section (All of the above).",
        "Pathogenesis_Deep": "A ventral midline laparotomy through the linea alba provides complete, rapid access to all abdominal organs in small animals. It is the approach of choice for exploring the abdomen (exploratory celiotomy) to find an intestinal obstruction, pulling abdominal organs out of the thorax during a diaphragmatic hernia repair, or accessing the uterus for a C-section.",
        "Why_Not": "Flank approaches provide limited access. The ventral midline is the universal small animal abdominal approach.",
        "Wow_Approach": "The linea alba is the white, avascular aponeurosis where the abdominal muscles meet. Suturing the linea alba is critical—if the surgeon misses the holding layer (the external rectus sheath) and only grabs muscle or fat, the abdomen will completely dehisce (burst open) within 3-5 days."
    },
    2818: {
        "topic": "Oesophageal Diverticulum - Surgical Treatment",
        "Core_Anatomy": "Cervical oesophagus.",
        "Pathogenesis_Immediate": "An oesophageal diverticulum must be treated Surgically.",
        "Pathogenesis_Deep": "As noted in previous loops, a diverticulum is an outpouching of the oesophageal wall that traps food, causing chronic regurgitation and aspiration pneumonia risk. Medical management is impossible; the stretched, weakened sac of tissue must be surgically resected (diverticulectomy) and the oesophageal wall reconstructed.",
        "Why_Not": "Probing it blindly risks rupturing the thin wall of the diverticulum, causing fatal mediastinitis.",
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
