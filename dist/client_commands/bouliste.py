import random


async def Bouliste(ctx):
    boule = ""
    for i in range(random.randint(3, 8)):
        boules = [word.strip() for word in open("assets/texts/bouliste.txt", encoding="utf-8")]
        boule += random.choice(boules)
        boule += " "
        
    await ctx.reply(boule)
