import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1183: {
        "topic": "Artificial Vagina - Thermal and Mechanical Stimulation (Repeated)",
        "Core_Anatomy": "Bovine, equine, or porcine external genitalia and the pelvic urethra.",
        "Pathogenesis_Immediate": "The Artificial Vagina (AV) is the standard device used for semen collection, designed to mimic the natural vagina by providing the optimal combination of temperature and pressure stimulation.",
        "Pathogenesis_Deep": "Semen collection using an AV requires careful calibration: temperature must be maintained at 42-45°C for bulls, 45-48°C for stallions, and 38-40°C for boars. Mechanical pressure is achieved by blowing air into the double-walled jacket, triggering the spinal ejaculation reflex.",
        "Why_Not": "Electroejaculation uses electrical stimulation of the pelvic sympathetic and parasympathetic nerves, bypasses the need for libido, and is used when bulls are injured. The AV requires a mount partner or dummy.",
        "Wow_Approach": "To ensure maximum semen quality and volume: perform 'active preparation' (two false mounts + 1 minute restraint), which triggers oxytocin release and increases sperm concentration by 40%."
    },
    1185: {
        "topic": "Prostatitis - Leukocytospermia in Canine Prostatic Disease (Repeated)",
        "Core_Anatomy": "Canine prostate gland and semen.",
        "Pathogenesis_Immediate": "Prostatitis (inflammation of the prostate gland) is characterized clinically by the presence of abundant white blood cells (Leucocytes) in the semen.",
        "Pathogenesis_Deep": "Bacterial colonization of hyperplastic prostatic tissue (BPH) leads to a breakdown of the blood-prostate barrier and infiltration of neutrophils into the prostatic fluid, causing pain during ejaculation, hematuria, and infertility.",
        "Why_Not": "Detached heads indicate a maturational or handling defect. Distal droplets indicate epididymal transit issues. Prostatitis is strictly an inflammatory infectious process presenting with white cells.",
        "Wow_Approach": "To diagnose canine prostatitis: collect the third fraction of the ejaculate (prostatic fraction) or perform a prostatic massage with fine-needle aspiration. Culturing the third fraction has a high diagnostic correlation."
    },
    1186: {
        "topic": "Semen Extenders - Preventing Sperm Agglutination (Repeated)",
        "Core_Anatomy": "Sperm membrane glycoproteins and extender buffers.",
        "Pathogenesis_Immediate": "Semen extenders are formulated to dilute and preserve semen, containing specific proteins (like albumin) that prevent the head-to-head or tail-to-tail agglutination of spermatozoa.",
        "Pathogenesis_Deep": "Sperm agglutination occurs due to changes in membrane surface charges or enzyme release. Extenders buffer the medium and coat the sperm membrane, maintaining the negative membrane charge that keeps cells repelled from one another.",
        "Why_Not": "Cryoprotectants (like glycerol) protect cells from freezing damage but do not prevent active room-temperature agglutination. Semen extenders serve primarily to preserve individual, free-swimming viability.",
        "Wow_Approach": "If head-to-head agglutination is observed under the microscope: check the pH and osmolarity of the extender. A drop in pH (<6.5) will neutralize surface charges, causing rapid clumping."
    },
    1187: {
        "topic": "Distal Cytoplasmic Droplet - Maturational Semen Defect (Repeated)",
        "Core_Anatomy": "Sperm midpiece and cytoplasmic droplet.",
        "Pathogenesis_Immediate": "The distal cytoplasmic droplet is a normal morphological structure of maturing sperm that is shed in the epididymis; its persistence in ejaculated semen is a maturational secondary defect.",
        "Pathogenesis_Deep": "Sperm transit through the epididymis moves the cytoplasmic droplet distally along the midpiece (distal droplet) where it is normally shed in the cauda. Persistence of distal droplets on >15-20% of sperm indicates immature semen (overuse of the stud) or epididymal dysfunction.",
        "Why_Not": "Proximal cytoplasmic droplets (located at the neck) represent a more severe testicular maturational defect and are classified as primary abnormalities. Distal droplets represent a milder, epididymal transit issue.",
        "Wow_Approach": "To correct high distal droplet percentages in a young stud bull: provide a 2-week sexual rest period. This allows cauda epididymal stores to replenish, leading to normal cytoplasmic shedding."
    },
    1188: {
        "topic": "Benign Prostatic Hyperplasia - Dihydrotestosterone in Dogs (Repeated)",
        "Core_Anatomy": "Canine prostate gland and systemic androgen receptors.",
        "Pathogenesis_Immediate": "Benign Prostatic Hyperplasia (BPH) is a spontaneous, age-related condition in intact male dogs, driven by the active androgen Dihydrotestosterone (DHT).",
        "Pathogenesis_Deep": "Testosterone is converted to the more potent Dihydrotestosterone (DHT) by the enzyme 5-alpha-reductase inside the prostatic cells. DHT binds androgen receptors, driving hyperplasia of the glandular epithelium and hypertrophy of the stroma, causing tenesmus and hematuria.",
        "Why_Not": "BPH is not driven by estrogen alone or progesterone. It is strictly a DHT-dependent process. BPH is benign; it is distinct from prostatic adenocarcinoma (which is highly malignant and not hormone-dependent).",
        "Wow_Approach": "Medical management of BPH: administer Finasteride (0.1-0.5 mg/kg orally once daily). Finasteride is a selective 5-alpha-reductase inhibitor that blocks the conversion of testosterone to DHT."
    },
    1191: {
        "topic": "Breeding Vices in Males - Management and Exercise Prevention (Repeated)",
        "Core_Anatomy": "Central nervous system and male neural behavior.",
        "Pathogenesis_Immediate": "The statement 'Proper management and exercise generally prevents development of vices in male animals' is TRUE. Confinement, isolation, and lack of exercise are major etiologies.",
        "Pathogenesis_Deep": "Male breeding vices (e.g., masturbation, mounting failure) are abnormal behaviors arising from boredom, high-energy rations, and sensory isolation. Regular exercise increases endorphins, reduces stress, and burns excess energy, preventing these destructive behavioral patterns.",
        "Why_Not": "Vices are rarely due to primary organic disease. Hormonal treatments are ineffective and often worsen the behavior. Environmental enrichment and exercise are the primary preventive strategies.",
        "Wow_Approach": "In stallions, masturbation can be managed by using a stallion ring, but the most effective treatment remains regular lunging exercise and pasture socialization."
    },
    1194: {
        "topic": "Balling Up - Penile Deviation Vice in Bulls (Repeated)",
        "Core_Anatomy": "Sigmoid flexure, retractor penis muscle, prepuce, and penile shaft.",
        "Pathogenesis_Immediate": "The statement 'Balling up' is one of the vices in males that occurs commonly in boars' is FALSE. 'Balling up' is a pathological defect that occurs in Bulls during attempted service.",
        "Pathogenesis_Deep": "In bulls, 'balling up' occurs when the bull attempts to mount but fails to achieve intromission. As he thrusts, the erect penis bends back inside the loose prepuce, forming a loop. The thrusting force is transmitted into the prepuce, causing severe preputial trauma or hematoma.",
        "Why_Not": "Boars have a corkscrew-type penis tip that locks into the sow's cervix, preventing telescoping or 'balling up'. 'Balling up' is strictly a bovine-specific mechanical failure of intromission.",
        "Wow_Approach": "To prevent 'balling up' in young bulls: provide experienced teaser cows, ensure the breeding pen floor is non-slip, and closely supervise the first 5 matings."
    },
    1199: {
        "topic": "Testicular Histology - Seminiferous Tubule Dominance (Repeated)",
        "Core_Anatomy": "Testicular parenchyma, seminiferous tubules, and Leydig cells.",
        "Pathogenesis_Immediate": "The statement 'About 80% testicular weight is made up of leydig cells' is FALSE. In mature domestic animals, the seminiferous tubules make up 80-90% of the total testicular weight.",
        "Pathogenesis_Deep": "The tubular compartment occupies 80-90% of the total testicular volume and weight. The interstitial compartment (containing Leydig cells) occupies only 10-20%. Leydig cells themselves make up only a small fraction (<5-8%) of the total testicular mass.",
        "Why_Not": "If Leydig cells occupied 80% of the weight, the testis would have an extremely small capacity for sperm production, resulting in severe infertility. The vast majority of the testis must be dedicated to germ cell meiosis.",
        "Wow_Approach": "To diagnose tubular vs. interstitial degeneration in a sterile bull: perform a scrotal ultrasound. A decrease in testicular size with increased hyperechogenic stromal lines indicates tubular atrophy."
    },
    1200: {
        "topic": "Testicular Hypoplasia - Age of Diagnosis in Bulls (Repeated)",
        "Core_Anatomy": "Testicular parenchyma, scrotal skin, and epididymis.",
        "Pathogenesis_Immediate": "The statement 'Testicular hypoplasia can be diagnosed at one year of age in bull' is TRUE. Scrotal circumference and semen analysis at 12 months reliably identify this defect.",
        "Pathogenesis_Deep": "Testicular hypoplasia is a congenital, hereditary failure of the seminiferous tubules to develop. At 12 months (puberty), a bull with testicular hypoplasia will present with abnormally small, firm testes (<28 cm scrotal circumference) and azoospermia. Diagnosis is highly reliable at one year.",
        "Why_Not": "Waiting until 2 years of age is uneconomical and risks breeding heifers to a subfertile bull. Diagnosing before 8 months is premature because normal prepubertal testicular growth is still actively progressing.",
        "Wow_Approach": "Testicular hypoplasia was historically linked to the white heifer disease gene in Swedish Red and White cattle. Affected bulls must be culled immediately, as they will transmit the hypoplasia gene."
    },
    1201: {
        "topic": "Cryptorchidism - Neoplastic Predisposition (Repeated)",
        "Core_Anatomy": "Abdominal cavity, inguinal canal, and retained testes.",
        "Pathogenesis_Immediate": "The statement 'Tumours are more common in cryptorchid males' is TRUE. Retained testes have up to a 13-fold higher risk of developing neoplasia.",
        "Pathogenesis_Deep": "The abdominal or inguinal environment is maintained at core body temperature, which is 2-4°C higher than the scrotum. This chronic elevated temperature suppresses normal spermatogenesis but stimulates the proliferation of Sertoli cells and germ cells, causing a high risk of Sertoli cell tumors or seminomas.",
        "Why_Not": "Normal scrotal testes are protected by thermoregulatory mechanisms, maintaining a cool temperature that suppresses the hyperplastic pathways that lead to tumor formation.",
        "Wow_Approach": "Feminization syndrome in a cryptorchid dog: look for bilateral symmetrical alopecia, hyperpigmentation of the groin, gynecomastia, and attraction of other male dogs, confirming an estrogen-secreting Sertoli cell tumor."
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
