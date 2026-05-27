#!/usr/bin/env pwsh
# Veterinary Exam Engine - OCR Pipeline Setup (PowerShell)
# Works on Windows, macOS, and Linux

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "   Veterinary Exam Engine - OCR Pipeline Setup" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed (try 'python' first, then 'py' launcher)
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonVersion = python --version 2>&1
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonVersion = py --version 2>&1
} else {
    Write-Host "ERROR: Python not found. Please install Python 3.10+" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green

# Create virtual environment (use 'py' launcher where available)
Write-Host "[1/4] Creating virtual environment..." -ForegroundColor Yellow
if (Get-Command python -ErrorAction SilentlyContinue) {
    python -m venv venv
} else {
    py -3 -m venv venv
}
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to create virtual environment" -ForegroundColor Red
    exit 1
}

# Activate virtual environment
Write-Host "[2/4] Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Install dependencies using the venv's pip via the launcher to avoid PATH issues
Write-Host "[3/4] Installing dependencies..." -ForegroundColor Yellow
if (Get-Command python -ErrorAction SilentlyContinue) {
    python -m pip install --upgrade pip setuptools wheel
    python -m pip install -r requirements.txt
} else {
    py -3 -m pip install --upgrade pip setuptools wheel
    py -3 -m pip install -r requirements.txt
}
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Create required directories
Write-Host "[4/4] Creating required directories..." -ForegroundColor Yellow
@("pdfs", "output") | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -ItemType Directory -Path $_ -Force | Out-Null
    }
}

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "   ✓ Setup Complete!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Copy your scanned PDFs to: pdfs\" -ForegroundColor White
Write-Host "  2. Run the pipeline:" -ForegroundColor White
Write-Host "     python scripts/run_pipeline.py" -ForegroundColor Yellow
Write-Host ""
Write-Host "For details, see: scripts\README_OCR_PIPELINE.md" -ForegroundColor Gray
Write-Host ""
