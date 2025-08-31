import os
import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()
CHAT_ID = int(os.getenv("REDSENDER_CHAT_ID"))
API_ID = int(os.getenv("API_ID"))  # Укажите ваш API ID
API_HASH = os.getenv("API_HASH")   # Укажите ваш API Hash

# Путь к файлу сессии
SESSION_FILE = "/home/arch/Red/redsession"

def send_video(file_path):
    start_time = time.time()  # Начало отсчета времени
    
    # Инициализация клиента Telethon
    with TelegramClient(SESSION_FILE, API_ID, API_HASH) as client:
        # Отправка видео в указанный чат
        client.send_file(CHAT_ID, file_path)
    
    # Вычисление и вывод времени выполнения
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Video sent successfully! Execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Error: No file path provided")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)
    
    send_video(file_path)
