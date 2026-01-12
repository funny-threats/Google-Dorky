# Linking Cursor to GitHub

## 🔗 Method 1: Cursor Settings (Recommended)

### Step 1: Open Cursor Settings
1. Press `Cmd + ,` (Mac) or `Ctrl + ,` (Windows/Linux)
2. Or go to: **Cursor → Settings** (Mac) or **File → Preferences → Settings** (Windows/Linux)

### Step 2: Sign in to GitHub
1. In Cursor settings, search for "GitHub"
2. Look for "GitHub Authentication" or "Source Control"
3. Click "Sign in with GitHub"
4. Authorize Cursor in your browser
5. You'll be redirected back to Cursor

### Step 3: Verify Connection
- Check the bottom status bar - you should see your GitHub username
- Or go to **View → Command Palette** → type "GitHub" to see available commands

## 🔗 Method 2: Command Palette

1. Press `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux)
2. Type: `GitHub: Sign in`
3. Follow the authentication flow
4. Authorize in browser
5. Return to Cursor

## 🔗 Method 3: Git Remote Setup

If you want to connect your local repository to GitHub:

### Step 1: Initialize Git (if not done)
```bash
cd /Users/64009257/Googledorky
git init
```

### Step 2: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `Googledorky` (or your preferred name)
3. **Don't** initialize with README (we already have one)
4. Click "Create repository"

### Step 3: Add Remote
```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/Googledorky.git

# Or use SSH (if you have SSH keys set up)
git remote add origin git@github.com:YOUR_USERNAME/Googledorky.git
```

### Step 4: Verify Remote
```bash
git remote -v
```

You should see:
```
origin  https://github.com/YOUR_USERNAME/Googledorky.git (fetch)
origin  https://github.com/YOUR_USERNAME/Googledorky.git (push)
```

## 📤 Push to GitHub

### First Time Setup
```bash
# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Google Dork SQL Injection Scanner

- Automated proxy scraping and validation
- Google search automation with dork queries
- SQL injection vulnerability detection
- SQLMap integration for automated exploitation
- Comprehensive payload library (100+ payloads)
- Database file extraction and parsing
- Professional UI with ASCII art graphics
- Full automation from search to exploitation"

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

### Future Updates
```bash
git add .
git commit -m "Your commit message"
git push
```

## 🔐 GitHub Authentication Methods

### Personal Access Token (PAT)
If you prefer using tokens:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Select scopes: `repo`, `workflow`
4. Copy the token
5. Use it when prompted for password

### SSH Keys (Recommended for Security)
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH and GPG keys → New SSH key
```

## ✅ Verify Connection

### In Cursor
- Check bottom status bar for GitHub icon
- Open Source Control panel (Ctrl/Cmd + Shift + G)
- You should see GitHub integration options

### Via Command Line
```bash
# Check git config
git config --global user.name
git config --global user.email

# Set if not configured
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 🎯 Quick Setup Script

Run this to set everything up:

```bash
cd /Users/64009257/Googledorky
chmod +x setup_github.sh
./setup_github.sh
```

Then follow the prompts to add your GitHub remote.

## 🔧 Troubleshooting

### "Git not found"
- Install Git: https://git-scm.com/downloads
- Or on Mac: `xcode-select --install`

### "Authentication failed"
- Check your GitHub credentials
- Try using Personal Access Token
- Or set up SSH keys

### "Remote already exists"
```bash
# Remove existing remote
git remote remove origin

# Add new remote
git remote add origin https://github.com/YOUR_USERNAME/Googledorky.git
```

### "Permission denied"
- Check repository permissions
- Ensure you're the owner or have write access
- Verify authentication method

## 📝 Next Steps

After linking:

1. ✅ Your code is synced with GitHub
2. ✅ You can use Cursor's GitHub features
3. ✅ Push/pull directly from Cursor
4. ✅ Create pull requests from Cursor
5. ✅ View issues and PRs in Cursor

## 🎉 You're All Set!

Your Cursor editor is now linked to GitHub and ready to use!
