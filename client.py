from os import getenv

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()


def create_app() -> Client:
    return Client(
        'guibot',
        api_id=getenv('TELEGRAM_API_ID'),
        api_hash=getenv('TELEGRAM_API_HASH'),
        bot_token=getenv('TELEGRAM_BOT_TOKEN')
    )
