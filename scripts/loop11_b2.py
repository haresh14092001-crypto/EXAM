import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1235: {
        "topic": "Equine Endometrial Cups - eCG Production",
        "Core_Anatomy": "Maternal endometrium and fetal chorionic girdle cells.",
        "Pathogenesis_Immediate": "Endometrial cups are unique, transient placental structures seen exclusively in the Mare.",
        "Pathogenesis_Deep": "Around day 35 of equine gestation, specialized fetal chorionic girdle cells detach, invade the maternal endometrium, and differentiate into endometrial cups. These cups secrete massive amounts of equine Chorionic Gonadotropin (eCG / PMSG). eCG acts on the maternal ovaries to stimulate the formation of secondary (accessory) corpora lutea, providing essential supplemental progesterone to maintain the pregnancy until the placenta fully takes over at day 120. The cups undergo immunological rejection and slough off by day 120-150.",
        "Why_Not": "Swine, cows, and buffalo do not possess endometrial cups; they rely on the primary corpus luteum or a different placental steroidogenic shift for progesterone maintenance.",
        "Wow_Approach": "If a mare loses her fetus after day 35, the endometrial cups will persist and continue secreting eCG, preventing the mare from returning to estrus for several months. This is termed 'pseudopregnancy'."
    },
    1236: {
        "topic": "Gestation Length - Ovine (Ewe)",
        "Core_Anatomy": "Ovine gravid uterus and feto-maternal HPA axis.",
        "Pathogenesis_Immediate": "The normal gestation length in the Ewe is approximately 150 days (typically 145-152 days depending on the breed and litter size).",
        "Pathogenesis_Deep": "Gestation length is genetically determined by the fetal HPA (hypothalamic-pituitary-adrenal) axis. In sheep, the fetus triggers parturition around day 150: fetal stress causes CRH and ACTH release, leading to a surge in fetal cortisol. This cortisol induces placental 17-alpha-hydroxylase, shifting placental steroidogenesis from progesterone to estrogen, which initiates myometrial contractions and cervical dilation.",
        "Why_Not": "114 days (3 months, 3 weeks, 3 days) is the gestation length of a sow. 280-285 days is the gestation length of a cow. 310-340 days is the gestation of a mare.",
        "Wow_Approach": "Because the ewe relies entirely on the placenta for progesterone maintenance during the final third of gestation (after day 50), ovariectomy after day 50 will NOT cause abortion in sheep."
    },
    1237: {
        "topic": "Lochia Coloration - Canine Uterine Discharge",
        "Core_Anatomy": "Canine endometrium and marginal hematomas of the placenta.",
        "Pathogenesis_Immediate": "Uterine lochia (postpartum discharge) that is distinctly greenish-black in color is characteristic of the Bitch.",
        "Pathogenesis_Deep": "The canine placenta is endotheliochorial and zonary. At the margins of this placental zone are specific structures called 'marginal hematomas' (or green borders) that contain a breakdown product of maternal hemoglobin called uteroverdin. When the placenta separates during parturition, uteroverdin is released, giving the normal canine lochia its dark green color.",
        "Why_Not": "In the cow, normal lochia is brownish-red due to caruncular sloughing. In the mare, it is dark brown and very sparse. In the sow, it is reddish-white. The green uteroverdin pigment is unique to dogs and cats.",
        "Wow_Approach": "In a pregnant bitch, if you observe green discharge from the vulva BEFORE any puppies are born, it indicates premature placental separation. This is an absolute obstetrical emergency requiring immediate C-section to save the hypoxic pups."
    },
    1238: {
        "topic": "Uterine Torsion - Bovine and Bubaline Predisposition",
        "Core_Anatomy": "Gravid uterine horn, broad ligament, and maternal abdomen.",
        "Pathogenesis_Immediate": "Torsion of the uterus (twisting of the gravid horn on its longitudinal axis) is extremely common in the Buffalo and Cow.",
        "Pathogenesis_Deep": "Buffaloes and cows are highly predisposed to uterine torsion due to their specific anatomical adaptations: (1) The gravid uterine horn rests completely unattached in the large abdominal cavity, suspended only by the broad ligaments which attach strictly to the lesser curvature (ventral aspect) of the uterus. (2) During the rolling movements of the mother or sudden fetal movements in late gestation, the heavy horn can flip over itself, twisting the cervix and anterior vagina. This traps the fetus and cuts off uterine blood supply.",
        "Why_Not": "In the mare, the broad ligaments attach dorsally, stabilizing the uterus (though torsion can occur, it's rare). In the sow and bitch, the multiple fetuses in bicornuate horns balance the uterus, making torsion extremely rare.",
        "Wow_Approach": "To diagnose uterine torsion in a buffalo: perform a vaginal exam. If the vaginal folds are twisted in a spiral (corkscrew pattern), torsion is confirmed. The twist is corrected by rolling the buffalo (Schaffer's method) in the direction of the torsion."
    },
    1239: {
        "topic": "Snare Placement - Obstetrical Traction Chains",
        "Core_Anatomy": "Fetal forelimb, fetlock joint, pastern joint, and metacarpus.",
        "Pathogenesis_Immediate": "When placing obstetrical chains or snares on a fetal limb for traction, the correct application is a double loop: one loop placed above the fetlock (around the metacarpus) and a half-hitch placed below the fetlock (around the pasterns).",
        "Pathogenesis_Deep": "This two-point placement distributes the massive mechanical pulling force across the long bone (metacarpus) and the distal phalanges. If a single loop is placed only around the pastern or only above the fetlock, the extreme traction force is concentrated on the joint capsule, which will frequently cause a fracture of the limb or severe epiphyseal avulsion.",
        "Why_Not": "Placing a chain around the neck is used only for specific head-guidance (head snare), not primary traction, as it will crush the trachea and break the cervical spine. Snaring above the neck is mechanically ineffective.",
        "Wow_Approach": "Always ensure the chain loops on the ventral aspect of the leg (behind the dewclaws) so that the pull aligns with the natural flexion of the joints, preventing snapping of the long bones."
    },
    1240: {
        "topic": "Obstetrical Terminology - Extension of Extremities",
        "Core_Anatomy": "Fetal appendicular skeleton (limbs) and axial skeleton (neck).",
        "Pathogenesis_Immediate": "The anatomical alignment and extension (or flexion) of the fetal extremities (limbs, head, neck) relative to the body of the fetus is defined as Posture.",
        "Pathogenesis_Deep": "Veterinary obstetrics relies on three specific definitions to describe fetal alignment: (1) Presentation: the relation of the long axis of the fetus to the long axis of the mother (longitudinal vs transverse). (2) Position: the relation of the dorsum of the fetus to the quadrants of the maternal pelvis (e.g., dorso-sacral is normal). (3) Posture: the anatomical disposition of the fetal appendages. 'Extension of extremities' describes a normal posture, whereas 'carpal flexion' describes an abnormal posture.",
        "Why_Not": "Presentation defines the fetal-maternal axis. Position defines fetal back relative to maternal pelvis.",
        "Wow_Approach": "Most dystocias in cattle are due to abnormalities in posture (e.g., carpal flexion or lateral deviation of the head). Correction (mutation) always involves correcting posture first before attempting to extract the calf."
    },
    1241: {
        "topic": "Vertex Presentation - Fetal Head Deviation",
        "Core_Anatomy": "Fetal cranium, cervical vertebrae, and maternal pelvic inlet.",
        "Pathogenesis_Immediate": "A posture where the fetal head is flexed downward such that the top of the head (the vertex or poll) is presented at the pelvic inlet, resting on the sternum, is termed a Vertex presentation.",
        "Pathogenesis_Deep": "Vertex presentation is a specific form of downward deviation of the head. Instead of the muzzle entering the pelvic canal (normal), the fetal neck is flexed ventrally so the chin presses tightly against the sternum. The highest point of the skull (the vertex/poll) jams against the maternal pubis. The forelimbs may be extended into the canal, but the head cannot follow.",
        "Why_Not": "In a nape presentation, the neck is flexed even further down so the back of the neck enters the canal. Transverse presentation means the fetus is lying sideways across the inlet.",
        "Wow_Approach": "To correct a vertex presentation: repel the fetal chest to create space, cup the fetal muzzle with your hand, and lift the head upward and backward in an arc to extend the neck into the pelvic canal."
    },
    1242: {
        "topic": "The Acetabulum - Maternal Pelvic Anatomy",
        "Core_Anatomy": "Maternal bony pelvis: ilium, ischium, and pubis.",
        "Pathogenesis_Immediate": "The acetabulum (the hip socket) is a deep articular cavity formed by the fusion of all three major bones of the pelvis: the Ilium, the Ischium, and the Pubis.",
        "Pathogenesis_Deep": "The maternal pelvic canal is formed by these three bones. The ilium forms the cranial and dorsal roof (shafts). The ischium forms the caudal floor. The pubis forms the cranial floor. All three bones converge and fuse at a central point on the lateral aspect of the pelvis to form the acetabulum, which receives the head of the femur. The size and shape of this bony ring dictate the maximum dimensions of the birth canal (pelvic area).",
        "Why_Not": "The sacrum forms the dorsal roof of the pelvic canal but does not participate in forming the acetabulum.",
        "Wow_Approach": "In young heifers, the symphysis (the junction between the two halves of the pelvis) is not yet fully ossified. During a severe dystocia, massive traction can cause this symphysis to split, leading to catastrophic pelvic fracture and the heifer 'doing the splits'."
    },
    1243: {
        "topic": "Fetal Mummification in Sows - Papyraceous Type",
        "Core_Anatomy": "Fetal tissues, chorioallantoic membrane, and uterine lumen.",
        "Pathogenesis_Immediate": "The type of fetal mummification typically observed in multiparous species like the Sow (and bitch/queen) is the Papyraceous type.",
        "Pathogenesis_Deep": "Mummification occurs when a fetus dies in utero during the middle or last third of gestation WITHOUT bacterial infection. The fetal fluids are absorbed by the maternal uterus, leaving a dry, shriveled, leathery mass of fetal bones and skin wrapped in fetal membranes. Papyraceous mummification ('parchment-like') occurs without hemorrhage. Because the sow is multiparous, if one fetus dies and mummifies, the surviving fetuses maintain the pregnancy, and the mummy is simply expelled at term along with the live piglets.",
        "Why_Not": "Haematic mummification is specific to the cow, where fetal death is accompanied by massive intercaruncular hemorrhage, forming a sticky, chocolate-brown gummy exudate around the mummy.",
        "Wow_Approach": "Porcine Parvovirus (PPV) is the classic infectious cause of SMEDI (Stillbirths, Mummification, Embryonic Death, and Infertility) in swine. Finding varying sizes of papyraceous mummies in a litter confirms the virus swept through the uterus at different stages of gestation."
    },
    1244: {
        "topic": "Parturient Paresis - Milk Fever (Hypocalcemia)",
        "Core_Anatomy": "Neuromuscular junction, systemic blood, and mammary gland.",
        "Pathogenesis_Immediate": "Parturient paresis in dairy cows is most commonly known as Milk Fever, a metabolic disorder caused by acute, severe hypocalcemia at or near the time of calving.",
        "Pathogenesis_Deep": "At the onset of lactation, the dairy cow suddenly drains massive amounts of calcium from her blood to produce colostrum. If her bone mobilization (via PTH and Vitamin D) cannot keep up, systemic blood calcium drops rapidly (<5 mg/dL). Calcium is required for the release of acetylcholine at the neuromuscular junction. Without it, the cow suffers flaccid paralysis (paresis), recumbency (downer cow), and smooth muscle atony (causing dystocia, retained placenta, and bloat).",
        "Why_Not": "Ketosis is a negative energy balance (hypoglycemia) disorder. Downer cow syndrome is a complication of prolonged recumbency (muscle crush injury). Naval ill is a neonatal calf infection. Milk fever is specifically the acute hypocalcemic crisis.",
        "Wow_Approach": "Treatment is immediate, slow intravenous infusion of Calcium Borogluconate. Monitor the heart with a stethoscope during infusion, as rapid calcium administration can cause fatal cardiac arrhythmias (heart block)."
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
