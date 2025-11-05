U Termux-u ukucaj:

# Idi u tvoj vault folder

cd
"/storage/emulated/0/Documents/moje-zabele-ke-/TV_Internet_Projekt.canvas"

cd "/storage/emulated/0/Documents/moje-zabele-ke-"

# Proveri šta je u folderu
ls -la

# Kreiraj canvas fajl
touch "TV_Internet_Projekt.canvas"


# Otvori fajl u text editoru u Termux-u:

nano TV_Internet_Projekt.canvas

# Kopiraj CEo JSON kod iz mog prethodnog odgovora

U Termux nano editoru:

Drži prst dugo u terminalu

Izaberi "Paste"
------------------------------------------------------
{
  "nodes": [
    {
      "id": "central",
      "type": "text",
      "text": "# 🎯 TV & INTERNET PAKETI SAAS\n\n## 💰 Budžet: Minimalan\n## 🎯 Cilj: Profitabilan SaaS\n## 🛠️ Tehnologije: Obsidian + Termux + Git + AI\n## 📈 Metrike: Posete, Konverzije, Klijenti",
      "x": 0,
      "y": 0,
      "width": 400,
      "height": 300,
      "color": "4"
    },
    {
      "id": "trenutna-nedelja",
      "type": "text",
      "text": "## 🧩 TEKUĆA NEDELJA\n\n- [ ] GitHub Repozitorijum\n- [ ] GitHub Pages Setup\n- [ ] Obsidian Git Plugin\n- [ ] Osnovna struktura sajta\n- [ ] Prvi deploy test",
      "x": -800,
      "y": -200,
      "width": 300,
      "height": 250,
      "color": "1"
    },
    {
      "id": "sledeca-nedelja",
      "type": "text",
      "text": "## 📅 SLEDEĆA NEDELJA\n\n- [ ] Telegram Bot registracija\n- [ ] Osnovne AI komande\n- [ ] Baza čestih pitanja\n- [ ] Kontakt forma",
      "x": -800,
      "y": 100,
      "width": 300,
      "height": 220,
      "color": "1"
    },
    {
      "id": "u-toku",
      "type": "text",
      "text": "## 🟡 U TOKU\n\n• GitHub Pages konfiguracija\n• Canvas setup",
      "x": 600,
      "y": -200,
      "width": 250,
      "height": 180,
      "color": "3"
    },
    {
      "id": "zavrseno",
      "type": "text",
      "text": "## ✅ ZAVRŠENO\n\n• GitHub nalog kreiran\n• Canvas template napravljen",
      "x": 600,
      "y": 50,
      "width": 250,
      "height": 180,
      "color": "2"
    },
    {
      "id": "resursi",
      "type": "text",
      "text": "## 📚 RESURSI\n\n• [GitHub Repozitorijum]()\n• [GitHub Pages Docs](https://docs.github.com/pages)\n• [Telegram Bot API](https://core.telegram.org/bots)\n• [Python Tutorial](https://docs.python.org)",
      "x": -800,
      "y": 400,
      "width": 280,
      "height": 220,
      "color": "5"
    },
    {
      "id": "ideje",
      "type": "text",
      "text": "## 💡 IDEJE ZA BUDUĆNOST\n\n• AI automatsko odgovaranje\n• SMS notifikacije\n• Payment integracija\n• Mobile app\n• YouTube kanal sa uputstvima",
      "x": 600,
      "y": 300,
      "width": 280,
      "height": 220,
      "color": "6"
    },
    {
      "id": "kontakt",
      "type": "text",
      "text": "## 📞 KONTAKT FORMA IDEJE\n\n• Ime i prezime\n• Email\n• Telefon\n• Interesovanje (TV/Internet)\n• Poruka\n• AI auto-odgovor",
      "x": -400,
      "y": 300,
      "width": 280,
      "height": 200,
      "color": "7"
    },
    {
      "id": "baza-pitanja",
      "type": "text",
      "text": "## ❓ BAZA PITANJA ZA AI\n\n• Koji su paketi dostupni?\n• Koliko košta instalacija?\n• Imam li ugovornu obavezu?\n• Kako funkcioniše prelazak?\n• Koji kanali su uključeni?",
      "x": -400,
      "y": 550,
      "width": 280,
      "height": 200,
      "color": "8"
    }
  ],
  "edges": [
    {
      "fromNode": "trenutna-nedelja",
      "fromSide": "right",
      "toNode": "central",
      "toSide": "left"
    },
    {
      "fromNode": "sledeca-nedelja",
      "fromSide": "right",
      "toNode": "central",
      "toSide": "left"
    },
    {
      "fromNode": "u-toku",
      "fromSide": "left",
      "toNode": "central",
      "toSide": "right"
    },
    {
      "fromNode": "zavrseno",
      "fromSide": "left",
      "toNode": "central",
      "toSide": "right"
    },
    {
      "fromNode": "resursi",
      "fromSide": "right",
      "toNode": "central",
      "toSide": "left"
    },
    {
      "fromNode": "ideje",
      "fromSide": "left",
      "toNode": "central",
      "toSide": "right"
    },
    {
      "fromNode": "kontakt",
      "fromSide": "right",
      "toNode": "central",
      "toSide": "left"
    },
    {
      "fromNode": "baza-pitanja",
      "fromSide": "right",
      "toNode": "central",
      "toSide": "left"
    }
  ]
}

-------------------------------
Ctrl+X → Y → Enter da sačuvaš


python3 tv_internet_sbb_complete.py
