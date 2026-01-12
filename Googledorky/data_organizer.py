"""
Data Organizer Module
Organizes and formats extracted data into structured output files
"""

import json
import os
from typing import List, Dict
from datetime import datetime
from collections import defaultdict

class DataOrganizer:
    def __init__(self, output_file: str = "results.txt"):
        self.output_file = output_file
        self.organized_data = {
            'vulnerable_urls': [],
            'database_files': [],
            'extracted_data': defaultdict(list),
            'summary': {}
        }
    
    def organize_vulnerable_urls(self, vulnerable_urls: List[Dict]):
        """Organize SQL injection vulnerable URLs"""
        self.organized_data['vulnerable_urls'] = vulnerable_urls
        
        # Count SQLMap successes
        sqlmap_successes = sum(1 for vuln in vulnerable_urls 
                              if vuln.get('sqlmap_result', {}).get('success', False))
        self.organized_data['sqlmap_exploited'] = sqlmap_successes
    
    def organize_database_files(self, database_files: List[Dict]):
        """Organize downloaded database files"""
        self.organized_data['database_files'] = database_files
        
        # Extract and organize data by table
        for db_file in database_files:
            for data_item in db_file.get('data', []):
                table_name = data_item.get('table', 'unknown')
                self.organized_data['extracted_data'][table_name].append(data_item)
    
    def generate_summary(self):
        """Generate summary statistics"""
        self.organized_data['summary'] = {
            'total_vulnerable_urls': len(self.organized_data['vulnerable_urls']),
            'total_database_files': len(self.organized_data['database_files']),
            'total_tables_found': len(self.organized_data['extracted_data']),
            'timestamp': datetime.now().isoformat()
        }
    
    def write_to_file(self):
        """Write organized data to output file"""
        self.generate_summary()
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            # Write header
            f.write("=" * 80 + "\n")
            f.write("GOOGLE DORK SQL INJECTION SCAN RESULTS\n")
            f.write("=" * 80 + "\n\n")
            
            # Write summary
            f.write("SUMMARY\n")
            f.write("-" * 80 + "\n")
            summary = self.organized_data['summary']
            f.write(f"Scan Date: {summary['timestamp']}\n")
            f.write(f"Total Vulnerable URLs: {summary['total_vulnerable_urls']}\n")
            f.write(f"Total Database Files: {summary['total_database_files']}\n")
            f.write(f"Total Tables Found: {summary['total_tables_found']}\n\n")
            
            # Write vulnerable URLs
            if self.organized_data['vulnerable_urls']:
                f.write("SQL INJECTION VULNERABLE URLS\n")
                f.write("-" * 80 + "\n")
                for i, vuln in enumerate(self.organized_data['vulnerable_urls'], 1):
                    f.write(f"\n[{i}] {vuln.get('url', 'N/A')}\n")
                    f.write(f"    Vulnerable Parameter: {vuln.get('vulnerable_param', 'N/A')}\n")
                    f.write(f"    Payload: {vuln.get('payload', 'N/A')}\n")
                    f.write(f"    Status Code: {vuln.get('status_code', 'N/A')}\n")
                    
                    # Add SQLMap results if available
                    sqlmap_result = vuln.get('sqlmap_result', {})
                    if sqlmap_result:
                        if sqlmap_result.get('success'):
                            f.write(f"    [SQLMap] Successfully Exploited: YES\n")
                            if sqlmap_result.get('databases'):
                                f.write(f"    [SQLMap] Databases Found: {', '.join(sqlmap_result['databases'])}\n")
                            if sqlmap_result.get('tables'):
                                f.write(f"    [SQLMap] Tables Found: {len(sqlmap_result['tables'])} tables\n")
                            if sqlmap_result.get('dumped_files'):
                                f.write(f"    [SQLMap] Data Dumped: {len(sqlmap_result['dumped_files'])} files\n")
                        else:
                            f.write(f"    [SQLMap] Exploitation: Failed\n")
                            if sqlmap_result.get('error'):
                                f.write(f"    [SQLMap] Error: {sqlmap_result['error']}\n")
                f.write("\n")
            
            # Write database files
            if self.organized_data['database_files']:
                f.write("DOWNLOADED DATABASE FILES\n")
                f.write("-" * 80 + "\n")
                for i, db_file in enumerate(self.organized_data['database_files'], 1):
                    f.write(f"\n[{i}] URL: {db_file.get('url', 'N/A')}\n")
                    f.write(f"    File: {db_file.get('filepath', 'N/A')}\n")
                    f.write(f"    Data Items: {len(db_file.get('data', []))}\n")
                f.write("\n")
            
            # Write extracted data by table
            if self.organized_data['extracted_data']:
                f.write("EXTRACTED DATA BY TABLE\n")
                f.write("-" * 80 + "\n")
                for table_name, data_items in self.organized_data['extracted_data'].items():
                    f.write(f"\nTable: {table_name}\n")
                    f.write(f"Items: {len(data_items)}\n")
                    for item in data_items[:5]:  # Show first 5 items
                        f.write(f"  - Type: {item.get('type', 'N/A')}\n")
                        f.write(f"    Data: {item.get('data', '')[:100]}...\n")
                    if len(data_items) > 5:
                        f.write(f"  ... and {len(data_items) - 5} more items\n")
                f.write("\n")
            
            f.write("=" * 80 + "\n")
            f.write("END OF REPORT\n")
            f.write("=" * 80 + "\n")
        
        print(f"[+] Results written to {self.output_file}")
    
    def write_json(self, json_file: str = "results.json"):
        """Write organized data to JSON file"""
        self.generate_summary()
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.organized_data, f, indent=2, default=str)
        
        print(f"[+] JSON results written to {json_file}")
