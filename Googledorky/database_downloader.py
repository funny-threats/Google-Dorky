"""
Database Downloader and Parser Module
Downloads and parses database files/links found
"""

import requests
from typing import List, Dict, Optional
import re
import os
from urllib.parse import urlparse
from fake_useragent import UserAgent
import json
import csv
import time

class DatabaseDownloader:
    def __init__(self, proxy: Optional[Dict] = None, output_dir: str = "downloads"):
        self.proxy = proxy
        self.ua = UserAgent()
        self.session = requests.Session()
        self.output_dir = output_dir
        self.downloaded_files = []
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
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
            'Accept': '*/*',
        }
    
    def is_database_url(self, url: str) -> bool:
        """Check if URL points to a database file"""
        db_extensions = ['.sql', '.db', '.sqlite', '.sqlite3', '.mdb', '.accdb', '.dbf']
        db_keywords = ['database', 'dump', 'backup', 'sql', 'db']
        
        url_lower = url.lower()
        parsed = urlparse(url)
        path = parsed.path.lower()
        
        # Check extension
        for ext in db_extensions:
            if path.endswith(ext):
                return True
        
        # Check keywords in path
        for keyword in db_keywords:
            if keyword in path:
                return True
        
        return False
    
    def download_file(self, url: str) -> Optional[str]:
        """Download a file from URL"""
        try:
            response = self.session.get(
                url,
                headers=self.get_headers(),
                timeout=30,
                stream=True
            )
            
            if response.status_code == 200:
                # Determine filename
                parsed = urlparse(url)
                filename = os.path.basename(parsed.path) or "downloaded_file"
                
                # Ensure unique filename
                filepath = os.path.join(self.output_dir, filename)
                counter = 1
                while os.path.exists(filepath):
                    name, ext = os.path.splitext(filename)
                    filepath = os.path.join(self.output_dir, f"{name}_{counter}{ext}")
                    counter += 1
                
                # Download file
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                return filepath
                
        except Exception as e:
            print(f"[!] Error downloading {url}: {e}")
        
        return None
    
    def parse_sql_file(self, filepath: str) -> List[Dict]:
        """Parse SQL file and extract data"""
        data = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
                # Extract INSERT statements
                insert_pattern = r'INSERT\s+INTO\s+(\w+)\s*\([^)]+\)\s*VALUES\s*\([^)]+\)'
                matches = re.finditer(insert_pattern, content, re.IGNORECASE)
                
                for match in matches:
                    table_name = match.group(1)
                    values = match.group(0)
                    data.append({
                        'table': table_name,
                        'data': values,
                        'type': 'insert'
                    })
                
                # Extract CREATE TABLE statements
                create_pattern = r'CREATE\s+TABLE\s+(\w+)[^;]+;'
                matches = re.finditer(create_pattern, content, re.IGNORECASE | re.DOTALL)
                
                for match in matches:
                    table_name = match.group(1)
                    data.append({
                        'table': table_name,
                        'data': match.group(0),
                        'type': 'schema'
                    })
                
        except Exception as e:
            print(f"[!] Error parsing SQL file {filepath}: {e}")
        
        return data
    
    def extract_data_from_urls(self, urls: List[str], proxy: Optional[Dict] = None) -> List[Dict]:
        """Extract and download database files from URLs"""
        extracted_data = []
        
        if proxy:
            self.setup_proxy(proxy)
        
        print(f"[*] Processing {len(urls)} URLs for database files...")
        
        for i, url in enumerate(urls, 1):
            print(f"[*] Processing {i}/{len(urls)}: {url[:60]}...")
            
            if self.is_database_url(url):
                filepath = self.download_file(url)
                if filepath:
                    print(f"[+] Downloaded: {filepath}")
                    parsed_data = self.parse_sql_file(filepath)
                    extracted_data.extend(parsed_data)
                    self.downloaded_files.append({
                        'url': url,
                        'filepath': filepath,
                        'data': parsed_data
                    })
            
            time.sleep(1)  # Rate limiting
        
        return extracted_data
