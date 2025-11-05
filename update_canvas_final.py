import json

with open('TV_Internet_Projekt.canvas', 'r') as f:
    canvas = json.load(f)

# Ažuriraj sve kartice sa konačnim statusom
nodes = [
    {
        "id": "central",
        "type": "text",
        "text": "# 🎯 TVINTERNET SBB PROJEKT\n\n## ✅ PROJEKT ZAVRŠEN!\n\n### 🎊 SVE FUNKCIONALNOSTI AKTIVNE:\n- 🤖 Telegram Bot radi\n- 🌐 Web sajt spreman\n- 💰 Biznis model definisan\n- 📊 Lead sistem spreman\n- 🚀 GitHub Pages postavljen",
        "x": 0,
        "y": 0,
        "width": 450,
        "height": 300,
        "color": "2"
    },
    {
        "id": "telegram-bot",
        "type": "text", 
        "text": "## 🤖 TELEGRAM BOT\n\n**Status:** ✅ AKTIVAN\n**Username:** @TVInternetSBB_bot\n**Token:** 8105923056:AAFdk-iRcIgmVGHxdAE7R-qhTNoq7WbRTW0\n\n### Funkcionalnosti:\n- AI odgovori na pitanja\n- TV/Internet paketi\n- Kontakt informacije\n- 24/7 dostupan",
        "x": -600,
        "y": -150,
        "width": 350,
        "height": 250,
        "color": "4"
    },
    {
        "id": "web-sajt",
        "type": "text",
        "text": "## 🌐 WEB SAJT\n\n**Status:** ✅ GOTOV\n**Tehnologije:** HTML5 + CSS3\n**Responsive:** Da\n**Telegram integracija:** Da\n\n### Sadržaj:\n- TV paketi sa cenama\n- Internet paketi sa cenama\n- Telegram bot integracija\n- Kontakt forme\n- Professional dizajn",
        "x": -600,
        "y": 150,
        "width": 350,
        "height": 250,
        "color": "1"
    },
    {
        "id": "gitHub",
        "type": "text",
        "text": "## 🐙 GITHUB\n\n**Status:** ✅ POSTAVLJEN\n**Pages:** Aktivan\n**Repo:** tv-internet-sbb\n**CI/CD:** Spreman\n\n### Sadržaj:\n- Source code bota\n- Web sajt files\n- Dokumentacija\n- Canvas projekt file",
        "x": 600,
        "y": -150,
        "width": 350,
        "height": 250,
        "color": "5"
    },
    {
        "id": "budzet",
        "type": "text",
        "text": "## 💰 BUDŽET\n\n### Troškovi: $0\n- Hosting: GitHub Pages (besplatno)\n- Domain: GitHub subdomain (besplatno)\n- Bot: Telegram API (besplatno)\n- Development: Termux + Obsidian (besplatno)\n\n### Potencijalni prihodi:\n- TV paketi: 1.990-2.990 RSD/mesec\n- Internet: 1.490-3.490 RSD/mesec\n- Kombinovani: 2.990 RSD/mesec",
        "x": 600,
        "y": 150,
        "width": 350,
        "height": 250,
        "color": "3"
    }
]

canvas["nodes"] = nodes

# Dodaj veze između karatica
canvas["edges"] = [
    {"fromNode": "telegram-bot", "toNode": "central", "fromSide": "right", "toSide": "left"},
    {"fromNode": "web-sajt", "toNode": "central", "fromSide": "right", "toSide": "left"},
    {"fromNode": "gitHub", "toNode": "central", "fromSide": "left", "toSide": "right"},
    {"fromNode": "budzet", "toNode": "central", "fromSide": "left", "toSide": "right"}
]

with open('TV_Internet_Projekt.canvas', 'w') as f:
    json.dump(canvas, f, indent=2)

print("✅ Canvas ažuriran - PROJEKT ZAVRŠEN!")
