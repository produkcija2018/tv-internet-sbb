### **Korak 10: Sinhronizacija Skripta**

**📍 Gde:** Termux

bash

# Kreiranje sinhronizacione skripte
cd ~/storage/shared/Obsidian-Vault

echo '#!/bin/bash
cd ~/storage/shared/Obsidian-Vault
git add .
git commit -m "Sync: $(date +\"%Y-%m-%d %H:%M\")"
git push
git pull
echo "✅ Sinhronizovano!"' > sync.sh

chmod +x sync.sh

### **Korak 11: Termux Widget**

**📍 Gde:** Termux
bash

# Kreiranje widget skripte
mkdir -p ~/.shortcuts
echo '#!/bin/bash
cd ~/storage/shared/Obsidian-Vault
./sync.sh
termux-vibrate -d 300 2>/dev/null' > ~/.shortcuts/sync-notes

chmod +x ~/.shortcuts/sync-notes

**📍 Sada na Home Screenu:**
text

1. Dug pritisak na prazno
2. Widgets → Termux Widget
3. Prevucite na home screen
4. Kliknite na widget da sinhronizujete

