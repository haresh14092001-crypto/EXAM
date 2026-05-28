import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1608: {
        "topic": "Veterinary Epidemiology - Herd Health Medicine",
        "Core_Anatomy": "Population-level epidemiology.",
        "Pathogenesis_Immediate": "Herd Health Medicine shifts the focus from treating an individual sick animal to optimizing the health, productivity, and economic viability of the entire herd.",
        "Pathogenesis_Deep": "This discipline relies heavily on preventative medicine: vaccination schedules, biosecurity protocols, nutritional profiling, and routine parasite control. It assumes that if one animal is clinically sick, many more are subclinically affected, which silently drains the farm's profitability. Thus, a herd health clinician uses tools like the Compton Metabolic Profile and bulk milk tank analysis rather than individual physical exams.",
        "Why_Not": "Sporadic disease refers to a single, isolated case occurring randomly. Herd health manages endemic/epidemic risks.",
        "Wow_Approach": "In herd health, it is often more economically sound to immediately cull (euthanize) a single sick animal (e.g., a cow with Mycoplasma bovis mastitis) rather than treat it, to protect the rest of the herd."
    },
    1611: {
        "topic": "VMD Objective Section Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Marks the beginning of the objective testing phase for VMD, focusing on rapid recall of systemic pathology.",
        "Pathogenesis_Deep": "This section typically heavily tests toxicology (snake bites, heavy metals) and metabolic diseases (calcium, phosphorus, and magnesium imbalances) because these present with acute, pathognomonic objective signs.",
        "Why_Not": "Subjective essays test the pathogenesis; this section tests the exact etiology.",
        "Wow_Approach": "Always read the units carefully in objective questions (e.g., total vs ionized calcium)."
    },
    1612: {
        "topic": "Bovine Hypocalcemia - Ionized Calcium",
        "Core_Anatomy": "Systemic blood and parathyroid gland.",
        "Pathogenesis_Immediate": "The normal serum ionized calcium level in cattle is approximately 1.0 to 1.3 mmol/L (4-5 mg/dL), representing the physiologically active fraction.",
        "Pathogenesis_Deep": "Total serum calcium (normally 9-11 mg/dL) is divided into three fractions: protein-bound (~40%), complexed (~10%), and ionized/free (~50%). The ionized fraction is the ONLY fraction capable of crossing cell membranes to facilitate neuromuscular transmission and muscle contraction. During the sudden onset of lactation (colostrogenesis), the massive drain on calcium specifically depletes the ionized fraction. If the parathyroid gland cannot mobilize bone calcium fast enough, the cow collapses in flaccid paralysis (Milk Fever).",
        "Why_Not": "Measuring total calcium can be misleading if the cow has severe hypoalbuminemia (low protein), which lowers total calcium but leaves the active ionized fraction perfectly normal.",
        "Wow_Approach": "Never give IV calcium gluconate too rapidly. High ionized calcium in the blood will directly stimulate the myocardium to contract maximally, stopping the heart in fatal systole."
    },
    1617: {
        "topic": "Multiple Choice Questions Header",
        "Core_Anatomy": "N/A - Examination Format.",
        "Pathogenesis_Immediate": "This header introduces standard MCQs, requiring the clinician to eliminate distractor etiologies.",
        "Pathogenesis_Deep": "MCQs in veterinary medicine often pair a disease with its most confusing differential (e.g., pairing hypocalcemia with hypomagnesemia). Success depends on identifying the single 'rule-out' clinical sign.",
        "Why_Not": "Do not select an answer simply because it causes similar signs; it must cause the EXACT signs described in the stem.",
        "Wow_Approach": "If two answers are exact opposites (e.g., Hypocalcemia vs Hypercalcemia), one of them is usually the correct answer."
    },
    1618: {
        "topic": "Lactation Tetany in Mares - Hypocalcemia",
        "Core_Anatomy": "Neuromuscular junction and skeletal muscle.",
        "Pathogenesis_Immediate": "Lactation tetany (also known as Eclampsia or Transit Tetany) in the mare is caused by Hypocalcaemia.",
        "Pathogenesis_Deep": "Unlike the cow, which develops flaccid paralysis (paresis) during hypocalcemia, the mare (and the bitch) develops severe tetanic spasms. In horses and dogs, a lack of extracellular calcium lowers the threshold potential of peripheral nerves. This makes the nerves hyperexcitable, firing spontaneously and causing violent, rigid muscle fasciculations, 'thumps' (diaphragmatic flutter), sweating, and stiff-legged gait.",
        "Why_Not": "Hypomagnesemia causes tetany in ruminants (Grass staggers) but is rarely the primary cause in mares. Hypercalcemia would depress the nervous system.",
        "Wow_Approach": "Always remember the species difference: Hypocalcemia = FLOPPY Cow, but RIGID/TWITCHING Mare and Bitch."
    },
    1619: {
        "topic": "Post-Parturient Hemoglobinuria (PPH) - Hypophosphatemia",
        "Core_Anatomy": "Erythrocyte plasma membrane and systemic blood.",
        "Pathogenesis_Immediate": "Post-parturient hemoglobinuria in high-producing dairy cows is primarily caused by severe Hypophosphatemia.",
        "Pathogenesis_Deep": "During early lactation, the cow loses massive amounts of phosphorus into the milk. Phosphorus is absolutely essential for the synthesis of ATP. Red blood cells (erythrocytes) rely entirely on glycolysis for ATP to power their Na+/K+ membrane pumps. When phosphorus drops critically low (<2.0 mg/dL), the RBCs cannot produce ATP. The membrane pumps fail, water rushes into the cells, and the RBCs undergo catastrophic intravascular hemolysis. The free hemoglobin spills into the urine, turning it dark red/brown (hemoglobinuria).",
        "Why_Not": "It is not a primary renal disorder; the kidneys are simply filtering out the massive amounts of free hemoglobin from the lysed RBCs. Hematuria (intact red blood cells) would indicate a renal/bladder issue.",
        "Wow_Approach": "You can easily differentiate PPH from Babesiosis (Tick Fever). Babesia also causes intravascular hemolysis, but the cow will have a high fever. In PPH, the cow's temperature is normal or subnormal."
    },
    1620: {
        "topic": "Falling Disease - Bovine Copper Deficiency (Repeated)",
        "Core_Anatomy": "Myocardium and vascular elastin.",
        "Pathogenesis_Immediate": "Falling disease in cattle is due to a severe deficiency of Copper.",
        "Pathogenesis_Deep": "Copper is the essential co-factor for lysyl oxidase, which cross-links elastin and collagen fibers. A chronic deficiency leads to severe weakening of the cardiovascular tissue. The cow will suffer acute heart failure (myocardial fibrosis) or a ruptured aorta upon mild exertion, literally dropping dead ('falling').",
        "Why_Not": "Cobalt deficiency causes wasting and ketosis. Magnesium causes tetanic convulsions. Manganese deficiency causes skeletal deformities (perosis).",
        "Wow_Approach": "Primary copper deficiency is rare; it is almost always secondary to grazing on pastures with high levels of Molybdenum and Sulfur, which bind Copper in the rumen into insoluble thiomolybdates."
    },
    1621: {
        "topic": "Toxicology - Viper Envenomation",
        "Core_Anatomy": "Vascular endothelium, platelets, and coagulation cascade.",
        "Pathogenesis_Immediate": "Viper envenomation (e.g., Russell's Viper, Rattlesnakes) in animals primarily causes Hemotoxic and Cytotoxic effects.",
        "Pathogenesis_Deep": "Viper venom is a highly complex soup of proteolytic enzymes, hyaluronidases, and phospholipases. It destroys the vascular endothelial lining, causing massive local tissue necrosis, swelling, and severe pain. Furthermore, the venom rapidly consumes the animal's clotting factors and platelets, leading to Disseminated Intravascular Coagulation (DIC). The animal bleeds uncontrollably from the bite site, mucous membranes, and internal organs.",
        "Why_Not": "Elapid snakes (Cobras, Kraits, Coral snakes) produce primarily Neurotoxins that cause flaccid paralysis and respiratory failure without massive local swelling.",
        "Wow_Approach": "If a dog presents with a snake bite and the face is massively swollen, bruising rapidly, and oozing blood, it is a Viper. If the dog has no swelling but is paralyzing and cannot swallow, it is an Elapid."
    },
    1622: {
        "topic": "Cud Dropping - Oral Pain and Neuropathy",
        "Core_Anatomy": "Oral cavity, pharynx, and cranial nerves (CN V, VII, IX, X).",
        "Pathogenesis_Immediate": "Cud dropping (quidding) in cattle is primarily caused by oral pain, dental disease, or cranial neuropathy (like Listeriosis), but in the context of forestomach disease, severe Vagal Indigestion or TRP can also disrupt normal rumination.",
        "Pathogenesis_Deep": "Normal rumination (cud-chewing) requires the coordinated regurgitation of a bolus, mastication, and reswallowing. If the cow drops the half-chewed cud from her mouth, it indicates either: (1) Severe pain (e.g., a wooden splinter in the hard palate, Actinobacillosis of the tongue, or molar abscess). (2) Neurological paralysis of the jaw/pharynx (e.g., Listeriosis affecting CN V/VII). (3) Severe systemic illness disrupting the vagal reflex (TRP).",
        "Why_Not": "Diaphragmatic hernia primarily causes chronic bloat and muffled heart sounds, not specific oral cud dropping.",
        "Wow_Approach": "Always wear thick gloves and use a mouth gag to manually explore the oral cavity of a cud-dropping cow. You will often find a simple physical obstruction, like a piece of wire wedged between the teeth."
    },
    1623: {
        "topic": "Avian Skeletal Deformities - Manganese Deficiency",
        "Core_Anatomy": "Tibiotarsal joint and gastrocnemius tendon.",
        "Pathogenesis_Immediate": "Manganese deficiency in growing birds causes a classic skeletal deformity known as Perosis (Slipped Tendon).",
        "Pathogenesis_Deep": "Manganese is essential for the synthesis of chondroitin sulfate, the major structural component of cartilage and bone matrix. In deficient chicks or poults, the epiphyseal growth plates of the long bones become severely deformed and flattened. As the tibiotarsal joint flattens, the deep groove that normally holds the gastrocnemius (Achilles) tendon in place disappears. The tendon slips laterally off the joint, permanently crippling the bird.",
        "Why_Not": "Rickets is caused by Calcium/Phos/Vit D deficiency and makes bones rubbery. Encephalitis is an infectious brain inflammation. Osteopenia is general bone thinning.",
        "Wow_Approach": "Once the tendon has slipped off the joint (Perosis), the anatomical damage is permanent. Nutritional supplementation with Manganese at this late stage will not cure the crippled bird; it only prevents the condition in the rest of the flock."
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
