import discord, json, time
from assets.recipes_data import recipes

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
        d = await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")
        await d.delete(delay=15)
    else:          
             
        if "mix" in arg:
            
            if data[id]["Level"] >= 10:
            
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
                                                if 5 in data[id]["Inventory"]["P Forge"]:
                                                    data[id]["Inventory"][k] += v + 1
                                                    mess = f"\nVotre Marteau de Crystal vous a permis de gagner `1` {k} supplémentaire !"
                                                else:
                                                    data[id]["Inventory"][k] += v
                                                    mess = ""
                                            if 7 in data[id]["Inventory"]["P Forge"]:
                                                data[id]["Forge Xp"] += res[num][9] + (res[num][9] / 100 * 15)
                                            else:
                                                data[id]["Forge Xp"] += res[num][9]
                                            
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
                                                
                                            buy_embed = discord.Embed(title="🛠 FORGE 🛠", description=f"Forge de **{res[num][1]}**{mess}", color=0xC0712C)
                                            buy_embed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
                                            buy_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                            buy_embed.add_field(name=":nut_and_bolt: • Points de Forgeron :", value=data[id]["Black-Smith Points"])
                                            buy_embed.add_field(name="💸 • Argent :", value=round(data[id]["Money"], 2))
                                            buy_embed.add_field(name="🧔 • Niveau de Forgeron :", value=data[id]["Forge Level"], inline=False)
                                            buy_embed.add_field(name="🧪 • Xp actuel :", value=data[id]['Forge Xp'], inline=False)
                                            for k, v in res[num][2].items():
                                                buy_embed.add_field(name=f"{k} : ", value=data[id]["Inventory"][k])
                                            for k, v in res[num][3].items():
                                                buy_embed.add_field(name=f"{k} : ", value=data[id]["Inventory"][k])
                                            if 1 in data[id]["Inventory"]["P Forge"]:
                                                buy_embed.set_footer(text="Vous devez maintenant vous reposer pendant %ss afin de pouvoir réutiliser la commande c!forge !" % (int(round(res[num][4]) / 100 * 60)))
                                            else:
                                                buy_embed.set_footer(text="Vous devez maintenant vous reposer pendant %ss afin de pouvoir réutiliser la commande c!forge !" % (res[num][4]))
                                                
                                            await ctx.send(embed=buy_embed)
                                        
                            else: 
                                await ctx.reply(f"Vous n'avez pas le niveau de forgeron pour pouvoir utiliser cette recette !\nNiveau requis : {res[num][7]}\nNiveau actuel : {data[id]['Forge Level']}") 
                                
                        else:
                            await ctx.reply("Vous n'avez pas débloqué ce plan.")     
                    
            else:
                await ctx.reply(f"Vous n'avez pas le niveau de mineur requis pour accéder à la forge !\nNiveau requis : 10\nNiveau actuel : {data[id]['Level']}")
                
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
                        
        else:
            to_next_level = int(100 * ((data[id]["Forge Level"] / 2) * (data[id]["Forge Level"] / 2)))
            exembed = discord.Embed(title="just Hervey 💎 | 🛠 FORGE 🛠", description="Ici, vous pouvez combiner différent matériaux/objets afin d'en fabriquer de nouveaux grâce à des recettes que vous pouvez débloquer !\n\n```c!forge recipes```  Avoir la liste des différentes recettes\n```c!forge mix```  Combiner deux matériaux ensemble pour réaliser une des recettes et gagner des Points de Forgeron (Niveau de mineur minimal requis : 10)", color=0x59514A)
            exembed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
            exembed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            exembed.add_field(name="", value="", inline=False)
            exembed.add_field(name=":nut_and_bolt: • Points de Forgeron :", value=data[id]["Black-Smith Points"], inline=False)
            exembed.add_field(name="🧔 • Niveau de Forgeron :", value=data[id]["Forge Level"], inline=False)
            exembed.add_field(name="🧪 • Xp actuel :", value=data[id]['Forge Xp'], inline=False)
            exembed.add_field(name="⚗ • Xp jusqu'au prochain niveau :", value=to_next_level, inline=False)
            exembed.set_footer(text="Les Points de Forgeron servent à acheter des objets uniques dans la boutique du forgeron !")
            
            await ctx.send(embed=exembed)
        
