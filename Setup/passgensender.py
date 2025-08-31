import random
import string
import os
import time
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
from dotenv import load_dotenv

load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
CHANNEL_ID = os.getenv('CHANNEL_ID')

def generate_password():
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 5)))
    digits = ''.join(random.choices(string.digits, k=random.randint(5, 6)))
    special = random.choice('!%$')
    password = uppercase + lowercase + digits + special
    return ''.join(random.sample(password, len(password)))

def escape_markdown(text):
    chars = '\_\*\[\]\(\)\~\`\>\#\+\-\=\|\{\}'  # Убрана точка (.)
    for char in chars:
        text = text.replace(char, f'\\{char}')
    return text

def save_to_file(purpose, login, password):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] Purpose: {purpose}, Login: {login}, Password: {password}\n"
    with open('logins.txt', 'a', encoding='utf-8') as f:
        f.write(entry)

def main():
    purpose = input("Enter purpose of the account: ")
    login = input("Enter login: ")
    password = generate_password()
    print(f"Generated password: {password}")

    save_to_file(purpose, login, password)

    message = (f"\*New Account\*\n"
               f"\*Purpose:\* `{escape_markdown(purpose)}`\n"
               f"\*Login:\* `{escape_markdown(login)}`\n"
               f"\*Password:\* `{escape_markdown(password)}`")

    try:
        with TelegramClient('session', int(API_ID), API_HASH) as client:
            client.start()
            channel_id = CHANNEL_ID
            if channel_id.startswith('-') or channel_id.isdigit():
                channel_id = int(channel_id)
            try:
                client.send_message(channel_id, message, parse_mode='md')
                print("Sent to Telegram and saved to logins.txt!")
            except FloodWaitError as e:
                print(f"Flood wait: {e.seconds} seconds")
                time.sleep(e.seconds)
                client.send_message(channel_id, message, parse_mode='md')
            except ValueError as e:
                print(f"Error: {e}. Check if CHANNEL_ID is correct and the account has access to the channel.")
                return
    except Exception as e:
        print(f"Failed to connect to Telegram: {e}")
        return

if __name__ == "__main__":
    main()
