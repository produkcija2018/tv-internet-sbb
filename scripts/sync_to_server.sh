#!/bin/bash
echo "🔄 Sinhronizacija koda na server..."
rsync -avz --delete \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    --exclude='.git' \
    --exclude='logs/*' \
    ~/sbb-project/ sbb-server:/home/Produkcija2018/tv-internet-sbb/

echo "✅ Kod uspešno sinhronizovan!"
echo "📊 Status:"
ssh sbb-server "ls -la /home/Produkcija2018/tv-internet-sbb/"
