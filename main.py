import json
import requests
import time

# Environment variables
BOT_TOKEN = "8036482272:AAHzj1Y1D9YT3JEy3bexmrX1zFB2HtZOIO4"
CHAT_ID = "5668268717"

def load_entries():
    with open("entries.json", "r") as file:
        return json.load(file)

def save_entries(entries):
    with open("entries.json", "w") as file:
        json.dump(entries, file, indent=4)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    return response.json()

def process_entries():
    entries = load_entries()
    for entry in entries:
        if not entry.get("sent", False):
            message = entry["message"]
            send_telegram_message(message)
            entry["sent"] = True
            save_entries(entries)
        time.sleep(1
