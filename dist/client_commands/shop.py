import discord, json

async def Shop(ctx, buy, cc):

    with open("data/player_data.json") as data:
        data = json.load(data)
            
    id = str(ctx.author.id)
    c = True

    for key in data.keys():
        if key == id:
            c = False

    if c:
        await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")

    else:

        s=discord.Embed(title="CHOIX DE LA BOUTIQUE", description="Ici, vous pouvez choisir la boutique dans laquelle vous voulez aller.", color=0x116792)
        s.add_field(name="**🎭 Boutique de Grade 🎭**", value="c!shop **rank** pour accéder à la boutique.", inline=False)
        s.add_field(name="**⚔ Boutique d'Objet ⚔**", value="c!shop **item** pour accéder à la boutiuqe.", inline=True)
        s.add_field(name="**😴 Créer ta Boutique 😴**", value="Bientôt disponible !", inline=False)
        s.set_footer(text="Chaque boutique vend des articles différents.")

        if not buy:
            await ctx.reply(embed=s)

        elif buy[0] == "rank":

            rank_embed=discord.Embed(title="**🎭 BOUTIQUE DES GRADES 🎭**", description="Ici, vous pouvez acheter les grades qui vous plaisent.", color=0x963636)
            rank_embed.add_field(name="**1** - GRADE | 😮-Mineur Débutant :", value="Prix : 1,000€", inline=False)
            rank_embed.add_field(name="**2** - GRADE | 😋-Mineur Amateur :", value="Requiert : Métier de Mineur Niv. 10\nPrix : 2,000€", inline=False)
            rank_embed.add_field(name="**3** - GRADE | ⛏-Mineur Affirmé :", value="Requiert : Métier de Mineur Niv. 20\nPrix : 5,000€", inline=False)
            rank_embed.add_field(name="**4** - GRADE | 😎-Mineur Professionel :", value="Requiert : Métier de Mineur Niv. 30\nPrix : 10,000€", inline=True)
            rank_embed.add_field(name="**5** - GRADE | 🐱‍🏍-Mineur Légendaire :", value="Requiert : Métier de Mineur Niv. 50\nPrix : 50,000€", inline=True)
            rank_embed.add_field(name="**6** - GRADE | 💎-Géologue :", value="Requiert : Métier de Mineur Niv. 50\nPrix : 150,000€", inline=True)
            rank_embed.add_field(name="**7** - GRADE | <:sacredstone:882234999145922621>-Récolteur de cristaux :", value="Requiert : Métier de Mineur Niv. 75\nPrix : 100,000€", inline=True)
            rank_embed.add_field(name="**8** - GRADE | 🧚‍♂️-Mineur Mythique :", value="Requiert : Métier de Mineur Niv. 75\nPrix : 500,000€", inline=True)
            rank_embed.add_field(name="**9** - GRADE | 👑-Mineur Suprême :", value="Requiert : Métier de Mineur Niv. 100\nPrix : 1,000,000€", inline=True)
            rank_embed.add_field(name="**10** - GRADE | <:drogue:882314468086931466>-DROGUÉ :", value="Requiert : Métier de Mineur Niv. 20\nPrix : 100 Charbons à Coke", inline=True)
            rank_embed.set_footer(text="Pour acheter un grade, faites la commande c!shop rank buy NUMÉRO DU GRADE.")

            try:
                if buy[1] == "buy":
                    try:
                        if int(buy[2]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                            buy_item = cc.item_shop_price[int(buy[2])]

                            if data[id]['Level'] >= buy_item["Level"]:

                                if data[id]['Money'] >= buy_item["Money"]:

                                    if int(buy[2]) not in data[id]['Inventory']["P Rank"]:

                                        if buy_item["Price"]:
                                            data[id]['Inventory'][buy_item["Price"][0]] -= buy_item["Price"][1]

                                        data[id]['Money'] -= buy_item["Money"]
                                        data[id]['Inventory']["P Rank"].append(int(buy[2]))

                                        with open("data/player_data.json", 'w') as d:
                                            data[id]['Money'] = round(data[id]['Money'], 2)
                                            json.dump(data, d, indent=4)

                                        money_embed = discord.Embed(title=f"Vous avez acheter le grade n°{buy[2]} avec succès (c!inventory equip rank {buy[2]} pour équiper votre rank !) !", description=f"-**{buy_item['Money']}**€", color=0x5455b0)
                                        money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                        money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                                        money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                        await ctx.reply(embed=money_embed)
                                        
                                    else:
                                        await ctx.reply("Vous possédez déjà ce grade !")
                                else:
                                    await ctx.reply("Vous n'avez pas l'argent requis !")
                            else:
                                await ctx.reply("Vous n'avez pas le niveau requis !")
                        else:
                            await ctx.reply("Veuillez choisir une valeure correcte !")
                            print("Hors du int")
                    except:
                        await ctx.reply("Veuillez choisir une valeure correcte !")
                else:
                    await ctx.reply(embed=rank_embed)
            except:
                await ctx.reply(embed=rank_embed)

        elif buy[0] == "item":

            for_changes_prices = cc.item_shop_price_2
            for_changes_prices[8]["Price"] = ["Diamond", data[id]['Inventory']["Item Limit"] * 5]
            for_changes_prices[8]["Money"] = data[id]['Inventory']["Item Limit"] * 100000

            item_embed=discord.Embed(title="⚔ **BOUTIQUE D'OBJET** ⚔", description="Ici, vous pouvez acheter les objets qui vous plaisent.", color=0x540788)
            item_embed.add_field(name="**1** - 🧲|Pioche en Fer : **10**Fer, **2,000**€", value="Vous avez **10%** de chance supplémentaire de miner des minerais.", inline=False)
            item_embed.add_field(name="**2** - 🥇|Pioche en Or : **10**Or, **7,500**€", value="Augmente la revente de vos minerais de **10%**.", inline=True)
            item_embed.add_field(name="**3** - 🔥|Pioche de Magma : **10**Pierre de Magma, **1,000**€", value="Vous ne perdez plus d'**argent** ni d'**xp** à cause de la Roche Magmatique.", inline=True)
            item_embed.add_field(name="**4** - ⛏|Alliage en Platine : **10**Platine, **2,000**€", value="Vous permet d'améliorer votre pioche pour qu'elle puisse miner le **rubis**, le **saphir** et l'**émeraude**.", inline=True)
            item_embed.add_field(name="**5** - 👨‍🔬|PIOCHE DU CHINOIS : **10**Joseph, **100,000**€.", value="GG, vous avez la meilleure pioche du jeu (ne sert à rien).", inline=True)
            item_embed.add_field(name="**6** - ✖|Pioche de multiplication : **30**Cobaltes, **50,000**€.", value="Duplique les minerais que vous minez.", inline=True)
            item_embed.add_field(name="**7** - 🕵️‍♂️|Pioche du maraudeur : **1000**Pierres, **25,000**€.", value="Vous ne minerez plus de débrits (ouf).", inline=True)
            item_embed.add_field(name=f"**8** - 👾|Multi-Pioche : **{data[id]['Inventory']['Item Limit'] * 5}**Diamant, **{data[id]['Inventory']['Item Limit']}00,000**€.", value="Vous permet d'équiper 2 pioches à la fois.", inline=True)
            item_embed.set_footer(text="Pour acheter un objet, faites la commande c!shop item buy NUMÉRO DE L'ITEM.")

            try:
                if buy[1] == "buy":
                    try:
                        if int(buy[2]) in [1, 2, 3, 4, 5, 6, 7, 8]:
                            buy_item = cc.item_shop_price_2[int(buy[2])]

                            if data[id]['Inventory'][buy_item["Price"][0]] >= buy_item["Price"][1]:

                                if data[id]['Money'] >= buy_item["Money"]:

                                    if int(buy[2]) not in data[id]['Inventory']["P Item"]:

                                        if not (int(buy[2]) == 4 and data[id]['Inventory']["Platinium Alliage"]):

                                            data[id]['Money'] -= buy_item["Money"]
                                            data[id]['Inventory'][buy_item["Price"][0]] -= buy_item["Price"][1]

                                            with open("data/player_data.json", 'w') as d:

                                                if int(buy[2]) == 4:
                                                    data[id]['Inventory']["Platinium Alliage"] = True
                                                    data[id]['Money'] = round(data[id]['Money'], 2)
                                                    json.dump(data, d, indent=4)
                                                    money_embed = discord.Embed(title=f"Vous avez acheter l'alliage n°{buy[2]} avec succès !", description=f"-**{buy_item['Money']}**€", color=0x5455b0)
                                                    money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                    money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                                                    money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                                    await ctx.reply(embed=money_embed)
                                                    
                                                
                                                elif int(buy[2]) == 8:
                                                    data[id]['Inventory']["Item Limit"] += 1
                                                    data[id]['Money'] = round(data[id]['Money'], 2)
                                                    json.dump(data, d, indent=4)
                                                    money_embed = discord.Embed(title=f"Vous avez acheter l'amélioration n°{buy[2]} avec succès !", description=f"-**{buy_item['Money']}**€", color=0x5455b0)
                                                    money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                    money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                                                    money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                                    await ctx.reply(embed=money_embed)

                                                else:
                                                    data[id]['Inventory']["P Item"].append(int(buy[2]))
                                                    data[id]['Money'] = round(data[id]['Money'], 2)
                                                    json.dump(data, d, indent=4)
                                                    money_embed = discord.Embed(title=f"Vous avez acheter l'item n°{buy[2]} avec succès (c!inventory equip item {buy[2]} pour équiper votre item) !", description=f"-**{buy_item['Money']}**€", color=0x5455b0)
                                                    money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                    money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
                                                    money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                                    await ctx.reply(embed=money_embed)

                                        else:
                                            await ctx.reply("Vous possédez déjà cet item !")
                                    else:
                                        await ctx.reply("Vous possédez déjà cet item !")
                                else:
                                    await ctx.reply("Vous n'avez pas l'argent requis !")
                            else:
                                await ctx.reply("Vous n'avez pas assez de ressources !")
                        else:
                            await ctx.reply("Veuillez choisir une valeure correcte !")
                    except:
                        await ctx.reply("Veuillez choisir une valeure correcte !")
                else:
                    await ctx.reply(embed=item_embed)

            except:
                    await ctx.send(embed=item_embed)

        else:
            await ctx.reply(embed=s)