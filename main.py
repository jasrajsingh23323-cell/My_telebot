import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest
from flask import Flask
from threading import Thread
import os

# Flask Server for Render
app_server = Flask('')
@app_server.route('/')
def home(): return "Bot is Running!"
def run(): app_server.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

# --- अपनी डिटेल्स यहाँ भरें ---
API_ID = 39834295  # अपना API ID यहाँ लिखें
API_HASH = "0a904deff6494ef8d2369afdcb9c3991" # अपना API Hash यहाँ लिखें
BOT_TOKEN = "8757303336:AAGsrzLWjieI1ZEW-XNvr7YOd_yN0uSctvk" # अपना बॉट टोकन यहाँ लिखें
CHANNEL_LINK = "https://t.me/+sUs1C78-PURmYmRl" # चैनल लिंक

# यहाँ अपनी File IDs डालें
VIDEO_1 = "ID_HERE"
VIDEO_2 = "ID_HERE"
PHOTOS = ["PHOTO_ID_1", "PHOTO_ID_2", "PHOTO_ID_3"]

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_join_request()
async def join_handler(client, request: ChatJoinRequest):
    user_id = request.from_user.id
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("↗️ Share", url="https://t.me/share/url?url=Join%20Now!")],
        [InlineKeyboardButton("⏩ Skip Share", callback_data="skip_share")]
    ])
    try:
        m1 = await client.send_video(user_id, VIDEO_1)
        m2 = await client.send_video(user_id, VIDEO_2)
        m3 = await client.send_message(user_id, "आपका स्वागत है!", reply_markup=buttons)
        await asyncio.sleep(180) # 3 मिनट बाद डिलीट
        await m1.delete(); await m2.delete(); await m3.delete()
     Lancaster except: pass

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    for p in PHOTOS: await client.send_photo(message.chat.id, p)
    await client.send_message(message.chat.id, "जुड़ने के लिए क्लिक करें:", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)]]))

@app.on_callback_query(filters.regex("skip_share"))
async def skip(client, cb):
    await start_cmd(client, cb.message)
    await cb.answer()

if __name__ == "__main__":
    Thread(target=run).start()
    app.run()
@app.on_message(filters.video | filters.photo)
async def get_ids(client, message):
    if message.video:
        print(f"VIDEO_ID: {message.video.file_id}")
    elif message.photo:
        print(f"PHOTO_ID: {message.photo.file_id}")

