import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3885: {
        "topic": "Greenstick Fracture (Review)",
        "Core_Anatomy": "Young bone.",
        "Pathogenesis_Immediate": "A Greenstick fracture is a classic type of incomplete fracture.",
        "Pathogenesis_Deep": "Reiterating that the cortex bends on one side and breaks on the other due to high organic content in juvenile bone.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3886: {
        "topic": "Compression Fracture (Review)",
        "Core_Anatomy": "Cancellous bone.",
        "Pathogenesis_Immediate": "A Compression fracture occurs when bones are crushed together, common in vertebrae or skull fractures.",
        "Pathogenesis_Deep": "Reiterating that axial loading causes the spongy bone trabeculae to collapse completely.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3887: {
        "topic": "Coxa Magna",
        "Core_Anatomy": "Femoral Head and Neck.",
        "Pathogenesis_Immediate": "Coxa Magna is a skeletal deformity characterized by the abnormal enlargement of the femoral head.",
        "Pathogenesis_Deep": "This hypertrophy occurs secondary to persistent joint inflammation or hyperemia (such as in early Legg-Perthes or hip dysplasia). The increased blood supply stimulates the articular cartilage and growth plate of the femoral head to grow excessively, leading to a poorly fitting femoral head that does not seat deeply inside the acetabulum, worsening joint laxity.",
        "Why_Not": "Coxa vara is a decrease in the femoral neck angle. Coxa valga is an increase. Coxa magna strictly refers to the size of the head.",
        "Wow_Approach": "N/A"
    },
    3895: {
        "topic": "Volvulus Definition",
        "Core_Anatomy": "Gastrointestinal Tract.",
        "Pathogenesis_Immediate": "A Volvulus is the pathological twisting of a loop of intestine (or the stomach) around its mesenteric axis.",
        "Pathogenesis_Deep": "This twisting instantly causes a double occlusion of the intestinal lumen (preventing flow of gas/digesta) and, more catastrophically, occludes the mesenteric veins and arteries. The bowel instantly undergoes venous congestion, rapid wall necrosis, bacterial translocation, and fatal septic/endotoxic shock.",
        "Why_Not": "Torsion is the twisting of an organ on its long axis (like a uterine torsion). Volvulus is specifically a mesenteric twisting.",
        "Wow_Approach": "N/A"
    },
    3907: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3908: {
        "topic": "VSR II Header (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3909: {
        "topic": "Exam Instruction (Duplicate)",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Instruction indicating handing over the paper.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3910: {
        "topic": "Radiology Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating Veterinary Surgery and Radiology Paper II (Radiology).",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3911: {
        "topic": "Fill in the Blanks Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a fill-in-the-blanks section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3921: {
        "topic": "X-Ray Physics - kVp and Penetration",
        "Core_Anatomy": "Diagnostic Imaging.",
        "Pathogenesis_Immediate": "An increase in the kilovoltage peak (kVp) setting in an X-ray machine directly increases the penetration power of the X-ray beam.",
        "Pathogenesis_Deep": "kVp represents the peak potential difference applied between the cathode and anode. Increasing kVp speeds up the electrons traveling to the target, resulting in X-ray photons with shorter wavelengths and higher energy. These high-energy photons are much more capable of penetrating thick, dense tissues (like bone) to reach the film, reducing overall radiographic contrast but increasing gray scale.",
        "Why_Not": "mA (milliampere) controls the quantity of X-ray photons (density/blackness), not their energy/penetration power.",
        "Wow_Approach": "For very thick structures (like a horse's stifle), you must crank up the kVp to physically force the photons through the massive tissue mass; otherwise, the film will be completely white (underexposed)."
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
print(f"Batch 4/5 DONE: Updated {updated} questions.")
