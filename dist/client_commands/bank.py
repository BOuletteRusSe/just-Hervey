import json, discord


async def Bank(ctx, pos):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    c = True
    id = str(ctx.author.id)

    for key in data.keys():
        if key == id:
            c = False

    if c:
        embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)

    elif "pos" in pos:
        try:
            p = pos[1]
            p = int(p)

            if p <= 0:
                await ctx.reply("Vous ne pouvez pas faire ça !")

            elif data[id]['Money'] - p < 0:
                await ctx.reply(f"Vous n'avez pas assez d'argent !\nArgent : **{data[id]['Money']}**")

            else:
                data[id]['Money'] -= p
                data[id]['Bank'] += p
                data[id]['Bank'] = round(data[id]['Bank'])
                data[id]['Money'] = round(data[id]['Money'])
                with open("assets/player_data.json", 'w') as d:
                    json.dump(data, d, indent=4)

                money_embed = discord.Embed(title="Transaction effectué avec succès !", color=0x5455b0)
                money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                await ctx.reply(embed=money_embed)

        except:
            deleted_message = await ctx.reply("Veuillez choisir une valeur correcte || c!bank pos **valeur**")
            await deleted_message.delete(delay=15)

    elif "get" in pos:
        try:
            p = pos[1]
            p = float(p)

            if p <= 0:
                await ctx.reply("Vous ne pouvez pas faire ça !")

            elif data[id]['Bank'] - p < 0:
                await ctx.reply(f"Vous n'avez pas assez d'argent en banque !\nArgent en banque : **{data[id]['Bank']}**")

            else:
                data[id]['Bank'] -= p
                data[id]['Money'] += p
                data[id]['Bank'] = round(data[id]['Bank'])
                data[id]['Money'] = round(data[id]['Money'])
                with open("assets/player_data.json", 'w') as d:
                    json.dump(data, d, indent=4)

                money_embed = discord.Embed(title="Transaction effectué avec succès !", color=0x5455b0)
                money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                await ctx.reply(embed=money_embed)

        except:
            deleted_message = await ctx.reply("Veuillez choisir une valeur correcte || c!bank get **valeur**")
            await deleted_message.delete(delay=15)

    else:
        bank_embed = discord.Embed(title="just Hervey 💎 | 💱 BANQUE 💱", description="Bienvenue dans la banque. Ici vous pouvez déposer de l'argent afin de le retirer plus tard.\n\n```c!bank pos <montant>```  Permet de déposer de l'argent en banque.\n```c!bank get <montant>```  Permet de retirer de l'argent de la banque.", color=0x278B4D)
        bank_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        bank_embed.add_field(name="", value="", inline=False)
        bank_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
        bank_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
        bank_embed.set_footer(text="Dans de futures mises à jour, la banque vous permettera de gagner des intérêts sur votre argent !")
        await ctx.send(embed=bank_embed)