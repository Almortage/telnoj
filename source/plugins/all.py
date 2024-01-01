from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatType
from config import *
from asyncio import sleep
import re
import os, time
from telegraph import upload_file
from os import remove
import time
import wget
import asyncio
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

os.environ['TZ'] = 'Africa/Cairo'
time.tzset()


async def is_Admin(chat, id):
    admins = []
    async for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if id in admins:
        return True
    else:
        return False


async def send_pv(ay, text):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type in {ChatType.PRIVATE, ChatType.BOT}:
            try:
                await ay.send_message(ahmed.chat.id, text)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def send_gp(ay, text):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type in {ChatType.SUPERGROUP, ChatType.GROUP}:
            try:
                await ay.send_message(ahmed.chat.id, text)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def send_ch(ay, text):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type == ChatType.CHANNEL:
            try:
                await ay.send_message(ahmed.chat.id, text)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def fwd_pv(ay, chat, msg):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type in {ChatType.PRIVATE, ChatType.BOT}:
            try:
                await ay.forward_messages(ahmed.chat.id, chat, msg)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def fwd_gp(ay, chat, msg):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type in {ChatType.SUPERGROUP, ChatType.GROUP}:
            try:
                await ay.forward_messages(ahmed.chat.id, chat, msg)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


async def fwd_ch(ay, chat, msg):
    async for ahmed in ay.get_dialogs():
        if ahmed.chat.type == ChatType.CHANNEL:
            try:
                await ay.forward_messages(ahmed.chat.id, chat, msg)
            except FloodWait as e:
                await sleep(e.value)
                await sleep(7)
            except Exception as e:
                print(e)
                await sleep(5)
                pass


@Client.on_message(filters.command("توجيه للخاص", prefixes=f".") & filters.me & filters.reply)
async def fwdpv(client, message):
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("جاري التجهيز للاذاعة")
    text = message.reply_to_message.text
    if not text:
        return await message.edit("تاكد انك تقوم بي الرد علي نص")
    await message.edit(f"جاري عمل توجيه للخاص في الحساب")
    await fwd_pv(client, message.chat.id, message.reply_to_message.id)
    await message.edit("• تم عمل الاذاعه")


@Client.on_message(filters.command("توجيه للمجموعات", prefixes=f".") & filters.me & filters.reply)
async def fwdgp(client, message):
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("جاري التجهيز للاذاعة")
    text = message.reply_to_message.text
    if not text:
        return await message.edit("تاكد انك تقوم بي الرد علي نص")
    await message.edit(f"جاري عمل توجيه للمجموعات في الحساب")
    await fwd_gp(client, message.chat.id, message.reply_to_message.id)
    await message.edit("• تم عمل الاذاعه")


@Client.on_message(filters.command("توجيه للقنوات", prefixes=f".") & filters.me & filters.reply)
async def fwdch(client, message):
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("جاري التجهيز للاذاعة")
    text = message.reply_to_message.text
    if not text:
        return await message.edit("تاكد انك تقوم بي الرد علي نص")
    await message.edit(f"جاري عمل توجيه للقنوات في الحساب")
    await fwd_ch(client, message.chat.id, message.reply_to_message.id)
    await message.edit("• تم عمل الاذاعه")


@Client.on_message(filters.command("اذاعه", prefixes=f".") & filters.me & filters.reply)
async def send_chats(client, message):
    if message.reply_to_message.from_user.id in sudo_command:
        return await message.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    await message.edit("جاري التجهيز للاذاعة")
    mod = message.text.split("اذاعه", 1)[1]
    text = message.reply_to_message.text
    if not mod:
        return await message.edit("تاكد انك قمت بتحديد نوع الاذاعة")
    if not text:
        return await message.edit("تاكد انك تقوم بي الرد علي نص")
    await message.edit("جاري تحديد حساب الاذاعة")
    if re.search('خاص', mod):
        await message.edit(f"جاري عمل الاذاعة للخاص في الحساب")
        await send_pv(client, text)
        await message.edit("• تم عمل الاذاعه")
    elif re.search('جروبات', mod):
        await message.edit(f"جاري عمل الاذاعة للجروبات في الحساب ")
        await send_gp(client, text)
        await message.edit("• تم عمل الاذاعه")
    elif re.search('قنوات', mod):
        await message.edit(f"جاري عمل الاذاعة للقنوات في الحساب")
        await send_ch(client, text)
        await message.edit("• تم عمل الاذاعه")
    else:
        await message.edit("نوع الاذاعه غير صحيح")


@Client.on_message(filters.command("تلجراف$", prefixes=f".") & filters.me)
async def tgph(c, msg):
    if not msg.reply_to_message:
        await msg.edit("قم بي الرد علي الصورة اولا")
        return
    if not msg.reply_to_message.photo:
        await msg.edit("ادعم الصور فقط")
        return
    await msg.edit("جاري تحميل الصورة")
    await msg.reply_to_message.download("./YYYBR")
    await msg.edit("جاري رفع الصورة علي تلجراف")
    response = upload_file("./YYYBR")
    remove("./YYYBR")
    await msg.edit(f"تم الرفع و استخراج الرابط :- \n<code>https://telegra.ph{response[0]}</code>")


@Client.on_message(filters.command("اضف جهاتي$", prefixes=f".") & filters.me & filters.group)
async def add_members(client, message):
    await message.edit("جاري اضافة جهاتك الي المجموعة")
    q, w, e = 0, 0, 0
    contacts = await client.get_contacts()
    await message.edit(f"جاري اضافة جهاتك الي المجموعة\nتم اضافة {w} عضو\nفشل اضافة {q} عضو")
    for a in contacts:
        e = e + 1
        try:
            await client.add_chat_members(message.chat.id, a.id)
            w = w + 1
        except:
            q = q + 1
        if e == 5:
            e = 0
            await message.edit(f"جاري اضافة جهاتك الي المجموعة\nتم اضافة {w} عضو\nفشل اضافة {q} عضو")
    await message.reply(f"تم اضافة {w} عضو\nفشل اضافة {q} عضو")
    await message.delete()


@Client.on_message(filters.command("ف", prefixes=f"."))
async def vsong(client, message):
    if message.reply_to_message:
        yad = message.reply_to_message.id
    else:
        yad = None
    text = message.text.split(None, 1)[1]
    await message.edit(f"جاري البحث عن {text}")
    if not text:
        return
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    await message.edit("جاري التحميل")
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
            video_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        await message.edit(f"خطأ في التحميل : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    await message.edit("جاري الرفع")
    try:
        await client.send_video(
            message.chat.id,
            video=video_file,
            duration=int(ytdl_data["duration"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            reply_to_message_id=yad,
            supports_streaming=True,
            caption=capy,
        )
        await message.delete()
        os.remove(video_file)
        os.remove(sedlyf)
    except Exception as e:
        await message.edit(f"حدث خطأ\n{e}")


@Client.on_message(filters.command("غ", prefixes=f"."))
async def msong(client, message):
    if message.reply_to_message:
        yad = message.reply_to_message.id
    else:
        yad = None
    text = message.text.split(None, 1)[1]
    if not text:
        return
    await message.edit(f"جاري البحث عن {text}")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    sedlyf = wget.download(kekme)
    opts = {
        'format': 'bestaudio[ext=m4a]',
        'keepvideo': False,
        'prefer_ffmpeg': False,
        'geo_bypass': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quite': True,
    }
    await message.edit("جاري التحميل")
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        await message.edit(f"خطأ في التحميل : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    file_stark = f"{ytdl_data['id']}.mp3"
    await message.edit("جاري الرفع")
    try:
        await client.send_audio(
            message.chat.id,
            audio=audio_file,
            duration=int(ytdl_data["duration"]),
            title=str(ytdl_data["title"]),
            performer=str(ytdl_data["uploader"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            reply_to_message_id=yad,
            caption=capy,
        )
        await message.delete()
        os.remove(audio_file)
        os.remove(sedlyf)
    except Exception as e:
        await message.edit(f"حدث خطأ\n{e}")
