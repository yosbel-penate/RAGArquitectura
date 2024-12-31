import os
import requests
from flask import Flask, request
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ApplicationBuilder

API_URL = "http://localhost:5000"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)
bot = telegram.Bot(token=TELEGRAM_TOKEN)

async def start(update, context):
    await update.message.reply_text('Hola! Envíame una pregunta y te responderé.')

async def handle_message(update, context):
    query = update.message.text
    response = requests.post(f"{API_URL}/generate_answer", json={'query': query})
    if response.status_code == 200:
        answer = response.json().get('answer', 'No se encontró respuesta.')
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text('Hubo un error al procesar tu solicitud.')

def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
