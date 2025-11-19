#!/bin/bash
BACKUP_DATE=$(date +%Y%m%d_%H%M%S)
echo "💾 Kreiranje backup-a: $BACKUP_DATE"

# Backup server koda
ssh sbb-server "tar -czf /home/Produkcija2018/backup_${BACKUP_DATE}.tar.gz /home/Produkcija2018/tv-internet-sbb/ 2>/dev/null"

# Preuzmi backup lokalno
scp sbb-server:/home/Produkcija2018/backup_${BACKUP_DATE}.tar.gz ~/sbb-project/backup/

echo "✅ Backup kreiran: backup_${BACKUP_DATE}.tar.gz"
