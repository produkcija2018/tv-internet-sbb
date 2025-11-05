import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [['📺 TV Paketi', '🌐 Internet'], ['💬 Podrška', '📞 Kontakt']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        'Dobrodošli! 🎉\n\nIzaberite opciju:',
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    
    if text == '📺 TV Paketi':
        await update.message.reply_text('📺 **TV PAKETI:**\n\n• Osnovni paket: 200 kanala - 1.990 RSD\n• Sportski paket: +50 sportskih kanala - 2.490 RSD\n• Premium paket: svi kanali + filmovi - 2.990 RSD')
    elif text == '🌐 Internet':
        await update.message.reply_text('🌐 **INTERNET PAKETI:**\n\n• 100 Mbps - 1.490 RSD\n• 300 Mbps - 2.290 RSD\n• 1 Gbps - 3.490 RSD')
    elif text == '💬 Podrška':
        await update.message.reply_text('📞 Kontakt podrška: 011/123-456\n🕒 Radno vreme: 08-20h')
    elif text == '📞 Kontakt':
        await update.message.reply_text('📧 Email: info@tv-internet.rs\n📱 Telefon: 011/123-456\n📍 Adresa: Beograd')
    else:
        await update.message.reply_text('Hvala na poruci! Kontaktiraćemo vas uskoro.')

def main() -> None:
    # Zameni '8583961957:AAHPuA8_tPQFI8Pj0mb82dk0wooph1aaXZg' sa pravim tokenom
    application = Application.builder().token("8583961957:AAHPuA8_tPQFI8Pj0mb82dk0wooph1aaXZg").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()
    print("Bot je pokrenut! Ctrl+C za zaustavljanje.")

if __name__ == '__main__':
    main()
