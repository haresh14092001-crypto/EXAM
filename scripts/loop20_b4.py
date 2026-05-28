import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2354: {
        "topic": "VPM Match the Following Header",
        "Core_Anatomy": "Systemic preventive veterinary medicine.",
        "Pathogenesis_Immediate": "This section requires precise matching of organisms/diseases to their key pathognomonic features or associated terms.",
        "Pathogenesis_Deep": "High-yield matches: Bipolar organism = Pasteurella/HS; LCL bodies = Chlamydia; Diamond skin = Erysipelas; Gas gangrene = Cl. novyi.",
        "Why_Not": "Use process of elimination—anchor on the most certain pair first.",
        "Wow_Approach": "Bipolar safety-pin staining with Giemsa is the fastest field diagnosis for Hemorrhagic Septicemia."
    },
    2355: {
        "topic": "Hemorrhagic Septicemia - Bipolar Organism",
        "Core_Anatomy": "Systemic vasculature and lymph nodes.",
        "Pathogenesis_Immediate": "The 'Bipolar organism' (safety-pin appearance on Giemsa staining) is matched to Pasteurella multocida, the causative agent of Hemorrhagic Septicemia (HS).",
        "Pathogenesis_Deep": "Pasteurella multocida is a Gram-negative, non-motile coccobacillus. When stained with Giemsa or Leishman stain, it exhibits pathognomonic 'bipolar staining'—the two poles of the bacterium take up intense dark blue stain while the center remains pale, giving the appearance of a 'safety pin'. Blood smears or tissue impression smears from HS-affected cattle processed with Giemsa stain can rapidly confirm the diagnosis at post-mortem.",
        "Why_Not": "Chlamydiosis produces LCL bodies (Levinthal-Cole-Lillie bodies) within cells, not bipolar staining. Anthrax produces the McFadyean capsule reaction.",
        "Wow_Approach": "HS (Hemorrhagic Septicemia/Barbone) is the most economically devastating cattle disease in South and Southeast Asia. The disease can kill a buffalo within 8-24 hours—faster than the farmer can arrange veterinary treatment."
    },
    2356: {
        "topic": "Chlamydiosis - LCL Bodies",
        "Core_Anatomy": "Epithelial cells and macrophages.",
        "Pathogenesis_Immediate": "Chlamydiosis in birds and animals is matched to LCL bodies (Levinthal-Cole-Lillie bodies).",
        "Pathogenesis_Deep": "Chlamydia psittaci exists in two forms: (1) Elementary Bodies (EB)—the small, infectious, extracellular form that enters host cells via receptor-mediated endocytosis. (2) Reticulate Bodies (RB)—the larger, intracellular, replicating form. Inside the host cell, EBs transform into RBs, replicate massively, then condense back into EBs. This entire intracellular lifecycle occurs within a membrane-bound inclusion body (phagosome), which appears as a large, basophilic cytoplasmic inclusion on Giemsa staining—historically named 'LCL bodies' (Levinthal-Cole-Lillie bodies).",
        "Why_Not": "Bipolar staining is for Pasteurella (HS). Negri bodies are for Rabies. Cowdry Type A bodies are for Herpesviruses.",
        "Wow_Approach": "In humans, the term for avian-to-human Chlamydia psittaci infection is 'Psittacosis'; for Chlamydia abortus (from parturient sheep) it is 'Enzootic abortion of ewes' (EAE) which is a major occupational hazard for pregnant women farmers."
    },
    2357: {
        "topic": "Mycotic Dermatitis - Dermatophilosis",
        "Core_Anatomy": "Stratum spinosum and stratum corneum of the skin.",
        "Pathogenesis_Immediate": "Mycotic dermatitis (Streptothricosis / Rain Scald / Lumpy Wool Disease) is caused by Dermatophilus congolensis.",
        "Pathogenesis_Deep": "Dermatophilus congolensis is a branching, filamentous Actinomycete bacterium (not a true fungus, despite the 'mycotic' misnomer). After skin barrier disruption (by prolonged rain, tick bites, or wounds), the motile zoospores of D. congolensis penetrate the epidermis. They germinate and form filaments that invade the stratum spinosum, triggering an acute inflammatory response. The skin forms characteristic thick, matted, 'paintbrush' crusts of coagulated exudate and infected epidermis that are pathognomonic for the disease.",
        "Why_Not": "True fungal dermatitis (dermatophytosis/ringworm) is caused by Trichophyton or Microsporum—not Dermatophilus. Diamond skin disease is Erysipelothrix.",
        "Wow_Approach": "To differentiate Dermatophilosis from Ringworm in the field: soak a crust in water for 4 hours, then crush it between glass slides and stain with Giemsa. Dermatophilosis shows the classic 'railroad track' branching filaments composed of rows of cocci."
    },
    2363: {
        "topic": "Oxytetracycline (OTC) - Anaplasmosis Treatment",
        "Core_Anatomy": "Erythrocytes (intracellular Anaplasma marginale).",
        "Pathogenesis_Immediate": "Oxytetracycline (OTC) is the specific drug of choice matched to Anaplasmosis.",
        "Pathogenesis_Deep": "Anaplasma marginale is an obligate intracellular rickettsial organism residing within erythrocytes. Like all rickettsiae, it lacks a cell wall and is resistant to beta-lactam antibiotics. Oxytetracycline penetrates erythrocyte membranes and inhibits the organism's 30S ribosomal protein synthesis, effectively clearing the bacteremia. For acute cases, a single high-dose IV OTC injection (22 mg/kg) combined with supportive blood transfusion in severely anemic animals is the emergency protocol.",
        "Why_Not": "Penicillin has no activity against rickettsiae (no cell wall). The answer is OTC (Oxytetracycline) or Doxycycline for all rickettsial diseases.",
        "Wow_Approach": "OTC can also be used for chemoprophylaxis—a single long-acting OTC injection every 28 days completely prevents clinical Anaplasmosis in cattle entering endemic tick areas (e.g., during cattle drives or when moving stock to new regions)."
    },
    2373: {
        "topic": "Kumri - Equine Cerebrospinal Nematodiasis",
        "Core_Anatomy": "Equine spinal cord (white matter).",
        "Pathogenesis_Immediate": "Kumri (equine cerebrospinal nematodiasis) is noticed most commonly in the Horse.",
        "Pathogenesis_Deep": "Kumri is caused by the aberrant migration of Setaria digitata larvae in the spinal cord of horses (and occasionally cattle in Northern India). Setaria digitata is a natural parasite of cattle where it lives harmlessly in the peritoneum. However, if its microfilariae are accidentally ingested by an intermediate host (Aedes mosquito) and then inoculated into a horse (an abnormal host), the L3 larvae undergo erratic migration through the spinal cord white matter, causing severe focal malacia (tissue softening). The horse develops progressive hindlimb ataxia and paralysis.",
        "Why_Not": "The host that truly suffers is the horse—in the natural host (cattle), the adult Setaria in the peritoneum causes no clinical signs.",
        "Wow_Approach": "Kumri is a seasonal disease in India, occurring predominantly in October-November (post-monsoon) when the Aedes mosquito population peaks, transmitting the L3 larvae from infected cattle to horses grazing together in the same paddock."
    },
    2375: {
        "topic": "Neospora caninum - Bovine Abortion",
        "Core_Anatomy": "Fetal nervous system (brain and spinal cord).",
        "Pathogenesis_Immediate": "Neospora caninum is a major cause of bovine abortion, causing repetitive late-term abortion storms in dairy herds.",
        "Pathogenesis_Deep": "Neospora caninum is an obligate intracellular apicomplexan protozoan. Its definitive host is the dog (and other canids). Dogs shed oocysts in feces; cattle ingest oocysts from contaminated feed/water and become infected. In pregnant cows, the tachyzoites cross the placenta and infect the fetal brain and spinal cord, causing necrotic encephalitis and fetal death at 3-9 months of gestation. Critically, persistently infected cows also transmit the parasite vertically (transplacental) to subsequent calves, causing repeated abortion in the same cow for multiple pregnancies.",
        "Why_Not": "Sarcocystis causes mild muscle cysts in cattle (rarely clinical). Toxoplasma causes abortion in sheep/goats (via cat oocysts). Trichomonas causes early embryonic death. Only Neospora caninum causes the specific repetitive late-term bovine abortion storms.",
        "Wow_Approach": "If a dairy farm has multiple cows aborting at 6-8 months in successive years, and the herd keeps dogs on-farm, suspect Neospora. The diagnosis is confirmed by IFAT (Indirect Fluorescent Antibody Test) on abortion-storm blood serum."
    },
    2376: {
        "topic": "FMD Inactivant - BEI (Binary Ethylenimine)",
        "Core_Anatomy": "FMD virus nucleic acid.",
        "Pathogenesis_Immediate": "The primary inactivant used for producing inactivated FMD vaccines is BEI (Binary Ethylenimine), not Formalin.",
        "Pathogenesis_Deep": "Binary Ethylenimine (BEI) is an aziridine compound. It specifically alkylates the guanine residues in the viral RNA genome, irreversibly destroying the genetic information while leaving the viral capsid proteins (the antigens) intact and immunogenic. This is critical for an FMD vaccine—the inactivated virus must retain its antigenic structure to induce neutralizing antibodies but must be completely unable to replicate. BEI achieves this with greater efficiency and less protein damage than formaldehyde.",
        "Why_Not": "Formalin (formaldehyde) is used for many other killed vaccines but damages the surface proteins of FMD virus, reducing antigenicity. NAOH (sodium hydroxide) inactivates FMD in the field (pH >9) but destroys antigenicity, making it unsuitable for vaccines.",
        "Wow_Approach": "The reason FMD vaccine requires cold chain storage (2-8°C) is that the BEI-inactivated viral particles are more heat-sensitive than live-attenuated vaccines, and loss of cold chain causes protein denaturation and loss of the critical 146S intact capsid antigen."
    },
    2377: {
        "topic": "FMD Outbreak Response - Ring Vaccination",
        "Core_Anatomy": "Susceptible animal population (epidemiological buffer zone).",
        "Pathogenesis_Immediate": "Vaccination of all susceptible animals in a prescribed area around an FMD outbreak is called Ring Vaccination.",
        "Pathogenesis_Deep": "Ring vaccination is a classic outbreak containment strategy. A defined geographical 'ring' or buffer zone (typically 3-10 km radius) is drawn around the confirmed outbreak farm. ALL susceptible species (cattle, buffalo, sheep, goats, pigs) within this ring are immediately vaccinated with the matching FMD serotype vaccine, regardless of their disease status. This creates an immune barrier of non-transmitting animals that physically prevents the virus from spreading beyond the ring.",
        "Why_Not": "Stamping-out (blanket depopulation) is used in FMD-free countries with no FMD vaccination history. Herd vaccination is targeted to the specific infected herd only. Ring vaccination protects the surrounding population.",
        "Wow_Approach": "Ring vaccination was the cornerstone strategy used to eradicate Rinderpest from Africa and Asia in the 1990s-2000s, moving vaccination rings progressively inward to close off the last remaining endemic pockets."
    },
    2378: {
        "topic": "BVD - Antigenic Relationship with Border Disease and CSF",
        "Core_Anatomy": "Systemic immune system (Pestivirus cross-reactivity).",
        "Pathogenesis_Immediate": "Bovine Viral Diarrhea Virus (BVD) is antigenically related to BOTH Border Disease virus (ovine) AND Classical Swine Fever virus.",
        "Pathogenesis_Deep": "BVD, Border Disease, and Classical Swine Fever are all caused by closely related Pestiviruses within the family Flaviviridae. They share common envelope glycoproteins (particularly E2/gp53) that are cross-reactive antigenically. This means: (1) Serum from BVD-vaccinated cattle may cross-react and give false-positive results in CSF ELISA tests. (2) BVD vaccines may provide partial cross-protection against Border Disease in sheep. (3) This antigenic relationship is exploited in the 'Virus Neutralization Test' to speciate Pestivirus isolates.",
        "Why_Not": "CDV (Canine Distemper Virus) is a Morbillivirus—completely unrelated to Pestiviruses.",
        "Wow_Approach": "This cross-reactivity is a major diagnostic pitfall: a CSF outbreak in vaccinated pigs may initially give false-negative results if the ELISA uses antibodies that also detect BVD antibodies from the vaccination."
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
