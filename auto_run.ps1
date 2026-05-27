# Minimal automation: install and run OCR pipeline using the Python launcher 'py'
# Uses --user installs to avoid requiring admin or venv activation

if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Python launcher 'py' not found. Install Python or add launcher." -ForegroundColor Red
    exit 1
}

Write-Host "Installing Python dependencies (user install)..." -ForegroundColor Cyan
py -3 -m pip install --user --upgrade pip setuptools wheel
py -3 -m pip install --user -r requirements.txt

Write-Host "Running OCR pipeline..." -ForegroundColor Cyan
py -3 scripts/run_pipeline.py

Write-Host "\nAutomation complete. Check the output/ directory for results." -ForegroundColor Green
