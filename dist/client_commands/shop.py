import discord, json
from assets.items_price import item_shop_price, item_shop_price_2, item_shop_price_3, item_shop_price_5
from assets.woods_data import woods

async def Shop(ctx, buy):

    with open("assets/player_data.json") as data:
        data = json.load(data)
            
    id = str(ctx.author.id)
    c = True

    for key in data.keys():
        if key == id:
            c = False

    if c:
        embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)

    else:

        s=discord.Embed(title="CHOIX DE LA BOUTIQUE", description="Ici, vous pouvez choisir la boutique dans laquelle vous voulez aller.", color=0x116792)
        s.add_field(name="**🎭 Boutique de Grade 🎭**", value="`c!shop rank` pour accéder à la boutique.", inline=False)
        s.add_field(name="**⛏ Boutique du Mineur ⛏**", value="`c!shop mine` pour accéder à la boutique.", inline=False)
        s.add_field(name="**🔨 Boutique du Forgeron 🔨**", value="Boutique accesible à partir du niveau `15` du métier de mineur. `c!shop forge` pour accéder à la boutique.", inline=False)
        s.add_field(name="**🪓 Scierie du Bûcheron 🪓**", value="`c!shop lj` pour accéder à la boutique.", inline=False)
        s.add_field(name="**👨‍🌾 Boutique d'Herboriste 👨‍🌾**", value="Bientôt disponible !", inline=False)
        s.set_footer(text="Chaque boutique vend des articles différents.")

        if not buy:
            await ctx.reply(embed=s)

        elif buy[0] in ["rank", "r"]:

            rank_embed=discord.Embed(title="**🎭 BOUTIQUE DES GRADES 🎭**", description="Vous marchez tranquillement sur la place publique, soudain un stand attire votre attention. Un homme masqué se présente sous le nom de `Falstaff le Fantaisiste`, ils vous tend un masque afin de l'essayer.", color=0xC922B7)
            rank_embed.set_image(url="https://i.ibb.co/VYvGtKV/shop-rank.png")
            rank_embed.add_field(name="`1` - GRADE | 😮 - Débutant :", value="Prix : `1,000€`", inline=False)
            rank_embed.add_field(name="`2` - GRADE | 😋 - Amateur :", value="Prix : `10,000€`", inline=False)
            rank_embed.add_field(name="`3` - GRADE | 🤑 -  Affirmé :", value="Prix : `25,000€`", inline=False)
            rank_embed.add_field(name="`4` - GRADE | 😎 - Professionel :", value="Prix : `50,000€`", inline=False)
            rank_embed.add_field(name="`5` - GRADE | 🐱‍🏍 - Légende :", value="Prix : `100,000€`", inline=False)
            rank_embed.add_field(name="`8` - GRADE | 🧚‍♂️ - Mineur Mythique :", value="Prix : `500,000€`", inline=False)
            rank_embed.add_field(name="`9` - GRADE | 👑 - N°1 :", value="Prix : `1,000,000€`", inline=False)
            rank_embed.add_field(name="`10` - GRADE | <:drogue:882314468086931466>-DROGUÉ :", value="Prix : `100 Charbons à Coke`", inline=False)
            rank_embed.add_field(name="`14` - GRADE | 🚮 - Éboueur :", value="Prix : `1000 Débrits`", inline=False)
            rank_embed.set_footer(text="Pour acheter un grade, faites la commande c!shop rank buy <NUMÉRO DU GRADE>.")

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
                                                await ctx.reply(f"Vous n'avez pas assez de ressources !\n{buy_item['Price'][0]} nécessaires : {buy_item['Price'][1]}\nDans l'inventaire : {data[id]['Inventory'][buy_item['Price'][0]]}")
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
                                            money_embed.add_field(name=f"**{buy_item['Price'][0]}** restant :", value=data[id]['Inventory'][buy_item['Price'][0]], inline=False)
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

        elif buy[0] in ["mine", "m"]:

            item_embed=discord.Embed(title="⚔ **BOUTIQUE D'OBJET** ⚔", description="Vous vous avancez un peu plus pronfondémment dans les mines et découvez un vieil homme tenant une lanterne. Il vous salut de la main et vous fait signe d'approcher. Se présentant sous le nom de `Drogath le Taciturne` puis ouvre son sac et vous propose diffférentes offres.", color=0xBCD8E8)
            item_embed.set_image(url="https://i.ibb.co/fCkHMpN/shop-mine.png")
            item_embed.add_field(name="`1` - 🧲|Pioche en Fer : `5 Fer`, `1,000 Points de Mineur`", value="Vous avez `10` de chance supplémentaire de miner des minerais.", inline=False)
            item_embed.add_field(name="`2` - 🥇|Pioche en Or : `5 Or`, `2,500 Points de Mineur`", value="Augmente le gain des points de mineur `10`", inline=False)
            item_embed.add_field(name="`3` - 🔥|Pioche de Magma : `5 Pierre de Magma`, `1,500 Points de Mineur`", value="Vous ne perdez plus de **Points de Mineur** ni d'**xp** à cause de la Roche Magmatique.", inline=False)
            item_embed.add_field(name="`4` - ⛏|Alliage en Platine : `5 Platine`, `2,000 Points de Mineur`", value="Vous permet d'améliorer votre pioche pour qu'elle puisse miner le **rubis**, le **saphir** et l'**émeraude**. (n'a pas besoin d'être équipé dans l'inventaire)", inline=False)
            item_embed.add_field(name="`12` - ⛏|Alliage en Obsidienne : `15 Obsidienne`, `15,000 Points de Mineur`, `20,000€`", value="Vous permet d'améliorer votre pioche pour qu'elle puisse miner l'**uranium** et le **plutonium**. (n'a pas besoin d'être équipé dans l'inventaire)", inline=False)
            item_embed.add_field(name="`11` - 🧪|Pioche Expérimentale : `20 Cuivre`, `5,000 Points de Mineur`, `10,000€`.", value=f"Vous gagnez `10{'%'}` d'**xp supplémentaire** en minant.", inline=False)
            item_embed.add_field(name="`5` - 👨‍🔬|PIOCHE DU CHINOIS : `10 Joseph`, `10,000 Points de Mineur`, `50,000€`.", value="GG, vous avez la **meilleure pioche du jeu** (ne sert à rien).", inline=False)
            item_embed.add_field(name="`13` - GRADE | 💎 - Géologue :", value="Requiert : Métier de Mineur Niv. `50`\nPrix : `15,000 Points de Mineur`, `75,000€`", inline=False)
            item_embed.add_field(name="`14` - GRADE | <:sacredstone:1078401347780608040> - Récolteur de cristaux :", value="Requiert : Métier de Mineur Niv. `75`\nPrix : `25,000 Points de Mineur`, `100,000€`", inline=False)
            item_embed.add_field(name="`6` - ✖|Pioche de multiplication : `100 Cobaltes`, `20,000 Points de Mineur`, `50,000€`.", value=f"A `33.33{'%'}` de **dupliquer** les minerais que vous minez.", inline=False)
            item_embed.add_field(name="`7` - 🕵️‍♂️|Pioche du maraudeur : `250 Pierres`, `15,000 Points de Mineur`, `20,000€`.", value="Vous ne minerez plus de **débrits** (ouf).", inline=False)
            item_embed.add_field(name=f"`9` - 👾|Multi-Pioche : `{data[id]['Inventory']['Item Limit'] * 10} Diamant`, `{(data[id]['Inventory']['Item Limit'])*5}0,000€`.", value=f"Vous permet d'équiper {data[id]['Inventory']['Item Limit'] + 1} pioches à la fois. Requier : Métier de Mineur Niv. {data[id]['Inventory']['Item Limit'] * 10} (pour équiper plusieurs pioches, faites __c!inventory equip item__ suivi du numéro des objets séparés d'espaces)", inline=False)
            item_embed.set_footer(text="Pour acheter un objet, faites la commande c!shop mine buy <NUMÉRO DE L'ITEM>.")
            
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
                                
                                if int(buy[2]) not in data[id]['Inventory']["P Rank"]:
                                
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
                                                                money_embed.add_field(name=f"**{buy_item['Price'][0]}** restant :", value=data[id]['Inventory'][buy_item['Price'][0]], inline=False)
                                                                await ctx.reply(embed=money_embed)
                                                                
                                                            
                                                            elif int(buy[2]) == 9:
                                                                data[id]['Inventory']["Item Limit"] += 1
                                                                data[id]['Money'] = round(data[id]['Money'], 2)
                                                                json.dump(data, d, indent=4)
                                                                money_embed = discord.Embed(title=f"Vous avez acheter l'amélioration n°{buy[2]} avec succès ! (pour équiper plusieurs pioches, faites __c!inventory equip item__ suivi du numéro des objets séparés d'espaces)", description=f"-**{money}**€", color=0x5455b0)
                                                                money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                                money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                                                money_embed.add_field(name=f"**{buy_item['Price'][0]}** restant :", value=data[id]['Inventory'][buy_item['Price'][0]], inline=False)
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
                                                                money_embed.add_field(name=f"**{buy_item['Price'][0]}** restant :", value=data[id]['Inventory'][buy_item['Price'][0]], inline=False)
                                                                await ctx.reply(embed=money_embed)

                                                    else:
                                                        await ctx.reply("Vous possédez déjà cet alliage !")
                                                else:
                                                    await ctx.reply("Vous possédez déjà cet item !")
                                            else:
                                                await ctx.reply("Vous n'avez pas l'argent requis !\nArgent : **%s**\nArgent Requis : **%s**" % (data[id]["Money"], buy_item["Money"]))
                                    
                                        else:
                                            await ctx.reply(f"Vous n'avez pas assez de ressources !\n**{buy_item['Price'][0]}** nécessaires : **{price}**\n**{buy_item['Price'][0]}** dans l'inventaire : **{data[id]['Inventory'][buy_item['Price'][0]]}**")
                                    else:
                                        await ctx.reply(f"Vous n'avez pas assez de Points de Mineur !\nPoints requis : **{buy_item['Miner Points']}**\nPoints actuels : **{data[id]['Miner Points']}**")
                                else:                            
                                    await ctx.reply("Vous possédez déjà ce grade !")
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

        elif buy[0] in ["forge", "f"]:
            
            if data[id]["Level"] >= 15:
            
                forge_embed = discord.Embed(title="**🔨 BOUTIQUE DU FORGERON 🔨**", description="Dans une petite cabane non loin de là, réside `Arcturus le Maître-forgeron`, l'un des forgerons les plus réputés de la région. Vous pénétrez en son logis et jetez un coup d'oeil.", color=0x929292)
                forge_embed.set_image(url="https://i.ibb.co/vjBgd5s/shop-forge.png")
                forge_embed.add_field(name="`1` - 🧲|Marteau Magnétique : `100 Magnétite`, `5,000 Points de Forgeron` et `100,000€`.", value="Une fois équipé, le **cooldown de la forge** est réduis de `40%`.", inline=False)
                forge_embed.add_field(name="`13` - RANK | 🧔 - Forgeron de renommée : `10,000 Points de Forgeron`, niveau de forgeron requis : `50`", value="Un grade spécial pour les utilisateurs affirmés de la forge.", inline=False)
                forge_embed.set_footer(text="Pour acheter un objet, faites la commande c!shop forge buy <NUMÉRO DE L'OBJET>.")
                forge_embed.add_field(name="`7` - ⛑|Casque de Forgeron : `25 Iron`, `Platine` et `Silver`, `5,000 Points de Forgeron` et `75,000€`.", value=f"Un casque que tout bon forgeron se doit d'avoir. Une fois équipé vous gagnez `25{'%'}` d'**xp supplémentaire**.", inline=False)
                forge_embed.add_field(name=f"`2` - 🍀|Lucky-Hammer : `25 Lucky Stones`, `1,500 Points de Forgeron`, `150,000€`.", value=f"En cours de création....", inline=True)
                forge_embed.add_field(name=f"`3` - ☢|Marteau Radioactif : `25 Uranium`, `Plutonium`, `Fluorite`, et `7,500 Points de Forgeron`.", value=f"Les plans que vous découvrez demandent `5` **niveaux en moins** afin d'être fabriqués.", inline=False)
                forge_embed.add_field(name=f"`4` - ⚓|Trident de Poséidon : `3 Aigue Marine`, `10,000 Points de Forgeron`, `500,000€`, niveau de forgeron requis : `10`", value=f"Les dieux vous guident, vos chances d'**obtenir un plan** augmentent de `15%`.", inline=False)
                forge_embed.add_field(name=f"`5` - 🔮|Marteau de Crystale : `25 Améthiste`, `10 Jades`, `7,500 Points de Forgeron`, `150,000€`, niveau de forgeron requis : `5`", value=f"Une combinaison de crystaux permettant d'avoir `25{'%'}` de chance de **multiplier un minerai** en le forgeant.", inline=False)
                forge_embed.add_field(name=f"`6` - 🐉|Marteau en Plaques de Dragon : `5 Dragonite`, `50 Platine`, `10,000 Points de Forgeron`, `250,000€`, niveau de forgeron requis : `10`", value=f"La puissance des dragons vous envahie, vous gagnez `25{'%'}` de **Points de Forgeron** lors de la fabrication d'une recette !", inline=False)

                try:
                    if buy[1] == "buy":
                        try:
                            if int(buy[2]) in [1, 13, 2, 3, 4, 5, 6, 7]:
                                buy_item = item_shop_price_3[int(buy[2])]
                                
                                if data[id]["Forge Level"] >= buy_item["Level"]:
                                    
                                    if int(buy[2]) not in data[id]['Inventory']["P Rank"]:

                                        if data[id]['Money'] >= buy_item["Money"]:
                                            
                                            if data[id]["Black-Smith Points"] >= buy_item["Black-Smith Points"]:

                                                if int(buy[2]) not in data[id]['Inventory']["P Forge"]:
                                                    
                                                    _c_ = True
                                                    for k, v in buy_item["Price"].items():
                                                        if data[id]["Inventory"][k] < v:
                                                            _c_ = False
                                                            
                                                    if _c_:
                                                        data[id]['Money'] -= buy_item["Money"]
                                                        for k, v in buy_item["Price"].items():        
                                                            data[id]['Inventory'][k] -= v
                                                        data[id]["Black-Smith Points"] -= buy_item["Black-Smith Points"]
                                                        if not buy_item["Rank"]:
                                                            data[id]['Inventory']["P Forge"].append(int(buy[2]))
                                                        else:
                                                            data[id]['Inventory']["P Rank"].append(int(buy[2]))
                                                        data[id]['Money'] = round(data[id]['Money'], 2)

                                                        with open("assets/player_data.json", 'w') as d:
                                                            json.dump(data, d, indent=4)
                                                            
                                                        if buy_item["Money"] > 0:
                                                            money_embed = discord.Embed(title=f"Vous avez acheter l'objet n°{buy[2]} avec succès", description=f"-**{buy_item['Money']}**€\n-**{buy_item['Black-Smith Points']}** Points de Forgeron", color=0x5455b0)
                                                        else:
                                                            money_embed = discord.Embed(title=f"Vous avez acheter l'objet n°{buy[2]} avec succès", description=f"-**{buy_item['Black-Smith Points']}** Points de Forgeron", color=0x5455b0)
                                                        money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                        money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                                        money_embed.add_field(name="Points de Forgeron restant:", value=data[id]['Black-Smith Points'], inline=False)
                                                        money_embed.set_footer(text="L'objet a été ajouté à votre établi. Pour voir tout les objets de votre établi, faites la commande c!inventory.")
                                                        t = ""
                                                        for k, v in buy_item["Price"].items():
                                                            money_embed.add_field(name=f"**{k}** restant:", value=data[id]['Inventory'][k], inline=False)
                                                        await ctx.reply(embed=money_embed)
                                                        
                                                    else:
                                                        t = ""
                                                        for k, v in buy_item["Price"].items():
                                                            if data[id]["Inventory"][k] < v:
                                                                t += f"\n**{k}** nécessaires : `{v}`\n**{k}** dans l'inventaire : `{data[id]['Inventory'][k]}`" 
                                                        await ctx.reply(f"Vous n'avez pas assez de ressources !{t}")
                                                else:
                                                    await ctx.reply("Vous possédez déjà ce grade !")                         
                                            else:
                                                await ctx.reply("Vous n'avez pas les Points de Forgeron requis !\nPoints de Forgeron : **%s**\nPoints de Forgeron requis : **%s**" % (data[id]["Black-Smith Points"], buy_item["Black-Smith Points"]))
                                        else:
                                            await ctx.reply("Vous n'avez pas l'argent requis !\nArgent : **%s**\nArgent Requis : **%s**" % (data[id]["Money"], buy_item["Money"]))
                                    else:
                                        await ctx.reply("Vous possédez déjà ce grade !")
                                else:
                                    await ctx.reply(f"Vous n'avez pas le niveau requis pour pouvoir acheter cela !\nNiveau requis : **{buy_item['Level']}**\nNiveau actuel : **{data[id]['Forge Level']}**")
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
        
        elif buy[0] in ["lumberjack", "lj"]:
            
            lj_embed = discord.Embed(title="**🪓 SCIERIE DU BÛCHERON 🪓**", description="Besoin d'améliorer votre hache ? Pas de soucis, `Thorne Ombrebois` se fera un plaisir de le faire pour vous en échange de quelques dûs.\nLes essences de bois sont fabriquables à partir de la commande `c!forge extract`.\nVous pourrez par la suite augmenter le niveau de vos améliorations dans de futures mises à jours.", color=0x48290D)
            lj_embed.set_image(url="https://i.ibb.co/58KQL5c/shop-lj.png")
            lj_embed.add_field(name=f"`1` - 🍃|Amélioration: Envol : `10 Bois de Chêne`, `1,000 Points de Bûcheron`, `500€`, `10 essences d'acacia`.", value=f"Cette amélioration augmente votre pourcentage d'xp lors du cassage d'un arbre de `10{'%'}` au niveau 1. (améliorable)", inline=False)
            lj_embed.add_field(name=f"`17` - 🌳-Partisan Écologiste : `100 Bois de Chêne`, `10,000 Points de Bûcheron`, `5,000€`, niveau de bûcheron requis : `25`.", value=f"Faut bien protéger la planète...", inline=False)
            lj_embed.set_footer(text="Pour acheter un objet, faites la commande c!shop lj buy <NUMÉRO DE L'OBJET>.")

            try:
                if buy[1] == "buy":
                    try:
                        if int(buy[2]) in [17, 1]:
                            buy_item = item_shop_price_5[int(buy[2])]
                            
                            if data[id]["Lj Level"] >= buy_item["Level"]:
                                
                                rn = None
                                if buy_item["Rank"]:
                                    if int(buy[2]) in data[id]['Inventory']["P Rank"]:
                                        rn = "ce grade"
                                else:
                                    if int(buy[2]) in data[id]['Inventory_2']["Upgrades"]:
                                        rn = "cette amélioration"
                                        
                                if rn is None:

                                    if data[id]['Money'] >= buy_item["Money"]:
                                        
                                        if data[id]["Lj Points"] >= buy_item["Lj Points"]:

                                            if int(buy[2]) not in data[id]['Inventory_2']["Upgrades"]:
                                                
                                                _c_ = True
                                                for k, v in buy_item["MPrice"].items():
                                                    if data[id]["Inventory"][k] < v:
                                                        _c_ = False
                                                        
                                                __c__ = True
                                                for k, v in buy_item["LPrice"].items():
                                                    if data[id]["Inventory_2"][k] < v:
                                                        __c__ = False
                                                        
                                                ___c___ = True
                                                for k, v in buy_item["Ess"].items():
                                                    if data[id]["Inventory_2"]["Essences"][int(k)] < v:
                                                        ___c___ = False
                                                        
                                                if _c_:
                                                    if __c__:
                                                        if ___c___:
                                                            data[id]['Money'] -= buy_item["Money"]
                                                            for k, v in buy_item["MPrice"].items():        
                                                                data[id]['Inventory'][k] -= v
                                                            for k, v in buy_item["LPrice"].items():        
                                                                data[id]['Inventory_2'][k] -= v
                                                            for k, v in buy_item["Ess"].items():        
                                                                data[id]["Inventory_2"]["Essences"][int(k)] -= v
                                                            data[id]["Lj Points"] -= buy_item["Lj Points"]
                                                            if not buy_item["Rank"]:
                                                                data[id]['Inventory_2']["Upgrades"].append(int(buy[2]))
                                                            else:
                                                                data[id]['Inventory']["P Rank"].append(int(buy[2]))
                                                            data[id]['Money'] = round(data[id]['Money'], 2)

                                                            with open("assets/player_data.json", 'w') as d:
                                                                json.dump(data, d, indent=4)
                                                            
                                                            if not buy_item["Rank"]:
                                                            
                                                                if buy_item["Money"] > 0:
                                                                    money_embed = discord.Embed(title=f"Vous avez acheter l'amélioration n°{buy[2]} avec succès", description=f"-**{buy_item['Money']}**€\n-**{buy_item['Lj Points']}** Points de Bûcheron", color=0x5455b0)
                                                                else:
                                                                    money_embed = discord.Embed(title=f"Vous avez acheter l'amélioration n°{buy[2]} avec succès", description=f"-**{buy_item['Lj Points']}** Points de Bûcheron", color=0x5455b0)
                                                                money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                                money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                                                money_embed.add_field(name="Points de Bûcheron restants:", value=data[id]['Lj Points'], inline=False)
                                                                money_embed.set_footer(text="L'amélioration a été ajouté à votre inventaire de bûcheron. c!inventory lj pour afficher votre inventaire de bûcheron.")
                                                                
                                                            else:
                                                                money_embed = discord.Embed(title=f"Vous avez acheter le grade n°{buy[2]} avec succès (c!inventory equip rank {buy[2]} pour équiper votre rank !) !", description=f"-**{buy_item['Money']}**€\n-**{buy_item['Lj Points']}** Points de Bûcheron", color=0x5455b0)
                                                                money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                                money_embed.add_field(name="Argent restant :", value=data[id]['Money'], inline=False)
                                                                money_embed.add_field(name="Points de Bûcheron restant:", value=data[id]['Lj Points'], inline=False)                                            
                                                                
                                                            t = ""
                                                            for k, v in buy_item["Ess"].items():
                                                                for k_, v_ in woods.items():
                                                                    for k__, v__ in v_.items():
                                                                        if k__ == "Id":
                                                                            if int(k) == v__:                                                                
                                                                                money_embed.add_field(name=f"🟢 Essences de **{k_}** restants:", value=data[id]['Inventory_2']['Essences'][int(k)], inline=False)
                                                            t = ""
                                                            for k, v in buy_item["LPrice"].items():
                                                                money_embed.add_field(name=f"**{k}** restant:", value=data[id]['Inventory_2'][k], inline=False)
                                                            
                                                            t = ""
                                                            for k, v in buy_item["MPrice"].items():
                                                                money_embed.add_field(name=f"**{k}** restant:", value=data[id]['Inventory'][k], inline=False)
                                                            
                                                            await ctx.reply(embed=money_embed)


                                                        else:
                                                            t = ""
                                                            for k, v in buy_item["Ess"].items():
                                                                if data[id]["Inventory_2"]["Essences"][int(k)] < v:
                                                                    for k_, v_ in woods.items():
                                                                        for k__, v__ in v_.items():
                                                                            if k__ == "Id":
                                                                                if int(k) == v__:
                                                                                    t += f"\n🟢 Essences de **{k_}** nécessaires : **{v}**\n🟢 Essences de **{k_}** dans l'inventaire : **{data[id]['Inventory_2']['Essences'][int(k)]}**" 
                                                            await ctx.reply(f"Vous n'avez pas assez de ressources !{t}\nPour obtenir des essences, utilisez la commande **c!forge extract**.")
                                                                                                                
                                                    else:
                                                        t = ""
                                                        for k, v in buy_item["LPrice"].items():
                                                            if data[id]["Inventory_2"][k] < v:
                                                                t += f"\n**{k}** nécessaires : **{v}**\n**{k}** dans l'inventaire : **{data[id]['Inventory_2'][k]}**" 
                                                        await ctx.reply(f"Vous n'avez pas assez de ressources !{t}")
                                                    
                                                else:
                                                    t = ""
                                                    for k, v in buy_item["MPrice"].items():
                                                        if data[id]["Inventory"][k] < v:
                                                            t += f"\n**{k}** nécessaires : **{v}**\n**{k}** dans l'inventaire : **{data[id]['Inventory'][k]}**" 
                                                    await ctx.reply(f"Vous n'avez pas assez de ressources !{t}")
                                            else:
                                                await ctx.reply("Vous possédez déjà ce grade !")                         
                                        else:
                                            await ctx.reply("Vous n'avez pas les Points de Bûcheron requis !\nPoints de Bûcheron : **%s**\nPoints de Bûcheron requis : **%s**" % (data[id]["Lj Points"], buy_item["Lj Points"]))
                                    else:
                                        await ctx.reply("Vous n'avez pas l'argent requis !\nArgent : **%s**\nArgent Requis : **%s**" % (data[id]["Money"], buy_item["Money"]))
                                else:
                                    await ctx.reply(f"Vous possédez déjà {rn} !")
                            else:
                                await ctx.reply(f"Vous n'avez pas le niveau requis pour pouvoir acheter cela !\nNiveau requis : **{buy_item['Level']}**\nNiveau actuel : **{data[id]['Lj Level']}**")
                        else:
                            await ctx.reply("Veuillez choisir une valeure correcte !")
                    except:
                        await ctx.reply("Veuillez choisir une valeure correcte !")
                else:
                    await ctx.reply(embed=lj_embed)
            except:
                    await ctx.reply(embed=lj_embed)

        else:
            await ctx.reply(embed=s)