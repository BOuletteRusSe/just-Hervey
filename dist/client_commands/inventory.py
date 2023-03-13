import discord, json, re, asyncio
from assets.items_price import item_shop_price, item_shop_price_2, item_shop_price_3, item_shop_price_5
from assets.minerals_data import *
from assets.woods_data import woods


def InventoryCheckNone(name, value, id, data, inventory_embed, car):
    
    if car == "mine":
        iv = data[id]["Inventory"]
    elif car == "lj":
       iv = data[id]["Inventory_2"] 
    
    if iv[value] != 0:
        inventory_embed.add_field(name=name, value=iv[value], inline=True)


async def CheckIfUserIsInGuild(ctx, arg):

    """
    0 --> No Problem
    1 --> La mention n'est pas dans le serveur
    2 --> Erreur lors de la mention
    """

    with open("assets/player_data.json") as data:
        data = json.load(data)

    try:
        ping = [int(s) for s in re.findall(r'\d+', str(arg[1]))]
    except:
        return 3

    if len(ping) == 1:
        cc = True
        ping_id = re.findall(r'\d+', str(arg[1]))[0]

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
        max_page = 2
        min_page = 0
        inventory_embed = discord.Embed(title="⚔ INVENTAIRE MINEUR ⚔ | Page %s" % (page + 1), description="Ici, vous pouvez voir tout ce que vous avez a disposition dans votre inventaire de mineur. Vous pouvez faire défiler les pages avec les flèches en bas du message.", color=0x1e4843)
        inventory_embed.set_author(name=user, icon_url=user.avatar_url)
        inventory_embed.add_field(name="💎 • Points de Minage :", value=data[id]["Miner Points"])
        inventory_embed.add_field(name="🛠 • Objet(s) Équipé(s) :", value=e_items)
        inventory_embed.add_field(name="🎭 • Grade :", value=item_shop_price[data[id]["Inventory"]["Rank"]]["Name"], inline=True)
        inventory_embed.add_field(name="Liste des Objets :", value=items, inline=True)
        inventory_embed.add_field(name="Liste des Grades :", value=ranks, inline=True)
        inventory_embed.add_field(name="Liste des Aliages :", value=alliages, inline=True)
        inventory_embed.add_field(name="🔧 • Établi", value=etabli, inline=True)
        inventory_embed.add_field(name=":pick: • Nombre de Pioches Max :", value=data[id]['Inventory']['Item Limit'], inline=True)
        inventory_embed.set_footer(text=f"c!inventory equip item/rank 'nombre' pour équiper une objet ou un grade. (Vous pouvez équiper jusqu'à {data[id]['Inventory']['Item Limit']} item(s) à la fois.)")
        
        if page == 0:
            InventoryCheckNone(f"<:debris:1078401153953435759> • Debrit :", "Debrit", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"<:stone:1082728403104444498> • Pierre :", "Stone", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Iron']['Emoji']} • Fer :", "Iron", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Silver']['Emoji']} • Argent :", "Silver", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Gold']['Emoji']} • Or :", "Gold", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Diamond']['Emoji']} • Diamant :", "Diamond", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Platinium']['Emoji']} • Platine :", "Platinium", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Rubis']['Emoji']} • Rubis :", "Rubis", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Saphir']['Emoji']} • Saphir :", "Saphir", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Emerald']['Emoji']} • Emeraude :", "Emerald", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Cobalt']['Emoji']}• Cobalt :", "Cobalt", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Amethist']['Emoji']} • Améthyste :", "Amethist", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Grenat']['Emoji']} • Grenat :", "Grenat", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Turquoise']['Emoji']} • Turquoise :", "Turquoise", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Obsidian']['Emoji']} • Obsidienne :", "Obsidian", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Dragonite']['Emoji']} • Dragonite :", "Dragonite", id, data, inventory_embed, "mine")
            
        elif page == 1:
            InventoryCheckNone(f"{minerals['Randomite']['Emoji']} • Randomite :", "Randomite", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Magma Stone']['Emoji']} • Pierre Magmatique :", "Magma Stone", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Fossil']['Emoji']} • Fossille :", "Fossil", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Sacred Stone']['Emoji']} • Pierre Sacrée :", "Sacred Stone", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Coke']['Emoji']} • Coke :", "Coke", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Fluorite']['Emoji']} • Fluorite", "Fluorite", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Jade']['Emoji']}• Jade", "Jade", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Coal']['Emoji']} • Charbon :", "Coal",id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Cooper']['Emoji']} • Cuivre :", "Cooper", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Magnetite']['Emoji']} • Magnétite :", "Magnetite", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Joseph']['Emoji']} • Joseph :", "Joseph", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Lucky Stone']['Emoji']} • Lucky Stone :", "Lucky Stone", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"🔱 • Aigue Marine :", "Aigue Marine", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Plutonium']['Emoji']} • Plutonium :", "Plutonium", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Uranium']['Emoji']} • Uranium :", "Uranium", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Quartz']['Emoji']} • Quartz :", "Quartz", id, data, inventory_embed, "mine")
            
        elif page == 2:
            InventoryCheckNone(f"{minerals['Mithril']['Emoji']} • Mithril :", "Mithril", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Dark Stone']['Emoji']} • Pierre Sombre :", "Dark Stone", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Cursed Stone']['Emoji']} • Pierre Maudite :", "Cursed Stone", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Black Mithril']['Emoji']} • Mithril Noir :", "Black Mithril", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Iliosite']['Emoji']} • Iliosite :", "Iliosite", id, data, inventory_embed, "mine")
            InventoryCheckNone(f"{minerals['Fengarite']['Emoji']} • Fengarite :", "Fengarite", id, data, inventory_embed, "mine")
        
        return [inventory_embed, max_page, min_page]
    
    upgrades = ""
    for upgrade in data[id]["Inventory_2"]["Upgrades"]:
        upgrades += f"{str(item_shop_price_5[upgrade]['Name'])} ({upgrade}) | "
        
    if data[id]["Inventory_2"]["Upgrades"] == []:
        upgrades = "Aucun"
    
    def LjEmbed(page):
        max_page = 0
        min_page = 0
        inventory_embed = discord.Embed(title="⚔ INVENTAIRE BÛCHERON ⚔ | Page %s" % (page + 1), description="Ici, vous pouvez voir tout ce que vous avez a disposition dans votre inventaire de bûcheron. Vous pouvez faire défiler les pages avec les flèches en bas du message.", color=0x1e4843)
        inventory_embed.set_author(name=user, icon_url=user.avatar_url)
        inventory_embed.add_field(name="💎 • Points de Bûcheron :", value=data[id]["Lj Points"])
        inventory_embed.add_field(name="🔺 • Améliorations de hache :", value=upgrades, inline=True)
        inventory_embed.add_field(name="🎭 • Grade :", value=item_shop_price[data[id]["Inventory"]["Rank"]]["Name"], inline=True)
        inventory_embed.add_field(name="Liste des Grades :", value=ranks, inline=True)
        inventory_embed.set_footer(text=f"c!inventory equip item/rank 'nombre' pour équiper une objet ou un grade.")
        
        if page == 0:
            InventoryCheckNone(f"{woods['Oak']['Emoji']} • Chêne :", "Oak", id, data, inventory_embed, "lj")
            InventoryCheckNone(f"{woods['Acacia']['Emoji']} • Acacia :", "Acacia", id, data, inventory_embed, "lj")
            InventoryCheckNone(f"{woods['Dark Oak']['Emoji']} • Chêne Noir :", "Dark Oak", id, data, inventory_embed, "lj")
            InventoryCheckNone(f"{woods['Basswood']['Emoji']} • Tilleul :", "Basswood", id, data, inventory_embed, "lj")
            InventoryCheckNone(f"{woods['Palm Tree']['Emoji']} • Palmier :", "Palm Tree", id, data, inventory_embed, "lj")

        return [inventory_embed, max_page, min_page]
        
    page = 0
    typev = 0
    cont = False
    
    try:
        
        cont2 = True
    
        if equip[0] in ["mine", "m"]:
            typev = 1
            dta = DefaultEmbed(page)
        
        elif equip[0] in ["lumberjack", "lj"]:
            typev = 2
            dta = LjEmbed(page)
            
        elif equip[0] == "equip":
            cont = True
            
        else:
            ivt_embed = discord.Embed(title="just Hervey 💎 | ⚔ INVENTAIRE ⚔", description="Bienvenue dans le système d'inventaire ! Pour naviguer à travers vos inventaires de métiers, vous pouvez utiliser les commandes suivantes.\n\n```c!inventory mine (<id d'un joueur>)```  Affiche votre inventaire de `mineur/forgeron` ou celui d'un autre joueur.\n```c!inventory lj (<id d'un joueur>)``` Affiche votre inventaire de `bûcheron` ou celui d'un autre joueur.\n```c!inventory equip item/rank <id de l'item/du rank>```  Permet d'équiper un objet ou un grade à partir de son id trouvable depuis les inventaires.", color=0x39278B)
            await ctx.reply(embed=ivt_embed)
            cont2 = False
            
    except:
        ivt_embed = discord.Embed(title="just Hervey 💎 | ⚔ INVENTAIRE ⚔", description="Bienvenue dans le système d'inventaire ! Pour naviguer à travers vos inventaires de métiers, vous pouvez utiliser les commandes suivantes.\n\n```c!inventory mine (<id d'un joueur>)```  Affiche votre inventaire de `mineur/forgeron` ou celui d'un autre joueur.\n```c!inventory lj (<id d'un joueur>)``` Affiche votre inventaire de `bûcheron` ou celui d'un autre joueur.\n```c!inventory equip item/rank <id de l'item/du rank>```  Permet d'équiper un objet ou un grade à partir de son id trouvable depuis les inventaires.", color=0x39278B)
        await ctx.reply(embed=ivt_embed)
        
    else:
        if cont2:
            if not cont:
                __embed__ = dta[0]
                max_page = dta[1]
                min_page = dta[2]
                mess = await ctx.reply(embed=__embed__)
                await mess.add_reaction("⬅")
                await mess.add_reaction("➡")
                

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
                            
                            if typev == 1: 
                                await mess.edit(embed=DefaultEmbed(page)[0])
                            elif typev == 2:
                                await mess.edit(embed=LjEmbed(page)[0])
                    
                else:
                    embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.reply(embed=embed)
                    
            else:

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
                    
            