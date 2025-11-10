#!/bin/bash
echo "🔍 MONITORING TERMUX - TVInternetSBB"
cd ~/moje-zabele-ke-

echo "📥 Povlačim promene sa GitHuba..."
git pull origin main

echo "📦 Dodajem promene..."
git add .

echo "💾 Pravim commit..."
git commit -m "Termux sync: $(date '+%Y-%m-%d %H:%M:%S')" || echo "⚠️ Nema novih promena"

echo "🚀 Šaljem na GitHub..."
if git push origin main; then
    echo "✅ SINHRONIZACIJA USPELA!"
else
    echo "❌ SINHRONIZACIJA NEUSPEŠNA!"
    exit 1
fi

echo "🎉 SVE ZAVRŠENO!"
