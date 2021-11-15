import discord, asyncio

async def ChangeActivity(c):
    while True:
        await c.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="➜ c!help pour afficher la liste des commandes."))
        await asyncio.sleep(5)
        await c.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="⇨ v %s ⇦" % (c.client_version)))
        await asyncio.sleep(5)
