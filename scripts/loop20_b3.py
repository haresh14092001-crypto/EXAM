import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2344: {
        "topic": "Stormont Test - Tuberculosis Screening",
        "Core_Anatomy": "Cutaneous delayed-type hypersensitivity.",
        "Pathogenesis_Immediate": "The Stormont test is used to screen for Tuberculosis in cattle.",
        "Pathogenesis_Deep": "The Stormont test is a two-injection tuberculin skin test used to detect sensitized (exposed) cattle with greater specificity than the single intradermal test. Bovine PPD is injected intradermally twice: first on Day 0, and a second injection at the same site 7 days later. In a tuberculosis-sensitized animal, the booster injection triggers a much more exaggerated, easily measurable delayed hypersensitivity swelling (an 'amnestic' response) at the injection site compared to a non-sensitized animal. This amplification improves detection sensitivity.",
        "Why_Not": "The Stormont test is strictly for TB. RBPT/BBAT is for Brucellosis. Ascoli test is for Anthrax. Mallein is for Glanders.",
        "Wow_Approach": "The Stormont test is particularly valuable for detecting 'anergic' TB reactors—cattle with such a heavy bacterial burden that their immune system has become exhausted and can no longer react to a single-dose tuberculin test, but CAN still respond to the booster stimulus."
    },
    2345: {
        "topic": "Terbinafine - Antifungal Drug",
        "Core_Anatomy": "Fungal cell membrane (Ergosterol synthesis pathway).",
        "Pathogenesis_Immediate": "Terbinafine is an Antifungal drug.",
        "Pathogenesis_Deep": "Terbinafine is an allylamine antifungal agent that works by specifically inhibiting squalene epoxidase, an enzyme in the ergosterol biosynthesis pathway of fungi. This leads to squalene accumulation (which is toxic to the fungal cell) and depletion of ergosterol (the essential component of fungal cell membranes). The drug is highly effective against dermatophytes (Trichophyton, Microsporum) and is used topically and systemically for ringworm treatment in small animals.",
        "Why_Not": "Terbinafine is not antiparasitic (like Ivermectin), antiviral (like Acyclovir), or antibacterial (like Amoxicillin). Its mechanism—blocking ergosterol synthesis—is completely fungal-specific.",
        "Wow_Approach": "Unlike Griseofulvin (which is fungistatic—stopping fungal growth), Terbinafine is fungicidal—it actually kills the fungal cells. This means shorter treatment courses are needed, improving owner compliance in pets with ringworm."
    },
    2346: {
        "topic": "Dermatophytosis - Sample Collection Site",
        "Core_Anatomy": "Skin keratinocytes at the lesion periphery.",
        "Pathogenesis_Immediate": "In dermatophytosis, the sample for diagnostic culture must be taken from the EDGE (periphery) of the lesion with deep scraping.",
        "Pathogenesis_Deep": "Dermatophytes (like Trichophyton or Microsporum) are active and proliferating at the ADVANCING EDGE of the circular skin lesion, not at the center. The center of a ringworm lesion is composed of old, dead, healing tissue where the fungus has already exhausted its nutrients and is dying. Collecting from the center yields false-negative cultures. Samples from the edge include active hyphae and arthrospores that will grow successfully in Sabouraud Dextrose Agar culture.",
        "Why_Not": "Collecting from the center of the lesion will almost always give a false-negative culture result, leading to misdiagnosis.",
        "Wow_Approach": "Before sampling, gently clean the lesion edge with 70% alcohol to remove surface environmental contaminants, then allow to dry before scraping—this dramatically improves culture yield by eliminating fast-growing environmental mold contaminants."
    },
    2347: {
        "topic": "Brucellosis Abortion - Timing in Cattle",
        "Core_Anatomy": "Placentome and cotyledons.",
        "Pathogenesis_Immediate": "Brucella abortus causes abortion most commonly at 6-9 months of gestation in cattle.",
        "Pathogenesis_Deep": "Brucella abortus is attracted to erythritol (a sugar alcohol found in highest concentrations in the bovine chorioallantois after 5 months of gestation). Before 5 months, erythritol levels are too low to support massive bacterial replication in the placenta. After 5 months, erythritol surges, the bacteria colonize the chorioallantois explosively, causing severe, necrotizing placentitis. The fetus dies from bacterial colonization and the toxins released, and abortion occurs most frequently at 6-9 months.",
        "Why_Not": "Early abortions (1-3 months) are more typical of Trichomoniasis or early-stage Leptospirosis. Late-term abortion at 6-9 months is the characteristic fingerprint of Brucellosis.",
        "Wow_Approach": "After aborting, the cow sheds massive quantities of Brucella abortus from the uterine discharge and the placenta for several weeks—the entire area must be cordoned off, and all placental material must be incinerated or buried in quicklime."
    },
    2348: {
        "topic": "Snuffles - Pasteurella multocida in Rabbits",
        "Core_Anatomy": "Nasal mucosa and upper respiratory tract.",
        "Pathogenesis_Immediate": "Snuffles is associated with Rabbits.",
        "Pathogenesis_Deep": "Snuffles is the common name for chronic upper respiratory tract infection in rabbits caused primarily by Pasteurella multocida. The rabbit presents with persistent mucopurulent nasal discharge, sneezing, and rustling respiratory sounds (the 'snuffles'). The infection spreads from the nasal cavity to the Eustachian tube (causing otitis media and head tilt) and occasionally to the conjunctiva (causing dacryocystitis). Transmission is by direct contact between rabbits.",
        "Why_Not": "Sheep, mice, and guinea pigs do not specifically suffer from this condition—Snuffles is the classic upper respiratory disease syndrome uniquely associated with rabbits.",
        "Wow_Approach": "Because Pasteurella multocida can become a latent carrier state in rabbits, a rabbit may appear clinically healthy but shed the organism continuously, infecting all naive rabbits it contacts—making introduction of new rabbits into a colony extremely high risk without quarantine testing."
    },
    2349: {
        "topic": "Anaplasmosis - Gall Sickness",
        "Core_Anatomy": "Erythrocytes (reticuloendothelial system).",
        "Pathogenesis_Immediate": "The tick-borne disease known as 'Gall Sickness' is another name for Anaplasmosis.",
        "Pathogenesis_Deep": "Anaplasmosis is caused by Anaplasma marginale, an obligate intracellular rickettsial organism that parasitizes bovine erythrocytes. Transmitted by Rhipicephalus (Boophilus) ticks, the organism forms inclusion bodies within RBCs (visible as purple 'marginal bodies' under Giemsa staining at the periphery of the RBC). The progressive destruction of infected RBCs causes severe hemolytic anemia, icterus, and fever. The term 'Gall Sickness' comes from the intense jaundice ('gall' = bile) characteristic of the disease.",
        "Why_Not": "Ehrlichiosis is a different rickettsial disease affecting white blood cells (neutrophils and monocytes). Q Fever is caused by Coxiella burnetii (a different rickettsial). Listeriosis causes CNS disease.",
        "Wow_Approach": "Unlike Babesiosis (where hemolysis causes hemoglobinuria/red urine), Anaplasmosis causes icterus WITHOUT hemoglobinuria—a key clinical distinguishing feature."
    },
    2350: {
        "topic": "Johne's Disease - Rectal Pinch Test",
        "Core_Anatomy": "Rectal mucosa and mesenteric lymph nodes.",
        "Pathogenesis_Immediate": "The Rectal Pinch test (or 'Rectal Mucosal Scraping' technique) is used as a diagnostic tool for Paratuberculosis (Johne's Disease / JD).",
        "Pathogenesis_Deep": "In cattle with advanced Johne's Disease, massive numbers of MAP organisms accumulate in the macrophages of the rectal submucosa. In the Rectal Pinch test, a small fold of the rectal mucosal wall is gently pinched between the fingers during rectal examination. The mucosa is scraped, and the cellular material is smeared onto a glass slide, fixed, and stained with Ziehl-Neelsen stain. Clusters of acid-fast red bacilli within macrophages confirm the MAP diagnosis.",
        "Why_Not": "Brucellosis is diagnosed by RBPT/STAT (serology). Listeriosis is diagnosed by CSF/brain culture. Tuberculosis uses the intradermal tuberculin test.",
        "Wow_Approach": "The Rectal Pinch test is only positive in ADVANCED, clinical JD cases (when the animal is already symptomatic and shedding massive MAP). It misses the huge population of subclinical MAP shedders—making ELISA and fecal PCR essential for herd-level surveillance."
    },
    2351: {
        "topic": "Carrion-Associated Botulism - Phosphorus Deficiency",
        "Core_Anatomy": "Bone pica behavior and gastrointestinal tract.",
        "Pathogenesis_Immediate": "Outbreaks of carrion-associated botulism in cattle are most strongly associated with a deficiency of Phosphorus.",
        "Pathogenesis_Deep": "Phosphorus deficiency (Aphosphorosis) is extremely common in extensive cattle grazing on phosphorus-deficient pastures (common in parts of Africa and South America). To satisfy their mineral craving (pica), phosphorus-deficient cattle chew and ingest bones and carcasses of dead animals. If those carcasses contain Clostridium botulinum toxin (from putrefying anaerobic protein), the cattle ingest pre-formed botulinum toxin (Toxico-infectious Botulism), leading to epidemic 'Lame Sickness' (Lamziekte) with flaccid paralysis.",
        "Why_Not": "Protein or calcium deficiency can also cause pica but are not classically linked to epidemic carrion-associated botulism outbreaks in cattle.",
        "Wow_Approach": "Preventing epidemic botulism in phosphorus-deficient areas is simple and cost-effective: supplement the mineral licks with Monocalcium phosphate (MCP). This resolves the pica behavior and eliminates the drive to scavenge carcasses."
    },
    2352: {
        "topic": "Enterotoxemia (ET) - Predisposing Factors",
        "Core_Anatomy": "Small intestinal starch load and Clostridium perfringens Type D.",
        "Pathogenesis_Immediate": "Predisposing factors for Enterotoxemia (ET) include grazing on rapidly growing lush pastures, heavy grain feeding, and sudden changes in diet—all of the above.",
        "Pathogenesis_Deep": "All these factors share a common mechanism: they rapidly increase the amount of fermentable carbohydrate (starch, simple sugars) reaching the small intestine. This starch overload explosively stimulates C. perfringens Type D proliferation and Epsilon toxin production. (1) Lush spring pastures have high non-structural carbohydrate content. (2) Grain feeding directly provides starch. (3) Sudden diet changes disrupt rumen microbiome balance, causing carbohydrate bypass to the intestine.",
        "Why_Not": "Low-quality roughage (hay) does not trigger the starch overload necessary for Type D proliferation.",
        "Wow_Approach": "When transitioning cattle or sheep onto grain-based diets, ALWAYS increase grain incrementally over 2-3 weeks (5-10% per day) to allow the rumen microbiome to adapt—sudden full ration introduction is the primary trigger for ET fatalities."
    },
    2353: {
        "topic": "Pulpy Kidney Disease - Rapid Renal Autolysis",
        "Core_Anatomy": "Renal parenchyma.",
        "Pathogenesis_Immediate": "Rapid autolysis (softening) of the kidney is the salient post-mortem finding of Enterotoxemia (ET) / Pulpy Kidney Disease.",
        "Pathogenesis_Deep": "C. perfringens Type D Epsilon toxin causes massive endothelial damage throughout the body, including the renal vasculature. The combination of vascular damage, renal ischemia, and a highly elevated blood glucose level (from toxin-induced gluconeogenesis) triggers a unique vulnerability of the renal tubular epithelium to extremely rapid post-mortem autolysis. Within just 30-60 minutes of death, the kidney softens dramatically, becoming a mushy, 'pulpy' consistency—the origin of the 'Pulpy Kidney' name.",
        "Why_Not": "HS (Hemorrhagic Septicemia) causes severe edema, congestion, and subcutaneous hemorrhage—NOT rapid renal autolysis. Anthrax causes dark, non-clotted blood and splenomegaly. BQ (Black Quarter) causes gas-crepitant muscle necrosis.",
        "Wow_Approach": "Because the kidneys autolyze so rapidly in Pulpy Kidney Disease, if the veterinarian does not reach the carcass within 1 hour of death, the kidneys are already too soft to section properly, making gross necropsy diagnosis difficult—hence the importance of collecting fresh kidney for histology or brain for toxin assay."
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
