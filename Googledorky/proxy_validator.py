"""
Proxy Validator Module
Validates and manages proxy rotation
"""

import requests
from typing import List, Dict, Optional
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from fake_useragent import UserAgent

class ProxyValidator:
    def __init__(self, timeout=5):
        self.timeout = timeout
        self.ua = UserAgent()
        self.valid_proxies = []
        
    def validate_proxy(self, proxy: Dict) -> Optional[Dict]:
        """Validate a single proxy"""
        try:
            proxy_url = f"{proxy['protocol']}://{proxy['ip']}:{proxy['port']}"
            proxies = {
                'http': proxy_url,
                'https': proxy_url
            }
            
            # Test with a simple request
            test_url = "http://httpbin.org/ip"
            response = requests.get(
                test_url,
                proxies=proxies,
                timeout=self.timeout,
                headers={'User-Agent': self.ua.random}
            )
            
            if response.status_code == 200:
                proxy['validated'] = True
                proxy['response_time'] = response.elapsed.total_seconds()
                return proxy
        except Exception:
            pass
        
        return None
    
    def validate_proxies(self, proxies: List[Dict], max_workers=20) -> List[Dict]:
        """Validate multiple proxies concurrently"""
        print(f"[*] Validating {len(proxies)} proxies...")
        valid_proxies = []
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_proxy = {
                executor.submit(self.validate_proxy, proxy): proxy 
                for proxy in proxies
            }
            
            for future in as_completed(future_to_proxy):
                result = future.result()
                if result:
                    valid_proxies.append(result)
        
        # Sort by response time
        valid_proxies.sort(key=lambda x: x.get('response_time', 999))
        
        print(f"[+] Validated {len(valid_proxies)} working proxies")
        return valid_proxies
    
    def get_proxy(self, proxies: List[Dict]) -> Optional[Dict]:
        """Get a random valid proxy"""
        if not proxies:
            return None
        return proxies[0]  # Return fastest proxy
    
    def rotate_proxy(self, proxies: List[Dict], current_proxy: Optional[Dict] = None) -> Optional[Dict]:
        """Rotate to next proxy"""
        if not proxies:
            return None
        
        if current_proxy and current_proxy in proxies:
            idx = proxies.index(current_proxy)
            next_idx = (idx + 1) % len(proxies)
            return proxies[next_idx]
        
        return proxies[0]
