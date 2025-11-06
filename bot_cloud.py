import os
import logging
import sqlite3
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Učitaj environment variables
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Database setup
def init_db():
    conn = sqlite3.connect('sbb_leads.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leads
                 (id INTEGER PRIMARY KEY, 
                  name TEXT, phone TEXT, package TEXT,
                  timestamp TEXT, status TEXT DEFAULT 'new')''')
    conn.commit()
    return conn

# Bot handlers (isti kao prethodni)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    
    keyboard = [
        ['📺 TV Paketi', '🌐 Internet Paketi'],
        ['🔥 Kombinovani Paket', '💰 Cene i Akcije'],
        ['💬 Kontakt Podrška', '🔧 Instalacija']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        f'👋 **Dobrodošao/la {user.first_name}!**\n\n'
        'Ja sam **TVInternetSBB asistent** 🤖\n'
        'Pomoći ću Vam da odaberete najbolji TV i internet paket!\n\n'
        '🎯 **Izaberite opciju ispod:**',
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Ostali handleri (tv_command, internet_command, itd.) ostaju isti
# Kopiraj ih iz tv_internet_sbb_complete.py

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    
    if text == '📺 TV Paketi':
        await update.message.reply_text(
            '📺 **TV PAKETI:**\n\n'
            '• Osnovni paket: 1.990 RSD\n'
            '• Sportski paket: 2.490 RSD\n' 
            '• Premium paket: 2.990 RSD\n\n'
            '📞 Detalji: 011/123-456',
            parse_mode='Markdown'
        )
    elif text == '🌐 Internet Paketi':
        await update.message.reply_text(
            '🌐 **INTERNET PAKETI:**\n\n'
            '• 100 Mbps: 1.490 RSD\n'
            '• 300 Mbps: 2.290 RSD\n'
            '• 1 Gbps: 3.490 RSD\n\n'
            '📞 Detalji: 011/123-456',
            parse_mode='Markdown'
        )
    elif text == '🔥 Kombinovani Paket':
        await update.message.reply_text(
            '🔥 **KOMBINOVANI PAKET:**\n\n'
            'TV + Internet: 2.990 RSD\n'
            '🎁 Ušteda 30%!\n\n'
            '📞 Detalji: 011/123-456',
            parse_mode='Markdown'
        )
    elif text == '💰 Cene i Akcije':
        await update.message.reply_text(
            '💰 **CENE I AKCIJE:**\n\n'
            'Prvi mesec 50% popusta!\n'
            'Besplatna instalacija!\n'
            'Nema ugovorne obaveze!\n\n'
            '📞 011/123-456',
            parse_mode='Markdown'
        )
    elif text == '💬 Kontakt Podrška':
        await update.message.reply_text(
            '💬 **KONTAKT:**\n\n'
            '📞 011/123-456\n'
            '📧 info@tvinternetsbb.rs\n'
            '🕒 08-20h\n\n'
            '🌐 https://produkcija2018.github.io/tv-internet-sbb/',
            parse_mode='Markdown'
        )
    elif text == '🔧 Instalacija':
        await update.message.reply_text(
            '🔧 **INSTALACIJA:**\n\n'
            'Besplatna instalacija!\n'
            'Termin za 24h!\n'
            'Profesionalni tehničari!\n\n'
            '📞 011/123-456',
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_text(
            '🤖 Hvala na poruci! Kontaktiraćemo vas.\n\n'
            '📞 011/123-456',
            parse_mode='Markdown'
        )

def main():
    # Initialize database
    init_db()
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    print("🚀 TVInternetSBB Bot starting on CLOUD...")
    application.run_polling()

if __name__ == '__main__':
    main()
