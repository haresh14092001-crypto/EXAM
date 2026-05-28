import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3661: {
        "topic": "True or False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a True or False section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3671: {
        "topic": "Exam Instruction",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating marks for a section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3672: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3673: {
        "topic": "Radial Nerve Paralysis",
        "Core_Anatomy": "Forelimb (Extensor muscles).",
        "Pathogenesis_Immediate": "Radial nerve paralysis presents with the classic pathognomonic sign of a 'Dropped Elbow' and an inability to extend the carpus and digits.",
        "Pathogenesis_Deep": "The radial nerve innervates all the extensor muscles of the forelimb (triceps, extensor carpi radialis, common digital extensor). If the nerve is damaged (high up near the brachial plexus), the massive triceps muscle loses all tone. The elbow drops, and the animal cannot bear any weight on the leg. The carpus and digits knuckle over and drag on the ground.",
        "Why_Not": "Suprascapular nerve paralysis causes Sweeny (shoulder subluxation), not a dropped elbow.",
        "Wow_Approach": "If the damage is 'low' (distal to the triceps innervation), the animal can still bear weight and the elbow does not drop, but it will still knuckle at the carpus."
    },
    3674: {
        "topic": "Cunean Tenotomy - Bone Spavin",
        "Core_Anatomy": "Equine Hock (Medial aspect).",
        "Pathogenesis_Immediate": "A Cunean tenotomy is a surgical treatment historically performed for Bone Spavin.",
        "Pathogenesis_Deep": "Bone Spavin is osteoarthritis of the distal intertarsal and tarsometatarsal joints of the hock. The cunean tendon (the medial tendon of insertion of the cranial tibial muscle) runs directly over the medial aspect of these arthritic joints. When the joint capsule swells, the tight tendon acts like a painful band rubbing over the exostosis. Cutting this tendon (tenotomy) removes the pressure and provides pain relief.",
        "Why_Not": "It does not cure the arthritis; it only provides mechanical analgesia while waiting for the joints to naturally fuse.",
        "Wow_Approach": "N/A"
    },
    3675: {
        "topic": "Osteodystrophy",
        "Core_Anatomy": "Skeletal System (Calcium metabolism).",
        "Pathogenesis_Immediate": "Osteodystrophy refers to defective bone formation due to severe metabolic or nutritional imbalances (e.g., Calcium/Phosphorus ratios).",
        "Pathogenesis_Deep": "The classic example is Nutritional Secondary Hyperparathyroidism ('Bran Disease' or 'Big Head' in horses). Feeding a diet massively high in phosphorus and low in calcium (like pure wheat bran) causes constant parathyroid hormone release. PTH aggressively leaches calcium out of all the bones (osteodystrophia fibrosa), leaving them soft, spongy, and prone to spontaneous folding fractures. The body tries to replace the lost bone with fibrous tissue, causing the facial bones to swell massively ('Big Head').",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3676: {
        "topic": "Peroneal Nerve Paralysis",
        "Core_Anatomy": "Hindlimb (Hock and Digits).",
        "Pathogenesis_Immediate": "Peroneal nerve paralysis causes knuckling of the fetlock and an inability to flex the hock.",
        "Pathogenesis_Deep": "The common peroneal nerve is the dorsal branch of the sciatic nerve. It innervates the flexors of the hock and the extensors of the digits. It runs very superficially over the lateral aspect of the stifle/fibula head, making it highly vulnerable to being crushed when a large animal (like a cow) lies on hard concrete for too long. If paralyzed, the animal drags the dorsal aspect of its hoof on the ground (knuckling).",
        "Why_Not": "Tibial nerve paralysis (the other branch of the sciatic) causes a dropped hock and inability to extend the digits.",
        "Wow_Approach": "N/A"
    },
    3684: {
        "topic": "Subjective Type Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting a subjective (Define/Explain) section.",
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
