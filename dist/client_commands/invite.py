import random, string


async def Invite(ctx):
    url = "https://discord.gg/"
    for i in range(8):
        url += random.choice(string.ascii_letters + string.digits)
    await ctx.reply(url)
