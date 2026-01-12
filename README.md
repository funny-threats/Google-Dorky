# Google Dork SQL Injection Scanner 🔍

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated penetration testing tool for bug bounty hunting that scrapes proxies, searches Google with dorks, identifies SQL injection vulnerabilities, and extracts database files.

## ⚠️ Legal Disclaimer

**This tool is intended for legitimate bug bounty programs and authorized penetration testing only.**

- Only use on systems you own or have explicit written permission to test
- Unauthorized access to computer systems is illegal
- Always comply with applicable laws and regulations
- Respect rate limits and terms of service
- Users are solely responsible for their actions

## ✨ Features

- **🔄 Proxy Scraping**: Automatically scrapes free proxy websites from multiple sources
- **✅ Proxy Validation**: Validates and rotates proxies for reliability
- **🔎 Google Search Automation**: Searches Google with custom dork queries using proxies
- **💉 SQL Injection Detection**: Comprehensive payload testing with 100+ injection vectors
- **🔥 SQLMap Integration**: Automatic exploitation with SQLMap for vulnerable sites
- **💾 Database Extraction**: Downloads and parses database files found in search results
- **📊 Data Organization**: Organizes results into structured text and JSON files
- **🎯 Comprehensive Dork Library**: Includes extensive collection of Google dorks
- **⚡ Full Automation**: End-to-end automated scanning and exploitation
- **🛡️ WAF Bypass**: Advanced payloads designed to bypass web application firewalls
- **📈 Aggressive Mode**: Maximum coverage with all payload types and techniques

## 📋 Requirements

- Python 3.7 or higher
- Internet connection
- (Optional) Virtual environment for isolated installation
- **SQLMap** (for automatic exploitation) - Install with: `sudo apt install sqlmap` (Kali Linux)

## 🚀 Quick Start

### Quick Test (Verify Installation)
```bash
python quick_test.py
```

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky

# Run setup script
chmod +x setup.sh
./setup.sh

# Activate virtual environment
source venv/bin/activate

# Run the scanner
python main.py --dorks dorks.txt
```

### Option 2: Manual Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky

# Install dependencies
pip install -r requirements.txt

# Run the scanner
python main.py --dorks dorks.txt
```

## Usage

### Basic Usage

```bash
python main.py --dorks dorks.txt
```

### Advanced Options

```bash
# Use specific number of proxies
python main.py --dorks dorks.txt --max-proxies 50

# Run without proxies (not recommended)
python main.py --dorks dorks.txt --no-proxy

# Skip proxy validation for faster execution
python main.py --dorks dorks.txt --skip-validation

# Specify custom output file
python main.py --dorks dorks.txt --output my_results.txt
```

### Command Line Arguments

- `--dorks, -d`: Path to dorks file (default: `dorks.txt`)
- `--max-proxies, -p`: Maximum number of proxies to use (default: 20)
- `--no-proxy`: Run without proxies (not recommended)
- `--output, -o`: Output file for results (default: `results.txt`)
- `--skip-validation`: Skip proxy validation (faster but less reliable)
- `--aggressive, -a`: Use aggressive SQL injection testing with all payloads
- `--use-sqlmap, -s`: Automatically use SQLMap on vulnerable URLs (requires SQLMap)
- `--sqlmap-path`: Path to SQLMap (auto-detected if not specified)
- `--max-urls`: Maximum number of URLs to test (default: unlimited)

### Full Power Mode (Kali Linux)

For maximum database extraction and exploitation:

```bash
python main.py --dorks dorks.txt --aggressive --use-sqlmap --max-proxies 50
```

This enables:
- ✅ Comprehensive payload testing (100+ payloads)
- ✅ Automatic SQLMap exploitation
- ✅ Database dumping
- ✅ Table extraction
- ✅ Full data extraction

## Dorks File Format

Create a `dorks.txt` file with one Google dork per line. Lines starting with `#` are treated as comments.

Example:
```
# SQL Injection vulnerable parameters
inurl:index.php?id=
inurl:page.php?id=

# Database files
filetype:sql
filetype:db
```

A sample `dorks.txt` file is included with common SQL injection and database discovery dorks.

## Output

The tool generates two output files:

1. **results.txt**: Human-readable formatted report with:
   - Summary statistics
   - Vulnerable URLs with details
   - Downloaded database files
   - Extracted data organized by table

2. **results.json**: Machine-readable JSON format with all data

## Important Notes

⚠️ **Legal and Ethical Use Only**

- This tool is intended for **legitimate bug bounty programs** and **authorized penetration testing** only
- Only use on systems you own or have explicit written permission to test
- Unauthorized access to computer systems is illegal
- Always comply with applicable laws and regulations
- Respect rate limits and terms of service

## How It Works

1. **Proxy Scraping**: Scrapes multiple free proxy websites to collect proxy lists
2. **Proxy Validation**: Tests proxies for functionality and speed
3. **Google Search**: Uses proxies to search Google with each dork query
4. **URL Collection**: Extracts URLs from search results
5. **Vulnerability Testing**: Tests URLs for SQL injection vulnerabilities
6. **Database Discovery**: Identifies and downloads database files
7. **Data Extraction**: Parses SQL files and extracts structured data
8. **Report Generation**: Organizes all findings into formatted reports

## Project Structure

```
Googledorky/
├── main.py                      # Main orchestrator script
├── proxy_scraper.py             # Proxy scraping module
├── proxy_validator.py           # Proxy validation module
├── google_searcher.py           # Google search automation
├── sql_checker.py               # SQL injection vulnerability checker
├── database_downloader.py       # Database file downloader and parser
├── data_organizer.py            # Data organization and report generation
├── dorks.txt                    # Google dorks list
├── requirements.txt             # Python dependencies
├── pyproject.toml               # Python project configuration
├── setup.sh                     # Automated setup script
├── setup_github.sh              # GitHub repository setup script
├── Makefile                     # Makefile for common tasks
├── LICENSE                      # MIT License
├── README.md                    # This file
├── INSTALL.md                   # Detailed installation guide
├── CONTRIBUTING.md              # Contribution guidelines
├── SECURITY.md                  # Security policy
└── .github/                     # GitHub configuration
    ├── workflows/
    │   └── python-app.yml       # CI/CD workflow
    └── ISSUE_TEMPLATE/          # Issue templates
        ├── bug_report.md
        ├── feature_request.md
        └── config.yml
```

## Limitations

- Google may rate limit requests, even with proxies
- Free proxies may be unreliable or slow
- SQL injection detection is basic and may produce false positives/negatives
- Database parsing is limited to common SQL formats
- Always manually verify findings before reporting

## Troubleshooting

**No proxies found:**
- Check your internet connection
- Proxy websites may be down, try again later
- Use `--no-proxy` flag (not recommended)

**Rate limited by Google:**
- The tool includes delays between requests
- Try using more proxies with `--max-proxies`
- Wait longer between runs

**No results found:**
- Verify your dorks are correct
- Some dorks may not return results
- Try different dork combinations

## 🛠️ Development

### Using Makefile

```bash
make setup      # Full setup with virtual environment
make install    # Install dependencies
make run        # Run the scanner
make clean      # Clean temporary files
make help       # Show all commands
```

### Setting Up GitHub Repository

```bash
# Run the GitHub setup script
chmod +x setup_github.sh
./setup_github.sh

# Then create a repository on GitHub and push:
git remote add origin https://github.com/YOUR_USERNAME/Googledorky.git
git branch -M main
git push -u origin main
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Feel free to improve this tool by:
- Adding more proxy sources
- Improving SQL injection detection
- Enhancing database parsing
- Adding support for more file formats
- Improving documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔒 Security

For security concerns, please see [SECURITY.md](SECURITY.md).

## ⚠️ Disclaimer

This tool is provided for educational and authorized testing purposes only. Use responsibly and ethically.

The authors and contributors are not responsible for any misuse of this tool. Users are solely responsible for ensuring they have proper authorization before testing any systems.

## 📞 Support

- Open an issue for bug reports or feature requests
- Check [INSTALL.md](INSTALL.md) for installation help
- Review [Troubleshooting](#troubleshooting) section for common issues

## 🙏 Acknowledgments

- Thanks to all contributors
- Built for the bug bounty and security research community