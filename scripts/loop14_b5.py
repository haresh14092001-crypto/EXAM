import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1636: {
        "topic": "Veterinary Forensics - Algor Mortis",
        "Core_Anatomy": "Post-mortem body surface and ambient temperature.",
        "Pathogenesis_Immediate": "After death, the body surface typically becomes cold (Algor Mortis) within 3 to 4 hours in domestic animals.",
        "Pathogenesis_Deep": "Algor mortis is the post-mortem cooling of the body. Once metabolism stops, the body passively loses heat to the environment via radiation and conduction until it reaches ambient temperature. The body surface cools rapidly (within 3-4 hours), while the internal core (rectal) temperature cools at a predictable rate of approximately 1.5°F per hour. This gradient is highly useful for forensic veterinarians estimating the Time Since Death (TSD).",
        "Why_Not": "Cooling within 1-2 hours only occurs in very small animals or freezing environments. Taking 8-12 hours for the *surface* to cool is excessively long; the core takes that long, but the skin is much faster.",
        "Wow_Approach": "To accurately estimate TSD in a suspected poisoning or poaching case, you must measure the rectal temperature, the ambient environmental temperature, and visually assess the animal's fat cover and fleece/hair density, as these heavily insulate the core."
    },
    1637: {
        "topic": "Meat Adulteration - Feline Substitution",
        "Core_Anatomy": "Skeletal muscle and osteology (vertebrae).",
        "Pathogenesis_Immediate": "Rabbit meat is classically known to be fraudulently adulterated with (or substituted by) the meat of a Cat.",
        "Pathogenesis_Deep": "The skinned carcass of a rabbit and a cat are remarkably similar in size, weight, and gross muscle appearance, making fraudulent substitution a common forensic issue in some markets. They are differentiated osteologically: (1) In the rabbit, the radius and ulna are completely fused; in the cat, they are separate. (2) The rabbit's lumbar vertebrae have massive, forward-pointing transverse processes; the cat's are shorter and point horizontally.",
        "Why_Not": "Lamb or goat carcasses are much larger and possess distinct ruminant fat profiles and bone structures. The cat is the exact anatomical doppelganger of the rabbit.",
        "Wow_Approach": "If you are presented with a skinned, headless carcass suspected of being a cat, look at the kidneys: a cat's kidneys are situated symmetrically opposite each other, whereas a rabbit's right kidney is situated significantly further forward (cranial) than the left."
    },
    1638: {
        "topic": "Veterinary Jurisprudence - IPC Section 272 (Adulteration)",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The adulteration of meat, milk, and meat products intended for human consumption is punishable under Section 272 of the Indian Penal Code (IPC).",
        "Pathogenesis_Deep": "IPC Section 272 deals specifically with the 'Adulteration of food or drink intended for sale'. If a butcher substitutes cat meat for rabbit, or a dairyman adds urea/detergent to milk, they are committing a criminal offense under this section. The forensic veterinarian is frequently called as an expert witness to provide the biological evidence (e.g., DNA, bone morphology, biochemical assays) that proves the adulteration occurred.",
        "Why_Not": "Section 428/429 deals with mischief (killing animals). Section 377 deals with unnatural offenses (bestiality). Section 272 is strictly for food adulteration.",
        "Wow_Approach": "Always seal and sign the sample containers collected for adulteration testing immediately in front of the police investigating officer to maintain the legal 'Chain of Custody'."
    },
    1639: {
        "topic": "Forensic Toxicology - Organophosphorus Poisoning",
        "Core_Anatomy": "Stomach (gastric contents) and systemic blood.",
        "Pathogenesis_Immediate": "In suspected organophosphorus (OP) poisoning cases, the Stomach Contents (and liver/kidney) are the primary samples analyzed.",
        "Pathogenesis_Deep": "Organophosphates (like Malathion or Parathion) are highly toxic agricultural pesticides. Malicious poisoning (e.g., lacing a piece of meat to kill stray dogs or wildlife) almost always occurs via ingestion. Therefore, the stomach contents provide the highest concentration of the unabsorbed parent compound. The toxicologist will also request whole blood to measure acetylcholinesterase (AChE) inhibition, which confirms the physiological mechanism of death.",
        "Why_Not": "Analyzing the lungs or brain is useless for detecting ingested OP compounds, as they do not concentrate the parent toxin.",
        "Wow_Approach": "OP compounds have a very distinct, pungent 'garlic' or 'petroleum' odor. Opening the stomach of a poisoned dog during necropsy will often instantly release this diagnostic smell."
    },
    1640: {
        "topic": "Veterinary Jurisprudence - IPC Section 429 (Mischief)",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "Killing, poisoning, or maiming an animal of value (like cattle or horses) is punishable under IPC Section 429.",
        "Pathogenesis_Deep": "Sections 428 and 429 of the IPC classify the intentional harming of animals as 'Mischief'. Section 428 applies to animals valued at ten rupees or more, while Section 429 applies specifically to major agricultural animals (elephants, camels, horses, mules, buffaloes, bulls, cows, or oxen) regardless of their value, or any other animal valued over fifty rupees. The crime is focused on the destruction of property and economic value.",
        "Why_Not": "Section 420 deals with cheating/fraud. Section 269 deals with spreading infectious diseases. Sections 428/429 are the specific 'Mischief' statutes for animals.",
        "Wow_Approach": "A post-mortem report for a Section 429 case must conclusively prove that the death was unnatural (e.g., a bullet trajectory or specific plant toxin) and not from natural disease, or the criminal case will be dismissed."
    },
    1641: {
        "topic": "Forensic Terminology - Maiming",
        "Core_Anatomy": "Limbs, eyes, or reproductive organs.",
        "Pathogenesis_Immediate": "Making an animal permanently useless by the use of violence (without actually killing it) is legally defined as Maiming.",
        "Pathogenesis_Deep": "Maiming involves the permanent privation of the use of a limb or organ, drastically reducing the animal's economic utility. Examples include maliciously blinding a racehorse, slashing the digital flexor tendons (hamstringing) of a draft bull, or amputating the udder of a dairy cow. In law, maiming is treated with the same severity as killing under IPC Section 429.",
        "Why_Not": "Spoiling or injuring are general terms. Poisoning involves toxins. Maiming specifically implies permanent physical disfigurement and loss of function.",
        "Wow_Approach": "In a maiming case, the veterinary certificate must explicitly state that the injury is permanent and the animal can no longer perform its intended agricultural function."
    },
    1642: {
        "topic": "Courtroom Ethics - Perjury",
        "Core_Anatomy": "N/A - Legal Procedure.",
        "Pathogenesis_Immediate": "The willful utterance of falsehood (lying) by an expert witness under oath in a court of law is called Perjury.",
        "Pathogenesis_Deep": "When a veterinarian takes the stand as an expert witness, they swear an oath to tell the truth. If they intentionally provide false testimony (e.g., claiming a cow died of natural causes when they know it was poisoned, perhaps due to bribery), they commit perjury (IPC Section 193). This is a serious criminal offense that destroys the veterinarian's credibility and can lead to imprisonment and the revocation of their veterinary license.",
        "Why_Not": "Cheating involves financial fraud. A witness is the person testifying. A summon is the legal order to appear in court.",
        "Wow_Approach": "If you are unsure of an answer during cross-examination, simply say 'I do not know' or 'The medical evidence is inconclusive.' Guessing or lying to sound competent can inadvertently lead to a perjury charge."
    },
    1643: {
        "topic": "Courtroom Ethics - Refusal of Oath (IPC 178)",
        "Core_Anatomy": "N/A - Legal Procedure.",
        "Pathogenesis_Immediate": "The refusal of a witness to take an oath or make an affirmation when legally bound to do so by a public servant is punishable under the IPC (specifically Section 178, though often grouped with Section 193 regarding false evidence).",
        "Pathogenesis_Deep": "A veterinarian cannot refuse to testify or refuse to take the oath if subpoenaed (summoned) by a court for a case they handled. Refusing the oath obstructs the judicial process.",
        "Why_Not": "Section 377 is bestiality. Section 428/429 is mischief. Section 193 is perjury (giving false evidence).",
        "Wow_Approach": "Veterinarians often try to avoid court appearances because they are time-consuming. However, ignoring a court summons or refusing the oath is a punishable contempt of court."
    },
    1644: {
        "topic": "Forensic Identification - Alteration of Stolen Animals",
        "Core_Anatomy": "Integument (hair coat, tail, horns).",
        "Pathogenesis_Immediate": "A stolen animal's physical description may be fraudulently altered by thieves using methods like Painting, Clipping, or Docking.",
        "Pathogenesis_Deep": "Thieves frequently alter the appearance of stolen livestock to evade detection before selling them at a different market. (1) Painting/Dyeing: used to cover up distinct white markings or change a coat color. (2) Clipping: shearing the hair to remove identifying brands or freeze-marks. (3) Docking/Cropping: amputating the tail or ears to change the silhouette or remove ear tags.",
        "Why_Not": "Starvation alters body condition but not the specific identifying marks. Alteration requires active, deceptive physical modification.",
        "Wow_Approach": "If you suspect a horse has been dyed, rub a swab soaked in alcohol or acetone vigorously over the coat. Artificial dyes will immediately transfer to the swab, whereas natural melanin pigment will not."
    },
    1645: {
        "topic": "Veterinary Jurisprudence - IPC Section 377 (Bestiality)",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "Bestiality (unnatural sexual offenses involving animals) is a criminal offense governed and punished under IPC Section 377.",
        "Pathogenesis_Deep": "Section 377 of the Indian Penal Code criminalizes 'carnal intercourse against the order of nature with any man, woman or animal'. When a human sexually abuses an animal, the forensic veterinarian is required to perform a meticulous physical examination of the animal's reproductive and anal tracts. They must collect vaginal/rectal swabs for human semen analysis and document any mucosal lacerations, bruising, or trauma.",
        "Why_Not": "Section 420 is fraud. Section 172 is absconding to avoid a summons. Section 377 is the specific statute used to prosecute the sexual abuse of animals.",
        "Wow_Approach": "In these highly sensitive cases, the veterinarian must collect DNA swabs (using sterile saline, not water, to preserve sperm cells) and immediately seal them in paper envelopes (never plastic, which promotes bacterial degradation of DNA)."
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
