import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest
from flask import Flask
from threading import Thread
import os

# --- 1. रेंडर के लिए वेब सर्वर (ताकि बॉट 24/7 चले) ---
app_server = Flask('')
@app_server.route('/')
def home(): 
    return "Bot is Running!"

def run():
    app_server.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

# --- 2. अपनी डिटेल्स यहाँ भरें ---
API_ID = 1234567               # अपना API ID यहाँ लिखें
API_HASH = "your_hash"         # अपना API Hash यहाँ लिखें
BOT_TOKEN = "your_token"       # अपना बॉट टोकन यहाँ लिखें
CHANNEL_LINK = "https://t.me/your_channel" # चैनल लिंक

# --- 3. फाइल ID (अभी खाली छोड़ दें, बाद में Logs से निकालकर यहाँ भरें) ---
VIDEO_1 = "ID_AAYEGI_YAHA"
VIDEO_2 = "ID_AAYEGI_YAHA"
PHOTOS = ["PHOTO_ID_1", "PHOTO_ID_2", "PHOTO_ID_3"]

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# जॉइन रिक्वेस्ट आने पर वीडियो भेजने वाला फंक्शन
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
        m3 = await client.send_message(user_id, "आपका स्वागत है! यहाँ आपके वीडियो हैं।", reply_markup=buttons)
        
        await asyncio.sleep(180) # 3 मिनट बाद मैसेज डिलीट
        await m1.delete()
        await m2.delete()
        await m3.delete()
    except Exception as e:
        print(f"Join Error: {e}")

# स्टार्ट कमांड और फोटो भेजने वाला फंक्शन
@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    try:
        for p in PHOTOS:
            await client.send_photo(message.chat.id, p)
        await client.send_message(message.chat.id, "जुड़ने के लिए नीचे क्लिक करें:", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)]]))
    except Exception as e:
        print(f"Start Error: {e}")

# --- 4. फाइल ID निकालने वाला खास हिस्सा (इसे ध्यान से देखें) ---
@app.on_message(filters.video | filters.photo)
async def get_ids(client, message):
    if message.video:
        print(f"VIDEO_ID_MIL_GAYI: {message.video.file_id}")
    elif message.photo:
        print(f"PHOTO_ID_MIL_GAYI: {message.photo.file_id}")

@app.on_callback_query(filters.regex("skip_share"))
async def skip(client, cb):
    await start_cmd(client, cb.message)
    await cb.answer()

if __name__ == "__main__":
    Thread(target=run).start()
    app.run()

