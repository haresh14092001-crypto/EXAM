import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3326: {
        "topic": "Ossifying Myopathy (Fibrotic Myopathy)",
        "Core_Anatomy": "Skeletal muscle (often Semitendinosus/Gracilis).",
        "Pathogenesis_Immediate": "Ossifying (or Fibrotic) myopathy results from severe trauma or chronic repetitive strain to a muscle.",
        "Pathogenesis_Deep": "When a muscle belly (most commonly the semitendinosus or gracilis in working dogs, or the semitendinosus in horses) suffers a severe tear, it heals via fibrosis. If the trauma is chronic or severe enough, the fibrotic scar tissue undergoes dystrophic calcification and eventually ossification (turning into actual bone within the muscle). This creates a rigid, non-elastic band that severely mechanically restricts the limb's range of motion.",
        "Why_Not": "It is not a primary bone disease or a tumor; it is a pathological healing response of damaged muscle tissue.",
        "Wow_Approach": "In dogs with gracilis fibrotic myopathy, they walk with a very characteristic, jerky, 'goose-stepping' gait. Surgery to cut the band provides immediate relief, but the condition almost universally recurs within months because the surgical cut itself heals with more fibrosis."
    },
    3327: {
        "topic": "Chondromalacia Patellae",
        "Core_Anatomy": "Patella (Articular cartilage).",
        "Pathogenesis_Immediate": "A degenerative change specifically in the articular cartilage of the patella is called Chondromalacia.",
        "Pathogenesis_Deep": "Chondromalacia involves the softening, fibrillation, and eventual erosion of the hyaline cartilage on the deep surface of the patella. It is almost always secondary to chronic patellar luxation or severe stifle malalignment, where the patella grinds abnormally against the trochlear ridges of the femur instead of gliding smoothly in the groove.",
        "Why_Not": "Osteoarthritis affects the whole joint. Chondromalacia specifically denotes the 'softening of cartilage' under the kneecap.",
        "Wow_Approach": "N/A"
    },
    3328: {
        "topic": "Thoroughpin - Tarsal Sheath Distension",
        "Core_Anatomy": "Equine Hock (Deep digital flexor tendon sheath).",
        "Pathogenesis_Immediate": "Distension of the tarsal sheath (the synovial sheath of the deep digital flexor tendon) in horses is called Thoroughpin.",
        "Pathogenesis_Deep": "Thoroughpin presents as a fluctuant, fluid-filled swelling in the hollows just cranial to the point of the hock (tuber calcanei), on both the medial and lateral sides (hence 'thorough-pin', as you can push the fluid 'through' from one side to the other). It is an idiopathic tenosynovitis or secondary to strain of the DDFT.",
        "Why_Not": "Bog spavin is distension of the tibiotarsal JOINT, not the tendon sheath. Bone spavin is osteoarthritis of the distal hock joints. Capped hock is bursitis of the superficial subcutaneous bursa.",
        "Wow_Approach": "Unlike bone spavin, true thoroughpin is usually just a cosmetic blemish and rarely causes actual lameness."
    },
    3340: {
        "topic": "Complete Fracture Definition",
        "Core_Anatomy": "Bone (Cortex and Medulla).",
        "Pathogenesis_Immediate": "A Complete fracture is the total disruption of the bone, breaking it into two or more distinct pieces.",
        "Pathogenesis_Deep": "The fracture line traverses the entire circumference of the bone, completely severing the cortex on all sides. This results in total loss of structural continuity and biomechanical stability.",
        "Why_Not": "An incomplete fracture (like a Greenstick fracture in young animals or a hairline fissure) only breaks one side of the cortex while the opposite side merely bends, retaining some structural continuity.",
        "Wow_Approach": "N/A"
    },
    3341: {
        "topic": "Canine Hip Dysplasia (CHD)",
        "Core_Anatomy": "Coxofemoral joint.",
        "Pathogenesis_Immediate": "Hip Dysplasia is the abnormal, lax development of the coxofemoral (hip) joint.",
        "Pathogenesis_Deep": "CHD is a highly heritable, polygenic, developmental disease of large breed dogs (Labs, German Shepherds). The primary defect is joint laxity (the ligamentum capitis femoris and joint capsule are too loose). This allows the femoral head to subluxate (rattle around) within the acetabulum as the puppy walks. This constant micro-trauma prevents the acetabulum from forming a deep, tight cup, leading to a shallow socket, flattened femoral head, and inevitable, severe osteoarthritis.",
        "Why_Not": "Legg-Calve-Perthes disease is avascular necrosis of the femoral head in small breeds, not developmental laxity. Hip luxation is acute trauma.",
        "Wow_Approach": "The Ortolani test is the gold standard physical exam maneuver to diagnose hip joint laxity in young puppies BEFORE radiographic arthritis develops."
    },
    3342: {
        "topic": "Intervertebral Disc Disease (IVDD) - Dachshunds",
        "Core_Anatomy": "Intervertebral discs (Nucleus pulposus).",
        "Pathogenesis_Immediate": "Intervertebral disc disease (Hansen Type I) is highly common in Chondrodystrophic breeds of dogs, most notably the Dachshund.",
        "Pathogenesis_Deep": "Chondrodystrophic breeds (Dachshunds, Basset Hounds, Corgis, French Bulldogs) have a genetic mutation that causes premature dwarfism of their limbs. This same mutation causes their intervertebral discs to undergo premature, massive chondroid metaplasia and calcification within the first year of life. The normally gel-like nucleus pulposus becomes hard and brittle. When the dog jumps, the brittle disc violently ruptures upward (extrusion) through the dorsal annulus, acting like a bullet striking the spinal cord.",
        "Why_Not": "Large breeds (like German Shepherds) get Hansen Type II IVDD, which is a slow, chronic bulging (protrusion) of the annulus in old age, not an acute explosive rupture.",
        "Wow_Approach": "A Dachshund that suddenly loses the use of its back legs (paraplegia) and loses deep pain sensation is an absolute surgical emergency. If a hemilaminectomy is not performed to decompress the spine within 24-48 hours, the paralysis becomes permanent."
    },
    3343: {
        "topic": "Hypertrophic Osteodystrophy (HOD)",
        "Core_Anatomy": "Metaphysis of long bones.",
        "Pathogenesis_Immediate": "Hypertrophic Osteodystrophy (HOD) is a developmental bone disease common in young, rapidly growing large breed dogs.",
        "Pathogenesis_Deep": "HOD presents as severe, acute, bilateral pain and swelling of the metaphyses of the long bones (most commonly the distal radius and ulna, and tibia). The dog is usually extremely febrile and reluctant to walk. It is characterized radiographically by a pathognomonic 'double physeal line' (a radiolucent line of necrosis parallel to the growth plate in the metaphysis) surrounded by dense, new bone formation.",
        "Why_Not": "Panosteitis affects the DIAPHYSIS (shaft), not the metaphysis. Osteochondritis dissecans (OCD) affects the ARTICULAR CARTILAGE (joint surface).",
        "Wow_Approach": "HOD is excruciatingly painful but usually self-limiting. Treatment consists of aggressive supportive care and NSAIDs until the dog finishes its rapid growth phase."
    },
    3344: {
        "topic": "HOD Age of Onset - 3 to 8 Months",
        "Core_Anatomy": "Long bones (Physes/Metaphyses).",
        "Pathogenesis_Immediate": "HOD classically presents in large/giant breed dogs between 3 to 8 months of age.",
        "Pathogenesis_Deep": "This is the window of maximum, explosive skeletal growth in giant breeds (like Great Danes, Weimaraners, and Irish Wolfhounds). The rapid bone turnover at the metaphysis becomes disrupted, leading to inflammation and necrosis.",
        "Why_Not": "At 10-12 months, the growth plates are closing, so metaphyseal diseases like HOD are rare. Panosteitis can persist up to 2 years of age.",
        "Wow_Approach": "N/A"
    },
    3345: {
        "topic": "Panosteitis - Radiographic Findings",
        "Core_Anatomy": "Diaphysis (Medullary cavity).",
        "Pathogenesis_Immediate": "Panosteitis is characterized radiographically by a 'Blurring pattern' or increased radiopacity within the medullary cavity of the diaphysis.",
        "Pathogenesis_Deep": "Panosteitis (often called 'growing pains') is an idiopathic inflammation of the bone marrow of the long bones in young large breed dogs (classically German Shepherds). On an X-ray, the normally dark (radiolucent) medullary canal of the diaphysis becomes filled with thumbprint-like, cloudy, white (radiopaque) patches of woven bone. The pain frequently shifts from leg to leg ('shifting leg lameness').",
        "Why_Not": "Widening of the nutrient foramen is also seen in panosteitis, as the inflammatory process causes hyperemia and enlargement of the foramen where the blood vessels enter the bone.",
        "Wow_Approach": "If you squeeze the mid-shaft (diaphysis) of the long bones on physical exam and the dog screams, it is almost certainly panosteitis."
    },
    3346: {
        "topic": "Craniomandibular Osteopathy (CMO) - Scottish Terriers",
        "Core_Anatomy": "Mandible and Tympanic bullae.",
        "Pathogenesis_Immediate": "The classic predisposed breeds for Craniomandibular Osteopathy (CMO) are the Scottish Terrier and West Highland White Terrier (WHWT).",
        "Pathogenesis_Deep": "CMO ('Lion Jaw') is an inherited, non-neoplastic, proliferative bone disease of young terriers (3-8 months). Massive, irregular new bone grows on the mandibles, temporomandibular joint (TMJ), and tympanic bullae. The dog presents with severe pain on opening the mouth, drooling, and an inability to eat. The jaw physically thickens.",
        "Why_Not": "Large breeds get HOD or Panosteitis. CMO is specifically a terrier disease of the skull.",
        "Wow_Approach": "Like HOD, CMO is usually self-limiting and stops progressing once the dog reaches skeletal maturity (1 year of age), at which point the excess bone may partially resorb. However, if the TMJ is completely fused by the bone growth, the dog must be euthanized as it can never eat again."
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
