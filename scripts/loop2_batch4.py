import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    155: {
        "topic": "Tetanus (Lockjaw) in Dogs - Risus Sardonicus",
        "Core_Anatomy": "The alpha-motor neurons of the spinal cord anterior horn, the inhibitory interneurons (Renshaw cells), and the peripheral nerve terminals.",
        "Pathogenesis_Immediate": "Tetanus in dogs is caused by *Clostridium tetani* neurotoxin (tetanospasmin) producing the classic triad: Risus Sardonicus (sardonic grin — facial muscle spasm), Trismus (lock jaw — masseter spasm), and opisthotonos (extensor rigidity of the spine).",
        "Pathogenesis_Deep": "Tetanospasmin (TeNT) produced at wound sites is transported retrogradely via motor neuron axons to the spinal cord. In the spinal cord, TeNT cleaves synaptobrevin (a SNARE protein) in the inhibitory interneurons (glycinergic and GABAergic). This blocks inhibitory neurotransmitter release, eliminating the normal inhibition of alpha-motor neurons. Unopposed excitatory input causes sustained, tonic contraction of all skeletal muscles simultaneously.",
        "Why_Not": "Canine Distemper causes polioencephalomalacia with chorea (rhythmic myoclonic jerks) and dementia — not the tonic rigidity of tetanus. Strychnine poisoning (glycine antagonist) causes identical spasms to tetanus but has a sudden onset without prodrome, and no wound is found. Tetanus has a characteristic progressive onset over days.",
        "Wow_Approach": "Treatment: Tetanus Antitoxin (TAT) neutralizes unbound toxin (10,000-100,000 IU IM/IV). Metronidazole kills remaining bacteria. Diazepam/methocarbamol controls spasms. House in a dark, quiet room (stimuli trigger spasms). The horse is the most susceptible species; dogs are relatively resistant. Most susceptible small animal: Horses >> Cattle >> Sheep >> Pigs >> Dogs >> Cats."
    },
    156: {
        "topic": "Risus Sardonicus and Tetanus Differential Diagnosis",
        "Core_Anatomy": "The facial muscles (zygomaticus, risorius), the masseter, and the temporal muscle.",
        "Pathogenesis_Immediate": "Risus Sardonicus ('sardonic smile') is the pathognomonic facial expression of tetanus, caused by sustained spasm of the facial muscles pulling the lips into a forced grin with the nose wrinkled and ears erect — a direct result of tetanospasmin blocking inhibitory interneurons controlling facial musculature.",
        "Pathogenesis_Deep": "The name 'sardonic grin' comes from the ancient Greek description of the facial appearance caused by the Sardinian plant *Oenanthe crocata* poisoning. In tetanus, the expression is produced by: zygomaticus major (cheek retraction) + orbicularis oris (lip retraction) + corrugator supercilii (brow furrowing) all contracting simultaneously without inhibitory control. In severe tetanus, the combination of Risus Sardonicus + Trismus + opisthotonos is unmistakable.",
        "Why_Not": "Rabies causes facial spasms but these are intermittent and associated with hydrophobia (pharyngeal spasm on seeing water), aggression, and terminal paralysis. Tetanus spasms are continuous tonic rigidity triggered by stimulation. Strychnine toxicosis mimics tetanus perfectly but has no fever, the wound is absent, and spasms are relieved between attacks.",
        "Wow_Approach": "Prognosis in dogs: Localized tetanus (one limb affected) has a good prognosis. Generalized tetanus (full-body rigidity) carries 50% mortality without aggressive intensive care. Nursing: provide padded flooring, sling support, IV fluids, nasogastric tube feeding, bladder catheterization, and minimal stimulation to reduce reflex spasm triggers."
    },
    157: {
        "topic": "Canine Distemper - Systemic Pathology and Treatment",
        "Core_Anatomy": "The respiratory epithelium, the CNS white matter, the skin (footpad hyperkeratosis), and lymphoid tissue.",
        "Pathogenesis_Immediate": "Canine Distemper Virus (CDV — Morbillivirus) causes a multisystemic disease in dogs with three phases: respiratory (cough, nasal discharge), gastrointestinal (vomiting, diarrhoea), and neurological (seizures, chorea, dementia, optic neuritis).",
        "Pathogenesis_Deep": "CDV infects dendritic cells in the respiratory tract, disseminates via lymphatics causing lymphopenia and immunosuppression, then spreads systemically to the epithelium (inclusion bodies in respiratory, urinary, and skin epithelium), and finally invades the CNS. The neurological phase involves demyelinating leukoencephalomyelitis. The classic lesion is 'Old Dog Encephalitis' (chronic progressive demyelination in older survivors). Footpad hyperkeratosis ('Hard Pad Disease') results from CDV-induced hyperkeratinization of the digital pads.",
        "Why_Not": "Ehrlichiosis (treated with Doxycycline) causes monocytosis and thrombocytopenia, not the classic respiratory-GI-neurological triad of CDV. Babesiosis (treated with Imidocarb Dipropionate) causes haemolytic anaemia. Parvoviral enteritis causes severe haemorrhagic diarrhoea without the neurological phase.",
        "Wow_Approach": "No specific antiviral treatment exists for CDV. Management is entirely supportive: broad-spectrum antibiotics (for secondary bacterial pneumonia), IV fluids, anticonvulsants (phenobarbitone), riboflavin supplementation for demyelination support. Prevention: Monovalent CDV vaccine or combination MLV vaccines (DA2PP) from 6 weeks; 3-injection puppy series + annual boosters."
    },
    163: {
        "topic": "Animal Welfare Ethics - Brambell Committee and Five Freedoms",
        "Core_Anatomy": "N/A — Animal welfare ethics framework.",
        "Pathogenesis_Immediate": "The Brambell Committee (1965, UK) established the foundational 'Five Freedoms' of animal welfare that became the global standard for assessing farm animal welfare. These freedoms are now embedded in all modern animal welfare legislation including India's PCA Act.",
        "Pathogenesis_Deep": "The Five Freedoms (Brambell Committee 1965, refined by UK Farm Animal Welfare Council 1979): (1) Freedom from Hunger and Thirst — access to fresh water and diet to maintain health. (2) Freedom from Discomfort — appropriate environment including shelter and rest area. (3) Freedom from Pain, Injury, or Disease — prevention or rapid diagnosis and treatment. (4) Freedom to Express Normal Behaviour — sufficient space, proper facilities, and company of the animal's own kind. (5) Freedom from Fear and Distress — conditions and treatment which avoid mental suffering.",
        "Why_Not": "The 'Five Domains' model (Mellor, 2017) is the modern update to Five Freedoms, adding a fifth domain of Mental State (incorporating positive welfare, not just absence of negative states). The WOAH Terrestrial Animal Health Code uses Five Freedoms as the basis for all member countries' welfare standards.",
        "Wow_Approach": "For board exams: Brambell Committee = 1965 = Five Freedoms origin. The Five Freedoms are now the global minimum standard for animal welfare. Any intensive production system that violates a Freedom (e.g., battery cages violating Freedom 4 — normal behaviour) is considered a welfare concern under international standards."
    },
    165: {
        "topic": "Livestock Insurance - Permanent Total Disability Payout Rate",
        "Core_Anatomy": "N/A — Animal insurance and veterinary certification.",
        "Pathogenesis_Immediate": "Under the Livestock Insurance Scheme (LIS), permanent total disability (PTD) — irreversible loss of productive/working capacity — entitles the insured animal owner to 75% of the insured value, confirmed by a PTD certificate issued by a registered veterinarian.",
        "Pathogenesis_Deep": "PTD definition in livestock insurance: Permanent blindness in both eyes, complete loss of a limb, permanent paralysis, or total inability to perform the insured productive function (milking/working/breeding). The PTD certificate must be issued within 7 days of the disability event, countersigned by the District Veterinary Officer, and submitted to the insurance company with the original policy document and post-mortem report if applicable.",
        "Why_Not": "Temporary disability (lameness, illness with expected recovery) does not qualify for PTD claims. Only permanent, irreversible conditions qualify. The insuring veterinarian must certify that the condition is permanent using clinical examination, radiography, and specialist opinion if needed.",
        "Wow_Approach": "The Centrally Sponsored Livestock Insurance Scheme provides 50% premium subsidy for BPL (Below Poverty Line) livestock owners. Veterinarians employed by government animal husbandry departments are frequently called upon to certify PTD and issue death certificates for insurance claims — a major medicolegal responsibility."
    },
    166: {
        "topic": "Wildlife Protection Act 1972 - Key Year and Mischief IPC Section",
        "Core_Anatomy": "N/A — Legislative timeline and animal crime law.",
        "Pathogenesis_Immediate": "Wildlife Protection Act 1972 came into force to protect India's wildlife heritage. Mischief causing animal death/injury is prosecuted under IPC Sections 428/429. Key dates: WPA 1972, PCA Act 1960, Project Tiger 1973, CITES (ratified by India 1976).",
        "Pathogenesis_Deep": "WPA 1972 key provisions: Section 9 — hunting of any wild animal (Schedule I) prohibited. Section 27 — entry into national parks without permit prohibited. Section 39 — all wild animals are government property. Section 40 — declaration of stocks of animal articles mandatory. Section 49B — prohibition on trade in animal articles. Section 51 — penalties: for Schedule I violations, minimum 3 years, maximum 7 years imprisonment + fine up to Rs.25,000.",
        "Why_Not": "The Forest Conservation Act (1980) protects forest land from diversion to non-forest uses. Environment Protection Act (1986) provides broad environmental safeguards. WPA 1972 specifically protects wild animals and their habitats — these three Acts together form India's environmental protection legal triad.",
        "Wow_Approach": "Project Tiger (1973): Started with 9 reserves. Now 55 Tiger Reserves covering >75,000 sq.km. Tiger census method: Camera trap + pugmark analysis + DNA from hair/scat. Current tiger population (2022 census): ~3,167 tigers — highest in any single country globally."
    },
    169: {
        "topic": "Zoo/Wild Animal Nutrition - Species-Specific Diet Formulation",
        "Core_Anatomy": "The digestive tract adaptations of carnivores (short intestine), herbivores (enlarged caecum/colon), and omnivores (intermediate).",
        "Pathogenesis_Immediate": "Zoo animal nutrition must replicate natural dietary composition, including appropriate macronutrient ratios, micronutrient supplementation (especially fat-soluble vitamins A, D, E, K for carnivores fed processed meat), and food presentation enrichment to stimulate natural foraging behaviours.",
        "Pathogenesis_Deep": "Common zoo nutritional problems: Big cats fed only muscle meat develop Vitamin A deficiency (liver is the dietary source of Vit A), hypocalcaemia (bone is required for calcium), and taurine deficiency (essential amino acid for felids). Primates on fruit-only diets develop iron deficiency and vitamin B12 deficiency. Herbivores overloaded with concentrate feeds develop laminitis and dental abnormalities.",
        "Why_Not": "Wild carnivores naturally eat the whole prey (muscle, organ meat, bone, fur/feathers) providing a complete nutritional profile. Zoo carnivores fed muscle meat alone (common mistake) are nutritionally deficient. Supplementation with complete prey items (day-old chicks, rodents) is preferred over vitamin/mineral powdering.",
        "Wow_Approach": "National Research Council (NRC) Nutrient Requirements provide species-specific minimum nutrient levels. Zoo animals commonly require: Vit D3 supplementation (sun exposure limited in indoor exhibits), taurine for felids, vitamin C for primates (cannot synthesize endogenously), and high-fibre diets for hindgut fermenters to maintain rumen/hindgut microbiome."
    },
    170: {
        "topic": "Canine Ehrlichiosis - Monocytosis as Pathognomonic Feature",
        "Core_Anatomy": "Canine monocytes, the spleen, bone marrow, and peripheral blood lymphocytes.",
        "Pathogenesis_Immediate": "Monocytosis (elevated circulating monocytes >1,500/μL) is a characteristic haematological feature of Canine Ehrlichiosis (*Ehrlichia canis*), a tick-borne rickettsial disease presenting with fever, weight loss, lymphadenopathy, and thrombocytopenia.",
        "Pathogenesis_Deep": "E. canis infects and multiplies within monocytes and macrophages, forming intracytoplasmic morulae (visible on blood smear in 4% of cases). The infected monocytes release cytokines that stimulate further monocyte production from bone marrow. Simultaneously, immune-mediated platelet destruction causes severe thrombocytopenia (platelet count <50,000/μL). Chronic Ehrlichiosis causes pancytopenia from bone marrow plasmacytosis and is often fatal.",
        "Why_Not": "Babesiosis primarily causes haemolytic anaemia with regenerative anaemia and haemoglobinuria. Rocky Mountain Spotted Fever (*Rickettsia rickettsii*) causes neutrophilia + thrombocytopenia. Canine Leishmaniasis causes monocytosis but also hypergammaglobulinaemia and facial alopecia. Ehrlichiosis monocytosis is the most distinctive haematological finding.",
        "Wow_Approach": "Three-phase Ehrlichiosis: (1) Acute (1-4 weeks): Fever, anorexia, lymphadenopathy, mild thrombocytopenia — best treatment response. (2) Subclinical (months-years): Haematology normal or mildly abnormal — dog appears healthy. (3) Chronic: Severe pancytopenia, haemorrhage, weight loss, cachexia — guarded prognosis. Doxycycline treatment is most effective in the acute phase."
    },
    175: {
        "topic": "Animal Welfare Act - Fill in the Blanks (Key Statutory Facts)",
        "Core_Anatomy": "N/A — Animal welfare law statutory knowledge.",
        "Pathogenesis_Immediate": "Key statutory facts tested in Animal Welfare, Ethics and Jurisprudence (VMD 511): Pack animals include horses, mules, and donkeys. Wounds made by sharp cutting weapons (blades, knives) are incised wounds with clean, even margins. The Animal Welfare Board of India (AWBI) is headquartered in Chennai.",
        "Pathogenesis_Deep": "Key definitions for exam blanks: Pack animal — any animal used to carry loads (horses, mules, donkeys, camels, oxen). Incised wound — caused by sharp-edged weapon; even, clean-cut margins, minimal bruising, bleeding prominent. Lacerated wound — caused by blunt weapon or tearing force; irregular, ragged margins, bruised surrounding tissue, less bleeding. Contused wound — bruising without skin break. Puncture wound — narrow deep track from a pointed object.",
        "Why_Not": "Examination-in-Chief (first examination by calling party) uses non-leading questions. Cross-Examination (by opposing party) uses leading questions designed to shake credibility. Re-Examination (by calling party after cross-exam) clarifies, using non-leading questions only on matters raised in cross-examination.",
        "Wow_Approach": "Syncope (fainting) is caused by transient cerebral ischaemia — cardiac origin (arrhythmia, heart block) OR vasovagal response OR orthostatic hypotension. In horses, syncope can occur from cardiac arrhythmia during exercise, mistaken for 'sudden collapse' — ECG Holter monitoring during exercise confirms diagnosis."
    },
    176: {
        "topic": "Wound Classification and Pack Animals in Legal Context",
        "Core_Anatomy": "The skin (epidermis, dermis, subcutis), underlying muscle, and the coagulation cascade.",
        "Pathogenesis_Immediate": "In veterinary jurisprudence, wound classification based on the causative weapon is essential for forensic reports. Wounds are categorized as: Incised (sharp blade), Lacerated (blunt force tearing), Contused (blunt impact without skin break), Puncture (pointed object), and Gunshot wounds.",
        "Pathogenesis_Deep": "Incised wounds from sharp weapons (blades, surgical scalpels): clean, even margins, minimal tissue bridging, brisk haemorrhage, no bruising of surrounding skin. Lacerated wounds from blunt force: irregular, ragged margins, tissue bridging visible across the wound, contused (bruised) margins, less haemorrhage. These distinctions are critical in veterinary forensic casework where animal abuse using different weapons must be documented for legal proceedings.",
        "Why_Not": "A bite wound produces a combination of puncture (canine teeth) and laceration (tearing action). An avulsion wound results from tissue being pulled away from its attachments. Each wound type has specific forensic implications regarding the weapon used and the force applied.",
        "Wow_Approach": "Forensic wound documentation protocol: (1) Measure wound dimensions (L x W x D) in cm. (2) Describe margin character (clean/ragged/contused/inverted/everted). (3) Photograph with scale ruler in frame. (4) Note anatomical location relative to landmarks. (5) Collect wound swabs for microbiology and trace evidence before cleaning. All documentation in ink on standard medicolegal form."
    },
    177: {
        "topic": "Syncope - Cardiac vs Respiratory Origin",
        "Core_Anatomy": "The cardiac conduction system (SA node, AV node), the aortic and carotid baroreceptors, and the vasomotor centre in the medulla.",
        "Pathogenesis_Immediate": "Syncope (fainting/sudden collapse with loss of consciousness) is caused by acute transient cerebral ischaemia, most commonly of CARDIAC origin (arrhythmias, outflow obstruction), NOT respiratory origin. Respiratory causes produce cyanosis and dyspnoea but not acute loss of consciousness.",
        "Pathogenesis_Deep": "Cardiac causes of syncope in animals: Ventricular tachycardia/fibrillation (most dangerous), complete heart block (AV dissociation), sick sinus syndrome (dogs — particularly Miniature Schnauzers), aortic stenosis (Golden Retrievers), pulmonic stenosis. The cerebral blood flow falls below critical threshold (<30 ml/100g/min) within 5-8 seconds, causing loss of consciousness. Recovery is spontaneous if the arrhythmia self-terminates.",
        "Why_Not": "Respiratory causes (laryngeal collapse, tracheal collapse) cause coughing syncope (Cough Syncope/Tussive Syncope) — the only respiratory mechanism of syncope, via vagal reflex causing transient cardiac slowing. Pure respiratory insufficiency causes gradual hypoxia with cyanosis, not sudden syncope.",
        "Wow_Approach": "Differentiate syncope from epileptic seizure: Syncope — flaccid collapse, pale mucous membranes, rapid recovery (seconds), no post-ictal phase, often triggered by exercise/excitement. Seizure — tonic-clonic activity, normal/red mucous membranes, longer recovery (minutes-hours), post-ictal confusion and lethargy."
    },
    178: {
        "topic": "Bestiality (IPC 377) and Zoo Recognition - Key Legal Matches",
        "Core_Anatomy": "N/A — Wildlife law and criminal procedure.",
        "Pathogenesis_Immediate": "Key legal matching pairs in veterinary jurisprudence: Bestiality = IPC 377 (unnatural sexual offences). Mischief killing animals = IPC 428/429. Recognition of Zoos = Central Zoo Authority (CZA) under WPA 1972. Brambell Committee = Five Freedoms (1965).",
        "Pathogenesis_Deep": "IPC 377 (now Section 38 of BNS 2023) criminalizes carnal intercourse against the order of nature, including with animals. Penalty: life imprisonment or up to 10 years + fine. IPC 274/275 relate to adulteration of drugs/food — relevant in veterinary pharmacy fraud cases. The CZA (Central Zoo Authority) was established under Section 38A of WPA 1972 to regulate the recognition, operation, and standards of all zoos in India.",
        "Why_Not": "The PCA Act 1960 Section 11 covers general cruelty. The WPA 1972 covers wildlife protection and zoo regulation. The IPC covers criminal acts against animals as property (IPC 428/429) and as victims of unnatural offences (IPC 377). These three legal frameworks operate concurrently.",
        "Wow_Approach": "The CZA minimum standards for zoo recognition include: Master Plan for the zoo, minimum land area (small zoo: 5 acres, medium: 25 acres, large: 100 acres), qualified veterinarian on staff (mandatory), species-appropriate enclosures, quarantine facility, and a public education programme."
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
print(f"Batch 4/5 DONE: Updated {updated} questions.")
