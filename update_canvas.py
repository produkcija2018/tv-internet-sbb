import json

with open('TV_Internet_Projekt.canvas', 'r') as f:
    canvas = json.load(f)

# Dodaj karticu za Telegram Bot
bot_node = {
    "id": "telegram-bot",
    "type": "text", 
    "text": "## 🤖 TELEGRAM BOT\\n\\n✅ Bot aktiviran\\n🤖 AI funkcionalnosti\\n💬 Auto-odgovori\\n🟢 Online status\\n\\n@tv_internet_paketi_bot",
    "x": 500,
    "y": 100,
    "width": 280,
    "height": 180,
    "color": "3"
}

# Dodaj ili ažuriraj bot karticu
existing_bot_index = None
for i, node in enumerate(canvas["nodes"]):
    if node.get("id") == "telegram-bot":
        existing_bot_index = i
        break

if existing_bot_index is not None:
    canvas["nodes"][existing_bot_index] = bot_node
else:
    canvas["nodes"].append(bot_node)

# Dodaj vezu između centralne i bot kartice
new_edge = {
    "fromNode": "central", 
    "fromSide": "right",
    "toNode": "telegram-bot", 
    "toSide": "left"
}

# Proveri da li veza već postoji
edge_exists = False
for edge in canvas["edges"]:
    if edge["fromNode"] == "central" and edge["toNode"] == "telegram-bot":
        edge_exists = True
        break

if not edge_exists:
    canvas["edges"].append(new_edge)

with open('TV_Internet_Projekt.canvas', 'w') as f:
    json.dump(canvas, f, indent=2)

print("✅ Canvas ažuriran sa Telegram bot statusom!")
