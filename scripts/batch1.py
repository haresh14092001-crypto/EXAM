import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    1: {
        "topic": "Bovine Viral Diarrhea Virus (BVDV) - Reproductive Pathology",
        "Core_Anatomy": "Fetal trophoblasts, fetal thymus (immune system), and the utero-placental interface.",
        "Pathogenesis_Immediate": "BVDV crosses the placenta during maternal viraemia. Infection before Day 125 of gestation causes fetal immunotolerance (persistent infection/PI calves), stillbirths, mummification, or congenital defects.",
        "Pathogenesis_Deep": "BVDV is a Pestivirus that is highly teratogenic. Infection in early gestation (Day 40-125) destroys fetal lymphocytes before immune competence is established, creating a PI calf that sheds massive quantities of virus lifelong without immune response. Infection in mid-gestation causes cerebellar hypoplasia, ocular defects, and stillbirth. Late gestation infection causes weak, immunocompromised calves.",
        "Why_Not": "Rabies (Rhabdovirus, Lyssavirus) is a strictly neurotropic virus transmitted via saliva of infected animals through bite wounds, causing fatal encephalomyelitis. BVDV is a Pestivirus transmitted by direct contact and transplacentally causing reproductive failure.",
        "Wow_Approach": "The most dangerous BVDV source on any farm is the PI calf — it looks clinically normal but sheds 10,000 times more virus than an acutely infected animal. Test and cull every PI animal to eradicate BVDV from the herd."
    },
    2: {
        "topic": "Marek's Disease (Avian Herpesvirus) and Sciatic Nerve Pathology",
        "Core_Anatomy": "Peripheral nerves (sciatic, brachial, vagal, and celiac plexuses) and lymphoid organs (thymus, bursa of Fabricius) in chickens.",
        "Pathogenesis_Immediate": "Marek's Disease Virus (MDV, Gallid alphaherpesvirus 2) causes T-lymphocyte transformation and demyelination of peripheral nerves, producing ascending paralysis of one or both legs (the classic 'Marek's split-leg' posture).",
        "Pathogenesis_Deep": "MDV replicates in feather follicle epithelium and is shed in feather dander. After inhalation, it infects B-lymphocytes (lytic phase), then establishes latency in T-lymphocytes. Neoplastic transformation of CD4+ T-cells causes infiltration and demyelination of the sciatic nerves, leading to asymmetric leg paralysis, drooping wings, and blindness (ocular lymphomatosis).",
        "Why_Not": "Newcastle Disease (Ranikhet) causes neurological signs in poultry (torticollis, opisthotonus) due to viral encephalomyelitis, not peripheral nerve demyelination. Marek's pathology is strictly a T-cell lymphoma invading peripheral nerves.",
        "Wow_Approach": "Vaccinate all chicks on Day 1 of life with HVT (Herpesvirus of Turkeys) or bivalent (HVT + SB-1) vaccines. The vaccine does not prevent infection but prevents T-cell transformation and tumor formation, eliminating clinical disease completely."
    },
    3: {
        "topic": "Enterotoxaemia (Pulpy Kidney Disease) - Clostridium perfringens Type D",
        "Core_Anatomy": "Small intestinal epithelium (jejunum/ileum), renal tubular epithelium, and the blood-brain barrier.",
        "Pathogenesis_Immediate": "Rapid dietary changes causing overgrowth of *Clostridium perfringens* Type D in the intestine, producing massive quantities of epsilon toxin, causing hyperacute fatal toxaemia (Pulpy Kidney Disease) primarily in well-nourished lambs and calves.",
        "Pathogenesis_Deep": "Under normal conditions, *C. perfringens* Type D exists in low numbers in the gut. A sudden influx of undigested starch (grain overload or lush pasture) reaches the small intestine, acting as a substrate for explosive bacterial multiplication. The bacteria produce epsilon protoxin, which is activated by intestinal proteases to epsilon toxin. This binds to endothelial cells in the intestinal mucosa and brain, causing severe vascular permeability, cerebral oedema, and rapid autolysis of the kidneys post-mortem (pulpy kidney).",
        "Why_Not": "Swine Fever (Classical Swine Fever/CSF) does not cause pulpy kidney. Pulpy kidney is pathognomonic for *C. perfringens* Type D in lambs. The CSF lesion triad is: button ulcers in the large intestine, splenic infarctions, and haemorrhages under the kidney capsule.",
        "Wow_Approach": "Prevent Enterotoxaemia through annual vaccination with *Clostridium* polyvalent vaccines (Types C+D or '8-in-1' clostridial bacterin-toxoids). During high-risk grain-feeding periods, supplement with oral sodium bicarbonate to limit intestinal pH drops that favour clostridial proliferation."
    },
    4: {
        "topic": "Pullorum Disease and Fowl Typhoid - Vertical Transmission in Poultry",
        "Core_Anatomy": "The ovarian follicles, yolk sac, and hepatic parenchyma in infected parent flocks.",
        "Pathogenesis_Immediate": "Pullorum disease (*Salmonella pullorum*) and Fowl Typhoid (*Salmonella gallinarum*) are vertically transmitted (transovarian) from infected parent hens to their eggs and chicks, causing high mortality in young poultry.",
        "Pathogenesis_Deep": "In infected laying hens, *Salmonella* organisms colonize the ovaries. The bacteria enter the developing yolk sac before the shell is formed, creating an infected egg. Upon hatching, chicks are systemically infected, developing acute septicaemia characterized by white diarrhoea (chalk-white pasty vent), huddling, and high mortality. *S. pullorum* uniquely colonizes the ovarian tissue, creating a persistent carrier state in surviving hens.",
        "Why_Not": "Fowl Typhoid (*S. gallinarum*) is primarily a disease of adult birds causing septicaemia, while *S. pullorum* primarily affects young chicks under 3 weeks. Both are vertically transmitted, unlike horizontally-transmitted *S. enteritidis*, which contaminates the egg surface after laying.",
        "Wow_Approach": "Eradicate Pullorum disease using the National Pullorum Testing Program: perform whole-blood rapid agglutination tests on all breeding flocks annually. Cull any reactor immediately. This test-and-cull strategy has eliminated Pullorum from commercial flocks in developed countries."
    },
    5: {
        "topic": "Johne's Disease (Paratuberculosis) - Diagnosis by Johnin Test and Rectal Pinch",
        "Core_Anatomy": "The ileal mucosa, regional (mesenteric) lymph nodes, and submucosal macrophages of ruminants.",
        "Pathogenesis_Immediate": "Chronic granulomatous enteritis of the small intestine caused by *Mycobacterium avium subsp. paratuberculosis* (MAP), presenting as profuse, non-foul-smelling diarrhoea, progressive weight loss, and submandibular oedema (bottle jaw) in adult cattle.",
        "Pathogenesis_Deep": "MAP is ingested by calves under 6 months (highly susceptible). The bacteria survive and multiply within macrophages in the ileal mucosa, causing a progressive granulomatous thickening of the intestinal wall. This destroys the absorptive villi, causing protein-losing enteropathy. The massive protein loss leads to hypoalbuminaemia, oncotic pressure failure, and plasma leakage into the submandibular space (bottle jaw).",
        "Why_Not": "Unlike Bovine Tuberculosis (*M. bovis*) which causes pulmonary and lymph node granulomas detectable by intradermal tuberculin test, Johne's disease causes strictly intestinal granulomas. The Johnin test (intradermal MAP antigen injection) and ELISA/faecal PCR are used for diagnosis.",
        "Wow_Approach": "The Rectal Pinch Test (Kaneko's test) can detect Johne's disease in the field: rectal palpation of corrugated (accordion-like), thickened intestinal folds in the ileum, palpable through the rectal wall, is virtually pathognomonic for advanced paratuberculosis."
    },
    6: {
        "topic": "Lungworm (Dictyocaulus viviparus) and Verminous Pneumonia in Cattle",
        "Core_Anatomy": "The bronchi and bronchioles of the pulmonary airways (lower respiratory tract) in cattle and sheep.",
        "Pathogenesis_Immediate": "Dictyocaulus viviparus (bovine lungworm/husk) causes verminous bronchitis/pneumonia in calves on pasture, presenting as severe persistent coughing (husk), respiratory distress, and weight loss.",
        "Pathogenesis_Deep": "Infective L3 larvae are ingested from pasture, penetrate the intestinal mucosa, migrate via lymphatics to mesenteric lymph nodes, and travel through the thoracic duct to the lungs. Adult worms develop in the bronchi, causing intense mechanical blockage and inflammatory mucus hypersecretion, resulting in airway obstruction, alveolar consolidation, and emphysema.",
        "Why_Not": "Pasteurella/Mannheimia pneumonia is caused by bacterial infection of the lungs, presenting with mucopurulent nasal discharge and pleural friction rubs. Verminous pneumonia is caused by adult nematodes in the airways with a characteristic dry, harsh bronchial cough without purulent nasal discharge.",
        "Wow_Approach": "Prevent by vaccinating calves with the oral live-larval *Dictyocaulus* vaccine (Huskvac) at 8 weeks and again at 4 weeks before first pasture season. Treat affected animals with benzimidazoles (Fenbendazole) or Ivermectin; monitor pasture larval counts using Baermann technique."
    },
    7: {
        "topic": "Triclabendazole as the Drug of Choice for Fasciolosis (Liver Fluke)",
        "Core_Anatomy": "The liver parenchyma, biliary system (bile ducts), and the peritoneal cavity of cattle, sheep, and goats.",
        "Pathogenesis_Immediate": "Fasciolosis (*Fasciola hepatica*) causes massive hepatic damage through migration of immature flukes through the liver parenchyma (acute phase) and bile duct pathology from adult flukes (chronic phase). Triclabendazole is uniquely effective against both immature and adult flukes.",
        "Pathogenesis_Deep": "After ingestion of metacercariae from contaminated pasture (snail intermediate host: *Lymnaea truncatula*), juvenile flukes migrate through the intestinal wall into the peritoneal cavity, then penetrate the liver capsule. The immature flukes tunnel through hepatic parenchyma for 6-8 weeks, causing haemorrhagic tracts, hepatocyte necrosis, and fibrosis. Adult flukes establish in the bile ducts, causing hyperplastic cholangitis, pipe-stem fibrosis, and anaemia.",
        "Why_Not": "Albendazole and Closantel are highly effective only against adult *Fasciola* (>12 weeks post-infection). Triclabendazole (a halogenated benzimidazole) is uniquely effective at both the early immature stage (1-week-old flukes) and adult stage due to its high lipophilicity and rapid penetration of the tegument.",
        "Wow_Approach": "Administer Triclabendazole during the acute (early) phase of fasciolosis outbreaks in autumn/wet seasons when immature fluke damage is maximal. Control the snail intermediate host by draining wet pastures, applying molluscicides (copper sulphate), and fencing wet areas from livestock access."
    },
    8: {
        "topic": "Self-Cure Phenomenon in Haemonchosis (Haemonchus contortus)",
        "Core_Anatomy": "The abomasal mucosa, gastric glands, and the mucosal immune effector cells (mast cells, eosinophils) of sheep.",
        "Pathogenesis_Immediate": "The Self-Cure Phenomenon in sheep is a rapid, IgE-mediated immune hypersensitivity reaction in the abomasal mucosa that expels a massive established adult *Haemonchus* burden within 24-48 hours following challenge with a new wave of infective larvae.",
        "Pathogenesis_Deep": "Repeated exposure to *H. contortus* larvae primes the mucosal immune system. When a sensitized sheep ingests a new large dose of infective L3 larvae, the larvae-triggered IgE-mast cell degranulation cascade causes violent smooth muscle contractions and hypersecretion of mucus. This dramatically increases abomasal motility, expelling the existing adult worm burden along with the newly ingested larvae in a single purgative event.",
        "Why_Not": "This immune expulsion is paradoxical: the trigger is *new larval* ingestion, but the worms expelled are the established *adult* population. This self-cure mechanism is temporary and highly dependent on nutritional status; protein-deficient sheep lose this immune expulsion capacity (periparturient rise).",
        "Wow_Approach": "The Self-Cure Phenomenon has practical significance: after a natural challenge event in well-nourished animals, Faecal Egg Count (FEC) drops dramatically without treatment. Always re-check FEC 2 weeks post-flush before administering anthelmintics to avoid unnecessary treatment."
    },
    9: {
        "topic": "Hydatid Disease (Echinococcosis) - Echinococcus granulosus",
        "Core_Anatomy": "The liver (primary target), lungs (secondary), and any organ of the intermediate host (cattle, sheep, humans).",
        "Pathogenesis_Immediate": "Echinococcosis is a zoonotic tapeworm disease where *Echinococcus granulosus* forms fluid-filled hydatid cysts in the liver and lungs of intermediate hosts (cattle, sheep, humans), causing chronic, space-occupying lesions.",
        "Pathogenesis_Deep": "Dogs (definitive host) harbour adult *E. granulosus* tapeworms in their small intestine. Eggs are shed in dog faeces. When ingested by intermediate hosts (cattle, sheep, or humans), the oncosphere hatches in the small intestine, penetrates the portal vein, and is carried to the liver, where it develops into a slowly growing hydatid cyst (germinal layer + laminated layer + pericyst) containing brood capsules and protoscolices.",
        "Why_Not": "Cysticercosis (*Taenia saginata/solium*) forms bladder worms (Cysticercus bovis/cellulosae) in muscle, liver, and brain of intermediate hosts but not fluid-filled cysts. Hydatid cysts contain daughter cysts with thousands of protoscolices and are dangerously anaphylactic if they rupture.",
        "Wow_Approach": "Control hydatidosis by the Dog-Sheep cycle interruption triad: (1) regular anthelmintic treatment of dogs with Praziquantel every 6 weeks, (2) condemning and proper disposal of infected offal at slaughter, and (3) preventing dogs from accessing abattoir waste."
    },
    10: {
        "topic": "Coenurosis (Gid / Sturdy) - Coenurus cerebralis in Sheep",
        "Core_Anatomy": "The cerebral hemispheres, cerebellum, and spinal cord of intermediate hosts (sheep, goats).",
        "Pathogenesis_Immediate": "Coenurosis is a larval cestode disease where *Coenurus cerebralis* (the larval stage of *Taenia multiceps*) forms large, fluid-filled, multi-scoliced cysts in the brain and spinal cord of sheep and goats, causing progressive neurological signs (Gid/Sturdy).",
        "Pathogenesis_Deep": "Dogs harbouring adult *Taenia multiceps* shed eggs in faeces. When ingested by sheep, the hexacanth embryo penetrates the intestinal wall, enters the bloodstream, and migrates to the CNS. The larva develops slowly into a *Coenurus cerebralis* cyst, growing over several months. As the cyst expands, it compresses the adjacent brain tissue, causing progressive circling (giddiness), head pressing, and blindness depending on cyst location.",
        "Why_Not": "Hydatid cysts (*Echinococcus granulosus*) primarily develop in the liver and lungs and contain brood capsules with daughter cysts. Coenurus cerebralis develops strictly in the CNS, contains multiple protoscolices attached directly to the germinal layer with no daughter cysts.",
        "Wow_Approach": "Diagnose by identifying a soft, fluctuant area on the skull (thinning of bone overlying the cyst) and confirming with ultrasound. Surgical trepanation and needle aspiration of the cyst can be curative if the cyst is superficial. Control by regular deworming of dogs with Praziquantel."
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

print(f"Batch 1/5 DONE: Updated {updated} questions.")
