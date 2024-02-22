from pyrogram import filters

from client import create_app

app = create_app()

print('🤖 Bot started')

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello world! 🌎")


app.run()
