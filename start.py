import threading
import os

def start_api_server():
    os.system("python app_api.py")

def start_telegram_bot():
    os.system("python telegram_bot.py")

def main():
    # Crear hilos para el servidor API y el bot de Telegram
    api_thread = threading.Thread(target=start_api_server)
    telegram_thread = threading.Thread(target=start_telegram_bot)

    # Iniciar los hilos
    api_thread.start()
    telegram_thread.start()

    # Esperar a que los hilos terminen
    api_thread.join()
    telegram_thread.join()

if __name__ == "__main__":
    main()
