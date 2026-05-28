import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3294: {
        "topic": "Pulsion Diverticulum",
        "Core_Anatomy": "Oesophagus.",
        "Pathogenesis_Immediate": "A Pulsion Diverticulum involves the herniation of the mucosal layer through a defect in the full thickness of the muscular wall.",
        "Pathogenesis_Deep": "An oesophageal diverticulum is a pathological pouch. A 'Pulsion' diverticulum occurs when there is a focal weakness or tear in the muscularis layer of the oesophagus. Internal pressure (from swallowing food) pushes the mucosa out through this hole, creating a balloon-like sac that traps food. A 'Traction' diverticulum, on the other hand, involves the full thickness wall being pulled outward by scarring from adjacent tissues.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3295: {
        "topic": "Gut Tie in Cattle",
        "Core_Anatomy": "Pelvic cavity and Spermatic cord.",
        "Pathogenesis_Immediate": "Gut Tie (Pelvic Hernia) is a specific strangulating intestinal obstruction in castrated male cattle (bullocks/steers).",
        "Pathogenesis_Deep": "This unique condition occurs years after a crude castration where the spermatic cord was forcibly pulled/torn rather than properly cut. The stump of the torn spermatic cord retracts into the abdomen and adheres to the abdominal wall or peritoneum, creating a taut fibrous band. A loop of intestine slips under this band and becomes trapped and strangulated (an internal hernia).",
        "Why_Not": "It only occurs in castrated males (never bulls or cows).",
        "Wow_Approach": "Because the trapped gut is in the caudal abdomen, it can often be palpated per rectum as a painful, tense band. Surgical correction requires a flank laparotomy to simply cut the fibrous band and release the bowel."
    },
    3296: {
        "topic": "Hypopyon",
        "Core_Anatomy": "Anterior chamber of the eye.",
        "Pathogenesis_Immediate": "Hypopyon is the accumulation of purulent exudate (pus) in the anterior chamber of the eye.",
        "Pathogenesis_Deep": "It is a severe sign of anterior uveitis or deep corneal ulceration. The white blood cells settle out by gravity, forming a distinct white/yellow fluid line at the bottom of the anterior chamber.",
        "Why_Not": "Hyphema is blood. Hypopyon is pus.",
        "Wow_Approach": "N/A"
    },
    3305: {
        "topic": "Abscess Treatment Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a subjective question on abscess treatment.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3319: {
        "topic": "VSR II Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3320: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3322: {
        "topic": "Orthopaedics Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the Orthopaedics and Lameness section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3323: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header for a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3324: {
        "topic": "Gonitis - Stifle Inflammation",
        "Core_Anatomy": "Stifle joint (Femorotibial/Femoropatellar).",
        "Pathogenesis_Immediate": "Inflammation of the stifle joint is specifically called Gonitis.",
        "Pathogenesis_Deep": "The stifle is the largest and most complex joint in the body. Gonitis can be acute (due to trauma, like a cranial cruciate ligament rupture) or chronic (osteoarthritis/DJD). In large animals, it causes severe, debilitating hindlimb lameness.",
        "Why_Not": "Carpitis is the carpus. Tarsitis is the hock. Gonitis strictly refers to the stifle.",
        "Wow_Approach": "N/A"
    },
    3325: {
        "topic": "Achilles Tendon Rupture - Plantigrade Stance",
        "Core_Anatomy": "Common calcanean tendon (Achilles) and Hock.",
        "Pathogenesis_Immediate": "Rupture of the tendo-achillis results in a dropped hock and a 'plantigrade' stance.",
        "Pathogenesis_Deep": "The common calcanean tendon (composed of the gastrocnemius, superficial digital flexor, and biceps femoris tendons) attaches to the tuber calcanei. It is the sole structure keeping the hock extended when the animal bears weight. If it is severed (e.g., by a dog fight bite to the back of the leg or a sharp laceration), the hock instantly collapses to the ground. The dog walks with its entire metatarsus flat on the floor (like a human foot), which is called a plantigrade stance.",
        "Why_Not": "Cruciate ligament rupture causes a drawer sign, not a dropped hock.",
        "Wow_Approach": "Surgical repair requires a heavy, locking loop suture pattern (like the 3-loop pulley or Krackow) to withstand the massive tension, followed by immobilization of the hock in extension for 6 weeks."
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
