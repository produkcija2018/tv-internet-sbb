#!/bin/bash
echo "🤖 Pokrećem TVInternetSBB bot u pozadini..."
cd ~/moje-zabele-ke-
while true; do
    echo "$(date): Starting bot..."
    python3 bot_cloud.py
    echo "$(date): Bot stopped, restarting in 5 seconds..."
    sleep 5
done
