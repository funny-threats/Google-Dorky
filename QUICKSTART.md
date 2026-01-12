# Quick Start Guide

Get up and running with Google Dork SQL Injection Scanner in minutes!

## 🚀 Fastest Setup (3 Steps)

### 1. Clone & Setup
```bash
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky
./setup.sh
source venv/bin/activate
```

### 2. Run Your First Scan
```bash
python main.py --dorks dorks.txt
```

### 3. View Results
```bash
cat results.txt
```

That's it! 🎉

## 📝 Customize Your Dorks

Edit `dorks.txt` to add your own Google dorks:

```bash
nano dorks.txt
# or
vim dorks.txt
```

Add one dork per line:
```
inurl:index.php?id=
filetype:sql
inurl:database.sql
```

## 🎯 Common Use Cases

### Quick Test Run
```bash
python main.py --dorks dorks.txt --max-proxies 10 --skip-validation
```

### Full Scan with Many Proxies
```bash
python main.py --dorks dorks.txt --max-proxies 50
```

### Custom Output File
```bash
python main.py --dorks dorks.txt --output my_scan_results.txt
```

### Without Proxies (Not Recommended)
```bash
python main.py --dorks dorks.txt --no-proxy
```

## 📊 Understanding Output

After running, you'll get:

1. **results.txt** - Human-readable report
2. **results.json** - Machine-readable data
3. **downloads/** - Any database files found

## 🔧 Troubleshooting

**Problem**: "No module named 'requests'"
```bash
pip install -r requirements.txt
```

**Problem**: "Permission denied"
```bash
chmod +x setup.sh main.py
```

**Problem**: "No proxies found"
- Check internet connection
- Try `--no-proxy` flag (not recommended)
- Wait a few minutes and try again

## 📚 Next Steps

- Read [README.md](README.md) for full documentation
- Check [INSTALL.md](INSTALL.md) for detailed installation
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## ⚠️ Remember

- Only use on authorized systems
- Always verify findings manually
- Respect rate limits
- Use responsibly!

Happy hunting! 🐛💰
