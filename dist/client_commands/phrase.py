import random


async def Phrase(ctx):
    phrase_ = ""

    for i in range(random.randint(3, 10)):
        word = random.choice([word.strip() for word in open("liste_francais.txt")])
        phrase_ += " "
        phrase_ += word

    await ctx.reply(phrase_)
