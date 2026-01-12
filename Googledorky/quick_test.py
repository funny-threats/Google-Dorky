#!/usr/bin/env python3
"""
Quick test script to verify all imports and basic functionality
"""

import sys
import os

def test_imports():
    """Test all imports"""
    print("Testing imports...")
    try:
        from colorama import init, Fore, Style
        print("✓ colorama")
        
        from proxy_scraper import ProxyScraper
        print("✓ proxy_scraper")
        
        from proxy_validator import ProxyValidator
        print("✓ proxy_validator")
        
        from google_searcher import GoogleSearcher
        print("✓ google_searcher")
        
        from sql_checker import SQLChecker
        print("✓ sql_checker")
        
        from database_downloader import DatabaseDownloader
        print("✓ database_downloader")
        
        from data_organizer import DataOrganizer
        print("✓ data_organizer")
        
        from sqlmap_integration import SQLMapIntegration
        print("✓ sqlmap_integration")
        
        from sqli_payloads import SQLIPayloads
        print("✓ sqli_payloads")
        
        from banner import print_banner
        print("✓ banner")
        
        print("\n✅ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("\nInstall missing dependencies:")
        print("  pip install -r requirements.txt")
        return False

def test_banner():
    """Test banner display"""
    print("\nTesting banner...")
    try:
        from banner import print_banner
        print_banner()
        print("✅ Banner works!")
        return True
    except Exception as e:
        print(f"❌ Banner error: {e}")
        return False

def test_payloads():
    """Test payload loading"""
    print("\nTesting payloads...")
    try:
        from sqli_payloads import SQLIPayloads
        payloads = SQLIPayloads()
        all_payloads = payloads.get_all_payloads()
        print(f"✅ Loaded {len(all_payloads)} payloads")
        return True
    except Exception as e:
        print(f"❌ Payload error: {e}")
        return False

def main():
    print("=" * 60)
    print("Google Dork Scanner - Quick Test")
    print("=" * 60)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Banner", test_banner()))
    results.append(("Payloads", test_payloads()))
    
    print("\n" + "=" * 60)
    print("Test Results:")
    print("=" * 60)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name:.<30} {status}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n✅ All tests passed! Application is ready to use.")
        print("\nQuick start:")
        print("  python main.py --dorks dorks.txt")
        print("  python main.py --dorks dorks.txt --aggressive --use-sqlmap")
    else:
        print("\n❌ Some tests failed. Please fix errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
