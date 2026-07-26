import os
import requests
from playwright.sync_api import sync_playwright

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://trouverunlogement.lescrous.fr/tools/47/search?occupationModes=alone&bounds=2.4130316_48.6485333_2.4705092_48.6109217&locationName=%C3%89vry+%2891000%29"


def send(message):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)

    text = page.locator("body").inner_text()

    browser.close()


if "Aucun logement trouvé pour Évry (91000)" in text:
    # Aucun logement : ne rien faire
    pass
else:
    send(
        "🚨🚨🚨 ALERTE CROUS 🚨🚨🚨\n\n"
        "🏠 UN LOGEMENT EST APPARU À ÉVRY !\n\n"
        "👉 Ouvre immédiatement :\n"
        "https://trouverunlogement.lescrous.fr/tools/47/search?occupationModes=alone&bounds=2.4130316_48.6485333_2.4705092_48.6109217&locationName=%C3%89vry+%2891000%29\n\n"
        "⚠️ Dépêche-toi !"
    )
