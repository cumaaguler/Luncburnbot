from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update

import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "merhaba":
        await update.message.reply_text("Merhaba!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot çalışıyor...")
app.run_polling()
