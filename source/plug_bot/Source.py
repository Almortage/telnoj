from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio

@bot.on_inline_query(filters.regex("^سورس$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("✅  قناه السورس  ",url="https://t.me/Tepthon"),
             ],
             [
             InlineKeyboardButton("☑️ لتنصيب حسابك   ",url="https://t.me/A_D_P"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="سورس البوت",
                input_message_content=InputTextMessageContent(
                    "╭───── • 𖥔 • ─────╮\n [𖥔 𝚂𝙾𝚄𝚁𝙲𝙴 Tepthon ⚡️](https://t.me/Tepthon)\n[𖥔 Tepthon Support ⚡️](https://t.me/Tepthon_Help)\n[𖥔 Taleb مُحمـد ⚡️](https://t.me/A_D_P)\n╰───── • 𖥔 • ─────╯\n⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼"
                ),
                url="https://t.me/Tepthon",
                description=" SOURCE",
                thumb_url="https://telegra.ph/file/d7612edc7380f0b69b350.jpg",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )








