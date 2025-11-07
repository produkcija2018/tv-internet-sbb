# bot_with_stats.py - AŽURIRANA VERZIJA SA STATISTIKOM
import os
import logging
import sqlite3
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from database_manager import DatabaseManager  # DODATO

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Database setup - DODATO
db = DatabaseManager()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    
    keyboard = [
        ['📺 TV Paketi', '🌐 Internet Paketi'],
        ['🔥 Kombinovani Paket', '💰 Cene i Akcije'],
        ['💬 Kontakt Podrška', '🔧 Instalacija'],
        ['📊 Statistika']  # DODATO
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

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    
    # DODATO: Handler za statistiku
    if text == '📊 Statistika':
        if str(update.message.from_user.id) == ADMIN_CHAT_ID:
            stats = db.get_lead_stats()
            daily = db.get_daily_stats()
            
            message = (
                "📊 **STATISTIKA LEADOVA**\n\n"
                f"• Novi leadovi: {stats['new_leads']}\n"
                f"• Kontaktirani: {stats['contacted_leads']}\n"
                f"• Ukupno leadova: {stats['total_leads']}\n\n"
                f"📈 **DANAŠNJA STATISTIKA**\n"
                f"• Obradjene poruke: {daily['messages_processed']}\n"
                f"• Novi leadovi danas: {daily['new_leads']}\n"
            )
            await update.message.reply_text(message, parse_mode='Markdown')
        else:
            await update.message.reply_text("❌ Samo administrator može videti statistiku.")
        return
    
    # Ostali handleri ostaju isti
    responses = {
        '📺 TV Paketi': '📺 **TV PAKETI:**\n\n• Osnovni: 1.990 RSD\n• Sportski: 2.490 RSD\n• Premium: 2.990 RSD\n\n📞 011/123-456',
        '🌐 Internet Paketi': '🌐 **INTERNET PAKETI:**\n\n• 100 Mbps: 1.490 RSD\n• 300 Mbps: 2.290 RSD\n• 1 Gbps: 3.490 RSD\n\n📞 011/123-456',
        '🔥 Kombinovani Paket': '🔥 **KOMBINOVANI:**\n\nTV + Internet: 2.990 RSD\n🎁 Ušteda 30%!\n\n📞 011/123-456',
        '💰 Cene i Akcije': '💰 **AKCIJE:**\n\nPrvi mesec 50% popusta!\nBesplatna instalacija!\n\n📞 011/123-456',
        '💬 Kontakt Podrška': '💬 **KONTAKT:**\n\n📞 011/123-456\n📧 info@sbb.rs\n🕒 08-20h',
        '🔧 Instalacija': '🔧 **INSTALACIJA:**\n\nBesplatna!\nTermin za 24h!\n\n📞 011/123-456'
    }
    
    if text in responses:
        await update.message.reply_text(responses[text], parse_mode='Markdown')
    else:
        await update.message.reply_text(
            '🤖 Hvala na poruci! Kontaktiraćemo vas.\n\n📞 011/123-456',
            parse_mode='Markdown'
        )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🚀 TVInternetSBB Bot with STATS starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
