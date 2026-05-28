import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2104: {
        "topic": "Ovine/Caprine Enterotoxemia - Dietary Trigger",
        "Core_Anatomy": "Small intestine (starch overload and Clostridium perfringens Type D).",
        "Pathogenesis_Immediate": "A presumptive diagnosis of enterotoxemia is based on sudden death in lambs and kids fed with a Carbohydrate-rich (high-starch/grain) diet.",
        "Pathogenesis_Deep": "Clostridium perfringens Type D produces the lethal Epsilon toxin only when the rumen/intestine is flooded with rapidly fermentable carbohydrates. High-starch feeds (grain, lush pasture) that overwhelm the normal digestive capacity pass into the small intestine undigested, providing explosive growth media for Type D clostridia. The resulting toxin production causes rapid brain and kidney damage (Pulpy Kidney Disease).",
        "Why_Not": "A protein-rich or fat-rich diet does not trigger the specific starch-driven clostridial overgrowth required for Epsilon toxin production.",
        "Wow_Approach": "Vaccinate ewes with a clostridial bacterin 4-6 weeks before lambing to ensure high maternal antibody levels in colostrum, passively protecting lambs during the highest-risk early weeks of life."
    },
    2106: {
        "topic": "Rumen pH - Normal Value",
        "Core_Anatomy": "Rumen microbial ecosystem.",
        "Pathogenesis_Immediate": "The normal, healthy physiological pH of the bovine rumen is approximately 6.2–6.8.",
        "Pathogenesis_Deep": "The rumen operates as a continuous fermentation vat. Billions of microbes (bacteria, protozoa, fungi) ferment dietary carbohydrates into volatile fatty acids (VFAs: acetate, propionate, butyrate) and produce CO2 and methane. This fermentation is inherently acidifying. The buffering capacity of copious bovine saliva (containing sodium bicarbonate and phosphate) neutralizes excess acid to maintain the optimal pH range of 6.2-6.8 for cellulolytic bacterial activity.",
        "Why_Not": "A pH above 6.8 (alkalotic rumen) indicates inadequate fermentation or very poor diet. A pH below 6.0 indicates sub-acute ruminal acidosis (SARA), and below 5.5 indicates acute lactic acidosis, causing massive microbiome death.",
        "Wow_Approach": "Rumenocentesis (directly measuring rumen pH via percutaneous needle aspiration) is the definitive clinical technique for diagnosing Sub-Acute Ruminal Acidosis (SARA) in dairy herds."
    },
    2107: {
        "topic": "Listeriosis Treatment - Drug of Choice",
        "Core_Anatomy": "Brainstem (intracellular pathogen).",
        "Pathogenesis_Immediate": "The drug of choice for treatment of Listeriosis is Chloramphenicol (or high-dose Penicillin G).",
        "Pathogenesis_Deep": "Listeria monocytogenes is an obligate intracellular pathogen; it actively survives inside macrophages. This makes treatment very challenging because the antibiotic must penetrate not just the blood-brain barrier, but also the macrophage membrane. Chloramphenicol and ampicillin penetrate the blood-brain barrier exceptionally well and are bacteriostatic against Listeria at achievable CSF concentrations. Treatment must begin immediately (before irreversible brainstem damage) and continue for a prolonged period (3-4 weeks) to prevent relapse.",
        "Why_Not": "Tylosin and Gentamicin have poor CNS penetration and no established efficacy against Listeria in the brain. Chlortetracycline is not preferred for CNS Listeriosis.",
        "Wow_Approach": "If caught very early (the animal is still ambulatory), aggressive IV Penicillin G (22,000 IU/kg every 6 hours) can dramatically reduce mortality. Once the animal is recumbent and comatose, the prognosis is grave regardless of treatment."
    },
    2108: {
        "topic": "Equine Tetanus - Antitoxin Dosage (Repeated)",
        "Core_Anatomy": "Neuromuscular junction.",
        "Pathogenesis_Immediate": "Passive immunity against tetanus in horses following a wound is achieved by administration of Tetanus Antitoxin at 1500–3000 IU.",
        "Pathogenesis_Deep": "Tetanus Antitoxin is pre-formed hyperimmune equine serum containing high titers of anti-tetanospasmin antibodies. Given immediately after a deep puncture wound in an unvaccinated horse, it instantly neutralizes any free toxin in the bloodstream (the toxin that has already bound to nerve endings cannot be displaced). The protection lasts approximately 2-3 weeks.",
        "Why_Not": "The Tetanus Toxoid vaccine initiates active immunity but takes 2-3 weeks—too slow to protect against imminent toxin production. Antitoxin provides the bridge.",
        "Wow_Approach": "Always give both Antitoxin (passive protection NOW) AND Toxoid (active protection for the FUTURE) simultaneously at different injection sites when treating an unvaccinated horse with a traumatic wound."
    },
    2109: {
        "topic": "Brucellosis Herd Screening - Milk Ring Test (Repeated)",
        "Core_Anatomy": "Mammary gland secretions (IgA/IgG antibodies in milk).",
        "Pathogenesis_Immediate": "At the herd level, lactating cows are screened against Brucellosis using the Abortus Bang Ring Test (ABR test / Milk Ring Test).",
        "Pathogenesis_Deep": "The ABR/Milk Ring Test detects Brucella antibodies directly in bulk tank milk. Blue-stained killed Brucella antigen is added to bulk milk. If antibodies are present, they bind to the antigen and adhere to milk fat globules. As the fat rises to form the cream layer, it carries the blue antigen-antibody complexes upward, creating a vivid blue ring in the cream layer above clear white milk—indicating the herd contains at least one infected cow.",
        "Why_Not": "The Rose Bengal Plate Agglutination test (RBPT) and Tube Agglutination Test (TAT) are performed on individual blood serum samples, not bulk milk.",
        "Wow_Approach": "The ABR test is so sensitive it can detect one infected cow per 100 in a herd bulk tank sample, making it the most cost-effective surveillance tool for Brucellosis in dairy herds."
    },
    2110: {
        "topic": "Brucellosis Screening - ABR Test Continuation",
        "Core_Anatomy": "Bulk tank milk antibodies.",
        "Pathogenesis_Immediate": "The Abortus Bang Ring (ABR) test is the continuation/correct answer for bulk milk herd-level brucellosis screening.",
        "Pathogenesis_Deep": "This MCQ option is the continuation from the previous question. The ABR test (also called the Brucella Milk Ring Test) utilizes pre-stained, killed Brucella antigens that bind specific anti-Brucella IgA antibodies in milk, producing a positive cream-layer ring result.",
        "Why_Not": "Tube Agglutination Test requires serum and is not practical for bulk herd milk screening.",
        "Wow_Approach": "Herds testing positive on ABR must have all individual cows blood-tested to identify and cull the specific reactors."
    },
    2111: {
        "topic": "Avian Salmonellosis - Bronze Liver (Fowl Typhoid Repeated)",
        "Core_Anatomy": "Hepatic parenchyma.",
        "Pathogenesis_Immediate": "The bronze liver is a characteristic post-mortem lesion observed in Salmonellosis, specifically Fowl Typhoid (Salmonella Gallinarum).",
        "Pathogenesis_Deep": "Salmonella Gallinarum causes acute septicemia in adult chickens. The liver undergoes massive hepatomegaly with severe multifocal necrosis and bile stasis, imparting a distinctive metallic bronze or mahogany-brown discoloration. This is due to the combination of hepatocellular destruction, iron pigment deposition from hemolysis, and elevated biliverdin (the avian equivalent of bilirubin) concentrations.",
        "Why_Not": "Pullorum Disease (Salmonella Pullorum) primarily causes white diarrhea in chicks (Bacillary White Diarrhea), not the bronze liver of adults. Avian Mycoplasmosis causes air sacculitis and joint disease.",
        "Wow_Approach": "Both Pullorum and Gallinarum can be detected by the same simple Rapid Plate Agglutination (RPA) test using a stained whole blood antigen; positive birds must be culled immediately."
    },
    2112: {
        "topic": "Equine Glanders - Strauss Reaction",
        "Core_Anatomy": "Peritoneal cavity (male guinea pig).",
        "Pathogenesis_Immediate": "The Strauss test (Strauss reaction) is a classical biological diagnostic test used specifically for the diagnosis of Glanders.",
        "Pathogenesis_Deep": "The Strauss reaction is performed by intraperitoneally injecting suspected nasal discharge from a horse with Glanders into a male guinea pig. If the material contains Burkholderia mallei, the bacteria will specifically localize in the guinea pig's peritoneum and the tunica vaginalis of the testicles. Within 3-5 days, the guinea pig develops severe orchitis (massive, swollen, inflamed testicles), which is pathognomonic for Glanders. Post-mortem reveals peritoneal nodules containing pure B. mallei cultures.",
        "Why_Not": "The Mallein test is the standard ante-mortem test in the live horse. The Strauss test is the definitive biological test when other methods are inconclusive.",
        "Wow_Approach": "The Strauss test is rarely performed today given biosafety concerns with maintaining live B. mallei cultures; PCR and ELISA have replaced it in modern reference labs."
    },
    2120: {
        "topic": "VPM Fill in the Blanks Section Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This section focuses on precise recall of epidemiological facts about major infectious diseases.",
        "Pathogenesis_Deep": "Commonly tested values include incubation periods, serotypes, notifiable disease categories, and specific epidemiological thresholds.",
        "Why_Not": "Approximate answers are insufficient; exact nomenclature and values are required.",
        "Wow_Approach": "High-yield fills: FMD incubation = 2-14 days; Rabies incubation in dogs = 14-90 days; Anthrax OIE incubation = 20 days."
    },
    2130: {
        "topic": "FMD - Predominant Serotypes in India",
        "Core_Anatomy": "Viral capsid and host receptor binding.",
        "Pathogenesis_Immediate": "In India, the predominantly prevalent FMD virus serotypes are O, A, and Asia-1.",
        "Pathogenesis_Deep": "Foot and Mouth Disease Virus (FMDV) exists as 7 serotypes (O, A, C, SAT-1, SAT-2, SAT-3, Asia-1). India is exclusively in the Asia-1 ecological zone. Serotype O is the most globally common and dominates Indian outbreaks. Serotype A and Asia-1 also circulate. Because there is NO cross-protection between serotypes, vaccines must contain all three relevant Indian serotypes. India's national FMD-Control Program (FMD-CP) uses a trivalent vaccine covering O, A, and Asia-1.",
        "Why_Not": "SAT-1, SAT-2, and SAT-3 serotypes are endemic to sub-Saharan Africa and have never established in India.",
        "Wow_Approach": "Even within serotype O, topotypes (geographic lineages like O/ME-SA/Ind-2001) can emerge with mutations in the VP1 protein that reduce vaccine coverage, requiring constant genomic surveillance."
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
print(f"Batch 4/5 DONE: Updated {updated} questions.")
