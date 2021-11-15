import discord, random
from colored import fg, attr


async def Boule(ctx, arg):

    if "add" in arg:
        content = ""
        for word in arg:
            if word != "add":
                content += word
                content += " "
        if content == "":
            deleteMessage = await ctx.reply(
                "Veuillez choisir un contenue à ajouter à la commande !\nc!boule add **contenue** <-- ICI")
            await deleteMessage.delete(delay=15)

        else:
            with open("boule.txt", "a", encoding="utf-8") as b: b.write(f"\n{content}")
            with open("boule.txt", "r", encoding="utf-8") as b: 
                with open("bouliste.txt", "w", encoding="utf-8") as bl: bl.write(b.read().replace(" ", "\n"))
            embed = discord.Embed(title="**just Hervey 💎 || Boule Add**",
                                description=f"__{content} a été ajouté entre les boules de {ctx.author.mention}__.",
                                color=0x461b30)
            embed.set_footer(text="La commande c!boule n'est pas modérée lol.")
            await ctx.send(embed=embed)

    else:
        boules = [word.strip() for word in open("boule.txt", encoding="utf-8")]
        boule_ = random.choice(boules)
        await ctx.reply(f"{boule_}")
