import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1752: {
        "topic": "Canine Parvovirus - Hemagglutination Test",
        "Core_Anatomy": "Viral capsid and porcine erythrocytes.",
        "Pathogenesis_Immediate": "The Hemagglutination (HA) and Hemagglutination Inhibition (HI) tests are classically used for the diagnosis of Canine Parvovirus-2 (CPV-2) infections.",
        "Pathogenesis_Deep": "CPV-2 possesses specific viral capsid proteins that naturally bind to the sialic acid receptors on the surface of erythrocytes (specifically porcine or rhesus macaque RBCs). When fecal extracts containing the virus are mixed with these RBCs in a microtiter plate, the virus cross-links the red blood cells, causing them to form a diffuse lattice (hemagglutination) rather than a tight button. Adding specific anti-CPV antibodies will inhibit this reaction (HI), confirming the virus's identity.",
        "Why_Not": "Infectious Canine Hepatitis (ICH) and Canine Distemper (CD) do not robustly hemagglutinate porcine RBCs in standard benchtop assays like Parvovirus does.",
        "Wow_Approach": "While PCR and rapid SNAP (ELISA) tests have largely replaced the HA test in clinics, HA remains the gold standard in diagnostic laboratories for quantifying viral shedding titers."
    },
    1753: {
        "topic": "Avian Influenza - RT-PCR Diagnosis",
        "Core_Anatomy": "Viral RNA genome.",
        "Pathogenesis_Immediate": "The most reliable, rapid, and definitive test for the diagnosis of Avian Influenza is RT-PCR (Reverse Transcription Polymerase Chain Reaction).",
        "Pathogenesis_Deep": "Avian Influenza is an Orthomyxovirus, meaning its genome consists of segmented, single-stranded RNA. Standard PCR only amplifies DNA. Therefore, the viral RNA must first be converted into complementary DNA (cDNA) by the enzyme Reverse Transcriptase (RT) before the PCR amplification step can occur. RT-PCR allows for extreme sensitivity and can specifically type the hemagglutinin (H5/H7) genes to immediately determine if the strain is Highly Pathogenic (HPAI).",
        "Why_Not": "ELISA detects antibodies or antigens but lacks the sensitivity and genetic typing capability of RT-PCR. VNT (Virus Neutralization Test) takes days to weeks to grow the virus in eggs.",
        "Wow_Approach": "In an outbreak scenario (e.g., thousands of dead chickens), waiting 7 days for a viral culture is unacceptable. RT-PCR provides a definitive diagnosis within 4-6 hours, allowing for immediate legal depopulation."
    },
    1754: {
        "topic": "African Horse Sickness - Natural Reservoir",
        "Core_Anatomy": "Vascular endothelium (Zebras) and Culicoides midges.",
        "Pathogenesis_Immediate": "The primary natural reservoir of African Horse Sickness (AHS) is the Zebra.",
        "Pathogenesis_Deep": "AHS is a highly fatal Orbivirus transmitted by Culicoides biting midges. Through thousands of years of co-evolution in sub-Saharan Africa, Zebras have developed a high degree of natural resistance. They experience a transient, subclinical viremia when infected, acting as a perfect amplifier and reservoir for the virus without dying. When the midges feed on the Zebras and then bite naive, highly susceptible horses, the horses develop massive pulmonary edema and die rapidly (often with frothy fluid pouring from the nostrils).",
        "Why_Not": "Mules are moderately susceptible and often die. Cattle and Deer are not the primary maintenance reservoirs for this specific equine Orbivirus.",
        "Wow_Approach": "Because AHS is an OIE/WOAH listed disease with up to 90% mortality in horses, importing zebras from Africa to zoos worldwide requires extreme quarantine protocols to prevent introducing the virus into native midge populations."
    },
    1755: {
        "topic": "Veterinary Public Health - Trichinoscopy",
        "Core_Anatomy": "Skeletal muscle (diaphragm and masseter).",
        "Pathogenesis_Immediate": "A Trichinoscope is a specialized projection microscope historically used in abattoirs to diagnose Trichinella spiralis cysts in pork.",
        "Pathogenesis_Deep": "Trichinella spiralis is a zoonotic nematode. Pigs become infected by eating raw meat scraps or rats. The adult worms breed in the pig's gut, and the larvae migrate to heavily oxygenated, active skeletal muscles (specifically the diaphragm pillars, masseters, and tongue), where they encyst. To prevent human infection, meat inspectors compress small samples of these muscles between two heavy glass plates (a compressorium) and examine them under the trichinoscope to visualize the coiled larvae.",
        "Why_Not": "Oxyuris (pinworms), Trichuris (whipworms), and Metastrongylus (lungworms) do not encyst in skeletal muscle; they remain in the GI or respiratory tracts.",
        "Wow_Approach": "Modern abattoirs have largely replaced the labor-intensive trichinoscope method with the 'Artificial Digestion' method, where pooled muscle samples are dissolved in pepsin/HCl to free the larvae for easier detection."
    },
    1756: {
        "topic": "Avian Pathology - Marek's Disease",
        "Core_Anatomy": "Sciatic nerve and peripheral nervous system.",
        "Pathogenesis_Immediate": "Severe unilateral or bilateral Sciatic nerve enlargement is the pathognomonic gross lesion seen in Marek's disease.",
        "Pathogenesis_Deep": "Marek's disease is caused by an Alphaherpesvirus (Gallid alphaherpesvirus 2). The virus is highly oncogenic, causing the massive neoplastic proliferation of T-lymphocytes. In the classic neurological form of the disease, these neoplastic T-cells heavily infiltrate the peripheral nerves, specifically the sciatic nerve. The nerve loses its normal white, striated appearance and becomes swollen, gray, and edematous (often 2-3 times its normal thickness). This destroys the nerve's function, causing the classic 'spastic paralysis' where the chicken lies with one leg stretched forward and the other pulled back.",
        "Why_Not": "Newcastle disease and ILT (Infectious Laryngotracheitis) cause respiratory and CNS signs, but NOT gross peripheral nerve enlargement. Mucosal disease affects cattle.",
        "Wow_Approach": "On necropsy of a paralyzed bird, you must dissect out BOTH the left and right sciatic nerves to compare them; often, only one side is massively enlarged."
    },
    1757: {
        "topic": "Veterinary Jurisprudence - Glanders and Farcy Act",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The Glanders and Farcy Act, an early piece of veterinary legislation in India, was enacted in the year 1899.",
        "Pathogenesis_Deep": "Because Glanders (Burkholderia mallei) was a highly fatal, zoonotic disease that decimated cavalry and transport horses in the late 19th century, the British Indian government enacted the Glanders and Farcy Act of 1899. This act provided immense statutory powers to veterinary inspectors to legally enter premises, test horses (using mallein), and mandate the immediate destruction and deep burial/burning of positive reactors without the owner's consent.",
        "Why_Not": "1890, 1892, and 1893 are incorrect dates. 1899 is the landmark year for this specific equine legislation.",
        "Wow_Approach": "Although originally enacted for Glanders, the Act was later legally amended to include the control of other devastating equine diseases like Epizootic Lymphangitis and Surra."
    },
    1758: {
        "topic": "Toxicology - Blood Coloration Diagnostics",
        "Core_Anatomy": "Erythrocytes (hemoglobin oxidation states).",
        "Pathogenesis_Immediate": "The color of the blood is a rapid diagnostic indicator in toxicology: Nitrate poisoning causes Chocolate brown blood, while Cyanide causes Bright red blood.",
        "Pathogenesis_Deep": "(1) Nitrate/Nitrite Poisoning: Rumen bacteria convert nitrates into toxic nitrites. Nitrite oxidizes the Fe2+ (ferrous) iron in hemoglobin to Fe3+ (ferric) iron, forming Methemoglobin. Methemoglobin cannot bind oxygen and physically turns the blood a dark, muddy, 'chocolate' brown. (2) Cyanide Poisoning: Cyanide completely blocks Cytochrome C Oxidase in the cellular mitochondria. The cells cannot extract oxygen from the blood. Therefore, the venous blood remains fully saturated with oxygen, returning to the heart as a striking, 'bright cherry red'.",
        "Why_Not": "Pink blood is not a standard toxicological finding. Dark red is normal venous blood. The extremes (Chocolate vs Cherry Red) are the pathognomonic toxicological clues.",
        "Wow_Approach": "If a cow dies suddenly in a pasture and the blood from the nose is chocolate brown, treat the rest of the herd with IV Methylene Blue. If the blood is bright cherry red, treat with IV Sodium Thiosulfate."
    },
    1768: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces questions that require pairing a specific disease, drug, or pathogen with its corresponding pathognomonic feature.",
        "Pathogenesis_Deep": "Matching questions test the clinician's ability to rapidly associate a specific clinical etiology with its most distinctive diagnostic or therapeutic hallmark, without the context of a full clinical case.",
        "Why_Not": "Process of elimination is critical here, as one incorrect match often guarantees a second incorrect match.",
        "Wow_Approach": "Always match the most obvious, indisputable pairs first (e.g., specific antidotes or classic anatomical lesions) to narrow down the remaining ambiguous options."
    },
    1769: {
        "topic": "Veterinary Pharmacology - Triclabendazole",
        "Core_Anatomy": "Hepatic parenchyma and bile ducts.",
        "Pathogenesis_Immediate": "Triclabendazole is uniquely matched to the treatment of Fascioliasis (Liver Fluke infection).",
        "Pathogenesis_Deep": "Fasciola hepatica causes severe liver damage. The immature flukes migrate through the liver parenchyma (causing acute fascioliasis), while the adults live in the bile ducts (causing chronic fascioliasis). Triclabendazole is the ONLY benzimidazole anthelmintic that is highly efficacious against BOTH the 1-week-old migrating early immature flukes AND the adult flukes. It works by inhibiting microtubule formation and disrupting the fluke's tegument (skin).",
        "Why_Not": "Canine ehrlichiosis is treated with Doxycycline. Toxoplasmosis is treated with Clindamycin. Standard albendazole only kills adult liver flukes, not the deadly immatures.",
        "Wow_Approach": "Because it kills the early migrating stages, Triclabendazole is the absolute drug of choice for acute outbreaks of liver fluke in sheep during the autumn."
    },
    1770: {
        "topic": "Equine Neurology - Kumri",
        "Core_Anatomy": "Cerebrospinal fluid and spinal cord.",
        "Pathogenesis_Immediate": "Kumri is the Indian colloquial term matched to Cerebrospinal Nematodiasis (specifically caused by the erratic migration of Setaria digitata).",
        "Pathogenesis_Deep": "Setaria digitata is a filarial nematode whose normal host is cattle (where it lives harmlessly in the peritoneal cavity). However, if an infected mosquito bites a horse (an aberrant host), the microfilariae migrate erratically into the central nervous system instead of the abdomen. The migrating worms physically tunnel through the spinal cord, causing severe focal malacia (necrosis). This results in an acute, progressive, asymmetric ataxia and paresis of the hindlimbs, historically known in India as 'Kumri' (weakness of the loins).",
        "Why_Not": "It is not caused by Toxoplasmosis or Ehrlichiosis. It is a specific aberrant helminth migration.",
        "Wow_Approach": "Because the damage is mechanical (a worm drilling through the spinal cord), anthelmintic treatment (like Ivermectin) will kill the worm, but the neurological deficits in the horse are often permanent due to the irreversible scarring."
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
