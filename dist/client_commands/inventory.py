import discord, json, re, asyncio
from assets.items_price import item_shop_price, item_shop_price_2, item_shop_price_3


def InventoryCheckNone(name, value, id, data, inventory_embed):
    if data[id]["Inventory"][value] != 0:
        inventory_embed.add_field(name=name, value=data[id]["Inventory"][value], inline=True)


async def CheckIfUserIsInGuild(ctx, arg):

    """
    0 --> No Problem
    1 --> La mention n'est pas dans le serveur
    2 --> Erreur lors de la mention
    """

    with open("assets/player_data.json") as data:
        data = json.load(data)

    try:
        ping = [int(s) for s in re.findall(r'\d+', str(arg[0]))]
    except:
        return 3

    if len(ping) == 1:
        cc = True
        ping_id = re.findall(r'\d+', str(arg[0]))[0]

        for key in data.keys():
            if key == ping_id:
                cc = False

        if cc:
            d = await ctx.reply(f"<@{ping_id}> n'est pas inscrit.")
            await d.delete(delay=15)
            return 4
        else:
            return 0
    else:
        return 2



async def Inventory(ctx, equip, c):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    if await CheckIfUserIsInGuild(ctx, equip) not in [0, 4]:
        id = str(ctx.author.id)
        user = ctx.author
    else:
        id = re.findall(r'\d+', str(equip[0]))[0]
        user = await c.bot.fetch_user(id)

    items = ""
    for item in data[id]["Inventory"]["P Item"]:
        items += f"{str(item_shop_price_2[item]['Name'])} ({item}) | "
        
    etabli = ""
    for item in data[id]["Inventory"]["P Forge"]:
        etabli += f"{str(item_shop_price_3[item]['Name'])} ({item}) | "
        
    alliages = ""
    for item in data[id]["Inventory"]["Alliages"]:
        alliages += f"{str(item_shop_price_2[item]['Name'])} ({item}) | "

    e_items = ""
    for item in data[id]["Inventory"]["MP"]:
        e_items += f"{str(item_shop_price_2[item]['Name'])} ({item})"

    if data[id]["Inventory"]["MP"] == []:
        e_items = "Aucun"

    ranks = ""
    for rank in data[id]["Inventory"]["P Rank"]:
        ranks += f"{str(item_shop_price[rank]['Name'])} ({rank}) | "
    
    def DefaultEmbed(page):
        inventory_embed = discord.Embed(title="⚔ INVENTAIRE ⚔ | Page %s" % (page + 1), description="Ici, vous pouvez voir tout ce que vous avez a disposition dans votre inventaire. Vous pouvez faire défiler les pages avec les flèches en bas du message.", color=0x1e4843)
        inventory_embed.set_author(name=user, icon_url=user.avatar_url)
        inventory_embed.add_field(name="🛠 • Objet(s) Équipé(s) :", value=e_items)
        inventory_embed.add_field(name="🎭 • Grade :", value=item_shop_price[data[id]["Inventory"]["Rank"]]["Name"], inline=True)
        inventory_embed.add_field(name=":nut_and_bolt: • Points de Forge :", value=data[id]["Forge Points"], inline=True)
        inventory_embed.add_field(name="Liste des Objets :", value=items, inline=True)
        inventory_embed.add_field(name="Liste des Grades :", value=ranks, inline=True)
        inventory_embed.add_field(name="Liste des Aliages :", value=alliages, inline=True)
        inventory_embed.add_field(name="🔧 • Établi", value=etabli, inline=True)
        inventory_embed.add_field(name="🎟 • Tickets :", value=data[id]["Ticket"], inline=True)
        inventory_embed.add_field(name=":pick: • Nombre de Pioches Max :", value=data[id]['Inventory']['Item Limit'], inline=True)
        inventory_embed.set_footer(text=f"c!inventory equip item/rank 'nombre' pour équiper une objet ou un grade. (Vous pouvez équiper jusqu'à {data[id]['Inventory']['Item Limit']} item(s) à la fois.)")
        
        if page == 0:
            InventoryCheckNone("<:debrit:882240995717156874> • Debrit :", "Debrit", id, data, inventory_embed)
            InventoryCheckNone("<:stone:882241850965118978> • Pierre :", "Stone", id, data, inventory_embed)
            InventoryCheckNone("<:iron:881949148876783646> • Fer :", "Iron", id, data, inventory_embed)
            InventoryCheckNone("<:silver:881958476287459408> • Argent :", "Silver", id, data, inventory_embed)
            InventoryCheckNone("<:gold:881954591774736395> • Or :", "Gold", id, data, inventory_embed)
            InventoryCheckNone("<:diamond:881949161753309194> • Diamant :", "Diamond", id, data, inventory_embed)
            InventoryCheckNone("<:platinium:881964089667121202> • Platine :", "Platinium", id, data, inventory_embed)
            InventoryCheckNone("<:rubis:881960449938186240> • Rubis :", "Rubis", id, data, inventory_embed)
            InventoryCheckNone("<:saphir:881963269424824370> • Saphir :", "Saphir", id, data, inventory_embed)
            InventoryCheckNone("<:emerald:881983813532647434> • Emeraude :", "Emerald", id, data, inventory_embed)
            InventoryCheckNone("<:cobalt:882231543358165002> • Cobalt :", "Cobalt", id, data, inventory_embed)
            InventoryCheckNone("<:amethist:881985189511839744> • Améthyste :", "Amethist", id, data, inventory_embed)
            InventoryCheckNone("<:grenat:881962367037087785> • Grenat :", "Grenat", id, data, inventory_embed)
            InventoryCheckNone("<:turquoise:882235863499686028> • Turquoise :", "Turquoise", id, data, inventory_embed)
            InventoryCheckNone("<:obsidian:882238111818612736> • Obsidienne :", "Obsidian", id, data, inventory_embed)
            
        elif page == 1:
            InventoryCheckNone("<:randomite:881964979639709748> • Randomite :", "Randomite", id, data, inventory_embed)
            InventoryCheckNone("<:mercury:882233112283742218> • Mercure :", "Mercury", id, data, inventory_embed)
            InventoryCheckNone("<:magmastone:881968174025801798> • Pierre Magmatique :", "Magma Stone", id, data, inventory_embed)
            InventoryCheckNone("<:fossil:881977977087336498> • Fossille :", "Fossil", id, data, inventory_embed)
            InventoryCheckNone("<:sacredstone:882234999145922621> • Pierre Sacrée :", "Sacred Stone", id, data, inventory_embed)
            InventoryCheckNone("<:coke:882232188177903626> • Coke :", "Coke", id, data, inventory_embed)
            InventoryCheckNone("<:fluorite:882237334848933918> • Fluorite", "Fluorite", id, data, inventory_embed)
            InventoryCheckNone("<:jade:882239569653792808> • Jade", "Jade", id, data, inventory_embed)
            InventoryCheckNone("<:coal:882226330110926908> • Charbon :", "Coal",id, data, inventory_embed)
            InventoryCheckNone("<:cooper:882228895192076339> • Cuivre :", "Cooper", id, data, inventory_embed)
            InventoryCheckNone("<:magnetite:1075060513593110689> • Magnétite :", "Magnetite", id, data, inventory_embed)
            InventoryCheckNone("<:josephEnModeHot:791311502460059708> • Joseph :", "Joseph", id, data, inventory_embed)
            InventoryCheckNone("🍀 • Lucky Stone :", "Lucky Stone", id, data, inventory_embed)
            InventoryCheckNone("🔱 • Aigue Marine :", "Aigue Marine", id, data, inventory_embed)
            InventoryCheckNone("🌑 • Plutonium :", "Plutonium", id, data, inventory_embed)
            InventoryCheckNone("☢ • Uranium :", "Uranium", id, data, inventory_embed)
        
        return inventory_embed
        
    max_page = 1
    min_page = 0
    page = min_page
    __embed__ = DefaultEmbed(page)
    mess = await ctx.reply(embed=__embed__)
    await mess.add_reaction("⬅")
    await mess.add_reaction("➡")
        
    if not equip:
        if not data[id]["Inventory"] is None:
            w = True
            while w:
                
                def CheckEmoji(reaction, user):
                    return ctx.message.author == user and mess.id == reaction.message.id and (str(reaction.emoji) in ["⬅", "➡"])

                try:
                    reaction, user = await c.bot.wait_for("reaction_add", timeout=60, check=CheckEmoji)
                except asyncio.TimeoutError:
                    w = False
                else:
                    if str(reaction.emoji) == "⬅":
                        if page != min_page:
                            page -= 1               
                    elif str(reaction.emoji) == "➡":
                        if page != max_page:
                            page += 1
                            
                    await mess.edit(embed=DefaultEmbed(page))
            
        else:
            await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")

    elif equip[0] == "equip":

        if not data[id]["Inventory"] is None:

            try:
                if equip[1] == "item":
                    
                    l = list(data[id]["Inventory"]["MP"])
                    print(f"l: {l}")
                    check_error = []
            

                    data[id]["Inventory"]["MP"] = list()
                    print(f"Inventaire: {data[id]['Inventory']['MP']}")

                    for i in range(data[id]['Inventory']['Item Limit']):
                        n = 2 + i
                        # Savoir Si l'Item est dans l'inventaire du joueur
                        try:
                            if int(equip[n]) in data[id]['Inventory']["P Item"]:
                                data[id]['Inventory']["MP"].append(int(equip[n]))
                            else:
                                await ctx.reply(f"Vous ne possédez pas l'objet n° {int(equip[n])} !")
                                check_error.append(False)
                                break
                        except:
                            await ctx.reply(f"Veuillez remplacer les espaces vides par des 0 (Vous pouvez équiper jusqu'à {data[id]['Inventory']['Item Limit']} objets).\nEx: **c!inventory equip item 1 3** équipera les items 1 et 3 alors que **c!inventory equip item 1 0** équipera seulement l'item 1.")
                            check_error.append(False)
                            break

                    
                    if not False in check_error:
                        await ctx.reply("Le(s) objet(s) ont bien été équipé(s) !")
                        with open("assets/player_data.json", "w") as d:
                            json.dump(data, d ,indent=4)

                    else:
                        data[id]['Inventory']["MP"] = l

            
                elif equip[1] == "rank":
                    try:
                        i = int(equip[2])
                        if i in data[id]['Inventory']["P Rank"]:
                            data[id]['Inventory']["Rank"] = i
                            with open("assets/player_data.json", "w") as d:
                                json.dump(data, d ,indent=4)
                            await ctx.reply("Le grade a bien été équipé !")

                        else:
                            await ctx.reply("Vous ne possédez pas ce grade !")

                    except:
                        await ctx.reply("Veuillez choisir un nombre ! || c!inventory equip rank **nombre**")

                else:
                    await ctx.reply("Argument incorrect ! (item, rank)")

            except:
                await ctx.reply("Commande incorrecte !")

        else:
            await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")
            
    else:
        if not data[id]["Inventory"] is None:
            w = True
            while w:
                
                def CheckEmoji(reaction, user):
                    return ctx.message.author == user and mess.id == reaction.message.id and (str(reaction.emoji) in ["⬅", "➡"])

                try:
                    reaction, user = await c.bot.wait_for("reaction_add", timeout=60, check=CheckEmoji)
                except asyncio.TimeoutError:
                    w = False
                else:
                    if str(reaction.emoji) == "⬅":
                        if page != min_page:
                            page -= 1               
                    elif str(reaction.emoji) == "➡":
                        if page != max_page:
                            page += 1
                            
                    await mess.edit(embed=DefaultEmbed(page))
        else:
            await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")

