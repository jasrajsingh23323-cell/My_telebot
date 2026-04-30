  from pyrogram import Client, filters

# आपकी डिटेल्स
API_ID = 39834295
API_HASH = "0a904deff6494ef8d2369afdcb9c3991"
BOT_TOKEN = "8757303336:AAGsrzLWjieI1ZEW-XNvr7YOd_yN0uSctvk"

app = Client("id_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video | filters.photo)
async def get_id(client, message):
    if message.video:
        file_id = message.video.file_id
        await message.reply_text(f"VIDEO ID:\n\n`{file_id}`")
    elif message.photo:
        file_id = message.photo.file_id
        await message.reply_text(f"PHOTO ID:\n\n`{file_id}`")

app.run()
     
