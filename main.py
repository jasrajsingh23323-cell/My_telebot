import asyncio
import os
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest

# --- Flask Server for Render (24/7 Active) ---
app_server = Flask('')
@app_server.route('/')
def home(): return "Bot is Running Successfully!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_server.run(host='0.0.0.0', port=port)

# --- Your Credentials ---
API_ID = 39834295
API_HASH = "0a904deff6494ef8d2369afdcb9c3991"
BOT_TOKEN = "8757303336:AAGsrzLWjieI1ZEW-XNvr7YOd_yN0uSctvk"

# --- Your Verified File IDs ---
V1 = "AAMCBQADGQEAAw5p8yAeZNIvMd7oUNV9CaOAGLy0KAACEiAAAtx3eFdehydOds-QDwEAB20AAzsE"
V2 = "AAMCBQADGQEAAxBp8yYkuqKyftOj9xbSHl3Rf10abQACEyAAAtx3eFeUUF8xraNAxQEAB20AAzsE"
P1 = "AgACAgUAAxkBAAMWafNGlvjLmUudTDebqbs-HmwG8WoAAjYSaxsmVplX4dWyKUtAH1sBAAMCAAN5AAM7BA"
P2 = "AgACAgUAAxkBAAMXafNHE59gwTscf5xvbkghqNJl1cEAAjcSaxsmVplX6CwxVMWINnMBAAMCAAN5AAM7BA"
P3 = "AgACAgUAAxkBAAMYafNHStJCSFlsJpHt86mp8RBbw6EAAjgSaxsmVplXCHaVIk9KEUEBAAMCAAN5AAM7BA"

app = Client("jaw_code_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- Auto Delete Logic (120 Seconds) ---
async def auto_delete(messages):
    await asyncio.sleep(120)
    for msg in messages:
        try: await msg.delete()
        except: pass

# --- Join Request Handler ---
@app.on_chat_join_request()
async def join_req(client, request: ChatJoinRequest):
    user = request.from_user
    name = f"@{user.username}" if user.username else user.first_name
    btns = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝗦𝗛𝗔𝗥𝗘 - 𝟬/𝟭", url="https://t.me/share/url?url=https://t.me/+sUs1C78-PURmYmRl")],
        [InlineKeyboardButton("𝗦𝗞𝗜𝗣 𝗦𝗛𝗔𝗥𝗘", callback_data="start_msg")]
    ])
    msg1 = await client.send_video(user.id, V1)
    msg2 = await client.send_video(user.id, V2)
    msg3 = await client.send_message(user.id, f"{name}\nNO ACCESS CHANELL!\n\nYOU CAN FIX IT 😏\n\nSHARE TO 2 GROUPS TO OPEN\n-- 0/2 (61.625 + VID) --", reply_markup=btns)
    asyncio.create_task(auto_delete([msg1, msg2, msg3]))

# --- Start Command Logic ---
async def send_start_content(client, chat_id):
    btns = InlineKeyboardMarkup([[InlineKeyboardButton("Waiting for u daddy❤️💕", callback_data="buy")]])
    m1 = await client.send_photo(chat_id, P1)
    m2 = await client.send_photo(chat_id, P2)
    m3 = await client.send_photo(chat_id, P3)
    m4 = await client.send_message(chat_id, "Full anonymity of payment and purchase\nLifetime Subscription\nGlobal Access - 1000 stars ⭐️\n\nJoin: https://t.me/+Qi4QrqampEk4MWU9", reply_markup=btns)
    asyncio.create_task(auto_delete([m1, m2, m3, m4]))

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await send_start_content(client, message.chat.id)

@app.on_callback_query()
async def cb(client, callback):
    if callback.data == "start_msg":
        await send_start_content(client, callback.message.chat.id)
        await callback.answer()
    elif callback.data == "buy":
        await callback.answer("Buy it daddy i m waiting for u", show_alert=True)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    print("✅ BOT IS LIVE!")
    app.run()
  
