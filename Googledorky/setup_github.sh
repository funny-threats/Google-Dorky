#!/bin/bash
# GitHub Repository Setup Script

echo "=========================================="
echo "GitHub Repository Setup"
echo "=========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "[!] Git is not installed. Please install git first."
    exit 1
fi

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "[*] Initializing git repository..."
    git init
    echo "[+] Git repository initialized"
else
    echo "[*] Git repository already initialized"
fi

# Add all files
echo "[*] Adding files to git..."
git add .

# Create initial commit
echo "[*] Creating initial commit..."
git commit -m "Initial commit: Google Dork SQL Injection Scanner

- Automated proxy scraping and validation
- Google search automation with dork queries
- SQL injection vulnerability detection
- Database file extraction and parsing
- Comprehensive result organization"

echo ""
echo "[+] Git repository setup complete!"
echo ""
echo "Next steps to push to GitHub:"
echo "1. Create a new repository on GitHub (https://github.com/new)"
echo "2. Run the following commands:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/Googledorky.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "Or use SSH:"
echo "   git remote add origin git@github.com:YOUR_USERNAME/Googledorky.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
