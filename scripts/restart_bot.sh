#!/bin/bash
echo "🔄 Restartovanje bota..."
ssh sbb-server "touch /var/www/produkcija2018_pythonanywhere_com_wsgi.py"
sleep 3
echo "✅ Bot restartovan!"

# Proveri status
echo "📡 Provera statusa..."
ssh sbb-server "curl -s https://produkcija2018.pythonanywhere.com/health"
