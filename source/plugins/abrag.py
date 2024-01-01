from pyrogram import Client, filters, enums
from config import *
import asyncio
import string_utils
import time
import csv
import json

@Client.on_message(filters.command(["ابراج$","الابراج$"],prefixes=f".") & filters.me )
async def commands(c,msg):
  try :
    result = await c.get_inline_bot_results(bot_user,query="الابراج")
    await msg.delete()
    await c.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  except :
    await msg.edit("• فعل الانلاين من @botFather")