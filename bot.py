import os
import requests

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
send_message(str(data.keys()))
    total = data["results"]["total"]["value"]

    if total > 0:
        logement = data["results"]["items"][0]
        residence = logement.get("residence", {})

        send_message(
            f"🚨 TEST API\n\n"
            f"Nombre trouvé : {total}\n"
            f"Adresse : {residence.get('address', 'Inconnue')}\n"
            f"ID logement : {logement.get('id')}"
        )

    else:
        send_message("🔎 Aucun logement trouvé.")

except Exception as e:
    send_message("❌ Erreur : " + str(e))
