import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2254: {
        "topic": "Equine Strangles - Streptococcus equi",
        "Core_Anatomy": "Lymph nodes of the head and neck.",
        "Pathogenesis_Immediate": "Equine Distemper (Strangles) is caused by Streptococcus equi subsp. equi.",
        "Pathogenesis_Deep": "S. equi possesses a hyaluronic acid capsule that resists phagocytosis by neutrophils and an M-protein that further inhibits opsonization. This allows the bacteria to survive in the lymph nodes and proliferate massively despite the horse's immune response, leading to the formation of huge, thick-walled abscesses (that can reach the size of a grapefruit) in the submandibular and retropharyngeal lymph nodes.",
        "Why_Not": "Glanders is a completely different OIE-listed disease caused by a Gram-negative bacillus. Salmonellosis causes enteric disease. Only S. equi causes the classic cervical/retropharyngeal abscessation.",
        "Wow_Approach": "The gold standard for Strangles diagnosis is NOT a swab but a Nasopharyngeal Lavage (NP wash) sent for PCR—because S. equi specifically colonizes the Guttural Pouches, and a throat swab may miss it entirely."
    },
    2255: {
        "topic": "Black Quarter (BQ) - Tiger Heart Lesion",
        "Core_Anatomy": "Myocardium (cardiac muscle).",
        "Pathogenesis_Immediate": "The 'Tiger heart' lesion (alternating pale and dark streaks resembling tiger stripes on the myocardium) is the pathognomonic post-mortem finding in Black Quarter (BQ) caused by Clostridium chauvoei.",
        "Pathogenesis_Deep": "Black quarter (Blackleg) is a rapidly fatal disease of cattle caused by C. chauvoei spores that activate in damaged or actively growing muscle (particularly in rapidly growing young cattle aged 6 months to 2 years). As the bacteria multiply anaerobically, they release powerful Alpha, Beta, and Gamma toxins that cause severe myonecrosis, gas production, and hemolysis. In the heart, this toxin-mediated muscle damage creates the alternating bands of pale necrotic muscle and dark hemorrhagic muscle—the Tiger Heart.",
        "Why_Not": "Anthrax causes a swollen, dark red spleen and dark, non-clotted blood at all orifices, but NOT the tiger heart pattern. J.D. (Johne's) causes intestinal changes.",
        "Wow_Approach": "A healthy young bull or heifer found dead in the field with a distinctly gas-crepitant swelling in a major muscle group (thigh/shoulder), and a tiger-striped heart on necropsy, is a classic BQ presentation."
    },
    2256: {
        "topic": "Psittacosis Treatment - Drug of Choice",
        "Core_Anatomy": "Avian respiratory macrophages and epithelium.",
        "Pathogenesis_Immediate": "The drug of choice for treating Psittacosis (Chlamydia psittaci) in birds is Chlortetracycline (Doxycycline is the modern clinical equivalent).",
        "Pathogenesis_Deep": "Chlamydia psittaci is an obligate intracellular pathogen. It lives inside host macrophages and epithelial cells, making cell-wall-targeting antibiotics (Penicillin, Streptomycin, Neomycin) completely ineffective. Tetracyclines (Chlortetracycline, Doxycycline) penetrate host cells and inhibit bacterial 70S ribosome protein synthesis. Treatment requires a prolonged course (45 days minimum) to eliminate the pathogen from the entire population.",
        "Why_Not": "Penicillin has NO activity against Chlamydia because they lack peptidoglycan cell walls. Streptomycin and Neomycin are aminoglycosides with very poor intracellular penetration.",
        "Wow_Approach": "Because treatment requires 45 days of Doxycycline-medicated feed for the entire flock/aviary, the prolonged course often selects for resistance. Always retest the birds post-treatment to confirm clearance."
    },
    2257: {
        "topic": "Bovine Mastitis - Nagase Test",
        "Core_Anatomy": "Mammary gland secretions.",
        "Pathogenesis_Immediate": "The Nagase (Catalase) test is employed in the diagnosis of Mastitis.",
        "Pathogenesis_Deep": "The Nagase test detects elevated catalase enzyme activity in milk. Catalase is present in high concentrations in PMNs (neutrophils), which invade the mammary gland in large numbers during bacterial mastitis. When hydrogen peroxide (H2O2) is added to mastitic milk, the catalase from the dead and living neutrophils rapidly breaks down the H2O2 into water and oxygen gas, producing vigorous bubbling. The California Mastitis Test (CMT) uses DNA-release from somatic cells as its detection mechanism and is more widely used today.",
        "Why_Not": "The Nagase test is specifically for mastitis (elevated somatic cells). BQ and Campylobacteriosis are not diagnosed by the Nagase/Catalase test.",
        "Wow_Approach": "The Nagase test is an indirect measure of somatic cell count (SCC); the more intense the bubbling, the higher the SCC, indicating more severe inflammatory reaction in the gland."
    },
    2258: {
        "topic": "Anthrax Diagnosis - Ascoli Test",
        "Core_Anatomy": "Anthrax polysaccharide antigens.",
        "Pathogenesis_Immediate": "The Ascoli Thermoprecipitin Test is used to diagnose Anthrax, specifically from post-mortem materials, hides, or processed animal products.",
        "Pathogenesis_Deep": "The Ascoli test is a thermoprecipitin (ring precipitation) test. Suspected tissue, hide, or bone is extracted by boiling to release Bacillus anthracis somatic polysaccharide antigens. This extract is carefully layered onto specific Anthrax precipitin antiserum in a narrow tube. If anthrax antigens are present, a distinct white precipitin ring forms at the interface between the two layers within minutes. It is particularly useful for testing already decomposed carcasses or tanned leather where bacterial culture is impossible.",
        "Why_Not": "Leptospirosis uses MAT. Glanders uses Mallein/CFT. Tetanus is diagnosed clinically. Only Anthrax uses the Ascoli thermoprecipitin test.",
        "Wow_Approach": "The Ascoli test can positively detect anthrax antigens from 100-year-old preserved museum specimens, hides, and even properly tanned leather—making it an invaluable forensic tool for tracing the source of imported animal product outbreaks."
    },
    2259: {
        "topic": "Dermatophytosis - Wood's Lamp Diagnosis",
        "Core_Anatomy": "Hair shaft and keratin (fluorescent metabolites).",
        "Pathogenesis_Immediate": "A Wood's Lamp (ultraviolet light at 365 nm) is useful in the preliminary diagnosis of Dermatophytosis (Ringworm).",
        "Pathogenesis_Deep": "Certain dermatophyte species (most notably Microsporum canis and M. audouinii) produce a fluorescent metabolite (tryptophan metabolites in infected hair shafts) that emits a characteristic apple-green or blue-green fluorescence when illuminated with a Wood's Lamp in a darkened room. This is a rapid, non-invasive, chair-side screening tool.",
        "Why_Not": "Footrot is diagnosed by culture of Dichelobacter nodosus. Coccidioidomycosis and Histoplasmosis are diagnosed by culture or serology. Only Dermatophytes (specifically Microsporum spp.) fluoresce under Wood's Lamp.",
        "Wow_Approach": "Only approximately 50% of Microsporum canis infections fluoresce, and Trichophyton species (the other major ringworm genus) do NOT fluoresce at all. A negative Wood's Lamp test CANNOT rule out ringworm—a positive is helpful, a negative is meaningless."
    },
    2260: {
        "topic": "Anthrax - McFadyean's Staining",
        "Core_Anatomy": "Bacillus anthracis polychrome capsule.",
        "Pathogenesis_Immediate": "Bacillus anthracis is specifically stained and detected using Polychrome Methylene Blue (McFadyean's reaction) for rapid presumptive diagnosis.",
        "Pathogenesis_Deep": "In the McFadyean's test, a blood smear from a suspected anthrax carcass is heat-fixed and stained with Polychrome Methylene Blue. Under the microscope, the large, square-ended, blue-stained bacilli (vegetative B. anthracis) are surrounded by a distinctive pink/reddish-purple capsule (poly-D-glutamic acid). This 'pink halo' around the blue bacilli is the positive McFadyean reaction—a pathognomonic finding confirming anthrax.",
        "Why_Not": "Gram's staining will show the large Gram-positive rods but cannot demonstrate the capsule. Spore staining (Schaeffer-Fulton) detects the spore but misses the key diagnostic capsule.",
        "Wow_Approach": "Never open a carcass suspected of dying from anthrax before performing a peripheral blood smear. Opening the body exposes the vegetative bacilli to oxygen, causing rapid sporulation and permanent environmental contamination."
    },
    2261: {
        "topic": "Anthrax - Peracute Form Duration",
        "Core_Anatomy": "Systemic vasculature and reticuloendothelial system.",
        "Pathogenesis_Immediate": "The peracute form of Anthrax in cattle has an extremely rapid clinical course of 1-2 hours from onset of signs to death.",
        "Pathogenesis_Deep": "The peracute form of anthrax is the classic 'sudden death' presentation. The bacilli produce a binary toxin (Protective Antigen + Lethal Factor/Edema Factor) that simultaneously causes massive capillary leakage (edema factor) and irreversible apoptosis of macrophages (lethal factor). This rapidly progresses to a complete toxemic circulatory collapse. The animal may be found dead with no observed premonitory signs, or may demonstrate sudden staggering, collapse, convulsions, and death within 1-2 hours.",
        "Why_Not": "The acute form lasts 12-36 hours with visible trembling and dyspnea. The peracute form's 1-2 hour course means observation of clinical signs is rarely possible.",
        "Wow_Approach": "The classic triad at autopsy: (1) dark, tarry, non-clotted blood from all body orifices, (2) massively enlarged, dark red, 'blackberry-jam' spleen, and (3) subcutaneous gelatinous edema confirm the diagnosis before lab results are available."
    },
    2262: {
        "topic": "Bovine Actinobacillosis - Wooden Tongue (MCQ Repeated)",
        "Core_Anatomy": "Lingual soft tissue.",
        "Pathogenesis_Immediate": "A nodule formed in the tongue causing immobility is caused by Actinobacillosis (Actinobacillus lignieresii).",
        "Pathogenesis_Deep": "A. lignieresii (Gram-negative) invades the tongue musculature through mucosal abrasions caused by coarse feed. The result is severe pyogranulomatous inflammation with encapsulation of bacterial colonies ('sulfur granules') in dense fibrous tissue. The entire tongue progressively hardens and becomes immobile—the classic 'Wooden Tongue'—preventing the animal from prehending feed, leading to starvation.",
        "Why_Not": "Actinomycosis (A. bovis) causes BONE involvement (Lumpy Jaw). Listeriosis causes BRAINSTEM involvement. Leptospirosis causes nephritis/abortion—not tongue nodules.",
        "Wow_Approach": "Remember: Actino**bacillus** attacks soft tissue (Back = soft tissue of body), while Actino**myces** attacks hard tissue (Myces = like a rock, attacks Bone)."
    },
    2263: {
        "topic": "Bovine Actinomycosis - Lumpy Jaw (Osteomyelitis)",
        "Core_Anatomy": "Mandibular and maxillary bone.",
        "Pathogenesis_Immediate": "The classic 'Lumpy Jaw' or 'Fistulous Wither' in cattle is caused by Actinomyces bovis.",
        "Pathogenesis_Deep": "Actinomyces bovis (Gram-positive, anaerobic filamentous bacterium) invades the alveolar bone of the jaw through tooth sockets or gingival wounds caused by erupting teeth or coarse feed. It causes a severe, chronic, proliferative osteomyelitis with intermittent draining sinuses. The characteristic finding is 'Madura-type' granules (sulfur granules—yellow/orange hard granules visible in the pus) containing dense clubs of bacterial filaments.",
        "Why_Not": "Actinobacillus lignieresii causes Wooden Tongue (soft tissue). Ulcerative lymphangitis is caused by Corynebacterium pseudotuberculosis. Glanders affects the respiratory tract and skin.",
        "Wow_Approach": "While both Actinomycosis and Actinobacillosis produce 'sulfur granules,' the granules of Actinomyces are 'hard' (calcified, like gritty sand) whereas those of Actinobacillus are 'soft' (mucoid). This tactile distinction can be felt when the pus is rubbed between gloved fingers."
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
