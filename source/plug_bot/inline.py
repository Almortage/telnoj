from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio

@bot.on_inline_query(filters.regex("^الاوامر$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("☑️ اوامر الخاص   ",callback_data="help1"),
             InlineKeyboardButton("☑️ اوامر الحمايه ",callback_data="help2"),
             ],
             [
             InlineKeyboardButton("☑️ اوامر اليوتيوب  ",callback_data="help3"),
             InlineKeyboardButton("☑️ اوامر الاذاعه",callback_data="help4"),
             ],
             [
             InlineKeyboardButton("☑️ اوامر الرفع ",callback_data="help5"),
             InlineKeyboardButton("☑️ اوامر النسب",callback_data="help6"),
             ],
             [
             InlineKeyboardButton("☑️ اوامر اضافيه ",callback_data="help7"),
             InlineKeyboardButton("☑️ اوامر الزخرفة",callback_data="help10"),
             ],
             [
             InlineKeyboardButton("☑️ اوامر تسلية1 ",callback_data="help8"),
             InlineKeyboardButton("☑️ اوامر تسلية2",callback_data="help9"),
             ],
             [
            
             InlineKeyboardButton("✅  قناه السورس  ",url="https://t.me/Tepthon"),
             ],
             [
             InlineKeyboardButton("☑️ لتنصيب حسابك   ",url="https://t.me/A_D_P"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(
                    "• اهلا بك في اوامر اليوزر البوت\n•"
                ),
                url="https://t.me/Tepthon",
                description=" SOURCE",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )
