import discord, random


async def Boule(ctx, arg):

    if "add" in arg:
        content = ""
        for word in arg:
            if word != "add":
                content += word
                content += " "
        if content == "":
            deleteMessage = await ctx.reply("Veuillez choisir un contenue à ajouter à la commande !\nc!boule add **contenue** <-- ICI")
            await deleteMessage.delete(delay=15)

        else:
            with open("assets/texts/boule.txt", "a", encoding="utf-8") as b: b.write(f"\n{content}")
            with open("assets/texts/boule.txt", "r", encoding="utf-8") as b: 
                with open("assets/texts/bouliste.txt", "w", encoding="utf-8") as bl: bl.write(b.read().replace(" ", "\n"))
            embed = discord.Embed(title="**just Hervey 💎 || Boule Add**",
                                description=f"__{content} a été ajouté entre les boules de {ctx.author.mention}__.",
                                color=0x461b30)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_footer(text="La commande c!boule n'est pas modérée lol.")
            await ctx.send(embed=embed)

    else:
        boules = [word.strip() for word in open("assets/texts/boule.txt", encoding="utf-8")]
        boule_ = random.choice(boules)
        await ctx.reply(f"{boule_}")
