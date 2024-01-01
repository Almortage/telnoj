from pyrogram import Client, filters
from config import app
import asyncio
#سورس القرش بيمسي - @T_3_A

@app.on_message(filters.command("ريفرسي$", prefixes=f".") & filters.me)
async def othello(app, msg):
  result = await app.get_inline_bot_results("U5iBOT", "othello")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("اكس او$", prefixes=f".") & filters.me)
async def xoxo(app, msg):
  result = await app.get_inline_bot_results("@XOOTABOT", ".")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("حجره$", prefixes=f".") & filters.me)
async def hgrh(app, msg):
  result = await app.get_inline_bot_results("U5iBOT", "حجره")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("القط المجنون$", prefixes=f".") & filters.me)
async def catc(app, msg):
  result = await app.get_inline_bot_results("gamee", "crazy Cat")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("ركل الكره$", prefixes=f".") & filters.me)
async def rclball(app, msg):
  result = await app.get_inline_bot_results("gamee", "KeepitUP")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("السمك الشائك$", prefixes=f".") & filters.me)
async def fishc(app, msg):
  result = await app.get_inline_bot_results("gamee", "Spiky Fish 3")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("كرة السله$", prefixes=f".") & filters.me)
async def balls(app, msg):
  result = await app.get_inline_bot_results("gamee", "BasketBoy")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("اطلاق النار$", prefixes=f".") & filters.me)
async def atlaq(app, msg):
  result = await app.get_inline_bot_results("gamee", "NeonBlaster")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("كرة القدم$", prefixes=f".") & filters.me)
async def footballstar(app, msg):
  result = await app.get_inline_bot_results("gamee", "Footballstar")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("موتسيكلات$", prefixes=f".") & filters.me)
async def motofx(app, msg):
  result = await app.get_inline_bot_results("gamee", "motofx")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
  
@app.on_message(filters.command("تبديل النجوم$", prefixes=f".") & filters.me)
async def switchy(app, msg):
  result = await app.get_inline_bot_results("gamee", "Switchy")
  await msg.delete()
  await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)