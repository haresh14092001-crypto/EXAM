import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    188: {
        "topic": "Post-Mortem Changes - Mummification vs Body Resolution",
        "Core_Anatomy": "The skin, subcutaneous fat, muscle, and visceral organs in the cadaver.",
        "Pathogenesis_Immediate": "Mummification is NOT the last stage of body decomposition. Mummification is a preserved (arrested) state of the cadaver in dry, sterile, hot environments that halts bacterial decomposition. The final stage of natural decomposition is Skeletonization.",
        "Pathogenesis_Deep": "Stages of body decomposition: (1) Fresh stage — autolysis begins. (2) Bloat stage — bacterial gas production. (3) Active decay — soft tissue liquefaction. (4) Advanced decay — adipocere formation OR mummification (competing pathways depending on environment). (5) Skeletonization — all soft tissue consumed, only bones remain. Mummification occurs in hot, dry, low-humidity environments where rapid desiccation prevents bacterial decomposition. The body dehydrates completely, becoming hard, dry, and leathery.",
        "Why_Not": "Saponification (adipocere formation) is another pathway of preservation that occurs in wet, anaerobic, cool environments — body fat converts to a soap-like material (grave wax). Both mummification and adipocere represent preservation endpoints, not final decomposition. Only skeletonization is the terminal stage of complete decomposition.",
        "Wow_Approach": "In veterinary forensics, mummified fetal remains found in cattle (mumia) represent fetal death in a sterile, progesterone-maintained uterus (persistent luteal activity). The mummified fetus becomes progressively dehydrated and compressed. Differential diagnosis: macerated fetus (death + bacterial entry = liquefaction), emphysematous fetus (death + clostridial gas), mummified fetus (death in sterile, closed uterus)."
    },
    193: {
        "topic": "Wild Dog (Dhole) and Deer Species Zoological Names",
        "Core_Anatomy": "Comparative canid and cervid anatomy; Schedule classification under WPA 1972.",
        "Pathogenesis_Immediate": "Key zoological names: Wild Dog = *Cuon alpinus* (Dhole). Tiger = *Panthera tigris*. Spotted Deer = *Axis axis*. Sambar = *Cervus unicolor*. All are Schedule I or II protected species under India's WPA 1972.",
        "Pathogenesis_Deep": "The Dhole (*Cuon alpinus*) is India's only pack-hunting wild canid, classified as Endangered on the IUCN Red List. Unlike wolves (social but distributed globally), Dholes are restricted to South and Southeast Asia. Key identification features: reddish-brown coat, bushy tail, and the unique 'whistle' communication call. Dholes are the only canid with more than 6 lower molars — they have uniquely reduced dentition (2 lower molars vs 3 in wolves and dogs).",
        "Why_Not": "*Panthera tigris* = Tiger. *Panthera leo persica* = Asiatic Lion. *Axis axis* = Chital (Spotted Deer). *Rusa unicolor* = Sambar Deer. *Cuon alpinus* = Dhole. These zoological names are directly tested in MCQ format in WPA/zoo management examinations.",
        "Wow_Approach": "Conservation status of key Indian species (IUCN 2024): Tiger — Endangered (NT globally, but Endangered in India under WPA Schedule I). Asiatic Lion — Endangered. Dhole — Endangered. Snow Leopard — Vulnerable. Indian Rhinoceros — Vulnerable. Indian Elephant — Endangered. All Schedule I species in India receive equivalent protection to IUCN Critically Endangered status."
    },
    194: {
        "topic": "Canine Ehrlichiosis - Monocytosis Pathognomonic Feature",
        "Core_Anatomy": "Canine monocytes, bone marrow haematopoietic compartment, and the splenic red pulp.",
        "Pathogenesis_Immediate": "Monocytosis (elevated circulating monocytes) is the pathognomonic haematological feature of Canine Monocytic Ehrlichiosis (*Ehrlichia canis*), distinguishing it from Babesiosis (haemolytic anaemia), Parvoviral enteritis (leucopenia/neutropenia), and Kennel Cough (lymphocytosis).",
        "Pathogenesis_Deep": "E. canis obligately infects monocytes and macrophages, forming characteristic intracytoplasmic clusters called morulae (seen in peripheral blood smear in only 4% of cases). The infected monocytes release IL-1, IL-6 and TNF-alpha → bone marrow monocyte production upregulated → peripheral monocytosis. Simultaneously, immune-mediated platelet destruction occurs (thrombocytopenia <50,000/μL) — the combination of monocytosis + thrombocytopenia is the haematological signature of acute Ehrlichiosis.",
        "Why_Not": "Babesiosis (Babesia canis) causes haemolytic anaemia (PCV drop, reticulocytosis, haemoglobinaemia, haemoglobinuria). Ehrlichiosis causes non-regenerative anaemia from bone marrow suppression in the chronic phase. Distinguishing these two tick-borne diseases is critical as treatment differs: Doxycycline for Ehrlichiosis, Imidocarb Dipropionate for Babesiosis.",
        "Wow_Approach": "Always test for co-infections: E. canis and Babesia canis are transmitted by the SAME tick (*Rhipicephalus sanguineus*), and co-infection in 20-30% of cases creates a combined haematological picture. Use PCR for definitive diagnosis; serology (ELISA) confirms exposure but cannot distinguish acute vs past infection."
    },
    195: {
        "topic": "Canine Distemper - Alimentary, Respiratory, and Nervous Forms",
        "Core_Anatomy": "The respiratory mucosa (trachea, bronchi), the intestinal epithelium, and the CNS white matter (myelin sheaths).",
        "Pathogenesis_Immediate": "Canine Distemper Virus (CDV) causes three major clinical forms based on which system is most severely affected: Respiratory form (most common — cough, nasal discharge), Alimentary/Gastrointestinal form (vomiting, diarrhoea), and Nervous form (seizures, chorea, myoclonus) — all three forms can occur simultaneously.",
        "Pathogenesis_Deep": "CDV replication sequence: (1) Respiratory form — virus infects nasal and bronchial epithelium, causing mucopurulent nasal discharge, tonsillitis, and bronchopneumonia. (2) Alimentary form — virus spreads via systemic viraemia to intestinal epithelium, causing vomiting and haemorrhagic diarrhoea. (3) Nervous form — virus crosses the blood-brain barrier 7-21 days after initial infection, causing demyelinating encephalomyelitis. Classic signs: rhythmic myoclonic jerks (chorea — 'chewing gum fits'), progressive paresis, and dementia.",
        "Why_Not": "Hard Pad Disease is caused by CDV hyperkeratinization of the digital pads and nasal planum — it is NOT a separate disease but a manifestation of the alimentary/cutaneous form of CDV. The eponym 'Old Dog Encephalitis' describes CDV-associated chronic progressive encephalitis in adult dogs who survived the acute phase.",
        "Wow_Approach": "Pathognomonic CDV findings: (1) Eosinophilic intranuclear and intracytoplasmic inclusion bodies in epithelial cells (brain, bladder, lung — Lentz inclusion bodies). (2) Demyelinating perivascular cuffing in the CNS. (3) Hard pad with skin hyperkeratosis. These three findings together are diagnostic at post-mortem."
    },
    196: {
        "topic": "Heaviest Dog Breed - Saint Bernard",
        "Core_Anatomy": "The musculoskeletal system of giant breed dogs — large skeletal frame, hip and elbow joints.",
        "Pathogenesis_Immediate": "The Saint Bernard is one of the heaviest dog breeds in the world, with adults typically weighing 64-120 kg, and exceptional individuals exceeding 140 kg. Other large breeds include Mastiff, Great Dane, and Newfoundland.",
        "Pathogenesis_Deep": "Giant breeds face breed-specific health challenges due to their extreme size: Hip Dysplasia (abnormal femoral head-acetabular conformation), Elbow Dysplasia, Gastric Dilatation-Volvulus (GDV — deep-chested conformation), Dilated Cardiomyopathy (DCM — increased cardiac workload), and a reduced lifespan (8-10 years vs 15+ years for small breeds). Growth plate closure is delayed in giant breeds — large-breed puppy diets with restricted calcium and calories are mandatory to prevent developmental orthopaedic disease.",
        "Why_Not": "Spitz dogs are small-to-medium sized (Pomeranian 2-3 kg; Finnish Spitz 12-15 kg). Chow Chow is a medium breed (20-32 kg). Dalmatian is a medium breed (23-30 kg). The Saint Bernard's extraordinary weight is due to its historical role as an alpine rescue dog requiring massive physical strength to carry victims.",
        "Wow_Approach": "Saint Bernards are the most associated breed with GDV (Bloat). Gastropexy at time of spay/neuter is strongly recommended prophylactically for Saint Bernards and other deep-chested giant breeds. Without gastropexy, lifetime GDV risk in Saint Bernards exceeds 40%."
    },
    197: {
        "topic": "Pet Bird Identification - Ringing (Leg Band) as Primary Technique",
        "Core_Anatomy": "The avian tarsometatarsus (leg) and the microchip implantation site (left pectoral muscle).",
        "Pathogenesis_Immediate": "Ringing (leg banding) is the most common technique used to identify pet birds. Closed metal or plastic rings applied at hatching contain the breeder code, year, and individual number — providing permanent, traceable individual identification.",
        "Pathogenesis_Deep": "Types of rings: (1) Closed ring — applied at 5-10 days of age (before the foot is too large to pass through). Permanently identifies the bird's hatchery of origin and year. (2) Open (split) ring — applied at any age; used for individual marking but less tamper-proof. (3) Microchip — injected into the left pectoral muscle at any age; provides internationally traceable identification (ISO standard). DNA analysis from feather pulp or blood confirms species and individual identity for legal/forensic purposes.",
        "Why_Not": "Tattooing (wing web) is used for poultry flocks (multiple birds identified by flock number), not individual pet birds. Ear notching is used for cattle and pig identification. Branding (hot iron or freeze-brand) is used for cattle and horses — not for birds (no appropriate anatomical site and extreme stress/injury risk).",
        "Wow_Approach": "CITES-listed pet birds (African Greys, Macaws, Cockatoos) legally imported must have a CITES permit number engraved on the closed ring AND a microchip. Ring reading without sedation can be done by reading the inscription using a magnifying glass. Microchip reading requires a 134.2 kHz ISO-compatible scanner."
    },
    199: {
        "topic": "Rivalta's Test - Clinical Diagnosis of FIP vs Other Effusions",
        "Core_Anatomy": "The peritoneum, the pleural space, and the hepatic portal circulation in cats with FIP.",
        "Pathogenesis_Immediate": "Rivalta's Test distinguishes high-protein exudate (characteristic of FIP) from low-protein transudate (cardiac/hepatic failure, hypoalbuminaemia) in feline effusions — a critical bedside diagnostic tool.",
        "Pathogenesis_Deep": "Rivolta's/Rivalta's Reaction: Add 1 drop of distilled water to a 4% glacial acetic acid solution. Drip 1 drop of effusion fluid gently onto the surface of the acetic acid solution. A positive result (white, jellyfish-like precipitate forming and sinking slowly) indicates high fibronectin + globulin content = exudate consistent with FIP. Negative (drop disperses) = transudate from cardiac or hepatic failure.",
        "Why_Not": "Chylothorax is a milky, triglyceride-rich effusion that tests Rivalta's negative because the high-fat content does not form protein-acetic acid precipitates. Bacterial pyothorax (empyema) gives a Rivalta's positive result — microbiological culture differentiates FIP from pyothorax.",
        "Wow_Approach": "FIP effusion characteristics (Weiss criteria): Colour = straw-yellow. Consistency = viscous (high fibrin). Protein = >35 g/L. Albumin:Globulin ratio in effusion = <0.4. Rivolta's test positive. Corona virus PCR from effusion fluid or lymph node aspirate confirms FIP. GS-441524 treatment now offers >85% remission — a revolutionary change in FIP prognosis."
    },
    240: {
        "topic": "Winking of Clitoris as Oestrus Sign in the Mare",
        "Core_Anatomy": "The vulva, clitoris (enlarged in mares), and the vestibulo-vaginal junction in the equine reproductive tract.",
        "Pathogenesis_Immediate": "Winking (rhythmic eversion and retraction of the clitoris, exposing the glans clitoris) is the pathognomonic behavioural sign of oestrus in mares, occurring in response to the presence of a stallion or teaser.",
        "Pathogenesis_Deep": "During oestrus, high estrogen levels sensitize the perivulvar musculature to tactile stimulation by the stallion's approach, vocalisation, and olfactory cues. The mare repeatedly everts the clitoris (winking) and abducts the hindlimbs (squatting), producing a characteristic 'show' posture. This is accompanied by lifting the tail (tail elevation), urination (squirting), and mucoid vaginal discharge. These signs collectively indicate sexual receptivity — the optimal time for natural mating or AI.",
        "Why_Not": "In cows, the primary oestrus sign is standing to be mounted (immobilisation reflex). In ewes, oestrus is virtually silent (cryptic oestrus). In sows, the standing oestrus reflex (lordosis response) and boar pheromone-triggered rigidity are the primary signs. Only in mares is clitoral winking pathognomonic for oestrus.",
        "Wow_Approach": "Teasing (exposing the mare to a stallion or teaser through a safe barrier daily) is the most sensitive oestrus detection method in mares — more reliable than tail painting or progesterone assays for field use. Mares typically show strong winking within 30 seconds of teaser exposure during peak oestrus."
    },
    241: {
        "topic": "Metoestral Bleeding (Post-Oestral Bleeding) in Cattle - Oestrogen Withdrawal",
        "Core_Anatomy": "The endometrial capillaries, the uterine luminal epithelium, and the hormonal axis (oestrogen→progesterone transition).",
        "Pathogenesis_Immediate": "Metoestral bleeding (post-oestral spotting) in cattle occurs on Days 1-3 after oestrus, caused by endometrial capillary haemorrhage following the abrupt withdrawal of oestrogen at the end of oestrus.",
        "Pathogenesis_Deep": "During oestrus, peak oestradiol causes maximal endometrial vascularization and capillary engorgement. After ovulation, the LH surge triggers luteinization — oestrogen drops sharply and progesterone begins to rise. The sudden oestrogen withdrawal causes vasoconstriction and breakdown of the distended endometrial capillaries, releasing a small amount of blood (1-2 ml) that appears as bloody mucus at the vulva 1-3 days post-oestrus.",
        "Why_Not": "Progesterone withdrawal (at luteolysis on Day 16-17) does NOT cause metoestral bleeding — it causes the return to follicular phase and subsequent oestrus. Metoestral bleeding is specifically caused by oestrogen withdrawal and is a NORMAL physiological finding — it actually confirms that oestrus and ovulation have occurred (a retrospective oestrus detection method).",
        "Wow_Approach": "Practical use: If a herd attendant observes bloody mucus on a cow, count back 3 days to identify the missed oestrus date and calculate the next expected oestrus (21 days later). This 'blood dating' technique is a valuable retrospective oestrus detection tool in herds without 24-hour observation."
    },
    242: {
        "topic": "PSP Dye Test for Fallopian Tube Patency",
        "Core_Anatomy": "The infundibulum, ampulla, and isthmus of the bovine oviduct.",
        "Pathogenesis_Immediate": "The PSP (Phenolsulfonphthalein) Test is the specific diagnostic test for detecting blockage of the Fallopian tube (oviduct) in cattle. It is the gold standard for confirming oviductal occlusion in repeat-breeding cattle with suspected salpingitis.",
        "Pathogenesis_Deep": "PSP Dye Test technique: Inject 5 ml of 0.5% PSP dye solution transcervically into each uterine horn using a long inseminating catheter. Wait 20 minutes. Collect peritoneal fluid by paracentesis (ventral midline) and observe for pink/red colour (indicating PSP passage through the oviducts into the peritoneum). Pink peritoneal fluid = patent oviducts. Colourless peritoneal fluid = oviductal occlusion.",
        "Why_Not": "Cuboni Test detects urinary oestrogen metabolites in pregnant mares' urine (a pregnancy test). White Side Test is a milk alkalinization test for subclinical mastitis (SCC detection). Spinnbarkeit is a measure of cervical mucus elasticity at oestrus. None of these tests evaluate oviductal patency.",
        "Wow_Approach": "Oviductal patency can also be assessed by hydrotubation (flushing sterile saline through the cervix under pressure) and feeling the resistance. Laparoscopic visualization is the gold standard but requires special equipment and sedation. In India, the PSP dye test remains the most practical and affordable field test for repeat-breeding cattle investigation."
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
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries. {len(empty2)} high-yield questions still empty.")
