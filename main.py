   import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest
from flask import Flask
from threading import Thread
import os

# --- 1. रेंडर को जगाए रखने के लिए (Anti-Sleep Flask) ---
app_server = Flask('')

@app_server.route('/')
def home(): 
    return "Bot is Running 24/7!"

def run_flask():
    # रेंडर के लिए पोर्ट 10000 सेट करना अनिवार्य है
    port = int(os.environ.get("PORT", 10000))
    app_server.run(host='0.0.0.0', port=port)

# --- 2. आपकी डिटेल्स ---
API_ID = 39834295
API_HASH = "0a904deff6494ef8d2369afdcb9c3991"
BOT_TOKEN = "8757303336:AAGsrzLWjieI1ZEW-XNvr7YOd_yN0uSctvk"

# --- यहाँ अपनी File IDs डालें ---
VIDEO_1 = "VIDEO_ID_HERE"
VIDEO_2 = "VIDEO_ID_HERE"
PHOTO_1 = "PHOTO_ID_HERE"
PHOTO_2 = "PHOTO_ID_HERE"
PHOTO_3 = "PHOTO_ID_HERE"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- 3. जॉइन रिक्वेस्ट फंक्शन ---
@app.on_chat_join_request()
async def join_handler(client, request: ChatJoinRequest):
    user = request.from_user
    username = f"@{user.username}" if user.username else user.first_name
    
    text = (
        f"{username}\n"
        "NO ACCESS CHANELL!\n\n"
        "YOU CAN FIX IT 😏\n\n"
        "SHARE TO 2 GROUPS TO OPEN\n"
        "-- 0/2 (61.625 + VID) --"
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝗦𝗛𝗔𝗥𝗘 - 𝟬/𝟭", url="https://t.me/share/url?url=https://t.me/+sUs1C78-PURmYmRl")],
        [InlineKeyboardButton("𝗦𝗞𝗜𝗣 𝗦𝗛𝗔𝗥𝗘", callback_data="skip_share")]
    ])
    
    try:
        v1 = await client.send_video(user.id, VIDEO_1)
        v2 = await client.send_video(user.id, VIDEO_2)
        m = await client.send_message(user.id, text, reply_markup=buttons)
        
        await asyncio.sleep(120) # 2 मिनट बाद ऑटो-डिलीट
        await v1.delete()
        await v2.delete()
        await m.delete()
    except Exception as e:
        print(f"Join Error: {e}")

# --- 4. स्टार्ट कमांड और मैसेज लॉजिक ---
async def start_logic(client, chat_id):
    photos = [PHOTO_1, PHOTO_2, PHOTO_3]
    text = (
        "Full anonymity of payment and purchase\n"
        "Lifetime Subscription\n"
        "Global Access - 1000 stars ⭐️\n\n"
        "Join: https://t.me/+Qi4QrqampEk4MWU9"
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Waiting for u daddy❤️💕", callback_data="buy_msg")]
    ])
    
    try:
        sent_items = []
        for p in photos:
            p_msg = await client.send_photo(chat_id, p)
            sent_items.append(p_msg)
            
        m = await client.send_message(chat_id, text, reply_markup=buttons)
        sent_items.append(m)
        
        await asyncio.sleep(120) # 2 मिनट बाद ऑटो-डिलीट
        for item in sent_items:
            await item.delete()
    except Exception as e:
        print(f"Start Error: {e}")

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await start_logic(client, message.chat.id)

# --- 5. बटन क्लिक हैंडलर ---
@app.on_callback_query()
async def cb_handler(client, cb):
    if cb.data == "skip_share":
        await start_logic(client, cb.message.chat.id)
        await cb.answer()
    elif cb.data == "buy_msg":
        await cb.answer("Buy it daddy i m waiting for u", show_alert=True)

# --- 6. रन करने का तरीका ---
if __name__ == "__main__":
    # Flask को अलग थ्रेड में चलाएं
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    print("🚀 BOT IS RUNNING WITH ANTI-SLEEP...")
    app.run()
     
