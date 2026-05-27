from pathlib import Path
import time
from datetime import datetime

PDFS_DIR = Path("pdfs")
OUT_DIR = Path("output")


def total_pdfs():
    return len(list(PDFS_DIR.rglob("*.pdf")))


def processed_count():
    files = set()
    for p in OUT_DIR.glob("*_blocks.json"):
        files.add(p.stem.replace("_blocks", ""))
    for p in OUT_DIR.glob("*_docling.json"):
        files.add(p.stem.replace("_docling", ""))
    return len(files)


def main():
    total = total_pdfs()
    if total == 0:
        print("No PDFs found under pdfs/ — monitor exiting.")
        return

    print(f"Monitoring OCR progress: target {total} PDFs. Updates every 10 minutes.")
    while True:
        done = processed_count()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Completed {done}/{total} PDFs")
        if done >= total:
            print(f"All {total} PDFs processed — monitor exiting.")
            break
        time.sleep(600)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Monitor error:', e)
