import discord, random


async def bronJames(ctx, arg):
    
    if "add" in arg:
        content = ""
        for word in arg:
            if word != "add":
                content += word
                content += " "
        if content == "":
            deleteMessage = await ctx.reply("Veuillez choisir une phrase à ajouter à la commande !\nc!bronjames add **phrase** <-- ICI")
            await deleteMessage.delete(delay=15)

        else:
            with open("assets/texts/bronjames.txt", "a", encoding="utf-8") as b: b.write(f"\n{content}")
            embed = discord.Embed(title="**just Hervey 💎 || LEBRON JAMES**", description=f"{content} ? Non quand même pas...", color=0xE51238)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_footer(text="Il parait que cette commande est une erreur de développement.")
            await ctx.send(embed=embed)

    else:
        lebrons = [word.strip() for word in open("assets/texts/bronjames.txt", encoding="utf-8")]
        lebron = random.choice(lebrons)
        embed = discord.Embed(title=f"**just Hervey 💎 || LEBRON JAMES**", description=f"{lebron}", color=0xA4142E)
        embed.set_footer(text="c!bronjames add pour ajouter des phrases !")
        await ctx.reply(embed=embed)

