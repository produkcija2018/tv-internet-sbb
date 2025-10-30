#!/bin/bash
cd ~/storage/shared/Documents/moje-zabele-ke-

echo "🔄 Proveravam promene..."
git add .

if git diff-index --quiet HEAD --; then
    echo "ℹ️ Nema novih promena za commit."
elseecho "📝 Pravim commit..."
    git commit -m "Sync: $(date +'%Y-%m-%d %H:%M:%S')"
    git push
    echo "✅ Promene poslate na GitHub!"
fi

echo "📥 Povlačim promene sa GitHub-a..."
git pull

echo "🎉 Sinhronizacija završena!"
