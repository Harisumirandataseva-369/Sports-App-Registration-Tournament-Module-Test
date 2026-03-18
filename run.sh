#!/bin/bash

# Sports Tournament Registration System - Quick Start
# This script sets up the virtual environment and runs the Streamlit app

echo ""
echo "========================================"
echo " Sports Tournament Registration System"
echo " Quick Start"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if .env exists
if [ ! -f ".env" ]; then
    echo ""
    echo "WARNING: .env file not found!"
    echo "Please copy .env.example to .env and update it with your Supabase credentials"
    echo ""
    read -p "Press Enter to continue..."
fi

# Run Streamlit app
echo ""
echo "Starting Streamlit application..."
echo "The app will open in your browser at http://localhost:8501"
echo "Press Ctrl+C to stop the application"
echo ""
streamlit run app.py
