#!/usr/bin/env python3
"""
Verification script to check if the project is properly set up
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ Missing: {description} ({filepath})")
        return False

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python 3.7+ required. Current: {version.major}.{version.minor}.{version.micro}")
        return False

def main():
    print("=" * 60)
    print("Google Dork SQL Injection Scanner - Setup Verification")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check Python version
    print("Checking Python version...")
    all_good = check_python_version() and all_good
    print()
    
    # Check core files
    print("Checking core files...")
    core_files = [
        ("main.py", "Main script"),
        ("proxy_scraper.py", "Proxy scraper module"),
        ("proxy_validator.py", "Proxy validator module"),
        ("google_searcher.py", "Google searcher module"),
        ("sql_checker.py", "SQL checker module"),
        ("database_downloader.py", "Database downloader module"),
        ("data_organizer.py", "Data organizer module"),
    ]
    
    for filepath, description in core_files:
        all_good = check_file_exists(filepath, description) and all_good
    print()
    
    # Check configuration files
    print("Checking configuration files...")
    config_files = [
        ("requirements.txt", "Requirements file"),
        ("dorks.txt", "Dorks file"),
        (".gitignore", "Git ignore file"),
        ("LICENSE", "License file"),
        ("README.md", "README file"),
    ]
    
    for filepath, description in config_files:
        all_good = check_file_exists(filepath, description) and all_good
    print()
    
    # Check documentation files
    print("Checking documentation files...")
    doc_files = [
        ("QUICKSTART.md", "Quick start guide"),
        ("INSTALL.md", "Installation guide"),
        ("CONTRIBUTING.md", "Contributing guide"),
        ("SECURITY.md", "Security policy"),
    ]
    
    for filepath, description in doc_files:
        check_file_exists(filepath, description)
    print()
    
    # Check GitHub files
    print("Checking GitHub files...")
    github_files = [
        (".github/workflows/python-app.yml", "GitHub Actions workflow"),
        (".github/ISSUE_TEMPLATE/bug_report.md", "Bug report template"),
        (".github/ISSUE_TEMPLATE/feature_request.md", "Feature request template"),
    ]
    
    for filepath, description in github_files:
        check_file_exists(filepath, description)
    print()
    
    # Final summary
    print("=" * 60)
    if all_good:
        print("✅ All core files present! Project is ready to use.")
        print()
        print("Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run the scanner: python main.py --dorks dorks.txt")
        print("3. Set up GitHub: ./setup_github.sh")
    else:
        print("❌ Some files are missing. Please check the errors above.")
    print("=" * 60)

if __name__ == "__main__":
    main()
