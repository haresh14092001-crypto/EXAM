import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1930: {
        "topic": "Veterinary Jurisprudence - Subpoena",
        "Core_Anatomy": "N/A - Legal Procedure.",
        "Pathogenesis_Immediate": "A Subpoena is a formal legal document issued by a court commanding a person (such as a veterinarian) to appear and give testimony or produce evidence.",
        "Pathogenesis_Deep": "In veterinary forensic cases (e.g., cruelty to animals, malicious poisoning, or meat adulteration), the presiding magistrate will issue a 'Subpoena ad testificandum' to compel the veterinarian to testify regarding their post-mortem findings. If the court requires the veterinarian to bring physical evidence (like the actual post-mortem report, toxicology results, or the weapon), they will issue a 'Subpoena duces tecum'.",
        "Why_Not": "Ignoring a subpoena is a criminal offense (Contempt of Court) under the Indian Penal Code.",
        "Wow_Approach": "Unlike an ordinary witness who only testifies to what they saw, a veterinarian summoned by subpoena acts as an 'Expert Witness', meaning they are legally permitted to offer their professional OPINION on how the animal died."
    },
    1950: {
        "topic": "Exam Instructions Header",
        "Core_Anatomy": "N/A - Examination Rules.",
        "Pathogenesis_Immediate": "Standard examination protocol header denoting the time limit for the objective section.",
        "Pathogenesis_Deep": "Objective questions require rapid cognitive recall; strict time limits prevent students from utilizing extensive deductive reasoning, forcing them to rely on ingrained rote knowledge.",
        "Why_Not": "Subjective sections allow for prolonged synthesis of information.",
        "Wow_Approach": "In objective exams, always answer the questions you know instantly first, then circle back to the challenging ones to maximize point yield."
    },
    1951: {
        "topic": "VMD Objective Section Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Marks the beginning of the objective testing phase for VMD, focusing on rapid recall of systemic pathology.",
        "Pathogenesis_Deep": "This section typically heavily tests toxicology and metabolic diseases because these present with acute, pathognomonic objective signs.",
        "Why_Not": "Subjective essays test the pathogenesis; this section tests the exact etiology.",
        "Wow_Approach": "Always read the units carefully in objective questions."
    },
    1952: {
        "topic": "VMD Fill in the Blanks Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of clinical terms without the benefit of elimination.",
        "Pathogenesis_Deep": "This format tests whether a clinical sign or legal parameter has been perfectly linked in memory to its specific pathophysiological etiology or statute.",
        "Why_Not": "Vague answers will not receive credit.",
        "Wow_Approach": "Rely on your first instinct for these blanks; overthinking often leads to changing a correct specific term to an incorrect generic one."
    },
    1971: {
        "topic": "VMD Objective Section - Multiple Choice Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "This header introduces standard MCQs, requiring the clinician to eliminate distractor etiologies.",
        "Pathogenesis_Deep": "MCQs in veterinary medicine often pair a disease with its most confusing differential. Success depends on identifying the single 'rule-out' clinical sign.",
        "Why_Not": "Do not select an answer simply because it causes similar signs; it must cause the EXACT signs described.",
        "Wow_Approach": "Read all four options before selecting an answer; the 'best' answer is required, not just the first plausible one."
    },
    1972: {
        "topic": "Porcine Diagnostics - Tuberculin Testing Site",
        "Core_Anatomy": "Cutaneous immune system (base of the ear).",
        "Pathogenesis_Immediate": "In pigs, the specific anatomical site used for Intradermal Tuberculin Testing is the loose skin at the base of the ear.",
        "Pathogenesis_Deep": "Unlike cattle (where the test is performed on the mid-cervical neck or caudal fold of the tail), pigs possess thick, tight skin over most of their body that does not clearly demonstrate delayed Type-IV hypersensitivity swelling. The skin at the base (dorsal aspect) of the ear is thin, relatively hairless, and highly vascular, allowing for accurate measurement of the tuberculin-induced granulomatous swelling 48-72 hours post-injection.",
        "Why_Not": "The caudal fold is strictly for cattle. The cervical fold is for cattle and primates. The thigh region is not used due to excessive subcutaneous fat masking the swelling in pigs.",
        "Wow_Approach": "In avian species (chickens), the equivalent specific testing site for TB is the wattle."
    },
    1973: {
        "topic": "Animal Welfare - Ban on Performing Animals",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "Under the Performing Animals Rules (enacted under the PCA Act), certain wild species like Bears, Monkeys, Lions, Tigers, and Panthers are absolutely prohibited from being exhibited or trained as performing animals.",
        "Pathogenesis_Deep": "In 1998, the Indian Government (acting on advice from the AWBI) issued a historic notification banning the use of these specific wild animals in circuses and street performances (e.g., dancing bears, circus tigers). The law recognizes that training these apex predators and wild primates inherently requires immense cruelty, starvation, and physical beatings to break their spirit.",
        "Why_Not": "Domesticated animals like dogs and horses can still be trained and exhibited, provided the trainer is legally registered with the AWBI and adheres to strict welfare guidelines.",
        "Wow_Approach": "This specific ban effectively ended the centuries-old tradition of the 'Madari' (street performers with dancing sloth bears and macaques) in India."
    },
    1974: {
        "topic": "Animal Welfare Board of India (AWBI) - Funding",
        "Core_Anatomy": "N/A - Institutional Framework.",
        "Pathogenesis_Immediate": "The official funds of the Animal Welfare Board of India (AWBI) consist of Grants from the Government, Contributions, and Subscriptions (All of the above).",
        "Pathogenesis_Deep": "The AWBI is a statutory advisory body. To maintain its massive operational scope (funding thousands of local SPCAs and gaushalas, running national ABC-ARV rabies control programs, and providing disaster relief for animals), it relies on a multi-tiered funding structure defined in the PCA Act 1960. It receives direct parliamentary grants, but is also legally empowered to accept massive private charitable contributions and subscriptions from animal welfare philanthropists.",
        "Why_Not": "It is not solely reliant on government grants, which allows it functional autonomy to pursue welfare activities even if state budgets are tight.",
        "Wow_Approach": "The AWBI uses these funds to provide 100% financial assistance to local NGOs to build animal shelters and purchase veterinary ambulances."
    },
    1975: {
        "topic": "Animal Welfare Board of India (AWBI) - Funding (Continuation)",
        "Core_Anatomy": "N/A - Institutional Framework.",
        "Pathogenesis_Immediate": "This is a continuation of the AWBI funding structure options (Grants, Contributions, Subscriptions).",
        "Pathogenesis_Deep": "The ability to accept private subscriptions and donations legally insulates the AWBI from political pressure and ensures that animal welfare projects can be continuously funded. All NGOs seeking these funds must undergo strict veterinary audits to prove the money is being used for genuine animal care.",
        "Why_Not": "Funding cannot be diverted for non-animal welfare purposes.",
        "Wow_Approach": "AWBI grants are the primary financial backbone for the nationwide 'Catch-Neuter-Vaccinate-Release' (CNVR) program for stray dogs in India."
    },
    1976: {
        "topic": "Ovine Enterotoxemia - Pulpy Kidney Disease Trigger",
        "Core_Anatomy": "Gastrointestinal tract (starch overload) and systemic vasculature.",
        "Pathogenesis_Immediate": "A presumptive diagnosis of Enterotoxemia (Pulpy Kidney Disease) is based on the sudden death of rapidly growing lambs fed a rich, high-carbohydrate (starch) diet.",
        "Pathogenesis_Deep": "Clostridium perfringens Type D lives harmlessly in the sheep's gut in low numbers. The disease is purely diet-driven. When a lamb over-consumes a highly fermentable carbohydrate diet (like lush spring pasture or heavy grain rations), the rapid fermentation produces massive amounts of undigested starch in the intestines. This starch acts as an explosive growth medium for Type D clostridia, which rapidly multiply and secrete the lethal Epsilon toxin. The toxin causes massive vascular endothelial damage, leading to fatal brain edema and autolysis of the kidneys.",
        "Why_Not": "A protein-rich or high-fiber diet does not trigger the explosive clostridial overgrowth; it specifically requires the rapidly fermentable carbohydrates.",
        "Wow_Approach": "This is why Pulpy Kidney Disease is ironically known as 'Overeating Disease' and almost exclusively kills the fattest, fastest-growing, and most valuable lambs in the flock."
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
