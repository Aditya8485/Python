#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from urllib.parse import urlparse

# Simple & clean console styling
class Style:
    CYAN = '\033[38;5;81m'
    GREEN = '\033[38;5;46m'
    YELLOW = '\033[38;5;226m'
    RED = '\033[38;5;196m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clean_domain(url_str):
    """Extracts raw string and normalizes it to a clean root domain to drop paths/protocols"""
    try:
        url_str = url_str.strip()
        if not url_str.startswith(('http://', 'https://')):
            url_str = 'http://' + url_str
        parsed = urlparse(url_str)
        domain = parsed.netloc if parsed.netloc else parsed.path
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain.lower()
    except:
        return url_str.lower()

def main():
    print(f"{Style.CYAN}{Style.BOLD}=== ULP TO COMBO EXTRACOR ENGINE ==={Style.RESET}")
    
    # 1. Keywords Selection
    keywords_input = input(f"\n[{Style.CYAN}?{Style.RESET}] Enter keywords to search (space separated, e.g., netflix spotify): ").strip()
    keywords = [k.lower() for k in keywords_input.split() if k]
    
    if not keywords:
        print(f"{Style.RED}[-] No search keywords provided. Exiting.{Style.RESET}")
        return

    # 2. Output Combo Type Filter
    print(f"\n[{Style.CYAN}*{Style.RESET}] Select Output Format Profile:")
    print("  1. USER:PASS (Only standard user profiles)")
    print("  2. MAIL:PASS (Only valid email structures)")
    print("  3. BOTH / MIXED (Bypass format constraints)")
    choice = input("Select Option (1/2/3): ").strip()
    if choice not in ['1', '2', '3']:
        choice = '3'
        print(f"{Style.YELLOW}[!] Invalid entry. Defaulting to Option 3 (BOTH).{Style.RESET}")

    # Detect current work path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Scan for input databases excluding output footprints
    txt_files = [f for f in os.listdir(script_dir) if f.endswith('.txt') 
                 and not f.startswith(('combo_', 'ULP_'))]
    
    if not txt_files:
        print(f"{Style.RED}[-] No source .txt files found in current directory!{Style.RESET}")
        return

    print(f"\n[{Style.CYAN}⏳{Style.RESET}] Analyzing source files and running deduplication matrix...")

    # Accurate data element targeting regex
    sitio_regex = re.compile(r'(?:Sitio|Url|Host|URL):\s*(.*?)(?:\s*\||\s*\n|$)', re.IGNORECASE)
    user_regex = re.compile(r'(?:Usuario|User|Login):\s*(.*?)(?:\s*\||\s*\n|$)', re.IGNORECASE)
    pass_regex = re.compile(r'(?:Contraseña|Pass|Password):\s*(.*?)(?:\s*\||\s*\n|$)', re.IGNORECASE)
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # Deduplication and collection structures
    global_seen_signatures = set()
    keyword_data_store = {kw: [] for kw in keywords}
    combined_master_lines = []

    for file_name in txt_files:
        file_path = os.path.join(script_dir, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as stream:
                for line in stream:
                    line_lower = line.lower()
                    
                    # Core filter optimization pass
                    matched_keywords = [kw for kw in keywords if kw in line_lower]
                    if not matched_keywords:
                        continue
                        
                    # Extract elements safely via dynamic patterns
                    sitio_match = sitio_regex.search(line)
                    user_match = user_regex.search(line)
                    pass_match = pass_regex.search(line)
                    
                    if sitio_match and user_match and pass_match:
                        raw_url = sitio_match.group(1).strip()
                        user = user_match.group(1).strip()
                        password = pass_match.group(1).strip()
                        
                        if not user or not password:
                            continue
                            
                        clean_site = clean_domain(raw_url)
                        is_email = bool(email_regex.match(user))
                        
                        # Validate structure choices
                        passes_filter = False
                        if choice == '1' and not is_email:
                            passes_filter = True
                        elif choice == '2' and is_email:
                            passes_filter = True
                        elif choice == '3':
                            passes_filter = True
                            
                        if passes_filter:
                            # Hardcore Unique Signature Lookup: Domain + User + Password uniqueness check
                            unique_sig = f"{clean_site}:{user}:{password}"
                            if unique_sig not in global_seen_signatures:
                                global_seen_signatures.add(unique_sig)
                                
                                combo_format = f"{user}:{password}"
                                combined_master_lines.append(combo_format)
                                
                                for kw in matched_keywords:
                                    keyword_data_store[kw].append(combo_format)
        except Exception as file_err:
            print(f"{Style.RED}[!] Failed parsing file: {file_name} | Err: {str(file_err)}{Style.RESET}")

    # Write organized outputs back to storage
    total_written = 0
    generated_files = []

    if combined_master_lines:
        # 1. Save specific categorized files for matches
        for kw, lines in keyword_data_store.items():
            if lines:
                out_name = f"combo_{kw}.txt"
                with open(os.path.join(script_dir, out_name), 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines) + '\n')
                generated_files.append(out_name)
                
        # 2. Save master merged clean combo file
        master_out_name = "combo_all_merged.txt"
        with open(os.path.join(script_dir, master_out_name), 'w', encoding='utf-8') as f:
            f.write('\n'.join(combined_master_lines) + '\n')
        generated_files.append(master_out_name)
        total_written = len(combined_master_lines)

    # Simple clean completion report
    print(f"\n{Style.GREEN}{Style.BOLD}[+] Extraction Process Completed!{Style.RESET}")
    print(f"  {Style.GREEN}✓{Style.RESET} Unique Combos Extracted: {total_written:,}")
    if generated_files:
        print(f"\n{Style.CYAN}{Style.BOLD}Files Saved Successfully:{Style.RESET}")
        for gf in generated_files:
            print(f"  {Style.GREEN}»{Style.RESET} {gf}")
    else:
        print(f"{Style.YELLOW}[!] No matching lines found for the provided filter criteria.{Style.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Style.RED}[-] Process aborted by user.{Style.RESET}")