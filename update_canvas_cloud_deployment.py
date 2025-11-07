import json

with open('TV_Internet_Projekt.canvas', 'r') as f:
    canvas = json.load(f)

# Ažuriraj sa cloud deployment statusom
cloud_node = {
    "id": "cloud-deployment",
    "type": "text",
    "text": "## ☁️ CLOUD DEPLOYMENT\n\n### 🚀 SPREMNO ZA HOSTING\n\n**Status:** Fajlovi pripremljeni\n**Bot:** bot_cloud.py optimizovan\n**Requirements:** requirements.txt kreiran\n\n### Cloud Opcije:\n1. PythonAnywhere (preporučeno)\n2. Railway.app (moderno)\n3. Render.com (jednostavno)\n\n### Prednosti Cloud-a:\n- ✅ 24/7 rad bota\n- ✅ Automatski restart\n- ✅ Bez brige o bateriji\n- ✅ Profesionalni hosting\n- ✅ Scalability\n\n### Sledeći korak:\nOdabir cloud provajdera i deploy!",
    "x": 600,
    "y": 150,
    "width": 400,
    "height": 380,
    "color": "4"
}

# Pronađi i zameni cloud karticu
for i, node in enumerate(canvas["nodes"]):
    if node.get("id") in ["cloud-hosting", "cloud-deployment"]:
        canvas["nodes"][i] = cloud_node
        break
else:
    canvas["nodes"].append(cloud_node)

with open('TV_Internet_Projekt.canvas', 'w') as f:
    json.dump(canvas, f, indent=2)

print("✅ Canvas ažuriran - Cloud deployment spreman!")
