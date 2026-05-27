@echo off
REM Veterinary Exam Engine - OCR Pipeline Setup Script
REM Automates venv creation, dependency installation, and initial pipeline run

echo.
echo ================================================
echo   Veterinary Exam Engine - OCR Pipeline Setup
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.10+ first.
    exit /b 1
)

echo [1/4] Creating virtual environment...
py -3 -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    exit /b 1
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
py -3 -m pip install --upgrade pip setuptools wheel >nul 2>&1
py -3 -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    exit /b 1
)

echo [4/4] Creating required directories...
if not exist "pdfs" mkdir pdfs
if not exist "output" mkdir output

echo.
echo ================================================
echo   ✓ Setup Complete!
echo ================================================
echo.
echo Next steps:
echo   1. Copy your scanned PDFs to: pdfs\
echo   2. Run the pipeline:
echo      python scripts/run_pipeline.py
echo.
echo For details, see: scripts\README_OCR_PIPELINE.md
echo.
