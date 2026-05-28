import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2179: {
        "topic": "Brucellosis Diagnosis - BBAT",
        "Core_Anatomy": "Systemic serology.",
        "Pathogenesis_Immediate": "The BBAT (Buffered Brucella Antigen Test), also known as the Buffered Plate Agglutination Test (BPAT) or Rose Bengal Plate Test (RBPT), is used specifically for the diagnosis of Brucellosis.",
        "Pathogenesis_Deep": "The BBAT/RBPT uses smooth Brucella abortus antigens stained with rose bengal dye, buffered to a low pH of 3.65. At this acidic pH, non-specific IgM antibodies (which cause false positives in standard plate agglutination) are denatured. Only highly specific IgG anti-Brucella antibodies remain functional and cause true agglutination. This makes the RBPT highly sensitive AND more specific than the unmodified Standard Plate Agglutination Test (SPAT).",
        "Why_Not": "BBAT is for Brucellosis. Rapid Plate Agglutination (RPA) is for Pullorum and Fowl Typhoid in poultry. TTV (Turkey Typhoid Vaccine) is irrelevant.",
        "Wow_Approach": "The RBPT is the most widely used field screening test for Brucellosis globally because it is fast (results in 4 minutes), inexpensive, and requires no equipment beyond a glass plate and a lamp."
    },
    2180: {
        "topic": "CCPP - Drug of Choice",
        "Core_Anatomy": "Pleural membranes and pulmonary parenchyma.",
        "Pathogenesis_Immediate": "The drug of choice for treating Contagious Caprine Pleuropneumonia (CCPP) is Tylosin (or Oxytetracycline for secondary infections).",
        "Pathogenesis_Deep": "CCPP is caused by Mycoplasma capricolum subsp. capripneumoniae. Like all Mycoplasma species, it lacks a cell wall, making all beta-lactam antibiotics (Penicillin, Cephalosporins) completely ineffective. Tylosin (a macrolide) and Oxytetracycline are highly effective because they target the ribosome (protein synthesis) rather than the cell wall. Tylosin is preferred because it achieves high concentrations in pulmonary secretions.",
        "Why_Not": "Penicillin is absolutely useless against any Mycoplasma species. Gentamicin has poor bioavailability via oral route and limited pulmonary penetration.",
        "Wow_Approach": "CCPP causes 100% morbidity and 60-100% mortality in naive goat herds. The Mycoplasma spreads via aerosol over very short distances, making quarantine of the entire affected unit essential."
    },
    2181: {
        "topic": "VPM True/False Section Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This section tests absolute evaluation of epidemiological and diagnostic facts.",
        "Pathogenesis_Deep": "These statements often contain a single incorrect epidemiological figure (incubation period, mortality rate, or reservoir species) that must be identified.",
        "Why_Not": "Partial correctness is not acceptable in disease control contexts; incorrect statements can lead to failure of a control program.",
        "Wow_Approach": "Look for qualifier words like 'always,' 'never,' 'only,' and 'all' as these are often the source of falsity in True/False statements."
    },
    2182: {
        "topic": "VPM True/False Section - Continued",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "Continuation of the True/False section in VPM.",
        "Pathogenesis_Deep": "Key areas tested: OIE notifiable disease lists, vaccination schedules, reservoir species, and vector identification.",
        "Why_Not": "Do not confuse the reservoir (maintenance host) with the amplifying host or the incidental (dead-end) host.",
        "Wow_Approach": "For any True/False on OIE diseases: Rinderpest (eradicated 2011) and Smallpox (eradicated 1980) are the only two infectious diseases officially declared globally eradicated."
    },
    2194: {
        "topic": "FMD 2013 Outbreak and PPR Etiology",
        "Core_Anatomy": "FMD: Oral epithelium, coronary band; PPR: Lymphoid tissue.",
        "Pathogenesis_Immediate": "In India, the FMD serotype O caused the major 2013 outbreak. The etiology of Goat Plague (PPR) is the Peste des Petits Ruminants Virus (PPRV), a Morbillivirus.",
        "Pathogenesis_Deep": "(1) FMD Serotype O/ME-SA/Ind-2001 lineage dominated Indian outbreaks in 2013, prompting urgent revision of vaccine strains in the national FMD-CP trivalent vaccine. (2) Goat Plague (PPR) is caused by the Peste des Petits Ruminants Virus (PPRV), a Morbillivirus closely related to Rinderpest and Measles viruses. PPRV causes severe mucopurulent nasal/ocular discharge, erosive stomatitis, and diarrhea with high mortality in sheep and goats.",
        "Why_Not": "PPR is NOT caused by Rinderpest virus (though they are in the same genus). PPR is also NOT the same as Ovine Rinderpest (a misnomer).",
        "Wow_Approach": "The global PPR eradication program (WOAH/FAO target: eradicate by 2030) is modeled after the successful Rinderpest eradication, using a live attenuated Homologous PPRV vaccine (Nigeria 75/1 strain)."
    },
    2200: {
        "topic": "VPM True/False Section II Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This section tests absolute factual recall about disease prevention, diagnostics, and zoonotic transmission.",
        "Pathogenesis_Deep": "Focus areas in this section include the zoonotic diseases, their specific vectors, and the legally mandated control measures under Indian law.",
        "Why_Not": "Even if a statement is partially correct, a single false epidemiological claim makes the entire statement FALSE.",
        "Wow_Approach": "Memorize the zoonotic tetrad: Anthrax, Brucellosis, Leptospirosis, and Rabies as the 'Big Four' occupational zoonoses of veterinarians in India."
    },
    2209: {
        "topic": "Bovine Trichomoniasis - Timing of Abortion",
        "Core_Anatomy": "Fetal trophoblast and uterine lumen.",
        "Pathogenesis_Immediate": "The statement 'Trichomoniasis causes late-term abortion in cattle' is FALSE. Bovine Trichomoniasis causes EARLY embryonic death and abortion (first trimester, typically before 16 weeks).",
        "Pathogenesis_Deep": "Tritrichomonas foetus is a venereal protozoan transmitted during natural mating. The organism colonizes the preputial smegma of bulls and the vaginal mucosa of cows. It does NOT cross the placenta to infect the fetus directly. Instead, it causes severe endometritis (inflammation of the uterine lining), creating a hostile environment that prevents proper embryo implantation or causes very early embryonic death and absorption, or abortion before 16 weeks.",
        "Why_Not": "Late-term abortion (after 5 months) is more characteristic of Brucellosis, Leptospirosis, and mycotic abortion. Trichomoniasis is strictly an early pregnancy loss disease.",
        "Wow_Approach": "Because cows abort so early that the fetus is often reabsorbed rather than expelled, the herd shows 'repeat breeding' (cows returning to estrus every 3-4 cycles) rather than visible abortions, making diagnosis challenging."
    },
    2210: {
        "topic": "BVD - Persistent Infection",
        "Core_Anatomy": "Fetal immune system (thymus and bone marrow).",
        "Pathogenesis_Immediate": "Persistent Infection (PI) is the unique immunological state classically matched to Bovine Viral Diarrhea Virus (BVD).",
        "Pathogenesis_Deep": "If a pregnant cow is infected with non-cytopathic BVD virus (ncpBVD) between days 40-120 of gestation, the virus crosses the placenta and infects the developing calf. At this stage, the fetal immune system is immature and cannot recognize the virus as 'foreign.' The calf is born immunotolerant to the specific BVD strain: it produces no antibodies against it and sheds massive amounts of virus for its entire life. These PI calves are the primary reservoir and driving engine of all BVD outbreaks.",
        "Why_Not": "Persistent Infection is a concept unique to Pestivirus family (BVD in cattle, BVDV-2, Border Disease). The Lasota vaccine is the live attenuated vaccine for Newcastle disease (Ranikhet), not BVD.",
        "Wow_Approach": "A single PI calf in a herd can infect every pregnant cow and create an explosive new cohort of PI calves the following year, causing the infection to spiral. Identifying and removing all PI animals is the cornerstone of BVD eradication programs."
    },
    2211: {
        "topic": "Hydatid Disease - Casoni Test",
        "Core_Anatomy": "Host immune system (Type I hypersensitivity).",
        "Pathogenesis_Immediate": "The Casoni test is a classic intradermal skin test used for the diagnosis of Hydatid Disease (Cysticercosis from Echinococcus granulosus).",
        "Pathogenesis_Deep": "In Hydatid Disease, a person (or animal) ingests Echinococcus eggs shed in dog feces. The oncospheres develop into fluid-filled hydatid cysts in the liver/lungs. In the Casoni test, 0.2 mL of sterilized hydatid cyst fluid is injected intradermally. If the patient has been exposed to Echinococcus antigens (either from an active cyst or past exposure), sensitized IgE antibodies on mast cells in the skin will react immediately, producing a classic wheal-and-flare response (Type I hypersensitivity) within 20-30 minutes.",
        "Why_Not": "Babesiosis is a tick-borne blood parasite diagnosed by blood smear microscopy. The Casoni test is strictly for Echinococcus/Hydatid disease.",
        "Wow_Approach": "The Casoni test has poor specificity (false positives from Taenia, Fasciola, or even ascariasis cross-reactions) and has largely been replaced by ELISA-based serology for clinical diagnosis, though it remains a classic board exam topic."
    },
    2212: {
        "topic": "Ranikhet Disease (Newcastle) - Lasota Vaccine",
        "Core_Anatomy": "Avian respiratory and GI epithelium.",
        "Pathogenesis_Immediate": "Ranikhet Disease (Newcastle Disease) is specifically associated with the live attenuated Lasota vaccine as its most widely used lentogenic strain vaccine.",
        "Pathogenesis_Deep": "Newcastle Disease Virus (NDV) is an Avulavirus classified by pathotype: lentogenic (mild), mesogenic (moderate), and velogenic (highly fatal). The Lasota strain is a lentogenic strain that safely replicates in the respiratory epithelium of vaccinated birds, stimulating strong mucosal and humoral immunity. It is administered via drinking water, eye drop, or coarse spray. A single dose provides approximately 2-3 months of protection, requiring booster intervals.",
        "Why_Not": "Respiratory Syncytial Virus (RSV) is a bovine/human pathogen, not avian. Cysticercosis (Taenia solium) is not associated with the Lasota vaccine.",
        "Wow_Approach": "Because NDV mutates rapidly under immune pressure, vaccine strain matching must be regularly updated. If a flock vaccinated with Lasota still breaks with Newcastle, test the outbreak strain for antigenic drift away from the vaccine prototype."
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
