import logging
import re
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Podesi logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Baza znanja
knowledge_base = {
    r'koliko košta|cijena|cijene': '💰 **CJENE PAKETA:**\n\n• TV Osnovni: 1.990 RSD\n• Internet 100 Mbps: 1.490 RSD\n• Kombinovani: 2.990 RSD\n\n📞 Pozovite za popust!',
    r'kanali|koji kanali': '📡 **KANALI:**\n\nPreko 200 kanala:\n• Sport Klub, Arena\n• RTS, Happy, Prva\n• National Geographic',
    r'internet|brzina': '🌐 **INTERNET:**\n\nBrzine 100 Mbps - 1 Gbps\nBez ugovorne obaveze\n24/7 podrška',
    r'ugovor|obaveza': '📝 **UGOVOR:**\n\nNema ugovorne obaveze!\nMožete otkazati bilo kada',
    r'instalacija|montaža': '🔧 **INSTALACIJA:**\n\nBesplatna instalacija\nTermin u roku 24h',
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    logger.info(f"User {user.id} ({user.first_name}) started bot")
    
    keyboard = [
        ['📺 TV Paketi', '🌐 Internet'],
        ['💬 Podrška', '📞 Kontakt'],
        ['❓ Česta Pitanja']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        'Dobrodošli! 🎉\nJa sam AI asistent za TV i internet pakete.\n\nIzaberite opciju:',
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    text = update.message.text
    logger.info(f"User {user.id}: {text}")
    
    # AI odgovori
    response = None
    for pattern, answer in knowledge_base.items():
        if re.search(pattern, text.lower()):
            response = answer
            break
    
    if response:
        await update.message.reply_text(response, parse_mode='Markdown')
    elif text == '📺 TV Paketi':
        await update.message.reply_text(
            '📺 **TV PAKETI:**\n\n• Osnovni: 200 kanala - 1.990 RSD\n• Sportski: +50 sportskih - 2.490 RSD\n• Premium: svi kanali - 2.990 RSD',
            parse_mode='Markdown'
        )
    elif text == '🌐 Internet':
        await update.message.reply_text(
            '🌐 **INTERNET PAKETI:**\n\n• 100 Mbps - 1.490 RSD\n• 300 Mbps - 2.290 RSD\n• 1 Gbps - 3.490 RSD',
            parse_mode='Markdown'
        )
    elif text == '💬 Podrška':
        await update.message.reply_text('🔧 **PODRŠKA:**\n\n📞 011/123-456\n🕒 08-20h\n✉️ podrska@tv-internet.rs')
    elif text == '📞 Kontakt':
        await update.message.reply_text('🏢 **KONTAKT:**\n\n📧 info@tv-internet.rs\n📱 011/123-456\n📍 Beograd')
    elif text == '❓ Česta Pitanja':
        await update.message.reply_text('❓ **ČESTA PITANJA:**\n\n• Cijene paketa?\n• Koji kanali?\n• Internet brzine?\n• Ugovorna obaveza?\n\nPitajte me bilo šta!')
    else:
        await update.message.reply_text('🤖 Hvala na poruci! Kontaktiraćemo vas uskoro.')
        logger.info(f"Unknown question from {user.id}: {text}")

def main():
    try:
        # Zameni sa tvojim tokenom
        TOKEN = "8583961957:AHPuA8_tPQF18Pj0mb82dk0wooph1aaXZg"
        
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("🤖 Bot starting...")
        print("🤖 Bot pokrenut! Check bot.log for details.")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Bot error: {e}")
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
