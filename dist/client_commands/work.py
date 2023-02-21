import discord, json, random
from assets.items_price import item_shop_price, item_shop_price_2
from assets.minerals_data import minerals

async def Mining(ctx, id, minerals, data, to_next_level, r):

    f = False
    
    print(r)

    for k, v in minerals.items():
        
        if v["Min"] <= r <= v["Max"]:
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
    if 11 in data[id]["Inventory"]["MP"]:
        mineral_xp = mineral_xp + (mineral_xp / 100 * 10)
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
        if random.choice[True, False]:
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
                                if random.choice[True, False]:
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
                                if random.choice[True, False]:
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
                            if random.choice[True, False]:
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
                        if random.choice[True, False]:
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
