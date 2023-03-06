import json, discord, random, asyncio
from assets.items_price import item_shop_price, item_shop_price_2
from assets.casino_prices import rewards, rewards_mineur

async def CheckSign(ctx, id):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    c = False
    
    for key in data.keys():
        if key == id:
            c = True
            return 0

    if not c:
        embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
        return 1
    
def EnumerateTickets():
    
    tickets = {
        "Ticket": {
            "id": 0,
            "price": 250,
            "points": 0,
            "tickets": 0
        },
        "Miner Ticket": {
            "id": 1,
            "price": 0,
            "points": 10000,
            "tickets": 1
        }
    }
    
    f = list()
    for t, da in tickets.items():
        for c, v in da.items():
            if c == "id": __id__ = v
            if c == "price": __price__ = v
            if c == "points": __points__ = v
            if c == "tickets": __tickets__ = v
        f.append([t, __id__, __price__, __points__, __tickets__])
        
    return f


async def Casino(ctx, arg):

    id = str(ctx.author.id)
    l = 0
    l_ = 0
    loots = {
        ":pick:": 75,
        ":heavy_dollar_sign:": 120,
        ":moneybag:": 100,
        ":gem:": 85,
        ":seven:": 75,
        ":question:": 100
    }
    minor_loots = {
        ":test_tube:": 100,
        ":scroll:": 50
    }
    line_0 = []
    line_1 = []
    line_2 = []
    lines = [line_0, line_1, line_2]

    table = """
╔═══╦☰╦═══╦☰╦═══╦☰╦═══╗
║       ║ 1 ║      ║ 2 ║     ║ 3 ║       ║
║       ╠ 4 ╣      ╠ 5 ╣     ╠ 6 ╣       ║
║       ║ 7 ║      ║ 8 ║     ║ 9 ║       ║
╚═══╩☰╩═══╩☰╩═══╩☰╩═══╝
"""
    table_ = table
    table__ = table
    table___ = table
    
    minor_table = """
╔═══╦☰╦═══╗
║         ║ 1 ║      ║
║         ╠ 2 ╣      ║
║         ║ 3 ║      ║
╚═══╩☰╩═══╝
"""
    minor_table_ = minor_table
    minor_table__ = minor_table
    minor_table___ = minor_table
    
    with open("assets/player_data.json") as data:
        data = json.load(data)

    if not arg:
        
        casino_embed = discord.Embed(title="just Hervey 💎 | 🍀 CASINO 🍀", description="Bienvenue dans le casino, ici vous pouvez acheter des tickets afin de tenter votre chance, et de gagner le gros lot !\n\n```c!casino shop```  Afficher les différents types de tickets et leur prix.\n```c!casino buy <montant> <id tu ticket>```  Permet d'acheter des tickets, les id des tickets peuvent être consultés en faisant la commande `c!casino shop`.\n```c!casino roll <id du ticket>```  Vous permet d'utiliser vos tickets et de jouer au casino. Les id des tickets peuvent être consultés en faisant la commande `c!casino shop`.", color=0x0B9629)
        casino_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        casino_embed.add_field(name="", value="", inline=False)
        casino_embed.add_field(name="🎟 • Tickets :", value=data[id]["Ticket"], inline=False)
        casino_embed.add_field(name="🎫 • Tickets de Mineur :", value=data[id]["Miner Ticket"], inline=False)
        casino_embed.set_footer(text="Dans de futures mises à jour, plusieurs raretés de tickets à des prix différents seront disponibles !")
        await ctx.send(embed=casino_embed)
        
    elif arg[0] == "roll":

        if await CheckSign(ctx, id) == 0:  
            async def CheckArg():
                
                try: 
                    vi = arg[1]
                except: 
                    await ctx.reply("Veuillez entrer une valeur correcte après le **roll**.\n**c!casino roll <id du ticket>**. Pour voirs les id des tickets, faites **c!casino shop**")
                    return False
                else:
                    try: 
                        vi = int(vi)
                    except:
                        await ctx.reply("Veuillez entrer une valeur correcte après le **roll**.\n**c!casino roll <id du ticket>**. Pour voirs les id des tickets, faites **c!casino shop**")
                        return False
                    else:
                        try:
                            if vi < 0:
                                0 / 0
                            dta = EnumerateTickets()
                            dta = dta[vi]
                        except:
                            await ctx.reply("Veuillez inscrire un id valide.\n**c!casino buy** ***<montant>*** **<id du ticket>**. Pour voir les id des tickets, faites **c!casino shop**.")
                            return False
                        else:
                            return dta

            dta_ = await CheckArg()
            
            if dta_:
                
                tid = dta_[1]
                tname = dta_[0]
                
                if not (data[id][tname] >= 1) :
                    await ctx.reply(f"Vous n'avez pas assez de {tname} pour pouvoir jouer.\n{tname} actuels : **{data[id][tname]}**\nPour voir le prix des tickets, vous pouvez éxécuter la commande **c!casino shop**.")
                else:
                    
                    if tid == 0:
                        for line in lines:
                            l_ += 1

                            if line != line_0:
                                for i in range(3):
                                    table__ = table__.replace(str(l + 1 + i), lines[(l_ - 2)][i])
                                    
                                table_ = table__
                                table = table__
                                

                            for i in range(3):
                                line.append(list(random.choices(*zip(*loots.items())))[0])
                            u = 0
                            for loot in line:
                                l += 1
                                u += 1
                                table = table.replace(str(u), loot)
                                table_ = table.replace(str(u), loot)
                            for i in range(10):
                                table_ = table_.replace(str(i), "      ")

                            if line == line_0:
                                casino_edit = await ctx.send(table_)
                            else:
                                if line == line_2:
                                    for i in range(3):
                                        table___ = table___.replace(str(i + 1), line_2[i])
                                        table___ = table___.replace(str(i + 4), line_1[i])
                                        table___ = table___.replace(str(i + 7), line_0[i])
                                    table_ = table___
                                await casino_edit.edit(content=table_)
                            
                            await asyncio.sleep(1)

                        win_line = tuple(line_1)
                        c = False
                        with open("assets/player_data.json") as data:
                            data = json.load(data)
                        for k, v in rewards.items():
                            if k == win_line:
                                c = True
                                if "Money" in v:
                                    if not type(v["Money"]) is list:
                                        data[id]["Money"] += v["Money"]
                                        m = v["Money"]
                                    else:
                                        m = random.randint(v["Money"][0], v["Money"][1])
                                        data[id]["Money"] += m

                                    for key in v["Description"].keys():
                                        title = key

                                    with open("assets/player_data.json", 'w') as d:
                                        json.dump(data, d, indent=4)

                                    money_embed = discord.Embed(title=f"{title} Vous avez gagné !", description=f"+ **{m}**€", color=0x278b5b)
                                    money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                    money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                                    money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                    money_embed.add_field(name="Tickets :", value=data[id]['Ticket'], inline=False)
                                    await ctx.reply(embed=money_embed)

                                elif "Item" in v:
                                    if not v["Item"] in data[id]["Inventory"]["P Item"]:
                                        data[id]["Inventory"]["P Item"].append(v["Item"])

                                        for key in v["Description"].keys():
                                            title = key

                                        with open("assets/player_data.json", 'w') as d:
                                            json.dump(data, d, indent=4)
                                            
                                        money_embed = discord.Embed(title=f"{title} Vous avez gagné !", description=f"{item_shop_price_2[v['Item']]['Name']}", color=0x278b5b)
                                        money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                        money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                                        money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                        money_embed.add_field(name="Tickets :", value=data[id]['Ticket'], inline=False)
                                        await ctx.reply(embed=money_embed)
                                    
                                    else:
                                        await ctx.reply("Vous possédez déjà cet objet !")

                                elif "Rank" in v:
                                    if not v["Rank"] in data[id]['Inventory']["P Rank"]:
                                        data[id]['Inventory']["P Rank"].append(v["Rank"])

                                        for key in v["Description"].keys():
                                            title = key

                                        with open("assets/player_data.json", 'w') as d:
                                            json.dump(data, d, indent=4)

                                        money_embed = discord.Embed(title=f"{title} Vous avez gagné !", description=f"{item_shop_price[v['Rank']]['Name']}", color=0x278b5b)
                                        money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                        money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                                        money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                        money_embed.add_field(name="Tickets :", value=data[id]['Ticket'], inline=False)
                                        await ctx.reply(embed=money_embed)
                                        
                                    else:
                                        await ctx.reply("Vous possédez déjà ce grade !")

                        if not c:
                            money_embed = discord.Embed(title=f"Vous n'avez malheureusement pas gagné...", color=0x8c2121)
                            money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                            money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                            money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                            money_embed.add_field(name="Tickets :", value=data[id]['Ticket'], inline=False)
                            await ctx.reply(embed=money_embed)
                            
                    elif tid == 1:
                        
                        rew = dict()
                        for i in range(5):
                            rew[str(i)] = list(random.choices(*zip(*minor_loots.items())))[0]
                            
                        for i in range(3):
                            for k, v in rew.items():
                                if k == str(i + 2):
                                    minor_table = minor_table.replace(str(i + 1), v)
                                    
                        casinomes = await ctx.send(minor_table)
                        await asyncio.sleep(1)
                        
                        for i in range(3):
                            for k, v in rew.items():
                                if k == str(i + 1):
                                    minor_table_ = minor_table_.replace(str(i + 1), v)
                        
                        await casinomes.edit(content=minor_table_)
                        await asyncio.sleep(1)
                        
                        for i in range(3):
                            for k, v in rew.items():
                                if k == str(i):
                                    minor_table__ = minor_table__.replace(str(i + 1), v)
                                    
                        await casinomes.edit(content=minor_table__)
                        await asyncio.sleep(1)
                        
                        for k, v in rew.items():
                            if k == "1":
                                win = v
                        
                        data[id]['Miner Ticket'] -= 1
                        
                        for k, v in rewards_mineur.items():
                            wxp = None
                            wplan = None
                            if win == k:
                                for k_, v_ in v.items():
                                    if k_ == "Description": desc = v_
                                    elif k_ == "Xp": wxp = random.randint(v_[0], v_[1])
                                    elif k_ == "Plan": wplan = list(random.choices(*zip(*v_.items())))[0]
                                break
                                    
                        if wxp is not None:
                            
                            to_next_level_2 = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))
                            data[id]["Xp"] += wxp
                            if data[id]['Xp'] >= to_next_level_2:
                                data[id]['Level'] += 1
                                data[id]['Xp'] -= to_next_level_2
                                to_next_level_2 = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))
                                embed = discord.Embed(title=f"**GG**, vous avez atteint le niveau **{data[id]['Level']}** !", description=f"XP nécessaire pour passer au prochain niveau : **{to_next_level_2}xp**", color=0x56860e)
                                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                embed.set_image(url="https://i.ibb.co/wyYCHVR/level-up.png")
                                await ctx.send(embed=embed)
                                
                            sec = f"Vous avez gagné `{wxp}` points d'expérience !"
                            xpDashes = 25
                            dashConvert2 = int(to_next_level_2 / xpDashes)
                            currentDashes2 = int(data[id]['Xp'] / dashConvert2)
                            remain2 = xpDashes - currentDashes2
                            xpDisplay2 = '━' * currentDashes2
                            remainingDisplay2 = '᲼' * remain2
                            percent2 = f"{round(data[id]['Xp'])}/{round(to_next_level_2)}"
                            space2 = '᲼' * int((len(xpDisplay2) + len(remainingDisplay2)) / 2)
                            d2 = f"**{data[id]['Level']}|{xpDisplay2}◈**{remainingDisplay2}**|{data[id]['Level'] + 1}**\n{space2}**{percent2}**"
                            d1 = "Niveau :"
                                
                        if wplan is not None:
                            data[id]["Inventory"]["Plans"].append(wplan)
                            sec = f"Vous avez gagné le plan n°`{wplan}` !\nFaites `c!forge recipes` pour voir votre nouveau plan !"
                                

                        with open("assets/player_data.json", 'w') as d:
                            json.dump(data, d, indent=4)
                            
                        win_embed = discord.Embed(title=desc, description=sec, color=0x278b5b)
                        win_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        win_embed.add_field(name=d1, value=d2, inline=False)
                        win_embed.add_field(name="Tickets de mineur :", value=data[id]['Miner Ticket'], inline=False)
                        await ctx.reply(embed=win_embed)
                        

    elif arg[0] == "shop":
     
        embed = discord.Embed(title="🏆 | Casino Shop", description="Pour acheter un des tickets, faites la commande `c!casino buy <nombre de ticket> <id du ticket>`. Ex : `c!casino buy 5 0` permet d'aceheter **5 tickets classiques**", color=0x537935)
        embed.add_field(name="🎟 • Ticket Classique (0)", value="Permet de lancer un casino classique ou de fabriquer des tickets spéciaux. 250€ l'unité.", inline=False)
        embed.add_field(name="🎫 • Ticket de Mineur (1)", value="Permet de lancer un casino du mineur. 1 ticket classique + 10000 Points de Mineur l'unité.", inline=False)
        await ctx.reply(embed=embed)

    elif arg[0] == "buy":
        if await CheckSign(ctx, id) == 0:
            try:
                n = int(arg[1])
                
            except:
                await ctx.reply("Veuillez inscrire un montant valide.\n**c!casino buy** ***<montant>*** **<id du ticket>**. Pour voir les prix des tickets, faites **c!casino shop**.")
                
            else:

                if n <= 0:
                    await ctx.reply("Veuillez au minimum acheter 1 ticket !")

                else:
                    
                    try:
                        n2 = int(arg[2])
                        if n2 < 0:
                            0 / 0
                        dta = EnumerateTickets()
                        dta = dta[n2]
                        
                    except:
                        await ctx.reply("Veuillez inscrire un id valide.\n**c!casino buy** ***<montant>*** **<id du ticket>**. Pour voir les id des tickets, faites **c!casino shop**.")

                    else:

                        tname = dta[0]
                        tprice = dta[2] * n
                        tpoints = dta[3] * n
                        ttickets = dta[4] * n

                        with open("assets/player_data.json") as data:
                            data = json.load(data)

                        if data[id]["Money"] >= tprice:
                            
                            if data[id]["Miner Points"] >= tpoints:
                                
                                if data[id]["Ticket"] >= ttickets:
                            
                                    data[id]["Money"] -= tprice
                                    data[id]["Miner Points"] -= tpoints 
                                    data[id]["Ticket"] -= ttickets
                                    data[id][tname] += n
                                    with open("assets/player_data.json", 'w') as d:
                                        json.dump(data, d, indent=4)
                                    money_embed = discord.Embed(title=f"Vous avez acheté **{n} {tname}** avec succès !", description=f"Pour utilisez vos tickets, faites `c!casino roll <id du ticket>`.", color=0x5455b0)
                                    money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                    money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                                    money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                    money_embed.add_field(name="Points de Mineur :", value=data[id]['Miner Points'], inline=False)
                                    money_embed.add_field(name="Tickets Classiques :", value=data[id]["Ticket"], inline=False)
                                    await ctx.reply(embed=money_embed)
                                    
                                else:
                                    await ctx.reply(f"Vous n'avez pas assez de tickets classiques pour acheter **{n} {tname}** !\nTickets nécéssaires : **{ttickets}**\nTickets actuels : **{data[id]['Ticket']}**")

                            else:
                                await ctx.reply(f"Vous n'avez pas assez de Points de Mineur pour acheter **{n} {tname}** !\nPoints nécéssaires : **{tpoints}**\nPoints actuels : **{data[id]['Miner Points']}**")

                        else:
                            await ctx.reply(f"Vous n'avez pas assez d'argent pour acheter **{n} {tname}** !\nPrix : **{tprice}**\nVotre Argent : **{data[id]['Money']}**")

    else:
        casino_embed = discord.Embed(title="just Hervey 💎 | 🍀 CASINO 🍀", description="Bienvenue dans le casino, ici vous pouvez acheter des tickets afin de tenter votre chance, et de gagner le gros lot !\n\n```c!casino shop```  Afficher les différents types de tickets et leur prix.\n```c!casino buy <montant> <id tu ticket>```  Permet d'acheter des tickets, les id des tickets peuvent être consultés en faisant la commande `c!casino shop`.\n```c!casino roll <id du ticket>```  Vous permet d'utiliser vos tickets et de jouer au casino. Les id des tickets peuvent être consultés en faisant la commande `c!casino shop`.", color=0x0B9629)
        casino_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        casino_embed.add_field(name="", value="", inline=False)
        casino_embed.add_field(name="🎟 • Tickets :", value=data[id]["Ticket"], inline=False)
        casino_embed.add_field(name="🎫 • Tickets de Mineur :", value=data[id]["Miner Ticket"], inline=False)
        casino_embed.set_footer(text="Dans de futures mises à jour, plusieurs raretés de tickets à des prix différents seront disponibles !")
        await ctx.send(embed=casino_embed)
