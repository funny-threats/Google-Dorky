# Feature Documentation

## 🔥 Full Power Features

### Comprehensive SQL Injection Payloads

The tool includes **100+ SQL injection payloads** organized by type:

- **Basic Payloads**: Standard injection vectors
- **Union-Based**: UNION SELECT attacks
- **Boolean-Based**: True/False blind injection
- **Time-Based**: Delayed response attacks
- **Error-Based**: Error message extraction
- **Stacked Queries**: Multiple query execution
- **Blind Injection**: Blind SQL injection techniques
- **Database-Specific**: MySQL, MSSQL, PostgreSQL, Oracle
- **WAF Bypass**: Advanced payloads to bypass firewalls
- **Encoded**: URL-encoded payloads

### SQLMap Integration

Automatic exploitation with SQLMap:

- **Auto-Detection**: Finds SQLMap installation automatically
- **Aggressive Mode**: Level 5, Risk 3 settings
- **Full Dumping**: Extracts all databases and tables
- **Multiple Techniques**: Uses all injection techniques (BEUSTQ)
- **WAF Bypass**: Includes tamper scripts
- **Parallel Processing**: Multi-threaded for speed

### Automated Workflow

1. **Proxy Collection**: Scrapes and validates proxies
2. **Google Search**: Searches with dork queries
3. **Vulnerability Detection**: Tests URLs with comprehensive payloads
4. **SQLMap Exploitation**: Automatically exploits vulnerable sites
5. **Database Extraction**: Downloads and parses database files
6. **Data Organization**: Structures all findings

## 🎯 Usage Modes

### Basic Mode
```bash
python main.py --dorks dorks.txt
```
- Standard payloads
- Basic vulnerability detection
- Manual exploitation required

### Aggressive Mode
```bash
python main.py --dorks dorks.txt --aggressive
```
- All payload types tested
- Maximum coverage
- Comprehensive detection

### Full Power Mode
```bash
python main.py --dorks dorks.txt --aggressive --use-sqlmap
```
- All payloads + SQLMap
- Automatic exploitation
- Database dumping
- Full automation

## 📊 Payload Categories

### 1. Basic Payloads (12 payloads)
Standard SQL injection vectors for quick detection.

### 2. Union-Based (10 payloads)
UNION SELECT attacks for data extraction.

### 3. Boolean-Based (10 payloads)
True/False blind injection techniques.

### 4. Time-Based (10 payloads)
Delayed response attacks (SLEEP, WAITFOR DELAY).

### 5. Error-Based (9 payloads)
Error message extraction (EXTRACTVALUE, UPDATEXML).

### 6. Database-Specific
- MySQL (6 payloads)
- MSSQL (6 payloads)
- PostgreSQL (5 payloads)
- Oracle (4 payloads)

### 7. WAF Bypass (14 payloads)
Advanced payloads designed to bypass web application firewalls.

### 8. Encoded (5 payloads)
URL-encoded payloads for special cases.

## 🔧 SQLMap Configuration

When using `--use-sqlmap`, the tool automatically configures SQLMap with:

```bash
--level 5          # Maximum testing level
--risk 3           # Maximum risk level
--dump-all         # Dump all databases
--threads 10       # Parallel processing
--technique BEUSTQ # All injection techniques
--tamper space2comment,charencode  # WAF bypass
--forms            # Test forms
--crawl 2          # Crawl depth
```

## 📈 Performance

### Speed Optimization
- Parallel proxy validation
- Multi-threaded SQLMap execution
- Efficient payload testing
- Smart URL filtering

### Resource Usage
- Moderate CPU usage
- Low memory footprint
- Network-intensive (uses proxies)

## 🛡️ Security Features

### Proxy Rotation
- Automatic proxy switching
- Failed proxy detection
- Speed-based selection

### Rate Limiting
- Built-in delays
- Respectful scanning
- Configurable timeouts

### Error Handling
- Graceful failures
- Retry mechanisms
- Comprehensive logging

## 📝 Output Formats

### Text Report (results.txt)
- Human-readable format
- Organized by category
- Summary statistics
- Detailed findings

### JSON Report (results.json)
- Machine-readable
- Complete data structure
- Easy parsing
- Integration-ready

### SQLMap Results
- Separate directory
- Per-URL results
- Database dumps
- Table extracts

## 🎓 Best Practices

1. **Start Small**: Test with `--max-urls 10` first
2. **Use Proxies**: Always use proxies for anonymity
3. **Be Patient**: Full scans can take hours
4. **Review Results**: Always verify findings manually
5. **Respect Limits**: Don't overload target servers

## ⚠️ Important Notes

- SQLMap requires significant time per URL
- Full scans can take 24+ hours
- Some payloads may trigger security alerts
- Always use on authorized systems only

## 🚀 Advanced Usage

### Custom Payloads
Edit `sqli_payloads.py` to add custom payloads.

### Custom SQLMap Options
Modify `sqlmap_integration.py` for custom SQLMap configuration.

### Integration
Use the JSON output to integrate with other tools.

## 📚 References

- [SQLMap Documentation](https://github.com/sqlmapproject/sqlmap/wiki)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
