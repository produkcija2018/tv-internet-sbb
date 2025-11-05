Done! Congratulations on your new bot. You will find it at t.me/tv_internet_paketi_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.  
  
Use this token to access the HTTP API:  

8583961957:AAHPuA8_tPQFI8Pj0mb82dk0wooph1aaXZg

  
Keep your token **secure** and **store it safely**, it can be used by anyone to control your bot.  
  
For a description of the Bot API, see this page: https://core.telegram.org/bots/api

cd "/storage/emulated/0/Documents/moje-zabele-ke"

# Koristi nano ili sed za zamenu tokena
sed -i 's/YOUR_BOT_TOKEN/8583961957:AAHPuA8_tPQFI8Pj0mb82dk0wooph1aaXZg/' bot.py


sed -i 's/YOUR_BOT_TOKEN/8583961957:AAHPuA8_tPQFI8Pj0mb82dk0wooph1aaXZg/' bot_ai.py



sed -i 's/YOUR_BOT_TOKEN/tvoj_actual_token_ovde/' bot_ai.py


sed -i 's/YOUR_BOT_TOKEN/tvoj_actual_token_ovde/' bot.py







Done! Congratulations on your new bot. You will find it at t.me/tv_internet_sbb_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.  
  
Use this token to access the HTTP API:  

8105923056:AAFdk-iRcIgmVGHxdAE7R-qhTNoq7WbRTW0

  
Keep your token **secure** and **store it safely**, it can be used by anyone to control your bot.  
  
For a description of the Bot API, see this page: https://core.telegram.org/bots/api


# Kreiraj najjednostavniji mogući test bot

cat > test_bot.py << 'EOF'
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
EOF










