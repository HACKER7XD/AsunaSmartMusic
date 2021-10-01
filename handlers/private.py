from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as yoga, BOT_USERNAME
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
#    await message.reply_sticker("CAACAgUAAx0CVEgMTAACE81hCsnWvf_ao9aBzJAhgUX08F9MBgAC7wEAAl7AKFSrtnT4_eRctSAE")
    await message.reply_text(
        f"""**👋🏻 нєℓℓσ, мү ηαмє ιs  {yoga} ✨

ρσωєrєd вү [cσвяα xd](https://t.me/zYxDx).

wαηт ρℓαү мυsιc ση vcg?, αdd мє тσ үσυr grσυρ.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ αdd мє тσ үσυr grσυρ ➕", url="https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🚨 sυρρσrт 🚨", url="https://t.me/MISTY_SUPORTER"
                    ),
                    InlineKeyboardButton(
                        "🔊 υρdαтєs 🔊", url="https://t.me/MISTY_SUPORT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 dσηαтιση", url="https://t.me/HEENAXD"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ Music player is online.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [   
                    InlineKeyboardButton(
                        "🚨 sυρρσrт's", url="https://t.me/MISTY_SUPORTER"),
                    InlineKeyboardButton(
                        "υρdαтє's 🔊", url="https://t.me/MISTY_SUPORT")
                ],[ 
                    InlineKeyboardButton("dєvєℓσρєr", url="https.t.me/XD_LIF")
                ]
            ]
        )
   )

@Client.on_message(filters.command(["help", f"help@{BOT_USERNAME}"]) & ~filters.group & ~filters.private)
async def helptext(_, message: Message):
      await message.reply_text(f"**User Command:\n/start for check bot alive\n/help to see this help menu\n/about for see about this bot and dev list\n/play <reply audio/url/title> for Play Music on VCG.\n/song <url/title> for Downloading song from Youtube.\nAdmin Command:\n/pause for pause current played music\n/resume for resuming paused music\n/skip for skipping currently played music\n/end for stop streaming music.\n\nInfo you can use / or ! for any command, also can tag bot username for avoid conflict with other bot,\nex: /end@{BOT_USERNAME}**",
      reply_markup=InlineKeyboardMarkup(
            [
                [   
                    InlineKeyboardButton(
                        "🚨 sυρρσrт's", url="https://t.me/MISTY_SUPORTER"),
                    InlineKeyboardButton(
                        "υρdαтє's 🔊", url="https://t.me/MISTY_SUPORT")
                ],[ 
                    InlineKeyboardButton("dєvєℓσρєr", url="https.t.me/XD_LIF")
                ]
            ]
        )
   )

@Client.on_message(filters.command(["about", f"about@{BOT_USERNAME}"]) & ~filters.private & ~filters.channel)
async def about(_, message: Message):
      await message.reply_text("""**Run on [Heroku](https://heroku.com)\nLibrary [Pyrogram](https://docs.pyrogram.org)\nWith [Pytgcalls](https://github.com/pytgcalls/pytgcalls)\nDevelopers:\n• [Cobra](https://t.me/XD_LIF)\n• [Queen](https://t.me/HEENAXD)**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [   
                    InlineKeyboardButton(
                        "🚨 sυρρσrт's", url="https://t.me/MISTY_SUPORTER"),
                    InlineKeyboardButton(
                        "υρdαтє's 🔊", url="https://t.me/MISTY_SUPORT")
                ],[ 
                    InlineKeyboardButton("dєvєℓσρєr", url="https.t.me/XD_LIF")
                ]
            ]
        )
    disable_web_page_preview=True
   )
