import discord, json, time
from assets.recipes_data import recipes

def EnumerateRecipes():
    result = list()
    for k, v in recipes.items():
        __input__ = dict()
        __output__ = dict()
        for _k, _v in v.items():
            if _k == "emoji": __emoji__ = _v
            elif _k == "points": __points__ = _v
            elif _k == "cooldown": __cooldown__ = _v
            elif _k == "command": __command__ = _v
            elif _k == "price": __price__ = _v
            elif _k  in ["input", "output"]:
                for __k, __v in _v.items():
                    if _k == "input": __input__[__k] = __v
                    else: __output__[__k] = __v

        result += [[__emoji__, k, __input__, __output__, __cooldown__, __points__, __command__, __price__]]   
        
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
            content = ""
            for word in arg:
                if word != "mix":
                    content += word
                    content += " "
            if content == "":
                deleteMessage = await ctx.reply("Pour réaliser une des recettes, utilisez la commande **c!forge mix** suivit de la recette (en anglais).\nEx pour la magnétite : **c!forge mix** *iron* + *gold*")
                await deleteMessage.delete(delay=15)

            else:
                
                def IfCommandIsCorrect(arg):
                    global num
                    for i in range(len(res)):
                        if arg in res[i][6]:
                            num = i
                            return True
                    return False
                
                arg = arg[1:]
                arg = str(arg).lower()
                res = EnumerateRecipes()
                
                if not IfCommandIsCorrect(arg):
                    deleteMessage = await ctx.reply("La commande est incorrecte ou la recette n'existe pas. Pour réaliser une des recettes, utilisez la commande **c!forge mix** suivit de la recette (en anglais).\nEx pour la magnétite : **c!forge mix** *iron* + *gold*")
                    await deleteMessage.delete(delay=15)
                else:
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
                        
                        if (data[id]["Money"] - res[num][7]) < 0:
                            deleteMessage = await ctx.reply("Vous n'avez malheureusement pas assez d'argent pour acheter **%s**.\nArgent requis : **%s**\nArgent actuel : **%s**" % (res[num][1], res[num][7], data[id]["Money"]))
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
                                data[id]["Forge Cooldown"] = {str(time.time()): res[num][4]}
                                data[id]["Forge Points"] += res[num][5]
                                data[id]["Money"] -= res[num][7]
                                for k, v in res[num][3].items():
                                    data[id]["Inventory"][k] += v
                                    
                                with open("assets/player_data.json", 'w') as d:
                                    json.dump(data, d, indent=4)
                                    
                                buy_embed = discord.Embed(title="🛠 FORGE 🛠", description="Forge de **%s**" % (res[num][1]), color=0xC0712C)
                                buy_embed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
                                buy_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                                buy_embed.add_field(name="", value="")
                                buy_embed.add_field(name=":nut_and_bolt: • Points de Forge :", value=data[id]["Forge Points"])
                                buy_embed.add_field(name="💸 • Argent :", value=round(data[id]["Money"], 2))
                                for k, v in res[num][2].items():
                                    buy_embed.add_field(name=f"{k} : ", value=data[id]["Inventory"][k])
                                for k, v in res[num][3].items():
                                    buy_embed.add_field(name=f"{k} : ", value=data[id]["Inventory"][k])
                                buy_embed.set_footer(text="Vous devez maintenant vous reposer pendant %ss afin de pouvoir réutiliser la commande c!forge !" % (res[num][4]))
                                
                                await ctx.send(embed=buy_embed)
                            
                            """deleteMessage = await ctx.reply('Malheureusement, la commande n\'est pas encore finis pour le moment ! 😿\nCette partie de la commande sera disponible dans de futures mises à jour donc restez actif !')
                            await deleteMessage.delete(delay=10)"""
                
        elif "recipes" in arg:
            recipe_embed = discord.Embed(title=":nut_and_bolt: | Forge Recipes", description="Pour réaliser une des recettes ci-dessus utilisez la commande **c!forge mix** suivit de la recette (en anglais).\nEx pour la magnétite: **c!forge mix** *iron* + *gold*", color=0x556b2f)
            res = EnumerateRecipes()
            for i in range(len(res)):
                inputs = str()
                outputs = str()
                for _k_, _v_ in res[i][2].items():
                    inputs += f"**{_v_} {_k_}** + "
                inputs = inputs[:-3]
                for _k_, _v_ in res[i][3].items():
                    outputs += f"**{_v_} {_k_}** + "
                outputs = outputs[:-3]
                
                recipe_embed.add_field(name=f"{res[i][0]} • {res[i][1]} Recipe :", value=f"Recette : {inputs} --> {outputs}\nCooldown : **{res[i][4]}s**\nPoints de Forge : **{res[i][5]}**\nArgent : **{res[i][7]}**", inline=False)
            
            await ctx.reply(embed=recipe_embed)
                        
        else: 
            exembed = discord.Embed(title="🛠 FORGE 🛠", description="Ici, vous pouvez combiner différent matériaux/objets afin d'en fabriquer de nouveaux !\n\n**c!forge recipes** : Avoir la liste des différentes recettes\n\n**c!forge mix** : Combiner deux matériaux ensemble pour réaliser une des recettes et gagner des Points de Forge", color=0x59514A)
            exembed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
            exembed.add_field(name="", value="", inline=False)
            exembed.add_field(name=":nut_and_bolt: • Points de Forge :", value=data[id]["Forge Points"], inline=False)
            exembed.set_footer(text="Dans de futures mises à jour, les Points de Forge serviront à acheter des objets uniques dans la boutique du forgeron !")
            
            await ctx.reply(embed=exembed)
        
