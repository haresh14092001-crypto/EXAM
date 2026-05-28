import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2533: {
        "topic": "Esophagus - Choke",
        "Core_Anatomy": "Oesophageal lumen.",
        "Pathogenesis_Immediate": "The Esophagus is clinically matched to 'Choke' (oesophageal obstruction).",
        "Pathogenesis_Deep": "Choke in large animals (especially horses and cattle) is the acute impaction of a food bolus (like a whole potato, apple, or dry unsoaked beet pulp) or foreign body within the oesophagus. Unlike human choke (which is a tracheal/airway obstruction), veterinary choke does not immediately threaten breathing. However, it completely blocks swallowing. The animal produces copious frothy saliva from the mouth/nostrils and attempts violently to swallow. If unresolved, pressure necrosis of the oesophageal wall leads to fatal rupture and mediastinitis.",
        "Why_Not": "Tracheal obstruction causes asphyxiation. Oesophageal obstruction causes dysphagia and regurgitation. The term 'choke' in veterinary medicine strictly means oesophageal blockage.",
        "Wow_Approach": "In cattle, choke is a true emergency not because they can't swallow, but because they can't ERUCTATE (belch). The blocked oesophagus prevents rumen gas escape, leading to rapidly fatal acute ruminal tympany (bloat) within hours."
    },
    2536: {
        "topic": "Recurrent Bloat - Rumen Fistula",
        "Core_Anatomy": "Rumen dorsal sac and left paralumbar fossa.",
        "Pathogenesis_Immediate": "Recurrent bloat in cattle is surgically managed by creating a temporary Rumen fistula.",
        "Pathogenesis_Deep": "When a cow suffers from chronic, recurrent ruminal tympany (e.g., due to vagal indigestion, chronic pneumonia causing mediastinal lymph node enlargement that compresses the oesophagus, or chronic tetanus), the repeated distension is life-threatening. A surgical rumen fistula (rumenostomy) is created by suturing the rumen wall directly to the skin of the left paralumbar fossa, creating a permanent or semi-permanent stoma. This allows continuous, passive escape of rumen gas, acting as a 'safety valve' while the primary condition is treated.",
        "Why_Not": "Trocarization (using a trocar and cannula) is for ACUTE emergency bloat relief. A fistula is for CHRONIC, recurrent bloat management.",
        "Wow_Approach": "A rumen fistula can be closed easily once the primary disease resolves, but in research settings, permanent rumen fistulas fitted with a plug (cannulated cows) are used to study rumen microbiology and provide healthy rumen fluid for transfaunation to sick cows."
    },
    2539: {
        "topic": "Mammary Neoplasm - Spaying",
        "Core_Anatomy": "Mammary gland and ovaries.",
        "Pathogenesis_Immediate": "Spaying (Ovariohysterectomy) is a critical preventive measure against Mammary Neoplasms in bitches.",
        "Pathogenesis_Deep": "Canine mammary tumors are highly hormone-dependent. The risk of a bitch developing mammary cancer is directly correlated with the number of estrous cycles she goes through before being spayed. Spaying before the first estrus reduces the risk of mammary neoplasia to 0.5%. Spaying after the first estrus increases the risk to 8%. Spaying after the second estrus raises it to 26%. Spaying after 2.5 years of age provides virtually no protective benefit against mammary tumor development.",
        "Why_Not": "Extending a hernia ring is a surgical technique for hernia repair (to allow reduction of incarcerated bowel), completely unrelated to mammary neoplasms.",
        "Wow_Approach": "This is one of the most powerful prophylactic surgical statistics in all of medicine. An elective surgery (spay) performed at 6 months of age almost completely eliminates the risk of the most common cancer in female dogs."
    },
    2544: {
        "topic": "Radical vs Elective Surgery",
        "Core_Anatomy": "Surgical pathology and decision making.",
        "Pathogenesis_Immediate": "Radical surgery involves extensive excision of tissue (usually for cancer cure); Elective surgery is a planned, non-emergency procedure chosen by the owner.",
        "Pathogenesis_Deep": "(1) Radical Surgery: The complete surgical excision of a diseased organ/tumor AND a wide margin of surrounding healthy tissue, plus regional lymph nodes (e.g., radical mastectomy, limb amputation for osteosarcoma). The goal is absolute disease eradication. (2) Elective Surgery: A procedure that is advantageous to the patient but not urgently required to save life (e.g., routine spay/neuter, elective orthopedics). It can be scheduled at the surgeon's and owner's convenience.",
        "Why_Not": "Emergency surgery (e.g., GDV repair, C-section) must be done immediately to save life. Palliative surgery relieves pain/symptoms without aiming for a cure. Radical aims for a cure through aggressive resection.",
        "Wow_Approach": "The classic 'radical' surgery in veterinary oncology is the 'Hemipelvectomy'—amputating the entire hindlimb AND half of the pelvis to achieve clean margins on a pelvic osteosarcoma."
    },
    2551: {
        "topic": "VSR 411 - General Veterinary Surgery Header",
        "Core_Anatomy": "Systemic surgical anatomy.",
        "Pathogenesis_Immediate": "Header denoting the objective section of the General Veterinary Surgery, Anaesthesiology, and Diagnostic Imaging exam.",
        "Pathogenesis_Deep": "This module tests the foundational principles applied to all surgical procedures: wound healing, asepsis, hemostasis, basic pharmacology of anaesthesia, and radiation physics.",
        "Why_Not": "Regional surgery (VSR 421) tests specific organ systems (e.g., ruminal surgery, ocular surgery). General surgery focuses on the shared principles.",
        "Wow_Approach": "Master the wound healing phases: Inflammation (Days 0-3), Proliferation (Days 3-14), and Maturation/Remodeling (Days 14 to months)."
    },
    2558: {
        "topic": "Surgery MCQ Header",
        "Core_Anatomy": "Systemic surgical anatomy.",
        "Pathogenesis_Immediate": "Header for the multiple-choice section of the surgery exam.",
        "Pathogenesis_Deep": "Questions will demand selection of the BEST answer from multiple plausible options. In surgery, the 'best' answer is the one that prioritizes patient safety, asepsis, and physiological stability.",
        "Why_Not": "Be cautious of 'always' or 'never' in surgical MCQs; biological variability often requires adaptable techniques.",
        "Wow_Approach": "For anaesthesia questions, always select the drug protocol that provides cardiovascular stability in compromised patients."
    },
    2560: {
        "topic": "Polyamide (Nylon) - Suture Material",
        "Core_Anatomy": "Dermal and fascial wound closure.",
        "Pathogenesis_Immediate": "Polyamide (Nylon) is a synthetic, non-absorbable suture material commonly used for skin closure.",
        "Pathogenesis_Deep": "Polyamide (Nylon/Ethilon) is a synthetic polyamide polymer. It is non-capillary (does not wick bacteria), inert (causes minimal tissue reaction), and maintains high tensile strength. This makes it the ideal material for skin sutures, where it must remain intact for 10-14 days without harboring surface bacteria. It does not absorb fluid, meaning it will not swell and cut into the skin like natural silk.",
        "Why_Not": "Catgut (natural) and Vicryl (synthetic) are absorbable and used for internal layers. Silk is highly reactive and capillary (wicks bacteria), making it a poor choice for skin despite its excellent handling.",
        "Wow_Approach": "Nylon has significant 'memory'—it tends to return to its original straight shape. Therefore, it requires at least 4-5 secure square throws on the knot to prevent it from spontaneously untying in the restless patient."
    },
    2561: {
        "topic": "Commercial Suture Sterilization - Irradiation",
        "Core_Anatomy": "Surgical asepsis.",
        "Pathogenesis_Immediate": "Commercially manufactured suture materials are primarily sterilized by Gamma Irradiation.",
        "Pathogenesis_Deep": "Most modern synthetic sutures (like Vicryl, PDS, Prolene) are heat-sensitive—autoclaving them (121°C) would melt or denature the polymer, destroying their tensile strength. Therefore, commercial manufacturers pack the sutures in foil/plastic and sterilize them using Cobalt-60 Gamma Irradiation. Gamma rays penetrate the packaging entirely and destroy microbial DNA without generating heat. Alternatively, Ethylene Oxide (EtO) gas is used for some materials in hospital settings.",
        "Why_Not": "Autoclaving and Hot Air Ovens use high heat, which destroys synthetic polymers and catgut. Gamma irradiation provides cold sterilization.",
        "Wow_Approach": "Never re-sterilize a previously opened packet of absorbable synthetic suture (like Vicryl) using steam or chemical baths—the moisture and heat immediately begin the hydrolysis breakdown process, rendering the suture dangerously weak for surgery."
    },
    2562: {
        "topic": "Third Degree Burn - Coagulation of Epidermis and Dermis",
        "Core_Anatomy": "Epidermis, dermis, and subcutaneous tissue.",
        "Pathogenesis_Immediate": "Coagulation (necrosis) of the entire epidermis and dermis is seen in a Third Degree Burn (full-thickness burn).",
        "Pathogenesis_Deep": "Burn depth dictates healing. (1) First degree: superficial epidermis (erythema, pain, no blisters). (2) Second degree: epidermis + partial dermis (blisters, severe pain, heals from adnexal structures like hair follicles). (3) Third degree: complete destruction of epidermis and the entire dermis down to the subcutaneous fat. The tissue is coagulated, appearing leathery, dry, and white/charred (eschar). Critically, third-degree burns are PAINLESS at the center because all dermal nerve endings have been destroyed.",
        "Why_Not": "First and second-degree burns leave the deep dermis intact. Third-degree destroys the entire skin thickness.",
        "Wow_Approach": "Because there are no surviving epidermal stem cells (in hair follicles or sweat glands) remaining in the center of a third-degree burn, it CANNOT heal by re-epithelialization from the center. It must heal slowly by contraction from the edges, or require a surgical skin graft."
    },
    2563: {
        "topic": "Reactionary Haemorrhage",
        "Core_Anatomy": "Surgical vascular ligation sites.",
        "Pathogenesis_Immediate": "Haemorrhage occurring within 24 hours of surgery (after initial haemostasis was achieved) is termed Reactionary Haemorrhage.",
        "Pathogenesis_Deep": "Surgical haemorrhage is classified by timing: (1) Primary: bleeding occurring during the surgery itself. (2) Reactionary: bleeding occurring within 24 hours post-op. This usually happens when the animal recovers from anaesthesia, blood pressure rises back to normal, and an improperly secured ligature slips off a vessel, or a blood clot is dislodged by movement. (3) Secondary: bleeding occurring 7-14 days post-op, usually due to bacterial infection eroding the vessel wall or dissolving the ligature.",
        "Why_Not": "Secondary haemorrhage happens a week later (infection). Primary is on the table. Reactionary is the classic 'slipped ligature' scenario in the recovery cage.",
        "Wow_Approach": "The classic, dreaded example of reactionary haemorrhage is a slipped ovarian pedicle ligature after a canine spay. The dog recovers, blood pressure rises, the knot slips, and the dog bleeds out internally into the abdomen within the first 12 hours."
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
