import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    110: {
        "topic": "Zoo Animal Management - Velvet Antler, Marsupials, Crop Milk",
        "Core_Anatomy": "Marsupial pouch (marsupium), cervid antler velvet (vascular periosteum), and the pigeon crop (ingluvies).",
        "Pathogenesis_Immediate": "Key zoo/wild animal anatomy: Velvet is the vascular, nerve-rich skin covering growing antlers in deer; Marsupials carry young in a pouch (marsupium); Crop milk is a protein/fat-rich secretion from the crop epithelium of pigeons and flamingos for neonatal feeding.",
        "Pathogenesis_Deep": "Antler velvet is a unique rapidly growing tissue (up to 2.5 cm/day) supplied by a complex vascular periosteum. When antler growth is complete, testosterone triggers velvet stripping. In marsupials, the underdeveloped neonate (joey) is born after a very short gestation (e.g., Kangaroo: 33 days) and migrates to the pouch, attaching to a teat for 6-8 months. Crop milk in pigeons is produced by prolactin-stimulated desquamation of crop epithelial cells, rich in protein (17%) and fat (9%).",
        "Why_Not": "Crop milk is unique to pigeons, doves, and flamingos among birds. It differs from mammalian milk by lacking lactose and calcium and being produced by epithelial cell desquamation rather than glandular secretion.",
        "Wow_Approach": "Velvet antler is used in traditional medicine (Korea/China) and is harvested under anaesthesia in deer farms. During velvet removal, the antler base must be tightly ligated before cutting to prevent haemorrhage. Improper velvet harvesting is classified as cruelty under the PCA Act and WPA 1972."
    },
    111: {
        "topic": "Indian Wildlife - Royal Bengal Tiger (Sunderbans) and Gir Lion",
        "Core_Anatomy": "Tiger (Panthera tigris tigris) and Asiatic Lion (Panthera leo persica) — felid carnivore anatomy.",
        "Pathogenesis_Immediate": "The Royal Bengal Tiger inhabits the Sunderbans mangrove forest (India/Bangladesh). The Asiatic Lion is exclusively found in Gir National Park, Gujarat. Both are Schedule I protected species under WPA 1972.",
        "Pathogenesis_Deep": "Sunderbans Tiger population: ~100 tigers in the world's largest mangrove delta. Tigers here are uniquely adapted to saltwater swimming. The Gir Asiatic Lion population has recovered from ~20 lions in 1893 to ~600+ currently, representing one of the greatest conservation success stories in Asia. Both are managed under Project Tiger (1973) and Project Lion (2020) respectively.",
        "Why_Not": "The African Lion (Panthera leo leo) is found in sub-Saharan Africa; the Asiatic Lion is a distinct subspecies. The Bengal Tiger (P.t. tigris) is the national animal of India; the Siberian Tiger (P.t. altaica) is the largest subspecies. Indian zoo management must house these species under CZA (Central Zoo Authority) minimum space norms.",
        "Wow_Approach": "CZA (Central Zoo Authority) minimum cage dimensions for large felids: Tiger/Lion — 1000 sq.m outdoor + 40 sq.m indoor per pair. Disease threats: Canine Distemper Virus (CDV) and Feline Panleukopaenia Virus are the two biggest infectious threats to wild felid populations."
    },
    113: {
        "topic": "Pet Bird Identification Techniques and Police Dogs",
        "Core_Anatomy": "Avian microchip placement site (pectoral muscle), and the canine olfactory mucosa (300 million olfactory receptors).",
        "Pathogenesis_Immediate": "Pet bird identification uses leg bands (rings), microchips (implanted in the pectoral muscle), and DNA feather analysis. Police dogs (K9 units) trained for law enforcement are called 'Police Dogs' or 'Service Dogs'; the specific term is 'K9' unit.",
        "Pathogenesis_Deep": "Microchipping in birds: A 2.12mm ISO-standard transponder is implanted into the left pectoral muscle under local anaesthesia. Leg banding: Closed bands (applied at hatching) or open bands (applied at any age) contain the year, breeder code, and individual number. DNA sexing using feather pulp or blood is the only reliable sexing method for monomorphic species (African Grey Parrot, many parakeets).",
        "Why_Not": "Tattooing (wing web) is used for poultry flock identification, not individual pet bird identification. Ear notching is used for cattle and pigs. Microchipping of the pectoral muscle is preferred over subcutaneous microchipping in birds (used in mammals) because birds lack sufficient subcutaneous fat.",
        "Wow_Approach": "Under the Wildlife Protection Act 1972, all species of parrots native to India (e.g., Rose-ringed Parakeet, Alexandrine Parakeet) are Schedule IV protected — keeping them as pets is illegal in India. However, exotic species (African Grey, Macaws, Cockatoos) bred in captivity with valid documentation can be legally kept."
    },
    114: {
        "topic": "Canine Ehrlichiosis and Zoonotic Diseases of Pet Animals",
        "Core_Anatomy": "Canine monocytes/macrophages and platelets (Ehrlichia target cells); avian proventriculus (grinding organ in birds).",
        "Pathogenesis_Immediate": "Monocytosis in dogs is a characteristic haematological feature of Ehrlichiosis (*Ehrlichia canis*), a tick-borne rickettsial disease causing thrombocytopenia, fever, anorexia, and lymphadenopathy.",
        "Pathogenesis_Deep": "E. canis is transmitted by the Brown Dog Tick (*Rhipicephalus sanguineus*). The bacteria infect monocytes and macrophages, forming intracytoplasmic clusters (morulae). The infected cells release pro-inflammatory cytokines, causing immune-mediated platelet destruction (thrombocytopenia). Chronic Ehrlichiosis causes pancytopenia from bone marrow suppression, which is often fatal if untreated.",
        "Why_Not": "Babesiosis (Babesia canis) causes haemolytic anaemia with regenerative response and haemoglobinuria, not monocytosis. Salmonellosis in dogs causes acute gastroenteritis with neutrophilia and left shift. Kennel Cough (Bordetella bronchiseptica) causes respiratory signs with lymphocytosis.",
        "Wow_Approach": "Diagnose Ehrlichiosis with a blood smear (morulae in monocytes — seen in only 4% of cases) or PCR. Serology (ELISA) confirms exposure. Treat with Doxycycline (5-10 mg/kg BID for 4 weeks). Tick control with acaricidal collars and monthly spot-on treatments is essential prevention."
    },
    119: {
        "topic": "Wild Animal Housing Principles (CZA Standards)",
        "Core_Anatomy": "Ethological requirements — species-specific space, social grouping, substrate, and environmental enrichment.",
        "Pathogenesis_Immediate": "Wild animal housing in zoos must comply with Central Zoo Authority (CZA) Recognition of Zoo Rules 2009, providing minimum space dimensions, species-appropriate substrates, social grouping, and environmental enrichment to meet behavioural and physiological needs.",
        "Pathogenesis_Deep": "CZA housing principles: (1) Minimum space: Species-specific, based on body size and locomotion needs. (2) Temperature: Tropical species require heated winter enclosures. (3) Substrate: Naturalistic (soil, rock, water features, climbing structures). (4) Social needs: Gregarious species must be housed in compatible groups; solitary felids require adequate visual barriers. (5) Enrichment: Puzzle feeders, novel objects, and scent trails prevent stereotypic behaviours (pacing, weaving).",
        "Why_Not": "Traditional zoo caging (barred enclosures with concrete floors) causes stereotypic behaviour, immunosuppression, and reproductive failure. Modern exhibit design uses naturalistic enclosures with moats, glass, and hidden wire mesh, providing an immersive visitor experience while meeting animal welfare standards.",
        "Wow_Approach": "Stereotypic behaviours (repetitive, invariant, functionless behaviours) in zoo animals are the primary welfare indicator. Pacing in felids, weaving in elephants, and bar-chewing in bears indicate inadequate enrichment or space. Eliminate by providing food-search enrichment, sensory novelty, and conspecific social interaction."
    },
    120: {
        "topic": "Dog Agility Training and Canine Performance Assessment",
        "Core_Anatomy": "The canine musculoskeletal system (hip joints, vertebral column), the motor cortex, and the vestibular system.",
        "Pathogenesis_Immediate": "Dog Agility is a competitive canine sport where dogs navigate an obstacle course (jumps, tunnels, weave poles, A-frame, dog walk) guided by a handler, testing speed, accuracy, and handler-dog teamwork.",
        "Pathogenesis_Deep": "Physical demands of agility training require: Strong hindquarter musculature for jumping, spinal flexibility for weave poles (10-12 alternate poles), core stability for the A-frame (inclined planks), proprioceptive competence for contact obstacles, and high cardiovascular fitness for course completion under time. Medical screening before agility training should include hip/elbow radiographs and a cardiac examination.",
        "Why_Not": "Canine Disc (Frisbee) competitions focus on catching and retrieving. Schutzhund/IPO tests tracking, obedience, and protection. Flyball is a relay race with hurdles. Agility is the only standardized obstacle course sport with FCI (Federation Cynologique Internationale) international competition rules.",
        "Wow_Approach": "Common agility injuries: Iliopsoas strain (from repeated jumping/landing), shoulder osteochondrosis, and carpal hyperextension. Warm-up with 5 minutes of trotting is mandatory before agility practice. Young dogs (<12-18 months) should not jump at full height — growth plate closure must be confirmed radiographically first."
    },
    123: {
        "topic": "Veterinary Jurisprudence - Examination-in-Chief and Evidence Law",
        "Core_Anatomy": "N/A — Legal procedure and evidence law.",
        "Pathogenesis_Immediate": "Examination-in-Chief is the first examination of a witness by the party who calls them to testify, conducted to elicit direct evidence supporting the calling party's case. It is followed by Cross-Examination by the opposing party.",
        "Pathogenesis_Deep": "Indian Evidence Act 1872 examination sequence: (1) Examination-in-Chief — by the calling party. (2) Cross-Examination — by the opposing party (tests credibility, introduces inconsistencies). (3) Re-Examination — by the calling party to clarify points raised in cross-examination. A veterinarian testifying in court about an injury report undergoes this 3-stage examination. Leading questions are prohibited in examination-in-chief but permitted in cross-examination.",
        "Why_Not": "A 'Subpoena' (also called a Summons) is the court order compelling a witness to appear and testify. A 'Solemn Affirmation' is the non-religious alternative to the oath, used by witnesses who object to taking a religious oath. Both are procedural tools, not examination types.",
        "Wow_Approach": "A Veterinary Witness is an expert witness (not an ordinary witness). Expert witnesses can give opinion evidence (ordinary witnesses can only testify to facts they personally observed). A veterinarian giving expert testimony on wound characteristics, time of death, or cause of disease is providing expert opinion admissible under Section 45 of the Indian Evidence Act 1872."
    },
    126: {
        "topic": "Livestock Insurance - Payment on Permanent Total Disability",
        "Core_Anatomy": "N/A — Animal insurance and veterinary certification.",
        "Pathogenesis_Immediate": "Under livestock insurance schemes, when an animal suffers permanent total disability (PTD) — defined as an irreversible loss of productive/working capacity — the insurance payout is typically 75% of the insured value, not the full 100% (which applies only on death).",
        "Pathogenesis_Deep": "Livestock Insurance Scheme (LIS) in India (under Department of Animal Husbandry): Death: 100% of insured value paid. Permanent Total Disability (PTD): 75% of insured value paid. PTD is certified by a registered veterinarian using a standard PTD certificate, confirming the animal cannot be used for breeding, milking, or working. Partial disability: Percentage payout proportional to the degree of disability as assessed by a veterinary panel.",
        "Why_Not": "The DICS (Disease Investigation Compensation Scheme) pays compensation for government-mandated culling of animals positive for notifiable diseases (e.g., Foot and Mouth, Avian Influenza) at market value. Livestock Insurance PTD payments are private insurance claims requiring veterinary certification of irreversible disability.",
        "Wow_Approach": "For board exams: Death of insured animal = 100% payout. Permanent Total Disability = 75% payout. The veterinarian's PTD certificate is the key document — it must be countersigned by the District Veterinary Officer and submitted within 7 days of disability occurrence to be eligible for the claim."
    },
    127: {
        "topic": "Veterinary Jurisprudence - IPC Sections Relevant to Animal Crimes",
        "Core_Anatomy": "N/A — Indian Penal Code and animal law.",
        "Pathogenesis_Immediate": "Key Indian Penal Code (IPC) sections in veterinary jurisprudence: IPC 428 — Mischief by killing or maiming animals of value of Rs. 10 or more. IPC 429 — Mischief by killing or maiming cattle worth Rs. 50 or more. IPC 377 — Bestiality (unnatural sexual offences with animals).",
        "Pathogenesis_Deep": "IPC 428: Deliberately killing, poisoning, maiming, or rendering useless any animal of Rs.10+ value = imprisonment up to 2 years + fine. IPC 429: Same acts against cattle (elephants, camels, horses, asses, mules, or any cattle) of Rs.50+ value = imprisonment up to 5 years + fine. These IPC sections are used alongside PCA Act Section 11 to prosecute serious animal cruelty cases.",
        "Why_Not": "PCA Act Section 11 addresses cruelty in general (fine up to Rs.50 for first offence — extremely low). IPC 428/429 provide much stronger criminal penalties. Most serious animal cruelty prosecutions use IPC sections rather than PCA Act due to higher penalties.",
        "Wow_Approach": "Bestiality (IPC 377) is prosecuted independently of animal welfare law. Recently, the Bharatiya Nyaya Sanhita (BNS 2023) replaced the IPC; Section 325 of BNS corresponds to former IPC 428/429 with enhanced penalties. All veterinarians must be aware of both the old IPC and new BNS sections."
    },
    128: {
        "topic": "Veterinary Forensics - Rivolta's Test and Vegetable Oil Adulteration",
        "Core_Anatomy": "N/A — Forensic chemistry and food adulteration detection.",
        "Pathogenesis_Immediate": "Rivolta's Test is a qualitative chemical test for detecting vegetable oil adulteration in ghee or animal fats, based on the Baudouin reaction for detecting sesame oil (sesamol) in butter/ghee.",
        "Pathogenesis_Deep": "Baudouin Test (Sesame oil detection): Mix 0.1 ml of the sample with 5 ml of hydrochloric acid + 0.1 ml of furfural solution. A pink/crimson colour indicates sesame oil. Rivolta's Test detects vegetable fats generally: Mix fat with Rivolta's reagent (lead acetate + acetic acid in ethanol); vegetable oils produce a yellow precipitate while animal fats remain clear. Halphen Test detects cottonseed oil; Elaidinization test detects vegetable oil in animal fat.",
        "Why_Not": "Ghee adulteration with animal fats (beef tallow) is detected using Phytosterol Acetate Test (plant sterols absent in animal fats). Adulteration with starch is detected by iodine solution. Each adulterant has a specific chemical test — this is a highly tested area in veterinary forensics.",
        "Wow_Approach": "The FSSAI (Food Safety and Standards Authority of India) mandates maximum limits for permitted additives in milk products. Adulteration of milk with urea is detected by Dimethylaminobenzaldehyde (DMAB) test. Adulteration with formalin (preservative) is detected by Hestrin's method."
    }
}

updated = 0
for q in data:
    if q['id'] in enrichment:
        q.update(enrichment[q['id']])
        updated += 1

with open(db_path, "w", encoding="utf-8") as f:
    f.write("// Auto-generated Hybrid Exam Database\n")
    f.write("const examData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n")
print(f"Batch 2/5 DONE: Updated {updated} questions.")
