import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1829: {
        "topic": "VMD 512 - Zoo and Wildlife Header",
        "Core_Anatomy": "Wildlife conservation and captive breeding.",
        "Pathogenesis_Immediate": "This section covers the management, restraint, and pathology of non-domesticated species.",
        "Pathogenesis_Deep": "Zoo medicine heavily emphasizes chemical immobilization (darting), zoonotic disease control in captive populations, and nutritional diseases unique to wild animals (like metabolic bone disease in reptiles or capture myopathy in ungulates).",
        "Why_Not": "Domestic animal medicine relies on physical restraint and standard dosages; wildlife medicine requires extreme stress-reduction and allometric scaling for drug dosages.",
        "Wow_Approach": "Always prioritize the safety of the human personnel first when approaching a wild animal question."
    },
    1833: {
        "topic": "Veterinary Jurisprudence - WII",
        "Core_Anatomy": "N/A - Wildlife Institution.",
        "Pathogenesis_Immediate": "WII stands for the Wildlife Institute of India.",
        "Pathogenesis_Deep": "Established in 1982 in Dehradun, the Wildlife Institute of India is an internationally acclaimed institution under the Ministry of Environment, Forest and Climate Change. It is the premier training and research facility for wildlife conservation, forensic science (identifying poached animal parts like ivory or tiger bone), and eco-development in South Asia.",
        "Why_Not": "It is not the Wildlife 'Initiative' or 'Investigation' of India; 'Institute' is the legally recognized term.",
        "Wow_Approach": "Forensic veterinarians often send confiscated DNA or morphological evidence (like suspected rhino horn or shahtoosh shawls) directly to the WII laboratory for definitive legal identification in poaching cases."
    },
    1839: {
        "topic": "Zoo Animal Classification - The Okapi",
        "Core_Anatomy": "Ruminant gastrointestinal tract.",
        "Pathogenesis_Immediate": "The Okapi is specifically matched to the category of 'Exotic Ruminants'.",
        "Pathogenesis_Deep": "The Okapi (Okapia johnstoni) is an endangered even-toed ungulate native strictly to the northeast of the Democratic Republic of the Congo. Despite having zebra-like stripes on its legs, it is actually the only living relative of the Giraffe (Giraffidae family). As an exotic ruminant, its veterinary care, parasite control, and anesthetic protocols are heavily extrapolated from domestic cattle and giraffes.",
        "Why_Not": "It is not an equid (despite the stripes) and therefore does not have a hindgut-fermenting digestive system like a horse or zebra.",
        "Wow_Approach": "Like giraffes, the okapi has an exceptionally long, prehensile, dark purplish tongue used for stripping leaves from trees, which can sometimes suffer from traumatic lacerations in captivity."
    },
    1840: {
        "topic": "Wildlife Conservation - Project Tiger",
        "Core_Anatomy": "N/A - Conservation Framework.",
        "Pathogenesis_Immediate": "Project Tiger is a major wildlife conservation initiative historically matched to the era of the Wildlife Protection Act (1972) and officially launched in 1973.",
        "Pathogenesis_Deep": "Project Tiger was launched by the Government of India in April 1973 from Jim Corbett National Park. Its primary aim was to ensure a viable population of Bengal tigers in their natural habitats, protecting them from extinction and preserving areas of biological importance as a national heritage. It led to the establishment of numerous heavily protected Tiger Reserves across the country.",
        "Why_Not": "Project Elephant (1992) and Project Snow Leopard (2009) are separate initiatives.",
        "Wow_Approach": "Veterinarians working in Tiger Reserves are primarily responsible for radio-collaring operations, tranquilization of conflict tigers, and conducting necropsies on tigers killed in territorial fights or by poachers."
    },
    1841: {
        "topic": "Elephant Anatomy - The Tusk",
        "Core_Anatomy": "Maxillary incisors and dentin.",
        "Pathogenesis_Immediate": "An elephant's tusk is matched anatomically to 'Modified Incisors'.",
        "Pathogenesis_Deep": "Unlike the tusks of wild boars or walruses (which are modified canine teeth), the massive tusks of the elephant (Elephas maximus or Loxodonta africana) are continuously growing, heavily modified upper (maxillary) second incisors. They are composed entirely of dentin (ivory) with a small enamel cap that quickly wears off. A massive pulp cavity extends deep into the base of the tusk inside the skull.",
        "Why_Not": "They are not canine teeth or molars.",
        "Wow_Approach": "Because the pulp cavity is highly vascular and innervated, a fractured tusk (exposing the pulp) is excruciatingly painful and often leads to fatal ascending bacterial pulpitis/osteomyelitis if not aggressively treated or endodontically capped by a specialized zoo veterinarian."
    },
    1842: {
        "topic": "Wildlife Immobilization - Ketamine",
        "Core_Anatomy": "NMDA receptors (Central Nervous System).",
        "Pathogenesis_Immediate": "Ketamine is classically matched to its pharmacological class as a 'Dissociative Anaesthetic agent'.",
        "Pathogenesis_Deep": "Ketamine is an NMDA receptor antagonist. Instead of causing generalized CNS depression (like barbiturates), it selectively interrupts the sensory association areas of the brain while leaving the limbic system active. This 'dissociates' the animal from its environment. The animal becomes profoundly analgesic and cataleptic (rigid), often keeping its eyes wide open and maintaining a strong swallowing reflex. It is highly safe for cardiovascular function, making it the backbone of darting combinations.",
        "Why_Not": "It is not a sedative (like Xylazine) or a tranquilizer (like Acepromazine). It is a true dissociative anesthetic.",
        "Wow_Approach": "Ketamine causes severe muscle rigidity. Therefore, it is almost NEVER used alone in wildlife darting; it is always combined with a muscle relaxant/sedative (like Xylazine or Medetomidine) to ensure smooth induction and recovery."
    },
    1843: {
        "topic": "Wildlife Immobilization - Xylazine and Yohimbine",
        "Core_Anatomy": "Alpha-2 adrenergic receptors (Central Nervous System).",
        "Pathogenesis_Immediate": "Xylazine (an alpha-2 agonist sedative) is matched with its specific reversal agent, Yohimbine (an alpha-2 antagonist).",
        "Pathogenesis_Deep": "In wildlife medicine, you cannot simply leave a sedated animal in the field to slowly wake up, as it will be killed by predators or die of hyperthermia/bloat. Xylazine provides profound sedation and muscle relaxation. Once the veterinary procedure (e.g., placing a radio collar) is complete, Yohimbine is injected intravenously. Yohimbine competitively blocks the alpha-2 receptors, instantly displacing the Xylazine. The animal wakes up and is on its feet within 1 to 3 minutes.",
        "Why_Not": "Atipamezole is the specific reversal for Medetomidine. Naloxone is the reversal for opioids (like Etorphine/M99). Yohimbine is the classic historical reversal for Xylazine.",
        "Wow_Approach": "Yohimbine only reverses the Xylazine. If you used a Ketamine-Xylazine dart mixture, reversing the Xylazine too early (before the Ketamine wears off) will cause the animal to wake up violently thrashing and hallucinating due to the un-opposed Ketamine."
    },
    1846: {
        "topic": "Companion Animal Objective Section Header",
        "Core_Anatomy": "Small Animal Systemic Medicine.",
        "Pathogenesis_Immediate": "This header introduces objective questions focused on feline and canine specific physiology and pathology.",
        "Pathogenesis_Deep": "Testing often revolves around unique species-specific reproductive traits, infectious diseases, and metabolic anomalies that differ sharply from large animals.",
        "Why_Not": "Do not apply bovine or equine physiology rules to cats and dogs.",
        "Wow_Approach": "Cats are not small dogs; their hepatic metabolism and reproductive cycles are entirely distinct."
    },
    1851: {
        "topic": "Feline Reproduction - Induced Ovulation",
        "Core_Anatomy": "Hypothalamus (GnRH) and ovaries.",
        "Pathogenesis_Immediate": "The statement 'Cats are induced ovulators' is absolutely TRUE.",
        "Pathogenesis_Deep": "Unlike dogs, cows, or horses (which are spontaneous ovulators releasing eggs at a set time in their cycle regardless of mating), queens (female cats) will not ovulate unless they are physically stimulated. The male cat's penis possesses hundreds of keratinized, backwards-facing spines. During copulation, the withdrawal of the penis violently scrapes the queen's vagina. This severe sensory stimulation triggers a massive neural reflex, causing the hypothalamus to release a surge of GnRH, followed by an LH surge that induces ovulation 24-48 hours later.",
        "Why_Not": "Without physical copulation (or artificial mechanical stimulation of the vagina), the queen's mature ovarian follicles will eventually regress, and she will cycle back into estrus repeatedly without ever releasing an egg.",
        "Wow_Approach": "Because multiple matings are required to trigger a sufficient LH surge, a queen will often mate with several different tomcats during one estrus cycle, frequently resulting in a single litter of kittens with multiple different fathers (superfecundation)."
    },
    1852: {
        "topic": "Canine Obstetrics - Eclampsia",
        "Core_Anatomy": "Neuromuscular junction and skeletal muscle.",
        "Pathogenesis_Immediate": "Eclampsia in the bitch (puerperal tetany) is classically matched with Hypocalcemia.",
        "Pathogenesis_Deep": "Eclampsia occurs most commonly in small-breed dogs (like Chihuahuas or Yorkies) 1 to 3 weeks after whelping (during peak lactation). The massive loss of calcium into the milk rapidly depletes the bitch's extracellular ionized calcium. In dogs, this lowers the threshold potential of peripheral nerve membranes, causing them to fire spontaneously. The bitch presents with severe, rigid muscle tremors, panting, high fever, and tetanic convulsions.",
        "Why_Not": "Unlike human eclampsia (which is related to hypertension and seizures during pregnancy), canine eclampsia is strictly a metabolic hypocalcemic tetany occurring post-partum.",
        "Wow_Approach": "Treatment requires slow, cautious intravenous administration of 10% Calcium Gluconate while constantly monitoring the heart rate. If the heart rate suddenly drops (bradycardia), you must stop the infusion immediately to prevent fatal cardiac arrest."
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
