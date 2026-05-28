import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    181: {
        "topic": "Dissociative Anaesthetics and Animal Identification Techniques",
        "Core_Anatomy": "The NMDA (N-methyl-D-aspartate) glutamate receptors in the thalamus and limbic system; the subcutaneous tissue for microchip placement.",
        "Pathogenesis_Immediate": "Dissociative anaesthetics (Ketamine, Tiletamine) produce a trance-like 'dissociative' state by blocking NMDA receptors, causing catalepsy with maintained laryngeal reflexes. Microchips (ISO 11784/11785 standard 15-digit transponders) are the gold standard for permanent animal identification.",
        "Pathogenesis_Deep": "Ketamine blocks NMDA receptors non-competitively, preventing glutamate-mediated calcium influx. This dissociates the thalamocortical system from the limbic system, causing a cataleptic state where the patient appears awake (eyes open, muscle tone maintained) but is unaware of painful stimuli. Microchips implanted subcutaneously emit a unique 15-digit ISO code when scanned, providing permanent, tamper-proof identification used for international pet travel (EU Pet Passport), anti-theft, and wildlife tracking.",
        "Why_Not": "Unlike inhalant anaesthetics (Isoflurane) which cause dose-dependent respiratory depression, ketamine maintains laryngeal-pharyngeal reflexes and preserves respiratory drive, making it safer for field use. However, ketamine alone causes excessive muscle tone and hypersalivation — always combine with a benzodiazepine (midazolam) or alpha-2 agonist (medetomidine).",
        "Wow_Approach": "Cropping of wildlife (ear notching) is used for population census in large mammals (elephants, rhinos) where each individual receives a unique notch pattern on the ear pinnae that can be identified from photographs at distance. Combined with photo-ID (whisker spot patterns in cheetahs, fluke patterns in whales), this allows non-invasive individual identification."
    },
    183: {
        "topic": "Breed-Specific Disease Associations in Dogs and Cats",
        "Core_Anatomy": "Breed-specific anatomical variations: brachycephalic facial structure (Pug), deep skin folds (Neapolitan Mastiff, Shar-Pei), and uric acid metabolism (Dalmatian).",
        "Pathogenesis_Immediate": "Key breed-specific disease associations: Pug — Feline Infectious Peritonitis (wrong — FIP is feline), actually BAOS/Pug Encephalitis. Skin fold dermatitis — Neapolitan Mastiff/Shar-Pei. Corneal ulcer — Pug/Boxer (exophthalmos). Urate urolithiasis — Dalmatian.",
        "Pathogenesis_Deep": "Dalmatian urate urolithiasis: Dalmatians uniquely lack hepatic uricase enzyme activity (due to a mutation in the SLC2A9 gene). Other dogs convert uric acid to allantoin (soluble). Dalmatians excrete uric acid unchanged, causing urate crystal precipitation in the urine. This leads to urate uroliths in the bladder and urethra, causing urinary obstruction — predominantly in intact male Dalmatians.",
        "Why_Not": "Oxalate uroliths are most common in Miniature Schnauzers and Bichon Frises. Struvite uroliths are most common in female dogs with concurrent UTI (Staphylococcus). Cystine uroliths are seen in English Bulldogs. Only Dalmatians have the unique purine metabolism defect causing urate urolithiasis.",
        "Wow_Approach": "Manage Dalmatian urate urolithiasis with: low-purine diet (avoid organ meats, sardines), alkalinize urine to pH 7.0-7.5 (potassium citrate), and allopurinol (xanthine oxidase inhibitor, reduces uric acid production). Surgical hydropulsion or cystotomy for obstructive uroliths."
    },
    184: {
        "topic": "Corneal Ulceration in Brachycephalic Dogs",
        "Core_Anatomy": "The corneal epithelium, Bowman's membrane, corneal stroma, and the lacrimal film.",
        "Pathogenesis_Immediate": "Corneal ulceration is highly prevalent in brachycephalic breeds (Pug, Boxer, Shih Tzu, Boston Terrier) due to exophthalmos (prominent eyes), incomplete blinking (lagophthalmos), and exposure keratitis causing corneal desiccation and epithelial breakdown.",
        "Pathogenesis_Deep": "Brachycephalic dogs have shallow orbits and large, prominent globes (exophthalmos). The eyelids cannot completely cover the cornea during blinking, leaving the central corneal surface chronically exposed to air (lagophthalmos). This causes desiccation of the pre-corneal tear film, epithelial cell death, and progression from superficial epithelial erosions to deep stromal ulcers. Deep corneal ulcers risk corneal perforation, iris prolapse, and phthisis bulbi.",
        "Why_Not": "Corneal ulcers in dolichocephalic breeds (German Shepherd, Collie) are usually caused by distichiasis (aberrant eyelashes) or traumatic injuries. In brachycephalic breeds, the primary cause is anatomical — chronic corneal exposure due to exophthalmos and lagophthalmos.",
        "Wow_Approach": "Treat deep corneal ulcers (descemetocele — only Descemet's membrane remaining) as emergencies: apply a conjunctival flap or corneoconjunctival transposition immediately to prevent perforation. Use triple therapy: broad-spectrum antibiotic eye drops (tobramycin), atropine (1% drops for ciliary spasm), and oral doxycycline (matrix metalloproteinase inhibitor to slow stromal dissolution)."
    },
    185: {
        "topic": "Animal Welfare Ethics and Jurisprudence - Key Fill-in Facts",
        "Core_Anatomy": "N/A — Statutory and ethical framework.",
        "Pathogenesis_Immediate": "Key facts for Animal Welfare, Ethics and Jurisprudence (VMD 511): The Five Freedoms were established by the Brambell Committee (1965). The CPCSEA (Committee for the Purpose of Control and Supervision of Experiments on Animals) oversees animal experimentation. The WPA 1972 lists six Schedules of animals/plants.",
        "Pathogenesis_Deep": "Critical exam fill-in facts: AWBI headquarters = Chennai. PCA Act year = 1960. WPA year = 1972. Project Tiger year = 1973. CITES ratified by India = 1976. CZA established = 1992. OIE/WOAH HQ = Paris. CITES HQ = Geneva. The 3Rs principle (Russell & Burch, 1959) for animal experiments: Replacement, Reduction, Refinement. Replacement = use of non-animal alternatives. Reduction = minimize number of animals. Refinement = minimize pain/distress per animal.",
        "Why_Not": "The 3Rs are legally mandated in India through CPCSEA guidelines and the Breeding of and Experiments on Animals (Control and Supervision) Rules 2006. Any research institution using animals must have an Institutional Animal Ethics Committee (IAEC) with a veterinarian member and 3Rs compliance monitoring.",
        "Wow_Approach": "The CPCSEA requires that all animal experiments be approved by the IAEC before commencement. Unapproved animal experiments constitute an offence under Rule 13 of the 2006 Rules, punishable by cancellation of the institution's registration to conduct animal experiments — an extremely serious professional consequence."
    },
    186: {
        "topic": "IPC Section 197 - False Certificate by Public Servant",
        "Core_Anatomy": "N/A — Criminal law and veterinary professional liability.",
        "Pathogenesis_Immediate": "IPC Section 197 (now BNS Section 220) criminalizes the issuance of false certificates by a public servant who is legally authorized to issue certificates. A government veterinarian issuing a false health certificate, transport fitness certificate, or post-mortem report is punishable under Section 197.",
        "Pathogenesis_Deep": "IPC 197 elements: (1) The person must be a public servant authorized by law to issue certificates. (2) The certificate must be false in a material point. (3) The person must know or believe the certificate to be false. Penalty: Imprisonment up to 2 years + fine. For government veterinarians, false certification can also attract VCI (Veterinary Council of India) disciplinary proceedings, suspension, or cancellation of registration.",
        "Why_Not": "IPC Section 193 (perjury — giving false evidence in judicial proceedings) and Section 178 (refusing to take oath when required) are related but distinct offences. IPC 197 specifically targets false certification by authorized public servants, whereas IPC 193 targets false oral evidence given in court.",
        "Wow_Approach": "Common scenarios of IPC 197 risk in veterinary practice: signing blank transport certificates, issuing post-mortem reports without examination, certifying animals as disease-free without testing, and falsely certifying animals as fit for breeding. Private veterinarians are NOT public servants under IPC — they fall under IPC 468 (forgery for cheating) and 471 (using forged documents)."
    },
    187: {
        "topic": "Livestock Insurance Scheme - PTD Payout and Death Payout",
        "Core_Anatomy": "N/A — Animal insurance scheme mechanics.",
        "Pathogenesis_Immediate": "Under the Livestock Insurance Scheme (LIS): Death of insured animal = 100% of insured value. Permanent Total Disability (PTD) = 75% of insured value. This differential is to account for the residual value of a disabled animal (e.g., for sale for slaughter or alternative use).",
        "Pathogenesis_Deep": "The LIS (currently under National Livestock Mission, Ministry of Animal Husbandry) provides insurance cover for: Cattle, Buffalo, Pig, Sheep, Goat, Rabbit, Poultry (broilers and layers). Premium rate: 3% of insured value per annum (50% subsidised by government for BPL farmers). Maximum insured value: Based on fair market value as certified by the attending veterinarian at time of inception of policy.",
        "Why_Not": "Crop insurance (PMFBY — Pradhan Mantri Fasal Bima Yojana) and livestock insurance are separate schemes. Livestock insurance specifically requires individual animal identification (ear tag + microchip number on policy), veterinary fitness certificate at inception, and reporting of death/PTD within 7 days.",
        "Wow_Approach": "Key examiner fact: Mummification is NOT the last stage in body resolution — it is a preserved, arrested state of the dead body in a sterile, dry environment. The true final stage in body decomposition is skeletonization. Mummification halts decomposition by dehydration, preserving the body indefinitely."
    },
    191: {
        "topic": "Cold-Blooded Animals (Poikilotherms) and Tusk Anatomy in Elephants",
        "Core_Anatomy": "The tusk (modified upper incisor tooth) of elephants, composed of dentine (ivory) with a persistent pulp cavity.",
        "Pathogenesis_Immediate": "Cold-blooded (Poikilothermic/Ectothermic) animals — Reptiles (lizards, snakes, crocodiles, turtles) and Fish — cannot regulate their body temperature internally; their body temperature varies with the environment. Elephant tusks are highly modified, continuously growing upper second incisor teeth composed of ivory (dentine).",
        "Pathogenesis_Deep": "Tusk structure: Outer layer of enamel (limited, at tip only in young elephants, wears away). Middle layer of cementum. Central ivory core (dentine). Persistent pulp cavity extending 2/3 of the tusk length. Tusks grow throughout life at ~17 cm/year (African elephant) and are used for digging, foraging, defense, and male social display. Tusk removal (live) is conducted under full general anaesthesia in wildlife veterinary practice.",
        "Why_Not": "Birds and mammals are warm-blooded (Homeothermic/Endothermic) — they maintain constant internal body temperature through metabolic heat production regardless of environmental temperature. Elephants (Proboscidea) are mammals, therefore warm-blooded, despite common misconceptions due to their wrinkled skin (which aids heat dissipation, not thermoregulation like reptiles).",
        "Wow_Approach": "Tusk pulpitis in captive elephants is an extremely painful, serious condition causing head tossing and aggression. Treatment: deep general anaesthesia (Etorphine-based protocols with Azaperone sedation), radiographic assessment of pulp extent, and either pulp capping or partial amputation of the tusk with dental burr under irrigation."
    },
    192: {
        "topic": "King Cobra (Ophiophagus) and WPA 1972 Enactment Year",
        "Core_Anatomy": "The fang apparatus of elapid snakes and the ophiophagous dietary specialization of the King Cobra.",
        "Pathogenesis_Immediate": "The King Cobra (*Ophiophagus hannah*) is the world's longest venomous snake (up to 5.5 m) and is strictly ophiophagous (feeds exclusively on other snakes). The Wildlife Protection Act was enacted in 1972.",
        "Pathogenesis_Deep": "King Cobra venom: Primarily neurotoxic — contains three-finger toxins (OH-55) and phospholipase A2. A single bite can deliver 7 ml of venom, enough to kill an Asian Elephant. Despite its fearsome reputation, the King Cobra avoids human confrontation. Its unique ophiophagous diet makes it a keystone species controlling rat snake and viper populations. Nesting behaviour: the only snake species that builds a nest and guards its eggs.",
        "Why_Not": "Pythons are strictly non-venomous constrictors. Vipers (Russell's Viper, Saw-scaled Viper) are ophiophagous opportunists but not exclusively. Kraits prey on other snakes occasionally. Only the King Cobra is exclusively and obligately ophiophagous, reflected in its genus name *Ophiophagus* (Greek: snake-eater).",
        "Wow_Approach": "King Cobra antivenom is monovalent and species-specific — polyvalent ASV does not protect against King Cobra envenomation. Thai Red Cross and Queen Saovabha Memorial Institute manufacture the only validated King Cobra antivenom. First aid: immobilize, pressure-immobilization bandage (for neurotoxic envenomation), rush to tertiary hospital with ICU and mechanical ventilator availability."
    },
    198: {
        "topic": "Diabetes Mellitus in Dogs - Type 1 (Insulin-Dependent)",
        "Core_Anatomy": "The islets of Langerhans (beta cells of the pancreas), the systemic glucose transport system (GLUT transporters), and the kidneys (renal glucose threshold).",
        "Pathogenesis_Immediate": "Diabetes Mellitus in dogs is almost exclusively Type 1 (Insulin-Dependent Diabetes Mellitus, IDDM), characterized by absolute insulin deficiency due to immune-mediated or idiopathic destruction of pancreatic beta cells, requiring lifelong insulin therapy.",
        "Pathogenesis_Deep": "In dogs, repeated bouts of pancreatitis or immune-mediated insulitis progressively destroy beta cells. With >80% beta cell loss, insulin secretion becomes critically insufficient. Without insulin, glucose cannot enter peripheral cells (muscle, adipose), causing hyperglycaemia. When blood glucose exceeds the renal threshold (>10 mmol/L in dogs), glucose spills into urine (glucosuria), causing osmotic diuresis (PU/PD), polyphagia (cellular starvation), and progressive weight loss.",
        "Why_Not": "Cats predominantly develop Type 2 DM (Insulin-Independent, NIDDM) caused by amyloid deposition in pancreatic islets causing insulin resistance — similar to human T2DM. Dogs develop Type 1 IDDM from beta cell destruction. This distinction is critical because diabetic cats can go into remission with dietary management; diabetic dogs almost never achieve remission.",
        "Wow_Approach": "Manage canine DM with twice-daily Lente (intermediate-acting) insulin (Caninsulin®). Monitor with glucose curves (8-hourly measurements) and fructosamine (reflects 2-3 week glycaemic control). Intact female dogs have progesterone-induced insulin resistance — always spay diabetic female dogs to significantly reduce insulin requirements."
    },
    200: {
        "topic": "Non-Core Vaccines in Dogs - Coronavirus Vaccine Status",
        "Core_Anatomy": "The intestinal epithelium (Coronavirus target) and the systemic immune system for vaccination.",
        "Pathogenesis_Immediate": "Canine Coronavirus Vaccine is classified as a NON-CORE vaccine in current vaccination guidelines (WSAVA 2016). Core vaccines (given to every dog) are: Canine Distemper (CDV), Canine Parvovirus (CPV-2), Canine Adenovirus-2 (CAV-2/Hepatitis), and Rabies.",
        "Pathogenesis_Deep": "Core vs Non-Core classification: Core vaccines protect against diseases that are severe, life-threatening, globally prevalent, and/or zoonotic. Non-Core vaccines (CCoV, Leptospira, Bordetella, Borrelia) are given based on individual risk assessment (lifestyle, geographic exposure, kennelling). Canine Coronavirus causes a mild, self-limiting enteritis in puppies — rarely fatal and not considered a universal threat. Leptospira vaccines are non-core in low-risk environments but core in high-exposure areas (flooding, cattle country).",
        "Why_Not": "Parvovirus vaccine is CORE because CPV-2 causes rapidly fatal haemorrhagic gastroenteritis with very high mortality rates (50-91% untreated). Distemper is CORE because CDV causes multisystemic, often fatal disease with no specific treatment. Coronavirus is non-core because natural immunity is acquired early and disease severity is low.",
        "Wow_Approach": "Vaccination Schedule: Puppy series — 6 wk (optional), 8 wk, 12 wk, 16 wk (all core vaccines). First adult booster — 1 year post-puppy series. Thereafter — CDV and CPV every 3 years (long duration of immunity); Rabies annually (per government mandate in India). Maternal antibody interference is the primary reason for the 3-injection puppy series."
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
