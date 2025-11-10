#!/bin/bash
cd ~/moje-zabele-ke- && git pull && git add . && git commit -m "Quick: $(date)" && git push
echo "✅ Quick sync done"
