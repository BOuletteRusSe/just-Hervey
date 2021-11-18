import random


async def Music(ctx):
    urls = [word.strip() for word in open("assets/texts/links.txt", encoding="utf-8")]
    url = random.choice(urls)
    await ctx.reply(url)
