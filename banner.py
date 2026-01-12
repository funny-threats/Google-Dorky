"""
ASCII Art Banner and Text Graphics Module
"""

from colorama import Fore, Style

def print_banner():
    """Print main banner"""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║  {Fore.YELLOW}╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗╦ ╦╔═╗╔═╗╦═╗╔═╗╔╦╗  {Fore.CYAN}╔═╗╔═╗╔═╗╦ ╦╔═╗╔═╗╦═╗╔═╗╔╦╗  ║
║  {Fore.YELLOW}║  ╠═╝╠═╝║ ╦║║║║ ║║║║║╣ ║╣ ╠╦╝╠═╣ ║   {Fore.CYAN}╚═╗║  ║ ║║║║║╣ ║ ╦╠╦╝╠═╣ ║   ║
║  {Fore.YELLOW}╚═╝╩  ╩  ╚═╝╩ ╩╚═╝╚╩╝╚═╝╚═╝╩╚═╩ ╩ ╩   {Fore.CYAN}╚═╝╚═╝╚═╝╚╩╝╚═╝╚═╝╩╚═╩ ╩ ╩   ║
║                                                                          ║
║  {Fore.RED}╔═╗╔═╗╦  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗  {Fore.CYAN}║
║  {Fore.RED}║╣ ║ ╦║  ╠═╝║ ║╠╦╝║╣ ║ ╦║ ╦║ ╦╠╦╝╠═╣ ║ ║╣ ╠╦╝  {Fore.CYAN}║
║  {Fore.RED}╚═╝╚═╝╩═╝╩  ╚═╝╩╚═╚═╝╚═╝╚═╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═  {Fore.CYAN}║
║                                                                          ║
║  {Fore.GREEN}Automated SQL Injection Scanner for Bug Bounty Hunting{Fore.CYAN}                  ║
║  {Fore.WHITE}Version 2.0 | Full Power Mode | SQLMap Integrated{Fore.CYAN}                        ║
╚══════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def print_section_header(text: str, color=Fore.CYAN):
    """Print section header"""
    width = 80
    print(f"\n{color}{'═' * width}{Style.RESET_ALL}")
    print(f"{color}{text.center(width)}{Style.RESET_ALL}")
    print(f"{color}{'═' * width}{Style.RESET_ALL}\n")

def print_progress_bar(current: int, total: int, prefix: str = "Progress", length: int = 50):
    """Print progress bar"""
    percent = ("{0:.1f}").format(100 * (current / float(total)))
    filled_length = int(length * current // total)
    bar = '█' * filled_length + '░' * (length - filled_length)
    print(f'\r{Fore.CYAN}{prefix}:{Style.RESET_ALL} |{Fore.GREEN}{bar}{Style.RESET_ALL}| {current}/{total} ({percent}%)', end='\r')
    if current == total:
        print()

def print_status(message: str, status_type: str = "info"):
    """Print status message with icon"""
    icons = {
        "info": f"{Fore.CYAN}[*]{Style.RESET_ALL}",
        "success": f"{Fore.GREEN}[+]{Style.RESET_ALL}",
        "warning": f"{Fore.YELLOW}[!]{Style.RESET_ALL}",
        "error": f"{Fore.RED}[!]{Style.RESET_ALL}",
        "vuln": f"{Fore.RED}[VULN]{Style.RESET_ALL}",
        "exploit": f"{Fore.MAGENTA}[EXPLOIT]{Style.RESET_ALL}",
    }
    icon = icons.get(status_type, icons["info"])
    print(f"{icon} {message}")

def print_stats(stats: dict):
    """Print statistics in a nice format"""
    print(f"\n{Fore.CYAN}{'─' * 80}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}📊 SCAN STATISTICS{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'─' * 80}{Style.RESET_ALL}")
    
    for key, value in stats.items():
        # Format key nicely
        formatted_key = key.replace('_', ' ').title()
        print(f"  {Fore.WHITE}{formatted_key:.<30}{Style.RESET_ALL} {Fore.GREEN}{value}{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}{'─' * 80}{Style.RESET_ALL}\n")

def print_vulnerability_found(url: str, param: str, payload: str):
    """Print vulnerability found message"""
    print(f"\n{Fore.RED}{'!' * 80}{Style.RESET_ALL}")
    print(f"{Fore.RED}🚨 SQL INJECTION VULNERABILITY DETECTED{Style.RESET_ALL}")
    print(f"{Fore.RED}{'!' * 80}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}URL:{Style.RESET_ALL} {url}")
    print(f"{Fore.YELLOW}Parameter:{Style.RESET_ALL} {param}")
    print(f"{Fore.YELLOW}Payload:{Style.RESET_ALL} {payload}")
    print(f"{Fore.RED}{'!' * 80}{Style.RESET_ALL}\n")

def print_sqlmap_success(url: str, databases: list, tables: list):
    """Print SQLMap success message"""
    print(f"\n{Fore.GREEN}{'═' * 80}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}✅ SQLMAP EXPLOITATION SUCCESSFUL{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * 80}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Target:{Style.RESET_ALL} {url}")
    if databases:
        print(f"{Fore.GREEN}📦 Databases Found:{Style.RESET_ALL} {', '.join(databases)}")
    if tables:
        print(f"{Fore.GREEN}📋 Tables Found:{Style.RESET_ALL} {len(tables)} tables")
    print(f"{Fore.GREEN}{'═' * 80}{Style.RESET_ALL}\n")

def print_footer(results_file: str):
    """Print footer with results"""
    footer = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║  {Fore.GREEN}✅ SCAN COMPLETE!{Fore.CYAN}                                                          ║
║                                                                          ║
║  {Fore.WHITE}Results saved to:{Fore.YELLOW} {results_file:<60}{Fore.CYAN}║
║                                                                          ║
║  {Fore.CYAN}Check the following files:{Fore.CYAN}                                                 ║
║  {Fore.WHITE}  • {results_file}{Fore.CYAN}                                                          ║
║  {Fore.WHITE}  • {results_file.replace('.txt', '.json')}{Fore.CYAN}                                                          ║
║  {Fore.WHITE}  • sqlmap_results/ (if SQLMap was used){Fore.CYAN}                                                          ║
║  {Fore.WHITE}  • downloads/ (database files){Fore.CYAN}                                                          ║
║                                                                          ║
║  {Fore.YELLOW}⚠️  Remember: Only use on authorized systems!{Fore.CYAN}                           ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(footer)
