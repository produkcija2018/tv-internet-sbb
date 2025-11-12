#!/usr/bin/env python3
import requests
import json

BOT_TOKEN = "8105923056:AAFdk-iRcIgmVGHxdAE7R-qhTNoq7WbRTW0"

print("🚨 EMERGENCY BOT FIX")

# 1. Proveri da li je bot aktivan
print("1. 🔍 Proveravam bot status...")
try:
    response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getMe", timeout=10)
    bot_info = response.json()
    print(f"✅ Bot info: {bot_info}")
except Exception as e:
    print(f"❌ Greška: {e}")

# 2. Proveri webhook
print("2. 🌐 Proveravam webhook...")
try:
    response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo", timeout=10)
    webhook_info = response.json()
    print(f"📊 Webhook status: {webhook_info}")
except Exception as e:
    print(f"❌ Greška: {e}")

# 3. Resetuj webhook
print("3. 🔄 Resetujem webhook...")
try:
    # Obriši
    response = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook", timeout=10)
    print(f"🗑️ Delete: {response.json()}")
    
    # Podesi ponovo
    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
        data={"url": "https://produkcija2018.pythonanywhere.com/webhook"},
        timeout=10
    )
    print(f"✅ Set: {response.json()}")
except Exception as e:
    print(f"❌ Greška: {e}")

print("🎯 Popravka završena!")
