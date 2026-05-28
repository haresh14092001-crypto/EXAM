import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    783: {
        "topic": "Canine Vaginal Cytology - Proestrus Cell Profile",
        "Core_Anatomy": "Vaginal mucosal epithelium, stratified squamous layers, and systemic estrogen.",
        "Pathogenesis_Immediate": "During proestrus in the bitch, the majority of vaginal epithelial cells are Intermediate and Superficial cells, accompanied by abundant red blood cells (RBCs) and variable neutrophils.",
        "Pathogenesis_Deep": "As proestrus progresses under the influence of rising estrogen from developing follicles, the vaginal mucosa thickens from a few layers of cuboidal cells to multiple layers of stratified squamous cells. Cells located furthest from the blood supply (superficial layers) begin to die and cornify: (1) Early proestrus: Parabasal and small intermediate cells dominate. (2) Mid-to-late proestrus: Large intermediate and superficial (cornified with pyknotic nuclei) cells dominate, representing estrogen-driven epithelial maturation. RBCs diapedese across capillary walls, causing the characteristic bloody discharge.",
        "Why_Not": "Superficial anuclear (fully cornified) cells dominate oestrus (>90% of cells), not proestrus. Parabasal cells dominate anestrus. Intermediate cells are the transition phase characteristic of proestrus.",
        "Wow_Approach": "To identify the transition from proestrus to oestrus: look for a shift where intermediate cells decrease and fully angular, anuclear superficial cells exceed 80-90%, while RBCs and background debris decline, creating a highly 'clean' slide."
    },
    784: {
        "topic": "Corpus Luteum - The Yellow Body",
        "Core_Anatomy": "Ovarian cortex, ruptured follicle, and luteal tissue.",
        "Pathogenesis_Immediate": "The Corpus Luteum is otherwise known as the 'yellow body' (due to high concentrations of the carotenoid pigment lutein in cattle, sheep, and humans).",
        "Pathogenesis_Deep": "Following ovulation, the collapsed Graafian follicle fills with blood, forming a temporary Corpus Haemorrhagicum (red body). Under LH influence, the theca and granulosa cells proliferate and luteinize, accumulating lipids and lutein pigment to form the Corpus Luteum (yellow body). If pregnancy does not occur, the CL regresses (luteolysis) into a white, fibrous scar called the Corpus Albicans (white body). The pigment gives the luteal tissue its characteristic yellow appearance on gross pathology.",
        "Why_Not": "The follicle is translucent and fluid-filled, not pigmented. The placenta is a complex vascular organ, not localized to the ovary. The zygote is a single-celled embryo.",
        "Wow_Approach": "The yellow coloration is highly species-specific: bovine and human CLs are bright yellow-orange due to dietary carotenoids, whereas porcine (sow) and canine (bitch) CLs are pale pink or cream-colored due to lower carotenoid accumulation."
    },
    785: {
        "topic": "Progesterone Profiling - Ovulation and AI Timing in Bitches",
        "Core_Anatomy": "Preovulatory follicles, granulosa cells, and the canine systemic blood compartment.",
        "Pathogenesis_Immediate": "Serial progesterone estimation in the bitch is primarily used to detect the exact time of Ovulation and plan breeding or artificial insemination.",
        "Pathogenesis_Deep": "Unlike other species, canine follicles undergo preovulatory luteinization under the influence of the LH surge, producing rising progesterone before follicle rupture. Progesterone levels reflect this timeline: (1) Proestrus baseline: <1 ng/ml. (2) LH surge: 1.5-2.0 ng/ml. (3) Ovulation: 4-10 ng/ml (or 2-4 ng/ml depending on assay). Because canine oocytes are ovulated as primary oocytes and require 48 hours to mature, monitoring the progesterone curve allows the clinician to schedule mating when fertilizable secondary oocytes are present.",
        "Why_Not": "Progesterone remains low throughout proestrus, making it useless for identifying the start of proestrus. It remains elevated throughout diestrus regardless of pregnancy status, so it cannot be used as a pregnancy test in bitches.",
        "Wow_Approach": "Schedule breeding based on progesterone: when P4 reaches 5 ng/ml (ovulation day), breed the bitch on Days 2 and 4 post-ovulation if using fresh/chilled semen, or on Day 3 if using frozen semen (which has a shorter lifespan)."
    },
    786: {
        "topic": "Ovarian Palpation - Mid-Cycle Heat Ovarian Structures",
        "Core_Anatomy": "Ovarian cortex, active corpus luteum, and developing antral follicles.",
        "Pathogenesis_Immediate": "The palpable ovarian structures during a mid-cycle heat (a physiological anomaly or sub-oestrus phase in dairy cows) are a mature, functional Corpus Luteum (CL) and a developing dominant follicle.",
        "Pathogenesis_Deep": "Mid-cycle heat can occur around Day 9-11 of the 21-day cycle, driven by peak estradiol from the dominant follicle of the first follicular wave. Although the cow may show mild signs of estrus, rectal palpation reveals a fully mature, large, firm CL (from the previous ovulation) on one ovary and a fluctuant dominant follicle (>10 mm) on the other. Systemic progesterone remains high, which blocks the preovulatory LH surge, preventing true ovulation. This 'false heat' does not culminate in cycle reset.",
        "Why_Not": "During true standing oestrus (Day 0), the CL is regressed (corpus albicans, small and hard) and progesterone is baseline (<0.5 ng/ml). Finding a mature CL confirms that the cow is in mid-cycle dioestrus, not true estrus.",
        "Wow_Approach": "Never breed a cow showing mid-cycle heat. Doing so will result in zero conception due to high progesterone blocking ovulation. Confirm the presence of the active CL by palpation or ultrasound and wait for natural luteolysis on Day 17."
    },
    787: {
        "topic": "Oxytocin Synthesis - Hypothalamic Nuclei and Pituitary Release",
        "Core_Anatomy": "Hypothalamus (paraventricular and supraoptic nuclei), pituitary stalk, and posterior pituitary (neurohypophysis).",
        "Pathogenesis_Immediate": "Oxytocin is synthesized in the cell bodies of the paraventricular (PVN) and supraoptic (SON) nuclei of the Hypothalamus and stored in the posterior pituitary gland.",
        "Pathogenesis_Deep": "Oxytocin is a nonapeptide hormone. Its synthesis occurs within magnocellular neurons in the PVN and SON of the hypothalamus. The hormone is packaged into neurosecretory vesicles along with its carrier protein, neurophysin I. These vesicles are transported down the long axons of the hypothalamo-neurohypophyseal tract through the pituitary stalk and stored in axon terminals in the posterior pituitary. Electrical stimulation triggers exocytosis of oxytocin into the capillary bed for systemic circulation.",
        "Why_Not": "The posterior pituitary is strictly a storage and release site, not a synthesis site. Small luteal cells synthesize progesterone, not oxytocin. The uterus expresses oxytocin receptors and secretes PGF2alpha, not oxytocin.",
        "Wow_Approach": "In addition to hypothalamic synthesis, local synthesis of oxytocin has been discovered in the bovine corpus luteum (specifically by large luteal cells) during the mid-luteal phase. This ovarian oxytocin plays a localized role in triggering luteolysis by stimulating endometrial PGF2alpha release."
    },
    788: {
        "topic": "Pseudopregnancy - High Prevalence in Bitches, Does, and Rabbits",
        "Core_Anatomy": "Hypothalamus, pituitary lactotrophs, persistent CL, and mammary glands.",
        "Pathogenesis_Immediate": "Pseudopregnancy (false pregnancy) is a common clinical condition seen in the Bitch, Doe (goat), and Rabbit (making 'All of the above' the correct answer).",
        "Pathogenesis_Deep": "The pathophysiology of pseudopregnancy varies: (1) In bitches, it is a normal physiological extension of the long luteal phase (diestrus), where declining progesterone and rising prolactin trigger lactation. (2) In does (goats), it is characterized by hydrometra ('cloudburst' or accumulation of sterile fluid in the uterus) maintained by a persistent CL. (3) In rabbits (induced ovulators), a sterile mating triggers the LH surge and ovulation, leading to a pseudopregnant state (lasting 16-18 days, half of normal gestation) with nesting behavior and mammary growth.",
        "Why_Not": "While the clinical manifestations differ (lactation in bitches, hydrometra in goats, nesting in rabbits), all three species are highly susceptible to clinical pseudopregnancy, making it a key comparative medicine topic.",
        "Wow_Approach": "To treat hydrometra (pseudopregnancy) in goats: administer two injections of PGF2alpha (e.g., Cloprostenol) 12 days apart. This regresses the persistent CL, causing a rapid discharge of the accumulated uterine fluid ('cloudburst') and restoring fertility."
    },
    789: {
        "topic": "Morula Stage - 16-32 Cell Embryonic Development",
        "Core_Anatomy": "Preimplantation embryo, blastomeres, and the zona pellucida.",
        "Pathogenesis_Immediate": "A pre-implantation embryo consisting of a solid mass of 16 to 32 cells (blastomeres) is defined anatomically as a Morula.",
        "Pathogenesis_Deep": "Following fertilization at the ampulla, the zygote undergoes rapid mitotic divisions (cleavage) without increasing in overall mass: (1) Cleavage stages: 2-cell, 4-cell, 8-cell. (2) Morula (Day 4-5 in cows): when the embryo reaches 16-32 cells, the blastomeres undergo 'compaction' — forming tight junctions between outer cells and gap junctions between inner cells. This seals the embryo, allowing the accumulation of fluid to form the blastocoel cavity, which marks the transition to the blastocyst stage (Day 7).",
        "Why_Not": "A blastocyst is characterized by the presence of a fluid-filled cavity (blastocoel) and cellular differentiation into the inner cell mass and trophoblast. A zygote is a single-celled fertilized egg. A trophoblast is the outer cell layer of the blastocyst.",
        "Wow_Approach": "Compaction is the crucial biological milestone of the morula stage. Without normal compaction, the embryo cannot pump sodium ions inward to create the osmotic gradient required for blastocoel fluid accumulation and blastocyst formation."
    },
    790: {
        "topic": "Brucellosis - High-Yield Infectious Abortion in Cattle",
        "Core_Anatomy": "Placentomes, fetal cotyledons, uterine caruncles, and the chorioallantoic membrane.",
        "Pathogenesis_Immediate": "Brucella abortus (Brucellosis) is the primary bacterial pathogen responsible for late-term abortion (7-9 months of gestation) in cattle, characterized by severe necrotizing placentitis.",
        "Pathogenesis_Deep": "Brucella abortus is an intracellular, Gram-negative bacterium with a tropism for the pregnant uterus due to high concentrations of erythritol (a sugar alcohol that stimulates Brucella growth) in the placenta. The bacteria invade the trophoblast cells, causing necrotizing placentitis. The chorioallantoic membrane becomes thickened, opaque, and yellow-brown ('leathery placenta'). The fetus dies due to vascular compromise, and abortion occurs in the third trimester. It is a major zoonotic pathogen causing undulant fever in humans.",
        "Why_Not": "Trichomoniasis and Vibriosis are venereal diseases that cause early embryonic death or first-trimester abortions (under 3-4 months). Tuberculosis rarely causes abortion and is primarily a chronic granulomatous respiratory disease.",
        "Wow_Approach": "Confirm Brucellosis: perform the Rose Bengal Plate Test (RBPT) or ELISA on maternal serum, or perform a modified Ziehl-Neelsen (Stamp's) stain on a smear of the aborted abomasal content or placental cotyledon to identify the red-staining coccobacilli."
    },
    792: {
        "topic": "Dicumarol Poisoning - Sweet Clover Induced Fetal Hemorrhage",
        "Core_Anatomy": "Fetal vascular compartment, coagulation factors, and the placenta.",
        "Pathogenesis_Immediate": "Dicumarol poisoning (caused by feeding moldy sweet clover) is a major toxic cause of fetal death and abortion in cattle, resulting from severe fetal hemorrhage due to interference with Vitamin K synthesis.",
        "Pathogenesis_Deep": "Sweet clover (Melilotus spp.) contains coumarin. When sweet clover becomes moldy (due to Penicillium or Aspergillus contamination), coumarin is converted into Dicumarol, a potent vitamin K antagonist. Dicumarol crosses the placenta easily. It inhibits the enzyme vitamin K epoxide reductase in both dam and fetus, blocking the synthesis of active coagulation factors II, VII, IX, and X. The fetus, having a more fragile vascular system, develops widespread internal hemorrhages, dies in utero, and is aborted.",
        "Why_Not": "Nitrate poisoning causes fetal hypoxia due to methaemoglobinaemia, presenting with chocolate-brown fetal blood, but does not directly block coagulation factors. Arsenic causes acute gastrointestinal necrosis. Oxalates cause renal tubular crystallization.",
        "Wow_Approach": "Moldy sweet clover hay must be discarded immediately. Treatment of affected animals: administer Vitamin K1 (phytonadione) at 1-2 mg/kg SQ or IV and perform blood transfusions in severely anemic dams to restore clotting factors."
    },
    793: {
        "topic": "Tritrichomonas foetus - Vaginal Epithelial Corrugation",
        "Core_Anatomy": "Vaginal mucosa, stratified squamous epithelium, and the cervix.",
        "Pathogenesis_Immediate": "A characteristic corrugation (folding or wrinkling) of the vaginal and cervical epithelium is a pathognomonic diagnostic lesion seen in Trichomoniasis (Tritrichomonas foetus) infection in heifers and cows.",
        "Pathogenesis_Deep": "Tritrichomonas foetus colonizes the vaginal, cervical, and uterine lumen. The protozoa adhere to the epithelial cells, releasing cytotoxic enzymes and inducing a localized inflammatory response. This causes infiltration of lymphocytes and plasma cells into the submucosa, leading to hyperplasia and the formation of prominent, visible, and palpable folds or 'corrugations' in the vaginal wall. This epithelial change is highly characteristic of chronic venereal trichomoniasis.",
        "Why_Not": "Brucellosis and Vibriosis do not cause significant vaginal epithelial corrugation. Listeriosis causes acute necrotic placentitis and late-term abortions without vaginal mucosal wrinkling.",
        "Wow_Approach": "During vaginoscopic examination of an infected heifer, direct illumination will reveal the vaginal mucosa to be thickened, hyperaemic, and presenting a distinct 'cobblestone' or corrugated appearance, particularly around the external cervical os."
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
print(f"Batch 3/5 DONE: Updated {updated} questions.")
