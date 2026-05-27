from pathlib import Path
import json
import time
import argparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


PDFS_DIR = Path("pdfs")
OUT_DIR = Path("output")
OUT_DIR.mkdir(exist_ok=True)


def already_processed(stem: str) -> bool:
    return (OUT_DIR / f"{stem}_blocks.json").exists() or (OUT_DIR / f"{stem}_docling.json").exists()


def process_pdf_worker(pdf_path_str: str) -> tuple:
    """Worker run inside a process: performs OCR for a single PDF and writes output."""
    from rapidocr import RapidOCR
    from rapidocr.utils.typings import EngineType
    from pypdfium2 import PdfDocument

    pdf_path = Path(pdf_path_str)
    stem = pdf_path.stem
    out_blocks = OUT_DIR / f"{stem}_blocks.json"
    if already_processed(stem):
        return (stem, "skipped")

    # Configure RapidOCR to prefer the torch engine, but gracefully fall back
    # to an OpenCV-based engine if torch isn't available on the system.
    params = {"Det.engine_type": EngineType.TORCH, "Cls.engine_type": EngineType.TORCH, "Rec.engine_type": EngineType.TORCH}
    try:
        ocr = RapidOCR(params=params)
    except ImportError as e:
        # torch not present — try OpenCV engines which are CPU-friendly
        try:
            # Some RapidOCR builds may not expose alternative EngineType members;
            # fall back to default constructor which will auto-select available
            # CPU-friendly engines when torch is unavailable.
            print(f"RapidOCR: falling back to default engine selection due to: {e}")
            ocr = RapidOCR()
        except Exception as e2:
            return (stem, f"ocr_init_error:{e2}")

    result = {"file": str(pdf_path), "pages": []}
    start = time.time()
    try:
        with PdfDocument(str(pdf_path)) as doc:
            for page_idx, page in enumerate(doc):
                try:
                    bitmap = page.render(scale=2)
                    arr = bitmap.to_numpy()
                    ocr_out = ocr(arr)

                    texts = []
                    boxes = []
                    scores = []

                    if hasattr(ocr_out, "txts") and ocr_out.txts is not None:
                        for i, txt in enumerate(ocr_out.txts):
                            score = None
                            if hasattr(ocr_out, "scores") and ocr_out.scores:
                                try:
                                    score = float(ocr_out.scores[i])
                                except Exception:
                                    score = None

                            box = None
                            if hasattr(ocr_out, "boxes") and ocr_out.boxes is not None:
                                try:
                                    b = ocr_out.boxes[i]
                                    xs = [float(p[0]) for p in b]
                                    ys = [float(p[1]) for p in b]
                                    box = [min(xs), min(ys), max(xs), max(ys)]
                                except Exception:
                                    box = None

                            texts.append(txt)
                            boxes.append(box)
                            scores.append(score)

                    page_entry = {"page_number": page_idx + 1, "texts": texts, "boxes": boxes, "scores": scores}
                    result["pages"].append(page_entry)

                except Exception as e:
                    # record page error and continue
                    result["pages"].append({"page_number": page_idx + 1, "error": str(e)})
    except Exception as e:
        return (stem, f"error:{e}")

    elapsed = time.time() - start
    try:
        with open(out_blocks, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)
        return (stem, f"done:{elapsed:.1f}")
    except Exception as e:
        return (stem, f"write_error:{e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", "-w", type=int, default=max(1, (os.cpu_count() or 2) - 1), help="Number of parallel worker processes")
    args = parser.parse_args()

    pdfs = sorted(PDFS_DIR.rglob("*.pdf"))
    if not pdfs:
        print("No PDFs found under pdfs/")
        return

    # Build list of PDFs that still need processing
    remaining = [str(p) for p in pdfs if not already_processed(p.stem)]
    print(f"Found {len(pdfs)} PDFs, {len(remaining)} remaining to process — workers={args.workers}")

    if not remaining:
        print("Nothing to do — all PDFs already processed.")
        return

    # Use a thread pool on Windows to avoid spawn/import issues with native
    # OCR libraries in child processes. Threads share the interpreter and
    # installed packages, preventing ModuleNotFoundError for packages like
    # `rapidocr` when using ProcessPoolExecutor on some systems.
    with ThreadPoolExecutor(max_workers=args.workers) as exe:
        futures = {exe.submit(process_pdf_worker, p): p for p in remaining}
        completed = 0
        for fut in as_completed(futures):
            stem, status = fut.result()
            completed += 1
            print(f"[{completed}/{len(remaining)}] {stem}: {status}")


if __name__ == "__main__":
    main()
