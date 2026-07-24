import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

API_URL = "https://trouverunlogement.lescrous.fr/api/fr/search/26"

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

try:
    response = requests.get(API_URL, timeout=20)

    if response.status_code == 200:
        data = response.text[:500]
        send_message(
            "✅ API accessible !\n\nRéponse reçue :\n" + data
        )
    else:
        send_message(
            f"❌ API erreur HTTP : {response.status_code}"
        )

except Exception as e:
    send_message(
        "❌ Erreur : " + str(e)
    )
