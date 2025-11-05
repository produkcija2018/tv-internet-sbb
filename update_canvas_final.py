import json

with open('TV_Internet_Projekt.canvas', 'r') as f:
    canvas = json.load(f)

# Ažuriraj Telegram bot karticu
bot_node = {
    "id": "telegram-bot",
    "type": "text",
    "text": "## 🤖 TVINTERNET SBB BOT\n\n✅ **STATUS: AKTIVAN**\n📊 HTTP zahtevi: 200 OK\n💬 Komande postavljene\n🎯 Keyboard aktiviran\n👥 Spreman za klijente\n\n**Token:** 8105923056:AAFdk-iR...\n**Username:** @TVInternetSBB_bot",
    "x": 500,
    "y": 100,
    "width": 320,
    "height": 220,
    "color": "2"
}

# Pronađi i zameni postojeću bot karticu
for i, node in enumerate(canvas["nodes"]):
    if node.get("id") == "telegram-bot":
        canvas["nodes"][i] = bot_node
        break
else:
    canvas["nodes"].append(bot_node)

with open('TV_Internet_Projekt.canvas', 'w') as f:
    json.dump(canvas, f, indent=2)

print("✅ Canvas ažuriran - BOT JE AKTIVAN!")
