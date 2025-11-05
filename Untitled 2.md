# Prvo saznaj svoj tačan token
echo "Tvoj token treba da izgleda ovako: 1234567890:ABCdefGHIjklMNopQRstUVwxyzXYZabc"

# Kreiraj novi fajl sa tokenom već unetim


cat > tv_internet_sbb_bot_fixed.py << 'EOF'
import logging
import re
import sqlite3
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ===== KONFIGURACIJA =====
BOT_TOKEN = "8105923056:AAFdk-iRcIgmVGHxdAE7R-qhTNoq7WbRTW0"  # NALEPI PRAVI TOKEN OVDE!
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

# ===== AI ODOOVORI =====
knowledge_base = {
    r'koliko košta|cijena|cijene': '💰 **CJENE PAKETA:**\n📺 TV: 1.990-2.990 RSD\n🌐 Internet: 1.490-3.490 RSD\n🔥 Kombinovani: 2.990 RSD',
    r'kanali|koji kanali': '📡 **TV KANALI:**\n200+ kanala\nSport, filmovi, dečji\nHD kvalitet',
    r'internet|brzina': '🌐 **INTERNET:**\n100 Mbps: 1.490 RSD\n300 Mbps: 2.290 RSD\n1 Gbps: 3.490 RSD',
}

# ===== TELEGRAM BOT HANDLERI =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    
    keyboard = [
        ['📺 TV Paketi', '🌐 Internet'],
        ['💰 Cene', '💬 Kontakt']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        f'👋 **Dobrodošao/la {user.first_name}!**\n\nJa sam TVInternetSBB asistent 🤖',
        reply_markup=reply_markup, 
        parse_mode='Markdown'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    
    # AI odgovori
    response = None
    for pattern, answer in knowledge_base.items():
        if re.search(pattern, text.lower()):
            response = answer
            break
    
    if response:
        await update.message.reply_text(response, parse_mode='Markdown')
    elif text == '📺 TV Paketi':
        await update.message.reply_text('📺 **TV PAKETI:**\n• Osnovni: 1.990 RSD\n• Sportski: 2.490 RSD\n• Premium: 2.990 RSD')
    elif text == '🌐 Internet':
        await update.message.reply_text('🌐 **INTERNET:**\n• 100 Mbps: 1.490 RSD\n• 300 Mbps: 2.290 RSD\n• 1 Gbps: 3.490 RSD')
    elif text == '💰 Cene':
        await update.message.reply_text('💰 **CENE:**\nTV: 1.990-2.990 RSD\nInternet: 1.490-3.490 RSD\n📞 011/123-456')
    elif text == '💬 Kontakt':
        await update.message.reply_text('💬 **KONTAKT:**\n📞 011/123-456\n📧 info@tvinternet.rs\n🕒 08-20h')
    else:
        await update.message.reply_text('🤖 Hvala! Kontaktiraćemo vas.\n📞 011/123-456')

def main():
    init_db()
    
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        print("🚀 TVInternetSBB bot pokrenut!")
        application.run_polling()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
EOF