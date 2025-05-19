from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ 𝗧ᴏ 𝗚ᴀᴀɴᴀ 𝗩𝟸 𝗥ᴇᴘᴏ ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @Fumkies ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗕ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗦ᴜᴘᴘᴏʀᴛ 𝗖ʜᴀɴɴᴇʟ", url="https://t.me/Fine_N_Ok"),
          InlineKeyboardButton("𝗠ᴀsᴛᴇʀ", url="https://t.me/Fumkies"),
          ],
               [
                InlineKeyboardButton("𝗦ᴜᴘᴘᴏʀᴛ 𝗚ʀᴏᴜᴘ", url=f"https://t.me/PURVI_SUPPORT"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/GaanaMusizBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/i493lf.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
