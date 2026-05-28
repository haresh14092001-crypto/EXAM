import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3513: {
        "topic": "Cryotherapy - Acute Phase (Review)",
        "Core_Anatomy": "Peripheral vasculature.",
        "Pathogenesis_Immediate": "The treatment of choice within the first 24-48 hours of an acute musculoskeletal injury is Cold therapy (Cryotherapy).",
        "Pathogenesis_Deep": "Reiterating that ice causes intense vasoconstriction, which is the only way to stop the active hemorrhage and massive edema that characterize the acute inflammatory phase.",
        "Why_Not": "Heat (Thermotherapy) during the first 48 hours is strictly contraindicated as it will massively increase bleeding and swelling.",
        "Wow_Approach": "N/A"
    },
    3514: {
        "topic": "Longwave Infrared Energy",
        "Core_Anatomy": "Skin (Epidermis).",
        "Pathogenesis_Immediate": "The wavelength of Longwave Infrared radiation is approximately 1500 to 12000 mμ (nanometers).",
        "Pathogenesis_Deep": "Unlike shortwave infrared (which penetrates deep into muscles), longwave infrared radiation is completely absorbed by the superficial layers of the skin (epidermis). It provides intense surface heating but has very poor deep tissue penetration.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3515: {
        "topic": "Therapeutic Shoeing - Navicular Syndrome",
        "Core_Anatomy": "Equine Hoof (Navicular bone and DDFT).",
        "Pathogenesis_Immediate": "The ideal therapeutic shoeing method for Navicular Syndrome typically involves an Egg Bar Shoe or an elevated heel bar shoe.",
        "Pathogenesis_Deep": "Navicular syndrome involves chronic degeneration of the navicular bone and inflammation of the deep digital flexor tendon (DDFT) where it rubs over the bone. The fundamental goal of shoeing is to reduce the tension on the DDFT. By elevating the heels (by 2-4 degrees) and providing a solid bar across the back of the shoe (egg bar or straight bar) to prevent the heel from sinking into the dirt, the mechanical pressure on the navicular bursa is significantly relieved.",
        "Why_Not": "A flat shoe with low heels maximizes tension on the DDFT, exacerbating the pain.",
        "Wow_Approach": "Therapeutic shoeing cannot cure navicular disease, but it can manage the biomechanics well enough to keep the horse comfortable and riding for years."
    },
    3516: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the start of a matching section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3517: {
        "topic": "Kumri (Cerebrospinal Nematodiasis)",
        "Core_Anatomy": "Equine Central Nervous System.",
        "Pathogenesis_Immediate": "Kumri is the traditional term for Cerebrospinal Nematodiasis in horses.",
        "Pathogenesis_Deep": "It is caused by the aberrant migration of Setaria digitata (a filarial nematode of cattle, transmitted by mosquitoes) through the brain and spinal cord of the horse. The migrating worms cause focal malacia (necrosis) in the cervical and thoracic spinal cord, resulting in severe, asymmetrical ataxia, weakness, and eventually paralysis of the hindlimbs.",
        "Why_Not": "N/A",
        "Wow_Approach": "Because the damage is physical (the worm chewing through the spinal cord), anthelmintic treatment to kill the worm stops the progression, but cannot reverse the neurological deficits already inflicted."
    },
    3518: {
        "topic": "Canine Wobbler Syndrome",
        "Core_Anatomy": "Cervical Spine (C5-C7).",
        "Pathogenesis_Immediate": "Canine Wobbler Syndrome is formally known as Cervical Spondylomyelopathy (CSM).",
        "Pathogenesis_Deep": "CSM is a devastating disease of the caudal cervical spine, classically affecting Doberman Pinschers and Great Danes. It involves a combination of vertebral malformation, ligamentous hypertrophy, and intervertebral disc protrusion that severely compresses the cervical spinal cord. The dog presents with a highly characteristic 'wobbly' (ataxic) gait in the hindlimbs, and a short, choppy, stiff gait in the forelimbs (the 'two-engine' gait).",
        "Why_Not": "N/A",
        "Wow_Approach": "Surgical treatment usually requires a ventral slot decompression followed by massive titanium plates and screws to distract and fuse the unstable cervical vertebrae."
    },
    3547: {
        "topic": "VSR III Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting Veterinary Surgery and Radiology Paper III.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3550: {
        "topic": "Orthopaedics Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the Orthopaedics section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3551: {
        "topic": "Fill in the Blanks Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3557: {
        "topic": "Ulcerative Sole - Rusterholz Ulcer (Review)",
        "Core_Anatomy": "Bovine Hoof.",
        "Pathogenesis_Immediate": "An ulcerative sole is commonly noticed in Dairy Cattle (Rusterholz ulcer).",
        "Pathogenesis_Deep": "Reiterating the focal necrosis at the sole-bulb junction of the lateral hind claw.",
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
