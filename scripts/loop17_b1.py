import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1899: {
        "topic": "Porcine Erysipelas - Diamond Skin Lesions",
        "Core_Anatomy": "Cutaneous vascular endothelium.",
        "Pathogenesis_Immediate": "The acute form of Erysipelothrix rhusiopathiae infection is universally known as 'Diamond skin disease'.",
        "Pathogenesis_Deep": "When E. rhusiopathiae enters the pig's bloodstream, it causes a severe acute septicemia. The bacteria specifically target and damage the endothelial cells lining the small capillaries in the skin. This causes localized micro-thrombosis (clots) and vasculitis, cutting off blood supply to geometric sections of the skin. These infarcted areas present as pathognomonic, raised, purplish-red, rhomboid (diamond-shaped) plaques on the back and flanks.",
        "Why_Not": "Swine fever and African swine fever cause diffuse purple hemorrhages (cyanosis) on the ears and abdomen, not discrete diamond-shaped plaques.",
        "Wow_Approach": "If the pig survives the acute septicemia, the diamond plaques often become completely necrotic, turning black, and physically slough off like large scabs."
    },
    1900: {
        "topic": "Porcine Polyserositis - Glasser's Disease",
        "Core_Anatomy": "Serosal membranes (pleura, pericardium, peritoneum, meninges).",
        "Pathogenesis_Immediate": "Glasser's disease in young pigs is caused by the bacterium Haemophilus parasuis (recently reclassified as Glaesserella parasuis).",
        "Pathogenesis_Deep": "Glaesserella parasuis is an early colonizer of the upper respiratory tract in piglets. Under extreme stress (like weaning, mixing, or transport), the bacteria breach the mucosal barrier and enter the bloodstream. They have a massive tropism for serosal surfaces. They trigger a severe fibrinous polyserositis, causing the lungs, heart, and intestines to be covered in thick, white, 'bread-and-butter' sheets of fibrin. It also frequently crosses the blood-brain barrier, causing fibrinous meningitis.",
        "Why_Not": "Erysipelothrix causes arthritis and endocarditis, not massive fibrinous polyserositis. Campylobacter causes swine dysentery (GI).",
        "Wow_Approach": "On necropsy, finding thick, stringy fibrin gluing the heart to the pericardial sac (fibrinous pericarditis) in a recently weaned piglet is highly suggestive of Glasser's disease."
    },
    1901: {
        "topic": "Bovine Bacillary Hemoglobinuria - Red Water Disease",
        "Core_Anatomy": "Hepatic parenchyma and erythrocytes.",
        "Pathogenesis_Immediate": "The highly fatal condition known as 'Red water disease' (Bacillary Hemoglobinuria) is caused by Clostridium haemolyticum (also known as Clostridium novyi Type D).",
        "Pathogenesis_Deep": "Clostridium haemolyticum spores lay dormant in the Kupffer cells of the bovine liver. When the liver is physically damaged and made anaerobic (most commonly by migrating Fasciola hepatica liver flukes), the spores germinate. The vegetative bacteria secrete large amounts of Beta toxin (phospholipase C). This toxin destroys red blood cell membranes, causing massive intravascular hemolysis. The resulting severe hemoglobinuria turns the urine dark red, hence 'Red water disease'.",
        "Why_Not": "Clostridium chauvoei causes Black quarter (muscle necrosis). Clostridium septicum causes Malignant edema. Only C. haemolyticum/novyi Type D causes classic Bacillary Hemoglobinuria.",
        "Wow_Approach": "Necropsy of a cow that died from Red Water Disease will invariably reveal a single, massive, pale necrotic infarct in the liver where the fluke migration triggered the clostridial germination."
    },
    1903: {
        "topic": "Veterinary Jurisprudence - IPC Section 377 (Bestiality)",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The crime of Bestiality is punishable under Section 377 of the Indian Penal Code.",
        "Pathogenesis_Deep": "Section 377 criminalizes 'unnatural offenses', specifically any voluntary carnal intercourse against the order of nature with any man, woman, or animal. In veterinary forensic medicine, a veterinarian may be called as an expert witness to testify on physical trauma found on an animal's genitalia or rectum, or to collect seminal fluid/DNA swabs for the forensic laboratory.",
        "Why_Not": "Section 366 deals with kidnapping. Section 388 deals with extortion. Section 355 deals with assault.",
        "Wow_Approach": "Veterinarians must never declare 'guilt' on a post-mortem report; they must strictly state 'findings are consistent with forced penetration/trauma' and allow the magistrate to determine the legal guilt under Section 377."
    },
    1905: {
        "topic": "Veterinary Jurisprudence - IPC Section 272 (Food Adulteration)",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The adulteration of food or drink (including milk and meat) intended for sale is a criminal offense under IPC Section 272.",
        "Pathogenesis_Deep": "Under the Indian Penal Code, Section 272 specifically penalizes anyone who adulterates any article of food or drink so as to make such article noxious, knowing it is likely to be sold as food. This is highly relevant to veterinarians acting as meat inspectors or dairy officers. Examples include adding urea to milk, selling meat from animals that died of natural diseases (not slaughtered), or artificially injecting water into meat to increase its sale weight.",
        "Why_Not": "Section 273 deals with the actual SALE of the noxious food. Section 272 deals with the ACT of adulterating it.",
        "Wow_Approach": "If a veterinarian catches a dairyman adding pond water containing nitrates to milk, the dairyman is charged under IPC 272, and the veterinarian's chemical analysis (diphenylamine test) forms the core of the prosecution's evidence."
    },
    1907: {
        "topic": "Veterinary Forensics - Modes of Somatic Death",
        "Core_Anatomy": "Brain, Lungs, and Heart (The Vital Tripod).",
        "Pathogenesis_Immediate": "In forensic pathology, somatic death beginning at the brain is termed Coma; at the lungs is Asphyxia; and at the heart is Syncope.",
        "Pathogenesis_Deep": "Somatic death is the irreversible failure of the 'Vital Tripod' (Bichat's Tripod: Brain, Heart, Lungs). (1) If the primary failure is the Brain (e.g., severe blunt force trauma to the skull, rabies encephalitis), the mode of death is Coma. (2) If the primary failure is the Lungs (e.g., drowning, strangulation, or severe pneumonia), the mode of death is Asphyxia. (3) If the primary failure is the Heart (e.g., cardiac tamponade, massive hemorrhage, or ionophore toxicity), the mode of death is Syncope.",
        "Why_Not": "Cyanosis is a clinical sign of hypoxia, not a mode of death itself.",
        "Wow_Approach": "Determining the primary mode of death is crucial in a forensic necropsy to reconstruct the timeline and cause of an animal's demise for a court case."
    },
    1908: {
        "topic": "Veterinary Jurisprudence - Cattle Trespass Act",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The Cattle Trespass Act was historically implemented in India in the year 1871.",
        "Pathogenesis_Deep": "The Cattle Trespass Act of 1871 was enacted to provide for the impounding of cattle doing damage to public roads, canals, or private agricultural crops. It established local cattle pounds (kanji houses). If a farmer's crop is destroyed by a neighbor's straying cattle, the farmer can seize the cattle and send them to the pound. The owner must pay a statutory fine to release them. This act was critical in reducing rural violence over crop destruction.",
        "Why_Not": "1860 is the year the Indian Penal Code (IPC) was drafted. 1871 is the specific year for the Cattle Trespass Act.",
        "Wow_Approach": "Veterinarians are often involved in these cases when impounded cattle suffer from starvation, disease, or cruelty while held in the government pounds, requiring welfare assessments."
    },
    1909: {
        "topic": "VMD Objective Section - True/False Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces statements requiring absolute evaluation of clinical or legal facts.",
        "Pathogenesis_Deep": "These questions often hinge on the difference between etiology and pathogenesis, or the presence of a single absolute word (always, never).",
        "Why_Not": "Partial correctness is not accepted.",
        "Wow_Approach": "Read the entire statement twice; the first half may be true, while the second half contains the fatal flaw."
    },
    1920: {
        "topic": "Veterinary Jurisprudence - The Dourine Act",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The Dourine Act, a specific piece of legislation targeting an equine venereal disease, was enacted in the year 1910.",
        "Pathogenesis_Deep": "Dourine is a highly fatal, sexually transmitted disease of horses and donkeys caused by the protozoan Trypanosoma equiperdum. Because it severely threatened the breeding programs of military cavalry mounts, the British Indian government passed the Dourine Act of 1910. This act gave veterinary inspectors the power to legally mandate the castration of infected stallions or the immediate destruction of infected mares without the owner's consent.",
        "Why_Not": "The Poisons Act was 1919. The Glanders and Farcy Act was 1899. The Dourine Act is strictly 1910.",
        "Wow_Approach": "Unlike Surra (caused by Trypanosoma evansi), which is transmitted by biting flies, Dourine is strictly venereal, making legal control of breeding animals the only effective method of eradication."
    },
    1922: {
        "topic": "Ruminant Parasitology - Haemonchosis",
        "Core_Anatomy": "Abomasum and systemic erythrocytes.",
        "Pathogenesis_Immediate": "Haemonchosis (infection with Haemonchus contortus, the Barber's pole worm) is universally matched with profound anemia and 'Bottle Jaw'.",
        "Pathogenesis_Deep": "Haemonchus contortus is a voracious blood-sucking nematode that resides exclusively in the abomasum of sheep and goats. It uses a small oral lancet to pierce the mucosal vessels and continuously suck whole blood. A heavy infection of thousands of worms can drain significant portions of the animal's total blood volume daily. This leads to a profound, life-threatening hemorrhagic anemia. The massive loss of serum proteins (hypoproteinemia) causes severe dependent edema, classically presenting as a fluid swelling under the mandible ('Bottle Jaw').",
        "Why_Not": "Unlike Ostertagia or Trichostrongylus (which primarily cause diarrhea and weight loss), Haemonchus is characterized by severe anemia; affected sheep often have completely white ocular mucous membranes but normal pelleted feces (no diarrhea).",
        "Wow_Approach": "The FAMACHA scoring system was specifically designed to selectively target and treat only sheep showing clinical anemia (pale conjunctiva) to slow the rampant development of anthelmintic resistance in Haemonchus."
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
