import discord, time, random
from colored import fg, attr

async def Crush(ctx, add):

    if "add" in add:
        name = ""
        for word in add:
            if word != "add":
                name += word
                name += " "
        if name == "":
            deleteMessage = await ctx.reply(
                "Veuillez choisir un nom à ajouter à la commande !\nc!crush add **nom** <-- ICI")
            await deleteMessage.delete(delay=15)

        else:
            addedName = open("assets/texts/crush_names.txtes.txt", mode="a")
            addedName.write(f"\n{name}")
            addedName.close()
            print(f"%s{ctx.author} a jouté {name} a la liste des crush.%s" % (fg(20), attr(1)))
            embed = discord.Embed(title="**just Hervey 💎 || Crush Add**",
                                description=f"__{ctx.author.mention} a ajouté {name} à la liste des crush__.",
                                color=0x461b30)
            embed.set_footer(text="Nottez bien que si le nom n'est pas approuvé, il pourra être supprimé.")
            await ctx.send(embed=embed)

    else:

        name = "error"
        if "+" in add:
            name = ""
            name_2 = ""
            conti = False
            for word in add:
                if word != "+" and not conti:
                    name += word
                    name += " "
                elif conti:
                    name_2 += word
                    name += " "
                elif word == "+":
                    conti = True

            name_2 = name_2.replace("+", "")
            await ctx.reply(f"Chargement de l'amour de **{name}** +  **{name_2}**...")
            time.sleep(1.5)
            percent = random.randint(0, 100)
            await ctx.reply(f"Résultat : **{name}** +  **{name_2}** = {percent}% d'amour.")

        else:
            if add != "add":

                _ameSoeur = None
                name = ""
                for word in add:
                    name += word
                    name += " "

                if not add:
                    name = ctx.author.mention

            names = [word.strip() for word in open("assets/texts/crush_names.txtes.txt")]
            await ctx.reply(f"Chargement de l'âme soeur de **{name}**...")
            time.sleep(1.5)
            _ameSoeur = random.choice(names)
            percent = random.randint(0, 100)
            await ctx.reply(
                f"L'âme soeur de **{name}** est **{_ameSoeur}** !\n**{name}**+ **{_ameSoeur}** = **{percent}% d'amour**.")
