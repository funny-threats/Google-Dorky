#!/bin/bash
# Quick script to link repository to GitHub

echo "=========================================="
echo "GitHub Repository Linker"
echo "=========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "[!] Git is not installed."
    echo "[*] Please install Git first:"
    echo "    Mac: xcode-select --install"
    echo "    Or download from: https://git-scm.com/downloads"
    exit 1
fi

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "[*] Initializing git repository..."
    git init
    echo "[+] Git repository initialized"
fi

# Get GitHub username
echo ""
read -p "Enter your GitHub username: " GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "[!] Username cannot be empty"
    exit 1
fi

# Get repository name
read -p "Enter repository name (default: Googledorky): " REPO_NAME
REPO_NAME=${REPO_NAME:-Googledorky}

# Check if remote already exists
if git remote get-url origin &> /dev/null; then
    echo ""
    echo "[!] Remote 'origin' already exists:"
    git remote -v
    echo ""
    read -p "Do you want to replace it? (y/n): " REPLACE
    if [ "$REPLACE" = "y" ] || [ "$REPLACE" = "Y" ]; then
        git remote remove origin
    else
        echo "[*] Keeping existing remote"
        exit 0
    fi
fi

# Choose authentication method
echo ""
echo "Choose authentication method:"
echo "1) HTTPS (easier, requires token)"
echo "2) SSH (more secure, requires SSH key)"
read -p "Enter choice (1 or 2): " AUTH_CHOICE

if [ "$AUTH_CHOICE" = "2" ]; then
    REMOTE_URL="git@github.com:${GITHUB_USERNAME}/${REPO_NAME}.git"
    echo "[*] Using SSH authentication"
else
    REMOTE_URL="https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"
    echo "[*] Using HTTPS authentication"
fi

# Add remote
echo ""
echo "[*] Adding remote..."
git remote add origin "$REMOTE_URL"

# Verify
echo ""
echo "[+] Remote added successfully!"
echo ""
echo "Remote configuration:"
git remote -v
echo ""

# Check if repository exists on GitHub
echo ""
echo "[*] Next steps:"
echo "1. Create the repository on GitHub:"
echo "   https://github.com/new"
echo "   Name: $REPO_NAME"
echo "   (Don't initialize with README)"
echo ""
echo "2. Then run:"
echo "   git add ."
echo "   git commit -m 'Initial commit'"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""

# Ask if user wants to set up git config
read -p "Do you want to configure git user.name and user.email? (y/n): " CONFIG_GIT
if [ "$CONFIG_GIT" = "y" ] || [ "$CONFIG_GIT" = "Y" ]; then
    read -p "Enter your name: " USER_NAME
    read -p "Enter your email: " USER_EMAIL
    git config --global user.name "$USER_NAME"
    git config --global user.email "$USER_EMAIL"
    echo "[+] Git configured"
fi

echo ""
echo "[+] Setup complete!"
echo ""
echo "To link Cursor to GitHub:"
echo "1. Open Cursor Settings (Cmd+,)"
echo "2. Search for 'GitHub'"
echo "3. Click 'Sign in with GitHub'"
echo "4. Authorize in browser"
echo ""
