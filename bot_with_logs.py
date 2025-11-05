import logging
import re
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Podesi logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

# Baza znanja
knowledge_base = {
    r'koliko košta|cijena|cijene': '💰 **CJENE PAKETA:**\\n\\n• TV Osnovni: 1.990 RSD\\n• Internet 100 Mbps: 1.490 RSD\\n• Kombinovani: 2.990 RSD',
    r'kanali|koji kanali': '📡 **KANALI:**\\n\\nPreko 200 kanala\\nSport, filmovi, dečji kanali',
    r'internet|brzina': '🌐 **INTERNET:**\\n\\nBrzine 100 Mbps - 1 Gbps\\nBez ugovorne obaveze',
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    logging.info(f"User {user.id} ({user.first_name}) started the bot")
    
    keyboard = [['📺 TV Paketi', '🌐 Internet'], ['💬 Podrška', '📞 Kontakt']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text('Dobrodošli! 🎉', reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    text = update.message.text
    logging.info(f"Message from {user.id}: {text}")
    
    # AI odgovori
    response = None
    for pattern, answer in knowledge_base.items():
        if re.search(pattern, text.lower()):
            response = answer
            break
    
    if response:
        await update.message.reply_text(response, parse_mode='Markdown')
    elif text == '📺 TV Paketi':
        await update.message.reply_text('📺 **TV PAKETI:**\\n\\n• Osnovni: 1.990 RSD\\n• Sportski: 2.490 RSD\\n• Premium: 2.990 RSD')
    elif text == '🌐 Internet':
        await update.message.reply_text('🌐 **INTERNET:**\\n\\n• 100 Mbps: 1.490 RSD\\n• 300 Mbps: 2.290 RSD\\n• 1 Gbps: 3.490 RSD')
    elif text == '💬 Podrška':
        await update.message.reply_text('📞 011/123-456\\n🕒 08-20h')
    elif text == '📞 Kontakt':
        await update.message.reply_text('📧 info@tv-internet.rs\\n📱 011/123-456')
    else:
        await update.message.reply_text('Hvala! Kontaktiraćemo vas.')
        logging.info(f"Unknown question from {user.id}: {text}")

def main():
    application = Application.builder().token("YOUR_BOT_TOKEN").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logging.info("🤖 Bot started successfully!")
    print("🤖 Bot je pokrenut! Check bot.log for details.")
    application.run_polling()

if __name__ == '__main__':
    main()
