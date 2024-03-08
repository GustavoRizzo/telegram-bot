from pyrogram import filters
from client import create_app
from utils import User

app = create_app()

print('🤖 Bot started')


@app.on_message(filters.private)
async def hello(client, message):
    user = User(message.chat)

    if not user.is_allowed:
        await message.reply("Que saaaaco, Eu não posso falar com você!")
        return
    await message.reply(f"Olá {user.first_name}, como eu posso lhe ser útil?")


app.run()
