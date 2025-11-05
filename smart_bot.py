import logging
import re
import json
import sqlite3
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# ===== KONFIGURACIJA =====
BOT_TOKEN = "YOUR_NEW_TOKEN_HERE"  # Zameni sa pravim tokenom
ADMIN_CHAT_ID = "123456789"  # Zameni sa tvojim chat ID

# ===== BAZA PODATAKA =====
def init_db():
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leads
                 (id INTEGER PRIMARY KEY, 
                  name TEXT, phone TEXT, package TEXT,
                  timestamp TEXT, status TEXT DEFAULT 'new')''')
    conn.commit()
    conn.close()

def save_lead(name, phone, package):
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute("INSERT INTO leads (name, phone, package, timestamp) VALUES (?, ?, ?, ?)",
              (name, phone, package, datetime.now().isoformat()))
    conn.commit()
    conn.close()

# ===== LOGOVANJE =====
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("smart_bot.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ===== AI ODOOVORI =====
knowledge_base = {
    r'koliko košta|cijena|cijene': '''
💰 **CJENE PAKETA:**

📺 TV PAKETI:
• Osnovni (200+ kanala): 1.990 RSD/mesec
• Sportski (+50 sportskih): 2.490 RSD/mesec  
• Premium (svi kanali): 2.990 RSD/mesec

🌐 INTERNET:
• 100 Mbps: 1.490 RSD/mesec
• 300 Mbps: 2.290 RSD/mesec  
• 1 Gbps: 3.490 RSD/mesec

🔥 KOMBINOVANI (ušteda 30%):
• TV + Internet: 2.990 RSD/mesec

🎁 **Akcija:** Prvi mesec 50% popusta!
''',

    r'kanali|koji kanali|program': '''
📡 **TV KANALI (200+):**

🏈 **SPORT:** Arena Sport, Sport Klub, ESPN
🎬 **FILMOVI:** HBO, Cinemax, Fox Movies
👨‍👩‍👧‍👦 **PORODIČNI:** RTS, Happy, Prva, B92
🔬 **EDUKATIVNI:** National Geographic, Discovery
🎵 **MUZIKA:** MTV, VH1, Music Box

📺 **Svi kanali u HD kvalitetu!**
''',

    r'internet|brzina|mbps': '''
🌐 **INTERNET PAKETI:**

⚡ **100 Mbps** - 1.490 RSD
• Idealno za surfing, email, društvene mreže
• Do 5 uređaja istovremeno

🚀 **300 Mbps** - 2.290 RSD  
• Savršeno za streaming (Netflix, YouTube)
• Rad od kuće, online časovi
• Do 10 uređaja

🎯 **1 Gbps** - 3.490 RSD
• Za gaming, 4K streaming, velike porodice
• Neograničen protok
• Do 20+ uređaja

🔧 **Besplatna instalacija uključena!**
''',

    r'ugovor|obaveza|otkaz': '''
📝 **UGOVORNA OBAVEZA:**

✅ **NEMA UGOVORNE OBAVEZE!**
✅ Možete otkazati BILO KADA
✅ 30-dnevni rok otkaza
✅ Nema skrivenih troškova

🆓 **Probni period:** 14 dana
💰 **Povrat novca** ako niste zadovoljni
''',

    r'instalacija|montaža|postavljanje': '''
🔧 **INSTALACIJA:**

🏠 **Besplatna instalacija** uz svaki paket
⏰ **Termin za 24h** od narudžbine
👨‍🔧 **Profesionalni tehničari**
📶 **WiFi ruter u paketu** (besplatno)

🌍 **Područje rada:** Ceo Beograd
🕒 **Radno vreme instalacija:** 08-20h
''',

    r'hvala|ćao|pozdrav|zbogom': '''
🤝 **Hvala Vam na poverenju!**

Ako imate još pitanja, slobodno nas kontaktirajte:
📞 011/123-456
📱 @tv_internet_helper_bot

🌐 **Website:** TVInternet.rs
'''
}

# ===== TELEGRAM BOT HANDLERI =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    logger.info(f"User {user.id} ({user.first_name}) started bot")
    
    keyboard = [
        ['📺 TV Paketi', '🌐 Internet Paketi'],
        ['🔥 Kombinovani Paket', '💰 Cene i Akcije'],
        ['💬 Kontakt Podrška', '🔧 Instalacija']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    welcome_text = f'''
👋 **Dobrodošao/la {user.first_name}!**

Ja sam **TVInternet.rs asistent** 🤖
Pomoći ću Vam da odaberete najbolji TV i internet paket za vaše potrebe.

🎯 **Izaberite opciju ispod ili mi postavite pitanje:**
'''
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    text = update.message.text
    logger.info(f"User {user.id}: {text}")
    
    # AI odgovori iz baze znanja
    response = None
    text_lower = text.lower()
    
    for pattern, answer in knowledge_base.items():
        if re.search(pattern, text_lower):
            response = answer
            break
    
    if response:
        await update.message.reply_text(response, parse_mode='Markdown')
    elif text == '📺 TV Paketi':
        await send_tv_packages(update, context)
    elif text == '🌐 Internet Paketi':
        await send_internet_packages(update, context)
    elif text == '🔥 Kombinovani Paket':
        await send_combined_package(update, context)
    elif text == '💰 Cene i Akcije':
        await send_prices(update, context)
    elif text == '💬 Kontakt Podrška':
        await send_contact(update, context)
    elif text == '🔧 Instalacija':
        await send_installation_info(update, context)
    else:
        # Ako ne prepoznaje pitanje, ponudi kontakt
        keyboard = [[InlineKeyboardButton("📞 Pozovite nas", callback_data="call")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            '🤖 Hvala na poruci! 🎉\n\n'
            'Naš operator će vas kontaktirati u roku od 24h.\n\n'
            'Za hitna pitanja:',
            reply_markup=reply_markup
        )

async def send_tv_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '''
📺 **TV PAKETI - Detaljna Ponuda:**

🎯 **OSNOVNI PAKET** - 1.990 RSD
• 200+ kanala u HD kvalitetu
• 15 sportskih kanala
• 10 filmskih kanala  
• 5 dečjih kanala
• Besplatna instalacija

⚽ **SPORTSKI PAKET** - 2.490 RSD  
• Sve iz Osnovnog paketa +
• Dodatnih 35 sportskih kanala
• Arena Sport, Sport Klub, ESPN
• Savršeno za ljubitelje sporta

🎬 **PREMIUM PAKET** - 2.990 RSD
• Svi kanali iz prethodnih paketa +
• HBO, Cinemax, Fox Movies
• National Geographic, Discovery
• Ukupno preko 250 kanala

🔥 **Akcija:** Prvi mesec 50% popusta!
'''
    
    keyboard = [
        [InlineKeyboardButton("📞 Želim Osnovni TV", callback_data="tv_basic")],
        [InlineKeyboardButton("⚽ Želim Sportski TV", callback_data="tv_sports")],
        [InlineKeyboardButton("🎬 Želim Premium TV", callback_data="tv_premium")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

async def send_internet_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '''
🌐 **INTERNET PAKETI - Detaljna Ponuda:**

🚀 **100 MBPS** - 1.490 RSD/mesec
• Idealno za osnovno korišćenje
• Streaming (YouTube, Netflix)
• Rad od kuće, online časovi
• Do 5 uređaja istovremeno

⚡ **300 MBPS** - 2.290 RSD/mesec  
• Za zahtevnije korisnike
• 4K streaming, gaming
• Veliki prenos podataka
• Do 10 uređaja istovremeno

🎯 **1 GBPS** - 3.490 RSD/mesec
• Najbrža dostupna opcija
• Profesionalni gaming
• Velike porodice, stanovi
• Do 20+ uređaja istovremeno

🔧 **Svi paketi uključuju:**
• Besplatnu instalaciju
• WiFi ruter (besplatno)
• Neograničen protok
• 24/7 tehničku podršku
'''
    
    keyboard = [
        [InlineKeyboardButton("🚀 Želim 100 Mbps", callback_data="inet_100")],
        [InlineKeyboardButton("⚡ Želim 300 Mbps", callback_data="inet_300")],
        [InlineKeyboardButton("🎯 Želim 1 Gbps", callback_data="inet_1000")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

async def send_combined_package(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '''
🔥 **KOMBINOVANI PAKET - Ušteda 30%!**

📺🌐 **TV + INTERNET 300 Mbps** - 2.990 RSD/mesec

🎁 **Šta dobijate:**
• TV Premium paket (250+ kanala)
• Internet 300 Mbps brzina
• Besplatna instalacija oba paketa
• WiFi ruter (besplatno)
• 24/7 premium podrška

💰 **Ušteda:** 1.490 RSD mesečno!
🎯 **Vrednost:** 4.480 RSD → **2.990 RSD**

⚡ **Najpopularniji izbor naših klijenata!**
'''
    
    keyboard = [[InlineKeyboardButton("🔥 Želim Kombinovani Paket", callback_data="combined")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

async def send_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '''
💰 **CENE I AKCIJE - Pregled**

📺 **TV PAKETI:**
• Osnovni: 1.990 RSD → **1.490 RSD** (prvi mesec)
• Sportski: 2.490 RSD → **1.990 RSD** (prvi mesec)  
• Premium: 2.990 RSD → **2.290 RSD** (prvi mesec)

🌐 **INTERNET:**
• 100 Mbps: 1.490 RSD
• 300 Mbps: 2.290 RSD
• 1 Gbps: 3.490 RSD

🔥 **KOMBINOVANI:**
• TV + Internet: 2.990 RSD → **2.290 RSD** (prvi mesec)

🎁 **SPECIJALNE AKCIJE:**
• Prvi mesec 50% popusta
• Besplatna instalacija (vrednost 5.000 RSD)
• WiFi ruter u paketu (vrednost 3.000 RSD)
• Nema ugovorne obaveze

📞 **Pozovite za još povoljnijim cenama!**
'''
    await update.message.reply_text(text, parse_mode='Markdown')

async def send_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '''
💬 **KONTAKT PODRŠKA:**

📞 **Telefon:** 011/123-456
🕒 **Radno vreme:** 08-20h (svaki dan)
📧 **Email:** info@tvinternet.rs
📍 **Adresa:** Beograd, Srbija

🔧 **Tehnička podrška:** 064/123-4567
📋 **Prodaja:** 011/123-456

🌐 **Website:** TVInternet.rs
🤖 **Telegram:** @tv_internet_helper_bot

🚗 **Besplatna instalacija** na teritoriji Beograda!
'''
    await update.message.reply_text(text, parse_mode='Markdown')

async def send_installation_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '''
🔧 **INSTALACIJA - Informacije**

🏠 **Šta uključuje instalacija:**
• Postavljanje TV prijemnika
• Podešavanje svih kanala
• Instalacija WiFi rutera
• Podešavanje mreže
• Obuka korišćenja

⏰ **Vreme instalacije:**
• Termin u roku od 24h
• Instalacija traje 1-2 sata
• Radimo svakim danom 08-20h

🎁 **BESPLATNA INSTALACIJA** uz svaki paket!
(vrednost 5.000 RSD)

📞 **Zakažite termin:** 011/123-456
'''
    await update.message.reply_text(text, parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    user = query.from_user
    data = query.data
    
    logger.info(f"Button click from {user.id}: {data}")
    
    # Mapiranje callback data na pakete
    package_map = {
        'tv_basic': ('Osnovni TV Paket', '1.990 RSD'),
        'tv_sports': ('Sportski TV Paket', '2.490 RSD'), 
        'tv_premium': ('Premium TV Paket', '2.990 RSD'),
        'inet_100': ('Internet 100 Mbps', '1.490 RSD'),
        'inet_300': ('Internet 300 Mbps', '2.290 RSD'),
        'inet_1000': ('Internet 1 Gbps', '3.490 RSD'),
        'combined': ('Kombinovani Paket', '2.990 RSD'),
        'call': ('Poziv', 'Kontakt')
    }
    
    if data in package_map:
        package_name, price = package_map[data]
        
        if data == 'call':
            await query.edit_message_text(
                f"📞 **Hvala {user.first_name}!**\n\n"
                f"Naš operator će vas pozvati u roku od 15 minuta.\n\n"
                f"💬 Možete i direktno pozvati: **011/123-456**",
                parse_mode='Markdown'
            )
        else:
            # Sačuvaj lead u bazi
            save_lead(user.first_name, 'nije uneo', package_name)
            
            await query.edit_message_text(
                f"🎉 **Hvala {user.first_name}!**\n\n"
                f"Odabrali ste: **{package_name}**\n"
                f"Cena: **{price}** mesečno\n\n"
                f"📞 Naš operator će vas kontaktirati u roku od 1h "
                f"da potvrdi detalje i zakaže instalaciju.\n\n"
                f"💬 Za hitan kontakt: **011/123-456**",
                parse_mode='Markdown'
            )
            
            # Obavesti admina o novom leadu
            try:
                await context.bot.send_message(
                    chat_id=ADMIN_CHAT_ID,
                    text=f"🎯 NOVI LEAD!\n\n"
                         f"Korisnik: {user.first_name} (@{user.username})\n"
                         f"Paket: {package_name}\n"
                         f"Cena: {price}\n"
                         f"Vreme: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                    parse_mode='Markdown'
                )
            except Exception as e:
                logger.error(f"Could not notify admin: {e}")

def main():
    # Inicijalizuj bazu
    init_db()
    
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Handleri
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button_handler))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("🤖 Smart Bot starting...")
        print("🚀 Ultra-pametni bot pokrenut!")
        print("📊 Baza podataka inicijalizovana")
        print("📝 Logovanje aktivirano")
        print("🎯 Spreman za leads!")
        
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Bot error: {e}")
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
