import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1549: {
        "topic": "Veterinary History - Renatus Vegetius",
        "Core_Anatomy": "N/A - Veterinary History.",
        "Pathogenesis_Immediate": "The statement 'Renatus Vegetius is regarded as the Father of Veterinary Medicine' is TRUE.",
        "Pathogenesis_Deep": "Publius Flavius Vegetius Renatus was a Roman writer in the 4th/5th century AD. He wrote the 'Digesta Artis Mulomedicinae' (a comprehensive guide to veterinary medicine, focusing heavily on horses and mules for the Roman army). Because he compiled and systemized existing veterinary knowledge (distinguishing it clearly from human medicine and magic), he is classically honored as the Father of Veterinary Medicine.",
        "Why_Not": "Hippocrates is the father of human medicine. Claude Bourgelat founded the first veterinary school in Lyon, France (1761), but Vegetius laid the ancient literary foundation.",
        "Wow_Approach": "Historical questions in VMD often serve as simple 'gimme' questions to reward students who read the introductory chapters of their medicine textbooks."
    },
    1556: {
        "topic": "Porcine Parakeratosis - Zinc Deficiency",
        "Core_Anatomy": "Epidermis (stratum corneum).",
        "Pathogenesis_Immediate": "Parakeratosis (matching question) is classically associated with Zinc deficiency in growing swine.",
        "Pathogenesis_Deep": "Zinc is an essential co-factor for DNA/RNA polymerases required by rapidly dividing cells, particularly the epidermis. In pigs fed high-calcium diets (which antagonize zinc absorption in the gut), severe zinc deficiency develops. The epidermal cells fail to shed their nuclei as they keratinize. This creates a thick, crusty, fissured, and non-pruritic scaly dermatitis over the belly and legs, termed Parakeratosis.",
        "Why_Not": "Iron deficiency causes microcytic hypochromic anemia (classic in indoor piglets). Calcium deficiency causes rickets. Zinc specifically causes the parakeratotic skin lesions.",
        "Wow_Approach": "If a farmer reports a severe, crusty skin disease in pigs that they are NOT scratching (non-pruritic), it is likely Parakeratosis (zinc deficiency). If they are scratching violently, it is Sarcoptic Mange."
    },
    1559: {
        "topic": "Capture Myopathy - Exertional Rhabdomyolysis",
        "Core_Anatomy": "Skeletal muscle and renal tubules.",
        "Pathogenesis_Immediate": "Capture myopathy (exertional rhabdomyolysis) is a fatal metabolic muscle disease triggered by extreme stress, fear, and prolonged exertion during the capture or transport of wild animals.",
        "Pathogenesis_Deep": "During a terrifying chase, the animal relies entirely on anaerobic glycolysis, causing a massive, unbuffered buildup of lactic acid in the muscles. This severe local acidosis destroys the muscle cell membranes (rhabdomyolysis), releasing massive amounts of myoglobin and potassium into the blood. The myoglobin clogs the renal tubules, leading to acute renal failure (myoglobinuric nephrosis), while the hyperkalemia causes fatal cardiac arrhythmias.",
        "Why_Not": "Nutritional myopathy (White Muscle Disease) is caused by Selenium/Vitamin E deficiency, not exertion. SIRS is systemic inflammation from sepsis.",
        "Wow_Approach": "In the wild, an animal may survive the initial capture but die days later from renal failure. Prevention is the only cure: use chemical immobilization (darting) quickly rather than pursuing the animal in a vehicle."
    },
    1562: {
        "topic": "VMD Objective Section - Fill in the Blanks",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of clinical terms, e.g., identifying exact nutrient deficiencies or specific anatomical respiratory patterns.",
        "Pathogenesis_Deep": "Unlike MCQs, there are no distractors to eliminate. This format tests whether the clinical sign (e.g., 'goose-stepping') has been perfectly linked in memory to its specific pathophysiological etiology (Pantothenic acid deficiency).",
        "Why_Not": "Vague answers like 'Vitamin B' will not receive credit when the specific B-vitamin (B5 vs B2) dictates entirely different clinical syndromes.",
        "Wow_Approach": "Group your study notes by 'Pathognomonic gait/posture' to ace this section."
    },
    1566: {
        "topic": "Goose Stepping Gait - Pantothenic Acid Deficiency",
        "Core_Anatomy": "Sciatic nerve and myelin sheath.",
        "Pathogenesis_Immediate": "The classic 'Goose Stepping' gait in pigs is due to a deficiency of Pantothenic acid (Vitamin B5).",
        "Pathogenesis_Deep": "Pantothenic acid is a critical component of Coenzyme A (CoA), which is essential for fatty acid synthesis and the maintenance of myelin in the peripheral nervous system. In growing pigs fed a deficient diet (e.g., heavily heated/processed grain), the sciatic nerve undergoes Wallerian degeneration. This causes a progressive spasticity of the hindlimbs. The pig lifts its hindlegs abnormally high and kicks them out straight before placing them down, mimicking a military 'goose-step'.",
        "Why_Not": "Niacin deficiency causes pellagra (diarrhea/dermatitis). Folic acid deficiency causes macrocytic anemia. Pyridoxine deficiency causes seizures. Riboflavin causes curled-toe paralysis in chicks.",
        "Wow_Approach": "Unlike other neurological diseases (like salt toxicity which affects the brain), pantothenic acid deficiency primarily affects the peripheral sciatic nerve, so the pig remains mentally alert with a normal appetite despite the bizarre gait."
    },
    1567: {
        "topic": "Equine Respiration - Costo-Abdominal Pattern",
        "Core_Anatomy": "Diaphragm and intercostal muscles.",
        "Pathogenesis_Immediate": "The normal type of respiration in healthy horses at rest is Costo-abdominal.",
        "Pathogenesis_Deep": "A normal horse utilizes both the ribcage (costal intercostal muscles) and the diaphragm (abdominal muscles) synchronously to breathe. If a horse experiences severe abdominal pain (colic or peritonitis), it will suppress abdominal movement and switch to a purely 'Costal' (chest-only) pattern. If it experiences severe pleuritis (chest pain), it will suppress chest movement and switch to a purely 'Abdominal' pattern, often developing a visible 'heave line' along the abdominal obliques.",
        "Why_Not": "Purely costal or purely abdominal breathing in a horse is always pathological, indicating severe pain in the non-moving cavity.",
        "Wow_Approach": "Observing the respiratory pattern from a distance before touching the horse provides immediate clues to localizing pain (chest vs abdomen)."
    },
    1568: {
        "topic": "Left Displacement of the Abomasum (LDA)",
        "Core_Anatomy": "Abomasum, rumen, and left abdominal wall.",
        "Pathogenesis_Immediate": "Left displacement of the abomasum (LDA) is the most common form of abomasal displacement in dairy cattle.",
        "Pathogenesis_Deep": "Post-calving, the rumen is temporarily smaller, leaving a void in the abdomen. If the cow develops abomasal atony (due to hypocalcemia or high-grain/high-VFA diets), the abomasum stops contracting and fills with gas. The gas-filled abomasum floats upward from its normal position on the ventral floor, sliding UNDER the rumen to become trapped between the rumen and the left body wall. This creates a classic, high-pitched 'ping' on auscultation/percussion of the left paralumbar fossa.",
        "Why_Not": "Right displacement (RDA) is less common but far more dangerous, as it often progresses to an abomasal volvulus (twist), causing rapid ischemic necrosis and death.",
        "Wow_Approach": "An LDA is typically a non-fatal metabolic issue causing a sudden drop in milk yield, whereas an RDA/Volvulus is an acute surgical emergency causing severe shock."
    },
    1569: {
        "topic": "Omasal Impaction - Ruminant Forestomach Obstruction",
        "Core_Anatomy": "Omasum (manyplies) and reticulo-omasal orifice.",
        "Pathogenesis_Immediate": "Omasal impaction is a severe mechanical obstruction of the third stomach compartment.",
        "Pathogenesis_Deep": "The omasum absorbs water and VFAs. If cattle are fed extremely coarse, dry, poor-quality roughage with inadequate water intake, the omasal leaves extract too much moisture, turning the ingesta into rock-hard, dry cakes that block the organ. It often occurs secondary to vagal indigestion or TRP (which paralyzes the omasum). Clinically, the cow shows complete anorexia, absolute cessation of feces, and a hard mass palpable in the right cranial abdomen.",
        "Why_Not": "Abomasal displacement involves gas floating the organ. Diaphragmatic hernia involves the reticulum migrating into the chest. Caecal obstruction occurs in the hindgut.",
        "Wow_Approach": "Because the omasum is located deep under the ribs on the right side, it is extremely difficult to access surgically. Treatment usually relies on aggressive IV fluids and oral administration of mineral oil/epsom salts to soften the impaction."
    },
    1570: {
        "topic": "Capture Myopathy - Deer Susceptibility",
        "Core_Anatomy": "Skeletal muscle and renal tubules.",
        "Pathogenesis_Immediate": "The most susceptible species for capture myopathy among wild animals is the Deer (and other wild ungulates like antelope).",
        "Pathogenesis_Deep": "Deer possess a very high proportion of fast-twitch (Type IIB) muscle fibers designed for explosive, short bursts of speed to escape predators. They have a relatively poor capacity for sustained aerobic running. If chased persistently (e.g., by a helicopter or dogs) or stressed heavily in a trap, their muscles rapidly deplete ATP and switch to anaerobic glycolysis. This generates massive amounts of lactic acid, leading to rapid muscle necrosis, myoglobinuria, and fatal renal failure.",
        "Why_Not": "Lions (predators) and Elephants are far less prone to the explosive panic-flight response that triggers this specific severe rhabdomyolysis compared to prey species like deer.",
        "Wow_Approach": "When capturing deer, chemical immobilization (darting) must be done from a blind or quietly. If the deer runs for more than 2-3 minutes before the drug takes effect, it has a high risk of dying from capture myopathy days later."
    },
    1575: {
        "topic": "Curled Toe Paralysis - Riboflavin (B2) Deficiency",
        "Core_Anatomy": "Sciatic nerve and avian digits.",
        "Pathogenesis_Immediate": "Curled toe paralysis is the classic matching sign for Riboflavin (Vitamin B2) deficiency in chicks.",
        "Pathogenesis_Deep": "Riboflavin is a critical component of FAD/FMN, required for cellular respiration. In rapidly growing chicks, a deficiency causes severe demyelination and hypertrophy of the peripheral nerves, specifically the sciatic nerve (which can swell to 4-5 times its normal size). The chicks develop a characteristic posture: they sit on their hocks with their toes tightly curled inward (curled-toe paralysis) because the damaged nerves cannot extend the digits.",
        "Why_Not": "Calcium gluconate is the treatment for milk fever (hypocalcemia) in cows, completely unrelated to avian curled-toe paralysis. Polyneuritis (star-gazing) in birds is caused by Thiamine (B1) deficiency.",
        "Wow_Approach": "If caught early (within the first few days of clinical signs), curled-toe paralysis is rapidly reversible by adding riboflavin to the drinking water. If demyelination is chronic, the paralysis is permanent."
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
