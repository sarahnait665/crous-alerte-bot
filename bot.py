import os
import requests
import json

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

API_URL = "https://trouverunlogement.lescrous.fr/api/fr/search/47"

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

payload = {
    "page": 0,
    "pageSize": 0,
    "occupationModes": ["alone"]
}

try:
    response = requests.post(
        API_URL,
        json=payload,
        timeout=20
    )

    data = response.json()

    send_message(
        json.dumps(
            data["aggregations"],
            indent=2,
            ensure_ascii=False
        )[:4000]
    )

except Exception as e:
    send_message("❌ Erreur : " + str(e))
