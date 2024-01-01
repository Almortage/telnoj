from pyrogram import Client, filters, enums
from config import *
import asyncio


def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"


async def is_Admin(chat, id):
    admins = []
    async for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if id in admins:
        return True
    else:
        return False


@Client.on_message(filters.command("كتم$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def mute(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    chek = await is_Admin(msg.chat.id, msg.from_user.id)
    if chek == False:
        await message.reply("• يجب ان تكون مشرف بالمجموعه لاستخدام الاوامر")
        return False
    try:
        if msg.reply_to_message.from_user.id == sudo_id:
            return await msg.edit("• لا يمكنك كتم نفسك")
        if msg.reply_to_message.from_user.id == 1001132193:
            return await msg.edit("• لا يمكنك كتم بارلو")
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.from_user.id)
        txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم كتمه بنجاح"
        await msg.edit(txx)
    except:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم كتم القناه في المجموعه")


@Client.on_message(filters.command("الغاء كتم$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_mute(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    try:
        if msg.reply_to_message.from_user.id == sudo_id:
            return await msg.edit("• لا يمكنك  الغاء كتم نفسك")
        if msg.reply_to_message.from_user.id == 1001132193:
            return await msg.edit("• لا يمكنك الغاء كتم بارلو")
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.from_user.id)
        txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم الغاء كتمه بنجاح"
        await msg.edit(txx)
    except:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم الغاء كتم القناه في المجموعه")


@Client.on_message(filters.command("مسح المكتومين", prefixes=f".") & filters.me & filters.group)
async def un_mute_all(c, msg):
    r.delete(f"{sudo_id}mute{msg.chat.id}")
    txx = f"• تم مسح المكتومين بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("حظر$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def bann(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    chek = await is_Admin(msg.chat.id, msg.from_user.id)
    if chek == False:
        await message.reply("• يجب ان تكون مشرف بالمجموعه لاستخدام الاوامر")
        return False
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك حظر نفسك")
    if msg.reply_to_message.from_user.id == 1001132193:
        return await msg.edit("• لا يمكنك حظر بارلو")
    try:
        await c.ban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
        txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم حظره بنجاح"
        await msg.edit(txx)
    except Exception as e:
        await msg.edit(f"• ليس لديك صلاحيات الحظر في المجموعه")


@Client.on_message(filters.command("الغاء حظر$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_ban(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم الغاء كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك  الغاء حظر نفسك")
    if msg.reply_to_message.from_user.id == 1001132193:
        return await msg.edit("• لا يمكنك الغاء حظر بارلو")
    try:
        await c.unban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
        txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم الغاء حظره بنجاح"
        await msg.edit(txx)
    except:
        await msg.edit("• العضو ليس محظور \n• او ليس لديك صلاحيات الحظر في المجموعه")


@Client.on_message(filters.command(["مسح المحظورين$", "مسح المطرودين$"], prefixes=f".") & filters.me & ~filters.private)
async def un_ban_all(c, msg):
    xxx = 0
    async for m in c.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.BANNED):
        try:
            await c.unban_chat_member(msg.chat.id, m.user.id)
            xxx += 1
        except:
            pass
    await msg.edit(f"• تم الغاء حظر {xxx} عضو")


@Client.on_message(filters.command("تدمير$", prefixes=f".") & filters.me & ~filters.private)
async def ban_all_members(c, msg):
    xxx = 0
    un = 0
    async for m in c.get_chat_members(msg.chat.id):
        try:
            if m.user.id == sudo_id:
                continue
            await c.ban_chat_member(msg.chat.id, m.user.id)
            if xxx % 10 == 0:
                await msg.edit(f"• تم حظر {xxx}")
            xxx += 1
        except:
            un += 1
    await msg.edit(f"• تم حظر {xxx} عضو\n• لم استطيع حظر {un} عضو")


@Client.on_message(filters.command("كتم عام$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def mute_all(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك كتم نفسك")
    if msg.reply_to_message.from_user.id == 1001132193:
        return await msg.edit("• لا يمكنك كتم بارلو")
    r.sadd(f"{sudo_id}mute", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم كتمه عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command(
    ["الغاء كتم عام$", "الغاء كتم العام$", "الغاء الكتم العام$", "الغاء العام$", "الغاء الحظر العام$", "الغاء حظر عام$",
     "الغاء حظر العام$"], prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_mute_all_user(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم الغاء كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك  الغاء كتم نفسك")
    if msg.reply_to_message.from_user.id == 1001132193:
        return await msg.edit("• لا يمكنك الغاء كتم بارلو")
    r.srem(f"{sudo_id}mute", msg.reply_to_message.from_user.id)
    r.srem(f"{sudo_id}ban", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم الغاء كتمه/حظره عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح قائمه العام$", prefixes=f".") & filters.me & filters.group)
async def un_mute_all_3am(c, msg):
    r.delete(f"{sudo_id}mute")
    r.delete(f"{sudo_id}ban")
    txx = f"• تم مسح المكتومين/المحظورين عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("حظر عام$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def ban_all(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("• تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("• لا يمكنك حظر نفسك")
    if msg.reply_to_message.from_user.id == 1001132193:
        return await msg.edit("• لا يمكنك حظر بارلو")
    r.sadd(f"{sudo_id}ban", msg.reply_to_message.from_user.id)
    txx = f"• العضو {get_name(msg.reply_to_message)} \n• تم حظره عام بنجاح"
    await msg.edit(txx)
