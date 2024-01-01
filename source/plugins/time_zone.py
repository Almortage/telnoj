from pyrogram import Client, filters
from pyrogram.types import Message
from config import *


@Client.on_message(filters.regex("^.وقت (.*)") & filters.me)
async def chg_timezone(c: Client, msg: Message):
    exe = msg.text[5:]
    iraq = "Asia/Baghdad"
    cairo = "Africa/Cairo"
    jordan = "Asia/Amman"
    yman = "Asia/Aden"
    Syria = "Asia/Damascus"
    if exe == "العراق" or exe == "عراق":
        r.set(f'{sudo_id}:tmz_medoo', iraq)
    if exe == "السعودية" or exe == "السعوديه":
        r.set(f'{sudo_id}:tmz_medoo', iraq)
    if exe == "مصر":
        r.set(f'{sudo_id}:tmz_medoo', cairo)
    if exe == "الاردن":
        r.set(f'{sudo_id}:tmz_medoo', jordan)
    if exe == "اليمن":
        r.set(f'{sudo_id}:tmz_medoo', yman)
    if exe == "سوريا":
        r.set(f'{sudo_id}:tmz_medoo', Syria)
    await msg.edit("• تم تغير الساعه")

