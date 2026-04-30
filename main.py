import asyncio
import os
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest, InputMediaVideo, InputMediaPhoto

# --- Flask Server for Render ---
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
V1 = "BAACAgUAAxkBAAMdafNPIdzKw7p04qRCljadZcIUOycAAhIgAALcd3hXXocnTnbPkA8eBA"
V2 = "BAACAgUAAxkBAAMeafNPfeCTxoiipcua_h1YKRkXrnMAAhMgAALcd3hXlFBfMa2jQMUeBA"
P1 = "AgACAgUAAxkBAAMfafNPsLYP5rgjVeBWCRC1eI2Yi-UAAjYSaxsmVplX4dWyKUtAH1sACAEAAwIAA3kABx4E"
P2 = "AgACAgUAAxkBAAMgafNPz8BmV_HOlL-z-EwYhgITfjEAAjgSaxsmVplXCHaVIk9KEUEACAEAAwIAA3kABx4E"
P3 = "AgACAgUAAxkBAAMhafNP-vnpRfYxNNtCover7Uq46jYAAjcSaxsmVplX6CwxVMWINnMACAEAAwIAA3kABx4E"

app = Client("jaw_code_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- Auto Delete Logic ---
async def delayed_delete(messages, delay):
    await asyncio.sleep(delay)
    for msg in messages:
        try: await msg.delete()
        except: pass

# --- Join Request Handler ---
@app.on_chat_join_request()
async def join_req(client, request: ChatJoinRequest):
    user = request.from_user
    name = f"@{user.username}" if user.username else user.first_name
    
    # Share Link Fixed (%2B for +)
    btns = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝗦𝗛𝗔𝗥𝗘 - 𝟬/𝟭", url="https://t.me/share/url?url=https%3A%2F%2Ft.me%2F%2BsUs1C78-PURmYmRl")],
        [InlineKeyboardButton("𝗦𝗞𝗜𝗣 𝗦𝗛𝗔𝗥𝗘", callback_data="start_msg")]
    ])
    
    # Videos Group (Barabar me)
    media_vids = await client.send_media_group(user.id, [InputMediaVideo(V1), InputMediaVideo(V2)])
    # Text Message
    msg_text = await client.send_message(
        user.id, 
        f"{name}\nNO ACCESS CHANELL!\n\nYOU CAN FIX IT 😏\n\nSHARE TO 2 GROUPS TO OPEN\n-- 0/2 (61.625 + VID) --", 
        reply_markup=btns
    )
    
    # Video 1 min (60s) baad delete
    asyncio.create_task(delayed_delete(list(media_vids), 60))
    # Text 2 min (120s) baad delete
    asyncio.create_task(delayed_delete([msg_text], 120))

# --- Start Content Logic ---
async def send_start_content(client, chat_id):
    btns = InlineKeyboardMarkup([[InlineKeyboardButton("Waiting for u daddy❤️💕", callback_data="buy")]])
    
    # Photos Group (Barabar me)
    media_photos = await client.send_media_group(chat_id, [
        InputMediaPhoto(P1),
        InputMediaPhoto(P2),
        InputMediaPhoto(P3)
    ])
    # Text Message
    msg_text = await client.send_message(
        chat_id, 
        "Full anonymity of payment and purchase\nLifetime Subscription\nGlobal Access - 1000 stars ⭐️\n\nJoin: https://t.me/+Qi4QrqampEk4MWU9", 
        reply_markup=btns
    )
    
    # Photos and Text dono 2 min (120s) baad delete
    asyncio.create_task(delayed_delete(list(media_photos) + [msg_text], 120))

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
    print("✅ BOT IS LIVE: Grouped Media & Custom Delete Timers!")
    app.run()
