import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2232: {
        "topic": "VPM Module Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This header marks the beginning of a new VPM exam paper.",
        "Pathogenesis_Deep": "VPM papers cover the full spectrum of disease prevention: epidemiology, disease surveillance, vaccination programs, vector control, and legislative frameworks.",
        "Why_Not": "Clinical treatment is outside the scope of preventive medicine exams.",
        "Wow_Approach": "Think 'PHEIC' framework for each disease: Prevention, Host, Environment, Intervention, Control measures."
    },
    2234: {
        "topic": "Exam Instructions Header",
        "Core_Anatomy": "N/A - Examination Rules.",
        "Pathogenesis_Immediate": "Standard examination protocol header denoting the time limit for Part A.",
        "Pathogenesis_Deep": "Part A objective questions require rapid recall within strict time limits.",
        "Why_Not": "Do not spend more than 30-45 seconds per objective question.",
        "Wow_Approach": "Always complete all fill-in-the-blanks first before MCQs, as they carry full marks with no partial credit risk."
    },
    2235: {
        "topic": "VPM 412 Objective Questions Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "Marks the beginning of the objective section covering Bacterial, Fungal, and Rickettsial diseases.",
        "Pathogenesis_Deep": "This section tests the specific epidemiological details of major bacterial and rickettsial zoonoses relevant to Indian veterinary practice.",
        "Why_Not": "Viral diseases are covered in a separate VPM-II module.",
        "Wow_Approach": "High-yield keywords: BBAT/RBPT (Brucella), MAT (Leptospira), Coggins/AGID (EIA), Casoni (Hydatid)."
    },
    2236: {
        "topic": "Brucellosis Herd Screening & Anthrax Decontamination",
        "Core_Anatomy": "Bulk tank milk antibodies and anthrax spore decontamination.",
        "Pathogenesis_Immediate": "For bulk milk Brucella herd screening: the Milk Ring Test (MRT/ABR). For Anthrax premises decontamination: 10% Formalin.",
        "Pathogenesis_Deep": "(1) The Milk Ring Test (Abortus Bang Ring Test) detects anti-Brucella antibodies in pooled bulk milk by their adherence to cream fat globules, creating a blue ring above white milk column. (2) After an anthrax outbreak, premises decontamination requires sporicidal agents. 10% Formalin (formaldehyde) is the only practical agent that effectively destroys Bacillus anthracis spores in the field environment.",
        "Why_Not": "Standard bleach (hypochlorite at household concentrations) is insufficient for anthrax spores. The MRT cannot be performed on individual animal blood.",
        "Wow_Approach": "In India, anthrax-contaminated hides and hoof products are a major occupational risk for leather workers, requiring mandatory formaldehyde fumigation of tanneries in endemic areas."
    },
    2248: {
        "topic": "Bovine Tuberculosis - Gold Standard Diagnosis in India",
        "Core_Anatomy": "Cutaneous immune system (tuberculin skin test).",
        "Pathogenesis_Immediate": "In India, the gold standard diagnostic test for Bovine Tuberculosis is the Single Intradermal Tuberculin Test (SITT) using Bovine Purified Protein Derivative (PPD).",
        "Pathogenesis_Deep": "The SITT relies on Type IV Delayed-Type Hypersensitivity (DTH). Bovine PPD is injected intradermally in the mid-cervical region. Memory T-cells in a Mycobacterium bovis-sensitized cow migrate to the site and release cytokines (IFN-γ, TNF-α), causing local induration and swelling. A skin fold increase of ≥4mm (differential test) or ≥3mm (comparative test) at 72 hours is considered a positive reactor.",
        "Why_Not": "The Gamma Interferon Assay (GIA/BOVIGAM) is a more sensitive blood-based alternative but is more expensive and not yet the primary field standard in India. ELISA and AFB staining are used for laboratory confirmation post-mortem.",
        "Wow_Approach": "India's National Animal Disease Control Program (NADCP) targets elimination of Bovine Tuberculosis by 2030 using systematic skin testing and culling of reactors, alongside the simultaneous elimination of Brucellosis and FMD."
    },
    2249: {
        "topic": "Clostridium septicum - Braxy",
        "Core_Anatomy": "Abomasal wall and systemic circulation.",
        "Pathogenesis_Immediate": "Clostridium septicum is the causative agent of Braxy (Abomasitis) in sheep.",
        "Pathogenesis_Deep": "Braxy (Bradsot) is a rapidly fatal peracute disease of young sheep, particularly in Scandinavia and Scotland, caused by C. septicum. It typically occurs in winter when sheep graze frosted pasture. The frozen grass damages the abomasal mucosa, creating ideal anaerobic conditions for C. septicum germination. The bacteria release powerful Alpha toxin (a lecithinase), causing severe hemorrhagic and necrotic abomasitis, acute toxemia, and rapid death—often before any clinical signs are observed.",
        "Why_Not": "Bacillary Hemoglobinuria is caused by C. haemolyticum/novyi type D. Botulism is caused by C. botulinum. Enterotoxemia is C. perfringens type D. Only C. septicum causes Braxy (abomasal disease) and Malignant Edema (wound disease).",
        "Wow_Approach": "Because death occurs so rapidly in Braxy, the most important intervention is PRE-EMPTIVE vaccination with a clostridial bacterin before the winter grazing season begins."
    },
    2250: {
        "topic": "Botulism - Resistant Species",
        "Core_Anatomy": "Neuromuscular junction (Acetylcholine vesicle fusion).",
        "Pathogenesis_Immediate": "Among domestic animals, the Dog is the most resistant species to botulism.",
        "Pathogenesis_Deep": "Botulism is caused by the neurotoxin of Clostridium botulinum, which prevents acetylcholine release at the neuromuscular junction, causing ascending flaccid paralysis. Species susceptibility varies dramatically: Cattle and horses are highly susceptible (especially to Types B and C toxins from contaminated water/feed). Dogs and cats are highly resistant due to differences in their intestinal microflora and specific neuroreceptor binding site architecture that reduces botulinum toxin uptake.",
        "Why_Not": "Cattle are among the most susceptible species. Sheep have intermediate susceptibility. The dog's resistance is a well-established clinical and experimental fact.",
        "Wow_Approach": "Canine botulism (rare) is typically Type C from eating raw poultry carcasses. Even then, the dose required to paralyze a dog is many times higher than that needed to kill a horse."
    },
    2251: {
        "topic": "Johne's Disease (JD) - Incubation Period",
        "Core_Anatomy": "Small intestinal submucosa and mesenteric lymph nodes.",
        "Pathogenesis_Immediate": "In Johne's Disease (JD / Paratuberculosis) infection, clinical signs manifest only after a prolonged incubation period of approximately 2-5 years.",
        "Pathogenesis_Deep": "Mycobacterium avium subsp. paratuberculosis (MAP) is ingested by calves primarily in the first few weeks of life from contaminated colostrum, feces, or environment. However, the immune system of young animals initially controls the infection. Over years, as the animal's immunity gradually wanes under production stress, MAP replicates massively in the ileal macrophages (causing granulomatous enteritis). By the time clinical signs (weight loss, 'pipe-stem' diarrhea, bottle jaw) appear, the cow is already 4-7 years old and has been shedding bacteria and infecting the environment for years.",
        "Why_Not": "A 1-year incubation is far too short; the typical clinical case presents at 4-7 years of age with infection acquired as a calf.",
        "Wow_Approach": "Because MAP is shed in feces years before clinical disease appears, regular fecal PCR testing of all cows in a herd (or ELISA serology) is the only way to identify and remove subclinical shedders before they contaminate the entire calf crop."
    },
    2252: {
        "topic": "Pullorum Disease - Species Susceptibility",
        "Core_Anatomy": "Small intestine and systemic organs (reticuloendothelial system).",
        "Pathogenesis_Immediate": "Pullorum disease (caused by Salmonella Pullorum) is primarily prevalent in Chickens and also in Turkeys (both are equally susceptible).",
        "Pathogenesis_Deep": "Salmonella Pullorum is highly host-adapted. It causes Bacillary White Diarrhea (BWD) in young chicks within the first 2 weeks of life (sourced from vertical/transovarial transmission). While chickens and turkeys are the main clinical species affected, Pullorum disease has been eradicated from commercial poultry in most developed countries through aggressive RPA-test-and-slaughter programs. In India, it remains endemic in backyard flocks.",
        "Why_Not": "While Quails and game birds can be infected experimentally, commercial relevance is restricted to chickens and turkeys. Wild birds rarely develop clinical disease.",
        "Wow_Approach": "Unlike most Salmonella strains that affect humans, Salmonella Pullorum is so highly host-adapted to chickens/turkeys that it essentially does NOT cause human illness—a unique exception to the zoonotic Salmonella group."
    },
    2253: {
        "topic": "Equine Strangles - 'Equine Distemper'",
        "Core_Anatomy": "Lymph nodes of the head (retropharyngeal and submandibular).",
        "Pathogenesis_Immediate": "The disease historically known as 'Equine Distemper' is Strangles, caused by Streptococcus equi subspecies equi.",
        "Pathogenesis_Deep": "Strangles is the most common equine bacterial respiratory disease worldwide. S. equi equi attaches to the tonsillar crypts and rapidly colonizes the upper respiratory tract. It then spreads to the regional lymph nodes (retropharyngeal, submandibular, and parotid). These lymph nodes undergo massive abscessation and eventually rupture externally, discharging thick, creamy yellow pus. In severe cases, swollen retropharyngeal nodes compress the airway, causing dyspnea and 'strangling' the horse—hence the name.",
        "Why_Not": "Glanders (B. mallei) is a completely different, fatal, OIE-listed disease. Tetanus (C. tetani) causes rigidity, not lymph node abscessation. Salmonellosis causes GI disease.",
        "Wow_Approach": "A rare but catastrophic complication of Strangles is 'Bastard Strangles' where abscesses metastasize to internal organs (liver, lungs, brain), or 'Purpura Hemorrhagica' where immune complex deposition causes severe vasculitis and massive skin edema."
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
