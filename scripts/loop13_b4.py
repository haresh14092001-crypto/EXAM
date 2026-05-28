import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1539: {
        "topic": "Avian Physiology - Crop Milk",
        "Core_Anatomy": "Avian crop (ingluvies) squamous epithelium.",
        "Pathogenesis_Immediate": "Crop milk is uniquely associated with columbiformes (Pigeons and Doves).",
        "Pathogenesis_Deep": "Unlike mammalian milk (produced by mammary alveolar cells), crop milk is produced by the sloughing of fluid-filled, lipid-rich squamous epithelial cells lining the crop of both male and female pigeons. This process is driven by the hormone prolactin. The thick, cheese-like substance is regurgitated to feed the squabs (nestlings) for the first few days of life, providing essential proteins, fats, and immune factors (IgA).",
        "Why_Not": "Chickens, ducks, and turkeys do not produce crop milk; their chicks eat standard feed immediately upon hatching.",
        "Wow_Approach": "Because both male and female pigeons produce crop milk, an orphaned squab can be fostered by any adult pigeon actively rearing young, regardless of sex."
    },
    1540: {
        "topic": "Diaphragmatic Hernia - Bubaline Predisposition",
        "Core_Anatomy": "Diaphragm and reticulum.",
        "Pathogenesis_Immediate": "Diaphragmatic hernia is exceptionally common in the Buffalo compared to other large animals.",
        "Pathogenesis_Deep": "In the buffalo, the condition is almost always secondary to Traumatic Reticuloperitonitis (TRP). A sharp metallic foreign body (like a wire) penetrates the cranial wall of the reticulum and pierces the diaphragm. This creates a weak point (fistula) in the diaphragmatic muscle. The heavy weight of the pregnant uterus or a full rumen forces the reticulum to herniate through this tear into the thoracic cavity, compressing the lungs and heart.",
        "Why_Not": "While cows get TRP (hardware disease), their diaphragm is structurally thicker and they are more prone to pericarditis. Buffaloes have an inherent anatomical weakness in the tendinous portion of the diaphragm, making herniation much more likely.",
        "Wow_Approach": "A buffalo with a diaphragmatic hernia will typically present with recurrent, chronic tympany (bloat) that does not respond to standard treatments, and muffled heart sounds on the left side."
    },
    1541: {
        "topic": "Caprine Vital Signs - Normal Temperature",
        "Core_Anatomy": "Hypothalamic thermoregulatory center.",
        "Pathogenesis_Immediate": "The normal average body temperature for goat species is approximately 39.5°C (103.1°F).",
        "Pathogenesis_Deep": "Small ruminants (goats and sheep) naturally run hotter than large domestic animals (cows/horses) and humans. The normal physiological range for a goat is 39.0°C to 40.0°C. Therefore, a temperature of 39.5°C is perfectly normal and does not indicate an infectious fever.",
        "Why_Not": "37.5°C is normal for a human or dog, but represents severe hypothermia in a goat. 41.0°C (105.8°F) indicates a high fever (e.g., from severe pneumonia).",
        "Wow_Approach": "Always factor in environmental conditions: a healthy goat standing in the direct afternoon sun during summer may temporarily read 40.5°C without being sick."
    },
    1542: {
        "topic": "Plasma Volume Expanders - Hydroxyethyl Starch (HES)",
        "Core_Anatomy": "Intravascular space and capillary endothelium.",
        "Pathogenesis_Immediate": "Hydroxyethyl starch (HES) is an example of a colloidal Plasma Volume Expander.",
        "Pathogenesis_Deep": "Fluid therapy is divided into crystalloids and colloids. (1) Crystalloids (Normal Saline, Ringer's) contain small molecules that rapidly leak out of the capillaries into the interstitium (only ~25% remains in the blood after 1 hour). (2) Colloids (like HES, Dextran, or plasma) contain massive starch/protein molecules that cannot cross the capillary endothelium. They remain in the vasculature, exerting oncotic pressure to pull water INTO the blood vessel, rapidly expanding plasma volume during hypovolemic shock.",
        "Why_Not": "Ringer's solution and Normal Saline are crystalloids. They hydrate the tissues but do not provide sustained intravascular volume expansion like a colloid.",
        "Wow_Approach": "In severe hemorrhagic shock, a bolus of HES acts much faster and lasts much longer than crystalloids, buying critical time for a blood transfusion."
    },
    1543: {
        "topic": "Neurological Terminology - Paresis vs Plegia",
        "Core_Anatomy": "Spinal cord motor tracts and peripheral nerves.",
        "Pathogenesis_Immediate": "Precision in defining motor deficits: Paresis is weakness/partial loss; Plegia is complete paralysis.",
        "Pathogenesis_Deep": "Prefixes denote localization: (1) Hemi: one side of the body (left/right). (2) Para: the hindlimbs only (e.g., paraparesis means weakness of both hindlegs, localizing the lesion to the T3-L3 spinal cord). (3) Tetra/Quadri: all four limbs (localizing the lesion to the cervical spine C1-T2). Therefore, paraparesis is the most common presentation for conditions like IVDD in Dachshunds.",
        "Why_Not": "Using 'paraplegia' when a dog can still slightly move its toes is clinically incorrect. If voluntary motor is present, it is paresis.",
        "Wow_Approach": "Assess deep pain perception (nociception) by pinching the toes with hemostats. If deep pain is lost in paraplegia, the prognosis drops from 80% to <5% for surgical recovery."
    },
    1544: {
        "topic": "Syncope vs Seizure - Loss of Consciousness",
        "Core_Anatomy": "Cerebral cortex and cardiovascular system.",
        "Pathogenesis_Immediate": "The sudden, transient loss of consciousness for a short period (fainting) due to a sudden drop in cerebral blood flow is called Syncope.",
        "Pathogenesis_Deep": "Syncope is fundamentally a cardiovascular problem, not a primary neurological one. When cardiac output plummets (e.g., due to an arrhythmia, severe aortic stenosis, or vagal tone), the brain is temporarily starved of oxygen, causing the animal to collapse and lose consciousness. Once the animal falls horizontally, blood flow returns to the brain, and recovery is usually rapid and complete within seconds to minutes, without a post-ictal state.",
        "Why_Not": "A seizure involves abnormal electrical discharges in the brain, often presenting with jaw chomping, paddling, loss of bowel control, and a prolonged groggy recovery phase (post-ictal). Coma is a prolonged, deep state of unconsciousness. Asphyxia is suffocation.",
        "Wow_Approach": "If an owner reports their dog 'faints' every time it gets excited to play, immediately listen for a heart murmur or arrhythmias; this is classic exercise-induced syncope."
    },
    1545: {
        "topic": "Urination Terminology - Frequency vs Volume",
        "Core_Anatomy": "Urinary bladder and detrusor muscle.",
        "Pathogenesis_Immediate": "An abnormally frequent passage of small amounts of urine is called Pollakiuria.",
        "Pathogenesis_Deep": "Pollakiuria indicates irritation of the lower urinary tract (bladder or urethra), such as cystitis, bladder stones (urolithiasis), or feline lower urinary tract disease (FLUTD). The animal constantly feels the urge to urinate due to mucosal inflammation, but only passes a few drops at a time.",
        "Why_Not": "Polyuria is the passage of a massive, abnormally large VOLUME of urine (usually seen with renal failure or diabetes). Stranguria is straining/painful urination. Dysuria is difficult urination. Differentiating pollakiuria (frequency) from polyuria (volume) completely changes the diagnostic workup.",
        "Wow_Approach": "If a cat visits the litter box 20 times a day but leaves tiny clumps, it has pollakiuria (bladder issue). If it visits 3 times a day but leaves massive, overflowing clumps, it has polyuria (kidney/endocrine issue)."
    },
    1546: {
        "topic": "Acute Peritonitis - Hemogram (Leukogram) Changes",
        "Core_Anatomy": "Peritoneum, bone marrow, and systemic blood.",
        "Pathogenesis_Immediate": "In the case of acute, severe local peritonitis, the classic hemogram change is Leucocytosis with a regenerative left shift.",
        "Pathogenesis_Deep": "When the peritoneum is inflamed (e.g., from a ruptured bowel or TRP in cattle), a massive demand for neutrophils occurs. The bone marrow responds by releasing large numbers of mature neutrophils (leucocytosis/neutrophilia) and immature band neutrophils (a 'left shift') into the circulation. If the bone marrow can keep up with the demand (mature segmented neutrophils > immature bands), it is called a 'regenerative' left shift, indicating a strong immune response.",
        "Why_Not": "Leukopenia (low WBCs) with a degenerative left shift occurs when the infection is so overwhelming (e.g., severe sepsis) that it completely depletes the bone marrow reserves. Eosinophilia indicates parasites or allergies.",
        "Wow_Approach": "In a cow with acute TRP (peritonitis), a WBC count of 15,000/µL with a regenerative left shift is a positive prognostic sign. A WBC count of 3,000/µL with a degenerative left shift means she is dying of septic shock."
    },
    1547: {
        "topic": "Aponomma Ticks - Reptile Ectoparasites",
        "Core_Anatomy": "Reptilian integument.",
        "Pathogenesis_Immediate": "Ticks of the genus Aponomma (now largely reclassified into Amblyomma or Bothriocroton) are primarily noticed among Snakes and Reptiles.",
        "Pathogenesis_Deep": "Unlike Boophilus (cattle) or Rhipicephalus (dogs), Aponomma ticks are highly specialized ectoparasites that almost exclusively infest cold-blooded hosts, particularly large snakes (pythons) and monitor lizards. They cluster beneath the scales, particularly around the cloaca, eyes, and dorsal spine, where the skin is thinnest.",
        "Why_Not": "Finding them on mammals or elephants is exceptionally rare; they are the quintessential reptilian tick.",
        "Wow_Approach": "When treating a captive snake for a heavy tick burden, you must physically remove the ticks and use cautious, reptile-safe acaricides (like dilute ivermectin or fipronil), as reptiles are highly sensitive to many common mammalian tick dips."
    },
    1548: {
        "topic": "Hypomagnesemic Tetany - Grass Staggers",
        "Core_Anatomy": "Neuromuscular junction and cerebrospinal fluid.",
        "Pathogenesis_Immediate": "Hypomagnesemic tetany (Grass Tetany/Staggers) is a fatal metabolic disorder caused by acute magnesium deficiency.",
        "Pathogenesis_Deep": "Magnesium is required to block acetylcholine release at the neuromuscular junction. When a cow grazes lush, rapidly growing spring pastures (which are high in potassium and nitrogen but extremely low in available magnesium), her CSF magnesium drops rapidly. Without magnesium, the neurons fire uncontrollably. This results in hyperesthesia, violent muscle tremors, tetanic spasms, convulsions, and rapid death.",
        "Why_Not": "Parturient paresis (milk fever, hypocalcemia) causes flaccid paralysis (weakness, coma). Hypomagnesemia causes violent tetanic convulsions (rigidity).",
        "Wow_Approach": "To differentiate: if a downed cow is dull, floppy, and has a cold nose, she has hypocalcemia. If she is alert, twitching, aggressively hypersensitive to sound, and paddling violently, she has hypomagnesemia. Treat cautiously, as stress can trigger a fatal convulsion."
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
