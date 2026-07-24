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
    "page": 1,
    "pageSize": 10
}

try:
    response = requests.post(
        API_URL,
        json=payload,
        timeout=20
    )

    send_message(
        "Status API : " + str(response.status_code) +
        "\n\nRéponse :\n" +
        response.text[:1000]
    )

except Exception as e:
    send_message("Erreur : " + str(e))
