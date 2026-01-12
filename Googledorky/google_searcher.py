"""
Google Search Automation Module
Performs Google searches using proxies with dork queries
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import time
import random
from urllib.parse import quote_plus, urlparse
from fake_useragent import UserAgent
import re

class GoogleSearcher:
    def __init__(self, proxy: Optional[Dict] = None):
        self.proxy = proxy
        self.ua = UserAgent()
        self.session = requests.Session()
        self.results = []
        
    def get_headers(self):
        """Generate realistic browser headers"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
        }
    
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
    
    def search_google(self, query: str, num_results: int = 10) -> List[Dict]:
        """Search Google with a dork query"""
        results = []
        
        try:
            # Google search URL
            search_url = f"https://www.google.com/search?q={quote_plus(query)}&num={num_results}"
            
            headers = self.get_headers()
            response = self.session.get(
                search_url,
                headers=headers,
                timeout=15
            )
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Parse search results
                search_results = soup.find_all('div', class_='g')
                
                for result in search_results:
                    try:
                        # Extract title
                        title_elem = result.find('h3')
                        title = title_elem.text if title_elem else "No title"
                        
                        # Extract URL
                        link_elem = result.find('a')
                        url = link_elem.get('href') if link_elem else None
                        
                        if url and url.startswith('http'):
                            # Extract snippet
                            snippet_elem = result.find('span', class_='aCOpRe')
                            snippet = snippet_elem.text if snippet_elem else ""
                            
                            results.append({
                                'title': title,
                                'url': url,
                                'snippet': snippet,
                                'query': query
                            })
                    except Exception as e:
                        continue
                
                # Random delay to avoid rate limiting
                time.sleep(random.uniform(2, 5))
                
            elif response.status_code == 429:
                print(f"[!] Rate limited. Waiting longer...")
                time.sleep(random.uniform(10, 20))
            else:
                print(f"[!] Google returned status code: {response.status_code}")
                
        except Exception as e:
            print(f"[!] Error searching Google: {e}")
        
        return results
    
    def search_multiple_dorks(self, dorks: List[str], proxy: Optional[Dict] = None) -> List[Dict]:
        """Search multiple Google dorks with progress tracking"""
        all_results = []
        
        if proxy:
            self.setup_proxy(proxy)
        
        from tqdm import tqdm
        
        # Use progress bar for better UX
        with tqdm(total=len(dorks), desc="Searching Google", unit="dork", ncols=80) as pbar:
            for i, dork in enumerate(dorks, 1):
                pbar.set_description(f"Searching: {dork[:40]}...")
                results = self.search_google(dork)
                all_results.extend(results)
                pbar.set_postfix(results=len(results))
                pbar.update(1)
                
                # Delay between searches (reduced for speed)
                if i < len(dorks):
                    time.sleep(random.uniform(2, 4))
        
        return all_results
