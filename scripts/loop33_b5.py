import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3798: {
        "topic": "Subluxation",
        "Core_Anatomy": "Synovial joints.",
        "Pathogenesis_Immediate": "The incomplete abnormal separation of joint surfaces is called a Subluxation.",
        "Pathogenesis_Deep": "Unlike a complete luxation (dislocation) where the bones are entirely separated and have no contact, a subluxation is a partial dislocation. The articular surfaces are abnormally aligned but still maintain some contact. It is usually caused by chronic ligamentous laxity or mild trauma.",
        "Why_Not": "Luxation and dislocation are synonymous for complete separation.",
        "Wow_Approach": "N/A"
    },
    3799: {
        "topic": "Pectus Excavatum",
        "Core_Anatomy": "Sternum and Costal cartilages (Thorax).",
        "Pathogenesis_Immediate": "Pectus excavatum is a congenital skeletal deformity characterized by the dorsal intrusion of the sternum, causing severe dorso-ventral compression of the thorax.",
        "Pathogenesis_Deep": "This congenital deformity (seen in puppies and kittens) involves the inward funneling of the caudal sternum and costal cartilages. This physically restricts the thoracic volume, compressing the lungs and shifting the heart laterally, leading to exercise intolerance, dyspnea, and murmurs.",
        "Why_Not": "Pectus carinatum ('pigeon chest') is the opposite—an outward protrusion of the sternum.",
        "Wow_Approach": "In young animals whose bones are still highly pliable, this can be corrected non-invasively by applying a custom-molded external fiberglass splint to the chest and suturing the sternum outward to the splint for 3-4 weeks."
    },
    3800: {
        "topic": "Splayed Foot (Review)",
        "Core_Anatomy": "Distal limb.",
        "Pathogenesis_Immediate": "A splayed foot refers to a toe-out (base-wide) conformation.",
        "Pathogenesis_Deep": "Reiterating that this conformation causes asymmetric joint loading and a dishing gait.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3801: {
        "topic": "Racing Joint (Equine Carpus)",
        "Core_Anatomy": "Equine Carpus ('Knee').",
        "Pathogenesis_Immediate": "In racehorses, the Carpus (Knee) is commonly referred to as the 'Racing Joint'.",
        "Pathogenesis_Deep": "Due to the extreme concussive forces and hyperextension that occur at high-speed gallops, the equine carpus is highly prone to severe injuries, particularly osteochondral chip fractures (most commonly on the distal radius or radial carpal bone) and osteoarthritis. Because it is the most common site of major skeletal injury in Thoroughbreds, it has earned the nickname 'Racing Joint'.",
        "Why_Not": "The hock and fetlock undergo stress, but the classic 'racing joint' of horse racing lore is strictly the carpus.",
        "Wow_Approach": "N/A"
    },
    3802: {
        "topic": "Coon Foot in Horses",
        "Core_Anatomy": "Equine Pastern (SDF & Suspensory apparatus).",
        "Pathogenesis_Immediate": "A 'Coon Foot' is an equine conformational defect characterized by an abnormally low (flat) pastern angle relative to a normal hoof angle, often associated with stretching/weakness of the suspensory apparatus.",
        "Pathogenesis_Deep": "Normally, the hoof and pastern should form a single, continuous straight line (45-50 degrees). In a coon foot, the pastern drops ventrally (slopes excessively), while the hoof wall remains upright. This places extreme, chronic tensile strain on the deep digital flexor tendon, suspensory ligament, and sesamoid bones, leading to early suspensory breakdown.",
        "Why_Not": "Rupture of the extensor tendons causes knuckling, not dropping of the pastern.",
        "Wow_Approach": "N/A"
    },
    3803: {
        "topic": "False Quarter",
        "Core_Anatomy": "Equine Hoof (Coronary Band).",
        "Pathogenesis_Immediate": "An extensive injury to the coronet (coronary band) that permanently disrupts horn growth and causes a deep vertical gap in the hoof wall is called a False Quarter.",
        "Pathogenesis_Deep": "The coronary band is the sole source of the hard outer hoof wall. If a portion of the coronet is severely crushed, lacerated, or necrotized, it can no longer produce keratinized horn. As the hoof grows, a permanent, deep vertical cleft (gap) forms in the wall at that spot (usually in the quarter). This leaves the underlying sensitive corium completely unprotected and prone to constant lameness and infection.",
        "Why_Not": "A sandcrack is a simple split in a fully formed hoof wall; a false quarter is a complete absence of wall tissue due to coronary band destruction.",
        "Wow_Approach": "N/A"
    },
    3804: {
        "topic": "True or False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a True or False section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3815: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
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
