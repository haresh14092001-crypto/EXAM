import json, re
from pathlib import Path

db_path = Path(r"C:\Users\hares\.copilot\EXAM\database.js")
with open(db_path, "r", encoding="utf-8") as f:
    content = f.read()
json_str = re.sub(r'^.*?const examData = ', '', content, flags=re.DOTALL)
json_str = json_str.rsplit(';', 1)[0].strip()
data = json.loads(json_str)

enrichment = {
    3868: {
        "topic": "Marsupialization in Vet Surgery",
        "Core_Anatomy": "Abdomen and Urogenital cysts.",
        "Pathogenesis_Immediate": "Marsupialization is the surgical technique of opening a cyst/abscess and suturing its edges to the abdominal skin to create a permanent draining pocket, classically done for massive Prostatic Cysts in male dogs or severe Uterine Stump cysts in bitches.",
        "Pathogenesis_Deep": "When a cyst or abscess is too large or too vascular to safely resect completely, marsupialization is a life-saving salvage procedure. The cyst wall is incised, the contents drained, and the edges of the cyst wall are sutured directly to the external skin incision. This keeps the cavity wide open to the air, allowing it to continuously drain and gradually shrink over weeks through granulation.",
        "Why_Not": "A simple pyometra is treated via complete ovariohysterectomy, not marsupialization.",
        "Wow_Approach": "N/A"
    },
    3869: {
        "topic": "Teat Spider (Membranous Obstruction)",
        "Core_Anatomy": "Bovine Teat (Teat cistern).",
        "Pathogenesis_Immediate": "A membranous obstruction of the teat cistern is colloquially known as a Teat Spider.",
        "Pathogenesis_Deep": "This is a fibrous, spider-web-like membrane or solid sheet of tissue that develops within the teat cistern, completely blocking the flow of milk from the gland cistern to the teat canal. It is usually secondary to trauma or chronic mastitis. The cow has a full udder but zero milk can be stripped.",
        "Why_Not": "A leaky teat (free milker) is due to sphincter laxity, the exact opposite of an obstruction.",
        "Wow_Approach": "Treatment requires using a specialized instrument (like a Hug's teat tumor extractor or teat bistoury) inserted through the streak canal to physically cut and shred the membrane."
    },
    3870: {
        "topic": "Gut Tie (Pelvic Hernia) in Bullocks",
        "Core_Anatomy": "Bovine Peritoneal Cavity and Spermatic Cord.",
        "Pathogenesis_Immediate": "Gut Tie (Pelvic Hernia) is a specific internal hernia noticed in bullocks exclusively as a sequel to improper Castration by traction.",
        "Pathogenesis_Deep": "When castrating a bullock via traction (pulling the testicle until the cord snaps), the torn spermatic cord (ductus deferens) retracts back into the pelvic cavity. The free, torn end of the cord can loop around and adhere to the abdominal wall or abdominal organs, creating a rigid fibrous ring. A loop of the small intestine or descending colon eventually slips through this ring, becomes strangulated (incarcerated), and causes fatal intestinal necrosis.",
        "Why_Not": "A rumenotomy or urethrotomy is performed on the midline or perineum and does not involve the spermatic cord anatomy that drives a gut tie.",
        "Wow_Approach": "The classic clinical sign is 'stretching' where the steer holds its hind legs far backward to relieve the intense abdominal pain."
    },
    3871: {
        "topic": "Caslick's Operation - Pneumovagina",
        "Core_Anatomy": "Equine Vulva.",
        "Pathogenesis_Immediate": "Caslick's vulvoplasty is the surgical treatment of choice for 'wind-sucking' (Pneumovagina) in mares.",
        "Pathogenesis_Deep": "Mares with poor perineal conformation (e.g., older, thin, or postpartum mares where the vulva slopes forward or sits high relative to the pelvic floor) aspirate air into the vagina every time they walk (pneumovagina). This aspirated air carries fecal bacteria directly into the vagina and uterus, causing chronic endometritis and infertility. Caslick's operation involves removing a thin strip of mucous membrane from the dorsal margins of the vulvar lips and suturing them together, permanently sealing the upper portion of the vulva.",
        "Why_Not": "A simple vaginal prolapse requires a Buhner's suture or retention harness, not a Caslick's.",
        "Wow_Approach": "The mare MUST undergo a 'surgical reversal' (an episiotomy) to reopen the vulva before she is allowed to foal, otherwise the foal's head will violently tear the entire perineum."
    },
    3872: {
        "topic": "Urethral Calculi - Male Dog",
        "Core_Anatomy": "Canine Urethra (Os penis).",
        "Pathogenesis_Immediate": "The most common site of urethral calculi obstruction in the male dog is just behind the Os Penis.",
        "Pathogenesis_Deep": "The canine urethra runs inside a groove on the ventral aspect of the os penis (the bone inside the penis). Because this bone is completely rigid, the urethra at this exact spot cannot expand. When stones pass from the bladder into the urethra, they easily travel through the pelvic urethra but instantly get wedged right at the caudal entrance to the os penis groove.",
        "Why_Not": "The ischial arch is wide and flexible, allowing stones to pass easily.",
        "Wow_Approach": "To resolve this surgically without cutting the penis itself, a Scrotal Urethrostomy is performed. The scrotum is removed, and the wide, highly vascular pelvic urethra is sutured directly to the skin, creating a permanent new opening that is large enough to let future stones pass safely without obstructing."
    },
    3873: {
        "topic": "Typhlectomy",
        "Core_Anatomy": "Caecum.",
        "Pathogenesis_Immediate": "Surgical resection of the caecum is called a Typhlectomy.",
        "Pathogenesis_Deep": "This procedure is indicated for chronic caecal impaction, caecal inversion (intussusception into the colon), or severe necrotizing caecitis. The caecum is amputated close to the ileocecocal junction, and the stump is closed with a double-row inverting suture pattern.",
        "Why_Not": "Colotomy is incising the colon. Colectomy is resecting the colon. Enterotomy is incising the small intestine.",
        "Wow_Approach": "N/A"
    },
    3874: {
        "topic": "True/False Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a True or False section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3882: {
        "topic": "Gastropexy - GDV Prevention (Review)",
        "Core_Anatomy": "Stomach and Abdominal Wall.",
        "Pathogenesis_Immediate": "Gastropexy is performed to prevent the recurrence of GDV in dogs (TRUE).",
        "Pathogenesis_Deep": "Reiterating that anchoring the pyloric antrum to the right body wall prevents the stomach from ever twisting again.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3883: {
        "topic": "Match the Following Header",
        "Core_Anatomy": "N/A",
        "Pathogenesis_Immediate": "Header indicating a matching section.",
        "Pathogenesis_Deep": "Structural marker.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
    },
    3884: {
        "topic": "Colles' Fracture",
        "Core_Anatomy": "Distal Radius.",
        "Pathogenesis_Immediate": "A Colles' fracture is a specific fracture of the distal end of the radius.",
        "Pathogenesis_Deep": "Classically described in humans and occasionally used in veterinary orthopaedics to refer to a transverse fracture of the distal radial metaphysis with dorsal and cranial displacement of the distal fragment, usually caused by falling forward onto an extended limb.",
        "Why_Not": "N/A",
        "Wow_Approach": "N/A"
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
