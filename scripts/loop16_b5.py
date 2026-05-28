import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1889: {
        "topic": "Veterinary Microbiology - Anthrax History",
        "Core_Anatomy": "N/A - Scientific History.",
        "Pathogenesis_Immediate": "The historically correct statement regarding Anthrax is that it was the very first disease definitively proven to be caused by a specific bacterium.",
        "Pathogenesis_Deep": "In 1876, Robert Koch utilized Bacillus anthracis to formulate 'Koch's Postulates'. By isolating the anthrax bacilli from a dead sheep, growing them in pure culture outside the body, and injecting them into a healthy mouse (which subsequently died of anthrax), he provided the first undeniable proof of the 'Germ Theory of Disease'—that a specific microorganism causes a specific pathology.",
        "Why_Not": "Rabies was later proven to be viral. Tuberculosis was discovered by Koch later in 1882. Anthrax was the foundational proof of bacteriology.",
        "Wow_Approach": "Anthrax was not only the first bacterium proven to cause disease, but it was also the first disease for which a live attenuated bacterial vaccine was created (by Louis Pasteur in 1881)."
    },
    1890: {
        "topic": "Brucellosis Prophylaxis - Calf-Hood Vaccination",
        "Core_Anatomy": "Systemic humoral and cell-mediated immunity.",
        "Pathogenesis_Immediate": "Mandatory 'Calf-hood vaccination' is specifically advised and legally utilized for the control of Bovine Brucellosis.",
        "Pathogenesis_Deep": "The classic Strain 19 (S19) vaccine is a live, attenuated smooth strain of Brucella abortus. Because it produces persistent antibodies that interfere with adult serum agglutination tests (STAT), it must ONLY be given to female calves between 4 to 8 months of age. If given during this specific 'calf-hood' window, the calf develops strong immunity, but the interfering vaccine antibodies naturally fade away by the time she reaches breeding age (so she won't trigger a false positive on a diagnostic test later in life).",
        "Why_Not": "Anthrax and Hemorrhagic Septicemia vaccines are given to animals of all ages, not restricted strictly to the calf-hood window.",
        "Wow_Approach": "Modern programs are shifting to the RB51 vaccine (a rough strain lacking O-side chains) because it NEVER interferes with diagnostic tests, allowing for adult cow vaccination."
    },
    1891: {
        "topic": "Foot and Mouth Disease (FMD) - Hairy Panters",
        "Core_Anatomy": "Hypothalamus and thyroid gland.",
        "Pathogenesis_Immediate": "The chronic, debilitating syndrome known as 'Hairy Panters' is a classic sequel of Foot and Mouth Disease (FMD) in cattle.",
        "Pathogenesis_Deep": "While acute FMD causes oral vesicles, the Aphthovirus also has a distinct tropism for the endocrine system, specifically causing severe, permanent necrosis of the hypothalamus, pituitary, and thyroid glands. Even after recovering from the acute vesicles, the cow loses its ability to thermoregulate. During hot weather, the cow suffers from profound hyperthermia, pants incessantly (panting syndrome), fails to shed its winter coat (hirsutism/hairy), and never returns to normal milk production.",
        "Why_Not": "Vesicular stomatitis and Vesicular exanthema cause similar acute blisters, but they do NOT cause the massive, permanent endocrine destruction seen as a sequel in FMD.",
        "Wow_Approach": "A 'Hairy Panter' is economically useless; despite surviving the virus, the cow will remain permanently emaciated and dyspneic, requiring culling."
    },
    1892: {
        "topic": "African Horse Sickness (AHS) - Zebra Presentation",
        "Core_Anatomy": "Vascular endothelium and systemic circulation.",
        "Pathogenesis_Immediate": "The specific form of African Horse Sickness seen in the natural reservoir, the Zebra, is the mild 'Horse Sickness Fever' form.",
        "Pathogenesis_Deep": "AHS presents in four forms: (1) Pulmonary (Dunkop) - 95% fatal, (2) Cardiac (Dikkop) - 50% fatal, (3) Mixed, and (4) Horse Sickness Fever - 100% survival. Because Zebras have co-evolved with the Orbivirus for millennia, they possess extreme innate resistance. When bitten by an infected midge, they only develop the mildest form: a transient fever (Horse Sickness Fever) with mild anorexia, allowing them to survive and act as the perfect amplifying reservoir.",
        "Why_Not": "The Pulmonary (Dunkop) form is the peracute, highly fatal form seen in fully naive, susceptible horses or dogs that eat infected horse meat.",
        "Wow_Approach": "This perfectly illustrates host-parasite evolution; a virus does not 'want' to rapidly kill its natural reservoir, as that halts transmission."
    },
    1893: {
        "topic": "Louping Ill - Ovine Encephalomyelitis",
        "Core_Anatomy": "Cerebellum and brainstem.",
        "Pathogenesis_Immediate": "A stiff, jerky, bounding gait (often compared to a kangaroo) in sheep is classically recorded in Louping Ill.",
        "Pathogenesis_Deep": "Louping Ill is a tick-borne Flavivirus (transmitted by Ixodes ricinus). The virus aggressively targets the central nervous system, causing severe non-suppurative encephalomyelitis with massive destruction of the Purkinje cells in the cerebellum. This loss of cerebellar coordination causes severe ataxia. The sheep exhibits a characteristic, exaggerated, leaping or bounding gait (the old Scottish word 'loup' means to jump or leap) before progressing to paralysis and death.",
        "Why_Not": "Scrapie causes pruritus (nibbling reflex) and ataxia, but 'Louping' is the specific eponymous leaping gait of the Flavivirus. Maedi-Visna primarily causes chronic pneumonia (Maedi) and wasting/paresis (Visna).",
        "Wow_Approach": "Louping Ill is zoonotic; veterinarians performing necropsies on these leaping sheep can contract the virus (causing severe human encephalitis) through aerosolized brain tissue or accidental scalpel nicks."
    },
    1894: {
        "topic": "Ovine Pulmonary Adenocarcinoma - Jaagsiekte",
        "Core_Anatomy": "Pulmonary alveoli (Type II pneumocytes).",
        "Pathogenesis_Immediate": "The classic, pathognomonic physical exam maneuver known as the 'Wheelbarrow Test' is recommended for the diagnosis of Jaagsiekte (Ovine Pulmonary Adenocarcinoma).",
        "Pathogenesis_Deep": "Jaagsiekte is caused by a Betaretrovirus that transforms the Type II pneumocytes in the sheep's lungs into neoplastic tumor cells. These tumors secrete massive, voluminous amounts of watery surfactant fluid. If you physically lift the sheep's hind legs high into the air (like holding the handles of a wheelbarrow) and lower its head, up to 100-200 mL of frothy, clear fluid will literally pour directly out of the nostrils. This confirms the diagnosis.",
        "Why_Not": "Scrapie is a prion disease of the brain. Contagious ecthyma (Orf) affects the lips. Maedi causes chronic dry pneumonia, but does NOT produce the massive fluid volumes seen in Jaagsiekte.",
        "Wow_Approach": "A positive wheelbarrow test is a death sentence; there is no treatment for this viral lung cancer, and the sheep must be immediately culled to prevent aerosol transmission to the flock."
    },
    1895: {
        "topic": "Bovine Mastitis - Blitz Therapy",
        "Core_Anatomy": "Mammary gland (Streptococcus agalactiae).",
        "Pathogenesis_Immediate": "The intensive, whole-herd antibiotic treatment strategy known as 'Blitz Therapy' is specifically indicated for the eradication of Streptococcus agalactiae mastitis.",
        "Pathogenesis_Deep": "Streptococcus agalactiae is an obligate parasite of the bovine udder; it cannot survive anywhere else in the environment. It is also exquisitely sensitive to Penicillin. In 'Blitz Therapy', every single quarter of every single cow in the herd (both clinical and subclinical) is cultured. ALL positive cows are simultaneously treated with intramammary penicillin. Because the bacteria cannot hide in the environment and are easily killed by the drug, this simultaneous 'blitz' permanently eradicates the pathogen from the entire farm.",
        "Why_Not": "Staphylococcus aureus micro-abscesses wall off the antibiotics, making Blitz therapy totally ineffective. Environmental pathogens (E. coli) will simply reinfect the cows from the bedding the next day.",
        "Wow_Approach": "Streptococcus agalactiae is the ONLY major mastitis pathogen that can be completely eradicated from a dairy farm using antibiotics alone."
    },
    1896: {
        "topic": "Caprine Brucellosis - Rev. 1 Vaccine",
        "Core_Anatomy": "Reproductive tract (placenta) and systemic immunity.",
        "Pathogenesis_Immediate": "The highly effective, live-attenuated Rev. 1 vaccine is specifically indicated and utilized against Brucella melitensis in sheep and goats.",
        "Pathogenesis_Deep": "Brucella melitensis is the most highly pathogenic and zoonotic of all Brucella species (causing severe Malta Fever in humans). To control abortion storms in small ruminants, the Elberg Rev. 1 vaccine is used. It is a live, attenuated strain of B. melitensis. It must be administered strictly via the conjunctival route (eye drops) or subcutaneously to young replacement females (3-5 months old) to confer lifelong cellular immunity.",
        "Why_Not": "Brucella abortus in cattle uses the S19 or RB51 vaccine. Brucella ovis (causing epididymitis in rams) is sometimes cross-protected by Rev. 1, but the primary target is B. melitensis.",
        "Wow_Approach": "Never inject the Rev. 1 vaccine into a pregnant goat; because it is a live vaccine, it retains enough residual virulence to cross the placenta and cause the exact abortion you are trying to prevent."
    },
    1897: {
        "topic": "Equine Infectious Anemia (EIA) - Coggins Test",
        "Core_Anatomy": "Serum antibodies (humoral immunity).",
        "Pathogenesis_Immediate": "The Agar Gel Immunodiffusion (AGID) test, universally known as the Coggins test, is the gold standard diagnostic for Equine Infectious Anemia (EIA).",
        "Pathogenesis_Deep": "EIA is a lifelong lentivirus infection. Leroy Coggins developed the AGID test in 1970. It relies on detecting specific antibodies against the viral p26 core protein in the horse's serum. In the test, viral antigen and patient serum are placed in adjacent wells cut into agar. They diffuse toward each other, and if antibodies are present, a visible white 'line of precipitation' forms where they meet, definitively confirming the horse is a lifelong carrier.",
        "Why_Not": "Equine Viral Arteritis (EVA) and Equine Influenza are typically diagnosed via PCR or Virus Neutralization, not the AGID Coggins test.",
        "Wow_Approach": "In almost all jurisdictions, a negative Coggins test certificate (drawn within the last 6-12 months) is a strict legal requirement for transporting a horse across state/provincial lines or entering a showground."
    },
    1898: {
        "topic": "Porcine Erysipelas - Vegetative Endocarditis",
        "Core_Anatomy": "Cardiac valves (mitral/aortic) and systemic circulation.",
        "Pathogenesis_Immediate": "Severe, cauliflower-like 'Vegetative Endocarditis' on the heart valves is a pathognomonic chronic lesion of Erysipelothrix rhusiopathiae (Diamond Skin Disease) in pigs.",
        "Pathogenesis_Deep": "While acute Erysipelas causes pathognomonic rhomboid ('diamond') skin lesions due to bacterial emboli in the cutaneous vessels, the chronic form is far more insidious. Erysipelothrix rhusiopathiae bacteria localize specifically on the heart valves (especially the mitral valve). The bacteria trigger massive fibrin deposition and granulomatous inflammation, creating enormous, friable, 'cauliflower-like' vegetative growths. These growths destroy the valve's competence, leading to chronic congestive heart failure and sudden death from cardiac arrest.",
        "Why_Not": "Listeria causes encephalitis. Leptospira causes nephritis/abortions. Pasteurella causes pneumonia. None of these classically cause massive valvular endocarditis in swine.",
        "Wow_Approach": "If a seemingly healthy, older breeding sow suddenly drops dead after mild exertion, and necropsy reveals massive warty growths on the mitral valve, chronic Erysipelas is the definitive diagnosis."
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

# Final validation
with open(db_path, "r", encoding="utf-8") as f:
    c2 = f.read()
d2 = json.loads(re.sub(r'^.*?const examData = ', '', c2, flags=re.DOTALL).rsplit(';',1)[0].strip())
empty2 = [x for x in d2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
