import discord, asyncio
from random import choice

async def ChangeActivity(c):
    while True:
        try: 
            # await c.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=str(choice([word.strip() for word in open("assets/texts/boule.txt", encoding="utf-8")]))))
            await c.bot.change_presence(activity=discord.Streaming(name="24/24 in comming, servers soon !", url='https://www.twitch.tv/sardoche'))
        except: 
            pass
        await asyncio.sleep(20)
