from assets.minerals_data import minerals
from assets.woods_data import woods
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
        embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        
        try:
            t = str(arg[0])
        except:
            sell_embed = discord.Embed(title="just Hervey 💎 | 💰 VENTE 💰", description="Bienvenue sur le lieu de vente. Pour vendre des matérieaux veuillez éxécuter la commande `c!sell minerals/woods <montant à vendre> <id du minéral>`.\nEx pour vendre 10 de pierre: `c!sell m 10 0`\nPour afficher les ids et les prix de revente des minéraux, utilisez la commande `c!stats`.", color=0xC7D62C)
            sell_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            sell_embed.add_field(name="", value="", inline=False)
            sell_embed.add_field(name="💵 • Argent :", value=data[id]["Money"], inline=False)
            await ctx.send(embed=sell_embed)
        else:
            try:
                n = int(arg[1])
                __m__ = int(arg[2])
            except:
                if t in ["m", "minerals"]:
                    await ctx.reply("Veuillez entrer un id et un montant correct pour pouvoir vendre vos minerais !\nEx : **c!sell minerals <montant> <id>**. Pour afficher les ids et les prix de revente des minéraux, utilisez la commande **c!stats minerals**")
                elif t in ["w", "woods"]:
                    await ctx.reply("Veuillez entrer un id et un montant correct pour pouvoir vendre votre bois !\nEx : **c!sell woods <montant> <id>**. Pour afficher les ids et les prix de revente du bois, utilisez la commande **c!stats woods**")
                else:
                    await ctx.reply("Veuillez entrer un type de vente correct !\n**c!sell woods** pour vendre du bois ou **c!sell minerals** pour vendre des minerais.")
            else:
        
                if t in ["m", "minerals"]:
                
                    err = True
                    
                    for m, s in minerals.items():
                        for g, v in s.items():
                            if g == "Id": __id__ = v
                            if g == "Price": price = v
                            if g == "Emoji": emoji = v
                            if g == 'Color': __color__ = v
                            
                        if n <= 0:
                            await ctx.reply("Veuillez entrer une valeure correcte !")
                            err = False
                            break
                            
                        elif __m__ == __id__:
                            if data[id]["Inventory"][m] < n:
                                await ctx.reply(f"Vous n'avez pas assez de {m} pour pouvoir en vendre {n} !")
                            else:
                                try: 
                                    price = price * n
                                except:
                                    price = (random.randint(price[0], price[1]) / 2) * n

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
                        await ctx.reply('Un problème est survenu, vérifier si vous avez bien ortographée la commande ou que l\'id existe !')
                
                elif t in ["w", "woods"]:
                    
                    for m, s in woods.items():
                        for g, v in s.items():
                            if g == "Id": __id__ = v
                            if g == "Price": price = v
                            if g == "Emoji": emoji = v
                            if g == 'Color': __color__ = v
                            
                        if n <= 0:
                            await ctx.reply("Veuillez entrer une valeure correcte !")
                            err = False
                            break
                            
                        elif __m__ == __id__:
                            if data[id]["Inventory_2"][m] < n:
                                await ctx.reply(f"Vous n'avez pas assez de {m} pour pouvoir en vendre {n} !")
                            else:
                                try: 
                                    price = price * n
                                except:
                                    price = (random.randint(price[0], price[1]) / 2) * n

                                data[id]["Inventory_2"][m] -= n
                                data[id]["Money"] += price
                                
                                with open("assets/player_data.json", 'w') as d:
                                    json.dump(data, d, indent=4)
                                
                                embed = discord.Embed(title=f"{emoji} • Vente de **{n} {m}** effectuée avec succès !", description=f"**{data[id]['Inventory_2'][m]}** {m} restant.", color=__color__)
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                embed.add_field(name="Argent :", value=data[id]["Money"], inline=True)
                                embed.add_field(name="Argent gagné :", value=f"{price}€", inline=True)
                                embed.add_field(name="Argent en banque :", value=data[id]["Bank"], inline=True)
                                await ctx.send(embed=embed)
                                err = False
                    
                    if err:         
                        await ctx.reply('Un problème est survenu, vérifier si vous avez bien ortographée la commande ou que l\'id existe !')
                    
                else:
                    await ctx.reply("Veuillez entrer un type de vente correct !\n**c!sell woods** pour vendre du bois ou **c!sell minerals** pour vendre des minerais.")

                

