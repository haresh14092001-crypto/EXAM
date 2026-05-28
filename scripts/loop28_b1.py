import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3199: {
        "topic": "Brachygnathism (Parrot Mouth)",
        "Core_Anatomy": "Maxilla and Mandible.",
        "Pathogenesis_Immediate": "The condition where the upper jaw (maxilla) is longer than the lower jaw (mandible) is called Parrot Mouth (Brachygnathism).",
        "Pathogenesis_Deep": "This is a severe congenital defect (Brachygnathia inferior) where the mandible fails to grow to its normal length. The incisors do not meet, resembling the curved beak of a parrot. In grazing animals (horses, sheep), this severely impairs their ability to prehend short grass, leading to malnutrition on pasture. They must be fed from elevated mangers.",
        "Why_Not": "Pig mouth/Monkey mouth is Prognathism (mandible is longer than maxilla).",
        "Wow_Approach": "N/A"
    },
    3200: {
        "topic": "Bier's Hyperemia Therapy",
        "Core_Anatomy": "Peripheral vasculature.",
        "Pathogenesis_Immediate": "Bier's hyperemia (active/passive congestion) therapy is classically indicated for Chronic inflammatory lesions.",
        "Pathogenesis_Deep": "Historically, August Bier introduced the concept of artificially inducing hyperemia (increased blood flow) to treat chronic, indolent, non-healing infections (like chronic joint ill or chronic abscesses). The theory was that by placing a tourniquet proximal to the lesion to restrict venous return (passive hyperemia), or by applying heat/counter-irritants (active hyperemia), the area would flood with leukocytes and fresh antibodies to finally clear the chronic infection.",
        "Why_Not": "Applying hyperemia to an ACUTE, hot, painful inflammatory lesion would massively exacerbate the pain and swelling, potentially causing tissue necrosis.",
        "Wow_Approach": "While largely obsolete in modern antibiotic-driven medicine, the principle survives in the use of hot fomentation (warm compresses) to 'point' a chronic abscess."
    },
    3201: {
        "topic": "Suture Holding Capacity - Fat",
        "Core_Anatomy": "Subcutaneous adipose tissue.",
        "Pathogenesis_Immediate": "The tissue with the least suture holding capacity is Fat.",
        "Pathogenesis_Deep": "Adipose tissue consists of large, fragile cells filled with lipids, with virtually no collagen or fibrous stroma. When a suture is tied tightly in fat, the suture instantly cuts straight through the lipid cells like a wire through butter. Therefore, fat provides ZERO holding strength for wound closure.",
        "Why_Not": "Fascia (like the linea alba) is dense collagen and has the HIGHEST suture holding capacity in the abdomen. Tendons and muscles also hold sutures much better than fat.",
        "Wow_Approach": "When closing the subcutaneous layer of a surgical incision, the surgeon must aim to catch the deep dermal fascia or the thin fascial planes between the fat lobes, rather than the fat itself, to eliminate dead space."
    },
    3202: {
        "topic": "Crush Syndrome",
        "Core_Anatomy": "Skeletal muscle and Kidneys.",
        "Pathogenesis_Immediate": "The pathological symptom resulting from extensive crush injuries is termed Crush Syndrome.",
        "Pathogenesis_Deep": "When large muscle masses are subjected to prolonged, severe crushing trauma (e.g., an animal trapped under a collapsed building or a downer cow lying on its own legs for days), massive muscle necrosis occurs (Rhabdomyolysis). Upon release of the pressure, the dead muscle cells release massive amounts of Myoglobin and Potassium into the bloodstream. The myoglobin physically plugs the renal tubules, causing acute, fatal kidney failure (Myoglobinuric Nephrosis), while the hyperkalemia causes cardiac arrest.",
        "Why_Not": "Gangrene is tissue death with putrefaction. Necrosis is simple cell death. Crush syndrome specifically involves the systemic, often fatal, toxemia and renal failure secondary to massive muscle crushing.",
        "Wow_Approach": "Patients with severe crush injuries must receive massive volumes of IV fluids (to flush the kidneys) BEFORE the crushing weight is removed."
    },
    3203: {
        "topic": "Burn Prognosis - Body Surface Area",
        "Core_Anatomy": "Skin (Epidermis/Dermis) and systemic vasculature.",
        "Pathogenesis_Immediate": "The prognosis is highly unfavorable if more than 50% of the body surface area is involved in severe burns.",
        "Pathogenesis_Deep": "Skin acts as a vital barrier against fluid loss and infection. When >50% of the body surface undergoes 2nd or 3rd-degree burns, the massive loss of plasma through the weeping burn wounds causes profound, refractory hypovolemic shock. Additionally, the complete loss of the protective epidermal barrier almost inevitably leads to fatal Pseudomonas or Staphylococcal sepsis.",
        "Why_Not": "Burns of 10-20% are painful but manageable with aggressive fluid resuscitation and wound care.",
        "Wow_Approach": "In animals, calculating the exact percentage of burned skin is difficult due to hair coats. The 'Rule of Nines' used in human medicine is adapted for dogs: each foreleg is 9%, each hindleg is 18%, thorax is 18%, abdomen is 18%, head is 9%."
    },
    3204: {
        "topic": "Focal Film Distance (FFD) - 100 cm",
        "Core_Anatomy": "Radiographic physics.",
        "Pathogenesis_Immediate": "The standard Focal Film Distance (FFD), also known as Source to Image Distance (SID), in veterinary radiography is 100 cm (or 40 inches).",
        "Pathogenesis_Deep": "The FFD is the distance from the X-ray tube's focal spot to the X-ray film/detector. Maintaining a standard distance is critical because X-ray intensity follows the Inverse Square Law. If you move the tube twice as far away, the intensity drops by a factor of FOUR. Standardizing to 100 cm ensures that exposure charts remain accurate and consistent across different machines.",
        "Why_Not": "Changing the FFD to 50 cm would require drastically reducing the mAs to prevent completely blackening (overexposing) the film.",
        "Wow_Approach": "N/A"
    },
    3205: {
        "topic": "Anode Heel Effect (Review)",
        "Core_Anatomy": "X-ray tube physics.",
        "Pathogenesis_Immediate": "The Heel Effect is specifically associated with the Anode of the X-ray tube.",
        "Pathogenesis_Deep": "As discussed, because the X-rays are produced deep inside the angled tungsten target of the anode, the anode material itself absorbs some of the rays. This makes the beam significantly weaker on the anode side and stronger on the cathode side.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3206: {
        "topic": "Radiographic Contrast - Long Scale",
        "Core_Anatomy": "Radiographic interpretation.",
        "Pathogenesis_Immediate": "A good quality radiograph of soft tissue (like the abdomen) will have a Long scale of contrast.",
        "Pathogenesis_Deep": "Contrast refers to the number of visible shades of gray. A 'Short Scale' (high contrast) image is mostly black and white with very few grays—ideal for looking at bones (fractures). A 'Long Scale' (low contrast) image has many, many subtle shades of gray. Because the organs in the abdomen (liver, spleen, kidneys, intestines) all have very similar physical densities, you MUST use a long scale of contrast to differentiate their borders.",
        "Why_Not": "If you shoot an abdomen with short scale contrast, the entire image will be a solid, undifferentiated gray/white blob.",
        "Wow_Approach": "To get a Long scale of contrast, you must use a HIGH kVp (high energy to penetrate the tissues evenly) and a relatively low mAs."
    },
    3207: {
        "topic": "X-Ray Tube Cathode - Tungsten Filament",
        "Core_Anatomy": "X-ray tube physics.",
        "Pathogenesis_Immediate": "The filament of the Cathode in an X-ray tube is made up of Tungsten.",
        "Pathogenesis_Deep": "The cathode contains a coiled wire filament. When an electrical current is applied, the filament heats up to extreme temperatures, 'boiling off' a cloud of electrons (Thermionic Emission). Tungsten is used because it has an exceptionally high melting point (3,370°C), allowing it to survive the massive heat generated without melting.",
        "Why_Not": "Copper melts at ~1000°C; it would instantly vaporize if used as the filament.",
        "Wow_Approach": "The anode target is ALSO made of Tungsten, for the exact same reason: to withstand the massive heat generated when those high-speed electrons crash into it."
    },
    3208: {
        "topic": "Motion Unsharpness",
        "Core_Anatomy": "Radiographic technique.",
        "Pathogenesis_Immediate": "Movement of the animal during a radiographic exposure causes Motion Unsharpness.",
        "Pathogenesis_Deep": "If the patient breathes, pants, or struggles while the X-rays are exposing the film, the borders of the organs will be blurred (Motion Unsharpness or blurring). This ruins the diagnostic quality of the image.",
        "Why_Not": "Penumbra is the natural geometric blurring at the edges of an image caused by the focal spot size, unrelated to patient movement.",
        "Wow_Approach": "To prevent motion unsharpness in panting dogs, the radiographer must use the highest mA station available on the machine to allow for the shortest possible exposure time (e.g., 1/120th of a second), 'freezing' the motion."
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
print(f"Batch 1/5 DONE: Updated {updated} questions.")
