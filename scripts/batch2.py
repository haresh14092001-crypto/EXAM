import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    11: {
        "topic": "Summer Sore (Habronemiasis) - Cutaneous Habronema in Horses",
        "Core_Anatomy": "The skin of the lower limbs, periorbital region, prepuce, and any wound site in horses.",
        "Pathogenesis_Immediate": "Cutaneous habronemiasis (Summer Sore) is a hypersensitivity-driven granulomatous skin disease in horses caused by deposition of *Habronema* spp. and *Draschia megastoma* larvae by fly vectors (Musca domestica, Stomoxys calcitrans) into wounds or mucous membranes.",
        "Pathogenesis_Deep": "Adult *Habronema* worms inhabit the gastric mucosa of horses. Fly maggots ingest infective larvae from horse faeces; larvae develop within the fly pupae. When infected flies feed on wound secretions or moisture around the eyes/prepuce, they deposit infective L3 larvae. In non-gastric sites, the larvae cannot complete their lifecycle; instead, they trigger a massive eosinophilic and granulomatous host reaction, forming characteristic soft, ulcerated, caseous (sulfur granule-containing) lesions that fail to heal through summer.",
        "Why_Not": "Pythiosis (Swamp Cancer) is a fungal-like (*Pythium insidiosum*) proliferative ulcerative lesion of the lower limbs in horses in tropical swampy regions, containing 'kunkers' (mineralized necrotic cores). Habronemiasis lesions contain soft, yellow, caseous granules without mineralisation.",
        "Wow_Approach": "Treat cutaneous habronemiasis by surgically debriding the granulomatous tissue and applying Ivermectin paste topically (off-label) directly to the lesion, combined with systemic Ivermectin (0.2 mg/kg PO). Fly control using insecticide ear tags and wound protection from fly access is critical for prevention."
    },
    16: {
        "topic": "Echinococcus granulosus - Epidemiology, Life Cycle, and Zoonotic Control",
        "Core_Anatomy": "The intestinal mucosa of the definitive host (dog), the portal hepatic sinusoids, and hepatic parenchyma of intermediate hosts.",
        "Pathogenesis_Immediate": "Hydatid disease (*Echinococcus granulosus*) is maintained in a dog-ruminant cycle. Dogs excrete tapeworm eggs; sheep and cattle ingest eggs from contaminated pasture or water, developing liver/lung cysts. Humans are accidental dead-end hosts.",
        "Pathogenesis_Deep": "The adult *E. granulosus* lives in the small intestine of dogs, producing gravid proglottids packed with eggs (oncospheres). Sheep/cattle ingesting eggs on pasture develop hydatid cysts growing at ~1 cm/year in the liver (70%) and lungs (20%). When dogs eat infected offal (condemned livers/lungs), the protoscolices evaginate and develop into new adult tapeworms, completing the cycle.",
        "Why_Not": "Anthelmintic resistance is a major issue with other tapeworms (like Moniezia in ruminants). *Echinococcus* remains highly sensitive to Praziquantel, making strategic dog deworming every 6 weeks the definitive control measure for breaking the transmission cycle.",
        "Wow_Approach": "One infected dog can shed millions of eggs that remain viable in the environment for 12 months. Human infection causes progressive liver cysts often diagnosed incidentally on ultrasonography. Treatment requires surgical cystectomy or PAIR (Puncture, Aspiration, Injection of protoscolicidal agent, Re-aspiration) combined with long-term Albendazole therapy."
    },
    17: {
        "topic": "Haemonchosis in Sheep - Pathogenesis and FAMACHA System",
        "Core_Anatomy": "The abomasal mucosa, gastric glands, and the circulatory system (packed cell volume/haematocrit).",
        "Pathogenesis_Immediate": "*Haemonchus contortus* is a blood-sucking abomasal nematode that causes severe haemorrhagic anaemia (bottle jaw, pallor, lethargy) and death in sheep and goats, especially during peri-parturient periods and in young stock.",
        "Pathogenesis_Deep": "Adult *H. contortus* females lay 5,000-10,000 eggs per day. Using a lancet tooth, the worm ruptures abomasal capillaries and feeds on blood (0.05 ml blood/worm/day). A burden of 500-1000 worms causes severe iron-deficiency anaemia. The blood loss is compounded by protein-losing gastroenteropathy and hypoalbuminaemia, leading to submandibular oedema (bottle jaw). Blood loss peaks during peri-parturition due to immune suppression.",
        "Why_Not": "Fasciola hepatica causes anaemia through hepatic parenchymal destruction and bile duct hyperplasia, while *Haemonchus* causes direct abomasal haemorrhage. The bottle jaw in Haemonchosis is due to hypoproteinaemia, while in Fasciolosis it is due to both hypoproteinaemia and liver failure.",
        "Wow_Approach": "Use the FAMACHA system: monthly assessment of conjunctival mucous membrane colour against a 5-card colour chart. Only treat animals scoring 3-5 (pale/white conjunctiva). This targeted selective treatment (TST) approach delays anthelmintic resistance by leaving refugia (untreated animals) on pasture."
    },
    18: {
        "topic": "Milk Fever (Parturient Paresis / Hypocalcaemia) in Dairy Cows",
        "Core_Anatomy": "The parathyroid glands, the skeletal calcium reservoir (bone), the intestinal calcium-absorptive epithelium, and the renal tubules.",
        "Pathogenesis_Immediate": "Parturient paresis (Milk Fever) is a non-febrile hypocalcaemic metabolic disorder occurring within 72 hours of calving in high-producing dairy cows, causing progressive muscle flaccidity, recumbency, loss of consciousness, and death if untreated.",
        "Pathogenesis_Deep": "At peak lactation onset, the mammary gland demands up to 30 g of calcium per day for colostrum production. This sudden drain exceeds the cow's capacity to mobilize calcium from bone and absorb it from the gut. Blood ionized calcium drops sharply. Low calcium impairs neuromuscular transmission (reduced acetylcholine release at the neuromuscular junction), causing progressive flaccidity: Stage 1 (excitement/tetany), Stage 2 (sternal recumbency, S-shaped neck bend), Stage 3 (lateral recumbency, coma).",
        "Why_Not": "Grass tetany (Hypomagnesaemia) causes muscle tremors and tetanic spasms (not flaccidity) due to low magnesium blocking NMDA receptor inhibition, causing hyperexcitability. Milk fever causes flaccid paralysis due to impaired calcium-dependent neuromuscular transmission.",
        "Wow_Approach": "Treat immediately with slow IV 400 ml of 40% Calcium Borogluconate under cardiac monitoring. Prevent by feeding high-anion DCAD (Dietary Cation-Anion Difference) diets (-50 to -100 mEq/kg) for 3 weeks pre-calving: acidified diets stimulate PTH responsiveness, priming calcium mobilization pathways before the calving demand hits."
    },
    21: {
        "topic": "Clinical Medicine Examination Overview - Cardiac Biomarkers in Animals",
        "Core_Anatomy": "Cardiomyocytes, the myocardial contractile apparatus, and the coronary vasculature.",
        "Pathogenesis_Immediate": "Cardiac Troponin I (cTnI) is the gold-standard serum cardiac biomarker in dogs and cats, released specifically from damaged cardiomyocytes. Elevated serum cTnI indicates acute myocardial injury with high sensitivity and specificity.",
        "Pathogenesis_Deep": "Troponins are structural proteins of the myocardial contractile apparatus (the troponin complex regulates actin-myosin interaction). In healthy animals, cTnI is undetectable in serum. Any myocardial cell injury (infarction, myocarditis, blunt thoracic trauma, sepsis-induced cardiomyopathy) disrupts membrane integrity, releasing cTnI into the systemic circulation. It peaks within 4-6 hours of injury and remains elevated for 24-72 hours.",
        "Why_Not": "AST, LDH, and CK-MB are non-specific muscle enzymes released from skeletal and cardiac muscle. Cardiac Troponin I is strictly myocardium-specific, as skeletal muscle expresses a different isoform (sTnI) which does not cross-react with cardiac assays.",
        "Wow_Approach": "In dogs with suspected dilated cardiomyopathy (DCM) or arrhythmic syncope, a serum cTnI >0.2 ng/ml is a highly sensitive marker of ongoing myocardial cell loss and indicates initiation of antiarrhythmic or positive inotropic therapy (e.g., Pimobendan)."
    },
    22: {
        "topic": "Vagal Indigestion (Hoflund Syndrome) in Cattle",
        "Core_Anatomy": "The vagus nerve branches (dorsal and ventral vagal trunks), the reticulum, rumen, omasum, and abomasum.",
        "Pathogenesis_Immediate": "Vagal Indigestion is a syndrome caused by impaired forestomach and abomasal motility following damage to the vagal nerve branches, producing characteristic abdominal distension ('papple-shaped' abdomen) and progressive deterioration.",
        "Pathogenesis_Deep": "The vagus nerve provides motor innervation for coordinated contraction of the forestomachs. When damaged (typically by adhesions from traumatic reticulo-peritonitis or right-sided abomasal displacement), vagal signals are blocked. This causes failure of reticulo-ruminal mixing, omasal transport failure, and abomasal outflow obstruction. Fluid and gas accumulate, producing marked bilateral (particularly left-sided) abdominal distension. The rumen pH shifts as fermentation becomes unregulated.",
        "Why_Not": "Simple ruminal bloat is caused by excessive gas production from fermentation without vagal nerve damage; treatment is trocarization. Vagal Indigestion produces a chronic, progressive bilateral distension that does not respond to trocarization or passing a stomach tube.",
        "Wow_Approach": "Four types of Vagal Indigestion (Hoflund classification): Type I (failure of eructation), Type II (failure of omasal transport), Type III (abomasal impaction), Type IV (late pregnancy abomasal displacement). Prognosis is guarded; most cases require rumenotomy to break adhesions and manually evacuate impacted rumen/omasal content."
    },
    26: {
        "topic": "Oesophageal Obstruction (Choke) in Ruminants",
        "Core_Anatomy": "The pharynx, cervical oesophagus, thoracic oesophagus, and cardia of the oesophagus.",
        "Pathogenesis_Immediate": "Oesophageal obstruction (Choke) in ruminants is caused by sudden lodgement of a foreign body (turnip, potato, apple, or maize cob) in the oesophagus, blocking eructation and causing secondary frothy bloat in the rumen.",
        "Pathogenesis_Deep": "Ruminants normally eructate rumen gas every 1-2 minutes via the cardia. Oesophageal obstruction physically prevents the passage of rumen gas upward, causing rapid frothy bloat (particularly if the animal was on lush legume pasture). The continuous gas pressure increases tympany, causing compression of the diaphragm, reducing lung capacity, and causing respiratory distress. Prolonged obstruction causes oesophageal mucosal necrosis and stricture formation.",
        "Why_Not": "Pharyngeal obstruction or oesophageal groove abnormalities can also block eructation, but these are rarer. Frothy bloat on legume pasture without an oesophageal obstruction is caused by mucus-stabilized foam trapping gas, treatable with antifoaming agents (dimethicone/poloxalene).",
        "Wow_Approach": "First attempt gentle flushing with a stomach tube to dislodge the obstruction. If the foreign body is in the cervical oesophagus, attempt external digital manipulation. If thoracic, use a flexible probang (McKinnon forceps). Treat secondary frothy bloat with trocarization of the left paralumbar fossa if the animal is in severe respiratory distress."
    },
    31: {
        "topic": "Fatty Liver Syndrome (Hepatic Lipidosis) in High-Producing Dairy Cows",
        "Core_Anatomy": "The hepatocytes, hepatic sinusoids, and the adipose (fat) tissue depots of the peripartum dairy cow.",
        "Pathogenesis_Immediate": "Fatty liver syndrome (hepatic lipidosis) occurs in overconditioned (fat) dairy cows around parturition, when a massive negative energy balance (NEB) mobilizes NEFA from adipose tissue at rates exceeding the liver's capacity to export them as VLDL, causing hepatic triglyceride accumulation.",
        "Pathogenesis_Deep": "The periparturient dairy cow experiences a dramatic NEB as feed intake drops but milk production energy demands surge. This triggers adipose lipolysis, releasing massive Non-Esterified Fatty Acids (NEFA) into the portal blood. Hepatocytes take up NEFAs and either oxidize them to ketone bodies (causing ketosis) or re-esterify them to triglycerides. The bovine liver has a very limited capacity to export triglycerides as VLDL compared to other species. Triglycerides accumulate in hepatocytes (hepatic steatosis), impairing gluconeogenesis, ammonia detoxification, and immune function.",
        "Why_Not": "In humans and cats, hepatic lipidosis is also caused by NEB (anorexia in cats), but the mechanism of damage in dairy cows involves both lipid overload AND impaired VLDL export capacity unique to ruminant hepatic physiology.",
        "Wow_Approach": "Prevent fatty liver by maintaining a Body Condition Score of 3.0-3.5 at dry-off (never >3.75). Supplementing pre-calving dry cows with Propylene Glycol (500 ml once daily) provides glucogenic substrate, reducing NEFA mobilization. Post-calving: Dextrose IV, Vitamin B12, and choline supplementation enhance VLDL export from the liver."
    },
    34: {
        "topic": "Nervous Ketosis and Isopropanol Accumulation in Dairy Cattle",
        "Core_Anatomy": "The hypothalamus, basal ganglia, and cerebral cortex; the hepatic mitochondrial ketogenic pathway.",
        "Pathogenesis_Immediate": "Nervous ketosis is an atypical form of bovine ketosis presenting with severe CNS signs (frenzied licking, star-gazing, aggression, apparent blindness), thought to be caused by accumulation of isopropanol derived from acetone reduction, rather than just hypoglycaemia.",
        "Pathogenesis_Deep": "In ketosis, the massive hepatic accumulation of acetyl-CoA (from NEFA oxidation) overwhelms the TCA cycle, diverting acetyl-CoA to ketone body synthesis (acetoacetate, beta-hydroxybutyrate, and acetone). Acetone is spontaneously reduced by gut bacteria and rumen microbes to isopropanol (isopropyl alcohol). Isopropanol is a CNS depressant, causing the neurological signs of nervous ketosis including circling, aggression, and visual deficits.",
        "Why_Not": "Type 1 (Wasting) Ketosis presents with reduced milk production, depression, and a sweet acetone breath, without CNS signs. Nervous ketosis (Type 2) presents with florid neurological signs due to isopropanol accumulation on top of hypoglycaemia.",
        "Wow_Approach": "Treat nervous ketosis aggressively with IV 50% Dextrose (500 ml bolus), followed by oral Propylene Glycol (400-500 ml BID for 5 days). Unlike wasting ketosis, Dexamethasone (20 mg IM) is often added to stimulate gluconeogenesis, and recovery is typically rapid and dramatic within 4-6 hours."
    },
    38: {
        "topic": "Equine Azoturia (Exertional Rhabdomyolysis / Monday Morning Disease)",
        "Core_Anatomy": "The skeletal muscles (primarily the epaxial muscles of the croup and hindquarters), the renal tubular epithelium, and the urinary system.",
        "Pathogenesis_Immediate": "Exertional Rhabdomyolysis (azoturia) in horses is a metabolic myopathy occurring after exercise, especially following rest on a high-carbohydrate (grain) diet, causing severe gluteal muscle necrosis, pain, and myoglobinuria (port-wine coloured urine).",
        "Pathogenesis_Deep": "During rest on a high-grain diet, glycogen accumulates excessively in the muscle. Upon sudden strenuous exercise, glycolysis produces massive quantities of lactic acid in excess of the buffering capacity. The resultant intramuscular acidosis activates calcium-dependent proteases (calpains) and disrupts the sarco-endoplasmic reticulum, causing uncontrolled calcium release, sustained myosin-actin cross-bridge formation, and myofiber rupture (rhabdomyolysis). Myoglobin released from damaged muscle precipitates in the renal tubules, causing acute tubular necrosis.",
        "Why_Not": "Horses with colic show non-weight-bearing abdominal pain, pawing, and rolling. Azoturia shows firm, board-like gluteal muscles that are exquisitely tender on palpation, with the horse refusing to move the hindlimbs, reluctant to stand, and producing dark myoglobinuric urine.",
        "Wow_Approach": "Stop exercise immediately, keep the horse warm and still, and administer IV fluids (isotonic saline with sodium bicarbonate) at 10-15 L/hr to alkalinize the urine and prevent myoglobin precipitation in the renal tubules. Monitor urine colour and serum CK/AST enzymes. Maintain grain intake at rest-day levels."
    }
}

updated = 0
for q in data:
    if q['id'] in enrichment:
        q.update(enrichment[q['id']])
        updated += 1

with open(db_path, "w", encoding="utf-8") as f:
    f.write("// Auto-generated Hybrid Exam Database\n")
    f.write("const examData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"Batch 2/5 DONE: Updated {updated} questions.")
