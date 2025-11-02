
---

## ⚡ **FAZA 5: AUTOMATIZACIJA**

**Kreirajte notu:** "⚡ Faza 5 - Automatizacija.md"

```markdown
# ⚡ Faza 5 - Automatizacija

## 🔄 5.1 Sinhronizaciona Skripta

### U Termux-u:
```bash
# Idite u vault folder
cd ~/storage/shared/Obsidian-Vault

# Kreirajte sinhronizacionu skriptu
echo '#!/bin/bash
cd ~/storage/shared/Obsidian-Vault

echo "🔄 Počinjem sinhronizaciju..."
git add .

if git diff-index --quiet HEAD --; then
    echo "ℹ️ Nema novih promena"
else
    git commit -m "Sync: $(date +\"%Y-%m-%d %H:%M\")"
    git push
    echo "✅ Promene poslate na GitHub!"
fi

git pull
echo "🎉 Sinhronizacija završena!"' > sync.sh

# Omogući izvršavanje
chmod +x sync.sh
