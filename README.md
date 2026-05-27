# Veterinary Exam Engine

A lightweight, offline, searchable web application for studying veterinary board exam questions using an educational framework that emphasizes deep clinical understanding over rote memorization.

## 🎯 Objective
Prepare for 4th-year Veterinary University Board Exams (June 8) covering:
- **Clinical Medicine**
- **Veterinary Surgery**
- **Theriogenology (OG)**

## 📚 Educational Framework: "Why, How, Why Not, Wow"

Every high-yield question is reverse-engineered down to basic sciences using four distinct pillars:

1. **Core Anatomy (The Roots):** Applied, functional anatomy relevant to the condition
2. **Pathogenesis (How & How Deep):**
   - *Immediate:* Active clinical failure mechanism (e.g., oxaloacetate depletion in Ketosis)
   - *Deep:* Full cellular/biochemical pathways for long-term understanding
3. **Comparative Mechanics (Why Not):** Why the condition presents differently in other species
4. **Surgical/Medical Logic (The Wow):** Why specific interventions work and alternative routes fail

## 🔄 Project Phases

### Phase 1: Bulk OCR Ingestion ✓ READY
Convert scanned PDF question papers to structured JSON using **Docling** (IBM's layout-aware vision models).

**Setup & Usage:**
```powershell
# Windows PowerShell
.\setup.ps1

# Then copy PDFs to pdfs/ and run:
python scripts/run_pipeline.py
```

**Output:**
- `output/all_questions_raw.json` — Extracted MCQ questions ready for enrichment
- See `scripts/README_OCR_PIPELINE.md` for detailed documentation

### Phase 2: LLM Enrichment (WIP)
Parse raw questions and apply Why-How-WhyNot-Wow framework using LLM.

### Phase 3: Frontend UI (TBD)
Interactive accordion-based exam viewer with search/filter functionality.

## 📁 Project Structure

```
EXAM/
├── pdfs/                      # Source: Scanned exam PDFs
├── output/                    # Generated: Docling JSON + parsed questions
├── scripts/
│   ├── ocr_pipeline.py        # Docling OCR wrapper
│   ├── question_parser.py     # Question extraction logic
│   ├── run_pipeline.py        # Full orchestrator
│   ├── llm_enricher.py        # [WIP] Enrichment pipeline
│   └── README_OCR_PIPELINE.md # Detailed OCR setup guide
├── src/                       # Frontend application
├── database.json              # Final enriched dataset (output)
├── index.html                 # Web UI (vanilla JS + Tailwind CDN)
├── requirements.txt           # Python dependencies
├── setup.bat / setup.ps1      # Automated setup scripts
└── README.md                  # This file
```

## ⚙️ Tech Stack

**Backend (Data Processing):**
- **Docling** — Layout-aware PDF → JSON conversion (no hallucination, preserves tables/lists)
- **Python 3.10+** — Orchestration and enrichment pipeline

**Frontend (UI):**
- **Vanilla JavaScript** — No frameworks, zero dependencies
- **Tailwind CSS** (CDN) — Responsive styling
- **index.html** — Single-file offline application
- Reads from `database.json` locally

## 🚀 Quick Start

1. **Clone & Setup:**
   ```powershell
   cd EXAM
   .\setup.ps1
   ```

2. **Add Your PDFs:**
   - Copy scanned exam papers to `pdfs/` directory

3. **Run OCR Pipeline:**
   ```powershell
   python scripts/run_pipeline.py
   ```

4. **View Results:**
   - Check `output/all_questions_raw.json` for extracted questions
   - Check `output/conversion_report.json` for statistics

## 📋 Design Principles

✅ **Separation of Concerns:**
- Data (`database.json`) strictly decoupled from UI (`index.html`)
- Modular Python scripts with clear responsibilities

✅ **Zero Hallucination Tolerance:**
- Medical/surgical/biochemical content must be rigorously accurate
- Veterinary terminology exact and verified

✅ **Offline-First:**
- Works entirely offline after setup
- No API dependencies for exam viewing
- PDF processing happens locally

✅ **Clean Code:**
- Vanilla JS (no Node.js dependencies)
- Tailwind via CDN only
- Python follows PEP 8 conventions

## 📖 Documentation

- **OCR Pipeline:** [`scripts/README_OCR_PIPELINE.md`](scripts/README_OCR_PIPELINE.md)
- **Docling Repo:** [https://github.com/docling-project/docling.git](https://github.com/docling-project/docling.git)

## 🔗 Repository

GitHub: `https://github.com/haresh14092001-crypto/EXAM.git`

## 📅 Timeline

- **May 26:** Phase 1 OCR pipeline ready ✓
- **By June:** Phase 2 & 3 (Enrichment + UI)
- **June 8:** Exam day