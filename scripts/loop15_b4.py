import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1703: {
        "topic": "Working Dogs - Search and Rescue",
        "Core_Anatomy": "Olfactory epithelium and olfactory bulb.",
        "Pathogenesis_Immediate": "The statement 'During disaster sniffer dogs are used for human rescue' is TRUE.",
        "Pathogenesis_Deep": "Dogs possess an olfactory epithelium that is roughly 40-50 times larger than humans, containing up to 300 million olfactory receptors. A significant portion of their brain is dedicated to analyzing odors. In disaster management (earthquakes, avalanches), sniffer dogs detect the specific volatile organic compounds (VOCs) released by human sweat, breath, and decomposition, allowing them to locate victims buried under meters of rubble where visual or auditory detection is impossible.",
        "Why_Not": "While electronic sensors exist, they lack the rapid mobility and complex discriminatory processing of a trained canine.",
        "Wow_Approach": "Search and Rescue (SAR) dogs are specifically trained to differentiate between the scent of a living human (Air Scenting/Tracking) and a deceased human (Cadaver dogs)."
    },
    1705: {
        "topic": "Anthrax - Sterne Spore Vaccine",
        "Core_Anatomy": "Cutaneous, GI, and respiratory immune systems.",
        "Pathogenesis_Immediate": "Anthrax prophylaxis is universally matched with the Sterne Spore Vaccine.",
        "Pathogenesis_Deep": "The Sterne strain (developed by Max Sterne in 1937) is an avirulent, live spore vaccine. Bacillus anthracis relies on two plasmids for full virulence: pXO1 (toxins) and pXO2 (poly-D-glutamic acid capsule). The Sterne strain has lost the pXO2 plasmid. Because it cannot form a capsule, the bacteria are quickly phagocytosed by the host's immune system, which then safely develops robust antibodies against the lethal toxins (pXO1) without the animal developing the fatal disease.",
        "Why_Not": "Cotton strain 19 is used for Brucella abortus. Schizont vaccine is for Theileria annulata.",
        "Wow_Approach": "Because it is a live spore vaccine, it must never be administered simultaneously with systemic antibiotics (like Penicillin), as the antibiotic will kill the vaccine strain before the animal can mount an immune response."
    },
    1706: {
        "topic": "Escherichia coli - Neonatal Scours",
        "Core_Anatomy": "Intestinal mucosa (enterocytes).",
        "Pathogenesis_Immediate": "Enterotoxigenic E. coli (ETEC) is the primary cause of fatal neonatal calf scours in the first week of life.",
        "Pathogenesis_Deep": "ETEC strains possess specific fimbriae (pili), most notably the K99 (F5) antigen, which allows the bacteria to firmly attach to the villi of the newborn calf's small intestine. Once attached, the bacteria secrete massive amounts of heat-stable enterotoxin (STa). This toxin stimulates cGMP production in the enterocytes, forcing the cells to aggressively pump chloride and water INTO the gut lumen, causing a catastrophic, watery, non-hemorrhagic secretory diarrhea and rapid death from hypovolemic shock.",
        "Why_Not": "Vaccinating the calf after birth is useless because ETEC strikes within hours of birth. The only effective prevention is vaccinating the DAM (cow) with a K99 bacterin late in pregnancy to ensure high IgA/IgG levels in the colostrum.",
        "Wow_Approach": "If a calf is over 7 days old, it naturally loses the specific intestinal receptors for the K99 fimbriae, meaning ETEC is almost never the cause of scours in older calves (suspect Rotavirus, Coronavirus, or Coccidia instead)."
    },
    1707: {
        "topic": "Theileriosis - Schizont Cell Culture Vaccine",
        "Core_Anatomy": "Lymphocytes and erythrocytes.",
        "Pathogenesis_Immediate": "Bovine Theileriosis (Tropical Theileriosis) is matched with the live attenuated Schizont vaccine (e.g., Raksha Vac-T).",
        "Pathogenesis_Deep": "Theileria annulata (transmitted by Hyalomma ticks) first infects the cow's lymphocytes, transforming them into rapidly dividing, immortalized cells containing the protozoan 'schizonts'. The vaccine is created by isolating these infected lymphocytes and passaging them continuously in cell culture (up to 100 times). This prolonged in-vitro culture causes the schizonts to lose their virulence while retaining their antigenicity. When injected into a healthy calf, it confers solid cell-mediated immunity.",
        "Why_Not": "Anthrax uses a bacterial spore vaccine. Brucellosis uses a modified live bacterial strain (S19). Theileria requires a specialized eukaryotic cell-culture vaccine.",
        "Wow_Approach": "Because this is a live, transformed lymphocyte vaccine, it must be stored and transported strictly in liquid nitrogen (-196°C) to maintain cell viability until the moment of administration."
    },
    1720: {
        "topic": "Exam Instructions Header",
        "Core_Anatomy": "N/A - Examination Rules.",
        "Pathogenesis_Immediate": "Standard examination protocol header denoting the time limit for the objective section.",
        "Pathogenesis_Deep": "Objective questions require rapid cognitive recall; strict time limits prevent students from utilizing extensive deductive reasoning, forcing them to rely on ingrained rote knowledge.",
        "Why_Not": "Subjective sections allow for prolonged synthesis of information.",
        "Wow_Approach": "In objective exams, always answer the questions you know instantly first, then circle back to the challenging ones to maximize point yield."
    },
    1721: {
        "topic": "VMD Objective Section - Fill in the Blanks Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of clinical terms.",
        "Pathogenesis_Deep": "Unlike MCQs, there are no distractors to eliminate. This format tests whether the clinical sign has been perfectly linked in memory to its specific pathophysiological etiology.",
        "Why_Not": "Vague answers will not receive credit when specific terminology is required.",
        "Wow_Approach": "Group your study notes by 'Pathognomonic gait/posture/test' to ace this section."
    },
    1738: {
        "topic": "VMD Objective Section - Multiple Choice Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces standard MCQs, requiring the clinician to eliminate distractor etiologies.",
        "Pathogenesis_Deep": "MCQs in veterinary medicine often pair a disease with its most confusing differential. Success depends on identifying the single 'rule-out' clinical sign.",
        "Why_Not": "Do not select an answer simply because it causes similar signs; it must cause the EXACT signs described.",
        "Wow_Approach": "Read all four options before selecting an answer; the 'best' answer is required, not just the first plausible one."
    },
    1739: {
        "topic": "Bovine Tuberculosis Diagnostics (Repeated)",
        "Core_Anatomy": "Cutaneous immune system (T-cell hypersensitivity).",
        "Pathogenesis_Immediate": "The Stormont test is used to specifically screen for and confirm Bovine Tuberculosis.",
        "Pathogenesis_Deep": "The Stormont test increases the specificity of standard tuberculin testing. By giving a primary intradermal injection of Bovine PPD and a second injection at the same site 7 days later, it amplifies the local memory T-cell response in a truly infected animal. This helps differentiate animals infected with true Mycobacterium bovis from those simply exposed to harmless environmental mycobacteria (which cause false positives on the single intradermal test).",
        "Why_Not": "Brucellosis is screened via serology (Rose Bengal, STAT). Glanders is screened via the Mallein test. Anthrax is diagnosed via blood smears, not skin tests.",
        "Wow_Approach": "An increase in skin fold thickness of 5 mm or more, 24 hours after the second injection, classifies the animal as a positive reactor."
    },
    1740: {
        "topic": "Veterinary Pharmacology - Terbinafine",
        "Core_Anatomy": "Epidermis, hair follicles, and nails.",
        "Pathogenesis_Immediate": "Terbinafine is utilized as the drug of choice for severe Antifungal therapy (specifically for dermatophytosis/ringworm).",
        "Pathogenesis_Deep": "Terbinafine is an allylamine antifungal. It works by inhibiting the enzyme squalene epoxidase, which is critical for the synthesis of ergosterol (the main component of the fungal cell membrane). This inhibition causes a lethal accumulation of toxic squalene inside the fungal cell, making terbinafine fundamentally fungicidal (kills the fungus). It is highly lipophilic, concentrating heavily in the skin, hair, and nails.",
        "Why_Not": "Antibacterial drugs (like Penicillin) target peptidoglycan. Antiviral drugs target DNA/RNA replication. Terbinafine specifically targets fungal ergosterol synthesis.",
        "Wow_Approach": "Unlike Griseofulvin (an older antifungal that is merely fungistatic and heavily teratogenic), Terbinafine actively kills the fungus and has a much wider margin of safety in cats and dogs."
    },
    1741: {
        "topic": "Lyme Disease Vector - Ixodes Ticks",
        "Core_Anatomy": "Systemic joints and kidneys.",
        "Pathogenesis_Immediate": "The primary tick vector responsible for transmitting Lyme disease is the Ixodes genus (the Black-legged tick or Deer tick).",
        "Pathogenesis_Deep": "Lyme disease is caused by the spirochete bacterium Borrelia burgdorferi. The Ixodes tick acquires the bacteria when feeding on infected wildlife reservoirs (like mice or deer). When the tick bites a dog, it must remain attached for at least 24-48 hours to fully reactivate and transmit the spirochetes into the dog's bloodstream. The bacteria then migrate to the joints, causing severe polyarthritis (shifting leg lameness), and occasionally to the kidneys (Lyme nephritis).",
        "Why_Not": "Rhipicephalus sanguineus (Brown Dog Tick) transmits Ehrlichia and Babesia. Tabanus (Horse fly) transmits Trypanosomes. Stomoxys (Stable fly) transmits Habronema.",
        "Wow_Approach": "Because the tick must be attached for over 24 hours to transmit Lyme disease, prompt daily visual inspection and removal of ticks after a walk in the woods is a highly effective preventative measure."
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
