"""
Proxy Scraper Module
Scrapes free proxy websites to collect proxy lists
"""

import requests
from bs4 import BeautifulSoup
import re
from typing import List, Dict
import random
from fake_useragent import UserAgent
import time

class ProxyScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.proxies = []
        
    def get_headers(self):
        """Generate random headers"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }
    
    def scrape_free_proxy_list(self) -> List[Dict]:
        """Scrape free-proxy-list.net"""
        proxies = []
        try:
            url = "https://www.free-proxy-list.net/"
            response = requests.get(url, headers=self.get_headers(), timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            table = soup.find('table', {'id': 'proxylisttable'})
            if table:
                rows = table.find_all('tr')[1:]  # Skip header
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) >= 2:
                        ip = cols[0].text.strip()
                        port = cols[1].text.strip()
                        protocol = 'https' if 'yes' in cols[6].text.lower() else 'http'
                        proxies.append({
                            'ip': ip,
                            'port': port,
                            'protocol': protocol,
                            'source': 'free-proxy-list'
                        })
        except Exception as e:
            print(f"Error scraping free-proxy-list: {e}")
        
        return proxies
    
    def scrape_proxy_scrape(self) -> List[Dict]:
        """Scrape proxyscrape.com API"""
        proxies = []
        try:
            urls = [
                "https://api.proxyscrape.com/v2/?request=get&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
                "https://api.proxyscrape.com/v2/?request=get&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all"
            ]
            
            for url in urls:
                response = requests.get(url, headers=self.get_headers(), timeout=10)
                if response.status_code == 200:
                    lines = response.text.strip().split('\n')
                    for line in lines:
                        if ':' in line:
                            ip, port = line.strip().split(':')
                            protocol = 'https' if 'https' in url else 'http'
                            proxies.append({
                                'ip': ip,
                                'port': port,
                                'protocol': protocol,
                                'source': 'proxyscrape'
                            })
        except Exception as e:
            print(f"Error scraping proxyscrape: {e}")
        
        return proxies
    
    def scrape_proxylist_me(self) -> List[Dict]:
        """Scrape proxylist.geonode.com"""
        proxies = []
        try:
            url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http%2Chttps"
            response = requests.get(url, headers=self.get_headers(), timeout=10)
            if response.status_code == 200:
                data = response.json()
                for proxy in data.get('data', []):
                    proxies.append({
                        'ip': proxy.get('ip'),
                        'port': str(proxy.get('port')),
                        'protocol': proxy.get('protocols', ['http'])[0],
                        'source': 'geonode'
                    })
        except Exception as e:
            print(f"Error scraping geonode: {e}")
        
        return proxies
    
    def scrape_all(self) -> List[Dict]:
        """Scrape all proxy sources"""
        print("[*] Scraping proxies from multiple sources...")
        all_proxies = []
        
        all_proxies.extend(self.scrape_free_proxy_list())
        time.sleep(2)
        
        all_proxies.extend(self.scrape_proxy_scrape())
        time.sleep(2)
        
        all_proxies.extend(self.scrape_proxylist_me())
        
        # Remove duplicates
        unique_proxies = []
        seen = set()
        for proxy in all_proxies:
            key = (proxy['ip'], proxy['port'])
            if key not in seen:
                seen.add(key)
                unique_proxies.append(proxy)
        
        print(f"[+] Found {len(unique_proxies)} unique proxies")
        return unique_proxies
