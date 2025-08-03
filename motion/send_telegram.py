#!/usr/bin/env python3
import requests
import sys

# Replace with your actual bot token and chat ID
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.status_code, response.text

if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
        status, resp = send_telegram_message(msg)
        print(f"Telegram response: {status}, {resp}")
    else:
        print("Usage: send_telegram.py "Your message here"")
