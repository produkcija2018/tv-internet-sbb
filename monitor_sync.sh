#!/bin/bash
echo "🔍 MONITORING TERMUX"
cd ~/moje-zabele-ke-
git pull origin main
git add .
git commit -m "Termux sync: $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
echo "✅ ZAVRŠENO"
