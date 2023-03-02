
import random

async def Drug(ctx):
    

    ls = [word.strip() for word in open("assets/texts/boule.txt", encoding="utf-8")]
    
    await ctx.reply(random.choice(ls))
