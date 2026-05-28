import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3574: {
        "topic": "Cortical Screws Usage (Review)",
        "Core_Anatomy": "Cortical bone.",
        "Pathogenesis_Immediate": "Cortical screws are specifically designed for cortical bone.",
        "Pathogenesis_Deep": "Reiterating that they have fine threads to grip hard bone.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3575: {
        "topic": "Orthopaedic Wire - Monofilament (Review)",
        "Core_Anatomy": "Fracture site.",
        "Pathogenesis_Immediate": "Orthopaedic (cerclage) wire is a monofilament.",
        "Pathogenesis_Deep": "Reiterating the use of solid stainless steel strands for maximum tensile strength and minimal infection risk.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3576: {
        "topic": "Interlocking Nail Sizes (Review)",
        "Core_Anatomy": "Long bones.",
        "Pathogenesis_Immediate": "Veterinary interlocking nails come in 6mm and 8mm sizes.",
        "Pathogenesis_Deep": "Reiterating their use in severe comminuted diaphyseal fractures.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3578: {
        "topic": "Complications of Fixation Options Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Options (Non-union, Mal-union, Delayed union) for the complications question.",
        "Pathogenesis_Deep": "Structural artifact.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3579: {
        "topic": "Plaster of Paris Temperature (Review)",
        "Core_Anatomy": "External coaptation.",
        "Pathogenesis_Immediate": "Plaster of Paris uses lukewarm water (approx 37°C).",
        "Pathogenesis_Deep": "Reiterating the risk of severe thermal burns if hot water is used to accelerate the exothermic reaction.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3580: {
        "topic": "Tibia Plating Approach (Review)",
        "Core_Anatomy": "Tibia (Medial surface).",
        "Pathogenesis_Immediate": "The medial approach is used for plating the tibia.",
        "Pathogenesis_Deep": "Reiterating the lack of muscle coverage on the medial aspect.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3581: {
        "topic": "Plate Removal Indications (Review)",
        "Core_Anatomy": "Healed fracture site.",
        "Pathogenesis_Immediate": "Bone plates are removed due to irritation, infection, or stress shielding.",
        "Pathogenesis_Deep": "Reiterating the specific complications that necessitate a second surgery to extract the hardware.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3582: {
        "topic": "Hydrotherapy - Downer Cow (Review)",
        "Core_Anatomy": "Skeletal muscle.",
        "Pathogenesis_Immediate": "The buoyancy of water in a hydrotherapy pool is used to treat Downer Cow syndrome.",
        "Pathogenesis_Deep": "Reiterating that removing the crushing weight of gravity allows ischemic muscles to perfuse and the cow to stand.",
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
