import os
import requests
from flask import Flask, request
import telegram
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder
from bs4 import BeautifulSoup

API_URL = "http://localhost:5000"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)
bot = telegram.Bot(token=TELEGRAM_TOKEN)

async def start(update, context):
    await update.message.reply_text('Hola! Envíame una pregunta y te responderé.')

def format_for_telegram(text):
    """
    Formatea el texto HTML para que sea visualizado correctamente en Telegram.
    """
    text = text.replace("```html", "")
    text = text.replace("```", "")

    # Limpiar etiquetas no soportadas
    soup = BeautifulSoup(text, "html.parser")
    for tag in soup.find_all(True):
        if tag.name not in ["b", "strong", "i", "em", "u", "ins", "s", "strike", "del", "code", "pre", "a"]:
            tag.unwrap()
    return str(soup).strip()

async def handle_message(update, context):
    query = update.message.text
    response = requests.post(f"{API_URL}/generate_answer", json={'query': query})
    if response.status_code == 200:
        answer = response.json().get('answer', 'No se encontró respuesta.')
        formatted_answer = format_for_telegram(answer)
        await update.message.reply_text(formatted_answer, parse_mode=telegram.constants.ParseMode.HTML)
    else:
        await update.message.reply_text('Hubo un error al procesar tu solicitud.')

def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
