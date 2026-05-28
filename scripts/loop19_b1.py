import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2161: {
        "topic": "VPM 412 - Bacterial/Fungal/Rickettsial Diseases Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This header marks the objective section of VPM 412, covering the prevention, control, and epidemiology of bacterial, fungal, and rickettsial diseases.",
        "Pathogenesis_Deep": "Questions here test the core principles of disease control: identification of specific causative agents, definitive diagnostic tests, and targeted interventions (vaccines, drugs, vector control).",
        "Why_Not": "Treatment of individual animals belongs to clinical medicine; VPM focuses on herd-level eradication strategies.",
        "Wow_Approach": "Group diseases by transmission route (zoonotic, vector-borne, contact) to rapidly predict control measures."
    },
    2162: {
        "topic": "Anthrax Control - Sporicidal Agent",
        "Core_Anatomy": "Environmental spore control.",
        "Pathogenesis_Immediate": "The sporicidal agent used for environmental decontamination and control of Anthrax is 10% Formalin (formaldehyde solution).",
        "Pathogenesis_Deep": "Bacillus anthracis spores are extremely resistant environmental structures that can survive in alkaline soils for decades. Standard disinfectants (quaternary ammonium compounds, bleach at normal dilutions) are completely ineffective. High-concentration formaldehyde (10% formalin) works by alkylating all free amino and thiol groups in the spore's proteins and nucleic acids, permanently denaturing them. The area where an anthrax carcass lay must be drenched with 10% formalin after deep burial or incineration.",
        "Why_Not": "Phenolic disinfectants and alcohol are insufficient to penetrate the spore coat. Only formalin, hot steam sterilization, or peracetic acid achieve reliable sporicidal activity.",
        "Wow_Approach": "Because anthrax spores can re-emerge after decades when soil is disturbed by floods or excavation, historical anthrax fields ('cursed fields') must be permanently marked and never used for agriculture."
    },
    2171: {
        "topic": "Bovine Summer Mastitis - Causative Agent",
        "Core_Anatomy": "Mammary gland (non-lactating dry cows and heifers).",
        "Pathogenesis_Immediate": "Summer mastitis is primarily caused by Arcanobacterium pyogenes (previously Trueperella pyogenes).",
        "Pathogenesis_Deep": "Summer mastitis is a severe, gangrenous form of mastitis that uniquely affects non-lactating dry cows and heifers during summer months (hence the name). The primary vector is the biting fly Hydrotaea irritans. The fly carries A. pyogenes (often in combination with Peptostreptococcus indolicus and Fusobacterium necrophorum) from affected udders to susceptible dry cows, depositing the bacteria in the teat canal. The result is acute, rapidly progressing, foul-smelling, gangrenous mastitis that often results in permanent loss of the quarter and frequently causes abortion.",
        "Why_Not": "Staphylococcus aureus and E. coli cause common lactating cow mastitis but are not specifically linked to summer fly transmission in dry/heifer animals.",
        "Wow_Approach": "Prevention is entirely fly control during the dry period: apply residual insecticide teat dips and fly repellent strips, and house dry cows away from fly-infested areas in summer."
    },
    2172: {
        "topic": "Summer Mastitis - MCQ Answer",
        "Core_Anatomy": "Mammary gland and teat canal.",
        "Pathogenesis_Immediate": "Arcanobacterium pyogenes is the correct answer for the causative organism of Summer Mastitis.",
        "Pathogenesis_Deep": "A. pyogenes produces leucotoxin (exotoxin that destroys neutrophils) and proteases that rapidly destroy mammary tissue. The exudate is characteristically thick, cream-white to pinkish, and has a distinctive fetid odor unlike other forms of mastitis.",
        "Why_Not": "S. aureus causes contagious, chronic mastitis in lactating cows (not seasonal/fly-borne). E. coli causes acute environmental mastitis.",
        "Wow_Approach": "The udder secretion in summer mastitis has a characteristic 'rotten apple' or 'fishy' odor due to concurrent Fusobacterium and Peptostreptococcus involvement—a strong diagnostic clue."
    },
    2173: {
        "topic": "Vertical Transmission - Pullorum Disease",
        "Core_Anatomy": "Ovary (transovarial transmission).",
        "Pathogenesis_Immediate": "Pullorum Disease (caused by Salmonella Pullorum) is the classic example of a vertically transmitted disease in poultry.",
        "Pathogenesis_Deep": "Salmonella Pullorum can colonize the ovary of an infected hen. When the developing yolk is formed, the bacteria are incorporated directly into the yolk before the egg shell is laid. The chick that hatches from such an infected egg is thus born already systemically infected, without any horizontal (environmental) exposure. This transovarial transmission causes explosive Bacillary White Diarrhea mortality in newborn chicks.",
        "Why_Not": "Fowl Typhoid and Avian Mycoplasmosis can also be transmitted vertically but Pullorum disease is the textbook example of strict transovarial (vertical) transmission.",
        "Wow_Approach": "The Rapid Plate Agglutination (RPA) test (whole-blood agglutination on a glass plate) is the primary flock screening tool; all RPA-positive breeders must be culled immediately to prevent vertical transmission."
    },
    2174: {
        "topic": "Cervical Mucus Agglutination Test - Brucellosis",
        "Core_Anatomy": "Cervical mucus IgA antibodies.",
        "Pathogenesis_Immediate": "The Cervical Mucus Agglutination Test (CMAT) is used for the diagnosis of Brucellosis, Campylobacteriosis, and Listeriosis (all of the above).",
        "Pathogenesis_Deep": "The cervical mucus of cattle in the post-abortion or post-calving period contains elevated levels of locally produced antibodies (IgA, IgG) against reproductive pathogens. The CMAT detects these antibodies by mixing cervical mucus with a colored bacterial antigen; if specific antibodies are present, visible agglutination (clumping) occurs. It is particularly useful for detecting reproductive pathogens like Brucella, Campylobacter fetus (causing early embryonic death), and Listeria.",
        "Why_Not": "Pullorum disease is a poultry disease, not a bovine reproductive pathogen requiring the CMAT.",
        "Wow_Approach": "The CMAT is ideally collected from the cervical mucus pool that forms in the posterior vagina 0-3 days post-calving or post-abortion, when local antibody concentrations are highest."
    },
    2175: {
        "topic": "Tetanus - Most Susceptible Species",
        "Core_Anatomy": "Inhibitory interneurons (Renshaw cells) of the spinal cord.",
        "Pathogenesis_Immediate": "Among domestic animals, the Horse is by far the most susceptible species to tetanus.",
        "Pathogenesis_Deep": "Clostridium tetani produces tetanospasmin, which travels retrogradely along motor nerves to block glycine and GABA release from inhibitory interneurons in the spinal cord and brainstem. Because horses have a very high density of these inhibitory interneurons controlling their extensive musculature, even small amounts of toxin cause severe, generalized rigidity. Additionally, equine wounds (especially deep hoof punctures from nails) provide the ideal anaerobic microenvironment for C. tetani germination.",
        "Why_Not": "Dogs and cats are extremely resistant to tetanus, rarely developing clinical disease even after contaminated wounds. Sheep and goats have intermediate susceptibility.",
        "Wow_Approach": "The susceptibility order is: Horse > Sheep/Goat > Cattle > Pig > Dog > Cat > Chicken. The classic horse tetanus presentation is the 'sawhorse' stance: rigid extended limbs, elevated tail, erect ears, and hypersensitivity to light/sound (Risus sardonicus)."
    },
    2176: {
        "topic": "Bovine Actinomycosis - Lumpy Jaw",
        "Core_Anatomy": "Mandible and maxillary bone (periosteum).",
        "Pathogenesis_Immediate": "Osteomyelitis of the jaw bone (Lumpy Jaw) in cattle is caused by Actinomyces bovis.",
        "Pathogenesis_Deep": "Actinomyces bovis is a Gram-positive, filamentous, anaerobic bacterium that is a normal commensal of the bovine oral cavity. When the bone periosteum is breached by a sharp piece of feed (wire, thorns, or rough forage) at the time of tooth eruption, A. bovis invades the bone. It triggers a chronic, proliferative, pyogranulomatous osteomyelitis that causes massive, bony swelling of the mandible or maxilla (Lumpy Jaw). The draining sinuses discharge the characteristic sulfur granules.",
        "Why_Not": "Actinobacillus lignieresii causes SOFT TISSUE granulomas (Wooden Tongue of the tongue/lymph nodes) and does not invade bone. Pasteurella causes septicemia/pneumonia.",
        "Wow_Approach": "The anatomical rule: 'A for Actinomyces = A for Alveolar bone' and 'B for soft Body tissue = Actinobacillus.' This single distinction resolves most Lumpy Jaw vs Wooden Tongue exam questions."
    },
    2177: {
        "topic": "Leptospirosis Diagnosis - MAT (VPM Repeated)",
        "Core_Anatomy": "Systemic serology (serovar-specific antibodies).",
        "Pathogenesis_Immediate": "The Microscopic Agglutination Test (MAT) is the gold standard test used specifically for the diagnosis of Leptospirosis.",
        "Pathogenesis_Deep": "The MAT is the only test capable of identifying the specific Leptospira serovar infecting an animal. Patient serum is serially diluted and mixed with live, motile cultures of different Leptospira serovars. Serovar-specific antibodies cause the live spirochetes to clump (agglutinate), visible as immobile aggregates under dark-field microscopy. A four-fold rise in titer between paired samples confirms active infection.",
        "Why_Not": "Salmonellosis is diagnosed via culture and biochemical tests. Brucellosis uses the RBPT/STAT. Only MAT provides serovar-level Leptospira identification.",
        "Wow_Approach": "Because MAT requires maintaining libraries of live, infectious Leptospira serovars, it is restricted to Leptospira Reference Laboratories. Clinicians send serum; they do not perform the test in-house."
    },
    2178: {
        "topic": "Psittacosis Transmission - Chlamydia psittaci",
        "Core_Anatomy": "Avian respiratory epithelium and macrophages.",
        "Pathogenesis_Immediate": "Chlamydiosis (Psittacosis/Ornithosis) in birds is transmitted through BOTH inhalation of dust from dried feces/secretions AND ingestion of contaminated food/water.",
        "Pathogenesis_Deep": "Chlamydia psittaci can survive for weeks in dried fecal droppings. Infectious elementary bodies aerosolize when contaminated feces dry out and create dust. This dust, when inhaled by susceptible birds or humans, results in respiratory infection. The organism can also be shed in nasal/ocular secretions and transmitted via ingestion (eating contaminated feed near infected feces). Transmission routes: (a) Inhalation + (b) Ingestion = Both are correct.",
        "Why_Not": "Direct contact without the intermediate of inhalation or ingestion is not a primary route; the tiny elementary body requires mucosal entry.",
        "Wow_Approach": "In an aviary or poultry facility, the highest risk of human infection is during cage cleaning when dried feces are disturbed and aerosolized—always wear N95 respirator and wet-mop rather than dry-sweep."
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
