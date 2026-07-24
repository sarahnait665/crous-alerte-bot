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
    "pageSize": 1,
    "occupationModes": ["alone"],
    "bounds": {
        "southWest": {
            "lat": 48.6109217,
            "lng": 2.4130316
        },
        "northEast": {
            "lat": 48.6485333,
            "lng": 2.4705092
        }
    }
}

try:
    response = requests.post(
        API_URL,
        json=payload,
        timeout=20
    )

    data = response.json()

    send_message(
        "Clés reçues par l'API :\n" +
        str(data.keys())
    )

except Exception as e:
    send_message(
        "❌ Erreur : " + str(e)
    )
