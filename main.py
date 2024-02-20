from os import getenv
from asyncio import run

from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

app = Client(
    'guibot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)

print('🤖 Bot started')

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello world! 🌎")


app.run()
