import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2078: {
        "topic": "Veterinary Jurisprudence - Mischief (IPC 428/429)",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The crime of 'Mischief' (intentional killing, maiming, or poisoning of livestock) is matched to IPC Section 428 and 429.",
        "Pathogenesis_Deep": "Under the IPC, Mischief (Section 425) becomes specifically penalized under Section 428 when the animal killed or maimed has a value of Rs. 10, and under Section 429 when the animal is a cattle/elephant of any value OR any other animal worth Rs. 50 or more. A veterinarian performing a post-mortem to determine if death was natural or caused by malicious poisoning provides the key forensic evidence for prosecution under these sections.",
        "Why_Not": "Section 377 is for bestiality. Section 272 is for adulteration of food for sale.",
        "Wow_Approach": "Any farm animal that dies suspiciously (e.g., entire flock of poultry found dead overnight) should prompt the farmer to immediately call the police and a veterinarian to preserve the GI contents for toxicological analysis under Section 428/429."
    },
    2079: {
        "topic": "Veterinary Jurisprudence - IPC 272 vs 273",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The adulteration of food or drink IS the act covered under IPC 272, while the selling of unfit/noxious food is covered under IPC 273.",
        "Pathogenesis_Deep": "These two sections are sequential and distinct. Section 272 penalizes the physical act of adulteration (mixing in the adulterant—e.g., adding formalin to milk). Section 273 penalizes the commercial act of selling that adulterated or noxious food. In a typical dairy fraud case, Section 272 catches the producer and Section 273 catches the retailer who knowingly sells the adulterated product.",
        "Why_Not": "Both sections can be applied simultaneously if the same person adulterates AND sells the product.",
        "Wow_Approach": "The maximum punishment under IPC 272/273 is 6 months imprisonment and/or a fine of Rs. 1000—relatively mild, which is why most enforcement relies on the PFA Act (Prevention of Food Adulteration Act) which carries heavier penalties."
    },
    2087: {
        "topic": "VPM - Preventive Medicine Introduction Header",
        "Core_Anatomy": "Epidemiology and population health.",
        "Pathogenesis_Immediate": "This header marks the beginning of the Veterinary Preventive Medicine module (VMD 412), covering the control, diagnosis, and eradication of bacterial, fungal, and rickettsial diseases.",
        "Pathogenesis_Deep": "VPM focuses on herd-level disease management, vaccination protocols, and the principles of epidemiology (source, route, host) rather than individual animal treatment.",
        "Why_Not": "Individual case treatment is covered in VMD Clinical Medicine. VPM focuses on population-level intervention.",
        "Wow_Approach": "Every VPM question should be approached with the epidemiological triad in mind: Agent, Host, and Environment."
    },
    2088: {
        "topic": "VPM Module Header",
        "Core_Anatomy": "Epidemiology and population health.",
        "Pathogenesis_Immediate": "This section covers Veterinary Preventive Medicine, emphasizing control strategies for major infectious diseases.",
        "Pathogenesis_Deep": "Control strategies include surveillance, quarantine, test-and-slaughter, vaccination, and vector control depending on the specific pathogen.",
        "Why_Not": "Treatment of individual animals is the domain of clinical medicine, not preventive medicine.",
        "Wow_Approach": "Stamping-out (depopulation) policies are only legally feasible for diseases with no treatment option and high zoonotic risk (e.g., Rabies, FMD outbreaks in clean countries)."
    },
    2090: {
        "topic": "VPM 412 - Bacterial/Fungal/Rickettsial Diseases Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This subsection specifically covers the epidemiology and control of bacterial, fungal, and rickettsial diseases at the herd level.",
        "Pathogenesis_Deep": "Bacterial diseases tested here include Anthrax, Brucellosis, Leptospirosis, and Tuberculosis. Fungal diseases include Ringworm (dermatophytosis) and Aspergillosis. Rickettsial diseases include Ehrlichiosis and Anaplasmosis.",
        "Why_Not": "Viral diseases (FMD, BVD, Rinderpest) are covered in a separate VPM viral diseases module.",
        "Wow_Approach": "For any rickettsial disease, the answer to 'drug of choice' is almost always Doxycycline or another Tetracycline."
    },
    2091: {
        "topic": "VPM Fill in the Blanks Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of epidemiological facts, control programs, and disease statistics.",
        "Pathogenesis_Deep": "This section specifically tests exact figures such as incubation periods, vaccination schedules, quarantine durations, and legislative dates.",
        "Why_Not": "Approximate answers are not acceptable in public health contexts.",
        "Wow_Approach": "Memorize the exact OIE incubation periods for major transboundary diseases as these are frequently tested in VPM fill-in-the-blanks."
    },
    2099: {
        "topic": "Avian Aspergillosis - Brooder Pneumonia",
        "Core_Anatomy": "Avian lower respiratory tract (air sacs and lungs).",
        "Pathogenesis_Immediate": "The condition known as 'Brooder Pneumonia' in young chicks is caused by Aspergillus fumigatus.",
        "Pathogenesis_Deep": "Aspergillus fumigatus spores are ubiquitous in the environment, particularly in moldy litter, feed, and bedding. When young chicks (brooder-age) inhale massive numbers of spores, the spores germinate and grow as septate hyphae in the thin, highly vascular air sacs and lung parenchyma. Because chicks have an immature immune system, they cannot contain the infection, resulting in rapidly fatal granulomatous pneumonia and air sacculitis. The air sacs develop thick, cheesy, greenish-gray plaques.",
        "Why_Not": "Bacterial pneumonia in poultry is caused by Pasteurella (fowl cholera) or Mycoplasma. Only Aspergillus causes the classic fuzzy white/gray mycotic plaques on the air sacs.",
        "Wow_Approach": "Brooder pneumonia is a management disease. Improving ventilation, reducing litter moisture, and using clean, dry wood shavings (not wood chips that can harbor moisture) is more important than any antifungal treatment."
    },
    2100: {
        "topic": "Leptospirosis - Multisystemic Pathology",
        "Core_Anatomy": "Renal tubules, hepatocytes, and meninges.",
        "Pathogenesis_Immediate": "Leptospirosis is associated with all of the following: Hepatic dysfunction, Renal dysfunction, and Meningitis.",
        "Pathogenesis_Deep": "Leptospira interrogans is a highly invasive spirochete. After entering the bloodstream, it disseminates to multiple organs. (1) Renal: The bacteria colonize the renal tubular epithelium, causing severe tubular nephritis, tubular necrosis, and interstitial nephritis, leading to azotemia and hemoglobinuria. (2) Hepatic: Hepatocellular damage causes hyperbilirubinemia (severe icterus). (3) Meningeal: CNS involvement can cause meningitis with headache, photophobia, and stiff neck.",
        "Why_Not": "This multisystem tropism is the reason Leptospirosis is so clinically challenging; the presentation varies widely by infecting serovar and host species.",
        "Wow_Approach": "In dogs, the serovar Icterohaemorrhagiae classically causes severe hepatic disease (Weil's Syndrome), while Canicola primarily causes renal disease."
    },
    2101: {
        "topic": "Bovine Listeriosis - Silage Connection",
        "Core_Anatomy": "Brainstem (Trigeminal nerve).",
        "Pathogenesis_Immediate": "Feeding of poor quality, rotting silage to cattle is directly associated with the occurrence of Listeriosis.",
        "Pathogenesis_Deep": "Listeria monocytogenes is a psychrotrophic (cold-tolerant) bacterium that flourishes in improperly fermented silage. Quality silage must reach a pH below 4.5 to inhibit Listeria growth. When silage pH remains above 5.5 (due to poor compaction, air leaks, or insufficient wilting), L. monocytogenes multiplies massively. Cattle feeding on this 'bad silage' near the face of the bunker/clamp ingest billions of bacteria, which penetrate oral mucosal abrasions and travel to the brainstem.",
        "Why_Not": "Brucellosis and Salmonellosis are not associated with silage quality but rather with contaminated water, feed, and contact with infected animals.",
        "Wow_Approach": "When a herd develops multiple 'Circling Disease' cases simultaneously, always physically inspect the silage being fed. Check the pH with a simple pH strip; values above 5.0-5.5 are highly suspicious."
    },
    2103: {
        "topic": "Bovine Listeriosis - Causative Agent MCQ",
        "Core_Anatomy": "Brainstem and cranial nerve nuclei.",
        "Pathogenesis_Immediate": "Among the listed options (Brucellosis, Anthrax, Listeriosis, Tuberculosis), the condition most directly linked to feeding poor-quality silage is Listeriosis.",
        "Pathogenesis_Deep": "Listeria monocytogenes thrives in high-pH silage. Cattle ingesting contaminated silage allow the bacteria to penetrate mucosal abrasions in the mouth, travel up the trigeminal nerve (CN V), and directly invade the brainstem, causing a severe unilateral meningoencephalitis. Affected cattle develop cranial nerve paralysis (drooping ear, dropped jaw, deviated tongue) and circle compulsively.",
        "Why_Not": "Anthrax is a soil-borne disease transmitted by spore ingestion or insect bites. Tuberculosis spreads via aerosol. Neither is directly associated with silage fermentation quality.",
        "Wow_Approach": "Remember: Listeria, Lactobacillus, and pH are the three keywords for understanding silage disease. When Lactobacillus fails to lower the pH, Listeria wins."
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
