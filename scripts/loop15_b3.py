import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1688: {
        "topic": "Avian Zoonoses - Psittacosis",
        "Core_Anatomy": "Respiratory tract and systemic macrophages.",
        "Pathogenesis_Immediate": "The classic zoonotic disease transmitted from pet psittacines (parrots, macaws, cockatiels) to humans is Psittacosis (also called Ornithosis or Parrot Fever).",
        "Pathogenesis_Deep": "Psittacosis is caused by the obligate intracellular bacterium Chlamydia psittaci. Infected birds shed the bacteria heavily in their feces and respiratory secretions. When the feces dry out, the elementary bodies aerosolize. If a human owner or veterinarian inhales this dust, the bacteria infect the alveolar macrophages, leading to severe, atypical, flu-like pneumonia that can be fatal if untreated.",
        "Why_Not": "Avian borreliosis (tick fever) is not directly transmitted to humans via aerosol. Crohn's disease is a human autoimmune bowel disease (though some link it to Mycobacterium avium paratuberculosis in cattle, not parrots).",
        "Wow_Approach": "Pet birds can be asymptomatic carriers for years, only shedding the bacteria when stressed (e.g., during transport or breeding). Always wear an N95 mask when cleaning the cage of a newly acquired parrot."
    },
    1689: {
        "topic": "Bovine Babesiosis - Hemoglobinuria",
        "Core_Anatomy": "Erythrocytes and renal glomeruli.",
        "Pathogenesis_Immediate": "The passage of dark red or 'Coffee-coloured' urine in cattle is highly characteristic of Babesiosis (Tick Fever / Redwater).",
        "Pathogenesis_Deep": "Babesia bigemina and Babesia bovis are tick-borne intraerythrocytic protozoan parasites. They actively replicate inside the cow's red blood cells and literally burst them open. This massive intravascular hemolysis releases huge amounts of free hemoglobin into the plasma. The hemoglobin passes through the renal glomeruli and oxidizes in the urine, turning it a dark red/brown 'coffee' color (Hemoglobinuria).",
        "Why_Not": "Trypanosomiasis (Surra) causes anemia but typically extravascular hemolysis (in the spleen), so there is no hemoglobinuria. Kennel cough is a respiratory disease in dogs.",
        "Wow_Approach": "To prove the coffee-colored urine is hemoglobin (intravascular hemolysis) and not myoglobin (muscle damage) or intact RBCs (hematuria), centrifuge the urine. If it stays dark brown, it's hemoglobin/myoglobin. Then check the blood serum: if the serum is pink/red, it's hemoglobinuria (Babesiosis)."
    },
    1690: {
        "topic": "Veterinary Dermatology - Scabies",
        "Core_Anatomy": "Epidermis (stratum corneum).",
        "Pathogenesis_Immediate": "The highly contagious, intensely pruritic skin disease known as Scabies is caused by the burrowing mite Sarcoptes scabiei.",
        "Pathogenesis_Deep": "Unlike surface-dwelling mites, female Sarcoptes mites physically tunnel into the stratum corneum of the epidermis to lay their eggs. The mite's feces and saliva trigger a massive Type IV delayed hypersensitivity reaction. This causes the animal to suffer from an overwhelming, maddening itch (pruritus), leading to severe self-excoriation, alopecia, and thick crusting, especially on the ear margins, elbows, and hocks.",
        "Why_Not": "Psoroptes and Chorioptes are non-burrowing surface mites. Demodex lives deep in the hair follicles and causes non-pruritic alopecia (unless secondarily infected).",
        "Wow_Approach": "Because the mites burrow deep, superficial skin scrapes will miss them 50% of the time. You must scrape the skin margin aggressively with a scalpel blade until capillary blood oozes to reliably catch a Sarcoptes mite."
    },
    1691: {
        "topic": "Ruminant Parasitology - Amphistomiasis",
        "Core_Anatomy": "Rumen, reticulum, and duodenum.",
        "Pathogenesis_Immediate": "The specific drug of choice for treating Amphistomiasis (Paramphistomosis / Stomach Flukes) in ruminants is Oxyclozanide.",
        "Pathogenesis_Deep": "Amphistomes (like Paramphistomum cervi) are conical flukes. The adults live harmlessly in the rumen, but the massive pathogenic damage occurs when thousands of immature flukes migrate through the duodenum and abomasum, causing severe erosive enteritis, fetid diarrhea, and 'bottle jaw'. Oxyclozanide is highly effective against both the adult flukes in the rumen and the deadly immature migrating flukes in the intestines.",
        "Why_Not": "Albendazole and Febantel are excellent for nematodes (roundworms) and tapeworms but have very poor efficacy against immature stomach flukes. Pyrantel is for small animal roundworms.",
        "Wow_Approach": "Finding a few adult conical flukes in the rumen on necropsy is considered a normal, incidental finding in grazing cattle; it is the migrating immatures in the duodenum that cause fatal disease."
    },
    1692: {
        "topic": "Veterinary Pharmacology - Tartar Emetic",
        "Core_Anatomy": "Bloodstream and systemic parasites.",
        "Pathogenesis_Immediate": "Tartar emetic (Potassium antimonyl tartrate) is historically used against the treatment of Schistosomiasis (blood flukes).",
        "Pathogenesis_Deep": "Before the advent of modern, safe anthelmintics like Praziquantel, heavy metal compounds containing antimony (like Tartar emetic) were the only drugs capable of killing Schistosoma species living in the mesenteric veins. The antimony selectively inhibits the fluke's phosphofructokinase enzyme, starving it of energy. However, the therapeutic index is incredibly narrow, and it often caused severe cardiac toxicity in the host.",
        "Why_Not": "Fascioliasis (liver fluke) is treated with Triclabendazole. Theileriosis is treated with Buparvaquone.",
        "Wow_Approach": "While historically important for Schistosomiasis, modern veterinary medicine has largely replaced Tartar emetic with Praziquantel due to the extreme risk of fatal antimony toxicity."
    },
    1693: {
        "topic": "Milk Adulteration - Nitrate Detection",
        "Core_Anatomy": "N/A - Public Health/Dairy Science.",
        "Pathogenesis_Immediate": "The presence of Nitrates in milk specifically indicates the adulteration of the milk with water (specifically, contaminated pond or ground water).",
        "Pathogenesis_Deep": "Pure, unadulterated cow's milk does NOT contain nitrates. If a dairyman fraudulently dilutes the milk to increase the volume, they often use cheap, accessible water sources like local ponds or shallow wells. These water sources are heavily contaminated with agricultural fertilizers (ammonium nitrate) and animal waste. Detecting nitrates via a diphenylamine test proves not only that water was added, but that the water was unsanitary.",
        "Why_Not": "Skimming removes fat (raising specific gravity). Adding fat does not introduce nitrates. Nitrates are the absolute chemical signature of environmental water contamination.",
        "Wow_Approach": "This is a classic forensic test: if a dairyman dilutes milk with pure distilled water, the nitrate test will be negative, but the lactometer reading (Specific Gravity) will drop from 1.030 to 1.020, revealing the fraud."
    },
    1694: {
        "topic": "Veterinary Jurisprudence - Animal Welfare Boards",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The major statutory bodies established under the Prevention of Cruelty to Animals (PCA) Act, 1960 are the Animal Welfare Board of India (AWBI) and the CPCSEA.",
        "Pathogenesis_Deep": "The PCA Act of 1960 created two massive regulatory pillars in India: (1) The AWBI, which oversees general animal welfare, shelter funding, and cruelty prevention. (2) The CPCSEA (Committee for the Purpose of Control and Supervision of Experiments on Animals), which specifically regulates and polices the ethical use of animals in laboratory research, ensuring the 3Rs (Replacement, Reduction, Refinement) are followed.",
        "Why_Not": "While the SPCA (Society for the Prevention of Cruelty to Animals) exists locally, the AWBI and CPCSEA are the specific apex national bodies formally established by the text of the 1960 Act.",
        "Wow_Approach": "No veterinary or medical college in India can legally conduct animal research without first establishing an IAEC (Institutional Animal Ethics Committee) that reports directly to the CPCSEA."
    },
    1695: {
        "topic": "Veterinary Jurisprudence - Bestiality (IPC 377)",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "Bestiality in animals is a criminal offense punishable under IPC Section 377.",
        "Pathogenesis_Deep": "Under the Indian Penal Code, Section 377 criminalizes 'carnal intercourse against the order of nature'. If a human commits sexual abuse against an animal, this is the specific statute used for prosecution. The veterinary forensic examination is critical; the vet must document physical trauma (lacerations, bleeding) and secure DNA evidence (semen swabs) to establish a chain of custody for the police.",
        "Why_Not": "IPC 420 is cheating/fraud. IPC 428 is mischief (killing/maiming animals). IPC 272 is adulteration of food.",
        "Wow_Approach": "Evidence collection in Section 377 cases must be pristine. Swabs must be air-dried and placed in paper envelopes (never plastic, which traps moisture and destroys DNA) before being handed to the magistrate."
    },
    1696: {
        "topic": "Courtroom Ethics - The Hostile Witness",
        "Core_Anatomy": "N/A - Legal Procedure.",
        "Pathogenesis_Immediate": "A witness who, on account of pressure, bribery, or coercion, changes their statement to side with the opposing party during a trial is legally termed a 'Hostile witness'.",
        "Pathogenesis_Deep": "In a veterinary negligence or cruelty case, the prosecution may call a veterinarian to the stand based on a necropsy report they wrote. If that veterinarian suddenly contradicts their own written report while testifying (perhaps because the defendant bribed or threatened them), the prosecuting lawyer will ask the judge to declare the veterinarian a 'hostile witness'. This allows the lawyer to cross-examine and aggressively question their own witness to expose the lie.",
        "Why_Not": "An Expert witness (like a specialized pathologist) is called purely for their technical opinion. A Common witness testifies to what they physically saw. A Hostile witness is one who intentionally betrays the party that called them.",
        "Wow_Approach": "Being declared a hostile witness as a veterinarian is a career-ending move. It invites a perjury investigation (IPC 193) and the revocation of your veterinary license by the State Council."
    },
    1697: {
        "topic": "VMD Objective Section - True/False Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces statements requiring absolute evaluation of clinical facts.",
        "Pathogenesis_Deep": "These questions often hinge on the difference between etiology and pathogenesis, or the presence of a single absolute word (always, never).",
        "Why_Not": "Partial correctness is not accepted.",
        "Wow_Approach": "Read the entire statement twice; the first half may be true, while the second half contains the fatal flaw."
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
