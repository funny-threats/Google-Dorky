#!/bin/bash
# Setup script for Google Dork SQL Injection Scanner

echo "=========================================="
echo "Google Dork SQL Injection Scanner Setup"
echo "=========================================="
echo ""

# Check Python version
echo "[*] Checking Python version..."
python3 --version || { echo "[!] Python 3 is required but not found. Please install Python 3.7+"; exit 1; }

# Create virtual environment
echo "[*] Creating virtual environment..."
python3 -m venv venv || { echo "[!] Failed to create virtual environment"; exit 1; }

# Activate virtual environment
echo "[*] Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "[*] Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "[*] Installing requirements..."
pip install -r requirements.txt || { echo "[!] Failed to install requirements"; exit 1; }

echo ""
echo "[+] Setup complete!"
echo ""
echo "To use the tool:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the scanner: python main.py --dorks dorks.txt"
echo ""
