import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2273: {
        "topic": "Clostridium perfringens Type D - Overeating Disease",
        "Core_Anatomy": "Small intestine and brain (Epsilon toxin target).",
        "Pathogenesis_Immediate": "Clostridium perfringens Type D is matched to 'Overeating Disease' (Pulpy Kidney Disease / Enterotoxemia).",
        "Pathogenesis_Deep": "C. perfringens Type D produces Epsilon toxin, a potent protoxin activated by intestinal trypsin. When the intestine is flooded with excess starch (from overeating grain or lush pasture), Type D proliferates explosively. The activated Epsilon toxin destroys the vascular endothelium of the gut and brain, causing rapid, fatal cerebral edema and renal autolysis. The 'Overeating Disease' name reflects the direct dietary trigger.",
        "Why_Not": "Type A causes gas gangrene and necrotic enteritis (poultry). Type B causes lamb dysentery. Type C causes 'struck' in sheep. ONLY Type D produces Epsilon toxin causing Pulpy Kidney.",
        "Wow_Approach": "Prophylactic vaccination of pregnant ewes 4-6 weeks before lambing transfers high antibody levels to colostrum, protecting lambs against Epsilon toxin during the highest-risk period."
    },
    2281: {
        "topic": "VPM Fill in the Blanks Section Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This section requires precise recall of epidemiological figures, disease control facts, and legislative details.",
        "Pathogenesis_Deep": "Commonly tested parameters include exact incubation periods, OIE notification obligations, vaccination schedules, and specific percentage thresholds for disease control programs.",
        "Why_Not": "Approximate answers are insufficient; exact values carry full mark weight.",
        "Wow_Approach": "High-yield blanks: Anthrax incubation = 1-3 days; Rabies in dogs = 14-90 days; FMD incubation = 2-14 days; JD clinical signs = 2-5 years post-infection."
    },
    2291: {
        "topic": "VPM MCQ Section - Choose Correct Answer Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This MCQ section tests specific diagnostic, epidemiological, and pharmacological facts in VPM.",
        "Pathogenesis_Deep": "Focus areas: gold-standard diagnostic tests, specific drugs of choice, definitive reservoir hosts, and vector species for major diseases.",
        "Why_Not": "Always identify what makes three options wrong before confirming the fourth is right.",
        "Wow_Approach": "For any MCQ asking 'drug of choice for Mycoplasma': the answer is NEVER Penicillin (no cell wall = no target)."
    },
    2292: {
        "topic": "Schistosoma nasale - Egg Shape",
        "Core_Anatomy": "Nasal mucosa and venous plexuses of cattle.",
        "Pathogenesis_Immediate": "The egg of Schistosoma nasale has the characteristic 'Palanquin' (or Indian litter) shape.",
        "Pathogenesis_Deep": "Schistosoma nasale is a blood trematode (blood fluke) infecting the nasal veins of cattle, buffaloes, and horses, causing 'Snoring Disease' in India. The eggs are uniquely shaped: the central oval egg body has lateral wing-like protrusions on each side, resembling the shape of a palanquin (a box-litter carried on poles). These characteristic eggs are passed through the nasal mucosa and are shed in nasal discharge or swallowed and passed in feces.",
        "Why_Not": "The Napoleon hat shape (bicornuate) is not characteristic of Schistosoma. Oval eggs are typical of many common intestinal nematodes. The Palanquin shape is unique and pathognomonic for S. nasale.",
        "Wow_Approach": "The intermediate host of S. nasale in India is the freshwater snail Indoplanorbis exustus—blocking the snail's habitat (draining stagnant pools, applying molluscicides) is the primary preventive measure."
    },
    2293: {
        "topic": "Schistosoma nasale Egg - MCQ Answer Confirmation",
        "Core_Anatomy": "Nasal venous plexuses.",
        "Pathogenesis_Immediate": "The Palanquin-shaped egg is the definitive answer for S. nasale egg morphology.",
        "Pathogenesis_Deep": "The palanquin shape results from the lateral expansions of the eggshell. When stained with Lugol's iodine and examined under a microscope at 40x, the miracidium inside the egg is visible, confirming the egg is embryonated and infective if ingested by the snail intermediate host.",
        "Why_Not": "Napoleon hat, oval, and elliptical shapes describe eggs of other parasites.",
        "Wow_Approach": "Sodium antimony tartrate (Tartar Emetic) administered intravenously was the classical drug for bovine schistosomiasis; modern therapy uses Praziquantel."
    },
    2294: {
        "topic": "Liver Flukes - Obstructive Jaundice",
        "Core_Anatomy": "Bile ducts and gallbladder.",
        "Pathogenesis_Immediate": "Obstructive (post-hepatic) jaundice is classically seen in liver fluke (Fasciola hepatica/Fasciola gigantica) infestations.",
        "Pathogenesis_Deep": "Adult Fasciola hepatica reside in the bile ducts of the liver. Hundreds of flukes cause severe, chronic, fibrotic cholangitis (bile duct inflammation and thickening), eventually obstructing bile flow. When bile cannot drain normally through the bile ducts into the duodenum, bilirubin accumulates in the bloodstream (hyperbilirubinemia), causing yellowing of mucous membranes, sclera, and serum (obstructive/cholestatic jaundice).",
        "Why_Not": "Hookworms cause hemorrhagic anemia. Schistosomes in the portal veins cause hepatic fibrosis ('pipe-stem fibrosis') but primarily cause portal hypertension rather than pure obstructive jaundice. Strongyles cause colic and larval cyathostominosis.",
        "Wow_Approach": "In cattle heavily infested with F. gigantica, necropsy reveals bile ducts thickened to the diameter of a garden hose, literally packed with large adult flukes. This 'corrugated bile duct' appearance is pathognomonic."
    },
    2295: {
        "topic": "Johne's Disease - Single Intradermal Test",
        "Core_Anatomy": "Cutaneous delayed-type hypersensitivity response.",
        "Pathogenesis_Immediate": "The Single Intradermal Test (using Johnin/avian tuberculin PPD) is used specifically to diagnose Johne's Disease (JD) / Paratuberculosis.",
        "Pathogenesis_Deep": "Mycobacterium avium subsp. paratuberculosis (MAP) is antigenically related to M. avium (avian tuberculosis). The Johnin test injects a purified protein derivative of MAP intradermally. In infected cattle, sensitized T-cells migrate to the injection site and release IFN-γ, causing a measurable skin-fold thickening at 72 hours (positive delayed hypersensitivity reaction).",
        "Why_Not": "IBR (Infectious Bovine Rhinotracheitis) is a herpesvirosis diagnosed by ELISA/VNT. BVD uses ELISA/PCR. Rinderpest (now eradicated) was diagnosed by AGID. The intradermal test is specifically for Mycobacterial diseases (TB and JD).",
        "Wow_Approach": "A critical limitation: MAP cross-reacts with M. avium on the bovine intradermal tuberculin test, causing false-positive TB reactions in herds where JD is endemic. The comparative intradermal test (using both avian and bovine PPD) helps differentiate them."
    },
    2296: {
        "topic": "Zoonotic Abortion Diseases - Leptospirosis and Brucellosis",
        "Core_Anatomy": "Placenta, fetal membranes, and uterus.",
        "Pathogenesis_Immediate": "Both Leptospirosis AND Brucellosis are major abortion-causing zoonotic diseases in cattle.",
        "Pathogenesis_Deep": "Both organisms target the placenta and cause late-term abortions: (1) Brucella abortus contains Erythritol (a sugar) in high concentrations in the bovine placenta, which actively stimulates bacterial growth, causing severe placentitis and abortion. (2) Leptospira interrogans crosses the placenta, causes fetal death and abortion, usually at 6-9 months gestation (mid-to-late term). Both are severely zoonotic, transmissible to veterinarians through contact with infected fetal membranes or uterine fluids.",
        "Why_Not": "These are the two most important zoonotic abortion diseases in cattle. The answer is 'both' (c).",
        "Wow_Approach": "A veterinarian assisting with a suspected abortion from an unknown cause should wear N95 respirator, face shield, AND shoulder-length OB gloves—because both Brucella and Leptospira can penetrate intact mucous membranes and conjunctiva with catastrophic consequences."
    },
    2297: {
        "topic": "Rabies - Cause of Death",
        "Core_Anatomy": "Brainstem (respiratory and cardiac centers).",
        "Pathogenesis_Immediate": "Death in rabies is due to failure of ALL vital centers: cardiac, respiratory, and nervous system failure.",
        "Pathogenesis_Deep": "Rabies virus replicates extensively in the limbic system and brainstem. The virus destroys the neurons of the respiratory center in the medulla oblongata, causing fatal apnea (respiratory arrest). Simultaneously, the cardiovascular control centers are damaged, causing cardiac arrhythmia and circulatory collapse. The neurological devastation causes convulsions, coma, and brain death. Death results from the combined, simultaneous failure of all three vital systems.",
        "Why_Not": "Selecting only 'cardiac' or only 'respiratory' failure is incomplete. Rabies causes the catastrophic failure of all three components of the vital tripod.",
        "Wow_Approach": "In the classic 'furious' (encephalitic) form of rabies in dogs, hypersalivation is not caused by excessive saliva production but by the paralysis of the pharyngeal muscles that prevents swallowing, combined with the intense fear of water (hydrophobia) that prevents voluntary drinking."
    },
    2298: {
        "topic": "VPM True/False Section Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This section evaluates absolute epidemiological statements requiring precise TRUE or FALSE determination.",
        "Pathogenesis_Deep": "Common True/False traps: confusing the reservoir with the dead-end host, mixing up incubation periods, or misidentifying the causal Clostridium type.",
        "Why_Not": "A single incorrect fact makes the entire statement FALSE.",
        "Wow_Approach": "Watch for 'Rinderpest is eradicated' (TRUE - 2011), 'Rabies has no treatment' (TRUE), and 'FMD affects pigs' (TRUE - pigs are highly susceptible amplifiers)."
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
