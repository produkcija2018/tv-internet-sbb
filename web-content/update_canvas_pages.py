import json

with open('TV_Internet_Projekt.canvas', 'r') as f:
    canvas = json.load(f)

# Ažuriraj sa GitHub Pages statusom
pages_node = {
    "id": "github-pages",
    "type": "text",
    "text": "## 🌐 GITHUB PAGES STATUS\n\n### 🔄 U DEPLOY-U\n\n**URL:** https://produkcija2018.github.io/tv-internet-sbb/\n**Branch:** main\n**Folder:** /web-content\n\n### Provera:\n- ✅ Push uspešan\n- 🔄 Čekamo deploy\n- ⏳ GitHub procesira\n\n### Akcije:\n1. Proveri Actions tab\n2. Proveri Pages settings\n3. Testiraj URL\n4. Sačekaj 5-10 minuta",
    "x": 600,
    "y": -150,
    "width": 380,
    "height": 300,
    "color": "3"
}

# Pronađi i zameni Pages karticu
for i, node in enumerate(canvas["nodes"]):
    if node.get("id") in ["github-pages", "git-status", "deployment"]:
        canvas["nodes"][i] = pages_node
        break
else:
    canvas["nodes"].append(pages_node)

with open('TV_Internet_Projekt.canvas', 'w') as f:
    json.dump(canvas, f, indent=2)

print("✅ Canvas ažuriran - GitHub Pages u toku!")
