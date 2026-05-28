import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1979: {
        "topic": "Equine Glanders - Diagnostics",
        "Core_Anatomy": "Cutaneous and respiratory immune systems.",
        "Pathogenesis_Immediate": "Glanders (Burkholderia mallei) in equines is classically diagnosed using the Mallein test.",
        "Pathogenesis_Deep": "The Mallein test relies on a Type IV delayed hypersensitivity reaction, fundamentally similar to the Tuberculin test. A purified protein derivative (mallein) from the bacterium is injected intrapalpebrally (into the eyelid) or applied as eye drops. In an infected horse, sensitized memory T-cells rapidly migrate to the eye, causing massive, purulent conjunctivitis and severe swelling of the eyelid within 48 hours.",
        "Why_Not": "Histoplasmosis and Salmonellosis do not utilize the Mallein test. Hemorrhagic septicemia is diagnosed via blood smears and culture.",
        "Wow_Approach": "Because Glanders is highly zoonotic and fatal to humans, a positive Mallein test in a horse legally mandates immediate euthanasia without any attempt at treatment."
    },
    1982: {
        "topic": "Colibacillosis - Adhesins (Fimbriae)",
        "Core_Anatomy": "Intestinal microvilli.",
        "Pathogenesis_Immediate": "Adhesins (specifically fimbriae or pili) are the absolute prerequisite virulence factors for Enterotoxigenic E. coli (ETEC) to cause disease.",
        "Pathogenesis_Deep": "Before ETEC can secrete its deadly enterotoxins (LT and ST), it must physically anchor itself to the host's intestinal lining to avoid being flushed out by peristalsis. It does this using highly host-specific protein appendages called fimbriae. In calves, the specific fimbria is K99 (F5); in piglets, it is K88 (F4). These fimbriae bind strictly to specific glycoprotein receptors on the enterocyte surface.",
        "Why_Not": "If an E. coli strain has toxins but no adhesins, it simply passes through the gut harmlessly.",
        "Wow_Approach": "Vaccines for neonatal scours don't target the toxins; they are specifically designed to produce antibodies against these fimbriae (anti-K99 antibodies), completely blocking the bacteria from ever attaching to the gut wall."
    },
    1990: {
        "topic": "Toxoplasmosis - Gold Standard Diagnosis",
        "Core_Anatomy": "Toxoplasma tachyzoites.",
        "Pathogenesis_Immediate": "The absolute 'Gold standard' reference test for the serological diagnosis of Toxoplasmosis is the Sabin-Feldman dye test.",
        "Pathogenesis_Deep": "The Sabin-Feldman dye test is a highly specific neutralization test. Live Toxoplasma gondii tachyzoites are mixed with the patient's serum and a complement protein. Normally, live tachyzoites will take up Methylene Blue dye. However, if the patient has antibodies against Toxoplasma, the antibodies (with complement) lyse the parasite's membrane, preventing it from absorbing the dye. A lack of blue staining indicates a positive test.",
        "Why_Not": "While ELISA and PCR are commonly used in modern clinics due to safety, the Sabin-Feldman dye test remains the definitive, international reference standard.",
        "Wow_Approach": "Because this test requires maintaining a constant supply of LIVE, highly infectious Toxoplasma tachyzoites, it is only performed in high-security reference laboratories, not in standard veterinary clinics."
    },
    1991: {
        "topic": "Veterinary Forensics - Doping Tests",
        "Core_Anatomy": "Systemic plasma.",
        "Pathogenesis_Immediate": "During routine equine doping control, the anticoagulant most commonly used for blood collection to preserve drugs is Heparin.",
        "Pathogenesis_Deep": "In equine sports medicine, forensic blood samples must be collected to detect illegal performance-enhancing drugs (like NSAIDs, steroids, or stimulants). Heparin is often preferred for toxicological/doping plasma screens because it does not heavily alter the pH or precipitate out specific drug metabolites the way citrate or heavy metal salts might. It works by activating Antithrombin III, preventing clot formation and yielding high-quality plasma.",
        "Why_Not": "EDTA is preferred for complete blood counts (CBCs) because it preserves cell morphology perfectly, but it chelates calcium and can interfere with certain mass-spectrometry drug assays.",
        "Wow_Approach": "For forensic doping samples, two identical vials (the 'A' and 'B' samples) must be drawn simultaneously; if the 'A' sample tests positive, the owner has the legal right to demand the 'B' sample be tested at an independent laboratory."
    },
    1992: {
        "topic": "Blood Transfusion - Anticoagulants",
        "Core_Anatomy": "Erythrocytes (cellular metabolism).",
        "Pathogenesis_Immediate": "Acid Citrate Dextrose (ACD) and Citrate Phosphate Dextrose (CPD) are specific anticoagulants utilized for long-term whole blood storage (transfusions).",
        "Pathogenesis_Deep": "Unlike Heparin or EDTA which are used for diagnostic testing, ACD and CPD are designed to keep red blood cells alive in a refrigerator for 21-35 days. The Citrate acts as the anticoagulant by chelating calcium. The Dextrose (glucose) provides the essential energy substrate for the RBCs to continue anaerobic glycolysis. The Phosphate acts as a buffer to maintain ATP levels and stabilize the pH.",
        "Why_Not": "Heparinized blood cannot be stored; the RBCs will die within 24-48 hours.",
        "Wow_Approach": "Because ACD/CPD heavily chelates calcium, performing a massive, rapid blood transfusion in a dog can inadvertently cause acute, fatal hypocalcemia."
    },
    1993: {
        "topic": "Ovine Fascioliasis - Acute Treatment",
        "Core_Anatomy": "Hepatic parenchyma (migrating flukes).",
        "Pathogenesis_Immediate": "The absolute drug of choice for treating acute fascioliasis in sheep is Triclabendazole.",
        "Pathogenesis_Deep": "Acute fascioliasis is caused by the simultaneous, massive migration of thousands of immature Fasciola hepatica flukes through the liver parenchyma, causing severe hemorrhage and traumatic hepatitis. Most flukicides (like Albendazole or Oxyclozanide) ONLY kill adult flukes in the bile ducts. Triclabendazole is unique; it is highly efficacious against early immature flukes (as young as 1 week old) migrating through the liver tissue, immediately stopping the fatal destruction.",
        "Why_Not": "Oxyclozanide and Closantel are only effective against adults or late immatures (6-8 weeks old), making them useless for saving a sheep currently dying from acute liver rupture.",
        "Wow_Approach": "Because Triclabendazole is used so heavily during acute autumn outbreaks, severe flukicide resistance has developed worldwide, requiring strategic rotation with Closantel where possible."
    },
    1994: {
        "topic": "Rabies Vaccinology - Minimum Antigenic Potency",
        "Core_Anatomy": "Systemic immunity (Neutralizing Antibodies).",
        "Pathogenesis_Immediate": "According to the WHO and WOAH, the minimum required antigenic concentration in each dose of a commercial cell-culture Rabies vaccine is > 2.5 IU.",
        "Pathogenesis_Deep": "Rabies is a 100% fatal zoonotic disease. To ensure absolute protection, international regulatory standards legally mandate that every single manufactured vial of rabies vaccine (whether for dogs, cats, or humans) must contain a minimum potency of 2.5 International Units (IU) of inactivated rabies antigen per dose. This ensures the animal mounts a robust humoral response (minimum neutralizing antibody titer of 0.5 IU/mL in the blood) to prevent the virus from entering the CNS.",
        "Why_Not": "Values like > 0.5 IU or > 1.0 IU are insufficient for the vaccine itself (though 0.5 IU/mL is the target blood titer post-vaccination). The vaccine dose must be > 2.5 IU.",
        "Wow_Approach": "If an animal travels internationally, the titer test (FAVN/RFFIT) must prove their blood level is above 0.5 IU/mL, which is only achievable if the original vaccine contained the mandatory > 2.5 IU potency."
    },
    1995: {
        "topic": "VMD Objective Section - True/False Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces statements requiring absolute evaluation of clinical facts.",
        "Pathogenesis_Deep": "These questions test whether the clinician can identify the single fatal flaw in a complex pathophysiological statement.",
        "Why_Not": "Partial correctness is not accepted.",
        "Wow_Approach": "Always read the entire statement twice; the first half may be true, while the second half contains the fatal flaw."
    },
    2006: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces questions requiring the clinician to pair specific diseases with pathognomonic diagnostic tests or features.",
        "Pathogenesis_Deep": "Matching questions test rapid associative recall without the benefit of a full clinical vignette.",
        "Why_Not": "A single incorrect guess often causes a cascade of incorrect matches.",
        "Wow_Approach": "Match the most definitive, universally known pairs first to narrow down the remaining options."
    },
    2007: {
        "topic": "Leptospirosis - Microscopic Agglutination Test (MAT)",
        "Core_Anatomy": "Systemic antibodies.",
        "Pathogenesis_Immediate": "The acronym MAT stands for the Microscopic Agglutination Test, which is the definitive gold standard diagnostic test for Leptospirosis.",
        "Pathogenesis_Deep": "Leptospira interrogans has over 250 different serovars (e.g., Icterohaemorrhagiae, Canicola, Hardjo). The MAT is the only test that can identify exactly which serovar is infecting the animal. The patient's serum is serially diluted and mixed with live, motile cultures of various Leptospira serovars. The mixture is examined under a dark-field microscope. If antibodies are present, they cause the live spirochetes to clump together (agglutinate).",
        "Why_Not": "Fowl typhoid (Salmonella Gallinarum) is diagnosed via standard plate agglutination or culture, not the MAT.",
        "Wow_Approach": "Because the MAT requires maintaining a library of dangerous, LIVE Leptospira cultures, it is strictly performed in specialized reference laboratories."
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
