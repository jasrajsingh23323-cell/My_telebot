import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest
from flask import Flask
from threading import Thread
import os

# --- 1. रेंडर के लिए वेब सर्वर ---
app_server = Flask('')
@app_server.route('/')
def home(): 
    return "Bot is Running!"

def run_flask():
    app_server.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

# --- 2. अपनी डिटेल्स यहाँ भरें ---
API_ID =      39834295          # असली ID डालें
API_HASH = "0a904deff6494ef8d2369afdcb9c3991"         # असली Hash डालें
BOT_TOKEN = "8757303336:AAGsrzLWjieI1ZEW-XNvr7YOd_yN0uSctvk"       # असली टोकन डालें
CHANNEL_LINK = "https://t.me/+sUs1C78-PURmYmRl" 

# फाइल ID (अभी खाली रहने दें)
VIDEO_1 = "ID_AAYEGI_YAHA"
VIDEO_2 = "ID_AAYEGI_YAHA"
PHOTOS = ["PHOTO_ID_1", "PHOTO_ID_2", "PHOTO_ID_3"]

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_join_request()
async def join_handler(client, request: ChatJoinRequest):
    user_id = request.from_user.id
    try:
        m1 = await client.send_video(user_id, VIDEO_1)
        m2 = await client.send_video(user_id, VIDEO_2)
        await asyncio.sleep(180)
        await m1.delete()
        await m2.delete()
    except Exception as e:
        print(f"Join Error: {e}")

@app.on_message(filters.video | filters.photo)
async def get_ids(client, message):
    if message.video:
        print(f"VIDEO_ID_MIL_GAYI: {message.video.file_id}")
    elif message.photo:
        print(f"PHOTO_ID_MIL_GAYI: {message.photo.file_id}")

# --- 3. सबसे सुरक्षित RUN तरीका ---
async def main():
    # Flask चालू करें
    Thread(target=run_flask).start()
    
    # बॉट चालू करें
    await app.start()
    print("✅ BOT STARTED SUCCESSFULLY!")
    await idle() # बॉट को चालू रखेगा
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
