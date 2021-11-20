import discord, asyncio
from random import choice

async def ChangeActivity(c):
    while True:
        try: await c.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=str(choice([word.strip() for word in open("assets/texts/boule.txt", encoding="utf-8")]))))
        except: pass
        await asyncio.sleep(10)
