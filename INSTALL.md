# Installation Guide

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection

## Installation Methods

### Method 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky

# Run setup script
chmod +x setup.sh
./setup.sh

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Method 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Method 3: Using pip (Development)

```bash
# Clone the repository
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky

# Install in development mode
pip install -e .
```

## Kali Linux Installation

```bash
# Update package list
sudo apt update

# Install Python and pip if not already installed
sudo apt install python3 python3-pip python3-venv -y

# Clone repository
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## Verification

After installation, verify everything works:

```bash
# Check Python version
python3 --version  # Should be 3.7 or higher

# Check if dependencies are installed
pip list | grep -E "requests|beautifulsoup4|selenium"

# Test the tool
python main.py --help
```

## Troubleshooting

### Import Errors

If you get import errors, make sure:
- Virtual environment is activated
- All dependencies are installed: `pip install -r requirements.txt`
- You're using Python 3.7 or higher

### Permission Errors

On Linux/macOS, if you get permission errors:
```bash
chmod +x setup.sh
chmod +x main.py
```

### Proxy Issues

If proxy scraping fails:
- Check your internet connection
- Some proxy sites may be blocked by your firewall
- Try using `--no-proxy` flag (not recommended)

## Updating

To update to the latest version:

```bash
cd Googledorky
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstallation

To remove the tool:

```bash
# Deactivate virtual environment if active
deactivate

# Remove the directory
rm -rf Googledorky
```
