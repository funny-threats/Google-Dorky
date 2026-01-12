# GitHub Repository Setup Guide

This guide will help you set up this project as a GitHub repository.

## Step 1: Initialize Git Repository

```bash
# If not already initialized
git init
```

Or use the automated script:
```bash
chmod +x setup_github.sh
./setup_github.sh
```

## Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository named `Googledorky` (or your preferred name)
3. **Do NOT** initialize with README, .gitignore, or license (we already have these)
4. Click "Create repository"

## Step 3: Add Remote and Push

### Using HTTPS:
```bash
git remote add origin https://github.com/YOUR_USERNAME/Googledorky.git
git branch -M main
git add .
git commit -m "Initial commit: Google Dork SQL Injection Scanner"
git push -u origin main
```

### Using SSH:
```bash
git remote add origin git@github.com:YOUR_USERNAME/Googledorky.git
git branch -M main
git add .
git commit -m "Initial commit: Google Dork SQL Injection Scanner"
git push -u origin main
```

## Step 4: Verify Repository

Visit your repository on GitHub:
```
https://github.com/YOUR_USERNAME/Googledorky
```

You should see:
- ✅ All project files
- ✅ README.md displayed
- ✅ LICENSE file
- ✅ Proper project structure

## Step 5: Configure Repository Settings

### Enable GitHub Actions
1. Go to Settings → Actions → General
2. Enable "Allow all actions and reusable workflows"
3. Save changes

### Add Topics (Optional)
Go to the repository main page → click the gear icon → Topics → Add:
- `security`
- `pentesting`
- `bug-bounty`
- `sql-injection`
- `google-dork`
- `python`

### Add Description
Add a description: "Automated Google Dork SQL Injection Scanner for Bug Bounty Hunting"

## Step 6: Create First Release (Optional)

1. Go to Releases → Create a new release
2. Tag: `v1.0.0`
3. Title: `Initial Release`
4. Description: Copy from README.md features section
5. Publish release

## Troubleshooting

### Authentication Issues
If you get authentication errors:
```bash
# For HTTPS, use GitHub CLI or Personal Access Token
gh auth login

# Or configure Git credentials
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Push Rejected
If push is rejected:
```bash
# Pull first (if repository was initialized on GitHub)
git pull origin main --allow-unrelated-histories

# Then push
git push -u origin main
```

### Large Files
If you have large files:
```bash
# Check file sizes
du -sh *

# Add to .gitignore if needed
echo "large_file.zip" >> .gitignore
```

## Next Steps

- ✅ Set up branch protection rules (Settings → Branches)
- ✅ Enable issues and discussions
- ✅ Add collaborators (Settings → Collaborators)
- ✅ Configure GitHub Pages (if needed)
- ✅ Set up GitHub Actions workflows

## Repository Checklist

- [ ] Git repository initialized
- [ ] GitHub repository created
- [ ] Remote added and pushed
- [ ] README displays correctly
- [ ] LICENSE file present
- [ ] .gitignore configured
- [ ] All files committed
- [ ] GitHub Actions enabled
- [ ] Topics added
- [ ] Description added

Your repository is now ready! 🎉
