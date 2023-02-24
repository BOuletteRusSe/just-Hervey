from assets.minerals_data import minerals
import json, discord, random


async def Sell(ctx, arg):
    
    with open("assets/player_data.json") as data:
        data = json.load(data)
            
    id = str(ctx.author.id)
    c = True

    for key in data.keys():
        if key == id:
            c = False

    if c:
        await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")
    else:
        
        try:
            n = int(arg[0])
            __m__ = int(arg[1])
        except:
            sell_embed = discord.Embed(title="just Hervey 💎 | ⛲ VENTE ⛲", description="Bienvenue sur le lieu de vente. Pour vendre des matérieaux veuillez éxécuter la commande `c!sell <montant à vendre> <id du minéral>`.\nEx pour vendre 10 de pierre: `c!sell 10 0`\nPour afficher les ids et les prix de revente des minéraux tapez la commande `c!minerals stats`.", color=0xC7D62C)
            sell_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            sell_embed.add_field(name="", value="", inline=False)
            sell_embed.add_field(name="💵 • Argent :", value=data[id]["Money"], inline=False)
            await ctx.send(embed=sell_embed)
        else:
            
            err = True
            
            for m, s in minerals.items():
                for g, v in s.items():
                    if g == "Id": __id__ = v
                    if g == "Price": price = v
                    if g == "Emoji": emoji = v
                    if g == 'Color': __color__ = v
                    
                if __m__ == __id__:
                    if data[id]["Inventory"][m] <= n:
                        await ctx.reply(f"Vous n'avez pas assez de {m} pour pouvoir en vendre {n} !")
                    else:
                        try: 
                            price = int(price)
                        except:
                            price = random.randint(price[0], price[1]) / 2

                        data[id]["Inventory"][m] -= n
                        data[id]["Money"] += price
                        
                        with open("assets/player_data.json", 'w') as d:
                            json.dump(data, d, indent=4)
                        
                        embed = discord.Embed(title=f"{emoji} • Vente de **{n} {m}** effectuée avec succès !", description=f"**{data[id]['Inventory'][m]}** {m} restant.", color=__color__)
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        embed.add_field(name="Argent :", value=data[id]["Money"], inline=True)
                        embed.add_field(name="Argent gagné :", value=f"{price}€", inline=True)
                        embed.add_field(name="Argent en banque :", value=data[id]["Bank"], inline=True)
                        await ctx.send(embed=embed)
                        err = False
            
            if err:         
                await ctx.reply('Un problème est survenu, vérifier si vous avez bien ortographée la commande !')

            
