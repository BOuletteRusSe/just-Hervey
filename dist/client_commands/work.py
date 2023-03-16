import discord, json, random, asyncio
from assets.items_price import item_shop_price, item_shop_price_2
from assets.minerals_data import minerals
from assets.woods_data import woods

async def Mining(ctx, id, minerals, data, to_next_level, job, cc):
    
    def ChoseFromList(level):
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
                
            if data[id][level] >= mineral_info["Level Requierd"]:
                return [mineral, mineral_info]
            
    def RandomStats(mineral_info, points):
        
        try:
            mineral_info["Xp"] + 1
            mineral_xp = mineral_info["Xp"]
        except:
            mineral_xp = random.randint(mineral_info["Xp"][0], mineral_info["Xp"][1])
        if (11 in data[id]["Inventory"]["MP"] and points == "Miner Points") or (1 in data[id]["Inventory_2"]["Upgrades"] and points == "Lj Points"):
            mineral_xp = mineral_xp + (mineral_xp / 100 * 10)
        try:
            mineral_info[points] + 1
            mineral_price = mineral_info[points]
        except:
            mineral_price = random.randint(mineral_info[points][0], mineral_info[points][1])
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
            
        return [mineral_xp, mineral_price, revente]
    
    if 4 in data[id]["Inventory"]["P Forge"]:
        n = random.randint(0, 1488)
    else:
        n = random.randint(0, 1750)
        
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
                return False
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
    
    elif job == "miner":
        if 1 not in data[id]["Inventory"]["MP"]:
            dic = {"Stone": 45, "Other": 55}
        else:
            dic = {"Stone": 35, "Other": 65}
            
        if list(random.choices(*zip(*dic.items())))[0] == "Stone":
            return False
        
        ml = ChoseFromList("Level")
        mineral = ml[0]
        mineral_info = ml[1]

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

        ml = RandomStats(mineral_info, "Miner Points")
        mineral_price = ml[1]
        mineral_xp = ml[0]
        revente = ml[2]

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
        embed.add_field(name="%s • %s :" % (mineral_info['Emoji'], str(mineral_info['Name'])[int(str(mineral_info['Name']).find('*'))-1:].replace('!', '').replace("'", "")), value=data[id]['Inventory'][mineral], inline=True)
        xpDashes = 25
        to_next_level_2 = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))
        dashConvert2 = int(to_next_level_2 / xpDashes)
        currentDashes2 = int(data[id]['Xp'] / dashConvert2)
        remain2 = xpDashes - currentDashes2
        xpDisplay2 = '━' * currentDashes2
        remainingDisplay2 = '᲼' * remain2
        percent2 = f"{round(data[id]['Xp'])}/{round(to_next_level_2)}"
        space2 = '᲼' * int((len(xpDisplay2) + len(remainingDisplay2)) / 2)
        embed.add_field(name="Rareté :", value=mineral_info["Rareté"], inline=True)
        embed.add_field(name="Points de Mineur :", value=f"**{round(data[id]['Miner Points'], 2)}**", inline=True)
        embed.add_field(name="Niveau :", value=f"**{data[id]['Level']}|{xpDisplay2}◈**{remainingDisplay2}**|{data[id]['Level'] + 1}**\n{space2}**{percent2}**", inline=False)
        embed.set_footer(text=f"+{round(mineral_xp, 2)}xp")
        await ctx.send(embed=embed)
        await ctx.message.delete()
        return True
    
    elif job == "lj":
        
        ml = ChoseFromList("Lj Level")
        mineral = ml[0]
        mineral_info = ml[1]
        
        ml = RandomStats(mineral_info, "Lj Points")
        mm = ml[1]
        mineral_xp = ml[0]
        revente = ml[2]
        dura = mineral_info["Hp"]
        
        await ctx.message.delete()
        
        def CreateEmbed(d):
            embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description=f"Vous avez trouvé {mineral_info['Name']} {mineral_info['Emoji']}\n{mineral_info['Description']}", color=mineral_info["Color"])
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_image(url=mineral_info["Image"])
            embed.add_field(name="Rareté :", value=mineral_info["Rareté"], inline=True)
            embed.add_field(name="🧱 Résistance", value=d, inline=False)
            embed.set_footer(text=f"Pour pouvoir récolter ce bois, veuillez cliquez réaction ci-dessous {d} fois.")
            return embed
        
        embed = CreateEmbed(dura)
        mess = await ctx.send(embed=embed)
        
        while dura > 0:
        
            await mess.add_reaction("🪓")

            def CheckEmoji(reaction, user):
                return ctx.message.author == user and mess.id == reaction.message.id and (str(reaction.emoji) == "🪓")

            try:
                reaction, user = await cc.bot.wait_for("reaction_add", timeout=60, check=CheckEmoji)
            except asyncio.TimeoutError:
                break
            else:
                if str(reaction.emoji) == "🪓":
                   dura -= 1
            
            embed = CreateEmbed(dura)
            await mess.edit(embed=embed)
            
        await mess.delete()

        data[id]["Lj Xp"] += mineral_xp
        data[id]['Lj Points'] += mm
        data[id]["Inventory_2"][mineral] += 1
        
        to_next_level = int(10 * (int(data[id]["Lj Level"] / 2) * data[id]["Lj Level"]))

        if data[id]["Lj Xp"] < 0:
            data[id]["Lj Xp"] = 0
        if data[id]['Lj Points'] < 0:
            data[id]['Lj Points'] = 0
        if data[id]["Lj Xp"] >= to_next_level:
            data[id]['Lj Level'] += 1
            data[id]["Lj Xp"] -= to_next_level

            # Calcul d'xp pour le prochain niveau
            to_next_level = int(10 * (int(data[id]["Lj Level"] / 2) * data[id]["Lj Level"]))

            with open("assets/player_data.json", 'w') as d:
                json.dump(data, d, indent=4)
            embed = discord.Embed(title=f"**GG**, vous avez atteint le niveau **{data[id]['Lj Level']}** !", description=f"XP nécessaire pour passer au prochain niveau : **{to_next_level}xp**", color=0x56860e)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_image(url="https://i.ibb.co/wyYCHVR/level-up.png")
            await ctx.send(embed=embed)
        with open("assets/player_data.json", 'w') as d:
            json.dump(data, d, indent=4)

        
        embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description=f"Vous avez trouvé {mineral_info['Name']} {mineral_info['Emoji']}\n{mineral_info['Description']}", color=mineral_info["Color"])
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url=mineral_info["Image"])
        embed.add_field(name="Rareté :", value=mineral_info["Rareté"], inline=True)
        embed.add_field(name="Points de Bûcheron gagnés :", value=f"**{round(mm, 2)}**", inline=True)
        embed.add_field(name="Prix de Revente :", value=f"**{revente}€**", inline=True)
        embed.add_field(name="%s • %s :" % (mineral_info['Emoji'], str(mineral_info['Name'])[int(str(mineral_info['Name']).find('*'))-1:].replace('!', '').replace("'", "")), value=data[id]['Inventory_2'][mineral], inline=True)
        xpDashes = 25
        to_next_level_2 = int(10 * (int(data[id]["Lj Level"] / 2) * data[id]["Lj Level"]))
        dashConvert2 = int(to_next_level_2 / xpDashes)
        currentDashes2 = int(data[id]['Lj Xp'] / dashConvert2)
        remain2 = xpDashes - currentDashes2
        xpDisplay2 = '━' * currentDashes2
        remainingDisplay2 = '᲼' * remain2
        percent2 = f"{round(data[id]['Lj Xp'])}/{round(to_next_level_2)}"
        space2 = '᲼' * int((len(xpDisplay2) + len(remainingDisplay2)) / 2)
        embed.add_field(name="Points de Bûcheron :", value=f"**{round(data[id]['Lj Points'], 2)}**", inline=True)
        embed.add_field(name="Niveau :", value=f"**{data[id]['Lj Level']}|{xpDisplay2}◈**{remainingDisplay2}**|{data[id]['Lj Level'] + 1}**\n{space2}**{percent2}**", inline=False)
        embed.set_footer(text=f"+{round(mineral_xp, 2)}xp")
        await ctx.send(embed=embed)
        
        return True

async def Work(ctx, arg, cc):

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
        embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        
        def EnumerateArg(t1, t2):
            for e in arg:
                if e in [t1, t2]:
                    return True
            return False

        def CheckIfIsBanned():
            for v in [word.strip() for word in open("assets/texts/autofarm_ids.txt", encoding="utf-8")]:
                if str(id) == v:
                    return False
            return True
        
        async def AfkTest():
            if random.randint(0, 100) == 0:
                embed = discord.Embed(title="Test Anti-AFK", description="Êtes vous toujours là ?", color=0x777777)
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed.set_footer(text="Veuillez réagir avec la réaction \"✅\" si dessous dans les 30 prochaines secondes afin de prouver que vous n'utilisez pas un système de farming automatique.")
                message = await ctx.reply(embed=embed)
                
                await message.add_reaction("✅")

                try:
                
                    def CheckEmoji(reaction, user):
                        return id == str(user.id) and message.id == reaction.message.id and str(reaction.emoji) == "✅"


                    reaction, user = await cc.bot.wait_for("reaction_add", timeout=30, check=CheckEmoji)

                    if reaction.emoji == "✅":
                        embed = discord.Embed(title="Test Anti-AFK", description="Merci de votre réponse.", color=0x54CD23)
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        embed.set_footer(text="Vous gagnez 1€ en gage d'honnêteté.")
                        data[id]["Money"] += 1
                        await message.edit(embed=embed) 
                        return False
                        
                except:
                    embed = discord.Embed(title="Test Anti-AFK", description="Délai dépassé !", color=0xCD2323)
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    embed.set_footer(text="Votre id a été enregistré dans la liste des potentiels personnes utilisant un système de farming automatique. Votre cas sera traité et passible d'une pénalisation.")
                    with open("assets/texts/autofarm_ids.txt", "a", encoding="utf-8") as b: b.write(f"{id}\n")
                    await message.edit(embed=embed)
                    return False
                
            else:
                return True

        if EnumerateArg("mine", "m"):
            
            if CheckIfIsBanned():
                if await AfkTest():

                    # Calcul d'xp pour le prochain niveau
                    to_next_level = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))

                    # Pioche ticket (pas de modification  nécessaire)
                    if 9 in data[id]['Inventory']["MP"]:
                        if random.randint(0, 10) == 10:
                            data[id]["Ticket"] += 1
                            with open("assets/player_data.json", 'w') as d:
                                json.dump(data, d, indent=4)
                            embed = discord.Embed(title="🎟 • Vous avez trouvé un ticket en minant !", color=0x157c0e)
                            embed.add_field(name="🎟 • Tickets :", value=data[id]["Ticket"])
                            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            await ctx.reply(embed=embed)

                    if await Mining(ctx, id, minerals, data, to_next_level, "miner", cc) == False:
                        
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
                                    embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description=f"Vous avez trouvé un **débrit** ! <:debris:1078401153953435759>\nLes débrits, des fragments de roche éparpillés dans les mines, semblent insignifiants à première vue. Pourtant, ces modestes éclats recèlent un potentiel incroyable. Les mineurs les ramassent en passant, sachant que ces résidus de pierre peuvent être fondus et transformés en matériaux précieux.{txt}", color=0x3a3c3d)
                                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                    embed.set_image(url="https://i.ibb.co/Lrt60yr/debris.png")
                                    embed.add_field(name="Points de Mineur gagnés :", value=f"**{round(mm, 2)}**", inline=True)
                                    embed.add_field(name="<:debris:1078401153953435759> • Débris :", value=data[id]['Inventory']["Debrit"], inline=True)
                                    xpDashes = 25
                                    to_next_level_2 = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))
                                    dashConvert2 = int(to_next_level_2 / xpDashes)
                                    currentDashes2 = int(data[id]['Xp'] / dashConvert2)
                                    remain2 = xpDashes - currentDashes2
                                    xpDisplay2 = '━' * currentDashes2
                                    remainingDisplay2 = '᲼' * remain2
                                    percent2 = f"{round(data[id]['Xp'])}/{round(to_next_level_2)}"
                                    space2 = '᲼' * int((len(xpDisplay2) + len(remainingDisplay2)) / 2)
                                    embed.add_field(name="Rareté :", value="⚫ • Commun", inline=True)
                                    embed.add_field(name="Points de Mineur :", value=f"**{round(data[id]['Miner Points'], 2)}**", inline=True)
                                    embed.add_field(name="XP :", value=f"**{data[id]['Level']}|{xpDisplay2}◈**{remainingDisplay2}**|{data[id]['Level'] + 1}**\n{space2}**{percent2}**", inline=False)
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
                            embed = discord.Embed(title=item_shop_price[data[id]['Inventory']["Rank"]]["Name"], description=f"Vous avez trouvé de la **pierre** ! <:stone:1082728403104444498>\nLa pierre, un minerai ancestral d'un gris élégant, est la base de nombreuses civilisations depuis des siècles. Les légendes disent que cette pierre est née de la fusion des éléments primordiaux qui ont créé notre monde. Certains croyaient même que la pierre avait des pouvoirs magiques, capables de guérir les maladies et de protéger les esprits des mauvais esprits.{txt}", color=0x808080)
                            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            embed.set_image(url="https://i.ibb.co/br7d4sL/stone.png")
                            embed.add_field(name="Points de Mineur gagnés :", value=f"**{round(mm, 2)}**", inline=True)
                            embed.add_field(name="<:stone:1082728403104444498> • Pierre :", value=data[id]['Inventory']["Stone"], inline=True)
                            xpDashes = 25
                            to_next_level_2 = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))
                            dashConvert2 = int(to_next_level_2 / xpDashes)
                            currentDashes2 = int(data[id]['Xp'] / dashConvert2)
                            remain2 = xpDashes - currentDashes2
                            xpDisplay2 = '━' * currentDashes2
                            remainingDisplay2 = '᲼' * remain2
                            percent2 = f"{round(data[id]['Xp'])}/{round(to_next_level_2)}"
                            space2 = '᲼' * int((len(xpDisplay2) + len(remainingDisplay2)) / 2)
                            embed.add_field(name="Rareté :", value="⚫ • Commun", inline=True)
                            embed.add_field(name="Points de Mineur :", value=f"**{round(data[id]['Miner Points'], 2)}**", inline=True)
                            embed.add_field(name="XP :", value=f"**{data[id]['Level']}|{xpDisplay2}◈**{remainingDisplay2}**|{data[id]['Level'] + 1}**\n{space2}**{percent2}**", inline=False)
                            embed.set_footer(text=f"+{xx}xp")
                            await ctx.send(embed=embed)
                            await ctx.message.delete()
                            
            else:
                
                embed = discord.Embed(title="Test Anti-AFK", description="Vous avez été temporairement banni du c!work.\nPour faire une demande de débannissement, veuillez envoyer un message à <@809412081358733332>", color=0xCD2323)
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed.set_footer(text="Votre id a été enregistré dans la liste des potentiels personnes utilisant un système de farming automatique. Votre cas sera traité et passible d'une pénalisation.")
                await ctx.reply(embed=embed)
                
        elif EnumerateArg("lj", "lumberjack"):
            
                if CheckIfIsBanned():
                    if await AfkTest():
                        to_next_level = int(10 * (int(data[id]["Lj Level"] / 2) * data[id]["Lj Level"]))
                        await Mining(ctx, id, woods, data, to_next_level, "lj", cc)
            
        else:
            work_embed = discord.Embed(title="just Hervey 💎 | ⌛ WORK ⌛", description="Bienvenue dans le c!work, ici vous pouvez travailler dans les différents métiers disponible en jeu.", color=0xEEA30D)
            work_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            work_embed.add_field(name="⛏ • Points de Mineur :", value=round(data[id]["Miner Points"]), inline=True)
            work_embed.add_field(name="🪓 • Points de Bûcheron :", value=data[id]["Lj Points"], inline=True)
            work_embed.add_field(name="```c!work mine``` ou ```c!work m```", value="Vous permet de travailler le métier de mineur.", inline=False)
            work_embed.add_field(name="```c!work lumberjack``` ou ```c!work lj```", value="Vous permet de travailler le métier de bûcheron.", inline=False)
            work_embed.set_footer(text="Différents sous-métiers sont disponibles hors de la commande c!work, pour avoir la liste de toutes les commande, faites c!help.")
            await ctx.send(embed=work_embed)