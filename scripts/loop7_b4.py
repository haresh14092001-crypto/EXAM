import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    794: {
        "topic": "Canine Corpus Luteum - PGF2alpha Refractoriness",
        "Core_Anatomy": "Canine corpus luteum, FP (prostaglandin) receptors, and systemic circulation.",
        "Pathogenesis_Immediate": "Prostaglandin F2-alpha is least effective as a luteolytic agent in the Bitch during the first 25-30 days of diestrus, as the canine CL is highly refractory to prostaglandin early in the cycle.",
        "Pathogenesis_Deep": "Unlike cattle where PGF2alpha easily induces luteolysis after Day 5 of the cycle, the canine corpus luteum lacks sufficient FP (prostaglandin) receptor expression or functional intracellular coupling pathways during early-to-mid diestrus. Consequently, administering standard doses of PGF2alpha during the first 25 days of diestrus fails to regress the CL or reduce progesterone. Luteolytic sensitivity only develops after Day 25-30, and even then, multiple repeated injections over several days are required to successfully terminate pregnancy in bitches.",
        "Why_Not": "In cows, buffaloes, ewes, and mares, the CL becomes highly sensitive to a single injection of PGF2alpha by Day 5-6 post-ovulation. Only in the bitch is the CL refractory for almost half of the luteal phase, making it the least responsive species.",
        "Wow_Approach": "To induce abortion in the bitch before Day 30 post-mating: do not rely on PGF2alpha alone. Instead, combine a dopamine agonist (e.g., Cabergoline) with low-dose PGF2alpha. The dopamine agonist suppresses prolactin (which supports the early CL), rendering the CL sensitive to luteolysis at lower, safer doses."
    },
    795: {
        "topic": "Equine Behavioral Estrus - Clitoral Winking",
        "Core_Anatomy": "Clitoris, vulvar labia, and the vestibular sphincter.",
        "Pathogenesis_Immediate": "The 'winking of clitoris' (repeated exposure of the clitoral glans by vulvar eversion) is a pathognomonic behavioral sign of standing oestrus in the Mare.",
        "Pathogenesis_Deep": "Under the influence of peak estradiol during oestrus, the mare shows clear receptivity when teased by a stallion. The behavioral signs include: (1) Tail raising and abduction. (2) Squatting and frequent urination (passing pheromone-rich urine). (3) Vulvar eversion or 'winking' of the clitoris, where the sphincter muscle relaxes and the vulvar lips pull back to expose the engorged clitoris. This behavioral display signals the stallion that she is ready for coitus.",
        "Why_Not": "Cows do not ever show clitoral winking (their primary oestrus sign is standing to be mounted by others, or mounting other cows). Bitches show flagging of the tail and vulvar swelling, but not active clitoral eversion.",
        "Wow_Approach": "Examine the clitoral sinuses during breeding soundness exams: these small mucosal invaginations on the dorsal surface of the clitoral glans are key harboring sites for Taylorella equigenitalis, the causative bacterium of Contagious Equine Metritis (CEM). Culture these sinuses before mating."
    },
    796: {
        "topic": "Embryonic Cleavage - Cell Division Without Growth",
        "Core_Anatomy": "Zygote, blastomeres, and the rigid zona pellucida.",
        "Pathogenesis_Immediate": "Embryo division without an increase in overall cytoplasmic mass or cellular growth is defined biologically as Cleavage.",
        "Pathogenesis_Deep": "Following fertilization at the ampulla, the zygote is enclosed within the rigid, inelastic glycoprotein shell of the zona pellucida. During the first 4-5 days, the zygote undergoes rapid, synchronous mitotic divisions. Because the outer zona pellucida cannot expand, each subsequent cell division halves the cytoplasmic volume of the individual blastomeres (e.g., 2-cell, 4-cell, 8-cell, 16-cell). The overall diameter of the embryo remains identical to that of the single-celled oocyte until hatching occurs.",
        "Why_Not": "Nidation is the process of embryo implantation into the uterine endometrium, which occurs much later. Morula is the solid-cell stage resulting from cleavage. Gastrulation involves active cell migration and growth to form germ layers.",
        "Wow_Approach": "Because there is no growth during cleavage, the cells rely entirely on endogenous nutrient stores (lipids, glycogen) and simple energy substrates (lactate, pyruvate) absorbed from the oviductal fluid, making early cleavage embryos highly adaptable to simple in-vitro culture media."
    },
    797: {
        "topic": "Maternal Recognition of Pregnancy in the Sow - Estrogen Redirection",
        "Core_Anatomy": "Porcine blastocyst (trophectoderm), uterine endometrium, and uterine lumen.",
        "Pathogenesis_Immediate": "Both endocrine and exocrine-type maternal recognition of pregnancy (MRP) occurs in the Sow, mediated by embryonic secretion of Estradiol-17beta.",
        "Pathogenesis_Deep": "The pig's MRP mechanism is unique and referred to as 'redirection of PGF2alpha'. In the non-pregnant sow, endometrial cells secrete PGF2alpha in an endocrine fashion (into the bloodstream), which travels to the ovaries and regresses the corpora lutea. Between Days 11 and 12, the elongated porcine blastocysts secrete large amounts of estrogen. Estrogen stimulates a shift in the endometrial cells, causing them to secrete PGF2alpha in an exocrine fashion (directly into the uterine lumen) instead. In the lumen, the PGF2alpha is sequestered and inactivated, protecting the corpora lutea from regression.",
        "Why_Not": "In buffaloes, cows, and ewes, MRP is purely endocrine-mediated via IFN-tau, which suppresses oxytocin receptors. Only in the sow does this endocrine-to-exocrine shift of PGF2alpha transport occur.",
        "Wow_Approach": "To ensure successful MRP in pigs: a minimum of 4 embryos (at least 2 in each uterine horn) must be present on Day 11-12. If fewer embryos are present, the estrogen signal is too weak, and the sow will return to estrus. This is a critical factor in pig embryo transfer programs."
    },
    798: {
        "topic": "Relaxin Assay - Placenta-Derived Canine Pregnancy Diagnosis",
        "Core_Anatomy": "Canine placenta (zonary), uterine compartment, and systemic blood.",
        "Pathogenesis_Immediate": "Relaxin is the only hormone currently used as a reliable, highly specific biomarker for the detection of pregnancy in the Bitch.",
        "Pathogenesis_Deep": "In the bitch, both pregnant and non-pregnant diestrus cycles are dominated by progesterone from the corpora lutea, making progesterone measurements useless for pregnancy diagnosis. However, beginning around Day 20-22 post-ovulation, the developing fetal-placental units (specifically the syncytiotrophoblast of the canine zonary placenta) synthesize and secrete Relaxin. Relaxin levels rise rapidly, peaking around Day 40-45. Measuring serum relaxin (using a commercial ELISA kit, e.g., Witness Relaxin) after Day 28 yields a highly accurate pregnancy diagnosis.",
        "Why_Not": "Progesterone is high in both pregnant and non-pregnant bitches. Estrogen is low during diestrus. Oxytocin is a labor-associated hormone and is not useful for early pregnancy detection.",
        "Wow_Approach": "If a relaxin test is performed on Day 25 and is negative, repeat the test 5-7 days later. If still negative on Day 30, it is 100% diagnostic of a non-pregnant state. If positive, it confirms active placental tissue (but does not guarantee fetal viability; combine with ultrasound to check for heartbeats)."
    },
    808: {
        "topic": "Follicular Dynamics and Synchronization Statements",
        "Core_Anatomy": "Ovarian cortex, Graafian follicle, and the pituitary axis.",
        "Pathogenesis_Immediate": "True/False Statements on cycle manipulation: follicle wave deviation occurs on Day 3 of the wave = TRUE; Buserelin dose for superovulation is 10 mcg = FALSE (FSH is used, Buserelin/GnRH is for ovulation/cyst treatment); CIDR devices can be reused = TRUE.",
        "Pathogenesis_Deep": "Superovulation protocols require sustained gonadotrophic stimulation using pituitary FSH extracts, not GnRH/Buserelin. GnRH can only induce a brief endogenous LH surge and is used to ovulate the follicles at the end of the FSH superovulation protocol. Reusing CIDR devices is a common farm practice: used CIDRs still contain ~60% of their original progesterone, which is sufficient to synchronize estrus in heifers.",
        "Why_Not": "Using GnRH as the primary superovulatory agent is biochemically impossible because it does not have the capacity to maintain elevated, long-acting FSH activity to rescue multiple subordinate follicles from atresia.",
        "Wow_Approach": "When reusing CIDR devices, always sanitize them thoroughly in a cold sterilant (chlorhexidine) to prevent vaginal infections (vaginitis). Reused CIDRs should only be used in heifers, as high-producing dairy cows require the maximum progesterone release of a new device."
    },
    810: {
        "topic": "Relaxin - Hormonal Role in Parturition and Pelvic Relaxation",
        "Core_Anatomy": "Pubic symphysis, pelvic ligaments, cervical connective tissue, and the birth canal.",
        "Pathogenesis_Immediate": "Relaxin is a peptide hormone responsible for the relaxation and widening of the pubic symphysis and pelvic ligaments, and the softening (ripening) of the cervix to facilitate parturition.",
        "Pathogenesis_Deep": "Relaxin is synthesized by the corpora lutea (in cows, sows) or the placenta (in mares, bitches). During late gestation, as progesterone falls, a surge in relaxin occurs. Relaxin binds receptors on connective tissue, activating matrix metalloproteinases (collagenases) that break down collagen bundles in the pelvic ligaments and pubic symphysis. This dramatically increases the elasticity of the birth canal, allowing the large fetus to pass through the pelvic inlet without causing pelvic fractures.",
        "Why_Not": "Oxytocin stimulates active smooth muscle contractions (myometrium), but does not relax the pelvic ligaments. Prostaglandins assist in cervical ripening but their primary mechanical role is luteolysis and myometrial activation.",
        "Wow_Approach": "In the mare, a rapid drop in systemic relaxin occurs immediately post-partum. If the placenta is retained (RFM), relaxin levels remain abnormally elevated. Monitoring relaxin post-foaling is a potential indicator of complete placental membrane passage."
    },
    811: {
        "topic": "Riding Test - Estrus Detection in Sows",
        "Core_Anatomy": "Porcine central nervous system, lordosis reflex, and lordosis muscle group.",
        "Pathogenesis_Immediate": "The 'riding test' (or back-pressure test) is the standard behavioral diagnostic test used for estrus detection in Sows, triggering the characteristic 'lordosis' (standing) reflex.",
        "Pathogenesis_Deep": "When a sow or gilt is in standing oestrus (estrus phase), high estradiol primes the central nervous system. When the handler applies firm downward pressure with both hands on the sow's loin/back (simulating the weight of a mounting boar), the sow exhibits the lordosis reflex: she stands completely rigid, arches her back downward, stiffens her legs, and cocks her ears backward. If she shows this standing reflex, she is ready for artificial insemination or natural service.",
        "Why_Not": "Cows exhibit standing to be mounted by other cows, but do not show the lordosis reflex in response to manual back pressure from a handler. Mares are detected by teasing with a stallion, not by back pressure.",
        "Wow_Approach": "To increase the sensitivity of the riding test: perform the test in the presence of a mature boar ('boar effect'). The boar's salivary pheromones (5-alpha-androstenone) act synergistically with the handler's manual pressure, increasing the estrus detection rate to >95% in gilts."
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
