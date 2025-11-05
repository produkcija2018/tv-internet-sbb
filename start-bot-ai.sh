#!/data/data/com.termux/files/usr/bin/bash

cd "/storage/emulated/0/Documents/moje-zabele-ke"

echo "Pokrećem AI Telegram bota..."
python3 bot_ai.py

# Ako bot padne, pokušaj ponovo za 30 sekundi
while true; do
    echo "Bot je pao, restartujem za 30 sekundi..."
    sleep 30
    python3 bot_ai.py
done
