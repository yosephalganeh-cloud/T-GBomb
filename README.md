# T-G Bomb 🚀

A powerful and colorful Telegram message bomber built with Python. Designed to run smoothly on Termux and other terminal emulators.

**Created by: Yoseph Alganeh**

## Features ✨
* 🎨 **Colorful Terminal UI** with a cool ASCII banner.
* 💾 **Smart Configuration:** Asks for your Bot Token only once and remembers it for future use.
* ⏱️ **Anti-Ban System:** Automatically handles Telegram's `429 Too Many Requests` (Rate Limits) by pausing and resuming the attack.
* 📱 **Termux Ready:** Fully optimized for Android mobile development.

## Prerequisites ⚙️
Make sure you have Python installed. You also need a Telegram Bot Token (get it from [@BotFather](https://t.me/botfather) on Telegram) and the target Chat ID.

## Installation for Termux 📱

Run the following commands one by one in your Termux application:

```bash
# 1. Update your packages
pkg update && pkg upgrade -y

# 2. Install Python and Git
pkg install python git -y

# 3. Clone this repository (Replace with your actual GitHub link)
git clone https://github.com/yosephalganeh-cloud/T-G-Bomb.git)

# 4. Open the directory
cd T-G-Bomb

# 5. Install the required requests library
pip install requests

# 6. Run the tool
python app.py
