import discord, json
from assets.items_price import item_shop_price, item_shop_price_2, item_shop_price_3

async def Shop(ctx, buy):

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

        s=discord.Embed(title="CHOIX DE LA BOUTIQUE", description="Ici, vous pouvez choisir la boutique dans laquelle vous voulez aller.", color=0x116792)
        s.add_field(name="**🎭 Boutique de Grade 🎭**", value="c!shop **rank** pour accéder à la boutique.", inline=False)
        s.add_field(name="**⛏ Boutique du Mineur ⛏**", value="c!shop **mine** pour accéder à la boutiuqe.", inline=False)
        s.add_field(name="**🔨 Boutique du Forgeron 🔨**", value="Boutique accesible à partir du niveau `15`. c!shop **forge** pour accéder à la boutique.", inline=False)
        s.add_field(name="**🪓 Boutique du Bûcheron 🪓**", value="Bientôt disponible !", inline=False)
        s.set_footer(text="Chaque boutique vend des articles différents.")

        if not buy:
            await ctx.reply(embed=s)

        elif buy[0] == "rank":

            rank_embed=discord.Embed(title="**🎭 BOUTIQUE DES GRADES 🎭**", description="Ici, vous pouvez acheter les grades qui vous plaisent.", color=0x963636)
            rank_embed.add_field(name="**1** - GRADE | 😮 - Débutant :", value="Prix : 1,000€", inline=False)
            rank_embed.add_field(name="**2** - GRADE | 😋 - Amateur :", value="Prix : 10,000€", inline=True)
            rank_embed.add_field(name="**3** - GRADE | 🤑 -  Affirmé :", value="Prix : 25,000€", inline=True)
            rank_embed.add_field(name="**4** - GRADE | 😎 - Professionel :", value="Prix : 50,000€", inline=True)
            rank_embed.add_field(name="**5** - GRADE | 🐱‍🏍 - Légende :", value="Prix : 100,000€", inline=True)
            rank_embed.add_field(name="**8** - GRADE | 🧚‍♂️ - Mineur Mythique :", value="Prix : 500,000€", inline=True)
            rank_embed.add_field(name="**9** - GRADE | 👑 - N°1 :", value="Prix : 1,000,000€", inline=True)
            rank_embed.add_field(name="**10** - GRADE | <:drogue:882314468086931466>-DROGUÉ :", value="Prix : 100 Charbons à Coke", inline=True)
            rank_embed.add_field(name="**14** - GRADE | 🚮 - Éboueur :", value="Prix : 1000 Débrits", inline=True)
            rank_embed.set_footer(text="Pour acheter un grade, faites la commande c!shop rank buy NUMÉRO DU GRADE.")

            try:
                if buy[1] == "buy":
                    try:
                        if int(buy[2]) in [1, 2, 3, 4, 5, 8, 9, 10, 14]:
                            buy_item = item_shop_price[int(buy[2])]

                            if data[id]['Level'] >= buy_item["Level"]:

                                if data[id]['Money'] >= buy_item["Money"]:

                                    if int(buy[2]) not in data[id]['Inventory']["P Rank"]:

                                        if buy_item["Price"]:
                                            if not data[id]['Inventory'][buy_item["Price"][0]] >= buy_item["Price"][1]:
                                                await ctx.reply(f"Vous n'avez pas assez de ressources !\n{buy_item['Price'][0]} nécéssaires : {buy_item['Price'][1]}\nDans l'inventaire : {data[id]['Inventory'][buy_item['Price'][0]]}")
                                                f = False
                                            else:
                                                data[id]['Inventory'][buy_item["Price"][0]] -= buy_item["Price"][1]
                                                f = True
                                        else: f = True

                                        if f:
                                            data[id]['Money'] -= buy_item["Money"]
                                            data[id]['Inventory']["P Rank"].append(int(buy[2]))

                                            with open("assets/player_data.json", 'w') as d:
                                                data[id]['Money'] = round(data[id]['Money'], 2)
                                                json.dump(data, d, indent=4)

                                            money_embed = discord.Embed(title=f"Vous avez acheter le grade n°{buy[2]} avec succès (c!inventory equip rank {buy[2]} pour équiper votre rank !) !", description=f"-**{buy_item['Money']}**€", color=0x5455b0)
                                            money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                            money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                            money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                            await ctx.reply(embed=money_embed)
                                        
                                    else:
                                        await ctx.reply("Vous possédez déjà ce grade !")
                                else:
                                    await ctx.reply(f"Vous n'avez pas l'argent requis !\nArgent : **{data[id]['Money']}**\nArgent Requis : **{buy_item['Money']}**")
                            else:
                                await ctx.reply("Vous n'avez pas le niveau requis !\nNiveau : **%s**\nNiveau Requis : **%s**" % (data[id]["Level"], buy_item["Level"]))
                        else:
                            await ctx.reply("Veuillez choisir une valeure correcte !")
                            print("Hors du int")
                    except:
                        await ctx.reply("Veuillez choisir une valeure correcte !")
                else:
                    await ctx.reply(embed=rank_embed)
            except:
                await ctx.reply(embed=rank_embed)

        elif buy[0] == "mine":

            item_embed=discord.Embed(title="⚔ **BOUTIQUE D'OBJET** ⚔", description="Ici, vous pouvez acheter les objets qui vous plaisent.", color=0x540788)
            item_embed.add_field(name="**1** - 🧲|Pioche en Fer : **5**Fer, **1,000** Points de Mineur", value="Vous avez **10%** de chance supplémentaire de miner des minerais.", inline=True)
            item_embed.add_field(name="**2** - 🥇|Pioche en Or : **5**Or, **2,500** Points de Mineur", value="Augmente le gain des points de mineur **10%**.", inline=True)
            item_embed.add_field(name="**3** - 🔥|Pioche de Magma : **5**Pierre de Magma, **1,500** Points de Mineur", value="Vous ne perdez plus d'**argent** ni d'**xp** à cause de la Roche Magmatique.", inline=True)
            item_embed.add_field(name="**4** - ⛏|Alliage en Platine : **5**Platine, **2,000** Points de Mineur", value="Vous permet d'améliorer votre pioche pour qu'elle puisse miner le **rubis**, le **saphir** et l'**émeraude**. (n'a pas besoin d'être équipé dans l'inventaire)", inline=True)
            item_embed.add_field(name="**12** - ⛏|Alliage en Obsidienne : **15**Obsidienne, **15,000** Points de Mineur, 20,000€", value="Vous permet d'améliorer votre pioche pour qu'elle puisse miner l'**uranium** et le **plutonium**. (n'a pas besoin d'être équipé dans l'inventaire)", inline=True)
            item_embed.add_field(name="**11** - 🧪|Pioche Expérimentale : **20**Cuivre, **5,000** Points de Mineur, 10,000€.", value=f"Vous gagnez 10{'%'} d'xp supplémentaire en minant.", inline=True)
            item_embed.add_field(name="**5** - 👨‍🔬|PIOCHE DU CHINOIS : **10**Joseph, **10,000** Points de Mineur, 50,000€.", value="GG, vous avez la meilleure pioche du jeu (ne sert à rien).", inline=True)
            item_embed.add_field(name="**13** - GRADE | 💎 - Géologue :", value="Requiert : Métier de Mineur Niv. 50\nPrix : 15,000 Points de Mineur, 75,000€", inline=True)
            item_embed.add_field(name="**14** - GRADE | <:sacredstone:1078401347780608040> - Récolteur de cristaux :", value="Requiert : Métier de Mineur Niv. 75\nPrix : 25,000 Points de Mineur, 100,000€", inline=True)
            item_embed.add_field(name="**6** - ✖|Pioche de multiplication : **25**Cobaltes, **20,000** Points de Mineur, 25,000€.", value=f"A 50{'%'} de dupliquer les minerais que vous minez.", inline=True)
            item_embed.add_field(name="**7** - 🕵️‍♂️|Pioche du maraudeur : **250**Pierres, **15,000** Points de Mineur, 20,000€.", value="Vous ne minerez plus de débrits (ouf).", inline=True)
            item_embed.add_field(name=f"**9** - 👾|Multi-Pioche : **{data[id]['Inventory']['Item Limit'] * 10}**Diamant, **{(data[id]['Inventory']['Item Limit'])*5}0,000**€.", value=f"Vous permet d'équiper {data[id]['Inventory']['Item Limit'] + 1} pioches à la fois. Requier : Métier de Mineur Niv. {data[id]['Inventory']['Item Limit'] * 10} (pour équiper plusieurs pioches, faites __c!inventory equip item__ suivi du numéro des objets séparés d'espaces)", inline=True)
            item_embed.set_footer(text="Pour acheter un objet, faites la commande c!shop mine buy NUMÉRO DE L'ITEM.")
            
            try:
                if buy[1] == "buy":
                    try:
                        if int(buy[2]) in [1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 13, 14]:
                            buy_item = item_shop_price_2[int(buy[2])]
                            
                            if int(buy[2]) == 9:
                                if buy_item["Price"]:
                                    price = buy_item["Price"][1] * data[id]['Inventory']['Item Limit']
                                money = buy_item["Money"] * data[id]['Inventory']['Item Limit']
                                level = buy_item["Level"] * data[id]['Inventory']['Item Limit']
                            else:
                                if buy_item["Price"]:
                                    price = buy_item["Price"][1]
                                money = buy_item["Money"]
                                level = buy_item["Level"]
                                
                            if data[id]["Level"] >= level:
                                
                                if data[id]["Miner Points"] >= buy_item["Miner Points"]:

                                    if (data[id]['Inventory'][buy_item["Price"][0]] >= price) or not buy_item["Price"]:

                                        if data[id]['Money'] >= money:

                                            if int(buy[2]) not in data[id]['Inventory']["P Item"]:

                                                if int(buy[2]) not in data[id]['Inventory']["Alliages"]:

                                                    data[id]['Money'] -= money
                                                    data[id]['Inventory'][buy_item["Price"][0]] -= price

                                                    with open("assets/player_data.json", 'w') as d:

                                                        if int(buy[2]) in [4, 12]:
                                                            data[id]['Inventory']["Alliages"].append(int(buy[2]))
                                                            data[id]['Money'] = round(data[id]['Money'], 2)
                                                            json.dump(data, d, indent=4)
                                                            money_embed = discord.Embed(title=f"Vous avez acheter l'alliage n°{buy[2]} avec succès ! (vous n'avez pas besoin d'équiper cet alliage)", description=f"-**{money}**€", color=0x5455b0)
                                                            money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                            money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                                            money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                                            await ctx.reply(embed=money_embed)
                                                            
                                                        
                                                        elif int(buy[2]) == 9:
                                                            data[id]['Inventory']["Item Limit"] += 1
                                                            data[id]['Money'] = round(data[id]['Money'], 2)
                                                            json.dump(data, d, indent=4)
                                                            money_embed = discord.Embed(title=f"Vous avez acheter l'amélioration n°{buy[2]} avec succès ! (pour équiper plusieurs pioches, faites __c!inventory equip item__ suivi du numéro des objets séparés d'espaces)", description=f"-**{money}**€", color=0x5455b0)
                                                            money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                            money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                                            money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                                            await ctx.reply(embed=money_embed)

                                                        else:
                                                            if not buy_item["Rank"]:
                                                                data[id]['Inventory']["P Item"].append(int(buy[2]))
                                                                money_embed = discord.Embed(title=f"Vous avez acheter l'item n°{buy[2]} avec succès (c!inventory equip item {buy[2]} pour équiper votre item) !", description=f"-**{money}**€", color=0x5455b0)
                                                            else:
                                                                data[id]['Inventory']["P Rank"].append(int(buy[2]))
                                                                money_embed = discord.Embed(title=f"Vous avez acheter le grade n°{buy[2]} avec succès (c!inventory equip rank {buy[2]} pour équiper votre grade) !", description=f"-**{money}**€", color=0x5455b0)
                                                            data[id]['Money'] = round(data[id]['Money'], 2)
                                                            json.dump(data, d, indent=4)
                                                            money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                            money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                                            money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                                            await ctx.reply(embed=money_embed)

                                                else:
                                                    await ctx.reply("Vous possédez déjà cet alliage !")
                                            else:
                                                await ctx.reply("Vous possédez déjà cet item !")
                                        else:
                                            await ctx.reply("Vous n'avez pas l'argent requis !\nArgent : **%s**\nArgent Requis : **%s**" % (data[id]["Money"], buy_item["Money"]))
                                    else:
                                        await ctx.reply(f"Vous n'avez pas assez de ressources !\n**{buy_item['Price'][0]}** nécéssaires : **{price}**\n**{buy_item['Price'][0]}** dans l'inventaire : **{data[id]['Inventory'][buy_item['Price'][0]]}**")
                                else:
                                    await ctx.reply(f"Vous n'avez pas assez de Points de Mineur !\nPoints requis : **{buy_item['Miner Points']}**\nPoints actuels : **{data[id]['Miner Points']}**")
                            else:
                                await ctx.reply("Vous n'avez pas le niveau requis !\nNiveau actuel : **%s**\nNiveau Requis : **%s**" % (data[id]["Level"], level))
                        else:
                            await ctx.reply("Veuillez choisir une valeure correcte !")
                    except:
                        await ctx.reply("Veuillez choisir une valeure correcte !")
                else:
                    await ctx.reply(embed=item_embed)
            except:
                    await ctx.send(embed=item_embed)

        elif buy[0] == "forge":
            
            if data[id]["Level"] >= 15:
            
                forge_embed=discord.Embed(title="**🔨 BOUTIQUE DU FORGERON 🔨**", description="Ici, vous pouvez acheter des objets liés à l'utilisation de la commande c!forge.", color=0xC0712C)
                forge_embed.add_field(name="**1** - 🧲|Marteau Magnétique : **100**Magnétite, **5,000** Points de Forge et 100,000€.", value="Une fois équipé, le cooldown de la forge est réduis de 40%.", inline=True)
                forge_embed.add_field(name="**13** - RANK | 🧔 - Forgeron de renommée : **10,000** Points de Forge.", value="Un grade spécial pour les utilisateurs affirmés de la forge.", inline=True)
                forge_embed.set_footer(text="Pour acheter un objet, faites la commande c!shop forge buy NUMÉRO DE L'OBJET.")
                forge_embed.add_field(name=f"**2** - 🍀|Lucky-Hammer : **25**Lucky Stones, **1,500** Points de Forge, **150,000**€.", value=f"Vous permet de lancer la commande c!casino jusqu'à 5 fois en même temps afin de gagner du temps.", inline=True)
                forge_embed.add_field(name=f"**3** - ☢|Hammer Radioactif : **25**Uranium, Plutonium, Fluorite, et **7,500** Points de Forge.", value=f"Les plans que vous découvrez demandent 5 niveaux en moins afin d'être fabriqués.", inline=True)
                forge_embed.add_field(name=f"**4** - 🔱|Trident de Poséidon : **3**Aigue Marine, **6,000** Points de Forge, **300,000**€.", value=f"Les dieux vous guident, vos chances d'obtenir un plan augmentent de 15%.", inline=True)

                try:
                    if buy[1] == "buy":
                        try:
                            if int(buy[2]) in [1, 11, 2, 3, 4]:
                                buy_item = item_shop_price_3[int(buy[2])]

                                if data[id]['Money'] >= buy_item["Money"]:
                                    
                                    if data[id]["Forge Points"] >= buy_item["Forge Points"]:

                                        if int(buy[2]) not in data[id]['Inventory']["P Forge"]:
                                            
                                            _c_ = True
                                            for k, v in buy_item["Price"].items():
                                                if data[id]["Inventory"][k] < v:
                                                    _c_ = False
                                                    
                                            if _c_:
                                                data[id]['Money'] -= buy_item["Money"]
                                                for k, v in buy_item["Price"].items():        
                                                    data[id]['Inventory'][k] -= v
                                                data[id]["Forge Points"] -= buy_item["Forge Points"]
                                                if not buy_item["Rank"]:
                                                    data[id]['Inventory']["P Forge"].append(int(buy[2]))
                                                else:
                                                    data[id]['Inventory']["P Rank"].append(int(buy[2]))
                                                data[id]['Money'] = round(data[id]['Money'], 2)

                                                with open("assets/player_data.json", 'w') as d:
                                                    json.dump(data, d, indent=4)
                                                    
                                                if buy_item["Money"] > 0:
                                                    money_embed = discord.Embed(title=f"Vous avez acheter l'objet n°{buy[2]} avec succès", description=f"-**{buy_item['Money']}**€\n-**{buy_item['Forge Points']}** Points de Forge", color=0x5455b0)
                                                else:
                                                    money_embed = discord.Embed(title=f"Vous avez acheter l'objet n°{buy[2]} avec succès", description=f"-**{buy_item['Forge Points']}** Points de Forge", color=0x5455b0)
                                                money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                                money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
                                                money_embed.add_field(name="Points de Forge restant:", value=data[id]['Forge Points'], inline=False)
                                                money_embed.set_footer(text="L'objet a été ajouté à votre établi. Pour voir tout les objets de votre établi, faites la commande c!inventory.")
                                                await ctx.reply(embed=money_embed)
                                                
                                            else:
                                                await ctx.reply(f"Vous n'avez pas assez de ressources !\n**{buy_item['Price'][0]}** nécéssaires : **{buy_item['Price'][1]}**\n**{buy_item['Price'][0]}** dans l'inventaire : **{data[id]['Inventory'][buy_item['Price'][0]]}**")
                                        else:
                                            await ctx.reply("Vous possédez déjà ce grade !")                         
                                    else:
                                        await ctx.reply("Vous n'avez pas les Points de Forge requis !\nPoints de Forge : **%s**\nPoints de Forge requis : **%s**" % (data[id]["Forge Points"], buy_item["Forge Points"]))
                                else:
                                    await ctx.reply("Vous n'avez pas l'argent requis !\nArgent : **%s**\nArgent Requis : **%s**" % (data[id]["Money"], buy_item["Money"]))
                            else:
                                await ctx.reply("Veuillez choisir une valeure correcte !")
                        except:
                            await ctx.reply("Veuillez choisir une valeure correcte !")
                    else:
                        await ctx.reply(embed=forge_embed)
                except:
                    await ctx.reply(embed=forge_embed)
            else:
                await ctx.reply(f"Vous n'avez pas le niveau requis pour accéder à cette boutique !\nNiveau requis : **15**\nNiveau actuel : **{data[id]['Level']}**")
                

        else:
            await ctx.reply(embed=s)