import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2131: {
        "topic": "Classical Swine Fever vs African Swine Fever",
        "Core_Anatomy": "Lymphoid tissue, vasculature, and leukocytes.",
        "Pathogenesis_Immediate": "Classical Swine Fever (CSF/Hog Cholera) is a Pestivirus, while African Swine Fever (ASF) is an Asfivirus—these are distinct diseases requiring different differential diagnoses.",
        "Pathogenesis_Deep": "CSF (caused by a Flavivirus-like Pestivirus) causes hemorrhagic disease with a classic 'button ulcer' in the cecum/colon and severe lymphopenia. ASF (caused by the unique Asfivirus, the only DNA arbovirus) is transmitted by Ornithodoros soft-bodied ticks and is currently catastrophic globally. Both cause severe hemorrhagic signs but ASF causes a distinctive 'Spanish flag' sign (cyanotic ear tips), and crucially ASF has NO vaccine while CSF has an effective lapinized live vaccine.",
        "Why_Not": "Swine flu (H1N1 Influenza A) is a respiratory disease and does NOT cause hemorrhagic signs. CSF vs ASF requires PCR for definitive differentiation.",
        "Wow_Approach": "If a pig herd has 100% mortality with severe hemorrhages and no response to any antibiotic, IMMEDIATELY suspect ASF and notify authorities—it is an OIE-listed disease with catastrophic economic consequences."
    },
    2132: {
        "topic": "EIA - Anemia Classification (VPM Repeated)",
        "Core_Anatomy": "Peripheral blood erythrocytes.",
        "Pathogenesis_Immediate": "Equine Infectious Anemia causes a Normocytic, Normochromic anemia.",
        "Pathogenesis_Deep": "Because horses do not release reticulocytes into peripheral blood during regenerative responses, the RBCs that remain in circulation after immune-mediated hemolysis in EIA are of normal size (normocytic) and normal hemoglobin concentration (normochromic). This is called a non-regenerative anemia when viewed on a blood smear, even though the bone marrow is actually responding.",
        "Why_Not": "Iron-deficiency anemia (e.g., in blood-sucking parasite infestations) causes microcytic, hypochromic anemia. Hemolytic anemia in dogs/cats causes macrocytic, hypochromic changes due to reticulocytosis.",
        "Wow_Approach": "The gold standard diagnostic for EIA is the Coggins Test (AGID); a positive result requires immediate life-long quarantine of the horse."
    },
    2133: {
        "topic": "Avian Pathology - IBD vs Egg Drop (VPM Repeated)",
        "Core_Anatomy": "Bursa of Fabricius.",
        "Pathogenesis_Immediate": "A drop in egg production in layers is NOT a feature of Infectious Bursal Disease (IBD/Gumboro Disease).",
        "Pathogenesis_Deep": "IBD exclusively targets the Bursa of Fabricius of young, growing chicks (3-6 weeks old). The bursa naturally involutes and disappears as the bird reaches sexual maturity. Adult laying hens have no bursa, therefore they cannot be clinically infected by IBD and will not experience an egg drop due to this disease.",
        "Why_Not": "Newcastle Disease, ILT (Infectious Laryngotracheitis), and Infectious Bronchitis all devastate adult laying flocks, causing severe egg drops, shell abnormalities, and internal laying.",
        "Wow_Approach": "IBD destroys B-lymphocytes in young birds permanently, causing immunosuppression that renders subsequent vaccination attempts (e.g., Newcastle vaccine) completely ineffective."
    },
    2134: {
        "topic": "Surra (Trypanosoma evansi) - Susceptible Species",
        "Core_Anatomy": "Erythrocytes and plasma (extracellular hemoflagellate).",
        "Pathogenesis_Immediate": "Among the listed options, the Elephant is highly susceptible to Surra (Trypanosoma evansi infection).",
        "Pathogenesis_Deep": "Trypanosoma evansi (causative agent of Surra) is transmitted by biting flies (Tabanus). It is not species-specific and infects a wide range of hosts. However, working elephants are classically and severely affected in Asian countries (India, Thailand). The disease causes progressive weight loss, severe anemia, edema, and hind-limb paralysis in elephants, and is often fatal if untreated with Suramin or Melarsomine.",
        "Why_Not": "Goats and buffalo are also susceptible to Surra but have higher natural resistance. Horses (Murra/Mal de Caderas) and camels are also highly susceptible. The question context points specifically to elephants.",
        "Wow_Approach": "Surra is the most important protozoan disease of working animals in Asia. Field diagnosis in elephants is done by examining blood smears (thin and thick smears) under a microscope for the characteristic undulating membrane flagellate."
    },
    2135: {
        "topic": "Surra Susceptible Species - Horse",
        "Core_Anatomy": "Erythrocytes and plasma.",
        "Pathogenesis_Immediate": "The Horse is also highly susceptible to Surra (Trypanosoma evansi), developing the lethal form known as 'Murra' in horses.",
        "Pathogenesis_Deep": "In horses, Trypanosoma evansi causes a rapidly progressive, often fatal disease characterized by anemia, edema, urticaria, keratoconjunctivitis, and progressive neurological signs (circling, paralysis). The disease has a high case fatality rate in horses without treatment. Suramin is the drug of choice.",
        "Why_Not": "Not all species show equal susceptibility; horses and camels are more severely affected compared to cattle, which often remain subclinically infected.",
        "Wow_Approach": "Unlike Dourine (T. equiperdum, sexually transmitted), Surra (T. evansi) is transmitted mechanically by biting flies and can affect any species at the fly's next feeding location."
    },
    2136: {
        "topic": "Avian IBD - Age of Susceptibility",
        "Core_Anatomy": "Bursa of Fabricius.",
        "Pathogenesis_Immediate": "Severe, clinical Infectious Bursal Disease (IBD/Gumboro) characteristically affects chicks at 3-6 weeks of age.",
        "Pathogenesis_Deep": "The Bursa of Fabricius is maximally active (producing B-lymphocytes) between 3-6 weeks of age in chickens. Before 3 weeks, maternal antibodies protect the chick. After 6 weeks, the bursa begins to involute and becomes a less dominant target organ. IBD virus therefore has a narrow window of maximum pathogenicity coinciding with peak bursal activity, causing devastating lymphocyte depletion during this critical 3-6 week period.",
        "Why_Not": "Newcastle Disease can affect birds of all ages. Fowl Pox affects adult birds seasonally (via mosquitoes). Only IBD has this specific 3-6 week age targeting.",
        "Wow_Approach": "Chicks vaccinated at day 1 against IBD may be protected, but if maternal antibodies interfere with the vaccine, there is a 'window of susceptibility' between 2-3 weeks when the maternal immunity has waned but vaccine immunity hasn't developed."
    },
    2137: {
        "topic": "Avian Pathology - Marek's Disease 'Pearl Eye'",
        "Core_Anatomy": "Iris (ocular lymphoma).",
        "Pathogenesis_Immediate": "'Pearl Eye' (ocular Marek's Disease) is a characteristic feature of Marek's Disease in poultry.",
        "Pathogenesis_Deep": "Gallid alphaherpesvirus 2 (Marek's Disease Virus) is highly oncogenic, causing T-lymphocyte tumors. In the classic ocular form, neoplastic T-lymphocytes infiltrate the iris of the eye. This lymphomatous infiltration causes the normally round, uniform pupil to become irregular and jagged, and the iris loses its normal pigmentation, turning gray or white (resembling a pearl). This 'Pearl Eye' or 'Gray Eye' sign is pathognomonic for Marek's ocular lymphoma.",
        "Why_Not": "Ranikhet Disease (Newcastle) and Fowl Pox cause respiratory/cutaneous signs but not iris depigmentation.",
        "Wow_Approach": "Marek's disease is the most successfully controlled avian disease in the world. The Rispens CVI988 herpesvirus turkey vaccine induces strong cell-mediated immunity preventing tumor formation—it was the world's first commercially successful anti-cancer vaccine."
    },
    2139: {
        "topic": "Cestode Treatment in Dogs - Praziquantel",
        "Core_Anatomy": "Intestinal tapeworm tegument.",
        "Pathogenesis_Immediate": "The drug of choice for treating tapeworm (cestode) infections in dogs is Praziquantel.",
        "Pathogenesis_Deep": "Praziquantel is a synthetic isoquinoline-pyrazine anthelmintic. It acts by dramatically increasing the permeability of the tapeworm's tegument (outer surface) to calcium ions. The massive influx of calcium causes violent muscular tetanic contraction, rupturing the tegument and allowing the host's digestive juices to destroy the worm. It is effective against all major cestodes (Taenia, Echinococcus, Dipylidium) with a single oral dose.",
        "Why_Not": "Albendazole has moderate activity against some tapeworms, while Piperazine is strictly for roundworms (ascarids). Praziquantel remains the definitively superior cestodicidal drug.",
        "Wow_Approach": "Echinococcus granulosus (causing hydatid disease in humans) is the most important public health tapeworm in dogs. Regular deworming of all dogs with Praziquantel in endemic areas is essential to break the dog-sheep-human transmission cycle."
    },
    2140: {
        "topic": "Rabies Post-Exposure Prophylaxis (PEP) Schedule",
        "Core_Anatomy": "Systemic humoral and cell-mediated immunity.",
        "Pathogenesis_Immediate": "The WHO-recommended Post-Exposure Prophylaxis (PEP) schedule for rabies using inactivated cell-culture vaccines is: Days 0, 3, 7, 14, and 28.",
        "Pathogenesis_Deep": "Rabies PEP involves two critical components: (1) Immediate thorough wound washing and debridement (most critical step—water/soap for 15 minutes). (2) Passive immunization with Rabies Immunoglobulin (RIG) on Day 0, injected directly into and around the wound. (3) Active immunization with cell-culture vaccine on Days 0, 3, 7, 14, and 28 (Essen regimen) to build long-term neutralizing antibody titers. The injections must NEVER be skipped or delayed.",
        "Why_Not": "The older schedules (0, 3, 7, 14 with only 4 doses) or non-standard schedules do not achieve adequate antibody titers by day 14.",
        "Wow_Approach": "If the biting dog is captured alive, it must be kept under observation for 10 days. If the dog remains healthy after 10 days, it was not shedding rabies virus at the time of the bite, and PEP may be discontinued after the initial doses."
    },
    2141: {
        "topic": "Bovine Theileriosis - Tropical Species (India)",
        "Core_Anatomy": "Lymphocytes and erythrocytes.",
        "Pathogenesis_Immediate": "Theileria annulata is the primary species causing Tropical Theileriosis (the most economically significant Theileria) in cattle in India.",
        "Pathogenesis_Deep": "Theileria annulata is transmitted by Hyalomma ticks. It infects and transforms bovine lymphocytes (Koch's Blue Bodies/macroschizonts), causing severe lymphoproliferation. When the schizonts rupture and release merozoites into the bloodstream to invade erythrocytes (piroplasms), they cause hemolytic anemia. The disease is characterized by high fever, lymphadenopathy, severe anemia, and icterus. Buparvaquone (Butalex) is the specific antitheilerial drug of choice.",
        "Why_Not": "Theileria parva causes East Coast Fever (Africa). Theileria hirci affects small ruminants in India. T. mutans is a relatively benign bovine species. T. annulata is the principal pathogen in Indian cattle.",
        "Wow_Approach": "The live attenuated Schizont cell-culture vaccine (e.g., Raksha-T) provides excellent protection against T. annulata but must be stored in liquid nitrogen—field deployment logistics are the primary challenge to widespread use."
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
