import discord, json, time, random
from assets.recipes_data import recipes
from assets.woods_data import woods

def EnumerateRecipes():
    global unlocked_plans
    result = list()
    unlocked_plans = [1, 3, 6]
    for k, v in recipes.items():
        __input__ = dict()
        __output__ = dict()
        for _k, _v in v.items():
            if _k == "emoji": __emoji__ = _v
            elif _k == "points": __points__ = _v
            elif _k == "cooldown": __cooldown__ = _v
            elif _k == "price": __price__ = _v
            elif _k == "level": __level__ = _v
            elif _k == "id": __id__ = _v
            elif _k == "xp": __xp__ = _v
            elif _k  in ["input", "output"]:
                for __k, __v in _v.items():
                    if _k == "input": __input__[__k] = __v
                    else: __output__[__k] = __v
            
        result += [[__emoji__, k, __input__, __output__, __cooldown__, __points__, __price__, __level__, __id__, __xp__]]
        
    return result

async def Forge(ctx, arg):
    
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
             
        if "mix" in arg:
            
            if (data[id]["Level"] >= 10) or (data[id]["Lj Level"] >= 10):
            
                content = ""
                for word in arg:
                    if word != "mix":
                        content += word
                        content += " "
                if content == "":
                    deleteMessage = await ctx.reply("Pour réaliser une des recettes, utilisez la commande **c!forge mix** suivit de l'id de la recette.")
                    await deleteMessage.delete(delay=15)

                else:
                    
                    def IfCommandIsCorrect(arg):
                        global num
                        for i in range(len(res)):
                            try: 
                                n = int(arg[1])
                            except: return False
                            else:
                                if n == res[i][8]:
                                    num = i
                                    return True
                        return False
                    
                    __arg__ = arg
                    arg = arg[1:]
                    arg = str(arg).lower()
                    res = EnumerateRecipes()
                    
                    if not IfCommandIsCorrect(__arg__):
                        deleteMessage = await ctx.reply("La commande est incorrecte ou la recette n'existe pas. Pour avoir la liste des recettes faites la commande **c!forge recipes**. Pour réaliser une des recettes, utilisez la commande **c!forge mix** suivit de l'id de la recette.")
                        await deleteMessage.delete(delay=15)
                    else:
                        
                        if res[num][8] in data[id]["Inventory"]["Plans"] or res[num][8] in unlocked_plans:
                            
                            if 3 in data[id]["Inventory"]["P Forge"]:
                                n = 5
                            else:
                                n = 0
                                
                            if data[id]["Forge Level"] >= (res[num][7] - n):
                            
                                ressources = str()
                                p = True
                                for k, v in res[num][2].items():
                                    if data[id]["Inventory"][k] < v:
                                        p = False
                                        ressources += f"{k} nécessaire : {v} | {k} dans l'inventaire : {data[id]['Inventory'][k]}\n"
                                
                                if not p:
                                    deleteMessage = await ctx.reply('Vous n\'avez malheureusement pas assez de ressources pour pouvoir fabriquer **%s** ! 😿\n%s' % (res[num][1], ressources))
                                    await deleteMessage.delete(delay=15)
                                else:
                                    
                                    if (data[id]["Money"] - res[num][6]) < 0:
                                        deleteMessage = await ctx.reply("Vous n'avez malheureusement pas assez d'argent pour acheter **%s**.\nArgent requis : **%s**\nArgent actuel : **%s**" % (res[num][1], res[num][6], data[id]["Money"]))
                                    else:
                                    
                                        def ReturnCooldownTimes():
                                            delta_t = time.time()
                                            for k, v in data[id]["Forge Cooldown"].items():
                                                if k != "":
                                                    return [delta_t, float(k) + v, k, True]
                                                else:
                                                    return [False, False, False, False]
                                        
                                        coo = ReturnCooldownTimes()
                                        if (coo[1] - coo[0]) > 0 and coo[3]:
                                            deleteMessage = await ctx.reply("Vous êtes fatigué après votre dernière session de forge. Vous devriez vous reposer.\nTemps avant de pourvoir réutiliser la forge : **%ss**" % (round(coo[1] - coo[0])))     
                                            await deleteMessage.delete(delay=15)
                                        else:
                                            
                                            for k, v in res[num][2].items():
                                                data[id]["Inventory"][k] -= v
                                            if 1 in data[id]["Inventory"]["P Forge"]:          
                                                data[id]["Forge Cooldown"] = {str(time.time()): int(round(res[num][4]) / 100 * 60)}
                                            else:
                                                data[id]["Forge Cooldown"] = {str(time.time()): res[num][4]}
                                            if 6 in data[id]["Inventory"]["P Forge"]:
                                                data[id]["Black-Smith Points"] += res[num][5] + (res[num][5] / 100 * 25)
                                            else:
                                                data[id]["Black-Smith Points"] += res[num][5]
                                            data[id]["Money"] -= res[num][6]
                                            for k, v in res[num][3].items():
                                                if 5 in data[id]["Inventory"]["P Forge"] and random.choice([True, False, False, False]):
                                                    data[id]["Inventory"][k] += v + 1
                                                    mess = f"\nVotre Marteau de Crystal vous a permis de gagner `1` {k} supplémentaire !"
                                                else:
                                                    data[id]["Inventory"][k] += v
                                                    mess = ""
                                            if 7 in data[id]["Inventory"]["P Forge"]:
                                                winned_xp =  res[num][9] + (res[num][9] / 100 * 25)     
                                            else:
                                                winned_xp = res[num][9]
                                            winned_xp = int(round(winned_xp + ((winned_xp / 10) * (data[id]["Forge Level"] / 2))))
                                            data[id]["Forge Xp"] += winned_xp
                                            
                                            while True:
                                            
                                                to_next_level = int(100 * ((data[id]["Forge Level"] / 2) * (data[id]["Forge Level"] / 2)))
                                                
                                                if data[id]["Forge Xp"] < 0:
                                                    data[id]["Forge Xp"] = 0
                                                if data[id]['Black-Smith Points'] < 0:
                                                    data[id]['Black-Smith Points'] = 0
                                                if data[id]["Forge Xp"] >= to_next_level:
                                                    data[id]['Forge Level'] += 1
                                                    data[id]["Forge Xp"] -= to_next_level
                                                    
                                                    to_next_level = int(100 * ((data[id]["Forge Level"] / 2) * (data[id]["Forge Level"] / 2)))

                                                    with open("assets/player_data.json", 'w') as d:
                                                        json.dump(data, d, indent=4)
                                                    embed = discord.Embed(title=f"**GG**, vous avez atteint le niveau **{data[id]['Forge Level']}** !", description=f"XP nécessaire pour passer au prochain niveau : **{to_next_level}xp**", color=0x56860e)
                                                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                                    await ctx.send(embed=embed)
                                                
                                                else:
                                                    break
                                                    
                                            with open("assets/player_data.json", 'w') as d:
                                                json.dump(data, d, indent=4)
                                                
                                            buy_embed = discord.Embed(title="🔨 FORGE COMBINAISON 🔨", description=f"Combinaison de **{res[num][1]}**{mess}", color=0xC0712C)
                                            buy_embed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
                                            buy_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                            buy_embed.add_field(name=":nut_and_bolt: • Points de Forgeron :", value=data[id]["Black-Smith Points"])
                                            buy_embed.add_field(name="💸 • Argent :", value=round(data[id]["Money"], 2))                                            
                                            xpDashes = 25
                                            dashConvert = int(to_next_level / xpDashes)
                                            currentDashes = int(data[id]['Forge Xp'] / dashConvert)
                                            remain = xpDashes - currentDashes
                                            xpDisplay = '━' * currentDashes
                                            remainingDisplay = '᲼' * remain
                                            percent = f"{round(data[id]['Forge Xp'])}/{round(to_next_level)}"
                                            space = '᲼' * int((len(xpDisplay) + len(remainingDisplay)) / 2)
                                            buy_embed.add_field(name=f"🧪 • Xp *(+{winned_xp}xp)* :", value=f"**{data[id]['Forge Level']}|{xpDisplay}◈**{remainingDisplay}**|{data[id]['Forge Level'] + 1}**\n{space}**{percent}**", inline=False)
                                            for k, v in res[num][2].items():
                                                buy_embed.add_field(name=f"{k} : ", value=data[id]["Inventory"][k])
                                            for k, v in res[num][3].items():
                                                buy_embed.add_field(name=f"{k} : ", value=data[id]["Inventory"][k])
                                            if 1 in data[id]["Inventory"]["P Forge"]:
                                                buy_embed.set_footer(text="Vous devez maintenant vous reposer pendant %ss afin de pouvoir réutiliser la commande c!forge mix !" % (int(round(res[num][4]) / 100 * 60)))
                                            else:
                                                buy_embed.set_footer(text="Vous devez maintenant vous reposer pendant %ss afin de pouvoir réutiliser la commande c!forge mix !" % (res[num][4]))
                                                
                                            await ctx.send(embed=buy_embed)
                                        
                            else: 
                                await ctx.reply(f"Vous n'avez pas le niveau de forgeron pour pouvoir utiliser cette recette !\nNiveau requis : {res[num][7]}\nNiveau actuel : {data[id]['Forge Level']}") 
                                
                        else:
                            await ctx.reply("Vous n'avez pas débloqué ce plan.")     
                    
            else:
                await ctx.reply(f"Vous n'avez pas le niveau de mineur/bûcheron requis pour accéder à la Forge Sacrée !\nNiveau requis : 10\nNiveau actuel mineur, bûcheron : {data[id]['Level']}, {data[id]['Lj Level']}")
                
        elif "recipes" in arg:
            recipe_embed = discord.Embed(title=":nut_and_bolt: | Forge Recipes", description="Pour réaliser une des recettes ci-dessus utilisez la commande **c!forge mix** suivit de l'id de la recette.\n", color=0x556b2f)
            res = EnumerateRecipes()
            locked = 0
            for i in range(len(res)):
                inputs = str()
                outputs = str()
                if res[i][8] in data[id]["Inventory"]["Plans"] or res[i][8] in unlocked_plans:
                    for _k_, _v_ in res[i][2].items():
                        inputs += f"**{_v_} {_k_}** + "
                    inputs = inputs[:-3]
                    for _k_, _v_ in res[i][3].items():
                        outputs += f"**{_v_} {_k_}** + "
                    outputs = outputs[:-3]
                    recipe_embed.add_field(name=f"{res[i][0]} • {res[i][1]} (id:{res[i][8]}) :", value=f"Recette : {inputs} --> {outputs}\nCooldown : **{res[i][4]}s**\nPoints de Forgeron : **{res[i][5]}**\nNiveau de Forgeron : **{res[i][7]}**\nArgent : **{res[i][6]}**\nXp : **{res[i][9]}**", inline=False)
                else:
                    locked += 1
                            
            recipe_embed.set_footer(text=f"Recettes cachées non débloquées : {locked}")
            await ctx.reply(embed=recipe_embed)
            
        elif "extract" in arg:
            try:
                wid = int(arg[1])
            except:
                await ctx.reply("Veuillez entrer un id correct ! c!forge extract **id**.\nLes id et les prix d'extractions peuvent être consultés depuis la commande **c!stats woods**.")
            else:           
                try:
                    wn = int(arg[2])
                except:
                    wn = 1
                    
                if wn <= 0:
                    await ctx.reply("Veuillez entrer un montant correct !\nc!forge extract <id> **<montant>**.")
                else:
                    
                    
                    def LoadStats():
                        for k, v in woods.items():
                            wname = None
                            for k_, v_ in v.items():
                                if k_ == "Ex":
                                    wex = v_
                                    print(wex)
                                if k_ == "Emoji":
                                    wemoji = v_
                                if k_ == "Id":
                                    if wid == v_:
                                        wname = k
                            if wname is not None:
                                return [wname, wemoji, wex]
                        return False
                    
                    l = LoadStats()
                    
                    if not l:
                        await ctx.reply("Veuillez entrer un id correct ! c!forge extract **id**.\nLes id et les prix d'extractions peuvent être consultés depuis la commande **c!stats woods**.")
                    else:
                        wname = l[0]
                        wemoji = l[1]
                        wex = l[2]
           
                        if data[id]["Inventory_2"][wname] < wn:
                            await ctx.reply(f"Vous n'avez pas assez de **{wname}** pour en extraire **{wn}**...\n{wname} dans l'inventaire : **{data[id]['Inventory_2'][wname]}**")
                        else:
                            wex *= wn
                            if data[id]["Lj Points"] < wex:
                                await ctx.reply(f"Vous n'avez pas assez de **Points de Bûcheron** pour pouvoir extraire **{wn} {wname}**...\nPoints de Bûcheron requis : **{wex}**\nPoints de Bûcheron acutels : **{data[id]['Lj Points']}**")
                            else:
                                data[id]["Inventory_2"][wname] -= wn
                                data[id]["Lj Points"] -= wex
                                data[id]["Inventory_2"]["Essences"][wid] += wn
                                data[id]["Forge Xp"] += round(wex / 4)
                                data[id]["Black-Smith Points"] += round(wex / 5)
                                
                                with open("assets/player_data.json", 'w') as d:
                                    json.dump(data, d, indent=4)
                                
                                to_next_level = int(100 * ((data[id]["Forge Level"] / 2) * (data[id]["Forge Level"] / 2)))
                                extract_embed = discord.Embed(title="🔬 FORGE EXTRACTION 🔬", description=f"Vous avez extrait `{wn}` {wname} pour le prix de `{wex}` Points de Bûcheron. Vous gagnez tout de même `{round(wex / 5)}` Points de Forgeron.", color=0x59514A)
                                extract_embed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
                                extract_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                extract_embed.add_field(name="", value="", inline=False)
                                extract_embed.add_field(name=":nut_and_bolt: • Points de Forgeron :", value=data[id]["Black-Smith Points"], inline=False)
                                extract_embed.add_field(name="🌲 • Points de Bûcheron :", value=data[id]["Lj Points"], inline=False)
                                extract_embed.add_field(name=f"{wemoji} • {wname} :", value=data[id]["Inventory_2"][wname], inline=False)
                                extract_embed.add_field(name=f"🟢 • Essences de {wname} :", value=data[id]["Inventory_2"]["Essences"][wid], inline=False)
                                xpDashes = 25
                                dashConvert = int(to_next_level / xpDashes)
                                currentDashes = int(data[id]['Forge Xp'] / dashConvert)
                                remain = xpDashes - currentDashes
                                xpDisplay = '━' * currentDashes
                                remainingDisplay = '᲼' * remain
                                percent = f"{round(data[id]['Forge Xp'])}/{round(to_next_level)}"
                                space = '᲼' * int((len(xpDisplay) + len(remainingDisplay)) / 2)
                                extract_embed.add_field(name=f"🧪 • Xp *(+{round(wex / 4)}xp)* :", value=f"**{data[id]['Forge Level']}|{xpDisplay}◈**{remainingDisplay}**|{data[id]['Forge Level'] + 1}**\n{space}**{percent}**", inline=False)
                                extract_embed.set_footer(text="Pour afficher vos nombres d'essences, vous pouvez utiliser la commande c!inventory lj.")

                                await ctx.send(embed=extract_embed)
                            
        else:
            to_next_level = int(100 * ((data[id]["Forge Level"] / 2) * (data[id]["Forge Level"] / 2)))
            exembed = discord.Embed(title="just Hervey 💎 | 🛠 FORGE SACRÉE 🛠", description="Bienvenue dans la Forge Sacrée, ici, vous pouvez combiner différent matériaux/objets afin d'en fabriquer de nouveaux grâce à des recettes que vous pouvez débloquer !\n\n```c!forge recipes```  Avoir la liste des différentes recettes\n```c!forge mix```  Combiner deux matériaux ensemble pour réaliser une des recettes et gagner des Points de Forgeron (Niveau de mineur/bûcheron minimal requis : 10)\n```c!forge extract <id du bois> (<montant>)```  Permet d'extraire de l'essence du bois afin d'améliorer votre hache. Les id et les prix d'extraction des différents bois peuvent être consultés via la commande `c!stats woods`.", color=0x59514A)
            exembed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
            exembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            exembed.add_field(name="", value="", inline=False)
            exembed.add_field(name=":nut_and_bolt: • Points de Forgeron :", value=data[id]["Black-Smith Points"], inline=False)
            xpDashes = 25
            dashConvert = int(to_next_level / xpDashes)
            currentDashes = int(data[id]['Forge Xp'] / dashConvert)
            remain = xpDashes - currentDashes
            xpDisplay = '━' * currentDashes
            remainingDisplay = '᲼' * remain
            percent = f"{round(data[id]['Forge Xp'])}/{round(to_next_level)}"
            space = '᲼' * int((len(xpDisplay) + len(remainingDisplay)) / 2)
            exembed.add_field(name="🧪 • Xp :", value=f"**{data[id]['Forge Level']}|{xpDisplay}◈**{remainingDisplay}**|{data[id]['Forge Level'] + 1}**\n{space}**{percent}**", inline=False)
            exembed.set_footer(text="Les Points de Forgeron servent à acheter des objets uniques dans la boutique du forgeron !")
            
            await ctx.send(embed=exembed)
        
