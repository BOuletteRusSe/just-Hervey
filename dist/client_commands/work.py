import discord, json, random
from assets.items_price import item_shop_price, item_shop_price_2

async def Mining(ctx, id, minerals, data, to_next_level, r):

    f = False

    for k, v in minerals.items():
        
        if v["Min"] < r < v["Max"]:
            mineral = k
            mineral_info = v
            f = True

    if not f:
        return False


    if mineral in ["Rubis", "Saphir", "Emerald"] and not data[id]["Inventory"]["Platinium Alliage"]:
        embed = discord.Embed(title=item_shop_price[data[id]["Inventory"]["Rank"]]["Name"], description=f"Vous avez trouvé {mineral_info['Name']} {mineral_info['Emoji']}\nVous avez besoin d'un aliage en platine pour pouvoir le miner ! (c!shop item pour en acheter)", color=0x393838)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url=mineral_info["Image"])
        await ctx.reply(embed=embed)
        return True

    if not data[id]["Level"] >= mineral_info["Level Requierd"]:
        return False

    try:
        mineral_info["Xp"] + 1
        mineral_xp = mineral_info["Xp"]
    except:
        mineral_xp = random.randint(mineral_info["Xp"][0], mineral_info["Xp"][1])
    try:
        mineral_info["Price"] + 1
        mineral_price = mineral_info["Price"]
    except:
        mineral_price = random.randint(mineral_info["Price"][0], mineral_info["Price"][1])
    try:
        mineral_info["Anti-Mine"]
        if 3 in data[id]['Inventory']["MP"]:
            return False
    except:
        1 + 1

    if 2 in data[id]["Inventory"]["MP"]:
        mm = mineral_price * 1.1
    else:
        mm = mineral_price

    data[id]["Xp"] += mineral_xp
    data[id]['Money'] += mm
    if 6 in data[id]['Inventory']["MP"]:
        data[id]["Inventory"][mineral] += 1
    data[id]["Inventory"][mineral] += 1

    if data[id]["Xp"]< 0:
        data[id]["Xp"] = 0
    if data[id]['Money']< 0:
        data[id]['Money'] = 0
    if data[id]["Xp"] >= to_next_level:
        data[id]['Level'] += 1
        data[id]["Xp"] -= to_next_level

        # Calcul d'xp pour le prochain niveau
        to_next_level = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))

        if data[id]['Level'] < 10:
            if 1 in data[id]["Inventory"]["MP"]:
                r = random.randint(0, 90)
            else:
                r = random.randint(0, 100)
                         
        elif 20 > data[id]['Level'] >= 10:
            if 1 in data[id]['Inventory']["MP"]:
                r = random.randint(0, 180)
            else:
                r = random.randint(0, 200)

        elif 30 > data[id]['Level'] >= 20:
            if 1 in data[id]['Inventory']["MP"]:
                r = random.randint(0, 260)
            else:
                r = random.randint(0, 300)
                
        elif 40 > data[id]['Level'] >= 30:
                if 1 in data[id]['Inventory']["MP"]:
                    r = random.randint(0, 350)
                else:
                    r = random.randint(0, 400)
                    
        else:
            if 1 in data[id]['Inventory']["MP"]:
                r = random.randint(0, 340)
            else:
                r = random.randint(0, 425)


        with open("assets/player_data.json", 'w') as d:
            json.dump(data, d, indent=4)
        embed = discord.Embed(title=f"**GG**, vous avez atteint le niveau **{data[id]['Level']}** !", description=f"XP nécessaire pour passer au prochain niveau : **{to_next_level}xp**", color=0x56860e)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url="https://i.ibb.co/wyYCHVR/level-up.png")
        await ctx.send(embed=embed)
    with open("assets/player_data.json", 'w') as d:
        json.dump(data, d, indent=4)

    embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description=f"Vous avez trouvé {mineral_info['Name']} {mineral_info['Emoji']}", color=mineral_info["Color"])
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.set_image(url=mineral_info["Image"])
    embed.add_field(name="Bénéfice :", value=f"**{round(mm, 2)}€**", inline=True)
    embed.add_field(name=f"{mineral_info['Emoji']} • {str(mineral_info['Name'])[int(str(mineral_info['Name']).find('*'))-1:]} :", value=data[id]['Inventory'][mineral], inline=True)
    embed.add_field(name="XP :", value=f"**{round(data[id]['Xp'], 2)}**", inline=True)
    embed.add_field(name="Argent :", value=f"**{round(data[id]['Money'], 2)}€**", inline=True)
    embed.add_field(name="Niveau :", value=f"**{data[id]['Level']}**", inline=True)
    embed.set_footer(text=f"+{round(mineral_xp, 2)}xp")
    await ctx.send(embed=embed)
    await ctx.message.delete()
    return True


async def Work(ctx, xp_, cc):

    # INSCRIPTION

    with open("assets/player_data.json") as data:
        data = json.load(data)

    id = str(ctx.author.id)
    c = True
    p = True

    for key in data.keys():
        if key == id:
            c = False

    if c:
        d = await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")
        await d.delete(delay=15)
    else:
        
        for key in data.keys():
            if key == id and data[key]["Hobby"] != None:
                p = False

        if p:
            jm = await ctx.reply("Veuillez choisir votre métier.\n⛏ --> **Mineur**\n(ya qun métier c la hess lol donne des idées)")
            await jm.add_reaction("⛏")

            def CheckEmoji(reaction, user):
                return ctx.message.author == user and jm.id == reaction.message.id and (str(reaction.emoji) == "⛏")

            try:
                reaction = await cc.bot.wait_for("reaction_add", timeout=60, check=CheckEmoji)
                data[id]["Hobby"] = 0
                data[id]["Xp"] = 0
                data[id]["Level"] = 1

                with open("assets/player_data.json", 'w') as d:
                    json.dump(data, d, indent=4)
                await jm.delete()
                await ctx.send(f"Vous êtes devenu(e) mineur avec succès {ctx.author.mention} !")
                await ctx.send("Pour commencer à travailler faites **c!work** !")
                
            except:
                await jm.delete()
                d = await ctx.reply("Délai dépassé !")
                await d.delete(delay=15)

        # Commande XP
        elif "xp" in xp_:

            # Calcul d'xp pour le prochain niveau
            to_next_level = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))

            embed=discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], color=0x393838)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Niveau :", value=f"**{data[id]['Level']}**", inline=False)
            embed.add_field(name="XP :", value=f"**{round(data[id]['Xp'], 2)}**", inline=False)
            embed.add_field(name="XP jusqu'au prochain niveau :", value=to_next_level, inline=False)
            embed.add_field(name="Argent :", value=f"**{round(data[id]['Money'], 2)}€**", inline=False)
            await ctx.send(embed=embed)


        elif data[id]['Hobby'] == 0:    

            # A REVOIR POUR LE SHOP

            # Calcul d'xp pour le prochain niveau
            to_next_level = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))

            if data[id]['Level'] < 10:
                if 1 in data[id]['Inventory']["MP"]:
                    r = random.randint(0, 90)
                else:
                    r = random.randint(0, 100)
        
            elif 20 > data[id]['Level'] >= 10:
                if 1 in data[id]['Inventory']["MP"]:
                    r = random.randint(0, 180)
                else:
                    r = random.randint(0, 200)

            elif 30 > data[id]['Level'] >= 20:
                if 1 in data[id]['Inventory']["MP"]:
                    r = random.randint(0, 260)
                else:
                    r = random.randint(0, 300)
                    
            elif 40 > data[id]['Level'] >= 30:
                if 1 in data[id]['Inventory']["MP"]:
                    r = random.randint(0, 350)
                else:
                    r = random.randint(0, 400)             
            else:
                if 1 in data[id]['Inventory']["MP"]:
                    r = random.randint(0, 340)
                else:
                    r = random.randint(0, 425)
                    
            # Liste des minéraux
            minerals = {
                "Iron" : {
                    "Min" : 0,
                    "Max" : 11,
                    "Name" : "du **Fer** !",
                    "Emoji" : "<:iron:881949148876783646>",
                    "Price" : (20, 75),
                    "Xp" : (5, 20),
                    "Color" : 0x7f7f7f,
                    "Level Requierd" : 0,
                    "Image" : "https://i.ibb.co/vxNTJTR/iron.png"
                },
                "Gold" : {
                    "Min" : 12,
                    "Max" : 22,
                    "Name" : "de **l'Or** !",
                    "Emoji" : "<:gold:881954591774736395>",
                    "Price" : (200, 300),
                    "Xp" : (20, 80),
                    "Color" : 0xffd700,
                    "Level Requierd" : 0,
                    "Image" : "https://i.ibb.co/RNdqgBr/gold.png"
                },
                "Diamond" : {
                    "Min" : 23,
                    "Max" : 31,
                    "Name" : "du **Diamant** !",
                    "Emoji" : "<:diamond:881949161753309194>",
                    "Price" : (800, 1200),
                    "Xp" : (80, 120),
                    "Color" : 0xddeeed,
                    "Level Requierd" : 0,
                    "Image" : "https://i.ibb.co/grpxfXD/diamond.png"
                },
                "Silver" : {
                    "Min" : 32,
                    "Max" : 42,
                    "Name" : "de l'**Argent** !",
                    "Emoji" : "<:silver:881958476287459408>",
                    "Price" : (50, 100),
                    "Xp" : (50, 100),
                    "Color" : 0xC0C0C0,
                    "Level Requierd" : 5,
                    "Image" : "https://i.ibb.co/1K2DxTZ/silver.png"
                },
                "Coal" : {
                    "Min" : 43,
                    "Max" : 54,
                    "Name" : "du **Charbon** !",
                    "Emoji" : "<:coal:882226330110926908>",
                    "Price" : 50,
                    "Xp" : 75,
                    "Color" : 0x463b34,
                    "Level Requierd" : 0,
                    "Image" : "https://i.ibb.co/gvS3YL6/coal.png"
                },
                "Cooper" : {
                    "Min" : 55,
                    "Max" : 63,
                    "Name" : "du **Cuivre** !",
                    "Emoji" : "<:cooper:882228895192076339>",
                    "Price" : 100,
                    "Xp" : 20,
                    "Color" : 0xb36700,
                    "Level Requierd" : 5,
                    "Image" : "https://i.ibb.co/V901trS/cooper.png"
                },
                "Rubis" : {
                    "Min" : 64,
                    "Max" : 71,
                    "Name" : "du **Rubis** !",
                    "Emoji" : "<:rubis:881960449938186240>",
                    "Price" : 2000,
                    "Xp" : 20,
                    "Color" : 0xe0115f,
                    "Level Requierd" : 10,
                    "Image" : "https://i.ibb.co/1dWF0rn/ruby.png"
                },
                "Grenat" : {
                    "Min" : 72,
                    "Max" : 79,
                    "Name" : "du **Grenat** !",
                    "Emoji": "<:grenat:881962367037087785>",
                    "Price" : (200, 600),
                    "Xp" : (50, 70),
                    "Color" : 0x6E0B14,
                    "Level Requierd" : 10,
                    "Image" : "https://i.ibb.co/tC4rgLL/grenat.png"
                },
                "Saphir" : {
                    "Min" : 80,
                    "Max" : 87,
                    "Name" : "du **Saphire** !",
                    "Emoji" : "<:saphir:881963269424824370>",
                    "Price" : 250,
                    "Xp" : 400,
                    "Color" : 0x6977a1,
                    "Level Requierd" : 10,
                    "Image" : "https://i.ibb.co/Gcvm4cy/saphir.png"
                },
                "Platinium" : {
                    "Min" : 88,
                    "Max" : 98,
                    "Name" : "du **Platine** !",
                    "Emoji" : "<:platinium:881964089667121202>",
                    "Price" : (200, 700),
                    "Xp" : (50, 100),
                    "Color" : 0xFAF0C5,
                    "Level Requierd" : 5,
                    "Image" : "https://i.ibb.co/GMr1xRg/platinium.png"
                },
                "Randomite" : {
                    "Min" : 99,
                    "Max" : 106,
                    "Name" : "de la **Randomite** !",
                    "Emoji" : "<:randomite:881964979639709748>",
                    "Price" : (0, 10000),
                    "Xp" : (0, 250),
                    "Color" : 0xe3d3d1,
                    "Level Requierd" : 10,
                    "Image" : "https://i.ibb.co/XJt7DqR/randomite.png"
                },
                "Magma Stone" : {
                    "Min" : 107,
                    "Max" : 112,
                    "Name" : "de la **Pierre de Magma** !",
                    "Emoji": "<:magmastone:881968174025801798>",
                    "Price" : (-1000, 0),
                    "Xp" : (-300, 0),
                    "Color" : 0xec8058,
                    "Level Requierd" : 10,
                    "Image" : "https://i.ibb.co/9tpHG3P/magma-stone.png",
                    "Anti-Mine" : True
                },
                "Joseph" : {
                    "Min" : 113,
                    "Max" : 115,
                    "Name" : "**Joseph** !",
                    "Emoji" : "<:josephEnModeHot:791311502460059708>",
                    "Price" : 10000,
                    "Xp" : 0,
                    "Color" : 0xF0E68C,
                    "Level Requierd" : 20,
                    "Image" : "https://i.ibb.co/fdbcdwp/joseph.png"
                },
                "Sacred Stone" : {
                    "Min" : 116,
                    "Max" : 117,
                    "Name" : "de la **Pierre Sacrée** !",
                    "Emoji" : "<:sacredstone:882234999145922621>",
                    "Price" : 100000,
                    "Xp" : 1000,
                    "Color" : 0xc5c3c2,
                    "Level Requierd" : 20,
                    "Image" : "https://i.ibb.co/hykPsCv/sacred-stone.png"
                },
                "Fossil" : {
                    "Min" : 118,
                    "Max" : 128,
                    "Name" : "un **Fossile** !",
                    "Emoji" : "<:fossil:881977977087336498>",
                    "Price" : 150,
                    "Xp" : 200,
                    "Color" : 0xcdc6bb,
                    "Level Requierd" : 20,
                    "Image" : "https://i.ibb.co/KqBKspq/fossil.png"
                },
                "Emerald" : {
                    "Min" : 129,
                    "Max" : 134,
                    "Name" : "de l**Émeraude** !",
                    "Emoji": "<:emerald:881983813532647434>",
                    "Price" : 2000,
                    "Xp" : 400,
                    "Color" : 0x01d758,
                    "Level Requierd" : 20,
                    "Image" : "https://i.ibb.co/S03kHNd/emerald.png"
                },
                "Amethist" : {
                    "Min" : 135,
                    "Max" : 141,
                    "Name" : "de **l'Améthyste** !",
                    "Emoji": "<:amethist:881985189511839744>",
                    "Price" : 400,
                    "Xp" : 500,
                    "Color" : 0x884da7,
                    "Level Requierd" : 20,
                    "Image" : "https://i.ibb.co/pxNJfPJ/amethist.png"
                },
                "Cobalt" : {
                    "Min" : 142,
                    "Max" : 149,
                    "Name" : "du **Cobalt** !",
                    "Emoji": "<:cobalt:882231543358165002>",
                    "Price" : (150, 500),
                    "Xp" : (200, 750),
                    "Color" : 0x22427c,
                    "Level Requierd" : 20,
                    "Image" : "https://i.ibb.co/wN6K1XQ/cobalt.png"
                },
                "Coke" : {
                    "Min" : 150,
                    "Max" : 157,
                    "Name" : "du **Charbon à Coke** !",
                    "Emoji" : "<:coke:882232188177903626>",
                    "Price" : -500,
                    "Xp" : 0,
                    "Color" : 0xF5FFFA,
                    "Level Requierd" : 20,
                    "Image" : "https://i.ibb.co/HzQN5cy/coke.png"
                },
                "Mercury" : {
                    "Min" : 158,
                    "Max" :165,
                    "Name" : "du **Mercure** !",
                    "Emoji": "<:mercury:882233112283742218>",
                    "Price" : 200,
                    "Xp" : 100,
                    "Color" : 0xc5473b,
                    "Level Requierd" : 30,
                    "Image" : "https://i.ibb.co/nM0ZVrP/mercury.png"
                },
                "Turquoise" : {
                    "Min" : 166,
                    "Max" : 170,
                    "Name" : "de la **Turquoise** !",
                    "Emoji" : "<:turquoise:882235863499686028>",
                    "Price" : 100,
                    "Xp" : 1000,
                    "Color" : 0x25fde9,
                    "Level Requierd" : 30,
                    "Image" : "https://i.ibb.co/TPvqt3X/turquoise.png"
                },
                "Fluorite" : {
                    "Min" : 171,
                    "Max" : 176,
                    "Name" : "de la **Fluorite** !",
                    "Emoji" : "<:fluorite:882237334848933918>",
                    "Price" : 150,
                    "Xp" : 800,
                    "Color" : 0x25fde9,
                    "Level Requierd" : 30,
                    "Image" : "https://i.ibb.co/jbpsNYf/fluorite.png"
                },
                "Obsidian" : {
                    "Min" : 177,
                    "Max" : 184,
                    "Name" : "de l'**Obsidienne** !",
                    "Emoji": "<:obsidian:882238111818612736>",
                    "Price" : 50,
                    "Xp" : 350,
                    "Color" : 0xd0eea4,
                    "Level Requierd" : 30,
                    "Image" : "https://i.ibb.co/wsMjdYs/obsidian.png"
                },
                "Jade" : {
                    "Min" : 185,
                    "Max" : 191,
                    "Name" : "du **Jade** !",
                    "Emoji": "<:jade:882239569653792808>",
                    "Price" : 700,
                    "Xp" : 300,
                    "Color" : 0x799d91,
                    "Level Requierd" : 30,
                    "Image" : "https://i.ibb.co/KLDjPjr/jade.png"
                },
                "Magnetite" : {
                    "Min" : 192,
                    "Max" : 181,
                    "Name" : "de la **Magnétite** !",
                    "Emoji": "<:magnetite:1075060513593110689>",
                    "Price" : 150,
                    "Xp" : (250, 1500),
                    "Color" : 0xfef590,
                    "Level Requierd" : 40,
                    "Image" : "https://i.ibb.co/C7mbYjR/magnetite.png"
                }
            }

            # Pioche ticket (pas de modification  nécessaire)
            if 9 in data[id]['Inventory']["MP"]:
                if random.randint(0, 7) == 7:
                    data[id]["Ticket"] += 1
                    with open("assets/player_data.json", 'w') as d:
                        json.dump(data, d, indent=4)
                    embed = discord.Embed(title="🎟 • Vous avez trouvé un ticket en minant !", color=0x157c0e)
                    embed.add_field(name="🎟 • Tickets :", value=data[id]["Ticket"])
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.reply(embed=embed)

            if await Mining(ctx, id, minerals, data, to_next_level, r) == False:
                
                # PIOCHE DU MARAUDEUR A REVOIR
                if 7 not in data[id]['Inventory']["MP"] and data[id]['Level'] >= 10:
                    v = random.randint(1, 3)
                    if not v == 1:
                        a = random.choice([True, False, True])
                        if a:
                            if 2 in data[id]['Inventory']["MP"]:
                                mm = round((0.25 * (data[id]['Level'] / 5)) * 1.1, 2)
                            else:
                                mm = round(0.25 * (data[id]['Level'] / 5), 2)
                            xx = round(data[id]['Level'] / 5, 2)
                            data[id]['Money'] += mm
                            data[id]['Xp'] += xx
                            if 6 in data[id]['Inventory']["MP"]:
                                data[id]['Inventory']["Debrit"] += 1
                            data[id]['Inventory']["Debrit"] += 1
                            with open("assets/player_data.json", 'w') as d:
                                json.dump(data, d, indent=4)
                            embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description="Vous avez trouvé un **débrit** ! <:debrit:882240995717156874>", color=0x3a3c3d)
                            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            embed.set_image(url="https://i.ibb.co/r3zYVN8/debrit.png")
                            embed.add_field(name="Bénéfice :", value=f"**{round(mm, 2)}€**", inline=True)
                            embed.add_field(name="<:debrit:882240995717156874> • Débrits :", value=data[id]['Inventory']["Debrit"], inline=True)
                            embed.add_field(name="XP :", value=f"**{round(data[id]['Xp'], 2)}**", inline=True)
                            embed.add_field(name="Argent :", value=f"**{round(data[id]['Money'], 2)}€**", inline=True)
                            embed.add_field(name="Niveau :", value=f"**{data[id]['Level']}**", inline=True)
                            embed.set_footer(text=f"+{xx}xp")
                            await ctx.send(embed=embed)
                            await ctx.message.delete()
                        else:
                            if 2 in data[id]['Inventory']["MP"]:
                                mm = round((0.25 * data[id]['Level']) * 1.1, 2)
                            else:
                                mm = round(0.25 * data[id]['Level'], 2)
                            xx = round(data[id]['Level'], 2)
                            data[id]['Xp']+= xx
                            data[id]['Money'] += mm
                            v = 1
                            if 6 in data[id]['Inventory']["MP"]:
                                data[id]['Inventory']["Stone"] += 1
                            data[id]['Inventory']["Stone"] += 1
                    else:
                        if 2 in data[id]['Inventory']["MP"]:
                                mm = round((0.25 * data[id]['Level']) * 1.1, 2)
                        else:
                            mm = round(0.25 * data[id]['Level'], 2)
                        xx = round(data[id]['Level'], 2)
                        data[id]['Xp'] += xx
                        data[id]['Money'] += mm
                        if 6 in data[id]['Inventory']["MP"]:
                            data[id]['Inventory']["Stone"] += 1
                        data[id]['Inventory']["Stone"] += 1

                else:
                    if 2 in data[id]['Inventory']["MP"]:
                                mm = round((0.25 * data[id]['Level']) * 1.1, 2)
                    else:
                        mm = round(0.25 * data[id]['Level'], 2)
                    xx = round(data[id]['Level'], 2)
                    data[id]['Xp'] += xx
                    data[id]['Money'] += mm
                    v = 1
                    if 6 in data[id]['Inventory']["MP"]:
                            data[id]['Inventory']["Stone"] += 1
                    data[id]['Inventory']["Stone"] += 1

                # IF LEVEL UP
                if data[id]['Xp'] >= to_next_level:
                    data[id]['Level'] += 1
                    data[id]['Xp'] -= to_next_level
                    
                    # Calcul d'xp pour le prochain niveau
                    to_next_level = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))

                    if data[id]['Level'] < 10:
                        if 1 in data[id]['Inventory']["MP"]:
                            r = random.randint(0, 90)
                        else:
                            r = random.randint(0, 100)
       
                    elif 20 > data[id]['Level'] >= 10:
                        if 1 in data[id]['Inventory']["MP"]:
                            r = random.randint(0, 180)
                        else:
                            r = random.randint(0, 200)

                    elif 30 > data[id]['Level'] >= 20:
                        if 1 in data[id]['Inventory']["MP"]:
                            r = random.randint(0, 260)
                        else:
                            r = random.randint(0, 300)

                    elif 40 > data[id]['Level'] >= 30:
                        if 1 in data[id]['Inventory']["MP"]:
                            r = random.randint(0, 350)
                        else:
                            r = random.randint(0, 400)
                    
                    else:
                        if 1 in data[id]['Inventory']["MP"]:
                            r = random.randint(0, 340)
                        else:
                            r = random.randint(0, 425)


                    with open("assets/player_data.json", 'w') as d:
                        json.dump(data, d, indent=4)

                    embed = discord.Embed(title=f"**GG**, vous avez atteint le niveau **{data[id]['Level']}** !", description=f"XP nécessaire pour passer au prochain niveau : **{to_next_level}xp**", color=0x56860e)
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    embed.set_image(url="https://i.ibb.co/wyYCHVR/level-up.png")
                    await ctx.send(embed=embed)
                
                if v == 1:
                    with open("assets/player_data.json", 'w') as d:
                        json.dump(data, d, indent=4)
                    embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description="Vous avez trouvé de la **pierre** ! <:stone:882241850965118978>", color=0x9f9c9a)
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    embed.set_image(url="https://i.ibb.co/23Wbsbp/stone.png")
                    embed.add_field(name="Bénéfice :", value=f"**{round(mm, 2)}€**", inline=True)
                    embed.add_field(name="<:stone:882241850965118978> • Pierre :", value=data[id]['Inventory']["Stone"], inline=True)
                    embed.add_field(name="XP :", value=f"**{round(data[id]['Xp'], 2)}**", inline=True)
                    embed.add_field(name="Argent :", value=f"**{round(data[id]['Money'], 2)}€**", inline=True)
                    embed.add_field(name="Niveau :", value=f"**{data[id]['Level']}**", inline=True)
                    embed.set_footer(text=f"+{xx}xp")
                    await ctx.send(embed=embed)
                    await ctx.message.delete()
