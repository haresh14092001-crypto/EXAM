# Veterinary Exam Engine - OCR Pipeline Setup

## Quick Start

### 1. Install Dependencies
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Place Your PDFs
Copy your scanned university question papers into the `/pdfs` directory:
```
EXAM/
├── pdfs/
│   ├── clinical_medicine_2024.pdf
│   ├── surgery_2024.pdf
│   ├── theriogenology_2024.pdf
│   └── ... (more PDFs)
├── output/
├── scripts/
└── ...
```

### 3. Run the Pipeline
```powershell
python scripts/run_pipeline.py
```

## What Happens

### Phase 1: Docling OCR Conversion
- **Input:** Phone-scanned PDFs from `/pdfs`
- **Process:** Docling converts each PDF using layout-aware vision models
- **Output:** 
  - `{filename}_docling.json` — Full document structure with metadata
  - `{filename}_blocks.json` — Extracted text blocks (page, type, content, bbox)
  - `conversion_report.json` — Execution summary

**Why Docling?**
- Preserves spatial layout (tables, columns, hierarchies)
- Handles phone scans without hallucination
- Local vision models (no API calls, fully offline)

### Phase 2: Question Extraction
- **Input:** `*_blocks.json` from OCR output
- **Process:** Regex-based pattern matching to identify:
  - Question text (Q1: ...)
  - Options (a), b), c), d))
  - Answer keys (Answer: A)
- **Output:** `all_questions_raw.json` — Structured question array

**Example Output Structure:**
```json
{
  "questions": [
    {
      "type": "mcq",
      "question_number": "1",
      "question_text": "A cow with ketosis shows which enzyme deficiency?",
      "options": [
        {"label": "A", "text": "Pyruvate carboxylase"},
        {"label": "B", "text": "Glucose-6-phosphatase"},
        {"label": "C", "text": "Isocitrate dehydrogenase"},
        {"label": "D", "text": "Malic enzyme"}
      ],
      "answer_key": "A",
      "requires_enrichment": true
    }
  ]
}
```

### Phase 3: LLM Enrichment (Next Step)
The extracted questions are flagged as `requires_enrichment: true`. Next, we'll:
1. Parse `all_questions_raw.json`
2. Feed each question to Claude/GPT with the **Why-How-WhyNot-Wow** prompt
3. Enrich with:
   - **Core Anatomy:** Applied anatomy relevant to the condition
   - **Pathogenesis:** Immediate mechanism + deep biochemical pathway
   - **Comparative Mechanics:** Why presentation differs in other species
   - **Surgical/Medical Logic:** Why specific interventions work
4. Output to `database.json` (frontend-ready format)

## Directory Structure
```
EXAM/
├── pdfs/                          # Source scanned PDFs
├── output/                        # Docling & parsed output
│   ├── clinical_medicine_docling.json
│   ├── clinical_medicine_blocks.json
│   ├── all_questions_raw.json     # Raw extracted questions
│   └── conversion_report.json
├── scripts/
│   ├── ocr_pipeline.py            # Docling wrapper
│   ├── question_parser.py         # Question extractor
│   ├── run_pipeline.py            # Orchestrator
│   └── llm_enricher.py            # [WIP] LLM enrichment
├── src/                           # Frontend code (HTML, JS, CSS)
├── requirements.txt               # Python dependencies
├── database.json                  # Final enriched dataset
├── index.html                     # Web UI
└── README.md
```

## Troubleshooting

### "No PDF files found"
- Ensure PDFs are in `/pdfs` directory
- Check permissions on PDF files

### Docling import error
```
pip install --upgrade docling docling_core
```

### Slow OCR
- First PDF may be slow (model loading)
- Subsequent PDFs are faster
- For 50+ PDFs, expect 5-15 minutes depending on page count

### Memory issues
- Reduce batch size by processing PDFs individually
- Or process subdirectories separately

## Next: LLM Enrichment
After OCR completes, see `scripts/llm_enricher.py` to:
1. Load `all_questions_raw.json`
2. Apply Why-How-WhyNot-Wow enrichment
3. Generate `database.json` with clinical context
