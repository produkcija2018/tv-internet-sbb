### **Korak 7: Templates Folder**

**📍 Gde:** Termux
bash

# Kreiranje Templates foldera
cd ~/storage/shared/Obsidian-Vault
mkdir Templates

# Kreiranje prvog template-a
echo "# {{title}}

## Kontekst


## Ključne Tačke
- 

## Povezano sa
[[🏠 Home]]

---
*Kreirano: \$(date +'%Y-%m-%d %H:%M')*" > Templates/"🧩 Osnovni Template.md"

### **Korak 8: Templater Plugin**

**📍 Gde:** Obsidian Settings

text

1. Settings → Community plugins
2. Turn on community plugins
3. Browse → "Templater" → Install → Enable
4. Templater Settings → Template folder location
5. Izaberite "Templates" folder

### **Korak 9: Test Template-a**

**📍 Gde:** Obsidian

text

1. Command Palette (Ctrl+P)
2. Type: "Templater: Create new note from template"
3. Izaberite: "🧩 Osnovni Template"
4. Unesite ime: "Test Nota"
5. ✅ Kreira se nova nota sa template-om!
