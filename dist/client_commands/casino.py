import json, discord, random, asyncio
from assets.items_price import item_shop_price, item_shop_price_2
from assets.casino_prices import rewards

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


async def IfUserHasTicket(ctx, id):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    if data[id]["Ticket"] >= 1:
        data[id]["Ticket"] -= 1
        with open("assets/player_data.json", 'w') as d:
            json.dump(data, d, indent=4)
        return 0
    else:
        await ctx.reply("Vous n'avez pas assez de ticket pour jouer.\n**c!casino buy** ***montant*** pour acheter des tickets. (**150€** --> **1** ticket)")
        return 1


async def Casino(ctx, arg):

    id = str(ctx.author.id)
    l = 0
    l_ = 0
    loots = [":pick:", ":heavy_dollar_sign:", ":moneybag:", ":gem:", ":seven:", ":question:"]
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
    
    with open("assets/player_data.json") as data:
        data = json.load(data)

    if not arg:
        
        casino_embed = discord.Embed(title="just Hervey 💎 | 🍀 CASINO 🍀", description="Bienvenue dans le casino, ici vous pouvez acheter des tickets afin de tenter votre chance, et de gagner le gros lot !\n\n```c!casino rewards```  Afficher les différents lots pouvant être gagnés avec la commande c!casino.\n```c!casino buy (<montant>)```  Permet d'acheter des tickets, les id des tickets peuvent être consultés en faisant la commande `c!caison rewards`.\n```c!casino roll (nombre de tours)```  Vous permet d'utiliser vos tickets et de jouer au casino. Si vous possédez le Lucky Hammer, vous pouvez préciser un nombre de tours (5max) à faire en même temps.", color=0x0B9629)
        casino_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        casino_embed.add_field(name="", value="", inline=False)
        casino_embed.add_field(name="🎟 • Tickets :", value=data[id]["Ticket"], inline=False)
        casino_embed.add_field(name="🎫 • Tickets spécials mineur :", value=data[id]["Miner Ticket"], inline=False)
        casino_embed.set_footer(text="Dans de futures mises à jour, plusieurs raretés de tickets à des prix différents seront disponibles !")
        await ctx.send(embed=casino_embed)
        
    elif arg[0] == "roll":

        if await CheckSign(ctx, id) == 0:
            if await IfUserHasTicket(ctx, id) == 0:
                
                async def CheckArg():
                    
                    global iterations
                    
                    iterations = 1
                
                    try: 
                        vi = arg[1]
                    except: 
                        return True
                    else:
                        try: 
                            vi = int(vi)
                        except:
                            await ctx.reply("Veuillez entrer une valeur correcte après le **roll**.")
                            return False
                        else:
                            if not (1 <= vi <= 5):
                                await ctx.reply(f'Veuillez entrer une valeure entre **1** et **5** !\n--> **{vi}**')
                                return False
                            else:
                                if 2 not in data[id]["Inventory"]["P Forge"]:
                                    await ctx.reply("Vous devez posséder le **Lucky-Hammer** afin de pouvoir utiliser le c!loto plus d'une fois en même temps.\n**c!shop forge** pour l'acheter ou **c!casino roll** sans arguments pour relancer la commande.")
                                    return False
                                else:
                                    return True
                                    iterations = vi

                if await CheckArg():
                    
                    if not (data[id]['Ticket'] >= iterations) :
                        await ctx.reply(f"Vous n'avez pas assez de ticket pour pouvoir utiliser la commande c!casino **{iterations}** fois.\nTickets actuels : **{data[id]['Ticket']}**")
                    else:
                        
                        for it in range(iterations):

                            for line in lines:
                                l_ += 1

                                if line != line_0:
                                    for i in range(3):
                                        table__ = table__.replace(str(l + 1 + i), lines[(l_ - 2)][i])
                                        
                                    table_ = table__
                                    table = table__
                                    

                                for i in range(3):
                                    line.append(random.choice(loots))
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


    elif arg[0] == "rewards":
        embed = discord.Embed(title="🎟 | Casino Rewards", color=0x537935)
        for k, v in rewards.items():
            for k_, v_ in v["Description"].items():
                embed.add_field(name=k_, value=v_, inline=False)
        await ctx.reply(embed=embed)

    elif arg[0] == "buy":
        if await CheckSign(ctx, id) == 0:
            try:
                n = int(arg[1])

                if n <= 0:
                    await ctx.reply("Fais pas le chaud mon reuf j'ai tout prévu")

                else:

                    with open("assets/player_data.json") as data:
                        data = json.load(data)

                    if data[id]["Money"] >= 150 * n:
                        data[id]["Money"] -= 150 * n
                        data[id]["Ticket"] += n
                        with open("assets/player_data.json", 'w') as d:
                            json.dump(data, d, indent=4)
                        money_embed = discord.Embed(title=f"Vous avez acheté {n} tickets avec succès !", description=f"-**{150 * n}**€", color=0x5455b0)
                        money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                        money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                        money_embed.add_field(name="Tickets :", value=data[id]["Ticket"], inline=False)
                        await ctx.reply(embed=money_embed)


                    else:
                        await ctx.reply(f"Vous n'avez pas assez d'argent pour acheter {n} tickets !\nPrix : {150 * n}\nVotre Argent : {data[id]['Money']}")

            except:
                await ctx.reply("Veuillez inscrire un montant valide.\n**c!casino buy** ***montant***. (*150€** --> **1** ticket)")

    else:
        d = await ctx.reply("Veuillez préciser un argument valide !\nc!casino (*rewards* / *buy montant*)")
        await d.delete(delay=15)
