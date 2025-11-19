#!/bin/bash
echo "🤖 Provera stanja bota..."
STATUS=$(ssh sbb-server "curl -s https://produkcija2018.pythonanywhere.com/health 2>/dev/null || echo 'error'")

if echo "$STATUS" | grep -q "healthy"; then
    echo "✅ Bot radi normalno: $(date)"
    termux-notification --title "🤖 TVInternetSBB" --content "Bot radi normalno"
else
    echo "🚨 BOT PAO! $(date)"
    termux-notification --title "🚨 TVInternetSBB Alert" --content "Bot je pao! Restartujem..."

    # Restartuj bot
    ~/sbb-project/scripts/restart_bot.sh
fi
