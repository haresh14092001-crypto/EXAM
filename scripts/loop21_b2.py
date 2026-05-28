import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2426: {
        "topic": "Antitetanus Serum & CBPP - Matching",
        "Core_Anatomy": "Neuromuscular junction (Tetanus); Pulmonary pleura (CBPP).",
        "Pathogenesis_Immediate": "Antitetanus serum provides passive immunity against Clostridium tetani toxin. Contagious Bovine Pleuropneumonia (CBPP) is caused by Mycoplasma mycoides subsp. mycoides Small Colony (MmmSC).",
        "Pathogenesis_Deep": "CBPP is an OIE-listed disease causing severe fibrinous pneumonia and pleuropneumonia in cattle with up to 50% mortality. It is eradicated from Europe but remains endemic in Sub-Saharan Africa. In the match context: Histoplasma farciminosum causes Epizootic Lymphangitis in horses—a chronic ulcerative lymphangitis resembling Glanders but caused by this dimorphic fungus.",
        "Why_Not": "Histoplasma farciminosum is often confused with Glanders (B. mallei) because both cause chronic ulcerative lymphangitis in horses. Key difference: H. farciminosum is a fungus treated with Sodium Iodide; Glanders requires immediate euthanasia.",
        "Wow_Approach": "Epizootic Lymphangitis (H. farciminosum) was a major military horse disease in WWI, responsible for massive losses in cavalry and transport horses in North Africa and the Middle East."
    },
    2431: {
        "topic": "Sterne Vaccine - Anthrax",
        "Core_Anatomy": "Systemic humoral immunity (anti-protective antigen antibodies).",
        "Pathogenesis_Immediate": "The Sterne vaccine is the live, attenuated, non-encapsulated spore vaccine used for immunization against Anthrax.",
        "Pathogenesis_Deep": "The Sterne strain (34F2) of Bacillus anthracis is an avirulent, non-encapsulated strain that retains its toxin-producing capability. When injected subcutaneously, the Sterne spores germinate and produce Protective Antigen (PA), Lethal Factor (LF), and Edema Factor (EF) in non-lethal amounts. The host immune system mounts a strong antibody response specifically against the Protective Antigen component. These anti-PA antibodies then neutralize future virulent toxin before it can bind to host cell receptors.",
        "Why_Not": "The Sterne vaccine is a living spore vaccine and MUST NOT be given with antibiotics—if penicillin is administered simultaneously (which was a common historical mistake), it kills the spore before the immune response is triggered.",
        "Wow_Approach": "Because the Sterne vaccine is a live spore vaccine, vaccinated animals may occasionally shed spores in the environment. Vaccination must be completed at least 3 weeks before slaughter to prevent residual live spores in carcass tissues."
    },
    2432: {
        "topic": "VPM 422 - Viral and Parasitic Diseases Fill in the Blanks Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This section (VPM 422) covers viral and parasitic disease prevention and control with fill-in-the-blank questions.",
        "Pathogenesis_Deep": "High-yield blanks in VPM 422: FMD inactivant = BEI; AHS reservoir = Zebra; Rabies diagnosis lab animal = Mouse; Trichinoscopy = Trichinella; Stormont test = TB.",
        "Why_Not": "Exact terms are required; generic answers are not accepted.",
        "Wow_Approach": "Cross-reference the specific diagnostic test with its specific disease and you will never miss a VPM fill-in-blank: Coggins (AGID) = EIA; MAT = Leptospirosis; DFAT = Rabies; Casoni = Hydatid."
    },
    2443: {
        "topic": "VPM 422 True/False Section Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine - Viral and Parasitic diseases.",
        "Pathogenesis_Immediate": "This True/False section evaluates absolute factual accuracy regarding viral and parasitic disease epidemiology.",
        "Pathogenesis_Deep": "Common True/False traps in VPM 422: 'BVD PI calves shed virus lifelong' (TRUE), 'AHS affects zebras severely' (FALSE—zebras are resistant reservoirs), 'Neospora causes late-term abortion' (TRUE—3-9 months).",
        "Why_Not": "Every word in the statement must be evaluated; a single incorrect detail makes the entire statement FALSE.",
        "Wow_Approach": "For all True/False questions on vaccines: check if it's a LIVE or KILLED vaccine, if it requires BOOSTER, and if it covers all relevant SEROTYPES."
    },
    2454: {
        "topic": "VPM Match the Following Header - Parasitic Diseases",
        "Core_Anatomy": "Systemic parasitology and preventive medicine.",
        "Pathogenesis_Immediate": "This match section pairs parasitic diseases with their diagnostic tests, control methods, or associated phenomena.",
        "Pathogenesis_Deep": "High-yield pairings: Nasal schistosomiasis → Indoplanorbis snail control; Stilbamide test → fungal diagnosis; Haemonchus contortus → self-cure phenomenon; snail control → copper sulphate.",
        "Why_Not": "Each pairing must be precisely matched; parasitology match questions are frequently tested with subtle distinctions between diseases.",
        "Wow_Approach": "The 'self-cure phenomenon' in Haemonchus contortus is one of immunology's most elegant examples: a sheep that mounts a strong IgE-mediated hypersensitivity reaction can expel thousands of adult worms within 48 hours during a reinfection challenge."
    },
    2455: {
        "topic": "Nasal Schistosomiasis - Copper Sulphate",
        "Core_Anatomy": "Freshwater snail intermediate host (Indoplanorbis exustus).",
        "Pathogenesis_Immediate": "Nasal Schistosomiasis control is matched to Copper Sulphate as the molluscicide used to kill the snail intermediate host.",
        "Pathogenesis_Deep": "The lifecycle of Schistosoma nasale requires the freshwater snail Indoplanorbis exustus as its obligate intermediate host. Cercariae shed from infected snails penetrate the skin or nasal mucosa of cattle, buffaloes, and horses during wading or drinking. Controlling Schistosomiasis in endemic areas involves: (1) Molluscicidal treatment of water bodies with copper sulphate (CuSO4) at 5-10 ppm to kill snails, (2) Treating infected animals with Sodium Antimony Tartrate or Praziquantel.",
        "Why_Not": "Copper sulphate specifically kills mollusks (snails); it does not kill the worms themselves. Stilbamide is a diagnostic test for Epizootic Lymphangitis (H. farciminosum).",
        "Wow_Approach": "Copper sulphate mollusciciding must be applied carefully—excessive concentration kills all aquatic life (fish, beneficial insects). Niclosamide (Bayluscide) is a more selective modern molluscicide that kills snails without devastating the broader aquatic ecosystem."
    },
    2456: {
        "topic": "Haemonchus contortus - Self-Cure Phenomenon",
        "Core_Anatomy": "Abomasal mucosa and IgE-mediated immunity.",
        "Pathogenesis_Immediate": "The 'Self-cure phenomenon' is a classic immunological response matched specifically to Haemonchus contortus infection in sheep.",
        "Pathogenesis_Deep": "In previously exposed, partially immune sheep, a sudden massive reinfection with Haemonchus contortus larvae triggers a dramatic IgE-mediated hypersensitivity response in the abomasal mucosa. The local mast cell degranulation releases massive amounts of histamine, serotonin, and proteases, creating a profoundly hostile environment in the abomasum. Within 24-48 hours, the sheep expels the entire existing adult worm burden (self-cure) while simultaneously resisting establishment of the incoming new larvae.",
        "Why_Not": "Self-cure does NOT occur in naive lambs (no prior sensitization). It requires prior exposure to build the IgE memory response. Trichostrongylus and Ostertagia do not trigger the same dramatic self-cure response.",
        "Wow_Approach": "Research into the self-cure phenomenon led directly to the development of the Barbervax vaccine (a recombinant H. contortus vaccine using gut membrane antigens H-gal-GP and APR-6), which mimics immune attack on the worm's gut lining."
    },
    2457: {
        "topic": "Verminous Bronchitis - Dictyocaulus",
        "Core_Anatomy": "Bronchi and bronchioles.",
        "Pathogenesis_Immediate": "Verminous Bronchitis (Husk/Hoose) in cattle is caused by Dictyocaulus viviparus, matched to snail control as a contextual pairing in this question.",
        "Pathogenesis_Deep": "Dictyocaulus viviparus is the bovine lungworm. L3 larvae are ingested from pasture, penetrate the intestinal wall, travel to mesenteric lymph nodes, enter lymphatics, pass through the thoracic duct into the venous blood, reach the lungs via the pulmonary artery, and break out of the capillaries into the alveoli. They crawl up to the bronchi, where adult worms cause massive mucus production, bronchitis, and bronchospasm. Severely affected calves develop 'hoose'—a harsh, dry cough with expiratory dyspnea.",
        "Why_Not": "Snail control is for liver flukes/Schistosoma. Dictyocaulus does not require a snail intermediate host—the larvae develop directly on pasture to L3 using fungal spores (Pilobolus) for dispersal.",
        "Wow_Approach": "A brilliant epidemiological adaption: Dictyocaulus L3 larvae actually hitch a ride on the sporangiophores of the coprophilous fungus Pilobolus crystallinus growing in cattle dung, which launches them up to 3 meters away from the dung pad—actively dispersing them onto fresh pasture grass."
    },
    2475: {
        "topic": "Veterinary Surgery and Radiology Module Header",
        "Core_Anatomy": "Systemic surgical anatomy and diagnostic imaging.",
        "Pathogenesis_Immediate": "This header marks the beginning of the Veterinary Surgery and Radiology (VSR) module, covering general surgery, anaesthesiology, and diagnostic imaging.",
        "Pathogenesis_Deep": "VSR covers: pre-operative assessment, anaesthesia protocols (local, regional, general), wound management, radiographic technique, and contrast studies.",
        "Why_Not": "Surgical pharmacology (drug doses) must be distinguished from medical pharmacology; the route of administration and monitoring requirements differ significantly for surgical patients.",
        "Wow_Approach": "The 'Rule of Fives' for anaesthetic monitoring: check every 5 minutes for pulse rate, respiratory rate, mucous membrane color, capillary refill time, and pupil size."
    },
    2477: {
        "topic": "VSR 411 - General Surgery, Anaesthesiology & Diagnostic Imaging Header",
        "Core_Anatomy": "Systemic surgical anatomy and radiology.",
        "Pathogenesis_Immediate": "This header introduces the objective section of VSR 411 covering general surgery principles, anaesthesia, and radiological techniques.",
        "Pathogenesis_Deep": "Key surgical areas: wound classification (clean/contaminated/dirty), healing mechanisms (primary/secondary/tertiary intention), aseptic technique, contrast radiography, and anaesthetic drug pharmacology.",
        "Why_Not": "Surgical decision-making requires integrating anatomy, pathology, and pharmacology simultaneously.",
        "Wow_Approach": "The most important principle in surgery: 'Do not add insult to injury.' Every surgical incision is a controlled wound—respect tissues, minimize trauma, maintain asepsis."
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
