import discord, json, random
from assets.items_price import item_shop_price, item_shop_price_2
from assets.minerals_data import minerals

async def Mining(ctx, id, minerals, data, to_next_level):
    
    if 4 in data[id]["Inventory"]["P Forge"]:
        n = random.randint(0, 2125)
    else:
        n = random.randint(0, 2500)
        
    if n == 0:
        
        plans = {
            "5": 50,
            "2": 25,
            "0": 75,
            "7": 50
        }
        
        while True:
        
            keys = []
            values = []
            t = False
            for k, v in plans.items():
                keys.append(int(k))
                values.append(v)
                if not int(k) in data[id]["Inventory"]["Plans"]:
                    t = True
            
            if not t:
                await ctx.reply("Vous avez déjà débloqué tout les plans disponibles en minant !")
                return True
            else:
                r = list(random.choices(keys, values))[0]
                if r not in data[id]["Inventory"]["Plans"]:
                    embed = discord.Embed(title=item_shop_price[data[id]["Inventory"]["Rank"]]["Name"], description=f"Vous avez trouvé le plan n°`{r}` ! <:plans:1078401293590204508>\nPour voir la recette faites la commande `c!forge recipes`.", color=0xACC2C6)
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    embed.set_image(url="https://i.ibb.co/Npj53zP/plans.png")
                    await ctx.reply(embed=embed)
                    
                    data[id]["Inventory"]["Plans"].append(r)
                    
                    with open("assets/player_data.json", 'w') as d:
                        json.dump(data, d, indent=4)
                    return True
    
    else:
        if 1 not in data[id]["Inventory"]["MP"]:
            dic = {"Stone": 45, "Other": 55}
        else:
            dic = {"Stone": 35, "Other": 65}
            
        if list(random.choices(*zip(*dic.items())))[0] == "Stone":
            return False
        
        while True:
        
            keys = []
            values = []
            for k, v in minerals.items():
                for k_, v_ in v.items():
                    if k_ == "Proba":
                        keys += [k]
                        values += [v_]
                    
            r = random.choices(keys, values)

            for k, v in minerals.items():
                if k == r[0]:
                    mineral = k
                    mineral_info = v
                
            if data[id]["Level"] >= mineral_info["Level Requierd"]:
                break

        if mineral in ["Rubis", "Saphir", "Emerald"] and not (4 in data[id]["Inventory"]["Alliages"]):
            embed = discord.Embed(title=item_shop_price[data[id]["Inventory"]["Rank"]]["Name"], description=f"Vous avez trouvé {mineral_info['Name']} {mineral_info['Emoji']}\nVous avez besoin d'un aliage en platine pour pouvoir le miner ! (c!shop item pour en acheter)", color=0x393838)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_image(url=mineral_info["Image"])
            await ctx.reply(embed=embed)
            return True
        
        elif mineral in ["Uranium", "Plutonium"] and not (12 in data[id]["Inventory"]["Alliages"]):
            embed = discord.Embed(title=item_shop_price[data[id]["Inventory"]["Rank"]]["Name"], description=f"Vous avez trouvé {mineral_info['Name']} {mineral_info['Emoji']}\nVous avez besoin d'un aliage en obsidienne pour pouvoir le miner ! (c!shop item pour en acheter)", color=0x393838)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_image(url=mineral_info["Image"])
            await ctx.reply(embed=embed)
            return True

        try:
            mineral_info["Xp"] + 1
            mineral_xp = mineral_info["Xp"]
        except:
            mineral_xp = random.randint(mineral_info["Xp"][0], mineral_info["Xp"][1])
        if 11 in data[id]["Inventory"]["MP"]:
            mineral_xp = mineral_xp + (mineral_xp / 100 * 10)
        try:
            mineral_info["Miner Points"] + 1
            mineral_price = mineral_info["Miner Points"]
        except:
            mineral_price = random.randint(mineral_info["Miner Points"][0], mineral_info["Miner Points"][1])
        try:
            mineral_info["Price"] + 1
            revente = mineral_info["Price"]
        except:
            revente = random.randint(mineral_info["Price"][0], mineral_info["Price"][1])
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
        data[id]['Miner Points'] += mm
        if 6 in data[id]['Inventory']["MP"] and random.choice([True, False, False]):
            txt = "\nVotre pioche de multiplication vous a permis de récolter un minerai en plus !"
            data[id]["Inventory"][mineral] += 2
        else:
            txt = ""
            data[id]["Inventory"][mineral] += 1

        if data[id]["Xp"] < 0:
            data[id]["Xp"] = 0
        if data[id]['Miner Points'] < 0:
            data[id]['Miner Points'] = 0
        if data[id]["Xp"] >= to_next_level:
            data[id]['Level'] += 1
            data[id]["Xp"] -= to_next_level

            # Calcul d'xp pour le prochain niveau
            to_next_level = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))

            with open("assets/player_data.json", 'w') as d:
                json.dump(data, d, indent=4)
            embed = discord.Embed(title=f"**GG**, vous avez atteint le niveau **{data[id]['Level']}** !", description=f"XP nécessaire pour passer au prochain niveau : **{to_next_level}xp**", color=0x56860e)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_image(url="https://i.ibb.co/wyYCHVR/level-up.png")
            await ctx.send(embed=embed)
        with open("assets/player_data.json", 'w') as d:
            json.dump(data, d, indent=4)

        embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description=f"Vous avez trouvé {mineral_info['Name']} {mineral_info['Emoji']}\n{mineral_info['Description']}{txt}", color=mineral_info["Color"])
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url=mineral_info["Image"])
        embed.add_field(name="Points de Mineur gagnés :", value=f"**{round(mm, 2)}**", inline=True)
        embed.add_field(name="Prix de Revente :", value=f"**{revente}€**", inline=True)
        embed.add_field(name=f"{mineral_info['Emoji']} • {str(mineral_info['Name'])[int(str(mineral_info['Name']).find('*'))-1:]} :", value=data[id]['Inventory'][mineral], inline=True)
        embed.add_field(name="XP :", value=f"**{round(data[id]['Xp'], 2)}**", inline=True)
        embed.add_field(name="Points de Mineur :", value=f"**{round(data[id]['Miner Points'], 2)}**", inline=True)
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
            embed.add_field(name="Points de Mineur :", value=f"**{round(data[id]['Miner Points'], 2)}**", inline=False)
            await ctx.send(embed=embed)


        elif data[id]['Hobby'] == 0:    

            # A REVOIR POUR LE SHOP

            # Calcul d'xp pour le prochain niveau
            to_next_level = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))

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

            if await Mining(ctx, id, minerals, data, to_next_level) == False:
                
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
                            if 11 in data[id]["Inventory"]["MP"]:
                                xx = round(xx + (xx / 100 * 10), 2)
                            data[id]['Miner Points'] += mm
                            data[id]['Xp'] += xx
                            if 6 in data[id]['Inventory']["MP"] and random.choice([True, False, False]):
                                txt = "\nVotre pioche de multiplication vous a permis de récolter un débris en plus !"
                                data[id]["Inventory"]["Debrit"] += 2
                            else:
                                txt = ""
                                data[id]["Inventory"]["Debrit"] += 1
                            with open("assets/player_data.json", 'w') as d:
                                json.dump(data, d, indent=4)
                            embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description=f"Vous avez trouvé un **débrit** ! <:debris:1078401153953435759>\nDeux boulons et trois vis, de quoi fabriquer, rien du tout...{txt}", color=0x3a3c3d)
                            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            embed.set_image(url="https://i.ibb.co/Lrt60yr/debris.png")
                            embed.add_field(name="Points de Mineur gagnés :", value=f"**{round(mm, 2)}**", inline=True)
                            embed.add_field(name="<:debris:1078401153953435759> • Débris :", value=data[id]['Inventory']["Debrit"], inline=True)
                            embed.add_field(name="XP :", value=f"**{round(data[id]['Xp'], 2)}**", inline=True)
                            embed.add_field(name="Points de Mineur :", value=f"**{round(data[id]['Miner Points'], 2)}**", inline=True)
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
                            if 11 in data[id]["Inventory"]["MP"]:
                                xx = round(xx + (xx / 100 * 10), 2)
                            data[id]['Xp']+= xx
                            data[id]['Miner Points'] += mm
                            v = 1
                            if 6 in data[id]['Inventory']["MP"] and random.choice([True, False, False]):
                                txt = "\nVotre pioche de multiplication vous a permis de récolter une pierre en plus !"
                                data[id]["Inventory"]["Stone"] += 2
                            else:
                                txt = ""
                                data[id]["Inventory"]["Stone"] += 1
                    else:
                        if 2 in data[id]['Inventory']["MP"]:
                                mm = round((0.25 * data[id]['Level']) * 1.1, 2)
                        else:
                            mm = round(0.25 * data[id]['Level'], 2)
                        xx = round(data[id]['Level'], 2)
                        if 11 in data[id]["Inventory"]["MP"]:
                            xx = round(xx + (xx / 100 * 10), 2)
                        data[id]['Xp'] += xx
                        data[id]['Miner Points'] += mm
                        if 6 in data[id]['Inventory']["MP"] and random.choice([True, False]):
                            data[id]['Inventory']["Stone"] += 1
                        data[id]['Inventory']["Stone"] += 1

                else:
                    if 2 in data[id]['Inventory']["MP"]:
                                mm = round((0.25 * data[id]['Level']) * 1.1, 2)
                    else:
                        mm = round(0.25 * data[id]['Level'], 2)
                    xx = round(data[id]['Level'], 2)
                    data[id]['Xp'] += xx
                    if 11 in data[id]["Inventory"]["MP"]:
                        xx = round(xx + (xx / 100 * 10), 2)
                    data[id]['Miner Points'] += mm
                    v = 1
                    if 6 in data[id]['Inventory']["MP"] and random.choice([True, False, False]):
                        txt = "\nVotre pioche de multiplication vous a permis de récolter une pierre en plus !"
                        data[id]["Inventory"]["Stone"] += 2
                    else:
                        txt = ""
                        data[id]["Inventory"]["Stone"] += 1

                # IF LEVEL UP
                if data[id]['Xp'] >= to_next_level:
                    data[id]['Level'] += 1
                    data[id]['Xp'] -= to_next_level
                    
                    # Calcul d'xp pour le prochain niveau
                    to_next_level = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))

                    with open("assets/player_data.json", 'w') as d:
                        json.dump(data, d, indent=4)

                    embed = discord.Embed(title=f"**GG**, vous avez atteint le niveau **{data[id]['Level']}** !", description=f"XP nécessaire pour passer au prochain niveau : **{to_next_level}xp**", color=0x56860e)
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    embed.set_image(url="https://i.ibb.co/wyYCHVR/level-up.png")
                    await ctx.send(embed=embed)
                
                if v == 1:
                    with open("assets/player_data.json", 'w') as d:
                        json.dump(data, d, indent=4)
                    embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description=f"Vous avez trouvé de la **pierre** ! <:stone:1078401377555976232>\nUn des matériaux d'artisanat les plus communs.\nIl peut servir à fabriquer des pioches.{txt}", color=0x9f9c9a)
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    embed.set_image(url="https://i.ibb.co/DQNdPY1/stone.png")
                    embed.add_field(name="Points de Mineur gagnés :", value=f"**{round(mm, 2)}**", inline=True)
                    embed.add_field(name="<:stone:1078401377555976232> • Pierre :", value=data[id]['Inventory']["Stone"], inline=True)
                    embed.add_field(name="XP :", value=f"**{round(data[id]['Xp'], 2)}**", inline=True)
                    embed.add_field(name="Points de Mineur :", value=f"**{round(data[id]['Miner Points'], 2)}**", inline=True)
                    embed.add_field(name="Niveau :", value=f"**{data[id]['Level']}**", inline=True)
                    embed.set_footer(text=f"+{xx}xp")
                    await ctx.send(embed=embed)
                    await ctx.message.delete()
