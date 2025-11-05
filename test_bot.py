import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TEST_TOKEN = "8105923056:AAFdk-iRcIgmVGHxdAE7R-qhTNoq7WbRTW0"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🤖 Bot radi! Test uspešan! 🎉')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Primio sam: {update.message.text}')

def main():
    application = Application.builder().token(TEST_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("🚀 Test bot pokrenut...")
    application.run_polling()

if __name__ == '__main__':
    main()
