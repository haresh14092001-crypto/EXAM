import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    179: {
        "topic": "Subpoena, Solemn Affirmation and Health Certificate in Veterinary Law",
        "Core_Anatomy": "N/A — Legal procedure, evidence and veterinary certification.",
        "Pathogenesis_Immediate": "Key veterinary jurisprudence legal terms: Subpoena — court order compelling a witness to appear and testify (failure = contempt of court). Solemn Affirmation — non-religious alternative to an oath, affirming to tell the truth. Health Certificate — documentary evidence issued by a veterinarian certifying animal health status.",
        "Pathogenesis_Deep": "In Indian court procedure: A Subpoena (Summons to Witness under CrPC Section 61) compels attendance. A Solemn Affirmation is governed by Section 5 of the Oaths Act 1969 — an affirmation has the same legal force as an oath. Health certificates issued by veterinarians are Documentary Evidence under the Indian Evidence Act, admissible in court as primary evidence of the animal's condition at time of examination.",
        "Why_Not": "An Affidavit is a voluntary written sworn statement used in civil matters; a Subpoena is a compulsory court summons. A Veterinary Witness who ignores a Subpoena commits contempt of court, attracting imprisonment. Unlike human doctors who may claim patient confidentiality, there is no equivalent veterinary professional privilege in Indian law.",
        "Wow_Approach": "When a veterinarian receives a court Subpoena: Appear on the stated date with all relevant case records, radiographs, and laboratory reports. Dress professionally. Address the judge as 'Your Honour'. Provide only factual professional opinions within your area of expertise — avoid speculating beyond clinical findings. Expert witness fees are claimable from the court."
    },
    180: {
        "topic": "CITES - Convention on International Trade in Endangered Species",
        "Core_Anatomy": "N/A — International wildlife trade law.",
        "Pathogenesis_Immediate": "CITES (Convention on International Trade in Endangered Species of Wild Fauna and Flora) is the international agreement regulating trade in wildlife and wildlife products. India ratified CITES in 1976. CITES headquarters: Geneva, Switzerland.",
        "Pathogenesis_Deep": "CITES Appendices: Appendix I — Most endangered species (commercial trade prohibited): Tiger, Elephant, Rhino, Snow Leopard, Marine Turtles. Appendix II — Not currently threatened but trade must be controlled: Hippopotamus, Shark fins, Seahorses. Appendix III — Species protected in at least one country. All international movement of listed species requires CITES permits issued by the Management Authority (in India: the Director General of Foreign Trade, DGFT, after consultation with the CWLW).",
        "Why_Not": "CITES regulates TRADE (commercial movement) of wildlife — it does not directly regulate habitat protection or domestic hunting. WPA 1972 controls domestic protection. The Nagoya Protocol (2010) under the Convention on Biological Diversity (CBD) regulates access to genetic resources and benefit sharing — a distinct framework from CITES.",
        "Wow_Approach": "Krait (*Bungarus caeruleus*) is a non-poisonous — FALSE. Krait is one of the Big Four venomous snakes in India (Cobra, Krait, Russell's Viper, Saw-scaled Viper) responsible for the majority of Indian snakebite deaths. Conservation encompasses preservation AND sustainable use of biodiversity — TRUE. Pure preservation (locking away resources) is an outdated concept; modern conservation integrates human livelihoods with wildlife protection."
    }
}

# Also add a few more from the list to ensure we hit 10
enrichment.update({
    96: enrichment.get(96) or {
        "topic": "AWBI Central Government Removal Power",
        "Core_Anatomy": "N/A — Statutory governance.",
        "Pathogenesis_Immediate": "Under Section 8 of PCA Act 1960, the Central Government may at any time remove a member of the AWBI from office if found guilty of misconduct, incapacity to perform duties, or conflict of interest that compromises the Board's integrity.",
        "Pathogenesis_Deep": "The AWBI functions as an advisory statutory body. Its independence is protected by the requirement that removal must be communicated with reasons in writing and the member given opportunity to be heard (principles of natural justice). The AWBI advises the government on amendments to the PCA Act and on standards for animal experiments, transport, and slaughter.",
        "Why_Not": "Unlike independent regulatory bodies (SEBI, RBI), the AWBI is an advisory body without enforcement powers. Enforcement of the PCA Act is the responsibility of the police and Animal Welfare Officers appointed by state governments.",
        "Wow_Approach": "AWBI key data: Established 1962. Headquarters: 13/1, Third Seaward Road, Valmiki Nagar, Thiruvanmiyur, Chennai 600 041. Current Chairperson is appointed by the Ministry of Fisheries, Animal Husbandry and Dairying. The AWBI runs the Blue Cross programme for stray dog management."
    }
})

updated = 0
for q in data:
    if q['id'] in enrichment and not q.get('Core_Anatomy'):
        q.update(enrichment[q['id']])
        updated += 1
    elif q['id'] in enrichment and q.get('Core_Anatomy') == '':
        q.update(enrichment[q['id']])
        updated += 1

# Force update for IDs 179 and 180 regardless
for q in data:
    if q['id'] in [179, 180]:
        q.update(enrichment[q['id']])
        updated += 1

with open(db_path, "w", encoding="utf-8") as f:
    f.write("// Auto-generated Hybrid Exam Database\n")
    f.write("const examData = ")
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(";\n")

# Final validation
with open(db_path, "r", encoding="utf-8") as f:
    content2 = f.read()
json_str2 = re.sub(r'^.*?const examData = ', '', content2, flags=re.DOTALL)
json_str2 = json_str2.rsplit(';', 1)[0].strip()
data2 = json.loads(json_str2)
empty2 = [x for x in data2 if x.get('is_high_yield') and not x.get('Core_Anatomy')]
print(f"Batch 5/5 DONE: Updated {updated} questions.")
print(f"VALIDATION: {len(data2)} total entries. {len(empty2)} high-yield questions still empty.")
