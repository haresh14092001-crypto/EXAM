import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1678: {
        "topic": "Canine Pediatrics - Ascariasis",
        "Core_Anatomy": "Small intestine and abdominal wall.",
        "Pathogenesis_Immediate": "A classic 'Pot-bellied' appearance in young puppies is pathognomonic for Chronic Parasitism (specifically Toxocara canis roundworms).",
        "Pathogenesis_Deep": "Toxocara canis is transmitted transplacentally and transmammary to virtually all puppies. The adult roundworms live in the small intestine, competing directly for nutrients (leading to stunted muscle growth/emaciation). However, the massive worm burden physically distends the bowel. Furthermore, the protein-losing enteropathy causes hypoalbuminemia, leading to mild ascites. This combination of intestinal distension, fluid, and poor abdominal muscle tone creates the classic 'pot-belly' on an otherwise skinny puppy.",
        "Why_Not": "Acute pneumonia causes dyspnea, not abdominal distension. Chronic bronchitis causes a harsh cough.",
        "Wow_Approach": "In severe infections, the sheer mass of roundworms can cause fatal intestinal impaction or intussusception. Deworming must start at 2 weeks of age, not 8 weeks."
    },
    1679: {
        "topic": "Bovine Mastitis - Contagious Pathogens",
        "Core_Anatomy": "Mammary gland and teat sphincter.",
        "Pathogenesis_Immediate": "Contagious bovine mastitis is primarily caused by Staphylococcus aureus (along with Streptococcus agalactiae and Mycoplasma bovis).",
        "Pathogenesis_Deep": "Mastitis pathogens are strictly classified by their source. 'Contagious' pathogens live ON the cow's udder skin or inside the gland. They are transmitted directly from cow to cow during milking via contaminated milking machine liners or the milker's hands. Staphylococcus aureus is notorious because it produces alpha-toxins that cause severe micro-abscessation and fibrosis deep in the udder tissue, walling itself off from systemic antibiotics and making it nearly impossible to cure.",
        "Why_Not": "Escherichia coli and Streptococcus uberis are 'Environmental' pathogens. They live in the bedding/feces and enter the teat canal between milkings. Streptococcus dysgalactiae is also primarily environmental.",
        "Wow_Approach": "To control contagious mastitis (S. aureus), you must use post-milking teat dips to kill bacteria transferred during milking. To control environmental mastitis (E. coli), you must keep the bedding clean and dry."
    },
    1680: {
        "topic": "Bovine Tuberculosis Diagnostics - The Stormont Test",
        "Core_Anatomy": "Cutaneous immune system (T-cell hypersensitivity).",
        "Pathogenesis_Immediate": "Tuberculosis in cattle can be highly specifically diagnosed using the Stormont test.",
        "Pathogenesis_Deep": "The standard Single Intradermal (SID) tuberculin test often yields false positives (due to exposure to atypical environmental mycobacteria). The Stormont test increases specificity. It involves giving a primary intradermal injection of Bovine PPD, and then giving a SECOND injection at the exact same site 7 days later. The skin thickness is read 24 hours after the second injection. An increase of >5mm confirms true Mycobacterium bovis infection because the first injection heavily primed the local memory T-cells.",
        "Why_Not": "The CMT (California Mastitis Test) detects somatic cells in milk. Mallein test is for Glanders in horses. Anergy is the failure of the immune system to respond.",
        "Wow_Approach": "The Stormont test is rarely used for routine herd screening because it requires three handling visits per cow, but it is the gold standard for resolving inconclusive reactors."
    },
    1681: {
        "topic": "Bovine Listeriosis - Cranial Neuropathy",
        "Core_Anatomy": "Brainstem and Cranial Nerves (V, VII, IX, X, XII).",
        "Pathogenesis_Immediate": "Cud dropping (quidding) accompanied by severe salivation and facial paralysis is a classic presentation of Listeriosis.",
        "Pathogenesis_Deep": "Listeria monocytogenes (often ingested from poorly fermented, rotting silage) enters the oral mucosa through micro-abrasions. It travels retrogradely up the Trigeminal nerve (CN V) directly into the brainstem, causing severe microabscessation (meningoencephalitis). This destroys the nuclei of the cranial nerves. Paralysis of CN V (mastication) causes cud dropping; CN VII (facial) causes a drooping ear/lip; CN IX/X (pharyngeal) causes inability to swallow (dysphagia and massive drooling).",
        "Why_Not": "Colibacillosis causes calf scours. Leptospirosis causes abortion and redwater. Ulcerative lymphangitis causes leg swelling. None of these cause unilateral cranial nerve paralysis.",
        "Wow_Approach": "Listeriosis is often called 'Circling Disease' because the unilateral brainstem lesion causes the cow to compulsively walk in circles toward the paralyzed side."
    },
    1682: {
        "topic": "Equine Glanders - Cutaneous Form (Farcy)",
        "Core_Anatomy": "Cutaneous lymphatics and respiratory tract.",
        "Pathogenesis_Immediate": "The cutaneous form of Glanders in horses is historically and clinically known as Farcy.",
        "Pathogenesis_Deep": "Glanders is a fatal, highly contagious, zoonotic disease caused by the bacterium Burkholderia mallei. It presents in three forms: Nasal, Pulmonary, and Cutaneous. The cutaneous form (Farcy) is characterized by severe purulent lymphangitis. Nodules ('farcy buds') develop along the course of the subcutaneous lymphatic vessels (typically on the hindlimbs). These nodules ulcerate and discharge highly infectious, sticky, yellow/honey-colored pus.",
        "Why_Not": "Epizootic lymphangitis is caused by a fungus (Histoplasma farciminosum). Strangles is caused by Streptococcus equi (lymph nodes of the head). Pseudoglanders is Melioidosis.",
        "Wow_Approach": "Glanders is a strict OIE notifiable disease. If a horse tests positive (via the Mallein test or CFT), treatment is legally prohibited due to the severe zoonotic risk; the horse must be euthanized and deeply buried or incinerated."
    },
    1683: {
        "topic": "OIE Disease Eradication - CBPP",
        "Core_Anatomy": "N/A - Global Epidemiology.",
        "Pathogenesis_Immediate": "The OIE (now WOAH) officially recognized India as free from Contagious Bovine Pleuropneumonia (CBPP) in 2007.",
        "Pathogenesis_Deep": "CBPP (caused by Mycoplasma mycoides subsp. mycoides) is a devastating respiratory disease of cattle causing massive fibrinous pneumonia and 'marbled' lungs. Due to aggressive stamping-out policies and movement restrictions, India successfully eradicated the disease. Achieving official OIE 'Freedom' status is critical because it immediately lifts international trade embargoes on the country's beef and dairy exports.",
        "Why_Not": "India is NOT free from Rabies or Bluetongue (both are highly endemic). India is also free from Rinderpest (eradicated globally in 2011). Contagious Caprine Pleuropneumonia (CCPP) is still present in Indian goat flocks.",
        "Wow_Approach": "A country cannot self-declare freedom from these major transboundary diseases; it requires years of rigorous sero-surveillance data submitted to and verified by the WOAH Scientific Commission."
    },
    1684: {
        "topic": "Rinderpest - Zebra Striping Pathognomonic Sign",
        "Core_Anatomy": "Colonic and rectal mucosa.",
        "Pathogenesis_Immediate": "In cattle, the necropsy finding of zones of hemorrhage and erythema running transversely along the colonic mucosa, creating a 'Zebra Striping' pattern, is pathognomonic for Rinderpest.",
        "Pathogenesis_Deep": "Rinderpest (Cattle Plague) was a devastating Morbillivirus. The virus had a massive tropism for lymphoid tissue and the gastrointestinal epithelium. It caused severe necrosis of the gut lining. In the large intestine and rectum, this necrosis presented as striking, parallel, transverse bands of bright red congestion and hemorrhage against the pale mucosa, perfectly mimicking the stripes of a zebra.",
        "Why_Not": "BVD (Bovine Viral Diarrhea) causes linear esophageal ulcers. FMD (Foot and Mouth Disease) causes oral/hoof vesicles. Only Rinderpest causes true Zebra striping in the colon.",
        "Wow_Approach": "Although Rinderpest is globally eradicated, this classic pathological lesion remains a heavily tested concept in veterinary board exams to ensure clinicians can recognize the disease if it were ever used as an agro-terrorism agent."
    },
    1685: {
        "topic": "Bluetongue - Ovine Orbivirus",
        "Core_Anatomy": "Vascular endothelium, oral mucosa, and coronary band.",
        "Pathogenesis_Immediate": "A non-contagious, insect-borne viral disease in sheep causing fever, severe lameness, and characteristic tongue cyanosis is Bluetongue.",
        "Pathogenesis_Deep": "Bluetongue is an Orbivirus transmitted exclusively by Culicoides biting midges (hence 'non-contagious' from sheep to sheep). The virus targets the vascular endothelium, causing severe vasculitis and thrombosis. This leads to massive edema and cyanosis of the tongue (which physically turns blue/purple), erosions of the oral mucosa, and severe inflammation of the coronary band of the hooves (coronitis), forcing the sheep to walk on its knees due to extreme lameness.",
        "Why_Not": "PPR (Peste des Petits Ruminants) is highly contagious via aerosol and primarily causes diarrhea and pneumonia. Maedi-Visna causes chronic wasting and dyspnea. FMD is contagious.",
        "Wow_Approach": "If you see a sheep with a swollen, protruding blue tongue and it refuses to stand (or 'knee-walks'), Bluetongue is the primary differential."
    },
    1686: {
        "topic": "Canine Parvovirus - Breed Predispositions",
        "Core_Anatomy": "Intestinal crypt cells and bone marrow.",
        "Pathogenesis_Immediate": "Certain black-and-tan breeds, specifically the Doberman Pinscher and the Rottweiler, are heavily genetically predisposed to severe, often fatal infections of Canine Parvoviral Enteritis (CPV-2).",
        "Pathogenesis_Deep": "While Parvovirus infects all dogs, Rottweilers, Dobermans, Pit Bulls, and German Shepherds exhibit a distinct immunodeficiency regarding CPV-2. Even with appropriate vaccination protocols, these breeds often fail to mount a sufficient humoral (IgG) immune response (vaccine non-responders). When infected, they suffer from much more profound neutropenia and hemorrhagic enteritis compared to a mixed-breed dog, leading to significantly higher mortality rates.",
        "Why_Not": "Pugs and Bulldogs are predisposed to Brachycephalic Airway Syndrome. Chippiparai and Rajapalayam are robust indigenous sighthounds. Labradors are predisposed to obesity and joint issues.",
        "Wow_Approach": "Because of this genetic susceptibility, Rottweilers and Dobermans should receive their final parvovirus booster at 16 to 20 weeks of age (rather than the standard 12-14 weeks) to ensure absolutely no maternal antibody interference blocks the vaccine."
    },
    1687: {
        "topic": "Avian Influenza - Highly Pathogenic Strains (HPAI)",
        "Core_Anatomy": "Avian respiratory, gastrointestinal, and nervous systems.",
        "Pathogenesis_Immediate": "The classic, highly lethal strain of Highly Pathogenic Avian Influenza (HPAI) that caused massive global panics and zoonotic deaths is H5N1.",
        "Pathogenesis_Deep": "Influenza A viruses are subtyped by their Hemagglutinin (H) and Neuraminidase (N) surface glycoproteins. H5 and H7 subtypes are unique because their hemagglutinin cleavage site contains multiple basic amino acids. This allows the virus to be cleaved (activated) by ubiquitous cellular proteases (like furin) found in ALL tissues of the bird's body, rather than just the respiratory/GI tract. This results in a catastrophic systemic infection with 100% mortality in poultry flocks within 48 hours.",
        "Why_Not": "H1N1 is the human/swine pandemic strain (Spanish Flu/Swine Flu). H5N1 is the quintessential, highly virulent avian strain.",
        "Wow_Approach": "A sudden, massive 'flock drop' (thousands of chickens dying overnight with cyanotic combs and subcutaneous hemorrhages on their shanks) is the hallmark of H5N1 HPAI, necessitating immediate reporting and depopulation."
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
