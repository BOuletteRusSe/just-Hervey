import random


async def Ping(ctx):
    id = random.randint(100000000000000000, 999999999999999999)
    await ctx.reply(f"<@{id}>")