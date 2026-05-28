import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1346: {
        "topic": "Testicular Descent - Fetal Timing in Cattle",
        "Core_Anatomy": "Gubernaculum testis, inguinal canal, and fetal scrotum.",
        "Pathogenesis_Immediate": "The testicular descent into the scrotum occurs by mid-fetal life in Cattle.",
        "Pathogenesis_Deep": "In the bovine fetus, the testes develop near the kidneys. Under the influence of Insulin-like 3 (INSL3) and testosterone, the gubernaculum swells and pulls the testes through the inguinal canal. In bulls, this process is completed completely in utero by the middle of the second trimester (mid-fetal life). Therefore, a bull calf is always born with both testes fully descended.",
        "Why_Not": "In dogs, descent is completed 30-40 days AFTER birth. In horses, descent occurs very late in gestation (often just before or right at birth). Mid-fetal life is specific to cattle and sheep.",
        "Wow_Approach": "If a bull calf is born without palpable testes in the scrotum, it is a true cryptorchid. Unlike puppies or foals, you should not 'wait for them to drop' in a bull calf."
    },
    1347: {
        "topic": "Canine Prostatic Fluid - Zinc Concentration",
        "Core_Anatomy": "Canine prostate gland and seminal plasma.",
        "Pathogenesis_Immediate": "The canine prostate secretion has an exceptionally high concentration of Zinc.",
        "Pathogenesis_Deep": "The dog possesses only the prostate gland, which secretes 100% of the seminal plasma volume. Prostatic fluid in the dog is rich in zinc and prostatic specific esterase (CPSE). Zinc acts as a potent antibacterial agent (prostatic antibacterial factor) protecting the male urogenital tract from ascending urinary infections and maintaining chromatin stability in the ejaculated spermatozoa.",
        "Why_Not": "Magnesium and calcium are present but not uniquely concentrated like zinc. Cadmium is a heavy metal toxin that causes severe testicular necrosis.",
        "Wow_Approach": "In chronic bacterial prostatitis in the dog, the zinc levels in the prostatic fluid drop drastically, removing this innate antibacterial barrier and allowing recurrent UTIs."
    },
    1348: {
        "topic": "The Flehmen Response - Vomeronasal Olfaction",
        "Core_Anatomy": "Vomeronasal organ (Jacobson's organ), incisive papilla, and upper lip.",
        "Pathogenesis_Immediate": "The Flehmen's reaction (curling of the upper lip to inhale pheromones) is classically seen in Bovine and Equine males during courtship.",
        "Pathogenesis_Deep": "When a bull or stallion investigates a female's urine or vulva, he curls his upper lip and inhales deeply. This action temporarily blocks the external nares and creates negative pressure, sucking the fluid/pheromones through the incisive ducts in the hard palate directly into the Vomeronasal Organ (Jacobson's organ). The organ detects non-volatile pheromones (e.g., estrus-specific glycoproteins), sending neural signals to the accessory olfactory bulb and hypothalamus to stimulate GnRH and libido.",
        "Why_Not": "Swine do not exhibit a true Flehmen response; instead, boars champ their jaws to produce frothy saliva. Canine Flehmen is subtle (tongue flicking), not the classic lip curl seen in ungulates.",
        "Wow_Approach": "The absence of the Flehmen response during a BSE libido test in a bull indicates a severe behavioral deficit or lack of central sensory processing, resulting in failure of the test."
    },
    1349: {
        "topic": "Appendix Testis - Embryological Mullerian Remnant",
        "Core_Anatomy": "Cranial pole of the testis and the epididymal head.",
        "Pathogenesis_Immediate": "The appendix testis (hydatid of Morgagni) is an embryological remnant of the Mullerian duct, commonly found attached to the cranial pole of the testis in the Equine (Stallion).",
        "Pathogenesis_Deep": "During male fetal development, Sertoli cells secrete Anti-Mullerian Hormone (AMH) to regress the female Mullerian ducts. Occasionally, the very cranial tip of the Mullerian duct fails to regress completely and forms a small, cystic, vestigial structure called the appendix testis. It is benign but can occasionally undergo torsion, causing acute, severe scrotal pain.",
        "Why_Not": "The Wolffian duct forms the epididymis. The Mullerian duct forms the appendix testis. It is most frequently documented as an incidental finding in stallions and humans, but is rare in bulls and boars.",
        "Wow_Approach": "During equine castration, a cystic appendix testis may be observed attached to the testicle. It should be removed along with the testicle, requiring no special treatment."
    },
    1350: {
        "topic": "Electroejaculation - Best Species Results",
        "Core_Anatomy": "Pelvic sympathetic/parasympathetic nerves and ampullae.",
        "Pathogenesis_Immediate": "The best and most consistent results for semen collection by electro-ejaculation techniques are seen in the Ram and Bull.",
        "Pathogenesis_Deep": "Electroejaculation (EE) uses a rectal probe to stimulate the pelvic plexus (pudendal and hypogastric nerves), bypassing the need for central nervous system libido. It triggers forced contraction of the accessory sex glands and the urethralis muscle. Bulls and rams respond exceptionally well to EE, producing high-quality, freezeable ejaculates.",
        "Why_Not": "The Stallion and Boar respond very poorly to electroejaculation. In stallions, it often yields only seminal plasma (no sperm) and causes severe distress. Boars have massive semen volumes that require prolonged cervical pressure, not electrical shocks.",
        "Wow_Approach": "In the bull, EE requires rhythmic, escalating electrical pulses (e.g., 3 seconds on, 3 seconds off, increasing from 2 to 15 volts) to induce emission followed by ejaculation."
    },
    1351: {
        "topic": "Sperm Viability Staining - Eosin-Nigrosin Logic (Repeated MCQ)",
        "Core_Anatomy": "Sperm plasma membrane and dye exclusion.",
        "Pathogenesis_Immediate": "In Eosin-Nigrosin viability staining, LIVE spermatozoa remain unstained (No colour / white) against a dark background, whereas DEAD spermatozoa take up the Eosin colour (pink/red).",
        "Pathogenesis_Deep": "This is a dye-exclusion test evaluating plasma membrane integrity. A live sperm has an intact, selectively permeable lipid bilayer that excludes the Eosin dye, keeping the cell white/clear. A dead sperm has a compromised membrane with microscopic pores, allowing the Eosin dye to rush in and stain the nucleus pink. Nigrosin is a colloidal background dye that does not penetrate any cells but provides a dark purplish-black contrast.",
        "Why_Not": "If both colors are inside the cell, the test is invalid. Live cells never take up Eosin.",
        "Wow_Approach": "Always count 200 sperm cells on a warm slide. A good quality bull ejaculate must have at least >70% live (unstained) spermatozoa."
    },
    1352: {
        "topic": "Male Reproductive Pathology - Diagnostic Differentials",
        "Core_Anatomy": "Testes, prepuce, and glans penis.",
        "Pathogenesis_Immediate": "Multiple-choice questions often test the ability to differentiate inflammatory versus degenerative male pathologies (e.g., Balanoposthitis vs. Orchitis).",
        "Pathogenesis_Deep": "Definitions are strictly anatomical: (1) Orchitis: inflammation of the testis (often infectious, e.g., Brucella), resulting in heat, pain, and swelling. (2) Balanoposthitis: inflammation of the glans penis (balanitis) and the prepuce (posthitis), commonly caused by BHV-1 in bulls. (3) Testicular degeneration: a non-inflammatory acquired atrophy due to heat or age. (4) Testicular hypoplasia: a congenital underdevelopment.",
        "Why_Not": "Confusing an inflammatory condition (orchitis) with a congenital condition (hypoplasia) will lead to incorrect culling or treatment decisions.",
        "Wow_Approach": "Balanoposthitis in bulls caused by Bovine Herpesvirus-1 (BHV-1) is termed Infectious Pustular Vulvovaginitis (IPV) in females. It presents with painful vesicles on the penis and prevents intromission."
    },
    1353: {
        "topic": "Epididymal Transit Time - Ram and Bull Metrics",
        "Core_Anatomy": "Caput, corpus, and cauda epididymis.",
        "Pathogenesis_Immediate": "The normal physiological transit time for spermatozoa through the epididymis in ruminants (bull/ram) is approximately 9 to 14 days (with options like 9 days or 12 days often being correct depending on the species-specific baseline).",
        "Pathogenesis_Deep": "Sperm transit through the epididymis is not passive; it is driven by rhythmic smooth muscle contractions. During this 9-14 day window, sperm acquire progressive motility and fertilizing capability in the corpus, and are stored in the cauda. Increased ejaculation frequency can shorten this time slightly, but a transit time less than 5 days will yield completely immature sperm with proximal droplets.",
        "Why_Not": "Transit times of 19 days indicate epididymal stasis, which leads to sperm senescence (aging) and poor fertility.",
        "Wow_Approach": "If a stud animal suffers a high fever, the damaged sperm will not appear in the ejaculate until ~10 days later, reflecting this mandatory epididymal transit delay."
    },
    1354: {
        "topic": "Epididymal Transit Constants - MCQ Options",
        "Core_Anatomy": "Epididymal duct smooth muscle.",
        "Pathogenesis_Immediate": "Objective questions test exact physiological constants (e.g., 12 days vs 13.5 days) for sperm transit.",
        "Pathogenesis_Deep": "The precise transit time varies slightly by species: Bulls average 9-14 days. Stallions average 9-11 days. Rams average 12-15 days. Boars average 9-14 days. These metrics are critical for scheduling sexual rest after a systemic illness.",
        "Why_Not": "Ignorance of transit time leads to misdiagnosing the timeline of a testicular insult.",
        "Wow_Approach": "Spermatogenesis takes ~60 days + Epididymal transit takes ~10 days. Total time from spermatogonium to ejaculation is ~70 days."
    },
    1355: {
        "topic": "Prostatitis - Canine Predisposition (Repeated MCQ)",
        "Core_Anatomy": "Canine prostate gland and urethra.",
        "Pathogenesis_Immediate": "Prostatitis (bacterial inflammation of the prostate) is overwhelmingly most common in Dogs.",
        "Pathogenesis_Deep": "Dogs possess only the prostate gland, which completely surrounds the pelvic urethra. Older intact male dogs almost universally develop Benign Prostatic Hyperplasia (BPH). The hyperplastic cysts alter the normal glandular architecture and decrease prostatic antibacterial zinc levels, making the gland highly susceptible to ascending bacterial infections (E. coli, Proteus) from the urethra, leading to acute or chronic prostatitis and prostatic abscessation.",
        "Why_Not": "Bulls and boars primarily suffer from seminal vesiculitis. The prostate is relatively small and rarely infected in ruminants.",
        "Wow_Approach": "Acute prostatitis in the dog causes severe systemic illness (fever, vomiting, stiff gait) and exquisite pain on rectal palpation of the prostate. Never perform vigorous prostatic massage on an acutely infected gland, as it can rupture an abscess and cause fatal peritonitis."
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
