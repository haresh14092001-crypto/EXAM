import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    724: {
        "topic": "Anatomy of the Oviduct - Infundibulum, Ampulla, and Isthmus",
        "Core_Anatomy": "Infundibulum (with fimbriae), ampulla, ampullary-isthmic junction, and isthmus.",
        "Pathogenesis_Immediate": "The oviduct is anatomically divided into three primary segments: the Infundibulum (funnel-shaped collector with fimbriae), the Ampulla (dilated, highly folded site of fertilization), and the Isthmus (thick-walled muscular segment connecting to the uterus).",
        "Pathogenesis_Deep": "Each region of the oviduct serves a distinct physiological role: (1) The infundibulum captures the ovulated oocyte from the ovarian surface using active, ciliated fimbriae. (2) The ampulla has a wide lumen and highly folded, ciliated mucosa that facilitates sperm capacitation and serves as the physical site where fertilization occurs. (3) The ampullary-isthmic junction acts as a physiological gatekeeper, only allowing fertilized embryos (zygotes) to pass into the isthmus. (4) The isthmus has a narrow lumen and thick circular muscle layer that regulates sperm transport and maintains early embryonic development before passage into the uterus.",
        "Why_Not": "The fimbriae are finger-like projections of the infundibulum, not a separate primary segment of the oviduct. The uterus, while embryologically continuous, is anatomically distinct from the oviduct.",
        "Wow_Approach": "In mares, only fertilized embryos are allowed to pass through the ampullary-isthmic junction into the uterus. Unfertilized oocytes (UFOs) are selectively retained and accumulate in the oviduct for months, forming degenerated structures that can be identified on post-mortem exams."
    },
    725: {
        "topic": "Tritrichomonas foetus - Potato Soup Pus Metritis",
        "Core_Anatomy": "Endometrium, cervical canal, vaginal mucosa, and uterine lumen.",
        "Pathogenesis_Immediate": "A characteristic 'potato soup' consistency of purulent uterine discharge (pus) is a pathognomonic diagnostic indicator of Tritrichomonas foetus (Trichomoniasis) infection in cattle.",
        "Pathogenesis_Deep": "Tritrichomonas foetus is a flagellated protozoan venereal pathogen of cattle. Following coitus with an infected bull, the protozoa colonize the vagina, cervix, and uterus. The infection causes mild vaginitis and progressive endometritis. When pregnancy is established, the protozoa attack the trophoblast, causing embryonic death, abortion (typically in the first trimester), and post-coital pyometra. The resulting uterine exudate is sterile, odorless, fluid-to-creamy, and has a distinct whitish-yellow, granular 'potato soup' appearance.",
        "Why_Not": "Brucellosis typically causes late-term abortion (7-9 months) characterized by a thick, leathery placenta (sclerotic metritis) and chocolate-brown, odorless uterine exudate. IBR-IPV causes pustular vulvovaginitis but not pyometra with potato-soup pus. Dourine is an equine venereal disease caused by Trypanosoma equiperdum.",
        "Wow_Approach": "To confirm Tritrichomonas foetus: collect a sample of the 'potato soup' pus or vaginal mucus and inoculate it into Diamond's media or an InPouch TF test kit. Incubate at 37°C and perform daily microscopic exams to identify the active, rolling, pear-shaped flagellates with three anterior flagella."
    },
    726: {
        "topic": "Rabbit Embryo Mucin Layer - Oviductal Secretion",
        "Core_Anatomy": "Oviductal mucosal epithelium, secretory peg cells, and the zona pellucida of the rabbit embryo.",
        "Pathogenesis_Immediate": "The rabbit (Oryctolagus cuniculus) is unique because a thick, gel-like mucin layer forms around the zona pellucida of the developing embryo during its transport through the oviduct.",
        "Pathogenesis_Deep": "As the fertilized rabbit zygote moves through the oviduct, secretory cells (peg cells) in the oviductal mucosa secrete a specialized, highly glycosylated mucin protein. This mucin deposits in concentric layers around the outer surface of the zona pellucida, forming a protective, elastic coating that can double the diameter of the embryo. This mucin layer is required for normal blastocyst expansion and implantation (nidation) within the rabbit's duplex uterus.",
        "Why_Not": "In mice, rats, cows, and humans, no mucin layer forms around the zona pellucida; the embryo enters the uterus surrounded only by the standard, unmodified glycoprotein zona pellucida. This makes the rabbit embryo highly distinct in reproductive biotechnology.",
        "Wow_Approach": "When performing in-vitro embryo production (IVP) or embryo transfer in rabbits, the culture media must be supplemented with specialized macromolecular substrates to support the formation of the mucin layer, or the zona pellucida must be mechanically protected during micromanipulation."
    },
    727: {
        "topic": "Trypsin Wash Protocol - Removing Zona-Bound Viruses from Embryos",
        "Core_Anatomy": "The zona pellucida glycoprotein matrix (ZP1, ZP2, ZP3) and the embryonic blastomere surface.",
        "Pathogenesis_Immediate": "The standard IETS (International Embryo Transfer Society) protocol to remove or inactivate viruses (such as IBR, BVDV, or Foot-and-Mouth Disease virus) bound to the outer surface of the zona pellucida is a Trypsin wash.",
        "Pathogenesis_Deep": "The zona pellucida is an effective physical barrier that protects the internal blastomeres from viral infection, provided it remains intact. However, viruses can adhere strongly to the outer glycoprotein layers of the zona. Washing the embryo in a 0.25% trypsin solution (a proteolytic enzyme) digests the outer, sticky glycoprotein layer of the zona, releasing and inactivating any bound viral particles. This wash must be followed by multiple rinses in PBS containing fetal bovine serum to neutralize the trypsin before transferring or freezing the embryo.",
        "Why_Not": "Antiserums are virus-specific and do not physically strip the virus from the zona matrix. Pronase is too aggressive and would digest the entire zona pellucida, exposing the fragile blastomeres. Trypsin is the standard, internationally validated enzyme for this sanitation procedure.",
        "Wow_Approach": "IETS 10-step wash protocol: The embryo must be washed in 10 separate drops of PBS/trypsin media, transferring only the embryo each time using a micro-pipette. This protocol guarantees that embryos collected from disease-positive donor cows can be safely exported worldwide without transmitting disease."
    },
    728: {
        "topic": "Dominant Follicle Definition - Size Thresholds in Cattle",
        "Core_Anatomy": "Ovarian cortex, Graafian follicle, and the follicular wave cohort.",
        "Pathogenesis_Immediate": "In cattle, a dominant follicle is clinically defined as a healthy, growing antral follicle that reaches a minimum diameter of 8-10 mm (typically 10 mm) and exerts inhibitory control over the growth of subordinate follicles.",
        "Pathogenesis_Deep": "During a follicular wave, a cohort of 3-6 small follicles (2-4 mm) is recruited by a surge in FSH. When the follicles grow to 6-8 mm, one follicle (the future dominant follicle) begins to grow faster and expresses LH receptors on its granulosa cells. It secretes high levels of estradiol and inhibin, which suppress pituitary FSH secretion. The drop in FSH causes the smaller cohort follicles (subordinates, which lack LH receptors) to undergo atresia, while the dominant follicle continues to grow, eventually reaching an ovulatory size of 15-20 mm.",
        "Why_Not": "A 4-5 mm follicle is at the recruitment stage and has not yet achieved deviation or dominance. A >20 mm follicle in cattle is classified as a follicular cyst or pre-ovulatory structure, not the standard newly-selected dominant follicle.",
        "Wow_Approach": "Identify follicular deviation (selection) on B-mode ultrasound: look for the point where the largest follicle (dominant) continues to grow at >1 mm/day while the second-largest (subordinate) stops growing at ~8 mm and begins to shrink. This occurs on Day 3 of the follicular wave."
    },
    729: {
        "topic": "Embryo Flushing Media - Modified PBS and Day 7 Recovery",
        "Core_Anatomy": "Uterine lumen, endometrium, and the Day 7 pre-implantation embryo.",
        "Pathogenesis_Immediate": "The most commonly used medium for non-surgical embryo flushing in cattle is Dulbecco's Modified Phosphate Buffered Saline (Modified PBS), and the optimal day for flushing is Day 7 post-insemination.",
        "Pathogenesis_Deep": "Modified PBS is formulated with glucose, sodium pyruvate, bovine serum albumin (BSA), and antibiotics. It provides an isotonic, buffered environment that maintains embryo viability during the flushing process. Day 7 is chosen because the embryo has entered the uterus from the oviduct but is still free-floating (unattached) and has reached the compact morula or early blastocyst stage, which is the most resilient stage for freezing and transfer.",
        "Why_Not": "TCM-199 and DMEM are complex cell culture media used for in-vitro fertilization and maturation, not for the rapid physical flushing of embryos in the field. Flushing on Day 4 is too early, as the embryo is still in the oviduct and cannot be collected non-surgically.",
        "Wow_Approach": "To ensure maximum embryo recovery, add 0.1% polyvinyl alcohol (PVA) or surfactant to the PBS flushing media. This prevents the embryos from sticking to the plastic lining of the Foley catheters, filter membranes, and searching dishes."
    },
    730: {
        "topic": "Anti-Müllerian Hormone (AMH) - Sertoli Cell Secretion",
        "Core_Anatomy": "Fetal testes, Sertoli cells, and the paramesonephric (Müllerian) duct system.",
        "Pathogenesis_Immediate": "Anti-Müllerian Hormone (AMH), secreted by the fetal Sertoli cells, prevents the development of the Müllerian (paramesonephric) ducts in male embryos, directing sexual differentiation toward the male phenotype.",
        "Pathogenesis_Deep": "Sexual differentiation relies on two fetal hormones: (1) Sertoli cells secrete AMH (a glycoprotein), which causes regression of the paramesonephric (Müllerian) ducts (which would otherwise develop into the oviducts, uterus, and cranial vagina). (2) Leydig cells secrete testosterone, which stimulates the mesonephric (Wolffian) ducts to develop into the epididymis, vas deferens, and seminal vesicles. In female embryos, the absence of AMH allows the Müllerian ducts to develop naturally.",
        "Why_Not": "Leydig cells secrete testosterone and insulin-like 3 (INSL3), not AMH. Giant cells and acinar cells have no role in sex determination. The lack of Sertoli cell AMH is what causes female development.",
        "Wow_Approach": "In veterinary medicine, measuring systemic AMH in adult animals is a highly sensitive diagnostic tool to: (1) Confirm cryptorchidism in dogs and horses (AMH is high in cryptorchids). (2) Diagnose granulosa-theca cell tumors in mares (AMH is highly elevated). (3) Predict the superovulatory response in donor cows."
    },
    731: {
        "topic": "Oocyte Maturation Stage at Ovulation - Metaphase II in Cows",
        "Core_Anatomy": "Graafian follicle, oocyte nucleus (germinal vesicle), and the first polar body.",
        "Pathogenesis_Immediate": "At the time of ovulation in cows, the oocyte is arrested at Metaphase II of the second meiotic division, having successfully extruded the first polar body.",
        "Pathogenesis_Deep": "The oocyte's meiotic journey is characterized by two arrests: (1) Dictyate stage of Prophase I (germinal vesicle stage) from fetal life until the LH surge. (2) The preovulatory LH surge triggers the resumption of meiosis I. The oocyte completes meiotic division I, extrudes the first polar body, and immediately enters meiosis II, arresting at Metaphase II. Ovulation occurs at this Metaphase II stage. Meiosis II is only completed, and the second polar body extruded, upon activation by sperm penetration.",
        "Why_Not": "The canine is the exception: bitches ovulate immature primary oocytes arrested at Prophase I of the first meiotic division. These canine oocytes require 48-72 hours in the oviduct to reach Metaphase II before fertilization can occur. Ruminants and mares ovulate directly at Metaphase II.",
        "Wow_Approach": "Identify Metaphase II oocytes during IVF: locate the tiny, translucent first polar body in the perivitelline space under a high-power microscope. The presence of the polar body confirms that nuclear maturation is complete and the oocyte is ready for fertilization."
    },
    732: {
        "topic": "Follicular Phase of the Oestrous Cycle - Proestrus and Oestrus",
        "Core_Anatomy": "Anterior pituitary gonadotrophs, preovulatory follicles, and the endometrium.",
        "Pathogenesis_Immediate": "The follicular phase of the oestrous cycle comprises Proestrus and Oestrus, during which estrogen secreted by the developing dominant follicle dominates the reproductive tract.",
        "Pathogenesis_Deep": "The oestrous cycle is divided into two major phases based on the dominant ovarian structure: (1) The Follicular Phase (Proestrus and Oestrus), characterized by rapid growth of the dominant follicle, high estrogen secretion, low progesterone due to luteolysis, and active reproductive behavior. (2) The Luteal Phase (Metoestrus and Dioestrus), dominated by the corpus luteum and high progesterone levels. The follicular phase is relatively short, lasting only 4-6 days of the 21-day cycle in cattle.",
        "Why_Not": "The luteal phase comprises Metoestrus and Dioestrus. Estrogen dominates the follicular phase, whereas progesterone dominates the luteal phase. Confusing these phases leads to incorrect timing of hormone treatments.",
        "Wow_Approach": "To synchronize the follicular phase in a herd, administer PGF2alpha (e.g., Cloprostenol). This regresses the CL, rapidly terminating the luteal phase and forcing the animals into the follicular phase (proestrus) within 24-36 hours."
    },
    733: {
        "topic": "Equine Transitional Season - Melatonin Decline and GnRH Activation",
        "Core_Anatomy": "Retinohypothalamic tract, pineal gland, and GnRH neurons in the hypothalamus.",
        "Pathogenesis_Immediate": "In the mare, the transition from the non-breeding (winter anestrus) to the breeding season (spring) is stimulated by a decrease in melatonin secretion, resulting from increasing day length.",
        "Pathogenesis_Deep": "Mares are seasonal long-day breeders. During winter (short days, long nights), the pineal gland secretes high levels of melatonin over a long duration. Melatonin acts as an inhibitory signal in the mare's brain, suppressing GnRH pulse frequency and keeping the mare in anestrus. As spring approaches and day length increases, the duration of nightly melatonin secretion declines. This removes the inhibition on the hypothalamus, stimulating pulsatile GnRH release, which triggers FSH and LH secretion to initiate spring transitional follicular waves.",
        "Why_Not": "Increasing melatonin is the signal that induces seasonal breeding in sheep (short-day breeders). In mares, melatonin must decrease to activate the reproductive axis. Progesterone changes occur post-ovulation, not as the primary photoperiodic trigger.",
        "Wow_Approach": "To advance the equine breeding season to early February: place mares under artificial lighting (16 hours light, 8 hours dark) starting on December 1st. This suppresses pineal melatonin secretion, tricking the mare's brain into initiating the spring transition 60 days early."
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
