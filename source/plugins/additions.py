from pyrogram import Client, filters,enums
from config import *
import asyncio
from autoname import main as name
import string_utils
import time
import csv
import json

@Client.on_message(filters.command("مسح جهاتي$",prefixes=f".") & filters.me )
async def my_con(c,msg):
  list_c = await c.get_contacts()
  ids = []
  for contact in list_c :
     ids.append(contact.id)
  await c.delete_contacts(ids)
  await msg.edit(f"• تم مسح {len(ids)} من جهاتك")
      

@Client.on_message(filters.command("جلب الاعضاء$",prefixes=f".") & filters.me )
async def get_members(c,msg):
  with open("members.txt","w") as f:
    ids = ""
    async for m in c.get_chat_members(msg.chat.id):
      ids += f"{m.user.id}\n"
    f.write(ids)
  await msg.reply_document(f"./members.txt")
  

@Client.on_message(filters.command("قلب$",prefixes=f".") & filters.me )
async def haert(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("❤💙💚💛🧡💜🖤🤍🤎❤️‍"))
    time.sleep(0.5)

@Client.on_message(filters.command("قلوب$",prefixes=f".") & filters.me )
async def haerts(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤️‍"))
    time.sleep(0.5)

@Client.on_message(filters.command(["قمر$","اقمار$"],prefixes=f".") & filters.me )
async def moon(c,msg):
  listt = ["🌑🌒🌓🌔🌕🌖🌗🌘","🌒🌓🌔🌕🌖🌗🌘🌑","🌓🌔🌕🌖🌗🌘🌑🌒","🌔🌕🌖🌗🌘🌑🌒🌓","🌕🌖🌗🌘🌑🌒🌓🌔","🌖🌗🌘🌑🌒🌓🌔🌕","🌗🌘🌑🌒🌓🌔🌕🌖","🌘🌑🌒🌓🌔🌕🌖🌗","🌑🌒🌓🌔🌕🌖🌗🌘"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command("مسح الروابط$",prefixes=f".") & filters.me & filters.group)
async def del_urls(c,msg):
  await msg.reply("• جاري جلب الروابط ..")
  num = 0
  async for message in c.search_messages(msg.chat.id, filter=enums.MessagesFilter.URL):
    try :
      await message.delete(revoke=True)
      num += 1
    except : 
      pass
  await msg.edit(f"• تم مسح {num} رساله تحتوي علي روابط")
@Client.on_message(filters.command(["الاوامر$","اوامر$"],prefixes=f".") & filters.me )
async def commands(c,msg):
  try :
    result = await c.get_inline_bot_results(bot_user,query="الاوامر")
    await msg.delete()
    await c.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  except :
    await msg.edit("• فعل الانلاين من @botFather")


@Client.on_message(filters.command(["سورس$","السورس$"],prefixes=f".") & filters.me )
async def source(c,msg):
  await msg.edit("• [☆ - • 𝚂𝙾𝚄𝚁𝙲𝙴 ¦ ✨](https://t.me/Tepthon)\n• [☆ - 𓆩˹𓏺َِTaleb مُحمـد ٍٍٍٍٍٍّّّّّّّ ¦ ✨](https://t.me/A_D_P)\n• [☆ -  ¦ 🔥](https://t.me/Tepthon)")
  

@Client.on_message(filters.command("مسح الصور$",prefixes=f".") & filters.me & filters.group)
async def del_photos(c,msg):
  await msg.reply("• جاري جلب الصور ..")
  num = 0
  async for message in c.search_messages(msg.chat.id, filter=enums.MessagesFilter.PHOTO):
    try :
      await message.delete(revoke=True)
      num += 1
    except : 
      pass
  await msg.edit(f"• تم مسح {num} رساله تحتوي علي صور")
  
@Client.on_message(filters.command("تفعيل الترحيب$",prefixes=f".") & filters.me )
async def wel(c,msg):
  r.set(f"{sudo_id}welcome","on")
  await msg.edit("• تم تفعيل الترحيب")

@Client.on_message(filters.command("تعطيل الترحيب$",prefixes=f".") & filters.me )
async def unwel(c,msg):
  r.delete(f"{sudo_id}welcome")
  await msg.edit("• تم تعطيل الترحيب")
  

@Client.on_message(filters.command("تعطيل الساعه$",prefixes=f".") & filters.me )
async def clockk(c,msg):
  r.delete(f"{sudo_id}clockk")
  get = await c.get_chat("me")
  await c.update_profile(first_name=f'{get.last_name}' ,last_name="")
  await msg.edit("• تم تعطيل الساعه")
@Client.on_message(filters.command("تفعيل الساعه$",prefixes=f".") & filters.me )
async def unclockk(c,msg):
  get = await c.get_chat("me")
  if get.last_name:
    my_name = f"{get.first_name} {get.last_name}"
  else :
    my_name = get.first_name
  r.set(f"{sudo_id}clockk",my_name)
  await msg.edit("• تم تفعيل الساعه")
  await name()
  
@Client.on_message(filters.regex("^.تغيير اسمي (.*)") & filters.me )
async def chang_name(c,msg):
  my_name = msg.text
  my_name = my_name.replace(".تغيير اسمي","")
  r.set(f"{sudo_id}clockk",my_name)
  await msg.edit(f"• تم تغيير اسمك الي {my_name}")
  await name()
  
@Client.on_message(filters.regex("^.مسح [0-9]+$") & filters.me )
async def del_message(c,msg):
  textt = msg.text
  num = int(textt.split(" ")[1])
  list1 = []
  msg_id = msg.id
  for i in range(1,num):
    list1.append(msg_id)
    msg_id = msg_id - 1
  try :
    await c.delete_messages(msg.chat.id, list1)
  except Exception as e :
    await msg.reply(e)
    
@Client.on_message(filters.regex("^.سبام (.*?) [0-9]+$") & filters.me )
async def spam_message(c,msg):
  await msg.delete()
  textt = msg.text
  num = int(textt.split(" ")[2])
  word = textt.split(" ")[1]
  for i in range(1,num):
    await c.send_message(msg.chat.id,word)
    
@Client.on_message(filters.regex("^.بحث (.*)") & filters.me )
async def search_word(c,msg):
  textt = msg.text
  word = textt.replace(".بحث ","")
  num = 0
  async for message in c.search_messages(msg.chat.id, query=word):
    try :
      await c.send_message(msg.chat.id,".",reply_to_message_id=message.id)
      num += 1
    except : 
      pass
  await message.reply(f"• العدد {num}")
  
@Client.on_message(filters.command("مسح رسايله$",prefixes=f".") & filters.me & filters.reply )
async def dell_all_msg(c,msg):
  if msg.reply_to_message.from_user.id in sudo_command:
    return await msg.edit("• لا يمكنك استخدام الامر علي مبرمجين السورس")
  try :
    await c.delete_user_history(msg.chat.id,msg.reply_to_message.from_user.id)
    await c.send_message(msg.chat.id,"• تم مسح رسايله")
  except Exception as e:
    await msg.edit("• ليس لديك صلاحيه المسح")