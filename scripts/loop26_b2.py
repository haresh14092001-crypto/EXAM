import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2953: {
        "topic": "Dehorning Complication - Sinusitis/Empyema",
        "Core_Anatomy": "Cornual diverticulum and Frontal Sinus.",
        "Pathogenesis_Immediate": "The most common surgical complication of dehorning adult cattle is Sinusitis (or Empyema of the frontal sinus).",
        "Pathogenesis_Deep": "As reviewed, because the frontal sinus pneumatizes into the horn core in adults, dehorning leaves a gaping hole directly into the sinus cavity. Environmental contamination (dirt, rain, fly larvae/maggots) enters the hole, causing a severe bacterial infection (Sinusitis). When this infection becomes purulent, it is termed Empyema of the frontal sinus.",
        "Why_Not": "Hemorrhage can be severe, but it is controlled intra-operatively (by pulling the cornual artery). Sinusitis is the most common POST-operative complication.",
        "Wow_Approach": "To treat frontal sinus empyema, the sinus must be trephined (a hole drilled into the bone) at its lowest dependent point on the forehead to allow the pus to drain by gravity, followed by aggressive daily flushing."
    },
    2954: {
        "topic": "Equine Eyeworm - Thelazia lacrymalis",
        "Core_Anatomy": "Conjunctival sac and Lacrimal ducts.",
        "Pathogenesis_Immediate": "The specific eyeworm of horses is Thelazia lacrymalis.",
        "Pathogenesis_Deep": "Thelazia spp. are small nematodes that reside in the conjunctival sac and tear ducts of various animals, transmitted by Face Flies (Musca autumnalis). The equine-specific species is T. lacrymalis. They cause chronic, severe conjunctivitis, excessive lacrimation, and corneal ulceration due to their physical movement across the cornea.",
        "Why_Not": "T. rhodesii and T. gulosa affect cattle. T. californiensis affects dogs/cats. T. lacrymalis is the equine species.",
        "Wow_Approach": "Because they live on the surface of the eye (extracorporeal), systemic dewormers may not reach high enough concentrations in the tears to kill them. They are often treated by directly flushing the eye with a dilute iodine solution (to stun them) followed by manual removal with fine forceps."
    },
    2955: {
        "topic": "Wooden Tongue - Actinobacillosis",
        "Core_Anatomy": "Tongue (muscularis).",
        "Pathogenesis_Immediate": "Thick-walled abscessation of the tongue is associated with Actinobacillosis (Wooden Tongue).",
        "Pathogenesis_Deep": "Actinobacillus lignieresii is a normal commensal bacterium of the bovine mouth. When rough feed (like dry stems) causes penetrating microtrauma to the tongue mucosa, the bacteria enter the deep muscle layers. They cause a massive, chronic, granulomatous, and pyogranulomatous inflammation (thick-walled abscesses). The tongue becomes massively swollen, hard, and immobile ('Wooden Tongue'), preventing the cow from eating.",
        "Why_Not": "Actinomycosis (Actinomyces bovis) causes Lumpy Jaw (granulomatous osteomyelitis of the mandible/bone), NOT the soft tissue of the tongue.",
        "Wow_Approach": "The classic, highly effective treatment for Wooden Tongue is the intravenous administration of Sodium Iodide. The iodine shrinks the granulomas rapidly, allowing the cow to eat again within 48 hours."
    },
    2957: {
        "topic": "Megaoesophagus Complication - Aspiration Pneumonia",
        "Core_Anatomy": "Oesophagus, Trachea, and Lungs.",
        "Pathogenesis_Immediate": "The primary, often fatal, complication of Megaoesophagus is Aspiration Pneumonia.",
        "Pathogenesis_Deep": "Megaoesophagus is a generalized dilation and loss of motility of the oesophagus (due to myasthenia gravis, neuropathies, or idiopathic causes). Because peristalsis is absent, food and water pool in the flaccid oesophagus. The dog chronically regurgitates (passive expulsion, no abdominal heaving). Because this pool of rotting food sits right above the larynx, it frequently spills over into the trachea, causing severe, recurrent aspiration pneumonia.",
        "Why_Not": "Oesophageal achalasia is the failure of the lower esophageal sphincter to relax. Megaoesophagus is the dilation of the entire tube.",
        "Wow_Approach": "Dogs with megaoesophagus must be fed in an upright position (using a Bailey Chair) and remain upright for 15-30 minutes after eating. Gravity is the only mechanism left to pull the food down into their stomach."
    },
    2958: {
        "topic": "True or False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header denoting the True or False section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2968: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching question section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2969: {
        "topic": "Reversal Match - Yohimbine",
        "Core_Anatomy": "Central nervous system (Alpha-2 receptors).",
        "Pathogenesis_Immediate": "Yohimbine is clinically matched with Xylazine.",
        "Pathogenesis_Deep": "Yohimbine is the specific alpha-2 antagonist used to reverse the alpha-2 agonist Xylazine.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2970: {
        "topic": "Prognathism (Underbite)",
        "Core_Anatomy": "Mandible and Maxilla.",
        "Pathogenesis_Immediate": "Prognathism refers to an abnormally elongated mandible (Underbite / Monkey mouth).",
        "Pathogenesis_Deep": "In veterinary dentistry, the standard reference point is the maxilla. Prognathism means the mandible protrudes further forward than the maxilla (underbite). This is a normal breed characteristic in brachycephalic dogs (Bulldogs, Pugs) but is considered a severe genetic fault in horses ('Monkey mouth' or 'Sow mouth'). Brachygnathism means the mandible is too short (overbite or 'Parrot mouth').",
        "Why_Not": "Parrot mouth = Brachygnathism. Monkey mouth = Prognathism.",
        "Wow_Approach": "In horses, severe prognathism prevents the incisors from meeting. Since horses use their incisors to graze short grass, a severely prognathic horse will starve on pasture and must be fed cut hay from a manger."
    },
    2978: {
        "topic": "Subjective Questions Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating subjective definition questions.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    2993: {
        "topic": "Essay Section Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating the essay section.",
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
print(f"Batch 2/5 DONE: Updated {updated} questions.")
