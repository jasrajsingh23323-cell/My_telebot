  import os
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

# रेंडर को शांत रखने के लिए Flask
app_server = Flask('')
@app_server.route('/')
def home(): return "ID Bot is Running!"

def run_flask():
    app_server.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# आपकी डिटेल्स
API_ID = 39834295
API_HASH = "0a904deff6494ef8d2369afdcb9c3991"
BOT_TOKEN = "8757303336:AAGsrzLWjieI1ZEW-XNvr7YOd_yN0uSctvk"

app = Client("id_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video | filters.photo)
async def get_id(client, message):
    file_id = message.video.file_id if message.video else message.photo.file_id
    await message.reply_text(f"FILE ID:\n\n`{file_id}`")

if __name__ == "__main__":
    Thread(target=run_flask).start()
    app.run()
