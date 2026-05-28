import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2264: {
        "topic": "Caseous Lymphadenitis - Corynebacterium",
        "Core_Anatomy": "Superficial and internal lymph nodes.",
        "Pathogenesis_Immediate": "Necrosis (caseation/suppuration) of the lymph nodes in sheep and goats is caused by Corynebacterium pseudotuberculosis.",
        "Pathogenesis_Deep": "Corynebacterium pseudotuberculosis produces a powerful phospholipase D exotoxin that damages vascular endothelium and inhibits neutrophil migration. This allows the bacteria to establish persistent infection within macrophages in lymph nodes. The resulting lesion is a characteristic 'onion ring' abscess with alternating concentric layers of necrotic pus (green-yellow, dry, caseous material) and connective tissue, pathognomonic for Caseous Lymphadenitis (CL/Cheesy Gland).",
        "Why_Not": "Staphylococcus causes hot, liquid abscess formation without the concentric layering. Streptococcus causes lymphadenopathy in Strangles. Pseudomonas causes wound infections.",
        "Wow_Approach": "Corynebacterium pseudotuberculosis can spread to internal lymph nodes and lungs, causing the devastating 'Thin Ewe Syndrome' in chronically infected animals that appear healthy externally but are slowly dying from internal abscesses."
    },
    2265: {
        "topic": "Brucella - Columbia Media",
        "Core_Anatomy": "N/A - Bacteriological Culture.",
        "Pathogenesis_Immediate": "Brucella species are cultured on specialized media; Columbia Blood Agar base supplemented with selective antibiotics (Farrell's Medium) is the preferred culture medium.",
        "Pathogenesis_Deep": "Brucella spp. are fastidious organisms requiring enriched culture media for primary isolation. Serum Dextrose Agar, Tryptic Soy Agar, and Columbia Blood Agar base are all acceptable enriched media. However, since Brucella is highly zoonotic, all culture work must be performed in a Biosafety Level 3 (BSL-3) cabinet. The growth is very slow (3-7 days), and CO2 (5-10%) is required for B. abortus on primary isolation.",
        "Why_Not": "Nutrient Agar alone is not enriched enough for primary Brucella isolation. Tryptic Soy Agar with appropriate supplements is acceptable.",
        "Wow_Approach": "Because Brucella can aerosolize during culture manipulation, laboratory-acquired Brucellosis is a significant occupational hazard—making real-time PCR on clinical samples the preferred diagnostic approach in most modern labs."
    },
    2267: {
        "topic": "Johne's Disease - Johne's Bacillus / MAP",
        "Core_Anatomy": "Ileal submucosa and mesenteric lymph nodes.",
        "Pathogenesis_Immediate": "Johne's Disease (Paratuberculosis) is caused by Mycobacterium avium subsp. paratuberculosis (MAP).",
        "Pathogenesis_Deep": "MAP is an extremely slow-growing mycobacterium requiring 8-16 weeks for primary culture. It establishes a profound granulomatous enteritis in the ileum, causing protein-losing enteropathy. The hallmark clinical sign is profuse, watery, non-bloody diarrhea without pain ('hose pipe diarrhea') combined with progressive weight loss and severe 'Bottle Jaw' (submandibular edema from hypoproteinemia).",
        "Why_Not": "Listeriosis causes brainstem disease. Leptospirosis causes nephritis. Brucellosis causes abortion. Only MAP causes chronic granulomatous enteritis with the classic clinical triad (diarrhea + weight loss + bottle jaw) in cattle.",
        "Wow_Approach": "The Map protein ELISA serology test is now the primary herd screening tool because culturing MAP takes 4 months. However, ELISA is negative during the early subclinical phase (false negatives in carriers), requiring a combination of ELISA AND fecal PCR for comprehensive herd testing."
    },
    2268: {
        "topic": "Leptospirosis Treatment - Doxycycline",
        "Core_Anatomy": "Renal tubular epithelium and systemic circulation.",
        "Pathogenesis_Immediate": "Leptospirosis can be treated successfully using Doxycycline (or Penicillin G for the early septicemic phase).",
        "Pathogenesis_Deep": "Treatment of leptospirosis is phase-dependent. (1) Early septicemic phase (first week): High-dose Penicillin G or Ampicillin is the drug of choice, as the spirochetes are in the bloodstream. (2) Immune phase (second week onward): The spirochetes have already localized in the renal tubules. Doxycycline is the drug of choice as it achieves high urinary concentrations and eliminates the renal carrier state. Doxycycline is also used prophylactically in high-risk personnel entering endemic areas.",
        "Why_Not": "Streptomycin has activity but significant nephrotoxicity, which is contraindicated in an already renally compromised leptospirosis patient. Gentamicin is similarly nephrotoxic. Isoniazid is for tuberculosis only.",
        "Wow_Approach": "Doxycycline 200 mg given once weekly is the WHO-recommended chemoprophylaxis protocol for humans entering areas flooded during leptospirosis outbreaks (e.g., after a monsoon)."
    },
    2269: {
        "topic": "Equine Strangles - Autogenous Vaccine",
        "Core_Anatomy": "Lymph nodes of the head (Streptococcus equi subsp. equi).",
        "Pathogenesis_Immediate": "Autogenous (autologous) vaccines are specifically preferred for the management of Strangles in horses.",
        "Pathogenesis_Deep": "An autogenous vaccine is prepared from the specific S. equi equi strain isolated from the affected horses in the outbreak on the same farm (the patient's own bacterial strain). Because S. equi subsp. equi shows significant strain-to-strain variation in surface protein antigens (particularly the SeM protein), using a commercially available generic S. equi bacterin may not perfectly match the outbreak strain. The autogenous vaccine guarantees antigenic identity, potentially eliciting a more effective and protective immune response.",
        "Why_Not": "Glanders (B. mallei) does not use autogenous vaccines; infected horses are euthanized. Tetanus uses a standardized toxoid vaccine. Fowl Cholera uses commercial bacterins.",
        "Wow_Approach": "Autogenous Strangles vaccines are typically injected intramuscularly, but intranasal live-attenuated vaccines (like Pinnacle IN) that stimulate mucosal IgA at the site of infection are now considered more physiologically appropriate."
    },
    2270: {
        "topic": "VPM Match the Following Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This section requires pairing specific diseases with their definitive diagnostic tests, vaccines, or pathognomonic features.",
        "Pathogenesis_Deep": "Match questions test the clinician's ability to rapidly pair a diagnostic tool with its specific target disease without contextual clues.",
        "Why_Not": "Process of elimination is essential—match the most certain pairs first to narrow the remaining options.",
        "Wow_Approach": "The key VPM test-disease pairs: MAT=Leptospirosis; Coggins/AGID=EIA; Ascoli=Anthrax; Mallein=Glanders; Casoni=Hydatid; BBAT/RBPT=Brucellosis."
    },
    2271: {
        "topic": "Maedi-Visna - Sigurdsson's Vaccine",
        "Core_Anatomy": "Lungs (Maedi) and brainstem/spinal cord (Visna).",
        "Pathogenesis_Immediate": "Sigurdsson's vaccine (the first vaccine ever developed for a retrovirus) is specifically associated with Maedi-Visna.",
        "Pathogenesis_Deep": "Maedi-Visna is caused by an Ovine Lentivirus (a retrovirus). 'Sigurdsson' refers to Dr. Björn Sigurdsson, the Icelandic virologist who first discovered and described this retroviral disease in Iceland sheep in the 1950s. He attempted to develop a protective vaccine (Sigurdsson's vaccine) for the Icelandic sheep. However, because lentiviruses integrate their genetic material into the host genome, developing effective vaccines against them remains extremely challenging, and his original vaccine provided only limited protection.",
        "Why_Not": "Lasota vaccine is for Newcastle Disease. Sterne is for Anthrax. Sigurdsson's is strictly historical for Maedi-Visna.",
        "Wow_Approach": "Sigurdsson's discovery of Maedi-Visna led him to coin the term 'slow virus infections'—the conceptual framework that later facilitated the understanding and discovery of HIV/AIDS in humans decades later."
    },
    2272: {
        "topic": "Clostridium novyi - Gas Gangrene",
        "Core_Anatomy": "Subcutaneous and deep muscle tissue.",
        "Pathogenesis_Immediate": "Clostridium novyi (type A and type B) is matched to Gas Gangrene (Malignant Edema) and Black Disease.",
        "Pathogenesis_Deep": "(1) C. novyi Type A causes Gas Gangrene (in wounds), producing Alpha toxin (a lecithinase) that destroys cell membranes, causing massive tissue necrosis with gas production. (2) C. novyi Type B (also called C. haemolyticum) causes Black Disease (Infectious Necrotic Hepatitis) in sheep, where dormant spores in the liver are activated by migrating Fasciola hepatica larvae. The resulting liver necrosis and massive toxin production cause rapid death.",
        "Why_Not": "C. chauvoei causes Black Quarter (Blackleg). C. perfringens type D causes Pulpy Kidney (Enterotoxemia). C. septicum causes Braxy and Malignant Edema. C. novyi specifically causes Gas Gangrene and Black Disease.",
        "Wow_Approach": "In Black Disease, the carcass rapidly turns black due to the auto-digestion caused by the Alpha toxin and associated putrefaction—the 'black' appearance comes from the dark, infarcted liver lobes visible through the abdominal wall and the rapidly decomposing carcass."
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
