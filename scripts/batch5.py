import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    78: {
        "topic": "Blood Type Universal Donor in Cats (Type A vs Type B)",
        "Core_Anatomy": "Feline erythrocyte surface membrane antigens and the neonatal gut mucosa (in neonatal isoerythrolysis).",
        "Pathogenesis_Immediate": "In cats, the AB blood group system is the dominant transfusion compatibility system. Type B cats have very strong naturally occurring anti-A alloantibodies that cause an immediate, fatal haemolytic reaction if given Type A blood.",
        "Pathogenesis_Deep": "Unlike dogs (where alloantibodies develop only after sensitization), cats naturally develop strong alloantibodies against the blood group antigens they lack. Type B cats (rare in domestic shorthairs, common in British Shorthairs and Somalis) have potent anti-A haemagglutinins and haemolysins that activate complement, causing rapid, catastrophic intravascular haemolysis, haemoglobinaemia, haemoglobinuria, and shock within minutes of a mismatched transfusion.",
        "Why_Not": "In dogs, DEA 1.1 is the primary concern because anti-DEA 1.1 antibodies only form after the first sensitizing transfusion. In cats, anti-A and anti-B antibodies are naturally present, making blood typing mandatory before every feline transfusion even in a first-time recipient.",
        "Wow_Approach": "Neonatal Isoerythrolysis (NI) is a critical neonatal syndrome when Type A or AB kittens nurse from a Type B queen: colostral anti-A antibodies are absorbed through the neonatal gut, causing life-threatening haemolytic anaemia. Prevent by blood typing breeding queens and removing kittens from Type B queens for the first 16-24 hours."
    },
    79: {
        "topic": "Non-Shivering Thermogenesis (Brown Adipose Tissue) in Neonates",
        "Core_Anatomy": "Brown adipose tissue (BAT) — located in the interscapular, perirenal, and periaortic regions — and the sympathetic nervous system.",
        "Pathogenesis_Immediate": "The principal site of cold-induced non-shivering thermogenesis (NST) in neonatal and young animals is Brown Adipose Tissue (BAT), not skeletal muscle. BAT generates heat without mechanical shivering by uncoupling mitochondrial electron transport from ATP synthesis.",
        "Pathogenesis_Deep": "Brown adipocytes contain a uniquely high density of mitochondria and a specific inner mitochondrial membrane protein called Uncoupling Protein 1 (UCP1/Thermogenin). Sympathetic stimulation by cold exposure activates UCP1, which allows protons to flow back across the inner mitochondrial membrane without passing through ATP synthase. The proton gradient is dissipated as heat rather than being used to produce ATP, generating extremely rapid and highly efficient heat production specifically for thermoregulation in neonates.",
        "Why_Not": "Skeletal muscle shivering is the primary heat-generating mechanism in adult animals during cold stress, but it is energetically inefficient and fatiguing. Brown adipose NST produces heat silently without any muscular effort, allowing neonates to maintain core temperature while their skeletal muscle mass is still minimal.",
        "Wow_Approach": "Neonatal foals, calves, and lambs are highly vulnerable to hypothermia at birth because BAT stores are limited, and shivering capacity is immature. Dry and warm neonates immediately after birth, ensure colostrum intake within 1-2 hours (colostrum provides glucose for thermogenesis), and use warming blankets in cold environments to prevent fatal neonatal hypothermia."
    },
    81: {
        "topic": "Pantothenic Acid (Vitamin B5) Deficiency - Goose-Stepping Gait in Pigs",
        "Core_Anatomy": "The peripheral nerves, the dorsal root ganglia, and the posterior funiculi of the spinal cord in pigs.",
        "Pathogenesis_Immediate": "Pantothenic acid (Vitamin B5) deficiency in pigs causes a characteristic 'goose-stepping' (hypermetric/high-stepping) gait of the hindlimbs due to degeneration of peripheral sensory nerve fibres and the spinal cord posterior columns.",
        "Pathogenesis_Deep": "Pantothenic acid is an essential component of Coenzyme A (CoA) and the Acyl Carrier Protein (ACP). Deficiency impairs fatty acid synthesis and energy metabolism in rapidly dividing cells, particularly myelinating Schwann cells. Peripheral nerve demyelination disrupts proprioceptive feedback from the hindlimb muscles; pigs cannot sense their hindlimb position, leading to the exaggerated, high-stepping gait characteristic of proprioceptive ataxia.",
        "Why_Not": "Thiamine (B1) deficiency causes Polioencephalomalacia (cerebrocortical necrosis) in ruminants, presenting with star-gazing and blindness, not goose-stepping. Riboflavin (B2) deficiency causes dermatitis, poor growth, and photosensitivity. Only Pantothenic acid (B5) deficiency produces the characteristic goose-stepping gait in pigs.",
        "Wow_Approach": "Prevent by ensuring complete, balanced commercial pig diets containing minimum 10 mg pantothenic acid/kg of feed. Treat deficient animals with 50 mg/day of calcium pantothenate orally. If caught early, nerve damage is reversible within 4-6 weeks; chronic deficiency leads to irreversible spinal cord lesions."
    },
    83: {
        "topic": "Nitrate/Nitrite Toxicosis and Methylene Blue Antidote in Cattle",
        "Core_Anatomy": "The erythrocyte haemoglobin molecule (iron atom), the systemic vascular endothelium, and the rumen (site of nitrate reduction).",
        "Pathogenesis_Immediate": "Nitrate toxicosis in cattle (from grazing nitrate-accumulating plants or drinking nitrate-contaminated water) converts haemoglobin to methaemoglobin, which cannot carry oxygen, causing cyanosis, muddy-brown blood, and tissue hypoxia (histotoxic anoxia).",
        "Pathogenesis_Deep": "Rumen bacteria convert ingested nitrate (NO3-) to nitrite (NO2-). Nitrite is absorbed into the bloodstream and oxidizes the ferrous iron (Fe2+) of haemoglobin to ferric iron (Fe3+), forming methaemoglobin (MetHb). MetHb cannot bind oxygen, and its presence shifts the oxygen-dissociation curve left (Bohr effect), impairing oxygen delivery to tissues. Blood becomes dark chocolate-brown. Cows on rapid plant growth (corn, sorghum, grasses) after rainfall or drought-stress are at high risk.",
        "Why_Not": "Carbon monoxide poisoning also causes tissue hypoxia by forming carboxyhaemoglobin. However, carboxyhaemoglobin gives blood a bright cherry-red colour, while methaemoglobin causes characteristic chocolate-brown blood — a key differentiating gross pathology finding.",
        "Wow_Approach": "Administer 1% Methylene Blue solution IV at 4-8 mg/kg. Methylene blue (as a reducing agent via the NADPH pathway) converts methaemoglobin back to functional haemoglobin within minutes. Dramatically satisfying treatment response: blood turns from chocolate-brown back to bright red as oxygen transport is restored."
    },
    84: {
        "topic": "Pregnancy Toxaemia (Ketosis) vs Parturient Paresis - Frog-Leg Differential",
        "Core_Anatomy": "The hepatic mitochondria (ketogenic pathway), the hypothalamus (glucose homeostasis), and the skeletal neuromuscular junction (calcium).",
        "Pathogenesis_Immediate": "Frog-like posture (hindlimbs extended caudally in lateral recumbency) is most commonly associated with Pregnancy Toxaemia in ewes and Parturient Hypocalcaemia (Milk Fever) in cows. Distinguishing them is critical as treatment differs.",
        "Pathogenesis_Deep": "In Pregnancy Toxaemia, frog posture results from profound CNS hypoglycaemia causing hindlimb extensor muscle weakness. The ewe remains aware (responds to stimuli) initially. Ketone breath is detectable. Blood BHBA is markedly elevated. In Parturient Hypocalcaemia, frog posture occurs with the S-neck sign and complete loss of consciousness in Stage 2-3. The cow is areflexive. No ketone breath. Serum calcium is critically low (<1.0 mmol/L).",
        "Why_Not": "Polioencephalomalacia (Thiamine deficiency) causes opisthotonus (neck dorsiflexion) and star-gazing in ruminants, not the frog posture. Selenium deficiency causes stiffness and inability to rise without the distinctive hindlimb caudal extension.",
        "Wow_Approach": "Field differentiation test: apply a few ml of 50% Dextrose IV/IO. A ketotic animal will show improved responsiveness within 5-10 minutes (glucose corrects CNS hypoglycaemia). A milk fever cow requires IV calcium. If uncertain, administer calcium borogluconate first (it addresses the immediate life threat) followed by dextrose."
    },
    85: {
        "topic": "Zinc Phosphide Rodenticide - Acetylene-Like Odour and Phosphine Gas",
        "Core_Anatomy": "The gastric mucosa, the hepatic mitochondria, and the olfactory system (clinical sign detection).",
        "Pathogenesis_Immediate": "Zinc Phosphide poisoning produces a characteristic acetylene-like (garlic/rotten fish) odour from the stomach contents during necropsy, caused by phosphine gas released from zinc phosphide reacting with gastric acid.",
        "Pathogenesis_Deep": "The diagnostic acetylene-like odour comes from phosphine gas (PH3) spontaneously venting from the stomach at autopsy. Phosphine is detectable at concentrations as low as 0.1-0.2 ppm. At necropsy, the stomach may be congested and haemorrhagic, the liver shows centrilobular necrosis, and the lungs show pulmonary oedema. The toxic phosphine is also hazardous to the attending veterinarian during necropsy; perform in a well-ventilated outdoor area.",
        "Why_Not": "ANTU poisoning causes milky-white pleural effusion (hydrothorax) without a distinctive gastric odour. Red Squill causes cardiac glycoside-type dysrhythmias. Fluoroacetate (Compound 1080) causes convulsions from TCA cycle blockade. Only Zinc Phosphide produces the pathognomonic phosphine smell.",
        "Wow_Approach": "Phosphine (PH3) is heavier than air (sinks to floor level). Ensure ventilation in treatment rooms where dogs vomit post-zinc phosphide ingestion. Safety protocol: wear N100 respirator and nitrile gloves when handling zinc-phosphide-poisoned vomit. No emesis induction in cats (cats vomit poorly and risk aspiration)."
    }
}

updated = 0
for q in data:
    if q['id'] in enrichment:
        q.update(enrichment[q['id']])
        updated += 1

with open(db_path, "w", encoding="utf-8") as f:
    f.write("// Auto-generated Hybrid Exam Database\n")
    f.write("const examData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n")

# Final validation
print(f"Batch 5/5 DONE: Updated {updated} questions.")

# Quick validation
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data_check = json.loads(json_str)
empty = [x for x in data_check if x.get('is_high_yield') and not x.get('Core_Anatomy')]
print(f"Validation: {len(data_check)} total entries. {len(empty)} high-yield questions still empty.")
