import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1977: {
        "topic": "Brucellosis Screening - Milk Ring Test (MRT)",
        "Core_Anatomy": "Mammary gland and bulk milk.",
        "Pathogenesis_Immediate": "At the herd level, lactating dairy cows are most efficiently screened for Brucellosis using the Brucella Milk Ring Test (MRT).",
        "Pathogenesis_Deep": "If a cow is infected with Brucella abortus, she will secrete IgA and IgG antibodies directly into her milk. In the MRT, a drop of blue-stained, killed Brucella antigen is added to a test tube of whole, unpasteurized milk. If antibodies are present, they bind the blue antigen and physically attach to the fat globules. As the fat naturally rises to the top of the tube to form the cream layer, it carries the blue antigen-antibody complexes with it, forming a distinct, deep blue ring at the top of the white milk column.",
        "Why_Not": "The Rose Bengal plate agglutination test (RBPT) is used on individual blood serum, not bulk herd milk.",
        "Wow_Approach": "The MRT is incredibly sensitive; it can detect a single infected cow's milk diluted in the bulk tank milk of up to 100 healthy cows, making it the perfect initial herd surveillance tool."
    },
    1980: {
        "topic": "Veterinary Jurisprudence - PCA Act 1960",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The foundational animal welfare legislation in India, the Prevention of Cruelty to Animals (PCA) Act, was enacted in 1960.",
        "Pathogenesis_Deep": "The PCA Act of 1960 replaced the colonial-era 1890 Act. It established the comprehensive legal definition of 'cruelty' (including beating, starving, overloading, and abandoning animals) and mandated the creation of the Animal Welfare Board of India (AWBI). It also provided the statutory framework for regulating experimentation on animals (CPCSEA).",
        "Why_Not": "1972 is the Wildlife Protection Act. 1960 is strictly the PCA Act.",
        "Wow_Approach": "Under Section 11 of the PCA Act, a registered veterinarian's written certificate stating that an animal is suffering incurably is the legal requirement for authorized euthanasia."
    },
    1981: {
        "topic": "Colibacillosis - ETEC Virulence Factors",
        "Core_Anatomy": "Intestinal mucosa (enterocytes).",
        "Pathogenesis_Immediate": "The major virulence factors associated with Enterotoxigenic Escherichia coli (ETEC) include Heat-labile enterotoxin (LT), Heat-stable enterotoxin (ST), and specialized Adhesins (fimbriae).",
        "Pathogenesis_Deep": "ETEC causes fatal secretory diarrhea in neonates without causing cellular damage. The pathogenesis requires a two-step mechanism: (1) Adhesion: The bacteria must first physically anchor to the enterocyte microvilli using specific fimbriae (like K99 in calves or K88 in piglets) so they aren't washed away by peristalsis. (2) Toxigenesis: Once attached, they secrete LT (which increases cAMP) and ST (which increases cGMP). These toxins force the enterocytes to hyper-secrete chloride and water, leading to massive dehydration.",
        "Why_Not": "If an E. coli strain has the toxin but lacks the fimbriae (or vice versa), it is completely avirulent and cannot cause disease.",
        "Wow_Approach": "Because the toxins do not destroy the gut lining, the diarrhea is purely watery and non-hemorrhagic, unlike Salmonella or Parvovirus."
    },
    1983: {
        "topic": "Equine Tetanus - Passive Immunity",
        "Core_Anatomy": "Neuromuscular junction and systemic circulation.",
        "Pathogenesis_Immediate": "Passive immunity against tetanus in adult horses following a deep puncture wound is achieved by the immediate administration of Tetanus Antitoxin (typically 1500 - 3000 IU).",
        "Pathogenesis_Deep": "If a horse with an unknown or lapsed vaccination history sustains a deep, anaerobic wound, it is at high risk for Clostridium tetani infection. The bacteria will rapidly produce the lethal tetanospasmin toxin. Because a standard Toxoid vaccine takes 2-3 weeks to generate an active antibody response, it is too slow to save the horse. Instead, pre-formed Tetanus Antitoxin (hyperimmune serum from another horse) is injected to instantly bind and neutralize any free toxin in the bloodstream before it can reach the CNS.",
        "Why_Not": "Toxoid provides active, long-lasting immunity. Antitoxin provides passive, immediate, but short-lived (2-3 weeks) protection.",
        "Wow_Approach": "Because it is equine serum, injecting Tetanus Antitoxin carries a small but documented risk of triggering Theiler's Disease (Equine Serum Hepatitis) several weeks later."
    },
    1984: {
        "topic": "Porcine Pseudorabies - Latent Carriers",
        "Core_Anatomy": "Trigeminal ganglion (Central Nervous System).",
        "Pathogenesis_Immediate": "Adult pigs that have clinically recovered from Pseudorabies (Aujeszky's Disease) act as lifelong 'Latent carriers'.",
        "Pathogenesis_Deep": "Pseudorabies is caused by Suid alphaherpesvirus 1 (PrV). Like all herpesviruses, once the acute infection resolves, the virus travels retrogradely up the sensory nerves and establishes latency (dormancy) in the trigeminal ganglion. The pig appears perfectly healthy and sheds no virus. However, periods of severe stress (farrowing, transport) cause immunosuppression, allowing the virus to reactivate, travel back down the nerve, and be shed in nasal/oral secretions, infecting naive piglets in the herd.",
        "Why_Not": "An incubatory carrier sheds before showing signs. A convalescent carrier sheds while recovering. A latent carrier harbors the pathogen indefinitely in a dormant state.",
        "Wow_Approach": "While pigs are the natural reservoir and can survive, if this herpesvirus infects a dog or cow (usually via ingestion of raw pork), it causes 'Mad Itch'—a rapidly fatal encephalitis with intense, self-mutilating pruritus."
    },
    1985: {
        "topic": "Veterinary Jurisprudence - Cruelty Definitions",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "Under the PCA Act, 'Overloading' a draft animal (like a bullock cart) is legally considered a punishable act of cruelty.",
        "Pathogenesis_Deep": "Section 11 of the PCA Act explicitly defines acts of cruelty. Beating, kicking, torturing, starving, and overloading an animal beyond its physical capacity are all criminal offenses. However, the Act contains specific exemptions for standard, accepted veterinary and agricultural practices. Operations like castration, dehorning of cattle (if done using accepted veterinary methods with anesthesia/analgesia as required), and branding are legally exempt from the definition of cruelty.",
        "Why_Not": "Veterinary procedures performed for the ultimate welfare or standard management of livestock are protected under the law.",
        "Wow_Approach": "If a farmer dehorns an adult cow using a blunt axe without local anesthesia, it ceases to be an exempted agricultural practice and becomes prosecutable cruelty."
    },
    1986: {
        "topic": "Equine Infectious Anemia - Anemia Classification",
        "Core_Anatomy": "Erythrocytes and bone marrow.",
        "Pathogenesis_Immediate": "The type of anemia classically observed in the chronic phase of Equine Infectious Anemia (EIA) is Normocytic and Normochromic.",
        "Pathogenesis_Deep": "In EIA, the lentivirus triggers immune-mediated destruction of red blood cells (hemolysis) and suppresses bone marrow erythropoiesis. Because horses do not release reticulocytes (immature, large, polychromatophilic RBCs) from their bone marrow into peripheral circulation even under severe anemic stress, the circulating red blood cells that remain are of normal size (normocytic) and normal hemoglobin concentration (normochromic).",
        "Why_Not": "Macrocytic (large cell) or hypochromic (pale cell) anemias are typically seen in regenerative responses (like in dogs/cats) or iron deficiency, but the equine bone marrow's strict retention of reticulocytes prevents this appearance in peripheral blood.",
        "Wow_Approach": "Never look for reticulocytes in a horse's blood smear to determine if an anemia is regenerative; you must rely on serial PCV monitoring or a bone marrow aspirate."
    },
    1987: {
        "topic": "Avian Pathology - Infectious Bursal Disease (Gumboro)",
        "Core_Anatomy": "Bursa of Fabricius (B-lymphocytes).",
        "Pathogenesis_Immediate": "A 'Drop in egg production' is NOT a feature of Infectious Bursal Disease (IBD), because IBD exclusively affects young, growing chicks long before they reach laying age.",
        "Pathogenesis_Deep": "IBD (Gumboro disease) is caused by a Birnavirus that strictly targets actively developing B-lymphocytes in the Bursa of Fabricius. The bursa is only active in young birds; it naturally atrophies and disappears as the bird reaches sexual maturity (16-20 weeks). Therefore, adult laying hens do not have a bursa, cannot be clinically infected with IBD, and will not suffer an egg drop from this specific virus.",
        "Why_Not": "Newcastle Disease, Infectious Laryngotracheitis (ILT), and Infectious Bronchitis (IB) all aggressively infect adult layers, causing severe drops in egg production and misshapen eggs.",
        "Wow_Approach": "IBD destroys the immune system of a 3-week-old chick, making it completely incapable of mounting an immune response to subsequent vaccinations (like Newcastle disease vaccines), leading to secondary fatal outbreaks."
    },
    1988: {
        "topic": "Veterinary Forensics - Animal Identification",
        "Core_Anatomy": "Cutaneous features and body condition.",
        "Pathogenesis_Immediate": "In legal cases of animal theft, the description of a stolen animal may be artificially altered by thieves through clipping, painting, or docking, but NOT by starvation.",
        "Pathogenesis_Deep": "Cattle rustlers and horse thieves actively try to alter the physical description of a stolen animal to evade police detection before sale. They will dock (amputate) the tail, clip the mane/coat, or use hair dye (painting) to change white markings into solid colors. Starvation is a systemic metabolic state that causes emaciation; while it makes the animal look poorly, it does not intentionally mask the animal's permanent anatomical identifying marks (like brands, whorls, or scars).",
        "Why_Not": "Physical alterations (docking, dyeing) permanently or semi-permanently change the 'signalment' (description) on a police report.",
        "Wow_Approach": "Forensic veterinarians can easily detect fraudulent 'painting' by applying alcohol or acetone to suspicious coat markings; natural hair color will not wipe off."
    },
    1989: {
        "topic": "Bovine Theileriosis - Koch's Blue Bodies",
        "Core_Anatomy": "Lymphocytes and erythrocytes.",
        "Pathogenesis_Immediate": "Pathognomonic structures called 'Koch's blue bodies' are observed in the stained blood or lymph node smears of cattle infected with Theileriosis.",
        "Pathogenesis_Deep": "Theileria annulata (Tropical Theileriosis) is a tick-borne protozoan. When an infected tick bites a cow, the sporozoites enter the cow's lymphocytes. Inside the lymphocyte cytoplasm, they replicate into a massive, multinucleated mass called a 'Macroschizont'. When stained with Giemsa and viewed under a microscope, these macroschizonts appear as distinct, granular, bright blue masses next to the lymphocyte nucleus. These are historically termed 'Koch's blue bodies'.",
        "Why_Not": "Babesia forms pear-shaped piroplasms inside red blood cells, not macroschizonts in lymphocytes. Trypanosomes are extracellular flagellates swimming in the plasma.",
        "Wow_Approach": "To definitively diagnose acute Theileriosis before severe anemia sets in, do not just take a blood smear; perform a Fine Needle Aspirate (FNA) of the massively swollen prescapular lymph node, as it will be packed with Koch's blue bodies."
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
