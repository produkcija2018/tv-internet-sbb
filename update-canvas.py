import json

# Čitaj postojeći Canvas
with open('TV_Internet_Projekt.canvas', 'r') as f:
    canvas = json.load(f)

# Dodaj novu karticu za GitHub
new_node = {
    "id": "github",
    "type": "text",
    "text": "## 🐙 GITHUB\n\n✅ Repozitorijum kreiran\n🌐 Pages aktiviran\n🤖 Auto-sync u toku",
    "x": 500,
    "y": -100,
    "width": 250,
    "height": 150,
    "color": "2"
}

canvas["nodes"].append(new_node)

# Sačuvaj updated Canvas
with open('TV_Internet_Projekt.canvas', 'w') as f:
    json.dump(canvas, f, indent=2)

print("Canvas ažuriran!")
