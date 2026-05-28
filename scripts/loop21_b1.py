import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2387: {
        "topic": "Bovine Trichomoniasis - Persistent Infection",
        "Core_Anatomy": "Preputial epithelium (bull) and uterine lumen (cow).",
        "Pathogenesis_Immediate": "Trichomoniasis is matched to 'Persistent infection' in the context of the carrier bull.",
        "Pathogenesis_Deep": "Tritrichomonas foetus establishes a permanent, lifelong persistent infection in the preputial smegma folds of bulls. Unlike cows (which eventually clear the infection after several months of sexual rest), infected bulls—particularly older bulls—never self-clear. The trichomonal organisms reside permanently in the crypts of the prepuce, causing NO clinical signs in the bull but being transmitted to every cow he services during natural breeding, causing early embryonic death and repeat breeding.",
        "Why_Not": "BVD virus creates persistent infection in CALVES (born from cows infected between days 40-120 of gestation). Trichomoniasis creates persistent infection in ADULT BULLS specifically.",
        "Wow_Approach": "Because infected bulls remain permanently and silently infected, the only control option is testing all bulls before the breeding season (using preputial scraping for culture/PCR) and culling all reactor bulls immediately."
    },
    2388: {
        "topic": "Spirocerca lupi - Oesophageal Location",
        "Core_Anatomy": "Oesophageal wall and aortic wall.",
        "Pathogenesis_Immediate": "Spirocerca lupi is matched to the Oesophagus as its primary anatomical location.",
        "Pathogenesis_Deep": "Spirocerca lupi is a bright red spirurid nematode of dogs and wild canids. Its complex lifecycle involves a coprophagous beetle intermediate host. After a dog ingests the infected beetle, the L3 larvae migrate through the aortic wall (causing aortic aneurysm) and then through surrounding tissues to the oesophageal wall. In the oesophagus, the worms encapsulate in large, nodular granulomas. These nodules can compress the oesophageal lumen (causing dysphagia), and in a remarkable biological phenomenon, the chronic inflammation can transform into fibrosarcoma or osteosarcoma.",
        "Why_Not": "Ascaris suum migrates through the liver and lungs. Dirofilaria immitis occupies the pulmonary arteries. Only Spirocerca lupi creates oesophageal nodules that can undergo neoplastic transformation.",
        "Wow_Approach": "Spirocercosis-associated osteosarcoma of the oesophagus is one of the clearest examples of parasite-induced malignancy in veterinary medicine. Dogs presenting with regurgitation AND hypertrophic osteopathy (periosteal new bone formation on the long bones) should be immediately endoscoped for Spirocerca nodules."
    },
    2389: {
        "topic": "Leechi Disease - Theileriosis",
        "Core_Anatomy": "Lymphocytes and erythrocytes.",
        "Pathogenesis_Immediate": "'Leechi Disease' is a colloquial regional name for Theileriosis in Indian livestock.",
        "Pathogenesis_Deep": "Theileria annulata causes Tropical Theileriosis in India, transmitted by Hyalomma ticks. The disease is characterized by fever, lymphadenopathy, anemia, and jaundice. In some parts of India (particularly Punjab and Rajasthan), the disease is colloquially called 'Leechi Disease' because the massively swollen, jugular lymph nodes at the neck resemble the appearance of a cluster of Lychee (Leechi) fruits. The prescapular and parotid lymph nodes enlarge dramatically as they fill with macroschizonts (Koch's Blue Bodies).",
        "Why_Not": "Leechi disease is not a separate disease entity—it is simply a regional vernacular for Theileriosis. Babesiosis is a separate tick-borne hemoprotozoan disease of RBCs (not lymphocytes).",
        "Wow_Approach": "In the field, diagnosing Leechi Disease is simple: aspirate the grossly enlarged prescapular lymph node with a 21G needle, make an impression smear, stain with Giemsa, and look for the large, granular Koch's Blue Bodies inside lymphocytes."
    },
    2399: {
        "topic": "Neospora caninum - Repeat Abortion in Crossbred Cow",
        "Core_Anatomy": "Placenta and fetal nervous system.",
        "Pathogenesis_Immediate": "A crossbred cow with abortion in the third trimester during TWO consecutive pregnancies is highly suspicious of Neospora caninum infection.",
        "Pathogenesis_Deep": "Neospora caninum causes vertically transmitted bovine abortion at 3-9 months gestation. A key diagnostic clue is REPETITION—the same cow aborting in successive pregnancies. This occurs because Neospora can establish persistent infection in the cow's tissues, and during each subsequent pregnancy, the tachyzoites cross the placenta again during the period of physiological immunosuppression in pregnancy. The cow is a 'reservoir' that perpetuates the infection vertically to each calf she carries.",
        "Why_Not": "Brucellosis also causes repeat abortion but typically resolves after the first abortion as the cow develops immunity. Leptospirosis causes sporadic abortions. Only Neospora causes the reliable, consistent, pregnancy-linked repeat abortion pattern in the same cow.",
        "Wow_Approach": "If two cows in the same herd are both showing repeat third-trimester abortions AND farm dogs have access to bovine placental material, the epidemiological triad (dog definitive host + cattle intermediate host + aborted fetuses fed to dogs) is complete—test the cows with IFAT for Neospora and immediately remove dogs from areas where cows calve."
    },
    2404: {
        "topic": "Exam Instructions Header",
        "Core_Anatomy": "N/A - Examination Rules.",
        "Pathogenesis_Immediate": "Standard examination protocol header for Part A objective section.",
        "Pathogenesis_Deep": "Part A objective sections require rapid recall within strict time limits of critical diagnostic and epidemiological facts.",
        "Why_Not": "Do not spend more than 45 seconds per objective question.",
        "Wow_Approach": "Complete all fill-in-the-blanks before MCQs—they carry full marks with no partial credit risk."
    },
    2405: {
        "topic": "VPM 412 Objective Section Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine - Bacterial, Fungal, and Rickettsial Diseases.",
        "Pathogenesis_Immediate": "This header marks the 30-mark objective section of VPM 412 covering bacterial, fungal, and rickettsial disease prevention and control.",
        "Pathogenesis_Deep": "This section tests key diagnostic tests, drug choices, and epidemiological associations for major bacterial zoonoses (Anthrax, Brucellosis, Leptospirosis, TB) and rickettsial diseases (Anaplasmosis, Ehrlichiosis, Q Fever).",
        "Why_Not": "Viral diseases are in VPM 422. Focus here is strictly on bacterial, fungal, and rickettsial pathogens.",
        "Wow_Approach": "Master the drug-of-choice for each pathogen class: Rickettsiae → Doxycycline/OTC; Mycoplasma → Tylosin/OTC; Fungi → Terbinafine/Griseofulvin."
    },
    2406: {
        "topic": "Anthrax Spore - Sporicidal Agent",
        "Core_Anatomy": "Bacillus anthracis endospore.",
        "Pathogenesis_Immediate": "The sporicidal agent used to kill Anthrax spores is 10% Formalin (formaldehyde).",
        "Pathogenesis_Deep": "Bacillus anthracis spores have a multi-layered structure (core, cortex, inner and outer spore coats) making them extraordinarily resistant to heat, UV light, desiccation, and most standard disinfectants. Formaldehyde (10% formalin) is effective because it crosslinks amino and thiol groups throughout the spore's proteins and nucleic acids via alkylation, preventing enzymatic activity permanently. Affected premises must be thoroughly drenched with 10% formalin after deep burial of the carcass.",
        "Why_Not": "Standard bleach at household dilutions is insufficient. Alcohol evaporates before achieving reliable sporicidal penetration. Only formalin, peracetic acid, or glutaraldehyde at sufficient concentrations achieve reliable anthrax spore destruction.",
        "Wow_Approach": "Historical anthrax 'cursed fields' (like Gruinard Island, Scotland) remained contaminated with viable B. anthracis spores for over 40 years after a WWII bioweapons test—ultimately requiring thousands of tonnes of formaldehyde solution and seawater to finally decontaminate."
    },
    2414: {
        "topic": "VPM True/False Section Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This True/False section tests absolute factual accuracy regarding disease epidemiology and control.",
        "Pathogenesis_Deep": "Common True/False traps in VPM: 'Rinderpest is eradicated' (TRUE), 'Maedi-Visna has an effective vaccine' (FALSE—Sigurdsson's provided limited protection), 'Trichomoniasis causes late-term abortion' (FALSE—it causes early embryonic death).",
        "Why_Not": "A single incorrect epidemiological claim renders the entire statement FALSE.",
        "Wow_Approach": "Watch for double-negatives and qualifying words like 'always,' 'never,' and 'only'—these are the primary sources of incorrect True/False statements."
    },
    2424: {
        "topic": "Strangles (Equine) - Streptococcus equi",
        "Core_Anatomy": "Submandibular and retropharyngeal lymph nodes.",
        "Pathogenesis_Immediate": "Strangles (Equine Distemper) is matched to Streptococcus equi subsp. equi.",
        "Pathogenesis_Deep": "S. equi equi possesses an anti-phagocytic hyaluronate capsule and M-like protein (SeM). After colonizing the tonsillar crypts, it spreads to regional lymph nodes where it forms large, thick-walled abscesses. These abscesses rupture externally, discharging characteristic thick, creamy, bright yellow pus. The disease is most severe in young horses (6 months to 5 years) with no prior immunity.",
        "Why_Not": "Strangles is NOT related to the parturient period (which is associated with milk fever/hypocalcemia). Parturient period = metabolic disease of parturition.",
        "Wow_Approach": "Strangles is the most common equine infectious disease worldwide. Critically, horses can remain as 'silent carriers' in the Guttural Pouches for years after clinical recovery, shedding S. equi intermittently and infecting naive horses—making guttural pouch endoscopy and lavage essential for full clearance certification."
    },
    2425: {
        "topic": "Psittacosis - Avian Pasteurellosis (Fowl Cholera)",
        "Core_Anatomy": "Avian respiratory epithelium and macrophages.",
        "Pathogenesis_Immediate": "In this match, Psittacosis (Chlamydia psittaci) is being paired with its route of transmission (inhalation/ingestion), while Avian Pasteurellosis (Fowl Cholera) is a separate highly fatal septicemic avian disease.",
        "Pathogenesis_Deep": "Fowl Cholera (Pasteurella multocida serotype A) is an acute to peracute septicemic disease of poultry causing extremely rapid death (birds found dead without premonitory signs). Post-mortem reveals severe congestion, pinpoint hemorrhages throughout the viscera, and a grossly enlarged, hemorrhagic liver. The distinctive 'bipolar' staining pattern of P. multocida is visible on impression smears.",
        "Why_Not": "Psittacosis is caused by Chlamydia psittaci—an intracellular organism requiring tetracyclines. Fowl Cholera is caused by Pasteurella multocida—an extracellular bacterium treated with sulfonamides or tetracyclines.",
        "Wow_Approach": "Autogenous vaccines are specifically preferred for Fowl Cholera control on individual farms because P. multocida shows significant serotype variation between farm strains, making commercial vaccines sometimes inadequate for specific outbreak strains."
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
