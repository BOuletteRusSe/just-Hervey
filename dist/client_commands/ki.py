import random


async def Ki(ctx):

    interrogatifs = ["Qui", "Comment", "Pourquoi", "Ou", "Quand", "Quel", "Combien"]
    await ctx.reply(
        f"{random.choice(interrogatifs)} {random.choice([word.strip() for word in open('liste_francais.txt')])} {random.choice([word.strip() for word in open('liste_francais.txt')])} ?")
