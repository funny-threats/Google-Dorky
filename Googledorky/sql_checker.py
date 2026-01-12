"""
SQL Injection Vulnerability Checker Module
Checks URLs for potential SQL injection vulnerabilities with comprehensive payloads
"""

import requests
from typing import List, Dict, Optional
import re
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from fake_useragent import UserAgent
import time
from sqli_payloads import SQLIPayloads

class SQLChecker:
    def __init__(self, proxy: Optional[Dict] = None, aggressive: bool = True):
        self.proxy = proxy
        self.ua = UserAgent()
        self.session = requests.Session()
        self.vulnerable_urls = []
        self.aggressive = aggressive
        
        # Load comprehensive payloads
        payload_loader = SQLIPayloads()
        if aggressive:
            # Use aggressive payloads for maximum coverage
            self.payloads = payload_loader.get_aggressive_payloads()
        else:
            # Use basic payloads for quick scan
            self.payloads = payload_loader.get_payloads_by_type('basic')
        
    def setup_proxy(self, proxy: Optional[Dict] = None):
        """Setup proxy for requests"""
        if proxy:
            self.proxy = proxy
            proxy_url = f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}"
            self.session.proxies = {
                'http': proxy_url,
                'https': proxy_url
            }
        else:
            self.session.proxies = {}
    
    def get_headers(self):
        """Generate headers"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
    
    def check_sql_error(self, response_text: str) -> bool:
        """Check if response contains SQL error messages"""
        sql_errors = [
            r"SQL syntax.*MySQL",
            r"Warning.*\Wmysql_",
            r"MySQLSyntaxErrorException",
            r"valid MySQL result",
            r"MySqlClient\.",
            r"PostgreSQL.*ERROR",
            r"Warning.*\Wpg_",
            r"valid PostgreSQL result",
            r"Npgsql\.",
            r"Oracle error",
            r"Oracle.*Driver",
            r"Warning.*\Woci_",
            r"Warning.*\Wora_",
            r"Microsoft SQL Server",
            r"ODBC SQL Server Driver",
            r"OLE DB.*SQL Server",
            r"Microsoft SQL Native Client error",
            r"SQLServer JDBC Driver",
            r"SQLException",
            r"SQLite.*error",
            r"SQLite3::",
            r"Warning.*\Wsqlite_",
            r"Warning.*\Wsqlite3_",
            r"SQLSTATE\[",
            r"PostgreSQL.*ERROR",
            r"Warning.*\Wpg_",
            r"valid PostgreSQL result",
        ]
        
        for error_pattern in sql_errors:
            if re.search(error_pattern, response_text, re.IGNORECASE):
                return True
        return False
    
    def test_url(self, url: str) -> Optional[Dict]:
        """Test a URL for SQL injection vulnerabilities"""
        try:
            parsed = urlparse(url)
            query_params = parse_qs(parsed.query)
            
            if not query_params:
                return None
            
            # Test each parameter with all payloads (or subset if not aggressive)
            # Optimize: test fewer payloads initially, expand if needed
            if self.aggressive:
                # In aggressive mode, test more payloads but prioritize
                priority_payloads = self.payloads[:20]  # Test top 20 first
                payloads_to_test = priority_payloads
            else:
                payloads_to_test = self.payloads[:5]  # Quick test with 5 payloads
            
            for param_name in query_params.keys():
                for payload in payloads_to_test:
                    try:
                        # Create test URL with payload
                        test_params = parse_qs(parsed.query)
                        test_params[param_name] = [payload]
                        test_query = urlencode(test_params, doseq=True)
                        test_url = urlunparse((
                            parsed.scheme,
                            parsed.netloc,
                            parsed.path,
                            parsed.params,
                            test_query,
                            parsed.fragment
                        ))
                        
                        response = self.session.get(
                            test_url,
                            headers=self.get_headers(),
                            timeout=5,  # Reduced timeout for speed
                            allow_redirects=False
                        )
                        
                        if self.check_sql_error(response.text):
                            return {
                                'url': url,
                                'vulnerable_param': param_name,
                                'payload': payload,
                                'status_code': response.status_code,
                                'vulnerable': True
                            }
                        
                        # Reduced delay for speed
                        time.sleep(0.1)
                        
                    except Exception:
                        continue
            
        except Exception as e:
            pass
        
        return None
    
    def check_urls(self, urls: List[str], proxy: Optional[Dict] = None) -> List[Dict]:
        """Check multiple URLs for SQL injection with progress tracking"""
        vulnerable = []
        
        if proxy:
            self.setup_proxy(proxy)
        
        from concurrent.futures import ThreadPoolExecutor, as_completed
        from tqdm import tqdm
        
        # Use threading for faster checking (limited to avoid overwhelming)
        max_workers = min(10, len(urls))
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_url = {executor.submit(self.test_url, url): url for url in urls}
            
            # Process with progress bar
            with tqdm(total=len(urls), desc="Testing URLs", unit="url", ncols=80) as pbar:
                for future in as_completed(future_to_url):
                    url = future_to_url[future]
                    try:
                        result = future.result()
                        if result:
                            vulnerable.append(result)
                    except Exception as e:
                        pass
                    finally:
                        pbar.update(1)
        
        return vulnerable
