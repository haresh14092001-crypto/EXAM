import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3439: {
        "topic": "Green Osselets (Review)",
        "Core_Anatomy": "Fetlock joint.",
        "Pathogenesis_Immediate": "Green osselets are the acute, serous inflammation of the dorsal fetlock joint capsule.",
        "Pathogenesis_Deep": "Reiterating the traumatic origin in young racehorses.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3440: {
        "topic": "True Osselets (Review)",
        "Core_Anatomy": "Fetlock joint.",
        "Pathogenesis_Immediate": "True osselets are chronic, bony exostoses on the dorsal fetlock.",
        "Pathogenesis_Deep": "Reiterating the permanent osteoarthritic progression.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3441: {
        "topic": "Wind Puff (Windgall)",
        "Core_Anatomy": "Fetlock (Digital flexor tendon sheath).",
        "Pathogenesis_Immediate": "A Wind Puff (Windgall) is the chronic, non-painful distension of the digital flexor tendon sheath at the level of the fetlock.",
        "Pathogenesis_Deep": "Similar to a thoroughpin (which is at the hock), a wind puff is an idiopathic tenosynovitis. It appears as soft, fluctuant, fluid-filled swellings just proximal to the fetlock joint on the palmar/plantar aspect. It is a sign of chronic wear and tear (heavy work) but is generally just a cosmetic blemish that does not cause lameness.",
        "Why_Not": "Articular windgalls specifically involve the fetlock JOINT capsule, not the tendon sheath.",
        "Wow_Approach": "N/A"
    },
    3442: {
        "topic": "Septic Arthritis (Review)",
        "Core_Anatomy": "Synovial joints.",
        "Pathogenesis_Immediate": "Septic arthritis is an acute bacterial joint infection.",
        "Pathogenesis_Deep": "Reiterating the rapid, enzyme-mediated destruction of articular cartilage.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3445: {
        "topic": "Chronic Laminitis (Review)",
        "Core_Anatomy": "Equine hoof (P3).",
        "Pathogenesis_Immediate": "The chronic phase of laminitis involves the rotation of the pedal bone.",
        "Pathogenesis_Deep": "Reiterating the mechanical failure of the sensitive laminae.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3447: {
        "topic": "Seedy Toe (Hollow Wall)",
        "Core_Anatomy": "Equine Hoof (White Line).",
        "Pathogenesis_Immediate": "Seedy toe is the separation of the hoof wall from the underlying sensitive laminae at the toe, creating a crumbly, hollow cavity.",
        "Pathogenesis_Deep": "Usually secondary to chronic laminitis or white line disease, opportunistic bacteria and fungi invade the stretched, damaged white line at the toe. They literally eat away the inner stratum medium of the hoof wall, leaving a dry, crumbly, 'seedy' gray material. The hoof wall sounds hollow when tapped.",
        "Why_Not": "Thrush is an infection of the frog (palmar/plantar). Seedy toe is specifically at the dorsal toe/white line.",
        "Wow_Approach": "The only cure is to completely resect (cut away) all of the separated outer hoof wall to expose the anaerobic bacteria/fungi to the air, and then apply a special therapeutic shoe to support the hoof until the wall grows back (which takes 9-12 months)."
    },
    3458: {
        "topic": "Avulsion Fracture",
        "Core_Anatomy": "Bone (Apophysis/Tendon attachment).",
        "Pathogenesis_Immediate": "An Avulsion fracture occurs when a piece of bone is violently torn away by the attached tendon or ligament.",
        "Pathogenesis_Deep": "Tendons and ligaments are incredibly strong. During explosive physical trauma (e.g., a dog jumping and rapidly decelerating), the tendon itself does not snap; instead, it physically rips its bony attachment site (the apophysis) clean off the main bone. Classic examples include avulsion of the tibial tuberosity (pulled off by the patellar ligament) or the olecranon (pulled off by the triceps).",
        "Why_Not": "A transverse fracture is a direct break across the shaft. An avulsion fracture specifically involves a tendon/ligament attachment point being ripped off.",
        "Wow_Approach": "Avulsion fractures cannot be repaired with plates. Because the attached muscle is constantly pulling the broken bone fragment away, it MUST be repaired using a Tension Band Wire technique to neutralize the massive pulling force."
    },
    3459: {
        "topic": "Define/Answer Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a subjective definition section.",
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
