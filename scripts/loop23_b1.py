import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2617: {
        "topic": "Suture Material - Natural vs Synthetic",
        "Core_Anatomy": "Surgical tissue closure.",
        "Pathogenesis_Immediate": "Silk is a NATURAL non-absorbable suture, whereas Polyamide, Polyester, and Polybutester are SYNTHETIC non-absorbables.",
        "Pathogenesis_Deep": "Suture materials are classified by origin (Natural vs Synthetic) and persistence (Absorbable vs Non-absorbable). Natural sutures (Catgut, Silk, Cotton) provoke a strong inflammatory response (macrophage and foreign body giant cell reaction) because they contain foreign proteins. Synthetic sutures (Nylon/Polyamide, Prolene, PDS) are inert polymers that cause minimal tissue reaction. Therefore, synthetic sutures are always preferred in modern surgery, especially for skin (nylon) and vascular (prolene) closures.",
        "Why_Not": "Polyamide (Nylon) and Polyester are synthetics. Silk is natural (spun by silkworms) and induces a severe tissue reaction.",
        "Wow_Approach": "Because silk is a multifilament natural fiber, it acts like a sponge (capillarity), wicking bacteria directly into the surgical wound. It should NEVER be used in contaminated wounds or the urinary tract."
    },
    2618: {
        "topic": "Cosmetic Surgery",
        "Core_Anatomy": "Dermal and superficial structures.",
        "Pathogenesis_Immediate": "Surgery performed solely to improve appearance or satisfy the owner's sentiments is termed Cosmetic Surgery.",
        "Pathogenesis_Deep": "Cosmetic surgeries in veterinary medicine include tail docking, ear cropping, debarking (ventriculocordectomy), and declawing (onychectomy). Historically performed to meet breed standards, these procedures provide zero medical benefit to the animal and cause unnecessary pain and potential long-term complications (e.g., phantom limb pain in declawed cats). Consequently, cosmetic surgeries are increasingly considered unethical and have been legally banned in many countries (including the UK, EU, and Australia) and strongly discouraged by the AVMA.",
        "Why_Not": "Elective surgery (like a spay) has a definitive medical benefit (preventing pyometra/cancer). Cosmetic surgery has NO medical benefit for the animal.",
        "Wow_Approach": "In countries where tail docking is banned, working dogs (like Spaniels) may still occasionally require therapeutic (not cosmetic) tail amputation later in life if they suffer severe, unhealing traumatic tail injuries."
    },
    2619: {
        "topic": "Pre-anaesthetic Drug Classes",
        "Core_Anatomy": "Central and peripheral nervous system.",
        "Pathogenesis_Immediate": "Drugs like Atropine and Glycopyrrolate are classified as Anticholinergics.",
        "Pathogenesis_Deep": "Pre-anaesthetic medication regimens typically combine different drug classes to achieve 'balanced anaesthesia'. (1) Anticholinergics (Atropine): Block muscarinic receptors to prevent bradycardia and reduce salivation. (2) Sedatives (Xylazine, Dexmedetomidine): Provide CNS depression and muscle relaxation. (3) Opioids (Morphine, Butorphanol): Provide pre-emptive analgesia. (4) General anaesthetics (Propofol, Isoflurane) induce unconsciousness but are NOT used as pre-anaesthetics.",
        "Why_Not": "Anticholinergics do NOT provide sedation or analgesia; their sole purpose is autonomic (parasympathetic) blockade.",
        "Wow_Approach": "Routine use of anticholinergics (Atropine) in all patients is no longer recommended because it causes tachycardia, which increases myocardial oxygen demand. It is now reserved specifically for treating vagally-induced bradycardia."
    },
    2621: {
        "topic": "Xylazine / Ketamine Dosing",
        "Core_Anatomy": "Central nervous system.",
        "Pathogenesis_Immediate": "3.3 mg/kg is a classic dosage reference, often pointing to specific sedative combinations or variations in species tolerance.",
        "Pathogenesis_Deep": "Drug dosages vary wildly between species due to differing receptor densities and metabolism. For example, Xylazine dosing requires extreme caution: Cattle are exquisitely sensitive to Xylazine (requiring only 0.05 mg/kg for standing sedation), whereas horses require roughly 1.1 mg/kg, and pigs require 2-3 mg/kg due to high resistance. Memorizing the precise decimal point for these powerful drugs is critical to prevent fatal overdoses.",
        "Why_Not": "Always double-check the species when selecting a dose. What sedates a horse will instantly kill a cow.",
        "Wow_Approach": "To remember Xylazine sensitivity: Cattle (most sensitive) > Sheep/Goats > Horses/Dogs > Pigs (least sensitive)."
    },
    2622: {
        "topic": "Xylazine Dose in Dogs",
        "Core_Anatomy": "Central nervous system (Alpha-2 Adrenoceptors).",
        "Pathogenesis_Immediate": "The standard sedative dose rate of Xylazine in dogs is 1 mg/kg (intravenously).",
        "Pathogenesis_Deep": "Xylazine is a potent alpha-2 agonist. In dogs, a dose of 1 mg/kg IV (or 2 mg/kg IM) provides reliable, deep sedation, analgesia, and muscle relaxation. However, it profoundly stimulates the chemoreceptor trigger zone (CRTZ), causing almost universal vomiting in cats and dogs shortly after administration. Furthermore, it causes an initial peripheral vasoconstriction (hypertension) followed by a profound, prolonged bradycardia and hypotension (second-degree AV blocks are common).",
        "Why_Not": "Doses higher than 1-2 mg/kg in dogs do not significantly increase the depth of sedation, but they drastically increase the risk of severe, fatal cardiovascular depression.",
        "Wow_Approach": "Because Xylazine reliably induces emesis in cats (at 0.4 - 1 mg/kg IM), it is actually the drug of choice for inducing therapeutic vomiting in cats that have ingested non-caustic toxins."
    },
    2623: {
        "topic": "Butyrophenone Derivative - Azaperone",
        "Core_Anatomy": "Central nervous system (Dopamine D2 receptors).",
        "Pathogenesis_Immediate": "Azaperone is a Butyrophenone derivative tranquilizer.",
        "Pathogenesis_Deep": "Tranquilizers in veterinary medicine fall into two main chemical classes: Phenothiazines (Acepromazine) and Butyrophenones (Azaperone, Droperidol). Azaperone blocks Dopamine (D2) receptors in the CNS. It is uniquely utilized almost exclusively in PIGS. It provides excellent tranquilization, reduces aggressive behavior (preventing fighting when mixing litters), and prevents Porcine Stress Syndrome (Malignant Hyperthermia) during transport.",
        "Why_Not": "Acepromazine is a phenothiazine. Etorphine is an opioid. Azaperone is the classic board-exam butyrophenone.",
        "Wow_Approach": "Never administer Azaperone intravenously to a pig; it causes a severe excitatory phase (paradoxical excitement). It must always be given deep intramuscularly (typically behind the ear)."
    },
    2624: {
        "topic": "Alpha-2 Agonist - Xylazine",
        "Core_Anatomy": "Central nervous system (Presynaptic Alpha-2 receptors).",
        "Pathogenesis_Immediate": "Xylazine is classified as an Alpha-2 Adrenoceptor Agonist.",
        "Pathogenesis_Deep": "Alpha-2 agonists (Xylazine, Detomidine, Medetomidine, Dexmedetomidine) bind to presynaptic alpha-2 receptors in the locus coeruleus of the brain. This binding provides negative feedback, halting the release of norepinephrine. The sudden lack of norepinephrine causes profound sedation (sleep-like state), analgesia, and central muscle relaxation. The major advantage of this drug class is that its effects can be completely and rapidly reversed by administering an alpha-2 antagonist (Yohimbine or Atipamezole).",
        "Why_Not": "Diazepam and Zolazepam are Benzodiazepines (GABA agonists). Tiletamine is a dissociative anaesthetic (NMDA antagonist).",
        "Wow_Approach": "The alpha-2/alpha-1 receptor selectivity ratio dictates the drug's safety. Xylazine has a low ratio (160:1), meaning it causes more non-target side effects. Dexmedetomidine is highly specific (1620:1), providing cleaner sedation with fewer peripheral side effects."
    },
    2625: {
        "topic": "Atropine Dose - Preanaesthetic in Dogs",
        "Core_Anatomy": "Parasympathetic nervous system (Muscarinic receptors).",
        "Pathogenesis_Immediate": "The standard preanaesthetic dose of Atropine in the dog is 0.02 - 0.04 mg/kg.",
        "Pathogenesis_Deep": "Atropine is an anticholinergic drug that acts as a competitive antagonist at postganglionic muscarinic acetylcholine receptors. When given at 0.02 - 0.04 mg/kg (SC or IM), it effectively blocks the vagus nerve's influence on the heart, preventing or treating bradycardia caused by vagal stimulation (e.g., endotracheal intubation, visceral traction during surgery, or opioid administration). It also dries up salivary and respiratory secretions.",
        "Why_Not": "Doses below 0.02 mg/kg can paradoxically CAUSE bradycardia initially by blocking presynaptic inhibitory M1 receptors before blocking postsynaptic M2 receptors in the heart. Therefore, exact dosing is critical.",
        "Wow_Approach": "Atropine crosses the blood-brain barrier and the placenta (affecting the fetus). Glycopyrrolate is a synthetic alternative that does NOT cross the blood-brain barrier or placenta, making it a safer choice for C-sections."
    },
    2626: {
        "topic": "Anaesthetic Pharmacology Distractor",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "This represents a numerical option (0.06 - 0.08 mg/kg) from the preceding Atropine dosage question.",
        "Pathogenesis_Deep": "Recognizing incorrect dosage ranges is as important as knowing the correct one. Overdosing Atropine (0.06+ mg/kg) causes severe tachycardia, decreased cardiac output (due to inadequate ventricular filling time), mydriasis, photophobia, and gut stasis (ileus).",
        "Why_Not": "Avoid high doses of anticholinergics unless treating organophosphate toxicity.",
        "Wow_Approach": "In cases of massive organophosphate poisoning (which causes extreme cholinergic SLUDGE signs), Atropine is given at massively higher doses (0.2 to 0.5 mg/kg) to block the overwhelmed muscarinic receptors."
    },
    2627: {
        "topic": "Anaesthetic Pharmacology - Correct Atropine Dose",
        "Core_Anatomy": "Vagus nerve and SA node of the heart.",
        "Pathogenesis_Immediate": "Re-affirmation that 0.02 - 0.04 mg/kg is the correct dosage range for Atropine in dogs.",
        "Pathogenesis_Deep": "Atropine acts extremely rapidly when given IV (within 1 minute), making it the emergency drug of choice for sudden intraoperative bradycardia. It increases the firing rate of the Sinoatrial (SA) node and increases conduction velocity through the Atrioventricular (AV) node.",
        "Why_Not": "If bradycardia is accompanied by hypertension (e.g., secondary to Dexmedetomidine administration), giving Atropine is CONTRAINDICATED because forcing the heart to beat faster against high vascular resistance drastically increases cardiac work and can induce fatal arrhythmias.",
        "Wow_Approach": "Rabbits possess a unique hepatic enzyme called 'Atropinase' which rapidly destroys Atropine within minutes. Therefore, Atropine is completely ineffective in about 30-40% of rabbits; Glycopyrrolate must be used instead."
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
