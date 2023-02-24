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
                await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")
            else:
                
                def InitEmbed(page):
                    
                    minerals_embed = discord.Embed(title="💎 STATS 💎 | Page %s" % (page + 1), description="Pour naviguer à travers les pages vous pouvez cliquer sur les flèches en dessous du message.", color=0x2C2CD6)
                    minerals_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

                    locked = 0
                    
                    for m, s in minerals.items():
                        proba = False
                        for e, v in s.items():
                            if e == "Emoji": emoji = v
                            if e == "Proba": 
                                proba = f"Probabilité d'obtention : **{v}**%"
                            if e == "Id": __id__ = v
                            if e == "Price": price = v
                            
                        if data[id]["Inventory"][m] > 0:
                            if not proba:
                                proba = f"Probabilité d'obtention : Non définie"
                            if page == 0 and __id__ <= 15:
                                minerals_embed.add_field(name=f"Id: {__id__} | {emoji} • {m}", value=f"Prix de revente : **{price}€**\n{proba}", inline=True)
                            elif page == 1 and 10 < __id__ <= 30:
                                minerals_embed.add_field(name=f"Id: {__id__} | {emoji} • {m}", value=f"Prix de revente : **{price}€**\n{proba}", inline=True)
                            elif page == 2 and 30 < __id__ <= 45:
                                minerals_embed.add_field(name=f"Id: {__id__} | {emoji} • {m}", value=f"Prix de revente : **{price}€**\n{proba}", inline=True)
                        else:
                            locked += 1
                                
                    minerals_embed.set_footer(text=f"Matériaux restants à débloquer : {locked}")
                            
                    return minerals_embed
                
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

                
