import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2305: {
        "topic": "Toxoplasmosis - Contagious Disease (True/False)",
        "Core_Anatomy": "Tissue cysts (bradyzoites) and systemic immune system.",
        "Pathogenesis_Immediate": "The statement 'Toxoplasmosis is a contagious disease of sheep and goats' is FALSE.",
        "Pathogenesis_Deep": "Toxoplasma gondii is NOT a contagious disease transmitted directly between sheep or goats. Sheep and goats are INTERMEDIATE hosts; they acquire infection by ingesting oocysts shed by the definitive host (domestic cat) from contaminated pasture, water, or feed. Infected sheep cannot directly transmit the parasite to other sheep via contact. Abortion in sheep occurs when a naive ewe ingests oocysts during pregnancy, and the parasite undergoes sexual reproduction in the placenta and fetal brain.",
        "Why_Not": "The disease is correctly classified as a zoonosis (humans can be infected) and an indirect transmission disease, but NOT a directly contagious disease between ruminants.",
        "Wow_Approach": "The most common route of human T. gondii infection is NOT from infected sheep but from: (1) ingesting undercooked meat containing tissue cysts, and (2) cleaning a cat's litter tray without gloves."
    },
    2306: {
        "topic": "Infectious Bronchitis - Disinfectant",
        "Core_Anatomy": "Avian respiratory epithelium.",
        "Pathogenesis_Immediate": "Infectious Bronchitis Virus (IBV, a Coronavirus) is effectively inactivated by Sodium Hypochlorite (bleach).",
        "Pathogenesis_Deep": "IBV is an enveloped virus (has a lipid membrane). Enveloped viruses are the most susceptible to disinfectants because detergents and oxidizing agents (like sodium hypochlorite) destroy the lipid envelope, exposing the nucleocapsid and inactivating the virus rapidly. A 0.5-1% sodium hypochlorite solution (diluted bleach) effectively decontaminates poultry houses, equipment, and vehicles during an IBV outbreak.",
        "Why_Not": "Phenolic compounds are more appropriate for non-enveloped viruses and bacteria with waxy cell walls. IBV, as an enveloped coronavirus, is far more susceptible to bleach.",
        "Wow_Approach": "During COVID-19, the same principle applied: SARS-CoV-2 (another coronavirus) was inactivated by simple soap/detergent within 20 seconds because the surfactant disrupts the same lipid envelope."
    },
    2307: {
        "topic": "Marek's Disease - Turkey Herpesvirus Vaccine",
        "Core_Anatomy": "T-lymphocytes and peripheral nerves.",
        "Pathogenesis_Immediate": "Marek's Disease vaccination utilizes the Turkey Herpesvirus (HVT - Herpesvirus of Turkeys), which is a non-oncogenic, apathogenic herpesvirus that cross-protects against Gallid alphaherpesvirus 2 (MDV).",
        "Pathogenesis_Deep": "HVT (MDV Serotype 3) is the most widely used Marek's disease vaccine strain worldwide. It is administered at hatchery (day 1) either as a single dose or in combination with MDV Serotype 2 (SB-1) or CVI988/Rispens (MDV Serotype 1). HVT establishes a harmless, lifelong replication in the feather follicle epithelium, constantly stimulating cell-mediated immunity that prevents tumor formation by virulent field MDV strains.",
        "Why_Not": "Phenolic compounds disinfect; they are not used for Marek's disease prevention. Sodium hypochlorite inactivates Infectious Bronchitis.",
        "Wow_Approach": "Marek's disease vaccination is a spectacular public health success: it was the world's FIRST anti-cancer vaccine ever developed for any species, and the HVT-based program eradicated clinical Marek's from commercial broiler and layer operations globally."
    },
    2308: {
        "topic": "FMD - Disinfectant (Onderstepoort)",
        "Core_Anatomy": "FMD virus (Aphthovirus, non-enveloped).",
        "Pathogenesis_Immediate": "The Onderstepoort research institution is matched to the development of important veterinary biologicals including FMD vaccines.",
        "Pathogenesis_Deep": "The Onderstepoort Biological Products (OBP) is South Africa's premier veterinary biologics producer, famous for developing and producing FMD vaccines for African serotypes (SAT-1, SAT-2, SAT-3). FMD virus is non-enveloped and is effectively killed by acid/alkali disinfectants. The virus is exquisitely sensitive to pH changes (inactivated below pH 6.0 or above pH 9.0), which is why sodium carbonate (washing soda) and citric acid are used as field disinfectants during FMD outbreaks.",
        "Why_Not": "Phenolic compounds are used as general bactericidal/virucidal disinfectants. The Onderstepoort association is specifically with FMD vaccine development.",
        "Wow_Approach": "During an FMD outbreak, vehicles leaving infected premises must drive through disinfectant foot baths containing 2% sodium carbonate or 1% citric acid to inactivate any residual FMDV on tyres before entering the road network."
    },
    2309: {
        "topic": "Canine Parvoviral Enteritis - Phenolic Compound Resistance",
        "Core_Anatomy": "Intestinal crypt epithelium.",
        "Pathogenesis_Immediate": "Canine Parvovirus (CPV-2) is extremely resistant to most disinfectants and requires Phenolic compounds (or bleach) for reliable inactivation.",
        "Pathogenesis_Deep": "CPV-2 is a non-enveloped virus with an extremely stable, tough protein capsid that resists desiccation, heat, and most common disinfectants (including quaternary ammonium compounds and many alcohol-based products). It can survive on contaminated surfaces for over 6 months at room temperature. The most effective disinfectants are: (1) Sodium hypochlorite (1:30 dilution), (2) Potassium peroxymonosulfate (Virkon-S), and (3) Phenolic compounds.",
        "Why_Not": "Quaternary ammonium compounds (like Benzalkonium Chloride) are ineffective against CPV-2. This is why CPV-2 spreads so explosively in kennels that are cleaned with ordinary cleaning products.",
        "Wow_Approach": "The Parvo-killing rule in kennels: 1 part household bleach to 30 parts water (1:30 dilution) must be left in contact for 10 minutes on the surface to achieve reliable CPV-2 inactivation."
    },
    2330: {
        "topic": "VPM Module Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This header marks the beginning of a new VPM exam paper.",
        "Pathogenesis_Deep": "VPM I covers Bacterial, Fungal, and Rickettsial diseases. VPM II covers Viral and Parasitic diseases. Both require mastery of diagnostic test matching and drug/disinfectant associations.",
        "Why_Not": "Clinical management belongs to VMD; VPM focuses on herd-level prevention and control programs.",
        "Wow_Approach": "India's NADCP (National Animal Disease Control Program) targets FMD, Brucellosis, and PPR for elimination—these three diseases generate the highest VPM exam question density."
    },
    2331: {
        "topic": "VPM Module Header (Continued)",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "Continuation of the VPM module header.",
        "Pathogenesis_Deep": "The scope of VPM includes both clinical prevention (vaccines, prophylaxis) and regulatory/legislative mechanisms (disease notification, quarantine, import regulations).",
        "Why_Not": "Individual animal diagnosis and treatment is the domain of VMD clinical medicine.",
        "Wow_Approach": "India notifies diseases to WOAH (formerly OIE) under two lists: OIE-listed diseases (mandatory notification within 24 hours) vs reportable diseases (domestic notification only)."
    },
    2333: {
        "topic": "VPM 412 Bacterial/Fungal/Rickettsial Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This header introduces the objective section of VPM 412, covering bacterial, fungal, and rickettsial disease prevention and control.",
        "Pathogenesis_Deep": "Key rickettsial diseases to master: Anaplasmosis (Ixodes/Dermacentor transmitted), Ehrlichiosis (Amblyomma transmitted), and Q Fever (Coxiella burnetii, aerosolized from parturient ruminants).",
        "Why_Not": "Viral diseases are covered in VPM II. This section focuses on bacterial/fungal/rickettsial pathogens only.",
        "Wow_Approach": "Q Fever is the most infectious disease known to science—a single inhaled organism of Coxiella burnetii is sufficient to establish infection in a human."
    },
    2334: {
        "topic": "VPM Fill in the Blanks Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of specific epidemiological values and diagnostic test names.",
        "Pathogenesis_Deep": "Targeted values: specific diagnostic test names (Ascoli, McFadyean, Strauss), dosage thresholds for vaccines, and specific regulatory quarantine periods.",
        "Why_Not": "Generic terms are not acceptable; exact proper nouns (names of tests, organisms, acts) are required.",
        "Wow_Approach": "High-yield: 'The ABR/MRT test is used for bulk milk Brucella screening.' 'Formaldehyde is the sporicidal agent for Anthrax premises decontamination.'"
    },
    2343: {
        "topic": "VPM MCQ Section Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This MCQ section tests diagnostic test–disease pairings, drug specificity, and epidemiological associations.",
        "Pathogenesis_Deep": "High-density MCQ areas in VPM: Clostridial disease classification, specific disinfectant-virus pairings, and zoonotic disease control legislation.",
        "Why_Not": "Do not mix up serological tests between diseases—each test has one primary target disease.",
        "Wow_Approach": "Master this chain: Anthrax → Ascoli/McFadyean/Polychrome MB; Brucella → RBPT/MRT; Leptospira → MAT; Glanders → Mallein/Strauss; Hydatid → Casoni."
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
