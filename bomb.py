import os
import time
import json
import requests
import concurrent.futures

CONFIG_FILE = "config.json"

# ANSI Color Codes
R = '\033[31m' # Red
G = '\033[32m' # Green
C = '\033[36m' # Cyan
Y = '\033[33m' # Yellow
W = '\033[0m'  # Reset

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner = f"""{R}
  _______      _____   ____                  _     
 |__   __|    / ____| |  _ \                | |    
    | |______| |  __  | |_) | ___  _ __ ___ | |__  
    | |______| | |_ | |  _ < / _ \| '_ ` _ \| '_ \ 
    | |      | |__| | | |_) | (_) | | | | | | |_) |
    |_|       \_____| |____/ \___/|_| |_| |_|_.__/ 
    {W}"""
    print(banner)
    print(f"{C}=================================================={W}")
    print(f"{G}          Created by: Yoseph Alganeh{W}")
    print(f"{C}=================================================={W}\n")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)

def send_message(url, payload, i):
    try:
        response = requests.post(url, json=payload)
        data = response.json()
        
        if response.status_code == 200:
            print(f"{G}[+] Message {i} sent!{W}")
        elif response.status_code == 429:
            retry_after = data.get("parameters", {}).get("retry_after", 5)
            print(f"{R}[!] Telegram Rate Limit! Sleeping for {retry_after}s...{W}")
            time.sleep(retry_after)
            # ከጥበቃ በኋላ ድጋሚ ይሞክራል
            requests.post(url, json=payload)
            print(f"{Y}[~] Message {i} sent after sleep.{W}")
        else:
            print(f"{R}[-] Failed to send {i}.{W}")
    except Exception as e:
        print(f"{R}[!] Error on message {i}: {e}{W}")

def main():
    show_banner()
    config = load_config()

    if "bot_token" not in config:
        print(f"{Y}[!] Bot token not found.{W}")
        bot_token = input(f"{C}Enter your Telegram Bot Token: {W}").strip()
        config["bot_token"] = bot_token
        save_config(config)
        print(f"{G}[+] Bot token saved successfully!{W}\n")
    else:
        bot_token = config["bot_token"]
        print(f"{G}[+] Loaded saved Bot Token.{W}\n")

    chat_id = input(f"{C}Enter Target Chat ID: {W}").strip()
    message = input(f"{C}Enter Message to send: {W}").strip()
    
    try:
        total_msgs = int(input(f"{C}Enter number of messages to send (e.g., 1000): {W}").strip())
    except ValueError:
        print(f"{R}[!] Invalid number. Defaulting to 1000 messages.{W}")
        total_msgs = 1000

    print(f"\n{Y}[*] Starting EXTREME FAST Attack on {chat_id}...{W}\n")
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    # ቁጥር (1, 2, 3...) ከፅሁፉ ጋር እንዳይላክ ተደርጓል
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    # Multi-threading በመጠቀም በአንድ ጊዜ እስከ 20 መልእክቶችን ወደ ሰርቨሩ ይልካል
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(1, total_msgs + 1):
            executor.submit(send_message, url, payload, i)

    print(f"\n{G}[+] Bombing operation finished!{W}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Program Exited.{W}")
