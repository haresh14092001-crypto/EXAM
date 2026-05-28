import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2379: {
        "topic": "Rabies Diagnosis - Laboratory Animal of Choice",
        "Core_Anatomy": "Central nervous system (hippocampus, cerebellum, Ammon's horn).",
        "Pathogenesis_Immediate": "The laboratory animal most commonly and classically used for the diagnosis of rabies via intracerebral inoculation is the Mice (Mouse).",
        "Pathogenesis_Deep": "In the classical mouse inoculation test, a 20% brain suspension from a suspected rabid animal is injected intracerebrally into a group of suckling or adult mice. If rabies virus is present, the mice develop characteristic progressive ascending paralysis (beginning with hindlimb paralysis) and die within 7-21 days. The harvested mouse brains are then examined by Sellers' staining for Negri bodies (eosinophilic intracytoplasmic inclusions in the Purkinje cells and hippocampal neurons).",
        "Why_Not": "Guinea pigs and rabbits were used historically but mice are the standard due to their exquisite susceptibility, small size, low cost, and rapid response. Chickens are used in biological standardization tests, not rabies diagnosis.",
        "Wow_Approach": "The gold standard modern diagnostic has replaced mouse inoculation entirely: the Direct Fluorescent Antibody Test (DFAT) on fresh brain impressions gives results in 2-3 hours vs 7-21 days for mouse inoculation."
    },
    2380: {
        "topic": "ICH / Canine Adenovirus - Brush Border Smear Test",
        "Core_Anatomy": "Transitional epithelium of the urinary bladder.",
        "Pathogenesis_Immediate": "The brush border smear of bladder transitional epithelium is a reliable test for the diagnosis of Infectious Canine Hepatitis (ICH) caused by Canine Adenovirus Type 1.",
        "Pathogenesis_Deep": "Canine Adenovirus Type 1 (CAV-1) infects hepatocytes, but it also has a distinct tropism for the transitional epithelium of the urinary bladder. In acute ICH, CAV-1 replicates within the bladder epithelial cells, producing characteristic basophilic intranuclear inclusion bodies (Cowdry Type A inclusions). By performing a gentle brush-border scraping of the bladder mucosa at necropsy and staining with Hematoxylin and Eosin (H&E), these pathognomonic inclusions can be readily identified.",
        "Why_Not": "BVD, Parvo, and FMD do not produce intranuclear inclusions in bladder epithelium.",
        "Wow_Approach": "One of the most dramatic clinical signs of acute ICH is the 'Blue Eye' phenomenon: CAV-1 infects and damages the corneal endothelium, causing unilateral or bilateral corneal edema (blue-grey opacity). This also occurs as a vaccine reaction with some older live-modified CAV-1 vaccines—which is why modern vaccines use CAV-2 instead."
    },
    2381: {
        "topic": "Rabies Diagnosis - RT-PCR",
        "Core_Anatomy": "Viral RNA (Nucleocapsid gene).",
        "Pathogenesis_Immediate": "The modern gold-standard molecular diagnostic test for rabies virus detection is RT-PCR (Reverse Transcriptase PCR).",
        "Pathogenesis_Deep": "Rabies virus is a negative-sense, single-stranded RNA virus. RT-PCR first converts the viral RNA into complementary DNA (cDNA) using reverse transcriptase enzyme, then amplifies specific regions of the nucleocapsid (N) gene using PCR. Real-time RT-PCR can detect as few as 10 viral genome copies and provides results within 4-6 hours. It can detect even degraded samples (partially decomposed brain) where fluorescent antibody tests fail.",
        "Why_Not": "VNT (Virus Neutralization Test) is used to measure vaccine-induced antibody titers (post-vaccination serology), not for diagnosing active infection. ELISA detects antibodies (past exposure/vaccination), not active viral antigen. PCR is for direct virus detection.",
        "Wow_Approach": "For rabies diagnosis in humans after a suspected animal bite, saliva, skin biopsies from the nuchal (nape of neck) region, and cerebrospinal fluid can be tested by RT-PCR while the patient is still alive—the only ante-mortem diagnostic option."
    },
    2382: {
        "topic": "African Horse Sickness - Zebra Reservoir",
        "Core_Anatomy": "Vascular endothelium (orbivirus tropism).",
        "Pathogenesis_Immediate": "The primary reservoir of African Horse Sickness (AHS) virus is the Zebra.",
        "Pathogenesis_Deep": "Zebras (Equus burchelli) are the natural reservoir and maintenance host of AHS Orbivirus. Because Zebras have co-evolved with the virus for millennia, they develop only the mild 'Horse Sickness Fever' form (a brief febrile illness with no mortality), while developing high-titer viremias that infect feeding Culicoides midges. These infected midges then transmit the virus to naive, susceptible horses (which have not co-evolved with the virus), causing the devastating pulmonary or cardiac forms with up to 95% mortality.",
        "Why_Not": "Mules have partial hybrid resistance. Deer are incidental hosts. Cattle do not develop AHS.",
        "Wow_Approach": "The control of AHS is primarily through Culicoides midge control (housing horses indoors at dawn/dusk when midges are active, using pyrethroid insecticide-impregnated rugs), and trivalent or polyvalent live attenuated AHS vaccines in endemic areas."
    },
    2383: {
        "topic": "Oxyuris equi - Egg Masses on Perianal Region",
        "Core_Anatomy": "Perianal skin and rectum.",
        "Pathogenesis_Immediate": "The presence of grayish-yellow egg masses on the perianal region indicates infestation with Oxyuris equi (Pinworm).",
        "Pathogenesis_Deep": "Oxyuris equi is the equine pinworm. The adult female worm migrates out of the large intestine at night and deposits clusters of sticky, yellow-grey eggs in the perianal skin folds using a cement-like substance. These eggs desiccate, forming the visible grayish-yellow egg masses. The intense perianal irritation causes the horse to rub its tail obsessively against fences and walls (tail rubbing), resulting in the classic 'rat tail' appearance.",
        "Why_Not": "Trichuris (whipworm) eggs are barrel-shaped with polar plugs and are deposited in feces, not perianally. Trichinella is a muscle parasite. Metastrongylus is a lungworm of pigs.",
        "Wow_Approach": "The Oxyuris egg does NOT float in standard saturated saline flotation (the egg is too dense and sticky). To detect Oxyuris eggs, use the Scotch tape test: press transparent adhesive tape against the perianal skin in the morning before the horse defecates, then examine the tape under a microscope for the characteristic D-shaped eggs."
    },
    2384: {
        "topic": "Trichinella - Trichinoscopy",
        "Core_Anatomy": "Skeletal muscle fibers (nurse cells).",
        "Pathogenesis_Immediate": "The Trichinoscope is used specifically to diagnose Trichinella spiralis infestation in skeletal muscle.",
        "Pathogenesis_Deep": "Trichinella spiralis is a zoonotic nematode. After ingestion of Trichinella-containing muscle (undercooked pork), L1 larvae excyst, mature to adults in the small intestine, and female worms deposit newborn larvae directly into the intestinal wall. These larvae travel via lymphatics and blood to skeletal muscles (especially the diaphragm, tongue, and extraocular muscles), where they coil inside 'nurse cells'—modified muscle fibers that provide a vascular supply to the larva. The Trichinoscope is a low-power microscope for examining compressed muscle sections (squash preparations) to identify these coiled Trichinella cysts.",
        "Why_Not": "Oxyuris is detected by the scotch tape test. Trichuris eggs are found in fecal flotation. Metastrongylus larvae are found in Baermann funnel tests on feces.",
        "Wow_Approach": "Trichinoscopy of pig diaphragm is mandatory meat inspection procedure in many countries for pigs intended for human consumption—a single positive muscle compression confirming a coiled larva condemns the entire carcass."
    },
    2385: {
        "topic": "VPM Match the Following Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine - Viral and Parasitic diseases.",
        "Pathogenesis_Immediate": "This section matches specific disease terms with their associated features, breeds, or diagnostic entities.",
        "Pathogenesis_Deep": "Key pairings to master in VPM II: Blue Eye = Canine Adenovirus (ICH); N'Dama = Trypanotolerant breed; specific disease-vaccine associations.",
        "Why_Not": "Use the process of elimination—anchor on the most certain pair first to narrow remaining options.",
        "Wow_Approach": "The N'Dama breed's trypanotolerance is a genetic trait; crossbreeding with Zebu destroys this resistance, an important livestock development consideration in tsetse-fly endemic African regions."
    },
    2386: {
        "topic": "Blue Eye - Canine Adenovirus 1 (ICH)",
        "Core_Anatomy": "Corneal endothelium (anterior uvea).",
        "Pathogenesis_Immediate": "'Blue Eye' (anterior uveitis with corneal edema) is the classic ocular manifestation of Infectious Canine Hepatitis (ICH), matched to the N'dama breed association in the original text's context of trypanotolerance.",
        "Pathogenesis_Deep": "Blue Eye in ICH: CAV-1 deposits immune complexes in the anterior uvea and corneal endothelium during the immune recovery phase (not the acute disease phase). The complement activation and inflammatory response damages corneal endothelial pump cells, causing acute aqueous humor accumulation in the stroma, producing the dramatic, unilateral blue-grey corneal opacity. This typically resolves spontaneously within 2-3 weeks but can occasionally cause permanent corneal scarring.",
        "Why_Not": "Blue Eye occurs during RECOVERY from ICH (immune complex deposition), not during the acute liver disease phase—an important distinction if asked about timing.",
        "Wow_Approach": "Modern CAV-2 vaccines do NOT cause Blue Eye (because CAV-2 does not have the corneal endothelium tropism of CAV-1), which is why all modern Adenovirus vaccines use the CAV-2 strain even though they cross-protect against CAV-1 ICH."
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
enriched = [x for x in d2 if x.get('is_high_yield') and x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(d2)} total entries.")
print(f"  Enriched HY questions: {len(enriched)}")
print(f"  Empty HY remaining:    {len(empty2)}")
