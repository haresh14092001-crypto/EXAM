import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1771: {
        "topic": "Equine Infectious Anemia (EIA) - Thrombocytopenia",
        "Core_Anatomy": "Platelets and erythrocytes.",
        "Pathogenesis_Immediate": "Severe platelet dysfunction and immune-mediated thrombocytopenia are classically matched with Equine Infectious Anemia (EIA).",
        "Pathogenesis_Deep": "EIA ('Swamp Fever') is caused by a lentivirus (retrovirus) transmitted by Tabanid flies. Once infected, the horse remains a lifelong carrier. The virus replicates in macrophages. The horse's immune system mounts a massive antibody response, but the virus constantly mutates its surface glycoproteins. These antibodies bind to both the virus and the horse's own platelets and RBCs (immune-complex deposition). This triggers massive complement-mediated destruction of platelets (thrombocytopenia) and RBCs (hemolytic anemia).",
        "Why_Not": "While other diseases cause anemia, EIA is the quintessential equine retrovirus that drives simultaneous, severe, immune-mediated platelet destruction, leading to petechial hemorrhages on the mucous membranes.",
        "Wow_Approach": "Because EIA is incurable and highly infectious via blood, any horse testing positive on the official Coggins Test (Agar Gel Immunodiffusion) must be legally quarantined for life or euthanized."
    },
    1780: {
        "topic": "Subjective Type Questions Header",
        "Core_Anatomy": "Veterinary Systemic Medicine.",
        "Pathogenesis_Immediate": "This header introduces subjective, essay-based questions requiring comprehensive pathological breakdowns.",
        "Pathogenesis_Deep": "Subjective answers require a structured breakdown of the etiology, pathogenesis, clinical signs, diagnosis, and treatment of a specific disease.",
        "Why_Not": "Unlike objective questions which rely on rote recall, subjective essays test the clinician's ability to synthesize a complete diagnostic pathway.",
        "Wow_Approach": "Always structure subjective answers with clear subheadings (Etiology, Pathogenesis, Clinical Signs, Treatment) to ensure maximum marks from the examiner."
    },
    1786: {
        "topic": "Short Notes Header",
        "Core_Anatomy": "Veterinary Systemic Medicine.",
        "Pathogenesis_Immediate": "This header introduces questions requiring concise, high-yield summaries of specific clinical topics.",
        "Pathogenesis_Deep": "Short notes should focus exclusively on the pathognomonic features of the disease rather than a broad, exhaustive essay.",
        "Why_Not": "Do not waste time writing a full essay for a 'short note' question; focus on the core mechanism and the definitive treatment.",
        "Wow_Approach": "Bullet points are highly effective for short notes, as they demonstrate clear, organized clinical reasoning."
    },
    1803: {
        "topic": "VMD Clinical Medicine II Header",
        "Core_Anatomy": "Specialized systemic medicine.",
        "Pathogenesis_Immediate": "This header denotes the progression into advanced clinical medicine, often covering infectious and metabolic diseases.",
        "Pathogenesis_Deep": "While VMD I covers general principles, VMD II dives deeply into specific infectious agents, vector-borne diseases, and complex multi-systemic conditions.",
        "Why_Not": "This section expects the clinician to integrate multiple body systems into a single unifying diagnosis.",
        "Wow_Approach": "Pay close attention to vector-borne transmission cycles in this section."
    },
    1805: {
        "topic": "VMD 511 - Animal Welfare and Jurisprudence Header",
        "Core_Anatomy": "Veterinary Legal Framework.",
        "Pathogenesis_Immediate": "This header introduces the objective testing section for veterinary law and ethics in India.",
        "Pathogenesis_Deep": "This section tests rote memorization of specific Indian Penal Code (IPC) sections, acts of parliament (like the PCA Act), and exact dates of legislation implementation.",
        "Why_Not": "Statutory law cannot be deduced biologically; it must be memorized exactly as written in the legal code.",
        "Wow_Approach": "Precision is paramount; misquoting a legal section in a real-world forensic report can invalidate a criminal prosecution."
    },
    1810: {
        "topic": "Veterinary Forensics - Somatic vs Molecular Death",
        "Core_Anatomy": "Systemic vital functions vs cellular metabolism.",
        "Pathogenesis_Immediate": "The death of an individual animal as a whole is called 'Somatic Death', and the subsequent death of the individual tissues/cells is called 'Molecular Death'.",
        "Pathogenesis_Deep": "(1) Somatic death occurs the exact moment the vital tripod (brain, heart, lungs) irreversibly ceases to function. The animal is clinically dead. (2) Molecular (Cellular) death occurs slowly over the following hours. Even though the heart has stopped, individual cells (like muscle or sperm cells) continue to undergo anaerobic metabolism until their ATP reserves are completely exhausted. Once ATP depletes, the cells undergo autolysis (molecular death), triggering rigor mortis.",
        "Why_Not": "Necrosis is the pathological death of tissue in a LIVING animal. Molecular death is the physiological death of tissue AFTER somatic death.",
        "Wow_Approach": "Because molecular death takes time, a veterinarian can successfully extract viable, motile sperm from the epididymis of a valuable stud bull several hours after he has suffered somatic death."
    },
    1811: {
        "topic": "Veterinary Jurisprudence - IPC Section 377 (Repeated)",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "Bestiality (unnatural sexual offenses involving animals) matches specifically to IPC Section 377.",
        "Pathogenesis_Deep": "Under the Indian Penal Code, Section 377 criminalizes carnal intercourse against the order of nature with any animal. The forensic veterinarian's role is strictly objective: to examine the animal for mucosal trauma, collect trace evidence (semen/DNA swabs from the vagina or rectum), and secure the chain of custody. The vet does not determine guilt, only the presence of physical evidence consistent with abuse.",
        "Why_Not": "Section 428/429 deals with mischief (killing). Section 377 is exclusively for unnatural sexual offenses.",
        "Wow_Approach": "Always use a sterile swab moistened with sterile saline (not plain water, which lyses cells via osmosis) when collecting forensic DNA evidence from the mucosa."
    },
    1812: {
        "topic": "Veterinary Jurisprudence - Livestock Importation Act",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The Livestock Importation Act was enacted in India in the year 1898.",
        "Pathogenesis_Deep": "To protect indigenous livestock from devastating exotic diseases (like Rinderpest, African Horse Sickness, and CBPP), the British Indian government passed the Livestock Importation Act of 1898. It legally empowers the central government to regulate, restrict, or absolutely prohibit the import of livestock and livestock products (meat, hides, semen) that could introduce infectious or contagious disorders into the country.",
        "Why_Not": "The Glanders and Farcy Act was 1899. The PCA (Prevention of Cruelty to Animals) Act was 1960. The Importation Act was 1898.",
        "Wow_Approach": "Even today, this Act forms the foundational legal basis for the strict quarantine stations located at major Indian airports and seaports."
    },
    1813: {
        "topic": "Veterinary Ethics - VCI Regulations",
        "Core_Anatomy": "N/A - Professional Conduct.",
        "Pathogenesis_Immediate": "The Veterinary Council of India (VCI) Act was established in 1984 to regulate veterinary practice and education.",
        "Pathogenesis_Deep": "The Indian Veterinary Council Act, 1984, led to the creation of the VCI. The VCI establishes the Minimum Standards of Veterinary Education (MSVE) and maintains the Indian Veterinary Practitioners Register. A person cannot legally practice veterinary medicine or perform surgery in India unless they hold a recognized degree (BVSc & AH) and are actively registered with the VCI or a State Veterinary Council. Practicing without registration is a punishable offense.",
        "Why_Not": "The AWBI regulates animal welfare. The VCI specifically regulates the academic and professional standards of the veterinarians themselves.",
        "Wow_Approach": "If a registered veterinarian is found guilty of gross professional negligence or moral turpitude (like perjury or issuing fake health certificates), the VCI has the statutory power to permanently strike their name from the national register."
    },
    1820: {
        "topic": "Veterinary Forensics - Stab Wounds (Punctured Wounds)",
        "Core_Anatomy": "Cutaneous and deep systemic tissues.",
        "Pathogenesis_Immediate": "In forensic pathology, a Stab wound is classified as a Punctured wound, characterized by a depth that is significantly greater than its surface length.",
        "Pathogenesis_Deep": "Forensic veterinarians must meticulously classify wounds to determine the weapon used. (1) An Incised wound (slash) is longer than it is deep, caused by the slicing motion of a sharp edge (like a scalpel or razor). (2) A Stab/Punctured wound is much deeper than it is long on the skin surface, caused by the thrusting motion of a pointed instrument (like a pitchfork, nail, or dagger). Punctured wounds are highly dangerous because they carry anaerobic bacteria (Clostridium tetani) deep into hypoxic tissues while the small surface hole seals over rapidly.",
        "Why_Not": "A laceration is caused by blunt force tearing the skin (has ragged, bruised edges). A stab wound has clean edges but massive depth.",
        "Wow_Approach": "When documenting a stab wound in a medicolegal post-mortem, never blindly probe the wound tract. You must carefully dissect the tissue layer by layer to trace the exact path and determine which vital internal organ was pierced."
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
print(f"Batch 2/5 DONE: Updated {updated} questions.")
