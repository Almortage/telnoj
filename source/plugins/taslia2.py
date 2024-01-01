import asyncio
import random
from collections import deque

import requests
from pyrogram import Client, filters
from pyrogram.types import Message

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


@Client.on_message(filters.regex("^.متحركات (.*)") & filters.me)
async def some(c, msg):
    count = 1
    if ";" in msg.text:
        inpt, count = msg.text.split(";")
    if 0 > int(count) > 20:
        await msg.edit("**- يجب عليك كتابة عدد المتحركات من عدد يبدأ من 1 الى 20"
        )
    jmthonevent = await c.send_message(msg.chat.id, "- جار ارسال المتحركات انتظر قليلا")
    res = requests.get("https://giphy.com/")
    res = res.text.split("GIPHY_FE_WEB_API_KEY =")[1].split("\n")[0]
    api_key = res[2:-1]
    r = requests.get(
        f"https://api.giphy.com/v1/gifs/search?q={inpt}&api_key={api_key}&limit=50"
    ).json()
    list_id = [r["data"][i]["id"] for i in range(len(r["data"]))]
    rlist = random.sample(list_id, int(count))
    for items in rlist:
        await c.send_document(msg.chat.id,  f"https://media.giphy.com/media/{items}/giphy.gif",
                              reply_to_message_id=msg.id)


# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.regex("^.همسة (.*)") & filters.me)
async def wspr(c, msg:Message):
    rrrd7 = "@nnbbot"
    tap = await c.get_inline_bot_results(rrrd7, msg.text[6:])
    await tap[0].click(msg.chat.id)
    await msg.delete()


@Client.on_message(filters.command("م26$", prefixes=f".") & filters.me)
async def _(c, msg):
    if not msg.text[0].isalpha() and msg.text[0] not in ("/", "#", "@", "!"):
        await msg.edit(
            "⌯︙اوامر الهمسه واكس او \n\n⌔︙الامر  • `.همسة`\n⌔︙الاستخدام  • لكتابة همسه سرية لشخص في المجموعه \n\n⌯︙الامر • `.الهمسة`\n⌯︙استخدامه • لعرض كيفية كتابة همسة سرية\n\n⌯︙الامر • `.اكس او `\n ⌯︙استخدامه • ففط ارسل الامر لبدء لعبة اكس او\n\n⌯︙CH  - @qd_G5")


@Client.on_message(filters.command("الهمسة$", prefixes=f".") & filters.me)
async def _(c, msg):
    if not msg.text[0].isalpha() and msg.text[0] not in ("/", "#", "@", "!"):
        await msg.edit(
            "**⌯︙شـرح كيـفية كـتابة همـسة سـرية**\n⌯︙اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n⌯︙مـثال  :   `.همسة ههلا @qd_G5`")


@Client.on_message(filters.command("اكس او$", prefixes=f".") & filters.me)
async def gamez(c, msg):
    jmusername = "@xoBot"
    uunzz = "play"
    tap = await c.get_inline_bot_results(jmusername, uunzz)
    await tap[0].click(msg.chat.id)
    await msg.delete()

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("هينه$", prefixes=f".") & filters.me)
async def permalink_heno(c, msg):
    heno = ['ده بغل مش مستآهل يتهان بالله 🧐😂', 'بس يآبطيخه اخرس خآلص 🤫']
    if not msg.reply_to_message:
        return
    if msg.reply_to_message.from_user.id == 1283542711:
        return await c.send_message(msg.chat.id, f"**- لكك دي هذا المطور**")
    if msg.reply_to_message.from_user.id == 5089553588:
        return await c.send_message(msg.chat.id, f"**- لكك دي هذا المطور**")
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.from_user.id
    sos = random.choice(heno)
    await c.send_message(msg.chat.id, f"{sos} .")

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("نسبة الحب$", prefixes=f".") & filters.me)
async def permalink_hob(c, msg):
    roz = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rza = random.choice(roz)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه الحب بينك وبينه هي {rza}"
    )

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نسبة الانوثة$", prefixes=f".") & filters.me)
async def permalink_onotha(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    if msg.reply_to_message.from_user.id == 5089553588:
        return await msg.edit(f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    if msg.reply_to_message.from_user.id == 1283542711:
        return await msg.edit(f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    sos = random.choice(rr7)
    return await msg.edit( f" • العضو {get_name(msg.reply_to_message)} \n• نسبة الانوثه هي {sos}"
    )

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نسبة الغباء$", prefixes=f".") & filters.me)
async def permalink_abaaa(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه غبائه هي {rzona}"
    )

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نسبة الرجولة$", prefixes=f".") & filters.me)
async def permalink_rgola(c, msg):
    kz = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    if msg.reply_to_message.from_user.id == 1283542711:
        return await msg.edit(f"**100%**")
    if msg.reply_to_message.from_user.id == 5089553588:
        return await msg.edit(f"**100%**")
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    sos = random.choice(kz)
    await msg.edit( f" • العضو {get_name(msg.reply_to_message)} \n• نسبة رجولته هي {sos}"
    )
    
# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نسبة الذكاء$", prefixes=f".") & filters.me)
async def permalink_zakaa(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه الذكاء بتعته هي {rzona}"
    )
    
# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نسبة الكره$", prefixes=f".") & filters.me)
async def permalink_korh(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه كره لك هي {rzona}"
    )
    
# == == == == == == == == == == == == == == == == == == == ==
    
@Client.on_message(filters.command("نسبة الشذوذ$", prefixes=f".") & filters.me)
async def permalink_rain(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه الشذوذ بتعته هي {rzona}"
    )
    
# == == == == == == == == == == == == == == == == == == == ==
    
@Client.on_message(filters.command("نسبة العفانه$", prefixes=f".") & filters.me)
async def permalink_afana(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه عفانته هي {rzona}"
    )

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نسبة الهطل$", prefixes=f".") & filters.me)
async def permalink_hatl(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه هطله هي {rzona}"
    )

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نسبة العبط$", prefixes=f".") & filters.me)
async def permalink_abat(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه عبطه هي {rzona}"
    )
    
# == == == == == == == == == == == == == == == == == == == ==
    
@Client.on_message(filters.command("نسبة القوه$", prefixes=f".") & filters.me)
async def permalink_barlo(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه قوته هي {rzona}"
    )

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نسبة الضعف$", prefixes=f".") & filters.me)
async def permalink_power(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه ضعفه هي {rzona}"
    )

# == == == == == == == == == == == == == == == == == == == ==
    
@Client.on_message(filters.command("نسبة الهبل$", prefixes=f".") & filters.me)
async def permalink_zeim(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"• العضو {get_name(msg.reply_to_message)} \n• نسبه الهبل بتعته هي {rzona}"
    )

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("تحميل$", prefixes=f".") & filters.me)
async def dwn_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(20)
    event = await c.send_message(msg.chat.id, "▯")
    animation_chars = ["▮", "▯", "▬", "▭", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 4])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("مربع$", prefixes=f".") & filters.me)
async def squre_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(20)
    event = await c.send_message(msg.chat.id, "◨")
    animation_chars = ["◧", "◨", "◧", "◨", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 4])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("شرطه$", prefixes=f".") & filters.me)
async def up_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(20)
    event = await c.send_message(msg.chat.id, "╻")
    animation_chars = ["╹", "╻", "╹", "╻", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 4])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("دائره$", prefixes=f".") & filters.me)
async def circle_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(20)
    event = await c.send_message(msg.chat.id, "دائره...")
    animation_chars = ["⚫", "⬤", "●", "∘", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 4])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("تنصيب$", prefixes=f".") & filters.me)
async def anem_1(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    event = await c.send_message(msg.chat.id, "😢")
    animation_chars = [
        "😁",
        "😧",
        "😡",
        "😢",
        "‎**تنصيب سورس كابوس**",
        "??",
        "😧",
        "😡",
        "😢",
        "__**[قناه تنصيب حسابات تيليثون - ✅]**__(t.me/qd_G5)",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("بشره$", prefixes=f".") & filters.me)
async def bshra_1(c, msg):
    animation_interval = 2
    animation_ttl = range(6)
    event = await c.send_message(msg.chat.id, "جميع ألوان البشره يرحقلبي - ❤.")
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁", "**#بباي....**"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قرد$", prefixes=f".") & filters.me)
async def monkey_1(c, msg):
    animation_interval = 2
    animation_ttl = range(12)
    event = await c.send_message(msg.chat.id, "خد قرود يرحقلبي 🤗😂")
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "🖕‎🐵🖕", "**بباي...**"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قياس$", prefixes=f".") & filters.me)
async def herber_1(c, msg):
    animation_interval = 2
    animation_ttl = range(10)
    event = await c.send_message(msg.chat.id, "Power On......")
    animation_chars = [
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 5.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.13GB\n    **🔹used:** 33.77GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 158.98GB\n    **🔹recv:** 146.27GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 159720314\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 20.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 7.18GB\n    **🔹used:** 28.26GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 146.27GB\n    **🔹recv:** 124.33GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 143565654\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 60.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 6.52GB\n    **🔹used:** 35.78GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 124.33GB\n    **🔹recv:** 162.48GB\n    **🔹sent_packets:** 25655655\n    **🔹recv_packets:** 165289456\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.81GB\n    **🔹used:** 30.11GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 162.48GB\n    **🔹recv:** 175.75GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 135345655\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 80.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.76GB\n    **🔹used:** 29.35GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 175.75GB\n    **🔹recv:** 118.55GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 185466554\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 62.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.23GB\n    **🔹used:** 33.32GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 118.55GB\n    **🔹recv:** 168.65GB\n    **🔹sent_packets:** 24786554\n    **🔹recv_packets:** 156745865\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 30.6%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.75GB\n    **🔹used:** 36.54GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 168.65GB\n    **🔹recv:** 128.35GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 1475823589\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 10.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 10.20GB\n    **🔹used:** 25.40GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 128.35GB\n    **🔹recv:** 108.31GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 157865426\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.25GB\n    **🔹used:** 31.14GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 108.31GB\n    **🔹recv:** 167.17GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 124575356\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 76.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.01GB\n    **🔹used:** 33.27GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 167.17GB\n    **🔹recv:** 158.98GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 165455856\n\n\n**===================**\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("يد$", prefixes=f".") & filters.me)
async def yad_1(c, msg):
    animation_interval = 1
    animation_ttl = range(13)
    event = await c.send_message(msg.chat.id, "🖐️")
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 13])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("العد التنازلي$", prefixes=f".") & filters.me)
async def down_t_1(c, msg):
    animation_interval = 1
    animation_ttl = range(12)
    event = await c.send_message(msg.chat.id, "العد التنازلي....")
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 12])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قتل$", prefixes=f".") & filters.me)
async def dier_1(c, msg):
    ALIVE_NAME = (await c.get_users(msg.from_user.id)).mention
    if not msg.reply_to_message:
        name = "مات"
    else:
        name = (await c.get_users(msg.reply_to_message.from_user.id)).mention
    animation_interval = 0.7
    animation_ttl = range(8)
    event = await c.send_message(msg.chat.id, f"**استعد ايها القائد **__{ALIVE_NAME}....")
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - -\n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n<,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}         \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - - {name}\n _/﹋\_\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 8])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("معاكسه$", prefixes=f".") & filters.me)
async def eyes_1(c, msg):
    ALIVE_NAME = (await c.get_users(msg.from_user.id)).mention
    if not msg.reply_to_message:
        name = "تم المعاكسه يبنلقمرر - 💋"
    else:
        name = (await c.get_users(msg.reply_to_message.from_user.id)).mention
    animation_interval = 0.7
    animation_ttl = range(15)
    event = await c.send_message(msg.chat.id, f"**جآري المعاكسه يا **__{ALIVE_NAME}....")
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        "👁👁\n  👱🏻‍♂️  =====>اي يا مزه عمله اي ؟",
        "👁👁\n  👱🏻‍♀️  =====> انا تمام",
        "👁👁\n  👱🏻‍♂️  =====> اي القمر ده🤤",
        "👁👁\n  👱🏻‍♀️  =====> اي مالك",
        "👁👁\n  👱🏻‍♂️  =====> مستغرب جمالك 🤤",
        "👁👁\n  👱🏻‍♀️  =====> بسسس ",
        "👁👁\n  👱🏻‍♂️  =====> متت 😹",
        "👁👁\n  👱🏻‍♀️  =====> لا تضحك",
        "👁👁\n  👱🏻‍♂️  =====> والله مستغرب بس 😹🤤",
        "👁👁\n  👱🏻‍♀️  =====> بس لتضحك😭😒",
        "👁👁\n  👱🏻‍♂️  =====> مححح🤤",
        "👁👁\n  👱🏻‍♀️  =====> متبوصش بس",
        "👁👁\n  👱🏻‍♂️  =====> دولي",
        "👁👁\n  👱🏻‍♂️  =====> ماشي بايي",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 15])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("عبقري$", prefixes=f".") & filters.me)
async def abkary_1(c, msg):
    animation_interval = 0.05
    animation_ttl = range(288)
    event = await c.send_message(msg.chat.id, "افكرر..")
    animation_chars = [
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "دا افكر 🙁😹 ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 36])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("افعي$", prefixes=f".") & filters.me)
async def aph3a_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(27)
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 27])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("ولد$", prefixes=f".") & filters.me)
async def man_1(c, msg):
    animation_interval = 0.5
    animation_ttl = range(16)
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🚗\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛🚗⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚗⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚗⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🚗⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛🚗⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n🚗⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛😊⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 16])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("مايكرو$", prefixes=f".") & filters.me)
async def miكابوسo_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(28)
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 28])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("فايروس$", prefixes=f".") & filters.me)
async def vayros_1(c, msg):
    animation_interval = 1
    animation_ttl = range(30)
    animation_chars = [
        "🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "‎◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎??🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",
        "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",
        "◼️◼️\n◼️◼️",
        "◼️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 30])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("قطار$", prefixes=f".") & filters.me)
async def train_1(c, msg):
    animation_interval = 0.2
    animation_ttl = range(30)
    animation_chars = [
        "**ت**",
        "**تو**",
        "**توتت**",
        "**تووووت**",
        "**توووت**",
        "**تووووت**",
        "**توووووت**",
        "**توووووت**",
        "**توووووووووت**",
        "**توووووووووووت**",
        "**اجه القطار 🚅**",
        "**وخر عن  🚅🚃🚃**",
        "**تووووت 🚅🚃🚃🚃**",
        "**جبنها وجت ويانه 🚅🚃🚃🚃🚃**",
        "**جبناها وجت ويانه 🚅🚃🚃🚃🚃🚃**",
        "**مطر 🚅🚃🚃🚃🚃🚃🚃**",
        "**بيباي 🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**مو قطار ضيم**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 30])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("نيكول$", prefixes=f".") & filters.me)
async def tikol_1(c, msg):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Lavde   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pehli   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(P)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Fursat  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Meeee   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀lodu⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("موسيقي$", prefixes=f".") & filters.me)
async def music_1(c, msg):
    animation_interval = 1.5
    animation_ttl = range(11)
    animation_chars = [
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀ [مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 11])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("رسم$", prefixes=f".") & filters.me)
async def pain_1(c, msg):
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("نجمه$", prefixes=f".") & filters.me)
async def star_1(c, msg):
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("مكعبات$", prefixes=f".") & filters.me)
async def mq3bat_1(c, msg):
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(50):
        await asyncio.sleep(0.3)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("مطر$", prefixes=f".") & filters.me)
async def rain_1(c, msg):
    msg = await c.send_message(msg.chat.id, "`مطر.......`")
    deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("تفريغ$", prefixes=f".") & filters.me)
async def tafreq_1(c, msg):
    # try:
    #     obj = msg.pattern_match.group(1)
    #     if len(obj) != 3:
    #         return await msg.edit("`Input length must be 3 or empty`")
    #     inp = " ".join(obj)
    # except IndexError:
    #     inp = "🥞 🎂 🍫"
    inp = "🥞 🎂 🍫"
    u, t, g, o, s, n = inp.split(), "🗑", "<(^_^ <)", "(> ^_^)>", "⠀ ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
            [
                y
                for y in (
                    [
                        "".join(x)
                        for x in (
                            f + (s, g, s + s * f.count(""), t),
                            f + (g, s * 2 + s * f.count(""), t),
                            f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                            f[:i] + (s + s * f.count(""), o, f[i], s, t),
                            f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                            f[:i] + (s * 3 + s * f.count(""), o, t),
                            f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                    ]
                    for i, f in enumerate(reversed(h))
            )
            ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            await msg.edit(something_else)

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("فليم$", prefixes=f".") & filters.me)
async def film_1(c, msg):
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
    ]
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])


love = [
    """
█▀███▀▀███▀▀███▀▀███▀▀███▀█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒█▒▒▒▒▒███▒▒█▒▒▒█▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒█▒▒▒▒▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█▒▒▒▒▒█
█▒▒████▒▒███▒▒▒▒█▒▒▒█████▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒█
█▒▒▒▒▒▒▒█──█▒████▒█──█▒▒▒▒█
█▒▒▒▒▒▒█──█─█────█─█──█▒▒▒█
█▒▒▒▒▒▒█─██───────███─█▒▒▒█
█▒▒▒▒▒▒█──────────────█▒▒▒█
█▒▒▒▒▒▒▒█────────────█▒▒▒▒█
█▒▒▒▒██▒▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█────███────█▒▒▒▒█
█▒▒▒█──█▒█───█───█──█▒▒▒▒▒█
█▒▒▒▒█──█─█───███──█▒▒▒▒▒▒█
█▒▒▒▒▒█────██────██▒▒▒▒▒▒▒█
█▒▒▒▒▒█──────████─██▒▒▒▒▒▒█
█▒▒▒▒▒▒█───────────█▒▒▒▒▒▒█
█▒▒▒▒▒▒▒███─────────█▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒█──────█───█▒▒▒▒█
█▒▒▒▒███▒▒█───────█───█▒▒▒█
█▒▒▒█──████─────████───█▒▒█
█▒▒▒█────█─────█────█─█▒▒▒█
█▒▒▒█─────█────█────██▒▒▒▒█
█▒▒▒█──────█───█──────█▒▒▒█
█▒▒▒▒█─────██████─────█▒▒▒█
█▒▒▒▒▒█──███▒▒▒▒█─────█▒▒▒█
█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█───█▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒█
█▒▒▒▒█▒▒▒▒█▒▒███▒▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒█▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒██▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒▒▒▒▒███▒▒▒███▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▄▄█▄▄██▄▄█▄▄█▄▄█▄▄██▄▄█▄▄█
""",
    """
╔══╗
╚╗╔╝
╔╝(¯`v´¯)
╚══`.¸.YOU
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄▄▄▄░░░░▄▄▄░░░░▄▄▄░░░░░░
░░░▀████▀░░▄█████▄▄█████▄░░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░▀██████████████▀░░░
░░░░▄██▄░░░░▀██████████▀░░░░░
░░░██████░░░░░▀██████▀░░░░░░░
░░░░░░░░░░░░░░░░▀██▀░░░░░░░░░
░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
░░▀███░███▀▄█▀▀█▄░▀██▀░▀██▀░░
░░░░▀█▄█▀░▄█░░░░█▄░██░░░██░░░
░░░░░░█░░░██░░░░██░██░░░██░░░
░░░░░░█░░░░█▄░░▄█░░██░░░██░░░
░░░░▄███▄░░░▀██▀░░░░▀███▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄░░░░▄███▄▄███▄░░░░░░▄░░▄░░░░░░░░
░░░░█░░░░░██████████░░░░░░█░░█░░░░░░░░
░░░░█░░░░░░▀██████▀░░░░░░░█░░█░░░░░░░░
░░░▀▀▀░░░░░░░▀██▀░░░░░░░░░░▀▀░░░░░░░░░
░░░░░░░░░░░░▄░░░░░█░▄▀░░▄░░░░░░░░░░░░░
░░░░░░░░▄░░░▀▄▄▄▀█▀▀█▀▀▄█▄░█░░░░░░░░░░
░░░░░░░░░▀▄▄▀█░░░▀░░░░░░░░█▄░▄▀▀░░░░░░
░░░░░▀▀▄░█▀░░░░░░░░░▄▄▄▄▄▄░▀█░░░░░░░░░
░░░░░░▄▀▀░▄▄▀▀▀▄░░▄█▀░░░░▀▄░▄█▀▀▀▄░░░░
░░░▄▄██░░█░░░░░░█░█░░███░▄▀░░░██░█░░░░
░░█░▄█░░░█░███░▄▀░▀▀▄███▀░░░░░██░█░░░░
░░█░▀█▄░░▀▄███▄▀░░░░░░░░░░░░░▄█▄▀░░░░░
░░░▀▀▀▀█░░░░░░░░░░░░░░░▄█▀░░▄▀░░░░▄░░░
░░░░▄░░░▀▄░▀▀▄▄░░░░░▄▄▀▀░░▄▀░░░░▄█▀░░░
░░▄▄█▄░░░░▀▀▄▄░▀▀▀▀▀░▄▄▄▀▀░░▄▄▀▀▀█▀▀░░
░░▄█▀▀▀▀▄▄▄▄░░▀▀▀▀▀█▀░░░▄▄▀▀░░░░░░▀░░░
░░░░░░░░░░░░▀▀▀▀▀▄▄█▄▄▀▀░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░░░
""",
    """
────╪███████╪────╪███████
──╪███████████╪╪███████████
──██████████████████████████
─████████████████████████████
─████████████████████████████
─████████████████████████████
─████████████████████████████
──██████████████████████████
──╪████████████████████████
───╪██████████████████████
─────████████████████████
──────╪████████████████
────────╪████████████
──────────╪████████
─────────────╪██
████─╪███╪╪████████──████─████
╪███─╪███─████╪████──████─████
─███─╪███─████─╪███╪─████─████
─███╪╪██╪─████─╪███╪─████─████
─╪██████──████─╪███╪─████─████
──██████──████─╪███╪─████─████
──█████╪──████─╪███╪─████─████
──╪████───████─╪███╪─████─████
───████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───█████████──█████████
───████────███████╪──╪███████
""",
    """
───▄▄▄▄▄▄─────▄▄▄▄▄▄
─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄
▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌
█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█
█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█
▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌
─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀
───▀█▓▓▒▒░░░░░▒▒▓▓█▀
─────▀█▓▓▒▒░▒▒▓▓█▀
──────▀█▓▓▒▓▓█▀
────────▀█▓█▀
──────────▀
""",
    """
░███████░
░█╬╬╬╬╬█░
░██╬╬███░
░██╬╬███░
░██╬╬███░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬╬████░
░█╬╬╬╬██░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░██╬╬╬██░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
""",
    '''
                /'    `\./'    `\
               (  o  o  |  u  u  )
               ;`.  V  /"\  V  .';
       """"\."     __ ) ( __     "./""""/
        \   ;     aP""Y,_,P""Ya     ;   /
         `,; ._  d'    `"'    `b  _. ;,'
      ,,,,aaaaaa.8,  I  Love  ,8.aaaaaa,,,,
      I8\\\\\\\\\`Y,   You   ,P'/////////8I
       "Ya\\\\\\\\\"Y,     ,P"/////////aY"
         "Ya\\\\\\\\\"Y,_,P"/////////aP"
           `"Ya\\\\\\\\`Y'////////aP"'
              `"""""""""""""""""""'
''',
    """
                         %%%%%%%%%%%%%
                         %%%%%%%%%%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                         %%%%%%%%%%%%%
                         %%%%%%%%%%%%%




  ::::          ::::::      ::::      ::::    :::::::::
  ::::        ::::  ::::    ::::      ::::    :::::::::
  ::::       ::::    ::::   ::::      ::::    ::::
  ::::       ::::    ::::    ::::    ::::     ::::::::
  ::::       ::::    ::::     ::::  ::::      ::::
  ::::       ::::    ::::      ::::::::       ::::
  ::::::::::  ::::  ::::        ::::::        :::::::::
  ::::::::::    ::::::           ::::         :::::::::


                   Y O U
""",
    """
           ..//``~~~~~-=+=-=+~~~~\\.      .//~~~~=-=+=-~~~~~''\\..
       ..//=+=-=+=-=+=-=+=-=+=-=+=-\\    //=+=-=+=-=+=-=+=-=+=-=+=\\..
      //+=-=+=-=+=-=+=-=+=-=+=-=+=-=+\\//=-=+=-=+=-=+=-=+=-=+=-=+=-=+\\
    //-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-\\
   ++=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=++
   ||~~\    /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~||
   ||  /    \        /   \        /   \        /   \        /   \       ||
   ||/        \    /       \    /       \    /       \    /       \    /||
   ||           \/           \/           \/           \/           \/  ||
   ++=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=++
    \\-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=//
      `\\=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+//'
        |`\\+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//'
        |   `\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''
        |      ``\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''
   _____|_____     ``\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''     
  |   I Love  |        ``\\=+=-=+=-=+=-=+=-=+=-=+=//''
  |    You.   |            ``\\=+=-=+=-=+=-=+=//''
  |   * HUG*  |                ``\\=+=-=+=//''
   ~~~~~~~~~~~                     ``\\//''
""",
    """
                  IIIIIIIIIII
                  IIIIIIIIIII
                      III
                      III
                      III
                      III
                      III
                  IIIIIIIIIII
                  IIIIIIIIIII

LLL          OOOOOOOO    VV       VV  EEEEEEEEEE
LLL         OOOOOOOOOO   VV       VV  EEEEEEEEEE
LLL         OO      OO   VV       VV  EE
LLL         OO      OO   VV       VV  EE
LLL         OO      OO   VV       VV  EEEEEEE
LLL         OO      OO    VV     VV   EE
LLL         OO      OO     VV   VV    EE
LLLLLLLLLL  OOOOOOOOOO      VV VV     EEEEEEEEEE
LLLLLLLLLL   OOOOOOOO         V       EEEEEEEEEE

        YY      YY   OOOOOOOO   UUU    UUU
         YY    YY   OOOOOOOOOO  UUU    UUU
          YY  YY    OO      OO  UUU    UUU
           YYYY     OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OOOOOOOOOO  UUUUUUUUUU
            YY       OOOOOOOO    UUUUUUUU
""",
    """
██─▄███▄███▄─██▄──▄██──▄███▄──██──██
██─█████████──▀████▀──██▀─▀██─██──██
██──▀█████▀─────██────██▄─▄██─██──██
██────▀█▀───────██─────▀███▀──▀████
""",
    '''
‎_/)______./¯"""/') ___/)___/)__,-----------’)_• ___/)_/)__./¯/)/)
¯¯\)¯¯¯¯¯'\_„„„„\) ¯\)¯¯¯¯¯\)¯¯‘-----------.)¯• ¯\)¯¯¯¯\)¯'\_\)\)
██░░░██░░░░▄███▄░░██░░░██░████░░░██░░██
██░░░██░░░██▀░▀██░██▄░▄██░██▄░░░░██░░██
██░░░██░░░██▄░▄██░░██▄██░░██▀░░░░██░░██
██░░░████░░▀███▀░░░░███░░░████░░░▀████▀
_/)______./¯"""/') ___/)___/)__,-----------’)_• ___/)_/)__./¯/)/)
¯¯\)¯¯¯¯¯'\_„„„„\) ¯\)¯¯¯¯¯\)¯¯‘-----------.)¯• ¯\)¯¯¯¯\)¯'\_\)\)
''',
    """
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒░░░░░░═░░▒▒▒▒░░░░░░▒▒▒░░░░═░▒▒▒▒▒▒
▒▒▒▒▒▒░████████▓░▒▒░░█████░══█████▓═░▒▒▒▒
▒▒▒▒▒░▓█████████░▒░█████████████████░▒▒▒▒
▒▒▒▒▒▒░░░▒███░▒░▒░▒██████████████████═▒▒▒
▒▒▒▒▒▒▒░░═███═░▒▒░███████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒░███████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███═▒▒▒░▒██████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒▒═█████████████████═▒▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒▒▒─███████████████░░▒▒▒▒
▒▒▒▒▒▒▒▒░═███═░▒▒▒▒▒─█████████████═░▒▒▒▒▒
▒▒▒▒▒▒░░░▒███░▒░▒▒▒▒▒░░█████████▒═▒▒▒▒▒▒▒
▒▒▒▒▒░▒█████████═▒▒▒▒▒░═░█████▒═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░████████▒░▒▒░░░▒▒░═░▓▒═░▒▒▒▒░▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░░▒░░═░░░░░░░░░▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████─██████████░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████═▒████████░░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░─███▒─▒░─███░═░░░▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─███▒░─███░░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─███═███▒░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─█████▒░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─████═▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███═▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░─███═══░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████▒░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████▓░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░──────═░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░═▓█████▒═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒█████████░░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═█████░░░████▒░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███═░░▒░═░███═▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═███░░▒▒▒▒▒░▓███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███═▒▒▒▒▒▒░░███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███░░▒▒▒▒▒░▒███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███─░▒▒░░═███░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═████▒══░▓████░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─██████████▓═▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███████═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░═───░───═░░░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓██████─███████░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███████─███████░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒███░░▒░░████─▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███═░▒▒░▒██▒░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▓██▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▓██▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▒███░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███─░▒░═███▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═████░░░████═▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─█████████═▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒█████▓─▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░═░░▒▒▒▒▒▒▒▒▒▒
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░▄▄▄▄▄▄░░░░░░░░░▄▄▄▄▄▄░░░░░░░░
░░░░▄▄▄▄░░░░▄▄▄▄░░░▄▄▄▄░░░░▄▄▄▄░░░░░
░▄▄▄▄░░░░░░░░░░░▄░▄░░░░░░░░░░░▄▄▄▄░░
▄▄░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░░▄▄░
▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄░
▄▄░▐█▀▀██▀▀▀█▀█▀█▀▀█▄▄▄▄▄▄▄▄▄▄▄▄░▄▄░
▄▄░▐█──██─█─█─█─█─▀█─█─█─█▀█─█─█░▄▄░
▄▄░▐█──██─▀─█▄─▄█─▀█──█──█▄█─█▄█░▄▄░
▄▄░▐█▄▄▄█▀▀▀▀▀▀▀▀▀▀▀████████████░▄▄░
░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄░░
░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░▄▄▄▄░░░░
░░░░░░▄▄▄▄░░░░░░░░░░░░░░░▄▄▄▄░░░░░░░
░░░░░░░░░▄▄▄▄░░░░░░░░░▄▄▄▄░░░░░░░░░░
░░░░░░░░░░░░▄▄▄▄░░░▄▄▄▄░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▄▄▄▄▄░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▄▄▄░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░░░░░
""",
]

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("hack", ".") & filters.me)
async def hak(client: Client, message: Message):
  await message.edit_text("Looking for WhatsApp databases in targeted person...")
  asyncio.sleep(2)
  await message.edit_text(" User online: True\nTelegram access: True\nRead Storage: True ")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\nLooking for WhatsApp...\nETA: 0m, 20s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\nLooking for WhatsApp...\nETA: 0m, 18s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\nFound folder C:/WhatsApp\nETA: 0m, 16s")  
  asyncio.sleep(2)
  await message.edit_text("Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\nFound folder C:/WhatsApp\nETA: 0m, 14s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\nSearching for databases\nETA: 0m, 12s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 55.30%\n[█████████░░░░░░░░░░░]\nFound msgstore.db.كابوسypt12\nETA: 0m, 10s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 64.86%\n[███████████░░░░░░░░░]\nFound msgstore.db.كابوسypt12\nETA: 0m, 08s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 74.02%\n[█████████████░░░░░░░]\nTrying to Deكابوسypt...\nETA: 0m, 06s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 86.21%\n[███████████████░░░░░]\nTrying to Deكابوسypt...\nETA: 0m, 04s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 93.50%\n[█████████████████░░░]\nDeكابوسyption successful!\nETA: 0m, 02s")
  asyncio.sleep(2)
  await message.edit_text("Hacking... 100%\n[████████████████████]\nScanning file...\nETA: 0m, 00s")
  asyncio.sleep(2)
  await message.edit_text("Hacking complete!\nUploading file...")
  asyncio.sleep(2)
  await message.edit_text("Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n./DOWNLOADS/msgstore.db.كابوسypt12")
 
# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("شرطة$", prefixes=f".") & filters.me)
async def offeser_1(c, msg):
    if not msg.reply_to_message:
        return
    animation_interval = 0.3
    animation_ttl = range(12)
    mention = (await c.get_users(msg.reply_to_message.from_user.id)).mention
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        f"{mention} **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 12])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("اذكار الصباح$", prefixes=f".") & filters.me)
async def jio_2(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
#اذكار_الصباح
«أعُوذُ بِكَلِمَاتِ اللهِ التَّامَّاتِ مِنْ شَرِّ مَا خَلَقَ»

- ٣ مرَّات.

-----------------------‐

«اللَّهُمَّ بِكَ أمْسَيْنَا ، وَبِكَ أصْبَحْنَا ، وَبِكَ نَحْيَا ، وَبِكَ نَمُوتُ ، وَإلَيْكَ المَصِيرُ»

-----------------------‐

«اللَّهُمَّ مَا أمْسَى بِي مِنْ نِعْمَةٍ أوْ بِأحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ ، فَلَكَ الحَمْدُ وَلَكَ الشُّكْرُ»

-----------------------‐

«اللَّهُمَّ إنِّي أمْسَيْتُ أُشْهِدُكَ ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ ، وَمَلَائِكَتَكَ ، وَجَمِيعَ خَلْقِكَ ، أنَّكَ أنْتَ اللهُ لَا إلَهَ إلَّا أنْتَ وَحْدَكَ لَا شَرِيكَ لَكَ ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ»

- ٤ مرَّات.

-----------------------‐

«أمْسَيْنَا وَأمْسَى المُلْكُ للهِ رَبِّ العَالَمِينَ ،
اللَّهُمَّ إنِّي أسْألُكَ خَيْرَ هَذِهِ اللَّيْلَةِ ، فَتْحَهَا ، وَنَصْرَهَا ، وَنُورَهَا ، وَبَرَكَتَهَا ، وَهُدَاهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِيهَا وَشَرِّ مَا بَعْدَهَا»

-----------------------‐

«أمْسَيْنَا عَلَى فِطْرَةِ الإسْلَامِ ، وَعَلَى كَلِمَةِ الإخْلَاصِ ، وَعَلَى دِينِ نَبِيِّنَا مُحَمَّدٍ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ ، وَعَلَى مِلَّةِ أبِينَا إبْرَاهِيمَ ، حَنِيفًا مُسْلِمًا وَمَا كَانَ مِنَ المُشْرِكِينَ»

-----------------------‐

«أمْسَيْنَا وأمْسَى المُلْكُ للهِ والحَمْدُ للهِ ، لَا إلَهَ إلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ المُلْكُ وَلَهُ الحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ،
رَبِّ أسْألُكَ خَيْرَ مَا فِي هَذِهِ اللَّيْلَةِ وَخَيْرَ مَا بَعْدَهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذِهِ اللَّيْلةِ وَشَرِّ مَا بَعْدَهَا ،
رَبِّ أعُوذُ بِكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ ، رَبِّ أعُوذُ بِكَ مِنْ عَذَابٍ فِي النَّارِ وَعَذَابٍ فِي القَبْرِ» .
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
        
        

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("اذكار المساء$", prefixes=f".") & filters.me)
async def jio_1(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
"""
#اذكار_المساء
«الحَمْدُ للهِ وَحْدَهُ ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى مَنْ لَا نَبِيَّ بَعْدَهُ»

-----------------------‐

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ :

﴿اللهُ لَا إِلَهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ وَلَا يَئُودُهُ حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ﴾

-----------------------‐

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ :

﴿قُلْ هُوَ اللهُ أَحَدٌ ۝ اللهُ الصَّمَدُ ۝ لَمْ يَلِدْ وَلَمْ يُولَدْ ۝ وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ﴾

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ :

﴿قُلْ أَعُوذُ بِرَبِّ الفَلَقِ ۝ مِن شَرِّ مَا خَلَقَ ۝ وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ ۝ وَمِن شَرِّ النَّفَّاثَاتِ فِي العُقَدِ ۝ وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ﴾

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ :

﴿قُلْ أَعُوذُ بِرَبِّ النَّاسِ ۝ مَلِكِ النَّاسِ ۝ إِلَهِ النَّاسِ ۝ مِن شَرِّ الوَسْوَاسِ الخَنَّاسِ ۝ الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ ۝ مِنَ الجِنَّةِ وَالنَّاسِ﴾

-----------------------‐

«أصْبَحْنَا وَأصْبَحَ المُلْكُ للهِ والحَمْدُ للهِ ، لَا إلهَ إلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ المُلْكُ وَلَهُ الحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ،
رَبِّ أسْألُكَ خَيْرَ مَا فِي هَذَا اليَوْمِ وَخَيْرَ مَا بَعْدَهُ ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذَا اليَوْمِ وَشَرِّ مَا بَعْدَهُ ،
رَبِّ أعُوذُ بِكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ ، رَبِّ أعُوذُ بِكَ مِنْ عَذَابٍ فِي النَّارِ وعَذَابٍ فِي القَبْرِ»

- وإذا أمسى يقول :

«أمْسَيْنَا وأمْسَى المُلْكُ للهِ والحَمْدُ للهِ ، لَا إلهَ إلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ المُلْكُ وَلَهُ الحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ،
رَبِّ أسْألُكَ خَيْرَ مَا فِي هَذِهِ اللَّيْلَةِ وَخَيْرَ مَا بَعْدَهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذِهِ اللَّيْلةِ وَشَرِّ مَا بَعْدَهَا ،
رَبِّ أعُوذُ بِكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ ، رَبِّ أعُوذُ بِكَ مِنْ عَذَابٍ فِي النَّارِ وَعَذَابٍ فِي القَبْرِ»

-----------------------‐

«اللَّهُمَّ بِكَ أصْبَحْنَا ، وَبِكَ أمْسَيْنَا ، وَبِكَ نَحْيَا ، وَبِكَ نَمُوتُ ، وَإلَيْكَ النُّشُورُ»

- وإذا أمسى يقول :

«اللَّهُمَّ بِكَ أمْسَيْنَا ، وَبِكَ أصْبَحْنَا ، وَبِكَ نَحْيَا ، وَبِكَ نَمُوتُ ، وَإلَيْكَ المَصِيرُ»

-----------------------‐

«اللَّهُمَّ أنْتَ رَبِّي لَا إلَهَ إلَّا أنْتَ ،
خَلَقْتَنِي وَأنَا عَبْدُكَ ، وَأنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ ، أعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ ،
أبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ ، وَأبُوءُ بِذَنْبِي فَاغْفِرْ لِي ؛ فَإنَّهُ لَا يَغْفِرُ الذُّنُوبَ إلَّا أنْتَ»

-----------------------‐

«اللَّهُمَّ إنِّي أصْبَحْتُ أُشْهِدُكَ ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ ، وَمَلائِكَتَكَ ، وَجَمِيعَ خَلْقِكَ ، أنَّكَ أنْتَ اللهُ لَا إلَهَ إلَّا أنْتَ وَحْدَكَ لَا شَرِيكَ لَكَ ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ»

- ٤ مرَّات.

- وإذا أمسى يقول :

«اللَّهُمَّ إنِّي أمْسَيْتُ أُشْهِدُكَ ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ ، وَمَلائِكَتَكَ ، وَجَمِيعَ خَلْقِكَ ، أنَّكَ أنْتَ اللهُ لَا إلَهَ إلَّا أنْتَ وَحْدَكَ لَا شَرِيكَ لَكَ ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ»

- ٤ مرَّات.

-----------------------‐

«اللَّهُمَّ مَا أصْبَحَ بِي مِنْ نِعْمَةٍ أوْ بِأحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ ، فَلَكَ الحَمْدُ وَلَكَ الشُّكْرُ»

- وإذا أمسى يقول :

«اللَّهُمَّ مَا أمْسَى بِي مِنْ نِعْمَةٍ أوْ بِأحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ ، فَلَكَ الحَمْدُ وَلَكَ الشُّكْرُ»

-----------------------‐

«اللَّهُمَّ عَافِنِي فِي بَدَنِي ، اللَّهُمَّ عَافِنِي فِي سَمْعِي ، اللَّهُمَّ عَافِنِي فِي بَصَرِي ، لَا إلَهَ إلَّا أنْتَ ،
اللَّهُمَّ إنِّي أعُوذُ بِكَ مِنَ الكُفْرِ وَالفَقْرِ ، وَأعُوذُ بِكَ مِنْ عَذَابِ القَبْرِ ، لَا إلَهَ إلَّا أنْتَ»

- ٣ مرَّات.
"""
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])



@Client.on_message(filters.command("barlo$", prefixes=f".") & filters.me)
async def jio_1(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    event = await c.send_message(msg.chat.id, "jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "*Optimising JIO NETWORK...*",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ █`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("النظام الشمسي$", prefixes=f".") & filters.me)
async def sun_sys_1(c, msg):
    animation_interval = 0.1
    animation_ttl = range(80)
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 8])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("افكر$", prefixes=f".") & filters.me)
async def guess_1(c, msg):
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("متت$", prefixes=f".") & filters.me)
async def mttt_1(c, msg):
    deq = deque(list("😹🤣😂😹🤣😂"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("زعلت$", prefixes=f".") & filters.me)
async def dayeg_1(c, msg):
    deq = deque(list("😕😞🙁☹️😕😞🙁"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("ساعه$", prefixes=f".") & filters.me)
async def clock_1(c, msg):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("مح$", prefixes=f".") & filters.me)
async def moh_1(c, msg):
    deq = deque(list("😗😙😚😚💋😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("جيم$", prefixes=f".") & filters.me)
async def game_11(c, msg):
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("الارض$", prefixes=f".") & filters.me)
async def ard_1(c, msg):
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)


# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قمر$", prefixes=f".") & filters.me)
async def qamr_1(c, msg):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("اقمار$", prefixes=f".") & filters.me)
async def aqmar_1(c, msg):
    event = await c.send_message(msg.chat.id, "اقمار")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.edit("اقمار..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("غبي", ".") & filters.me)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("brain")
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("دايره", ".") & filters.me)
async def gkahgagw(client: Client, message: Message):
    animation_interval = 0.3
    animation_ttl = range(0, 30)
    animation_chars = [
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜  [𝚁𝙾𝚈𝙰𝙻 𝚂𝙾𝚄𝚁𝙲𝙴](https://t.me/qd_G5) ⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
    ]
    if message.forward_from:
        return
    await message.edit("كابوس..كابوس..كابوس..كابوس")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command(["سلاحف", "سلحفه"], ".") & filters.me)
async def solhfa(client: Client, message: Message):
    await message.edit_text("`وسع يبآشا 🧐`")
    asyncio.sleep(1)
    await message.edit_text("`جآري بدأ سباق السلآحف.`")
    asyncio.sleep(1)
    await message.edit_text("`جآري بدأ سباق السلآحف..`")
    asyncio.sleep(1)
    await message.edit_text("`جآري بدأ سباق السلآحف...`")
    asyncio.sleep(1)
    await message.edit_text("`جآري بدأ سباق السلآحف....`")
    asyncio.sleep(1)
    await message.edit_text("`جآري بدأ سباق السلآحف.....`")
    asyncio.sleep(1)
    await message.edit_text("`آنتظر يسسسستا 🧐😂`")
    asyncio.sleep(1)
    await message.edit_text("`جآري بدء السبآق الآن........`")
    asyncio.sleep(1)
    await message.edit_text("🙈🙈🙈🙈")
    await message.edit_text("🙉🙉🙉🙉")
    await message.edit_text("🙈🙈🙈🙈")
    await message.edit_text("🙉🙉🙉🙉")
    await message.edit_text("`تم بدء السبآق يرحقلبي ❤`")
    await message.edit_text("🙉🙉🙉🙉")
    await message.edit_text("🐢                       🚶")
    await message.edit_text("🐢                      🚶")
    await message.edit_text("🐢                     🚶")
    await message.edit_text("🐢                    🚶")
    await message.edit_text("🐢                   🚶")
    await message.edit_text("🐢                  🚶")
    await message.edit_text("🐢                 🚶")
    await message.edit_text("🐢                🚶")
    await message.edit_text("🐢               🚶")
    await message.edit_text("🐢              🚶")
    await message.edit_text("🐢             🚶")
    await message.edit_text("🐢            🚶")
    await message.edit_text("🐢           🚶")
    await message.edit_text("🐢          🚶")
    await message.edit_text("🐢         🚶")
    await message.edit_text("🐢        🚶")
    await message.edit_text("🐢       🚶")
    await message.edit_text("🐢      🚶")
    await message.edit_text("🐢     🚶")
    await message.edit_text("🐢    🚶")
    await message.edit_text("🐢   🚶")
    await message.edit_text("🐢  🚶")
    await message.edit_text("🐢 🚶")
    await message.edit_text("🐢🚶")
    await asyncio.sleep(1)
    await message.edit_text("🚶🐢")
    await message.edit_text("🚶 🐢")
    await message.edit_text("🚶  🐢")
    await message.edit_text("🚶   🐢")
    await message.edit_text("🚶    🐢")
    await message.edit_text("🚶     🐢")
    await message.edit_text("🚶      🐢")
    await message.edit_text("🚶       🐢")
    await message.edit_text("🚶        🐢")
    await message.edit_text("🚶         🐢")
    await message.edit_text("🚶          🐢")
    await message.edit_text("🚶           🐢")
    await message.edit_text("🚶            🐢")
    await message.edit_text("🚶             🐢")
    await message.edit_text("🚶              🐢")
    await message.edit_text("🚶               🐢")
    await message.edit_text("🚶                🐢")
    await message.edit_text("🚶                 🐢")
    await message.edit_text("🚶                  🐢")
    await message.edit_text("🚶                   🐢")
    await message.edit_text("🚶                    🐢")
    await message.edit_text("🚶                     🐢")
    await message.edit_text("🚶                      🐢")
    await message.edit_text("🚶                       🐢")
    await message.edit_text("🚶                        🐢")
    await message.edit_text("🚶                         🐢")
    await message.edit_text("🚶                          🐢")
    await message.edit_text("🚶                           🐢")
    await message.edit_text("🚶                            🐢")
    await message.edit_text("🚶                             🐢")
    await message.edit_text("🚶                              🐢")
    await message.edit_text("🚶                               🐢")
    await message.edit_text("🚶                                🐢")
    await message.edit_text("🚶                                 🐢")
    await message.edit_text("`AHHH TAPATAP`")
    await message.edit_text("🙉")
    await message.edit_text("🙈")
    await message.edit_text("🙉")
    await message.edit_text("🙈")
    await message.edit_text("🙉")
    await message.edit_text("😂")
    await message.edit_text("🐢                       🚶")
    await message.edit_text("🐢                      🚶")
    await message.edit_text("🐢                     🚶")
    await message.edit_text("🐢                    🚶")
    await message.edit_text("🐢                   🚶")
    await message.edit_text("🐢                  🚶")
    await message.edit_text("🐢                 🚶")
    await message.edit_text("🐢                🚶")
    await message.edit_text("🐢               🚶")
    await message.edit_text("🐢              🚶")
    await message.edit_text("🐢             🚶")
    await message.edit_text("🐢            🚶")
    await message.edit_text("🐢           🚶")
    await message.edit_text("🐢          🚶")
    await message.edit_text("🐢         🚶")
    await message.edit_text("🐢        🚶")
    await message.edit_text("🐢       🚶")
    await message.edit_text("🐢      🚶")
    await message.edit_text("🐢     🚶")
    await message.edit_text("🐢    🚶")
    await message.edit_text("🐢   🚶")
    await message.edit_text("🐢  🚶")
    await message.edit_text("🐢 🚶")
    await message.edit_text("🐢🚶")
    await asyncio.sleep(1)
    await message.edit_text("🚶🐢")
    await message.edit_text("🚶 🐢")
    await message.edit_text("🚶  🐢")
    await message.edit_text("🚶   🐢")
    await message.edit_text("🚶    🐢")
    await message.edit_text("🚶     🐢")
    await message.edit_text("🚶      🐢")
    await message.edit_text("🚶       🐢")
    await message.edit_text("🚶        🐢")
    await message.edit_text("🚶         🐢")
    await message.edit_text("🚶          🐢")
    await message.edit_text("🚶           🐢")
    await message.edit_text("🚶            🐢")
    await message.edit_text("🚶             🐢")
    await message.edit_text("🚶              🐢")
    await message.edit_text("🚶               🐢")
    await message.edit_text("🚶                🐢")
    await message.edit_text("🚶                 🐢")
    await message.edit_text("🚶                  🐢")
    await message.edit_text("🚶                   🐢")
    await message.edit_text("🚶                    🐢")
    await message.edit_text("🚶                     🐢")
    await message.edit_text("🚶                      🐢")
    await message.edit_text("🚶                       🐢")
    await message.edit_text("🚶                        🐢")
    await message.edit_text("🚶                         🐢")
    await message.edit_text("🚶                          🐢")
    await message.edit_text("🚶                           🐢")
    await message.edit_text("🚶                            🐢")
    await message.edit_text("🚶                             🐢")
    await message.edit_text("🚶                              🐢")
    await message.edit_text("🚶                               🐢")
    await message.edit_text("🚶                                🐢")
    await asyncio.sleep(1)
    await message.edit_text("🐢                       🚶")
    await message.edit_text("🐢                      🚶")
    await message.edit_text("🐢                     🚶")
    await message.edit_text("🐢                    🚶")
    await message.edit_text("🐢                   🚶")
    await message.edit_text("🐢                  🚶")
    await message.edit_text("🐢                 🚶")
    await message.edit_text("🐢                🚶")
    await message.edit_text("🐢               🚶")
    await message.edit_text("🐢              🚶")
    await message.edit_text("🐢             🚶")
    await message.edit_text("🐢            🚶")
    await message.edit_text("🐢           🚶")
    await message.edit_text("🐢          🚶")
    await message.edit_text("🐢         🚶")
    await message.edit_text("🐢        🚶")
    await message.edit_text("🐢       🚶")
    await message.edit_text("🐢      🚶")
    await message.edit_text("🐢     🚶")
    await message.edit_text("🐢    🚶")
    await message.edit_text("🐢   🚶")
    await message.edit_text("🐢  🚶")
    await message.edit_text("🐢 🚶")
    await message.edit_text("🐢🚶")
    await asyncio.sleep(1)
    await message.edit_text("🚶🐢")
    await message.edit_text("🚶 🐢")
    await message.edit_text("🚶  🐢")
    await message.edit_text("🚶   🐢")
    await message.edit_text("🚶    🐢")
    await message.edit_text("🚶     🐢")
    await message.edit_text("🚶      🐢")
    await message.edit_text("🚶       🐢")
    await message.edit_text("🚶        🐢")
    await message.edit_text("🚶         🐢")
    await message.edit_text("🚶          🐢")
    await message.edit_text("🚶           🐢")
    await message.edit_text("🚶            🐢")
    await message.edit_text("🚶             🐢")
    await message.edit_text("🚶              🐢")
    await message.edit_text("🚶               🐢")
    await message.edit_text("🚶                🐢")
    await message.edit_text("🚶                 🐢")
    await message.edit_text("🚶                  🐢")
    await message.edit_text("🚶                   🐢")
    await message.edit_text("🚶                    🐢")
    await message.edit_text("🚶                     🐢")
    await message.edit_text("🚶                      🐢")
    await message.edit_text("🚶                       🐢")
    await message.edit_text("🚶                        🐢")
    await message.edit_text("🚶                         🐢")
    await message.edit_text("🚶                          🐢")
    await message.edit_text("🚶                           🐢")
    await message.edit_text("🚶                            🐢")
    await message.edit_text("🚶                             🐢")
    await message.edit_text("🚶                              🐢")
    await message.edit_text("🚶                               🐢")
    await message.edit_text("🚶                                🐢")
    await message.edit_text("`GABUT`")
    
# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command(["طياره", "طير"], ".") & filters.me)
async def tyara(client: Client, message: Message):
    await message.edit_text("✈-------------")
    asyncio.sleep(1)
    await message.edit_text("-✈------------")
    asyncio.sleep(1)
    await message.edit_text("--✈-----------")
    asyncio.sleep(1)
    await message.edit_text("---✈----------")
    asyncio.sleep(1)
    await message.edit_text("----✈---------")
    asyncio.sleep(1)
    await message.edit_text("-----✈--------")
    asyncio.sleep(1)
    await message.edit_text("------✈-------")
    asyncio.sleep(1)
    await message.edit_text("-------✈------")
    asyncio.sleep(1)
    await message.edit_text("--------✈-----")
    asyncio.sleep(1)
    await message.edit_text("---------✈----")
    asyncio.sleep(1)
    await message.edit_text("----------✈---")
    asyncio.sleep(1)
    await message.edit_text("-----------✈--")
    asyncio.sleep(1)
    await message.edit_text("------------✈-")
    asyncio.sleep(1)
    await message.edit_text("-------------✈")
    
# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command(["مرتبطين", "كبلز"], ".") & filters.me)
async def zeyenk(client: Client, message: Message):
    await message.edit_text("💝💘💓💗")
    asyncio.sleep(2)
    await message.edit_text("💞💕💗💘")
    asyncio.sleep(2)
    await message.edit_text("💝💘💓💗")
    asyncio.sleep(2)
    await message.edit_text("💞💕💗💘")
    asyncio.sleep(2)
    await message.edit_text("💘💞💗💕")
    asyncio.sleep(2)
    await message.edit_text("💘💞💕💗")
    asyncio.sleep(2)
    await message.edit_text("LOVE YOU 💝💖💘")
    asyncio.sleep(2)
    await message.edit_text("💝💘💓💗")
    asyncio.sleep(2)                   
    await message.edit_text("💞💕💗💘")
    asyncio.sleep(2)
    await message.edit_text("💘💞💕💗")
    asyncio.sleep(2)
    await message.edit_text("LOVE")
    asyncio.sleep(2)
    await message.edit_text("YOU")
    asyncio.sleep(2)
    await message.edit_text("FOREVER 💕")
    asyncio.sleep(2)
    await message.edit_text("💘💘💘💘")
    asyncio.sleep(2)
    await message.edit_text("LOVE")
    asyncio.sleep(2)
    await message.edit_text("I")
    asyncio.sleep(2)
    await message.edit_text("LOVE")
    asyncio.sleep(2)
    await message.edit_text("BABY")
    asyncio.sleep(2)
    await message.edit_text("I LOVE YOUUUU")
    asyncio.sleep(2)
    await message.edit_text("MY BABY")
    asyncio.sleep(2)
    await message.edit_text("💕💞💘💝")
    asyncio.sleep(2)
    await message.edit_text("💘💕💞💝")
    asyncio.sleep(2)
    await message.edit_text("LOVE YOU 💞")

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قنبلة", ".") & filters.me)
async def gahite(client: Client, message: Message):
    if message.forward_from:
        return
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await message.edit("`BOOOOOOOM......`")
    await asyncio.sleep(2)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command(["كابوس", "سورس كابوس", "السورس"], ".") & filters.me)
async def gajjajay(client: Client, message: Message):
    await message.edit("هلو")
    await asyncio.sleep(0.3)
    await message.edit("هنا")
    await asyncio.sleep(0.2)
    await message.edit("هتشوف الجمدان كلو")
    await asyncio.sleep(0.5)
    await message.edit("كابوس بتعمل عظمه ")
    await asyncio.sleep(0.2)
    await message.edit("فوق")
    await asyncio.sleep(0.3)
    await message.edit("اي حد")
    await asyncio.sleep(0.3)
    await message.edit("🔥🔥🔥")
    await asyncio.sleep(0.3)
    await message.edit("هلو هنا هتشوف الجمدان كلو كابوس بتعمل عظمه فوق اي حد 🔥🔥🔥")

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قمور$", prefixes=f".") & filters.me)
async def qmor_1(c, msg):
    animation_interval = 0.2
    animation_ttl = range(96)
    await msg.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 32])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قناص", ".") & filters.me)
async def knasas(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉\n" r"_/﹋\_" "\n اثبت محلك ؟! انت مفكرها زريبه ولا اي ي كابتن اثبت مكانك واقلع هدومك 🧐😂 ??!",
    ]
    if message.forward_from:
        return
    await message.edit("جآري تثبيت الضحيه ...")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])


# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("انتحر", ".") & filters.me)
async def anthar(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
         "`كتفم حياتي اه😂...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    ]
    if message.forward_from:
        return
    await message.edit("خلآص زهقتت من حيآتي جآري الانتحارر ...")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("اجري", ".") & filters.me)
async def agryy(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`اوعييي..`",
    ]
    if message.forward_from:
        return
    await message.edit("يلآ انا هجري الي يحصلني يكسرني 🧐😂 ...")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("لايك", ".") & filters.me)
async def likenice(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
         "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    ]
    if message.forward_from:
        return
    await message.edit("جآري رزع افخم لآيك ع الابب يرحقلبي 💋❤ ...")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("دبابه", ".") & filters.me)
async def dbabaa(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ 💣💣\n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤☃️\n",
    ]
    if message.forward_from:
        return
    await message.edit("وسع يعم هدوسسك بالدبابه بتعتي 🤫😂 ...")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("خنزير", ".") & filters.me)
async def hanzer(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok    ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈️\n",
    ]
    if message.forward_from:
        return
    await message.edit("يلآ هطبخلك خنزير ع العشا انهارده 😎😂")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])
# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("كلب", ".") & filters.me)
async def klbklab(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
                "╥━━━━━━━━╭━━╮━━┳\n"
                "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣️\n"
                "╨━━┗┛┗┛━━┗┛┗┛━━┻\n",
    ]
    if message.forward_from:
        return
    await message.edit("خد يرحقلبي آفخم كلب بيتبول ليك - 🐕")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == =

@Client.on_message(filters.command("مدينة", ".") & filters.me)
async def madina(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
                "☁️☁️☁️🌞      ☁️     ☁️  ☁️ ☁️"
                "☁️ ☁️  ✈️    ☁️    🚁    ☁️    ☁️"
                "☁️  ☁️    ☁️       ☁️     ☁️   ☁️ ☁️"
                "  🏬🏨🏫🏢🏤🏥🏦🏪🏫"
                " 🌲/        l🚍   \🌳👭"
                "🌳/   🚘    l 🏃   \🌴 👬"
            "👬🌴/           l  🚔   \🌲"
             "🌲/   🚖       l         \ "
            "🌳/🚶           |   🚍     \ 🌴🚴🚴"
           "🌴/               |            \🌲",
    ]
    if message.forward_from:
        return
    await message.edit("جآري انشاء مدينتك يرحقلبي - 🏯")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])



@Client.on_message(filters.command("سبونج", ".") & filters.me)
async def sbong(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
                "┈┈ ╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
                "┈╱╭▏╮╭┻┻╮╭┻┻╮ ╭▏ \n"
                "▕╮╰▏╯┃╭╮┃┃╭╮┃ ╰▏ \n"
                "▕╯┈▏┈┗┻┻┛┗┻┻┻╮ ▏ \n"
                "▕╭╮▏╮┈┈┈┈┏━━━╯ ▏\n"
                "▕╰╯▏╯╰┳┳┳┳┳┳╯ ╭▏ \n"
                "▕┈╭▏╭╮┃┗┛┗┛┃┈ ╰▏ \n"
                "▕┈╰▏╰╯╰━━━━╯┈┈ ▏I'm سبـونـج بــوب\n",
    ]
    if message.forward_from:
        return
    await message.edit("آنا سبونج بوب هوب لوب اصفر كموني 🤗😂")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])



@Client.on_message(filters.command("صدمه", ".") & filters.me)
async def sadma(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
                "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
                 "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
                 "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
                  "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
                  "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
                  "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
                  "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
                  "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                  "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                  "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
                  "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
                  "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
                 "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
                "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n",
    ]
    if message.forward_from:
        return
    await message.edit("جآري انشاء صدمتك - 😱")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])



@Client.on_message(filters.command("فيل", ".") & filters.me)
async def fela(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(6)
    animation_chars = [
               "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
               "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
               "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
               "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
              "╭▏┈┈┈┈┈┈┈▏╲▂▂ ╱┈\n"
              "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
              "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
               "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈ν2.ο\n",
    ]
    if message.forward_from:
        return
    await message.edit("وسسع يعم الفيل القمدد بتعي جآآي - 🐘")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])       
        
                 
# Copyright (C) 2021 JepThon TEAM
# FILES WRITTEN BY  @lMl10l

import asyncio
from telethon import events
from jepthon import jepiq
import random
from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from . import ALIVE_NAME

plugin_category = "fun"


@Client.on_message(filters.command("تهكير$", ".") & filters.me)
async def fela(client: Client, message: Message):=("تهكير", plugin_category),
    info={
        "header": "Fun hack animation.",
        "description": "Reply to user to show hack animation",
        "note": "This is just for fun. Not real hacking.",
        "usage": "{tr}hack",
    },
)
async def _(event):
    "Fun hack animation."
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        idd = reply_message.sender_id
        if idd == 705475246:
            await edit_or_reply(
                event, "**᯽︙ عـذرا لا استـطيع اخـتراق مـطوري اعـتذر او سيقـوم بتهـكيرك**"
            )
        else:
            event = await edit_or_reply(event, "يتـم الاختـراق ..")
            animation_chars = [
                "᯽︙ تـم الربـط بسـيرفرات الـتهكير الخـاصة",
                "تـم تحـديد الضحـية",
                "**تهكيـر**... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "**تهكيـر**... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "**تهكيـر**... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "**تهكيـر**... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "**تهكيـر**... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "**تهكيـر**... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "**تهكيـر**... 84%\n█████████████████████▒▒▒▒ ",
                "**تهكيـر**... 100%\n████████████████████████ ",
                f"᯽︙ ** تـم اخـتراق الضـحية**..\n\nقـم بالـدفع الى {USER_NAME} لعـدم نشـر معلوماتك وصـورك",
            ]
            animation_interval = 3
            animation_ttl = range(11)
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await event.edit(animation_chars[i % 11])
    else:
        await edit_or_reply(
            event,
            "᯽︙ لم يتـم التعـرف على المستـخدم",
            parse_mode=_format.parse_pre,
        )
@jepiq.ar_cmd(
    pattern="تهكير2$",
    command=("تهكير2", plugin_category),
    info={
        "header": "Fun hack animation.",
        "description": "Reply to user to show hack animation",
        "note": "This is just for fun. Not real hacking.",
        "usage": "{tr}hack",
    },
)
async def _(event):
    if event.fwd_from:
        return

    animation_interval = 3

    animation_ttl = range(11)

    
    await event.edit("**جارِ الاختراق الضحية..**")

    animation_chars = [
        
            "**جار تحديد الضحية...**",
            "**تم تحديد الضحية بنجاح ✓**",
            "`يتم الاختراق... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`يتم الاختراق... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`يتم الاختراق... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`يتم الاختراق... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`يتم الاختراق... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`يتم الاختراق... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`يتم الاختراق... 84%\n█████████████████████▒▒▒▒ `",
            "`يتم الاختراق... 100%\n████████████████████████ `",
            "` تم رفع معلومات الشخص...\n\nسيتم ربط المعلومات بسيرفرات التهكير الخاصه..`"
        ]
  
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
# Made for Hussein
        await event.edit(animation_chars[i % 11])

    await asyncio.sleep(2)

    animation_interval = 1
    animation_ttl = range(0,14)
    await event.edit("**يتم الاتصال لسحب التوكن الخاص به عبر موقع.telegram.org**")
    await asyncio.sleep(1)
    animation_chars = [
           "root@anon:~# ls\n\n  usr  ghost  codes  \n\nroot@aono:~# # So Let's Hack it ...\nroot@anon:~# touch setup.py\n\nsetup.py deployed ...\nيتم الان الرفع عبر CMD تلقائياً ...\n\nroot@anon:~# trap whoami\n\nwhoami=user\nboost_trap on force ...\nvictim detected  in ghost ...\n\nتم اكتمال العملية ✓!\nيتم الان استخراج توكن الضحية!\nToken=`DJ65gulO90P90nlkm65dRfc8I`",
         ]
            

    for i in animation_ttl:
# Made for Hussein        
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])
    
    await asyncio.sleep(2)

    await event.edit("`starting telegram hack`")
    await asyncio.sleep(2)
    await event.edit("`يتم سحب الصور والمعلومات...\n 88%completed\nall data from telegram private server downloaded\nterminal download sucessfull--with status jh3233fdg66y yr4vv.irh\n data collected from tg-bot\nTERMINAL:\n Bruteforce-Telegram-0.1.tar.gz (1.3)downloaded`")
    await asyncio.sleep(5)
    await event.edit("`100%\n█████████████████████████ `\n\n\n  TERMINAL:\nيتم تنزيل Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  يتم تنزيل Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: `")
    await asyncio.sleep(5)
    await event.edit(f"`تم سحب جميع معلومات الحساب\n قم بلدفع الى {ALIVE_NAME} 100$ \n حتى لا يقم بنشر صورك ومحادثاتك !`")
    await asyncio.sleep(5)
    h=(random.randrange(1,5)) 
    if h==1:
        await event.edit("`تم رفع جميع الصور المخزونة والمحادثات وجهات اتصال المستخدم عبر مجلد pdf \n\n😂 لا تقلق انا فقط من ارئ معلوماتك 😎😎.. اذا لم تصدق ادخل الى هذا الرابط وانظر بنفسك` 🙂\n\nhttps://drive.google.com/file/d/1EHJSkt64RZEw7a2h8xkRqZSv_4dWhB02/view?usp=sharing")
    if h==2:
        await event.edit("`تم رفع جميع الصور المخزونة والمحادثات وجهات اتصال المستخدم عبر مجلد pdf \n\n😂 لا تقلق انا فقط من ارئ معلوماتك 😎😎.. اذا لم تصدق ادخل الى هذا الرابط وانظر بنفسك` 🙂\n\nhttps://drive.google.com/file/d/1YaUfNVrHU7zSolTuFN3HyHJuTWQtdL2r/view?usp=sharing")
    if h==3:
        await event.edit("`تم رفع جميع الصور المخزونة والمحادثات وجهات اتصال المستخدم عبر مجلد pdf \n\n😂 لا تقلق انا فقط من ارئ معلوماتك 😎😎.. اذا لم تصدق ادخل الى هذا الرابط وانظر بنفسك` 🙂\n\nhttps://drive.google.com/file/d/1o2wXirqy1RZqnUMgsoM8qX4j4iyse26X/view?usp=sharing")
    if h==4:
        await event.edit("`تم رفع جميع الصور المخزونة والمحادثات وجهات اتصال المستخدم عبر مجلد pdf \n\n😂 لا تقلق انا فقط من ارئ معلوماتك 😎😎.. اذا لم تصدق ادخل الى هذا الرابط وانظر بنفسك` 🙂\n\nhttps://drive.google.com/file/d/15-zZVyEkCFA14mFfD-2DKN-by1YOWf49/view?usp=sharing")
    if h==5:
        await event.edit("`تم رفع جميع الصور المخزونة والمحادثات وجهات اتصال المستخدم عبر مجلد pdf \n\n😂 لا تقلق انا فقط من ارئ معلوماتك 😎😎.. اذا لم تصدق ادخل الى هذا الرابط وانظر بنفسك` 🙂\n\nhttps://drive.google.com/file/d/1hPUfr27UtU0XjtC20lXjY9G3D9jR5imj/view?usp=sharing")
