import discord, json
from assets.minerals_data import minerals
from assets.recipes_data import recipes

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
                deleteMessage = await ctx.reply('Malheureusement, la commande n\'est pas encore finis pour le moment ! 😿\nCette partie de la commande sera disponible dans de futures mises à jour donc restez actif !')
                await deleteMessage.delete(delay=10)
                
        elif "recipes" in arg:
            recipe_embed = discord.Embed(title=":nut_and_bolt: | Forge Recipes", description="Pour réaliser une des recettes ci-dessus utilisez la commande **c!forge mix** suivit de la recette (en anglais).\nEx pour la magnétite: **c!forge mix** *iron* + *gold*", color=0x556b2f)
            __input__ = dict()
            __output__ = dict()
            inputs = str()
            outputs = str()
            for k, v in recipes.items():
                for _k, _v in v.items():
                    if _k == "emoji": __emoji__ = _v
                    elif _k == "points": __points__ = _v
                    elif _k == "cooldown": __cooldown__ = _v
                    elif _k  in ["input", "output"]:
                        for __k, __v in _v.items():
                            if _k == "input": __input__[__k] = __v
                            else: __output__[__k] = __v
                for _k_, _v_ in __input__.items():
                    inputs += f"**{_v_} {_k_}** + "
                inputs = inputs[:-3]
                for _k_, _v_ in __output__.items():
                    outputs += f"**{_v_} {_k_}** + "
                outputs = outputs[:-3]
        
                recipe_embed.add_field(name=f"{__emoji__} • {k} Recipe :", value=f"Recette : {inputs} --> {outputs}\nCooldown : **{__cooldown__}s**\nPoints de Forge : **{__points__}**", inline=False)

            await ctx.reply(embed=recipe_embed)
                        
        else: 
            exembed = discord.Embed(title="🛠 FORGE 🛠", description="Ici, vous pouvez combiner différent matériaux/objets afin d'en fabriquer de nouveaux !\n\n**c!forge recipes** : Avoir la liste des différentes recettes\n\n**c!forge mix** : Combiner deux matériaux ensemble pour réaliser une des recettes et gagner des Points de Forge", color=0x59514A)
            exembed.set_image(url="https://i.ibb.co/DgDTy5J/forge-icon.png")
            exembed.add_field(name="", value="", inline=False)
            exembed.add_field(name=":nut_and_bolt: • Points de Forge :", value=data[id]["Forge Points"], inline=False)
            exembed.set_footer(text="Dans de futures mises à jour, les Points de Forge serviront à acheter des objets uniques dans la boutique du forgeron !")
            
            await ctx.reply(embed=exembed)
        
