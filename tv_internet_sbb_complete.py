import logging
import re
import sqlite3
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ===== KONFIGURACIJA =====
BOT_TOKEN = "8105923056:AAFdk-iRcIgmVGHxdAE7R-qhTNoq7WbRTW0"
ADMIN_CHAT_ID = "123456789"

# ===== BAZA PODATAKA =====
def init_db():
    conn = sqlite3.connect('sbb_leads.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leads
                 (id INTEGER PRIMARY KEY, 
                  name TEXT, phone TEXT, package TEXT,
                  timestamp TEXT, status TEXT DEFAULT 'new')''')
    conn.commit()
    conn.close()

# ===== LOGOVANJE =====
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===== KOMANDE =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    logger.info(f"User {user.id} started bot")
    
    keyboard = [
        ['📺 TV Paketi', '🌐 Internet Paketi'],
        ['🔥 Kombinovani', '💰 Cene i Akcije'],
        ['💬 Kontakt', '🔧 Instalacija']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        f'👋 **Dobrodošao/la {user.first_name}!**\n\n'
        'Ja sam **TVInternetSBB asistent** 🤖\n'
        'Pomoći ću Vam da odaberete najbolji TV i internet paket!\n\n'
        '🎯 **Izaberite opciju ispod ili upotrebite komande:**\n'
        '/tv - TV paketi\n'
        '/internet - Internet paketi\n' 
        '/cene - Cene i akcije\n'
        '/kontakt - Kontakt podrška\n'
        '/help - Pomoć',
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def tv_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '📺 **TV PAKETI:**\n\n'
        '• **Osnovni paket** - 1.990 RSD/mesec\n'
        '   - 200+ kanala u HD kvalitetu\n'
        '   - 15 sportskih kanala\n'
        '   - 10 filmskih kanala\n'
        '   - Besplatna instalacija\n\n'
        '• **Sportski paket** - 2.490 RSD/mesec\n'
        '   - Sve iz Osnovnog paketa +\n'
        '   - Dodatnih 35 sportskih kanala\n'
        '   - Arena Sport, Sport Klub, ESPN\n\n'
        '• **Premium paket** - 2.990 RSD/mesec\n'
        '   - Svi kanali iz prethodnih paketa +\n'
        '   - HBO, Cinemax, Fox Movies\n'
        '   - National Geographic, Discovery\n\n'
        '🔥 **Prvi mesec 50% popusta!**',
        parse_mode='Markdown'
    )

async def internet_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '🌐 **INTERNET PAKETI:**\n\n'
        '• **100 Mbps** - 1.490 RSD/mesec\n'
        '   - Idealno za surfing, email\n'
        '   - Streaming (YouTube, Netflix)\n'
        '   - Do 5 uređaja istovremeno\n\n'
        '• **300 Mbps** - 2.290 RSD/mesec\n'
        '   - Za zahtevnije korisnike\n'
        '   - 4K streaming, gaming\n'
        '   - Do 10 uređaja istovremeno\n\n'
        '• **1 Gbps** - 3.490 RSD/mesec\n'
        '   - Najbrža dostupna opcija\n'
        '   - Profesionalni gaming\n'
        '   - Do 20+ uređaja istovremeno\n\n'
        '🔧 **Besplatna instalacija uključena!**',
        parse_mode='Markdown'
    )

async def cene_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '💰 **CENE I AKCIJE:**\n\n'
        '📺 **TV PAKETI:**\n'
        '• Osnovni: 1.990 RSD → **1.490 RSD** (prvi mesec)\n'
        '• Sportski: 2.490 RSD → **1.990 RSD** (prvi mesec)\n'  
        '• Premium: 2.990 RSD → **2.290 RSD** (prvi mesec)\n\n'
        '🌐 **INTERNET:**\n'
        '• 100 Mbps: 1.490 RSD\n'
        '• 300 Mbps: 2.290 RSD\n'
        '• 1 Gbps: 3.490 RSD\n\n'
        '🔥 **KOMBINOVANI:**\n'
        '• TV + Internet: 2.990 RSD → **2.290 RSD** (prvi mesec)\n\n'
        '🎁 **Akcije:**\n'
        '• Prvi mesec 50% popusta\n'
        '• Besplatna instalacija\n'
        '• WiFi ruter u paketu\n'
        '• Nema ugovorne obaveze',
        parse_mode='Markdown'
    )

async def kontakt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '💬 **KONTAKT PODRŠKA:**\n\n'
        '📞 **Telefon:** 011/123-456\n'
        '🕒 **Radno vreme:** 08-20h (svaki dan)\n'
        '📧 **Email:** info@tvinternetsbb.rs\n'
        '📍 **Adresa:** Beograd, Srbija\n\n'
        '🔧 **Tehnička podrška:** 064/123-4567\n'
        '📋 **Prodaja:** 011/123-456\n\n'
        '🚗 **Besplatna instalacija na teritoriji Beograda!**',
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '❓ **POMOĆ - Kako koristiti bota:**\n\n'
        '• Kliknite na dugmiće ispod za brzi odabir\n'
        '• Ili upotrebite komande:\n'
        '  /start - Pokreni bota\n'
        '  /tv - TV paketi\n'
        '  /internet - Internet paketi\n'
        '  /cene - Cene i akcije\n'
        '  /kontakt - Kontakt podrška\n\n'
        '🤖 **Mogućnosti bota:**\n'
        '• Automatski odgovori na pitanja\n'
        '• Prikaz TV i internet paketa\n'
        '• Informacije o cenama i akcijama\n'
        '• Kontakt informacije\n'
        '• Dostupan 24/7',
        parse_mode='Markdown'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    text = update.message.text
    
    if text == '📺 TV Paketi':
        await tv_command(update, context)
    elif text == '🌐 Internet Paketi':
        await internet_command(update, context)
    elif text == '🔥 Kombinovani':
        await update.message.reply_text(
            '🔥 **KOMBINOVANI PAKET - Ušteda 30%!**\n\n'
            '📺🌐 **TV + INTERNET 300 Mbps** - 2.990 RSD/mesec\n\n'
            '🎁 **Šta dobijate:**\n'
            '• TV Premium paket (250+ kanala)\n'
            '• Internet 300 Mbps brzina\n'
            '• Besplatna instalacija oba paketa\n'
            '• WiFi ruter (besplatno)\n'
            '• 24/7 premium podrška\n\n'
            '💰 **Ušteda:** 1.490 RSD mesečno!\n'
            '🎯 **Vrednost:** 4.480 RSD → **2.990 RSD**',
            parse_mode='Markdown'
        )
    elif text == '💰 Cene i Akcije':
        await cene_command(update, context)
    elif text == '💬 Kontakt':
        await kontakt_command(update, context)
    elif text == '🔧 Instalacija':
        await update.message.reply_text(
            '🔧 **INSTALACIJA:**\n\n'
            '🏠 **Šta uključuje instalacija:**\n'
            '• Postavljanje TV prijemnika\n'
            '• Podešavanje svih kanala\n'
            '• Instalacija WiFi rutera\n'
            '• Podešavanje mreže\n'
            '• Obuka korišćenja\n\n'
            '⏰ **Vreme instalacije:**\n'
            '• Termin u roku od 24h\n'
            '• Instalacija traje 1-2 sata\n'
            '• Radimo svakim danom 08-20h\n\n'
            '🎁 **BESPLATNA INSTALACIJA uz svaki paket!**\n'
            '(vrednost 5.000 RSD)\n\n'
            '📞 **Zakažite termin:** 011/123-456',
            parse_mode='Markdown'
        )
    else:
        # AI odgovori na pitanja
        response = None
        text_lower = text.lower()
        
        if 'koliko košta' in text_lower or 'cijena' in text_lower:
            response = '💰 **CJENE PAKETA:**\n📺 TV: 1.990-2.990 RSD\n🌐 Internet: 1.490-3.490 RSD\n🔥 Kombinovani: 2.990 RSD\n\n🎁 Prvi mesec 50% popusta!'
        elif 'kanali' in text_lower:
            response = '📡 **TV KANALI:**\n200+ kanala\nSport, filmovi, dečji\nHD kvalitet'
        elif 'internet' in text_lower or 'brzina' in text_lower:
            response = '🌐 **INTERNET:**\n100 Mbps: 1.490 RSD\n300 Mbps: 2.290 RSD\n1 Gbps: 3.490 RSD'
        elif 'hvala' in text_lower or 'ćao' in text_lower:
            response = '🤝 Hvala Vam! Za više informacija pozovite 011/123-456'
        
        if response:
            await update.message.reply_text(response, parse_mode='Markdown')
        else:
            await update.message.reply_text(
                '🤖 Hvala na poruci! 🎉\n\n'
                'Naš operator će vas kontaktirati u roku od 24h.\n\n'
                'Za hitna pitanja pozovite: **011/123-456**',
                parse_mode='Markdown'
            )

def main():
    init_db()
    
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Dodaj komande
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("tv", tv_command))
        application.add_handler(CommandHandler("internet", internet_command))
        application.add_handler(CommandHandler("cene", cene_command))
        application.add_handler(CommandHandler("kontakt", kontakt_command))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("🤖 TVInternetSBB Bot sa komandama pokrenut!")
        print("🚀 Bot sa komandama pokrenut!")
        print("📱 Sada bi trebalo da ima meni u Telegramu!")
        
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Bot error: {e}")
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
