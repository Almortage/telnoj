from datetime import timezone, datetime, timedelta
from asyncio import sleep
from time import strftime
from config import *
from pyrogram.errors import FloodWait
import pytz as pytz

def zhrf_time(time):
  time = str(time)
  repl = ["𝟬","𝟭","𝟮","𝟯","𝟰","𝟱","𝟲","𝟳","𝟴","𝟵"]
  curn = ["0","1","2","3","4","5","6","7","8","9"]
  for i in range(0,10) :
    time = time.replace(curn[i],repl[i])
  return time

async def main():
   ay = None
   while r.get(f"{sudo_id}clockk") :
      tmz = pytz.timezone('Africa/Cairo')
      if r.get(f'{sudo_id}:tmz_medoo'):
          tmz = pytz.timezone(r.get(f'{sudo_id}:tmz_medoo'))
      else:
          tmz = pytz.timezone('Africa/Cairo')
      time = datetime.now(tz=tmz).strftime('%I:%M')
      my_name = r.get(f"{sudo_id}clockk")
      try:
         if ay != time:
            ay = time
            await app.update_profile(first_name=f'{zhrf_time(time)}' ,last_name=my_name)
         else:
            await sleep(0)
      except FloodWait as e:
         await sleep(e.value)
         await sleep(7)
