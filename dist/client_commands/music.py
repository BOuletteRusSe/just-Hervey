import random


async def Music(ctx):
    urls = [word.strip() for word in open("links.bdd", encoding="utf-8")]
    url = random.choice(urls)
    await ctx.reply(url)
