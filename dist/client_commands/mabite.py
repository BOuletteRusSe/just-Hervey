import discord, random


async def MaBite(ctx, arg):
    
    if "add" in arg:
        content = ""
        for word in arg:
            if word != "add":
                content += word
                content += " "
        if content == "":
            deleteMessage = await ctx.reply("Veuillez choisir une énigme à ajouter à la commande !\nc!mabite add **énigme** <-- ICI")
            await deleteMessage.delete(delay=15)

        else:
            with open("assets/texts/cmabite.txt", "a", encoding="utf-8") as b: b.write(f"\n{content}")
            embed = discord.Embed(title="**just Hervey 💎 || Énigmes du Père Fouras**", description=f"Une nouvelle énigme a été ajoutée ! {content}. Qui suis-je ? C'EST MA BITE !", color=0xE17CBB)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_footer(text="Ajoutes des trucs drôles zebi.")
            await ctx.send(embed=embed)

    else:
        enigmes = [word.strip() for word in open("assets/texts/cmabite.txt", encoding="utf-8")]
        enigme = random.choice(enigmes)
        pere_fouras = random.choice([word.strip() for word in open("assets/texts/pere_fouras.txt", encoding="utf-8")])
        embed = discord.Embed(title=f"[A lire avec la voix du père fouras] **{enigme}. Qui suis-je ?**", description=f"Réponse : ||C'EST MA BITE !||", color=0x960F9B)
        embed.set_image(url=pere_fouras)
        embed.set_footer(text="Le père fouras t'as bien eu lol!")
        await ctx.reply(embed=embed)

