import discord, json
from assets.minerals_data import minerals
from assets.recipes_data import recipes

def EnumerateRecipes():
    __input__ = dict()
    __output__ = dict()
    result = list()
    for k, v in recipes.items():
        for _k, _v in v.items():
            if _k == "emoji": __emoji__ = _v
            elif _k == "points": __points__ = _v
            elif _k == "cooldown": __cooldown__ = _v
            elif _k == "command": __command__ = _v
            elif _k  in ["input", "output"]:
                for __k, __v in _v.items():
                    if _k == "input": __input__[__k] = __v
                    else: __output__[__k] = __v

        result += [[__emoji__, k, __input__, __output__, __cooldown__, __points__, __command__]]   
        
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
                    for i in range(len(res)):
                        if arg in res[i][6]:
                            return True
                    return False
                
                arg = arg[1:]
                arg = str(arg).lower()
                res = EnumerateRecipes()
                print(arg)
                
                if not IfCommandIsCorrect(arg):
                    deleteMessage = await ctx.reply("La commande est incorrecte ou la recette n'existe pas. Pour réaliser une des recettes, utilisez la commande **c!forge mix** suivit de la recette (en anglais).\nEx pour la magnétite : **c!forge mix** *iron* + *gold*")
                    await deleteMessage.delete(delay=15)
                else:
                    deleteMessage = await ctx.reply('Malheureusement, la commande n\'est pas encore finis pour le moment ! 😿\nCette partie de la commande sera disponible dans de futures mises à jour donc restez actif !')
                    await deleteMessage.delete(delay=10)
                
        elif "recipes" in arg:
            recipe_embed = discord.Embed(title=":nut_and_bolt: | Forge Recipes", description="Pour réaliser une des recettes ci-dessus utilisez la commande **c!forge mix** suivit de la recette (en anglais).\nEx pour la magnétite: **c!forge mix** *iron* + *gold*", color=0x556b2f)
            res = EnumerateRecipes()
            print(res)
            for i in range(len(res)):
                inputs = str()
                outputs = str()
                for _k_, _v_ in res[i][2].items():
                    inputs += f"**{_v_} {_k_}** + "
                inputs = inputs[:-3]
                for _k_, _v_ in res[i][3].items():
                    outputs += f"**{_v_} {_k_}** + "
                outputs = outputs[:-3]
                
                recipe_embed.add_field(name=f"{res[i][0]} • {res[i][1]} Recipe :", value=f"Recette : {inputs} --> {outputs}\nCooldown : **{res[i][4]}s**\nPoints de Forge : **{res[i][5]}**", inline=False)
            
            await ctx.reply(embed=recipe_embed)
                        
        else: 
            exembed = discord.Embed(title="🛠 FORGE 🛠", description="Ici, vous pouvez combiner différent matériaux/objets afin d'en fabriquer de nouveaux !\n\n**c!forge recipes** : Avoir la liste des différentes recettes\n\n**c!forge mix** : Combiner deux matériaux ensemble pour réaliser une des recettes et gagner des Points de Forge", color=0x59514A)
            exembed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
            exembed.add_field(name="", value="", inline=False)
            exembed.add_field(name=":nut_and_bolt: • Points de Forge :", value=data[id]["Forge Points"], inline=False)
            exembed.set_footer(text="Dans de futures mises à jour, les Points de Forge serviront à acheter des objets uniques dans la boutique du forgeron !")
            
            await ctx.reply(embed=exembed)
        
