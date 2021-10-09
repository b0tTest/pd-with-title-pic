# (c) HeimanPictures
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START = """"**Hai👋 {} ,
A Simple PDsik Uploader Bot. It Can Upload Link To PDisk.
Send Me Any Direct Link Or YouTube or Video Link I Will Upload To PDisk And Give Direct Pdisk Link**

> __Support Custom Thumbnail__
> __Support Custom Tittle Name__

__ • /help for More detail__
**Made With❤BY @MyTestBotZ**
"""

HELP = """**How to Use Me...

⦿ Its Easy to Use me **
✪ » __Send me Any Direct Link or YouTube Link__
✪ » __i will upload to PDisk & Give Link__

➠ **If you want Upload Telegram file,Videos to PDisk**
✪ » __First Send any File to__ <a href="https://telegram.me/Link4filesbot">@Link4Filesbot</a> __to generate Direct Link__
✪ » __Copy Generated Link and Paste here...__
✪ » __Violaaaa.... Done__


➠ **If You Want add Custom Tittle & Thumbnail Follow These Steps**

✪ » `link | Title`

**Or**

✪ » `Video link | Title | Thumbnail link`
        __(generate Thumbnail Link with Telegraph bot[@TGraphXbot])__

**NOTE**:
➢ __Do Not Spam, Send Link One By One, __
➢ __The Video File is Available on Your LINK ones Upload Process is Complete, it Take Time Depend on Your File Size & My Server Upload Speed So,be Patient__ 😴😴😴😴
"""

ABOUT = """➠ **My Name : PDisk Upload bot**
➠ **Creator : <a href="https://telegram.dog/oo7robot">This Person</a>**
➠ Credits : <code>Everyone in this journey</code>
➠ Language : <code>Python3.9.6</code>
➠ Library : <a href="https://docs.pyrogram.org/">Pyrogram v1.2.9</a>
➠ Server : <b>Heroku</b>
➠ Build Status : <b>Stable V1</b>
➠ <i>Source Code</i> ⤵️
"""


SB = InlineKeyboardMarkup(
  [[
    InlineKeyboardButton("📡 Updates Channel", url="https://t.me/MyTestBotZ"),
    InlineKeyboardButton("⚙️ Help", callback_data="help")
  ],[
    InlineKeyboardButton("🍿 Source Code 🍿", url="https://github.com/OO7ROBot/Pdisk-Upload-Bot")
  ],[
    InlineKeyboardButton("👨‍💻 Creator", url="https://t.me/OO7ROBOT"),
    InlineKeyboardButton("❣️BotsList", url="https://telegram.me/mybotzlist"),
    InlineKeyboardButton("⛔ Close", callback_data="close")
  ]]
)

HB = InlineKeyboardMarkup(
  [[
    InlineKeyboardButton("🏡 Home", callback_data="home"),
    InlineKeyboardButton("📝 About", callback_data="about"),
    InlineKeyboardButton("⛔ Close", callback_data="close")
  ]]
)
 
AB = InlineKeyboardMarkup(
  [[
    InlineKeyboardButton("🍿 Source Code 🍿", url="https://github.com/OO7ROBot/Pdisk-Upload-Bot")
  ],[
    InlineKeyboardButton("🏡 Home", callback_data="home"),
    InlineKeyboardButton("⚙️ Help", callback_data="help"),
    InlineKeyboardButton("⛔ Close", callback_data="close")
  ]]
)
  
OLD_HELP = """
**Send Me Direct Download Link Like Mirror Or From @LinkXGenBot.

Send As This Format**

`link | Title`

**Or**

`Video link | Title | Thumbnail link`

**NOTE:
➢ Do Not Spam, Send Link One By One
➢ To Know Status Just Go To cofilink.com/home**
"""

# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"





@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=START.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=SB
        )


@Client.on_message(filters.command('about') & filters.private)
async def about(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=ABOUT,
            disable_web_page_preview=True,
            reply_markup=AB
        )
      
@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HB
        )


@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=SB
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HB
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT,
            disable_web_page_preview=True,
            reply_markup=AB
        )
    else:
        await update.message.delete()
