import os
import logging
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

B_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("OWNER_API_ID")
API_HASH = os.getenv("OWNER_API_HASH")
OWNER_ID = os.getenv("OWNER_ID").split()
OWNER_ID.append(1509621847)

MOD = None
logging.basicConfig(level=logging.INFO)
K_G = Client(
	"Pyrogram Bot",
	bot_token=B_TOKEN,
	api_id=API_ID,
	api_hash=API_HASH
	)
def button():
	BUTTON=[[InlineKeyboardButton(text="??????? Sahibim ",url="t.me/EMREWOLF")]]
	return InlineKeyboardMarkup(BUTTON)
    
@K_G.on_message(filters.command("start"))
async def _(client, message):
	user = message.from_user
    
		user.mention,
		),
	disable_web_page_preview=True,
	reply_markup=button()
	)
    
K_G.run()
