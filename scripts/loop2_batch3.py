import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    130: {
        "topic": "Wildlife Zoological Names and Necropsy Rules for Notifiable Diseases",
        "Core_Anatomy": "N/A — Wildlife taxonomy and forensic pathology protocol.",
        "Pathogenesis_Immediate": "Key zoological names for Indian wildlife: Bonnet Macaque — *Macaca radiata*. Wild Dog (Dhole) — *Cuon alpinus*. Tiger — *Panthera tigris*. Spotted Deer (Chital) — *Axis axis*. Sambar — *Cervus unicolor*. Carcasses of animals suspected for anthrax must never be opened (to prevent environmental spore contamination).",
        "Pathogenesis_Deep": "Anthrax (*Bacillus anthracis*) spores are released in massive quantities when an anthrax carcass is opened and exposed to atmospheric oxygen. Sporulation occurs when the vegetative bacilli contact air; spores persist in soil for 40-80+ years. Therefore, the primary rule in anthrax-suspected carcasses is: do not open, do not bleed, incinerate or bury with quicklime. A blood smear from a peripheral vessel (ear vein) is the only safe sample.",
        "Why_Not": "For most other notifiable diseases (FMD, BVD, Brucellosis), full necropsy is mandatory. Anthrax is the ONLY major disease where the absolute rule is no carcass opening. In reptiles, full necropsy is performed routinely as they often harbour Salmonella and Cryptosporidium without clinical signs.",
        "Wow_Approach": "Anthrax necropsy rule: Take a drop of blood from the external jugular vein using a needle/syringe, smear on a slide, fix with methanol, and stain with Polychrome Methylene Blue (McFadyean's stain). The distinctive rectangular bamboo-rod shaped bacilli surrounded by a pink capsule are diagnostic."
    },
    133: {
        "topic": "Indian Wild Dog (Dhole) Zoological Name and Deer Species",
        "Core_Anatomy": "Canid (Dhole) and cervid (deer) comparative anatomy and conservation status.",
        "Pathogenesis_Immediate": "The Indian Wild Dog (Dhole) has the zoological name *Cuon alpinus*. It is a Schedule II animal under WPA 1972. Spotted Deer (Chital) = *Axis axis*. Sambar Deer = *Rusa unicolor* (formerly *Cervus unicolor*). These are critical identifications for zoo/wildlife management exams.",
        "Pathogenesis_Deep": "Dholes are highly social, pack-hunting canids that are the apex predators of Indian forests alongside tigers and leopards. Their pack coordination and stamina hunting (exhausting prey over km-long chases) is unique among Asian canids. Dholes are endangered due to prey depletion and disease transmission from domestic dogs (CDV, rabies, parvovirus). Gestation period: 60-63 days. Litter size: 4-8 pups.",
        "Why_Not": "The Indian Fox (*Vulpes bengalensis*) is a solitary canid. The Jackal (*Canis aureus*) is an opportunistic scavenger. The Dhole (*Cuon alpinus*) is a highly specialized pack hunter with unique dentition (only 2 lower molars vs 3 in most canids) and is the only living species of its genus.",
        "Wow_Approach": "Dholes cannot bark but communicate with whistles, clucks, and screams. They have a unique pre-hunt ritual of energetic play and vocalizations. Gestation and litter behaviour is managed in ex-situ conservation programs at Mysuru Zoo and Arignar Anna Zoological Park (Chennai)."
    },
    140: {
        "topic": "IPC Section 299 - Culpable Homicide and Veterinary Negligence",
        "Core_Anatomy": "N/A — Criminal law and veterinary professional liability.",
        "Pathogenesis_Immediate": "IPC Section 299 defines Culpable Homicide — causing death by an act done with the intention of causing death or with knowledge that the act is likely to cause death. In veterinary context, gross negligence causing human death (zoonotic transmission due to negligent handling) can be prosecuted under this section.",
        "Pathogenesis_Deep": "Veterinary negligence can attract criminal liability under: IPC 304A (causing death by negligence — 2 years imprisonment); IPC 337/338 (causing hurt/grievous hurt by negligence); IPC 304 (culpable homicide not amounting to murder — if negligence is reckless). Civil liability (tort of negligence) requires proving: duty of care, breach of duty, causation, and damage. The Bolam Test (UK) standard applies: a veterinarian is not negligent if they act in accordance with a practice accepted by a responsible body of veterinary peers.",
        "Why_Not": "IPC Section 192 relates to fabricating false evidence. IPC Section 156 relates to failure of a police officer to investigate. IPC Section 199 relates to giving false statement on oath. These are distinct from the animal cruelty/negligence provisions under IPC 428/429.",
        "Wow_Approach": "The Consumer Protection Act 2019 covers veterinary services. A client can file a consumer complaint against a veterinarian for deficiency of service. The compensation limit in consumer courts has been enhanced significantly under the 2019 Act. Professional indemnity insurance is strongly recommended for all veterinary practitioners."
    },
    141: {
        "topic": "International Animal Health Code (OIE/WOAH) and Stress Biomarker in Dairy Cows",
        "Core_Anatomy": "The hypothalamic-pituitary-adrenal axis, cortisol synthesis in the adrenal cortex, and adrenal chromaffin cells (epinephrine).",
        "Pathogenesis_Immediate": "The International Animal Health Code is formulated by the WOAH (World Organisation for Animal Health, formerly OIE — Office International des Epizooties), headquartered in Paris. The most reliable serum biomarker for assessing stress in dairy cows is Cortisol.",
        "Pathogenesis_Deep": "Stress in dairy cows activates the HPA axis: Hypothalamic CRH → Pituitary ACTH → Adrenal cortisol synthesis and release. Cortisol causes immunosuppression (neutrophil trapping in circulation, lymphocyte apoptosis), hyperglycaemia (gluconeogenesis), and reproductive suppression (inhibits LH pulsatility). Chronically elevated cortisol in transport-stressed or overcrowded dairy cows causes decreased milk production, increased SCC, and increased susceptibility to mastitis and respiratory disease.",
        "Why_Not": "Total protein is a non-specific marker of hydration status and liver function. Thyroxine (T4) reflects metabolic rate and thyroid function. Serum Amyloid A (SAA) is an acute phase protein reflecting inflammation. Cortisol is the specific HPA-axis activation marker used in validated animal welfare stress assessment protocols.",
        "Wow_Approach": "Non-invasive cortisol measurement from faecal samples (fGCM — faecal glucocorticoid metabolites) is now preferred for wild and zoo animal welfare assessment, avoiding the sampling stress of blood collection. Salivary cortisol is also increasingly used in dogs and horses."
    },
    142: {
        "topic": "Taxidermy, Trophy, and Vermin under WPA 1972",
        "Core_Anatomy": "N/A — Wildlife law definitions.",
        "Pathogenesis_Immediate": "Under the Wildlife Protection Act 1972: Trophy — any animal article including antlers, horns, feathers, skin, or taxidermied specimen. Taxidermy — the art of preserving an animal's body by mounting or stuffing for display. Vermin — Schedule V animals that may be hunted (e.g., common crow, fruit bats, rats) without a licence.",
        "Pathogenesis_Deep": "WPA 1972 Section 2 definitions: Animal Article — any article made from animals/animal parts. Trophy — any animal product that has not undergone complete chemical processing. Taxidermy — preservation and mounting of dead animals. The Chief Wildlife Warden must be notified of any wild animal trophy found. Dealing in or possessing any Schedule I animal trophy without a licence is punishable with 3-7 years imprisonment.",
        "Why_Not": "Cure (in WPA context) means any process of preserving or dressing animal skins. A Cured Trophy is one that has undergone chemical preservation (tanning). The distinction matters because the legality of ownership and transfer differs between uncured trophies (always restricted) and cured trophies (may be transferred with Chief Wildlife Warden permission).",
        "Wow_Approach": "Exam key: Vermin animals (Schedule V) can be hunted without any permit — includes Common Crow (*Corvus splendens*), Fruit Bats, Rats, Mice. All other wildlife requires permits. CITES Appendix I species (most endangered) have the strongest international trade restrictions — equivalent to India's Schedule I."
    },
    143: {
        "topic": "Rights of Accused and Death Sentence in Indian Criminal Law",
        "Core_Anatomy": "N/A — Criminal procedure and rights of the accused.",
        "Pathogenesis_Immediate": "Under the Code of Criminal Procedure (CrPC), the rights of an accused person are protected at every stage of criminal proceedings. A veterinarian accused of gross negligence or animal cruelty has specific legal rights including right to legal representation, right to bail (in bailable offences), and right to fair trial.",
        "Pathogenesis_Deep": "Criminal procedure for animal welfare violations: (1) FIR (First Information Report) lodged at police station. (2) Investigation by police. (3) Charge sheet filed in court. (4) Trial (magistrate court for PCA Act offences). (5) Conviction or acquittal. PCA Act offences are bailable; IPC 428/429 offences may be non-bailable in serious cases. Death sentence is the highest punishment in India, reserved for the 'rarest of rare' murders — not applicable to animal welfare crimes.",
        "Why_Not": "Life imprisonment exceeding 7 years is the second-highest punishment. For PCA Act Section 11 cruelty offences, the maximum punishment is only a fine of Rs.50 for the first offence — this grossly inadequate penalty is a major criticism of the Act.",
        "Wow_Approach": "The Prevention of Cruelty to Animals (Amendment) Bill 2022 proposed significantly enhanced penalties (up to Rs.75,000 fine and 5-year imprisonment), but has not yet been passed into law. Until amendment, IPC 428/429 remains the primary legal tool for serious prosecution."
    },
    144: {
        "topic": "Bestiality (IPC 377 / BNS 2023) and Expert Witness in Court",
        "Core_Anatomy": "N/A — Veterinary forensic examination for sexual abuse of animals.",
        "Pathogenesis_Immediate": "Bestiality (sexual intercourse with animals) is a criminal offence under IPC Section 377 (now Section 38 of BNS 2023). Veterinarians may be called as Expert Witnesses to assess and document evidence of animal sexual abuse.",
        "Pathogenesis_Deep": "Forensic examination for bestiality: Document injuries to perineum, vulva, rectum, or prepuce (lacerations, bruising, haematomas). Collect swabs for human DNA/seminal fluid. Photograph all injuries with scale reference. Prepare a detailed written forensic report. Preserve all samples in sterile containers with chain of custody documentation. This report constitutes documentary evidence admissible in court under the Indian Evidence Act 1872.",
        "Why_Not": "A Barbiturate test is used in veterinary forensics to detect euthanasia drug residues in carcasses (confirming euthanasia vs natural death). Stimulants (Amphetamine) and suppressants used in doping are detected by urine/blood screening — a different area of veterinary forensics.",
        "Wow_Approach": "Veterinary forensic evidence collection must follow strict chain of custody protocols: each sample is sealed, labelled with case number, date, animal ID, and veterinarian signature, and handed to police with a written receipt. Any break in chain of custody can render evidence inadmissible in court."
    },
    145: {
        "topic": "Doping in Animal Sports - Stimulants and Suppressants",
        "Core_Anatomy": "The sympathetic nervous system (stimulants) and the CNS/analgesic pathways (suppressants) in race horses and racing dogs.",
        "Pathogenesis_Immediate": "Doping in equine and canine sports uses two major categories: Stimulants (increase arousal, speed, and aggression) and Suppressants (mask pain, reduce anxiety, reduce movement detection in detection animals). Both are prohibited under racing rules and animal welfare legislation.",
        "Pathogenesis_Deep": "Common equine doping agents: Stimulants — Amphetamine, Cocaine, Caffeine (increase sympathetic drive, raise HR and cardiac output). Suppressants — Acepromazine (tranquilliser), Buprenorphine (opioid analgesic for masking lameness pain), Flunixin Meglumine (NSAID masking musculoskeletal pain). Detection methods: Post-race urine/blood sampling, analyzed by GC-MS (Gas Chromatography-Mass Spectrometry) for detection of parent compounds or metabolites.",
        "Why_Not": "Unlike human sports doping (enhancement of performance), veterinary doping can also be suppressant-based (masking lameness to run an unfit horse). Both types are equally prohibited because: stimulants are cruelty (forced performance beyond capacity), and suppressants are dangerous (a horse with masked pain may catastrophically fracture during racing).",
        "Wow_Approach": "Detection windows vary: Amphetamine detectable in urine for 48-72 hours. Acepromazine metabolites detectable for 96 hours. NSAIDs (Phenylbutazone) detectable for 7-10 days. Racing authorities maintain withdrawal time databases (Equine Prohibited Substances database) that veterinarians must consult before treating competing horses."
    },
    146: {
        "topic": "Rigor Mortis, Wound Classification and Documentary Evidence",
        "Core_Anatomy": "Skeletal muscle (actin-myosin cross bridges), the skin and subcutaneous tissue, and the cardiovascular system post-mortem.",
        "Pathogenesis_Immediate": "Rigor Mortis is the post-mortem stiffening of skeletal muscles due to irreversible actin-myosin cross-bridge formation following depletion of ATP. Wound margins help classify weapon type; Documentary Evidence includes written records, photographs, and laboratory reports admissible in court.",
        "Pathogenesis_Deep": "Rigor Mortis onset: 2-6 hours post-death (depletion of ATP causes cross-bridge locking). Duration: 24-48 hours. Resolution: after 48-72 hours (proteolysis by muscle enzymes). Rate is temperature-dependent: faster in hot environments, slower in cold. Wound classification: Sharp weapon = even, clean-cut wound margins with minimal surrounding bruising. Blunt weapon = irregular, lacerated, contused margins. Firearm = entry wound (small, circular, inverted edges) vs exit wound (large, stellate, everted edges).",
        "Why_Not": "Rigor Mortis must be differentiated from ante-mortem muscle spasm (cadaveric spasm/instantaneous rigor) — the latter occurs immediately at the moment of death from extreme emotional stress or nervous exhaustion and indicates the body position at death. True rigor mortis takes 2-6 hours to establish.",
        "Wow_Approach": "For forensic time-of-death estimation use all three post-mortem changes together: Rigor Mortis (time since death 2-48 hrs), Livor Mortis/Hypostasis (blood pooling, fixed after 6-8 hrs), and Algor Mortis (cooling rate ~1°C/hr in ambient conditions). Insect activity (forensic entomology) is used for time-of-death estimates beyond 72 hours."
    },
    151: {
        "topic": "Transport of Animals Rules - Dogs, Cats and Schedule Coverage",
        "Core_Anatomy": "N/A — Animal transport welfare legislation.",
        "Pathogenesis_Immediate": "Rules 4-14 of the Prevention of Cruelty to Animals (Transport of Animals) Rules 2001 apply specifically to the transport of dogs and cats, prescribing minimum cage dimensions, ventilation, water provision, and maximum journey durations.",
        "Pathogenesis_Deep": "Transport requirements for dogs/cats under PCA Rules: Individual cages (no group transport of adult dogs). Minimum cage dimensions: Length = body length + 10 cm; Width = body width x2; Height = standing height + 5 cm. Bedding: Dry, absorbent material. Temperature range: 7-29°C. Feed and water access every 6 hours. Health certificate mandatory. Sedation is NOT permitted during air/rail transport (sedated animals cannot respond to temperature/hypoxia changes).",
        "Why_Not": "IATA Live Animal Regulations (LAR) govern international air transport of animals, which are more stringent than Indian domestic rules. For exotic animals (CITES listed), a CITES import/export permit is required in addition to the fitness certificate.",
        "Wow_Approach": "The landmark animal welfare case in India regarding transport: Amidst the COVID-19 lockdowns, the AWBI issued specific guidelines for movement of animals during emergencies. Veterinarians must be aware that animal welfare law continues to apply even during declared national emergencies."
    },
    152: {
        "topic": "Indian Rock Python and Cobra - Classification Under WPA 1972",
        "Core_Anatomy": "Ophidian (snake) anatomy: the fang apparatus, heat-pit organs (pythons), and venom gland.",
        "Pathogenesis_Immediate": "The Indian Rock Python (*Python molurus*) is a non-venomous constrictor and a Schedule I protected species under WPA 1972. The Indian Cobra (*Naja naja*) is a venomous elapid snake, also Schedule II protected.",
        "Pathogenesis_Deep": "Python molurus is one of the world's largest snakes (up to 6 m). It is a constrictor (kills by coiling and asphyxiation, not venom). Loreal pits on the labial scales detect infrared radiation for prey detection. Cobra (*Naja naja*) is a proteroglyphous elapid with hollow fixed front fangs. Its venom is primarily neurotoxic (post-synaptic alpha-bungarotoxin blocking acetylcholine receptors at the NMJ) causing flaccid paralysis.",
        "Why_Not": "The Russell's Viper (*Daboia russelii*) is solenoglyphous (retractable hollow fangs) and has a hemotoxic/cytotoxic venom causing DIC and renal failure. The Krait (*Bungarus caeruleus*) has neurotoxic venom causing pre-synaptic blockade and nocturnal biting. Pythons are non-venomous — their danger is strictly mechanical constriction.",
        "Wow_Approach": "Antivenom treatment for cobra bite: Polyvalent Anti-Snake Venom Serum (ASVS) manufactured by Haffkine Bio-pharmaceutical or VINS BioProducts. Administer 10 vials IV initially, repeat if neostigmine challenge test shows improvement. Atropine (0.6 mg IV) must always precede neostigmine administration."
    },
    153: {
        "topic": "Feline Infectious Peritonitis (FIP) - Rivolta's Test",
        "Core_Anatomy": "The peritoneum, pleural cavity, and macrophages in domestic cats.",
        "Pathogenesis_Immediate": "Rivolta's Test (Nonne-Apelt test) is used to detect the high protein content in the effusion fluid of cats with Feline Infectious Peritonitis (FIP), distinguishing it from transudate effusions.",
        "Pathogenesis_Deep": "FIP is caused by a virulent mutant of Feline Coronavirus (FCoV) that infects macrophages. In the wet (effusive) form, immune complex deposition causes complement-mediated vasculitis in the peritoneal/pleural vessels, producing a straw-yellow, viscous, high-protein effusion (exudate). Rivolta's Test: Mix 1 drop of effusion with 1 ml of glacial acetic acid. A white turbid precipitate (Pandy's reaction positive) indicates high protein = exudate = suggestive of FIP. Clear = transudate.",
        "Why_Not": "Feline Chylothorax produces a milky-white, triglyceride-rich effusion (chyle) that is Rivolta's negative. Cardiac effusion is a clear, low-protein transudate that is also Rivolta's negative. Only high-protein exudates (FIP, pyothorax) are Rivolta's positive.",
        "Wow_Approach": "FIP is now treatable with Remdesivir (GS-5734) or GS-441524 — nucleoside analogues that inhibit FCoV RNA-dependent RNA polymerase. Previously considered 100% fatal, FIP now has >85% remission rates with 84 days of GS-441524 treatment. This is one of the most important recent advances in feline medicine."
    },
    154: {
        "topic": "Brachycephalic Airway Obstruction Syndrome (BAOS) in Pugs",
        "Core_Anatomy": "The nares, nasopharynx, soft palate, larynx, and trachea of brachycephalic breeds.",
        "Pathogenesis_Immediate": "Brachycephalic Airway Obstruction Syndrome (BAOS) is a complex of anatomical abnormalities in brachycephalic breeds (Pug, English Bulldog, French Bulldog, Boston Terrier) causing severe upper respiratory obstruction.",
        "Pathogenesis_Deep": "BAOS components: (1) Stenotic nares (narrowed nostrils) — primary resistance to airflow. (2) Elongated soft palate — obstructs the glottis during inspiration. (3) Hypoplastic trachea — reduced tracheal lumen. (4) Everted laryngeal saccules — secondary to chronic increased negative inspiratory pressure. These combine to cause chronic hypoxia, exercise intolerance, heat stroke susceptibility, and sleep apnoea.",
        "Why_Not": "German Shepherds have a dolichocephalic head structure and are prone to degenerative myelopathy and hip dysplasia, not BAOS. Golden Retrievers are mesocephalic. BAOS is strictly a brachycephalic breed problem linked to selective breeding for extreme facial flattening.",
        "Wow_Approach": "Surgical correction (done before 2 years of age gives best results): rhinoplasty (widening stenotic nares), soft palate resection (staphylectomy — remove excess 3-4 mm), and saccule removal. Post-op: cool environment, supplemental oxygen, anti-inflammatory corticosteroids. BAOS dogs must never be sedated without intubation equipment immediately available — airway collapse at induction is the primary anaesthetic risk."
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
