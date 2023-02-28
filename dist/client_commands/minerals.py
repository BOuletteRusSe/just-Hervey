from assets.minerals_data import minerals
import discord, json, asyncio

async def Minerals(ctx, arg, cc):
    
    if "stats" in arg:

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
                
                def InitEmbed(page):
                    
                    minerals_embed = discord.Embed(title="💎 STATS 💎 | Page %s" % (page + 1), description="Pour naviguer à travers les pages vous pouvez cliquer sur les flèches en dessous du message.\nPour avoir plus d'info sur un minerais, ajouter son id après la commande. Ex: **c!minerals stats <id>**", color=0x2C2CD6)
                    minerals_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

                    locked = 0
                    
                    for m, s in minerals.items():
                        for e, v in s.items():
                            if e == "Emoji": emoji = v
                            elif e == "Id": __id__ = v
                            elif e == "Price": price = v
                            
                        if data[id]["Inventory"][m] > 0:
                            if page == 0 and __id__ <= 20:
                                minerals_embed.add_field(name=f"Id: {__id__} | {emoji} • {m} *({data[id]['Inventory'][m]})*", value=f"Prix de revente : **{price}€**", inline=True)
                            elif page == 1 and 20 < __id__ <= 40:
                                minerals_embed.add_field(name=f"Id: {__id__} | {emoji} • {m} *({data[id]['Inventory'][m]})*", value=f"Prix de revente : **{price}€**", inline=True)
                            elif page == 2 and 40 < __id__ <= 60:
                                minerals_embed.add_field(name=f"Id: {__id__} | {emoji} • {m} *({data[id]['Inventory'][m]})*", value=f"Prix de revente : **{price}€**", inline=True)
                        else:
                            locked += 1
                                
                    minerals_embed.set_footer(text=f"Matériaux restants à débloquer : {locked}")
                            
                    return minerals_embed
                
                async def CheckMineral(mid_, data):
                    
                    ms = {}
                    for m, s in minerals.items():
                        proba = "Aucune donnée"
                        __image__ = False
                        for e, v in s.items():
                            if e == "Id": __id__ = v 
                            elif e == "Proba": proba = f"{v}%"
                            elif e == "Color": __color__ = v
                            elif e == "Price": __price__ = v
                            elif e == "Rareté": __r__ = v
                            elif e == "Description": __description__ = v
                            elif e == "Image": __image__ = v
                            elif e == "Level Requierd": __level__ = v
                            elif e == "Emoji": __emoji__ = v
                        ms[__id__] = [__color__, __price__, __r__, __description__, __image__, __level__, proba, m, __emoji__]
                                
                    for k, v in ms.items():
                        if str(k) == str(mid_):
                            if data[id]["Inventory"][v[7]] > 0:
                                return v
                            else:
                                await ctx.reply("Vous n'avez pas ce minerai dans votre inventaire, vous devez en avoir un pour pouvoir l'examiner !")
                                return 0
                    return 1
                
                
                try:
                    if arg[1]:
                        vv = await CheckMineral(arg[1], data)
                        if vv == 1:
                            await ctx.reply("Veuillez saisir un id correct !\n**c!minerals stats <id>**")
                        elif vv != 0:
                            membed = discord.Embed(title=f"{vv[8]} • {vv[7]} *({data[id]['Inventory'][vv[7]]})*", description=vv[3], color=vv[0])
                            membed.set_image(url=vv[4])
                            membed.add_field(name="Rareté :", value=vv[2], inline=False)
                            membed.add_field(name="Niveau de minage requis :", value=vv[5], inline=False)
                            membed.add_field(name="Probabilité d'obtention :", value=vv[6], inline=False)
                            membed.add_field(name="Prix de revente :", value=vv[1], inline=False)
                            
                            await ctx.reply(embed=membed)
                               
                except:
            
                    max_page = 2
                    min_page = 0
                    page = min_page
                    __embed__ = InitEmbed(page)
                    mess = await ctx.reply(embed=__embed__)
                    await mess.add_reaction("⬅")
                    await mess.add_reaction("➡")
                    w = True
                    
                    while w:
                        
                        def CheckEmoji(reaction, user):
                            return ctx.message.author == user and mess.id == reaction.message.id and (str(reaction.emoji) in ["⬅", "➡"])

                        try:
                            reaction, user = await cc.bot.wait_for("reaction_add", timeout=60, check=CheckEmoji)
                        except asyncio.TimeoutError:
                            w = False
                        else:
                            if str(reaction.emoji) == "⬅":
                                if page != min_page:
                                    page -= 1               
                            elif str(reaction.emoji) == "➡":
                                if page != max_page:
                                    page += 1
                                    
                            await mess.edit(embed=InitEmbed(page))
                        
    else:
        d = await ctx.reply("Veuillez éxécuter la commande de cette façon : **c!minerals stats**")
        await d.delete(delay=15)

                
