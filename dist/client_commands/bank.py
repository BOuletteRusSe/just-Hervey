import json, discord


async def Bank(ctx, pos):

    with open("data/player_data.json") as data:
        data = json.load(data)

    c = True
    id = str(ctx.author.id)

    for key in data.keys():
        if key == id:
            c = False

    if c:
        await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")

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
                with open("data/player_data.json", 'w') as d:
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
                with open("data/player_data.json", 'w') as d:
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
        d = await ctx.reply("**c!bank get** --> Retirer l'argent depuis la banque.\n**c!bank pos** --> Poser de l'argent en banque.")
        await d.delete(delay=15)