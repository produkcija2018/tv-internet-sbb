### **Korak 1: GitHub Nalog**

**📍 Gde:** Web browser na telefonu

text

1. Otvorite: https://github.com
2. Kliknite "Sign up"
3. Unesite: email, password, username
4. Potvrdite email
5. Kreirajte novi repozitorijum:
   - Kliknite "+" → "New repository"
   - Ime: "moje-zabeleške"
   - Public (besplatno)
   - ✅ "Add a README.md"
### **Korak 2: Termux Setup**

**📍 Gde:** Termux aplikacija

bash

# Unesite ove komande u Termux:
pkg update && pkg upgrade
pkg install git openssh
termux-setup-storage

### **Korak 3: SSH Ključ**
**📍 Gde:** Termux

bash

# Generisanje SSH ključa
ssh-keygen -t ed25519 -C "tvoj_email@gmail.com"
# Pritisni ENTER 3 puta za sve podrazumevano

# Prikaz javnog ključa
cat ~/.ssh/id_ed25519.pub
**📍 Sada idite na GitHub:**

1. `https://github.com/settings/keys`
    
2. "New SSH key"
    
3. Title: "Android Phone"
    
4. Nalepite ključ iz Termux-a
    
5. "Add SSH key"
### **Korak 4: Git Repozitorijum**
**📍 Gde:** Termux

bash

# Kloniranje repozitorijuma
cd ~/storage/shared/
git clone git@github.com:tvoj_username/moje-zabeleške.git Obsidian-Vault

# Provera
cd Obsidian-Vault
ls -la  # treba da vidite README.md