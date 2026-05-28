import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    2052: {
        "topic": "Bovine Ketosis - Silage as Predisposing Factor",
        "Core_Anatomy": "Hepatic gluconeogenesis and rumen fermentation.",
        "Pathogenesis_Immediate": "In ketosis, the cow initially refuses to eat concentrate (grain) feeds but continues eating roughage such as silage in the early stage.",
        "Pathogenesis_Deep": "Bovine ketosis (acetonemia) occurs in early lactation when the energy demands of peak milk production vastly exceed dietary energy intake, creating a severe negative energy balance (NEB). The liver compensates by massively mobilizing body fat reserves (NEFA). In the liver, these NEFAs are converted into ketone bodies (acetoacetate, beta-hydroxybutyrate, acetone). These accumulate in the blood, causing ketonemia. One of the earliest signs is a selective anorexia: the cow will still eat sweet-smelling roughage/silage but refuses energy-dense concentrates.",
        "Why_Not": "Total anorexia (refusing all feed) is a later, more severe sign. Early selective anorexia for concentrates is the clinician's key to catching ketosis before it progresses to the nervous form.",
        "Wow_Approach": "The easiest field test for ketosis is to smell the cow's milk or breath. A distinct sweet, fruity acetone odor (like nail polish remover) is pathognomonic for severe ketosis."
    },
    2058: {
        "topic": "Nutritional Deficiency Matching Header",
        "Core_Anatomy": "Systemic micronutrient metabolism.",
        "Pathogenesis_Immediate": "This header introduces the critical clinical association between specific nutritional deficiencies and their pathognomonic diseases.",
        "Pathogenesis_Deep": "Mastering these pairings is fundamental to veterinary board exams: each deficiency causes a uniquely recognizable clinical syndrome that is directly testable.",
        "Why_Not": "Confusing mineral/vitamin deficiencies with each other is a major source of exam errors.",
        "Wow_Approach": "Create a mental map: Selenium = Muscle (WMD); Zinc = Skin (Parakeratosis); Iodine = Thyroid (Goiter); Manganese = Bone (Perosis)."
    },
    2059: {
        "topic": "Zinc Deficiency - Parakeratosis",
        "Core_Anatomy": "Epidermis (stratum spinosum and granulosum).",
        "Pathogenesis_Immediate": "Parakeratosis (a severe, crusty skin disease) is the classic clinical manifestation of Zinc deficiency in pigs.",
        "Pathogenesis_Deep": "Zinc is a critical cofactor for over 300 enzymes, particularly those involved in epidermal cell differentiation and keratinization. In zinc deficiency, the normal progression of keratinocytes from the basal layer to the surface is disrupted. The cells fail to fully mature and lose their nuclei (parakeratosis = retention of pyknotic nuclei in the stratum corneum). This manifests as severe, symmetric, dark, scaly, crusty plaques that coalesce across the abdomen and hindlimbs of pigs.",
        "Why_Not": "Selenium deficiency causes White Muscle Disease (muscle necrosis). Iodine deficiency causes Goiter. Vitamin E deficiency causes muscle disease.",
        "Wow_Approach": "In large-breed puppies, parakeratosis is often secondary not to outright zinc deficiency, but to an excess of dietary calcium (from overzealous supplementation) that competitively blocks intestinal zinc absorption."
    },
    2060: {
        "topic": "Selenium Toxicity - Alkali Disease",
        "Core_Anatomy": "Hoof horn, hair follicles, and liver.",
        "Pathogenesis_Immediate": "Selenium toxicity (Selenosis) in livestock grazing selenium-accumulator plants is classically known as 'Alkali Disease' (chronic form) or 'Blind Staggers' (acute/subacute form).",
        "Pathogenesis_Deep": "In areas with naturally high selenium soil content (seleniferous soils), cattle and horses that chronically graze indicator plants (like Astragalus spp.) accumulate toxic amounts of selenium. Selenium substitutes for sulfur in the disulfide bonds of structural proteins (keratin in hoof horn and hair). This destroys the structural integrity, causing the hoof horn to crack and slough off and the long hair to fall out. Affected animals also develop severe liver necrosis.",
        "Why_Not": "Iodine deficiency causes Goiter (thyroid enlargement), not hoof/hair disease. Vitamin E deficiency causes muscle disease.",
        "Wow_Approach": "Paradoxically, selenium deficiency (White Muscle Disease) and selenium toxicity (Alkali Disease) are managed with the same trace element—one too low, one too high. The therapeutic window for selenium is the narrowest of any trace mineral."
    },
    2067: {
        "topic": "Iodine Deficiency - Goiter",
        "Core_Anatomy": "Thyroid gland.",
        "Pathogenesis_Immediate": "Goiter (enlarged thyroid gland) is the pathognomonic manifestation of Iodine deficiency in all species.",
        "Pathogenesis_Deep": "Iodine is an essential component of the thyroid hormones T3 and T4. When iodine is deficient, the thyroid gland cannot produce sufficient T3/T4. The pituitary gland senses this and secretes massive amounts of TSH (Thyroid Stimulating Hormone). The chronic TSH stimulation causes uncontrolled proliferation of thyroid follicular cells, resulting in a huge, visibly palpable swelling of the thyroid glands on both sides of the trachea (Goiter).",
        "Why_Not": "Pantothenic acid (Vitamin B5) deficiency causes 'Goose-stepping' gait in pigs. Goiter is strictly Iodine deficiency.",
        "Wow_Approach": "In goitrogenic regions of India (e.g., mountainous areas far from the sea), supplement the salt lick with potassium iodide (KI) to prevent endemic goiter in livestock."
    },
    2068: {
        "topic": "VMD Fill in the Blanks Header",
        "Core_Anatomy": "Systemic Veterinary Medicine.",
        "Pathogenesis_Immediate": "Fill in the blanks require precise recall of clinical terms without the benefit of elimination.",
        "Pathogenesis_Deep": "This format tests whether a clinical sign or legal parameter has been perfectly linked in memory to its specific pathophysiological etiology or statute.",
        "Why_Not": "Vague answers will not receive credit.",
        "Wow_Approach": "Rely on your first instinct for these blanks."
    },
    2073: {
        "topic": "Veterinary Forensics - Bishoping (Tooth Fraud)",
        "Core_Anatomy": "Equine incisor teeth.",
        "Pathogenesis_Immediate": "The fraudulent practice of artificially altering a horse's teeth to make it appear younger than it is is called 'Bishoping'.",
        "Pathogenesis_Deep": "A horse's age is accurately estimated by examining the progressive changes in the incisor teeth (emergence, wear patterns, Galvayne's groove, table surface angle). To defraud buyers, dishonest sellers will artificially create a 'mark' or 'cup' (the dark depression on the biting surface of young horses' teeth) in the teeth of an older horse using a hot iron or a dental burr. This process is called Bishoping.",
        "Why_Not": "Unlike cattle (where the age is estimated by dental eruption), the detailed wear pattern of equine incisors allows age estimation up to approximately 20 years.",
        "Wow_Approach": "A forensic veterinarian can easily detect Bishoping because artificially created cups are perfectly circular and uniform, whereas natural cups are irregular; also, the surrounding enamel of the artificial cup will show heat-induced cracks or a sharp, unnatural edge."
    },
    2074: {
        "topic": "Veterinary Forensics - Blood Stain Examination",
        "Core_Anatomy": "Erythrocytes (dried blood morphology).",
        "Pathogenesis_Immediate": "The statement 'Examination of blood stains is of great importance for veterolegal purposes' is TRUE.",
        "Pathogenesis_Deep": "In cases of animal cruelty, malicious killing, or poaching, blood stain analysis by a forensic veterinarian can determine: (1) Species of origin: Using serum precipitation tests (Ouchterlony/precipitin test) or PCR-based species identification, you can confirm if blood found at a crime scene is from cattle, human, or a protected wildlife species. (2) Age of the stain: Fresh blood is red; oxidized blood turns brown. (3) Stain pattern: Arterial spurts, drips, and cast-off patterns can reconstruct how the animal was killed.",
        "Why_Not": "Blood stain examination is absolutely critical for wildlife crime; if poachers are found with tiger bone powder, detecting blood from Panthera tigris on their tools using PCR can directly link them to the kill.",
        "Wow_Approach": "The preliminary Luminol test will detect blood stains that have been scrubbed away, as even minute hemoglobin residues cause a bright blue chemiluminescent glow."
    },
    2076: {
        "topic": "Milk Adulteration - Ghee Fraud",
        "Core_Anatomy": "N/A - Food Science / Public Health.",
        "Pathogenesis_Immediate": "The adulteration of Ghee (clarified butter) with vegetable oil or sesame oil is a common and legally prosecutable form of food fraud in India.",
        "Pathogenesis_Deep": "Pure ghee is composed almost exclusively of saturated animal fats (short-chain fatty acids from milk). Its adulterants (vegetable oil, sesame oil, cottonseed oil) contain distinctive plant sterols and long-chain unsaturated fatty acids that are absent in pure ghee. Forensic tests include the Baudouin test (detects sesame oil by a red color with concentrated H2SO4 and sugar) and the Butyro-refractometer test (measures the optical refraction index of the fat).",
        "Why_Not": "Adding water to ghee is difficult due to its anhydrous nature; the typical adulterant is cheaper plant-based fat.",
        "Wow_Approach": "Ghee adulterated with vanaspati (partially hydrogenated vegetable oil) will test positive for trans-fats and plant sterols (sitosterol/campesterol) using gas chromatography, forming the basis of the prosecution's evidence."
    },
    2077: {
        "topic": "Veterinary Jurisprudence - Match IPC Sections",
        "Core_Anatomy": "N/A - Legal Framework.",
        "Pathogenesis_Immediate": "The crime of Bestiality is matched to IPC Section 377.",
        "Pathogenesis_Deep": "This is a classic match-the-following question requiring memorization of the Indian Penal Code pairings. The IPC section 377 deals with unnatural offenses (including sexual crimes against animals). This is distinct from IPC 273 (Sale of noxious food), IPC 272 (Adulteration of food), and IPC 428/429 (Mischief by killing/maiming animals).",
        "Why_Not": "IPC 273 is the sale of adulterated food, not bestiality.",
        "Wow_Approach": "Memory trick: 377 = '3-s-e-x' (three comes before seven). It is the sex offense section."
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
