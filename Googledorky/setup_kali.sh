#!/bin/bash
# Kali Linux Setup Script for Google Dork SQL Injection Scanner

echo "=========================================="
echo "Kali Linux Setup - Google Dork Scanner"
echo "=========================================="
echo ""

# Check if running on Kali Linux
if ! grep -q "Kali" /etc/os-release 2>/dev/null; then
    echo "[!] Warning: This script is optimized for Kali Linux"
    echo "[*] Continuing anyway..."
fi

# Update package list
echo "[*] Updating package list..."
sudo apt update -qq

# Install Python and pip if not already installed
echo "[*] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "[*] Installing Python 3..."
    sudo apt install -y python3 python3-pip python3-venv
fi

# Install SQLMap (required for full functionality)
echo "[*] Checking SQLMap installation..."
if ! command -v sqlmap &> /dev/null; then
    echo "[*] Installing SQLMap..."
    sudo apt install -y sqlmap
else
    echo "[+] SQLMap already installed"
fi

# Install additional tools
echo "[*] Installing additional dependencies..."
sudo apt install -y \
    git \
    curl \
    wget \
    build-essential \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev

# Create virtual environment
echo "[*] Creating virtual environment..."
python3 -m venv venv || { echo "[!] Failed to create virtual environment"; exit 1; }

# Activate virtual environment
echo "[*] Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "[*] Upgrading pip..."
pip install --upgrade pip --quiet

# Install Python requirements
echo "[*] Installing Python requirements..."
pip install -r requirements.txt || { echo "[!] Failed to install requirements"; exit 1; }

# Make scripts executable
echo "[*] Making scripts executable..."
chmod +x main.py setup.sh setup_github.sh verify_setup.py

# Verify SQLMap installation
echo "[*] Verifying SQLMap installation..."
if command -v sqlmap &> /dev/null; then
    SQLMAP_VERSION=$(sqlmap --version 2>/dev/null | head -1)
    echo "[+] SQLMap installed: $SQLMAP_VERSION"
else
    echo "[!] Warning: SQLMap not found in PATH"
    echo "[*] You may need to install it manually: sudo apt install sqlmap"
fi

# Create aliases for easy access
echo "[*] Creating aliases..."
cat >> ~/.bashrc << 'EOF'

# Google Dork SQL Injection Scanner Aliases
alias googledorky='cd /opt/Googledorky 2>/dev/null || cd ~/Googledorky 2>/dev/null; source venv/bin/activate'
alias gdscan='python main.py --dorks dorks.txt --aggressive --use-sqlmap'

EOF

echo ""
echo "[+] Setup complete!"
echo ""
echo "To use the tool:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run basic scan: python main.py --dorks dorks.txt"
echo "  3. Run aggressive scan with SQLMap: python main.py --dorks dorks.txt --aggressive --use-sqlmap"
echo ""
echo "Or use the aliases:"
echo "  googledorky  - Navigate to project and activate venv"
echo "  gdscan       - Run aggressive scan with SQLMap"
echo ""
echo "For full automation:"
echo "  python main.py --dorks dorks.txt --aggressive --use-sqlmap --max-proxies 50"
echo ""
