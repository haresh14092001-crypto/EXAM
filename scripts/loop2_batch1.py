import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    86: {
        "topic": "CSF Pressure in Vitamin A Deficiency and Molybdenum-Copper Antagonism",
        "Core_Anatomy": "The choroid plexus, the arachnoid granulations (CSF reabsorption), and the optic nerve sheath.",
        "Pathogenesis_Immediate": "Vitamin A deficiency increases CSF pressure (Pseudotumour Cerebri) by impairing arachnoid granulation reabsorption of CSF. Excess dietary Molybdenum causes secondary copper deficiency by forming thiomolybdate complexes in the rumen that block copper absorption.",
        "Pathogenesis_Deep": "In Vit A deficiency: Retinoic acid is essential for normal glycoprotein synthesis in the choroid plexus and arachnoid villi. Deficiency impairs CSF reabsorption, causing intracranial hypertension. In ruminants, this manifests as optic nerve pressure atrophy and blindness. In Molybdenum excess: Mo + S in the rumen form tetrathiomolybdate (TM), which tightly binds copper both in the gut (preventing absorption) and in blood (chelating systemic copper), causing functional copper deficiency even when dietary copper appears adequate.",
        "Why_Not": "Primary copper deficiency is rare on well-managed pastures. The most common cause of copper deficiency in cattle grazing high-molybdenum/high-sulphur pastures (Teart pastures in UK) is secondary/conditioned copper deficiency caused by thiomolybdate formation, not low copper intake.",
        "Wow_Approach": "Diagnose secondary copper deficiency by the Mo:Cu ratio in feed and blood. Correct by supplementing with injectable copper glycinate or oral copper sulphate. Increase dietary copper supplementation above NRC recommendations when pasture Mo exceeds 5 ppm (normal: <3 ppm)."
    },
    87: {
        "topic": "Diagnostic Biochemical Tests for Mineral Deficiencies",
        "Core_Anatomy": "The renal tubular epithelium (calcium/magnesium excretion), hepatic parenchyma (zinc storage), and the adrenal cortex.",
        "Pathogenesis_Immediate": "Specific biochemical tests are used to diagnose mineral deficiencies: Sulkowich Test (calcium in urine), Xylidil Blue Test (magnesium in serum/urine), and gross pathological/histological findings for zinc, copper, and selenium deficiencies.",
        "Pathogenesis_Deep": "Sulkowich test: Oxalic acid precipitates calcium as calcium oxalate from urine; absence of precipitate = hypocalcaemia. Xylidil Blue (Calmagite) test: This chromogenic dye forms a coloured complex with magnesium ions in alkaline solution; intensity of colour correlates with magnesium concentration. Peat Scours (Molybdenosis-induced copper deficiency on peaty soils) causes depigmentation, diarrhoea, and unthriftiness — diagnosed by blood copper and liver copper analysis.",
        "Why_Not": "Peat Scours is not a primary molybdenum toxicosis — it is the secondary copper deficiency caused by the interaction of molybdenum and sulphate in peat soils. The Sulkowich test is purely qualitative (bedside test), while the Xylidil Blue test can be quantitative when performed on a spectrophotometer.",
        "Wow_Approach": "Always pair Sulkowich and Xylidil Blue tests with a full blood panel (albumin, total protein, BUN) in periparturient cows, as concurrent hypoalbuminaemia lowers total serum calcium even when ionized calcium is normal, creating a pseudo-hypocalcaemia picture."
    },
    94: {
        "topic": "PETA and Animal Welfare Legislation in India (PCA Act 1960)",
        "Core_Anatomy": "N/A — Legal and regulatory framework.",
        "Pathogenesis_Immediate": "The Prevention of Cruelty to Animals (PCA) Act, 1960 is the primary Indian legislation protecting animals from unnecessary pain and suffering. It established the Animal Welfare Board of India (AWBI) as a statutory advisory body.",
        "Pathogenesis_Deep": "Key provisions of PCA Act 1960: Section 11 defines cruelty offences (overloading, beating, mutilating, abandoning, etc.). Section 35 mandates that anyone who keeps a performing animal must register with the CPCSEA (Committee for the Purpose of Control and Supervision of Experiments on Animals). Transport of animals is regulated under Prevention of Cruelty to Animals (Transport) Rules 2001, and slaughter under the Slaughter House Rules 2001.",
        "Why_Not": "PETA (People for the Ethical Treatment of Animals) is a non-governmental animal rights organization, not a statutory government body. The AWBI is the statutory government body constituted under Section 4 of the PCA Act 1960, advising the government on animal welfare matters.",
        "Wow_Approach": "Key exam facts: PCA Act came into force in 1960. AWBI headquarters: Chennai. Chairperson of AWBI is appointed by the Central Government. CPCSEA oversees animal experiments under the Drugs and Cosmetics Act. Wildlife Protection Act (1972) provides absolute legal protection to Schedule I animals."
    },
    96: {
        "topic": "Animal Welfare Board of India (AWBI) - Powers and Constitution",
        "Core_Anatomy": "N/A — Statutory and regulatory body.",
        "Pathogenesis_Immediate": "The Animal Welfare Board of India (AWBI) is a statutory body constituted under Section 4 of the Prevention of Cruelty to Animals (PCA) Act 1960. The Central Government can remove any member of the AWBI for stated reasons including misconduct, incapacity, or conflict of interest.",
        "Pathogenesis_Deep": "AWBI composition: 5 Members of Parliament, 6 persons representing animal welfare organizations, 2 veterinarians, a government representative, 3 persons representing municipal corporations in large cities, and the Director of the Zoological Survey of India, among others. Total: 28 members. The AWBI advises the government on animal welfare amendments and maintains a register of performing animals.",
        "Why_Not": "CPCSEA (Committee for Control and Supervision of Experiments on Animals) is a different body constituted under Rule 13 of the Breeding of and Experiments on Animals (Control and Supervision) Rules 1998, specifically overseeing experiments on animals, not general welfare.",
        "Wow_Approach": "Key AWBI facts for exams: AWBI was established in 1962. Headquarters: Chennai (Tamil Nadu). Annual grants from the Central Government fund its operations. AWBI conducts inspections of gaushalas, animal markets, and slaughterhouses. Performing animals must be registered under Section 26 of the PCA Act."
    },
    99: {
        "topic": "Wildlife Protection Act 1972 - National Parks, Sanctuaries and Schedules",
        "Core_Anatomy": "N/A — Conservation law and protected area framework.",
        "Pathogenesis_Immediate": "The Wildlife Protection Act (WPA), 1972 is the primary Indian legislation for wildlife conservation. It provides absolute protection to Schedule I species (e.g., Tiger, Lion, Leopard, Elephant) and regulates hunting, trade, and habitat protection through a National Park and Wildlife Sanctuary system.",
        "Pathogenesis_Deep": "WPA 1972 Schedules: Schedule I — Absolute protection (no hunting or trade). Schedule II — Partial protection. Schedule III & IV — Lesser-protected animals and plants. Schedule V — Vermin (may be hunted). Schedule VI — Protected plants. National Parks are areas of highest protection (no human activities allowed). Wildlife Sanctuaries allow limited human activities. Tiger Reserves are designated under Project Tiger (1973).",
        "Why_Not": "The Environment Protection Act (1986) provides broad environmental protection powers. The Forest Conservation Act (1980) regulates forest land diversion. The WPA 1972 specifically regulates wildlife, hunting, and trade in wildlife products (trophies, animal articles). All three acts work together for comprehensive biodiversity protection.",
        "Wow_Approach": "Key WPA facts: First Indian National Park: Jim Corbett (1936). CITES (Convention on International Trade in Endangered Species) is the international equivalent. India has 106 National Parks and 567 Wildlife Sanctuaries. Tiger Project 2.0 uses camera traps and radio collars for census. Schedule I violation carries imprisonment up to 7 years."
    },
    101: {
        "topic": "PCA Act - Weight Limits for Animal Transport",
        "Core_Anatomy": "N/A — Animal transport welfare regulation.",
        "Pathogenesis_Immediate": "Under the Prevention of Cruelty to Animals Act (Transport of Animals Rules 2001), specific weight and number limits are prescribed for transporting animals in vehicles to prevent overcrowding and suffering.",
        "Pathogenesis_Deep": "Key transport rules under PCA Act 2001: Maximum weight of cattle per transport vehicle: 750 kg per vehicle for large cattle. Poultry: 4 birds per crate for broilers. Sheep/Goats: Maximum 36 per vehicle compartment. No animal should be transported for more than 48 hours without feed and water. Pregnant animals in advanced gestation, animals with young calves, and animals that are ill are prohibited from transport. Veterinary fitness certificate required for all transport.",
        "Why_Not": "The Transport of Animals Rules 2001 specifically covers livestock transport. The Motor Vehicles Act governs road transport logistics. For air transport, IATA Live Animal Regulations apply. For sea transport, the IMSBC Code applies. All modes require species-specific container dimensions and environmental controls.",
        "Wow_Approach": "Common exam question: The number of cattle allowed per goods vehicle — Answer: Depends on vehicle capacity and animal weight. Large cattle (>300 kg): 6 per vehicle. Small cattle: 12 per vehicle. These limits are strictly enforced by police checkposts; veterinary certificates must accompany every animal consignment."
    },
    102: {
        "topic": "Animal Welfare Board of India - Funding and Grants",
        "Core_Anatomy": "N/A — Statutory funding and governance.",
        "Pathogenesis_Immediate": "The funds of the Animal Welfare Board of India (AWBI) consist of grants made by the Central Government, donations from private individuals and organizations, and income from AWBI publications and activities.",
        "Pathogenesis_Deep": "Under Section 9 of the PCA Act 1960, the AWBI's fund is used to: (1) Award grants to animal welfare organizations and gaushalas. (2) Fund research on animal welfare. (3) Conduct public awareness campaigns. (4) Finance inspections of animal facilities. The AWBI's annual report is submitted to Parliament. All grants require utilization certificates from recipient organizations.",
        "Why_Not": "State Animal Welfare Boards (SAWBs) are separate bodies constituted by individual state governments under their respective state-level PCA rules. They are funded by state governments and operate independently under the umbrella of the Central AWBI.",
        "Wow_Approach": "The AWBI's biggest practical contribution is funding approximately 3,000+ Pinjarapoles (animal shelters/gaushalas) across India, providing refuge for injured, sick, and abandoned animals. Recognition as an AWBI-approved gaushala comes with funding eligibility and inspection oversight."
    },
    103: {
        "topic": "Prevention of Cruelty to Animals Act - Year of Commencement (1960)",
        "Core_Anatomy": "N/A — Legislative history.",
        "Pathogenesis_Immediate": "The Prevention of Cruelty to Animals (PCA) Act came into force in 1960, replacing the older Cruelty to Animals Act of 1890. It is the cornerstone animal protection legislation in India.",
        "Pathogenesis_Deep": "Historical context: The PCA Act 1960 was enacted during the first term of the Indian Parliament, reflecting India's commitment to the Directive Principles of the Constitution (Article 48: organization of agriculture and animal husbandry; Article 51A(g): duty to protect wildlife and have compassion for living creatures). The Act has been amended several times, with the 1982 amendment establishing the CPCSEA.",
        "Why_Not": "The Wildlife Protection Act was enacted in 1972 (12 years after PCA Act 1960). The Environment Protection Act in 1986. The Biological Diversity Act in 2002. Chronological sequence for exams: PCA 1960 → WPA 1972 → EPA 1986 → BDA 2002.",
        "Wow_Approach": "Key PCA Act sections for board exams: Section 3 (duty of owners to animals), Section 11 (cruelty offences — most commonly tested), Section 14 (experiments on animals require registration), Section 26 (performing animals registration), Section 38 (powers of entry/inspection). Section 11 violation = fine up to Rs. 50 (original) — the derisory penalty has been the subject of major reform advocacy."
    },
    104: {
        "topic": "Permitted vs Prohibited Animal Procedures under PCA Act Section 11",
        "Core_Anatomy": "N/A — Legal definitions of cruelty vs. permitted procedures.",
        "Pathogenesis_Immediate": "Section 11 of the PCA Act 1960 defines acts of cruelty to animals. Certain procedures (dehorning, castration, branding, tattooing) are explicitly permitted when performed by veterinarians following prescribed standards, while others (overloading, beating with cruel instruments, abandonment) are prohibited.",
        "Pathogenesis_Deep": "Permitted procedures under PCA Act: Dehorning (when performed with proper anaesthesia by a qualified vet). Castration (with appropriate analgesics). Ear notching for identification. Branding for permanent identification. Prohibited acts: Overloading any animal. Causing unnecessary pain during transport. Working a sick/injured/pregnant animal. Abandoning an animal in circumstances likely to cause suffering. Using any animal for performance after an age of 6 months without registration.",
        "Why_Not": "The PCA Act distinguishes between 'necessary' procedures (veterinary treatment, breed improvement, agricultural purposes) and 'unnecessary' infliction of pain. The legal standard is whether a reasonable person would consider the action to cause unnecessary suffering.",
        "Wow_Approach": "Under the PCA Act (Transport Rules), No person shall transport any animal which is pregnant, or which has delivered recently within 10 days, or which has not attained the age of 4 months. Neonates and pregnant animals have absolute transport protection under Indian law."
    },
    105: {
        "topic": "Farriery and Equine Hoof Care Legislation",
        "Core_Anatomy": "The equine hoof capsule, the sensitive laminae, the digital cushion, and the coffin bone (distal phalanx/P3).",
        "Pathogenesis_Immediate": "A Farrier is a specialist trained in equine hoof care, including trimming, balancing, and fitting horseshoes. Improper shoeing causes lameness (laminitis, navicular syndrome, white line disease) and is considered an act of cruelty if done negligently.",
        "Pathogenesis_Deep": "The equine hoof is a complex structure that bears the entire body weight of the horse. Proper farriery requires trimming the hoof at the correct angle (50-55° for forelimbs), balancing the mediolateral axis, and fitting shoes that distribute weight evenly. The Lamellar interface (sensitive and insensitive laminae) is the primary structural support between P3 and the hoof wall — disruption from incorrect shoeing causes rotation of P3 (founder/laminitis).",
        "Why_Not": "A Cobbler works with leather goods and footwear for humans. A Farrier specifically works with equine hooves and horseshoes. In India, farriery is regulated under the PCA Act as proper hoof care is considered essential for equine welfare.",
        "Wow_Approach": "Signs of poor farriery requiring immediate veterinary intervention: flaring of the hoof wall, long toe/low heel conformation, under-run heels, white line separation, and 'seedy toe' (fungal invasion of the white line). Regular 6-8 week farriery cycles are mandatory for working equines."
    },
    106: {
        "topic": "Transport of Cattle - PCA Act Rules for Goods Vehicles",
        "Core_Anatomy": "N/A — Animal welfare during transportation regulation.",
        "Pathogenesis_Immediate": "Under the Prevention of Cruelty to Animals (Transport of Animals) Rules 2001, the maximum number of cattle allowed per goods vehicle is specified to prevent overcrowding-related stress, injuries, and deaths during transit.",
        "Pathogenesis_Deep": "Transport stress ('transit fever') causes cortisol-mediated immunosuppression in cattle. Overcrowded vehicles cause physical injuries from trampling, hyperthermia from body heat accumulation, dehydration from excessive panting, and severe weight loss. PCA Transport Rules mandate: adequate ventilation, non-slip flooring, availability of feed and water during journeys exceeding 6 hours, veterinary fitness certificates, and prohibition of transport in the hottest part of the day (10 AM to 4 PM in summer).",
        "Why_Not": "The number per vehicle varies by animal class: Large cattle (buffaloes/cows >300 kg): 6 per truck. Small cattle (calves/sheep/goats): higher numbers with minimum space allocations. Poultry: separate crate regulations under the Prevention of Cruelty to Animals (Poultry Birds Transport) Rules.",
        "Wow_Approach": "Cattle transported for more than 12 hours must be unloaded, rested, fed, and watered for at least 6 hours before re-loading. All transporters must carry a signed Form A (transport fitness certificate issued by a veterinarian) and maintain transport records for inspection by animal welfare officers."
    },
    107: {
        "topic": "Veterinary Health Certificate for Animal Transport (PCA Act)",
        "Core_Anatomy": "N/A — Veterinary certification and documentation.",
        "Pathogenesis_Immediate": "A Certificate of Fitness (Form A) must be issued by a registered Veterinary Doctor certifying the health and fitness of animals for transport under the Prevention of Cruelty to Animals (Transport of Animals) Rules 2001, before any livestock consignment can legally move across state lines.",
        "Pathogenesis_Deep": "The fitness certificate must state: species, number, age, sex, breed, owner's name and address, destination, mode of transport, absence of infectious/contagious disease, fitness for transport. The certificate is valid for 10 days from date of issue. For interstate transport, the certificate must be countersigned by the District Veterinary Officer (DVO). Absence of a valid certificate is a violation of the PCA Act.",
        "Why_Not": "The Certificate of Fitness for transport is distinct from: (1) the Slaughter Fitness Certificate (issued before slaughter). (2) The Import/Export Health Certificate (for international movement, issued under the Livestock Importation Act). (3) The Brucellosis-free certificate required for cattle movement across some state borders.",
        "Wow_Approach": "The veterinarian issuing a transport fitness certificate is legally responsible for the accuracy of the health declaration. Issuing a false certificate constitutes professional misconduct under the Veterinary Council of India (VCI) Code of Ethics and is punishable under IPC Section 197 (false certificate by a public servant)."
    },
    108: {
        "topic": "Terminology - Young Ones of Farm Animals",
        "Core_Anatomy": "N/A — Veterinary terminology and species identification.",
        "Pathogenesis_Immediate": "Correct species-specific terminology for young animals is essential in legal documents, veterinary certificates, and clinical records. The young one of a goat below one year of age is called a Kid.",
        "Pathogenesis_Deep": "Standard veterinary terminology for young ones: Cattle — Calf (up to 6 months: calf; 6-12 months: weaner). Horse — Foal (male: colt foal; female: filly foal). Donkey — Foal. Sheep — Lamb. Goat — Kid. Pig — Piglet. Dog — Puppy. Cat — Kitten. Rabbit — Kitten/Kit. Deer — Fawn. Elephant — Calf. Camel — Calf. Buffalo — Calf.",
        "Why_Not": "The term 'Lamb' refers specifically to a young sheep, not a goat. Misidentifying species in legal or transport documents can result in regulatory violations. The term 'Cub' is used for young carnivores (lion cubs, tiger cubs, bear cubs) but is incorrect for domestic species.",
        "Wow_Approach": "A 'Wether' is a castrated male goat or sheep. A 'Barrow' is a castrated male pig. A 'Steer' is a castrated bull. A 'Capon' is a castrated male chicken. These castrated-animal terms frequently appear in veterinary jurisprudence and livestock management exam questions."
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

print(f"Batch 1/5 DONE: Updated {updated} questions.")
