@echo off
REM Sports Tournament Registration System - Quick Start
REM This script sets up the virtual environment and runs the Streamlit app

echo.
echo ========================================
echo  Sports Tournament Registration System
echo  Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if .env exists
if not exist ".env" (
    echo.
    echo WARNING: .env file not found!
    echo Please copy .env.example to .env and update it with your Supabase credentials
    echo.
    pause
)

REM Run Streamlit app
echo.
echo Starting Streamlit application...
echo The app will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the application
echo.
streamlit run app.py

pause
