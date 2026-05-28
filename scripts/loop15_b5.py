import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1742: {
        "topic": "Mycotic Abortion - Bovine Aspergillosis",
        "Core_Anatomy": "Placentome and fetal skin.",
        "Pathogenesis_Immediate": "In bovine Aspergillosis, abortion is typically noticed during the late stages, primarily between 6 to 9 months of gestation.",
        "Pathogenesis_Deep": "Aspergillus fumigatus spores are inhaled from moldy hay and spread hematogenously to the gravid uterus. The fungus invades the placentome, causing severe necrotic placentitis. Because the placenta is a highly privileged, slow-reacting immune site, the fungal infection takes months to destroy enough placental tissue to cause fetal death. Consequently, the abortion occurs late in gestation (third trimester).",
        "Why_Not": "Tritrichomonas foetus causes early embryonic death (1-3 months). Campylobacter causes mid-term abortion (4-6 months). Mycotic abortions are classically late-term.",
        "Wow_Approach": "A pathognomonic finding on the aborted fetus is a severe, raised, ringworm-like mycotic dermatitis over the head and shoulders, caused by the fungus growing in the amniotic fluid."
    },
    1743: {
        "topic": "Bovine Anaplasmosis - Gall Sickness",
        "Core_Anatomy": "Erythrocyte margins and hepatic biliary system.",
        "Pathogenesis_Immediate": "The tick-borne disease Bovine Anaplasmosis is colloquially and clinically referred to as 'Gall Sickness'.",
        "Pathogenesis_Deep": "Anaplasma marginale is an intraerythrocytic rickettsial organism that localizes at the margin of the red blood cell. Unlike Babesia (which bursts the RBCs), Anaplasma causes the RBCs to be tagged for destruction by macrophages in the spleen and liver (extravascular hemolysis). Because the liver is overwhelmed with processing the massive amounts of bilirubin from the destroyed RBCs, the gallbladder becomes enormously distended with thick, granular, dark green bile—hence the term 'Gall Sickness'.",
        "Why_Not": "Ehrlichiosis causes pancytopenia in dogs. Listeriosis causes neurological signs. Q-fever causes abortion.",
        "Wow_Approach": "Unlike Babesiosis (Redwater), Anaplasmosis does NOT cause hemoglobinuria (red urine) because the hemolysis is extravascular, not intravascular."
    },
    1744: {
        "topic": "Ovine Dermatophilosis - Strawberry Foot Rot",
        "Core_Anatomy": "Coronary band and interdigital epidermis.",
        "Pathogenesis_Immediate": "Classic 'Strawberry foot rot' lesions in sheep are noticed in Dermatophilosis (caused by Dermatophilus congolensis).",
        "Pathogenesis_Deep": "Dermatophilus congolensis is an actinomycete bacterium that produces motile zoospores. During prolonged wet weather (which macerates the skin), the zoospores invade the epidermis of the lower limbs. They cause a severe exudative dermatitis. Thick, hard scabs form around the coronet and pastern. When these crusts are forcibly peeled off, the underlying bleeding, granulomatous granulation tissue looks exactly like the surface of a red strawberry.",
        "Why_Not": "Dermatophytosis (Ringworm) causes dry, scaly circular alopecia. Blastomycosis is a systemic fungal pneumonia. Footrot is caused by Dichelobacter nodosus (affecting the hoof horn, not just the skin).",
        "Wow_Approach": "Dermatophilosis on the back/fleece of the sheep is called 'Lumpy Wool', but when it specifically affects the lower limbs, it is termed 'Strawberry Foot Rot'."
    },
    1745: {
        "topic": "Systemic Mycoses - Coccidioidomycosis",
        "Core_Anatomy": "Pulmonary parenchyma and long bones.",
        "Pathogenesis_Immediate": "Among domestic animals, the most susceptible species for clinically severe Coccidioidomycosis (Valley Fever) is the Dog.",
        "Pathogenesis_Deep": "Coccidioides immitis is a dimorphic soil fungus endemic to the arid deserts (e.g., Arizona, California). Dogs are highly susceptible because they actively sniff and dig in the dry dirt, inhaling massive numbers of arthroconidia. The fungus transforms into large spherules in the lungs, causing severe granulomatous pneumonia, and frequently disseminates to the long bones (causing painful osteomyelitis).",
        "Why_Not": "Cats are relatively resistant and usually only develop skin lesions. Pigs and small ruminants are rarely clinically affected.",
        "Wow_Approach": "If a dog that recently traveled to a desert region presents with a chronic, non-responsive harsh cough and shifting leg lameness, Coccidioidomycosis should be the top differential."
    },
    1746: {
        "topic": "Actinobacillosis - Wooden Tongue Treatment",
        "Core_Anatomy": "Lingual soft tissue and systemic circulation.",
        "Pathogenesis_Immediate": "The traditional and highly effective specific drug for treating 'Wooden Tongue' is intravenous Sodium Iodide.",
        "Pathogenesis_Deep": "Wooden Tongue is caused by Actinobacillus lignieresii, a Gram-negative bacterium that invades the soft tissues of the tongue via coarse feed abrasions, causing severe granulomatous fibrosis (hardening the tongue like wood). While modern antibiotics (like Streptomycin/Tetracycline) are used, IV Sodium Iodide acts uniquely by altering the granulomatous inflammatory response, actively dissolving the fibrotic capsules and allowing the tongue to regain mobility.",
        "Why_Not": "Potassium iodide is used orally, but IV administration of potassium is cardiotoxic (fatal). Therefore, only SODIUM iodide can be given safely as a rapid IV infusion.",
        "Wow_Approach": "Watch for signs of 'Iodism' during treatment: excessive tearing (epiphora), scaly skin (dandruff), and a dry hacking cough indicate you need to pause the iodide therapy."
    },
    1747: {
        "topic": "Vaccine Manufacturing - FMD Inactivant",
        "Core_Anatomy": "Viral RNA genome.",
        "Pathogenesis_Immediate": "The standard, highly effective inactivant used for the production of the Foot and Mouth Disease (FMD) vaccine is BEI (Binary Ethylenimine).",
        "Pathogenesis_Deep": "Historically, Formalin was used to kill the FMD virus for vaccines. However, Formalin cross-links surface proteins, which drastically altered the viral capsid (antigen) shape, leading to a weak immune response. BEI is vastly superior because it specifically targets and alkylates the viral RNA genome (destroying infectivity) while leaving the outer protein capsid structurally perfect and intact. This creates a highly immunogenic, safe vaccine.",
        "Why_Not": "Formalin damages the antigen. NaOH/Na2CO3 are strong alkalis used to disinfect premises, not for precision vaccine manufacturing.",
        "Wow_Approach": "Because BEI only damages RNA, it is also widely used for inactivating other critical RNA viruses like Rabies for modern cell-culture vaccines."
    },
    1748: {
        "topic": "Veterinary Epidemiology - Ring Vaccination",
        "Core_Anatomy": "Population-level immune barrier.",
        "Pathogenesis_Immediate": "The aggressive vaccination of all susceptible animals in a prescribed geographic area immediately surrounding a disease outbreak is called Ring Vaccination.",
        "Pathogenesis_Deep": "When a highly contagious, catastrophic disease (like FMD or Rinderpest) breaks out in a naive population, stamping out (culling) the infected herd is the first step. To prevent outward spread, epidemiologists draw a geographic 'ring' (e.g., a 10 km radius) around the index farm. Every susceptible animal within that ring is immediately vaccinated. This creates an impenetrable 'firebreak' of immune animals that the virus cannot cross.",
        "Why_Not": "Frontline vaccination protects borders. Mass vaccination covers an entire country regardless of outbreak loci.",
        "Wow_Approach": "Ring vaccination was the exact epidemiological strategy used by the WHO and WOAH to successfully eradicate Smallpox in humans and Rinderpest in cattle globally."
    },
    1749: {
        "topic": "Bovine Abortion - Neospora and BVDV Synergy",
        "Core_Anatomy": "Fetal brain/heart and maternal immune system.",
        "Pathogenesis_Immediate": "The protozoan Neospora caninum is highly notorious for enhancing and causing massive abortion storms in cattle, particularly when the herd is co-infected with BVDV.",
        "Pathogenesis_Deep": "Neospora caninum is an obligate intracellular protozoan (with dogs as the definitive host). It causes severe non-suppurative encephalomyelitis in the bovine fetus. While many cows can carry Neospora subclinically without aborting, co-infection with Bovine Viral Diarrhea Virus (BVDV) severely immunosuppresses the pregnant cow. This loss of cell-mediated immunity allows the latent Neospora bradyzoites to rapidly reactivate, cross the placenta, and kill the fetus.",
        "Why_Not": "Toxoplasma gondii causes massive abortion in sheep, but rarely affects cattle. Sarcocystis rarely causes primary abortion storms.",
        "Wow_Approach": "If a dairy herd experiences an explosive abortion storm with mid-term fetuses, always test for both BVDV and Neospora, as the viral immunosuppression is often the trigger for the protozoal abortion."
    },
    1750: {
        "topic": "Canine Ehrlichiosis - Breed Predisposition",
        "Core_Anatomy": "Monocytes, macrophages, and bone marrow.",
        "Pathogenesis_Immediate": "The breed classically known to be highly susceptible to the severe, chronic form of Canine Ehrlichiosis (Tropical Canine Pancytopenia) is the German Shepherd Dog (GSD).",
        "Pathogenesis_Deep": "Ehrlichia canis is a tick-borne rickettsial organism that infects circulating monocytes. While most dogs clear the acute infection or remain subclinical, German Shepherds have a specific, genetically driven cell-mediated immune defect regarding this pathogen. They fail to clear the organism, progressing to the severe chronic phase where the bone marrow is completely destroyed (aplastic anemia/pancytopenia), resulting in fatal hemorrhagic diathesis (bleeding out).",
        "Why_Not": "Spitz, Doberman, and Rottweiler can get the disease, but the fatal, profound bone marrow aplasia is overwhelmingly documented in the GSD.",
        "Wow_Approach": "If a German Shepherd presents with epistaxis (nosebleeds) and severe lethargy, immediately perform a blood smear to look for Ehrlichia morulae in the monocytes, and start Doxycycline before waiting for the PCR results."
    },
    1751: {
        "topic": "Laboratory Animal Medicine - Tuberculosis Model",
        "Core_Anatomy": "Pulmonary granulomas (Tubercles).",
        "Pathogenesis_Immediate": "In laboratory animal medicine and classical microbiological diagnostics, the Guinea Pig is the quintessential animal model for diagnosing and studying Mycobacterium tuberculosis.",
        "Pathogenesis_Deep": "Guinea pigs are exquisitely hypersensitive to human and bovine tuberculosis. Historically, before PCR and rapid culture systems were available, diagnosing TB in a human or cow involved injecting the suspect sputum or milk into a guinea pig. If the sample contained even a few viable bacilli, the guinea pig would develop massive, generalized miliary tuberculosis and die within 4 to 6 weeks, confirming the diagnosis.",
        "Why_Not": "Mice are highly resistant to standard TB. Chickens are used for Marek's/Newcastle research. Rabbits are used for syphilis and pyrogen testing.",
        "Wow_Approach": "Because of this extreme susceptibility, guinea pig colonies must be strictly protected from human caretakers who might be shedding subclinical TB."
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
