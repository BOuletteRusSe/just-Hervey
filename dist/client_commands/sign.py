import json, discord


async def Sign(ctx):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    id = str(ctx.author.id)
    c = True

    for key in data.keys():
        if key == id:
            c = False

    if c:
        data[id] = {
            "Money": 100,
            "Black-Smith Points" : 0,
            "Miner Points": 0,
            "Forge Cooldown" : {"": 0},
            "Last Daily": 1677343207.8307042,
            "Bank": 0,
            "Level": 1,
            "Forge Level": 1,
            "Lj Level": 1,
            "Lj Xp": 0,
            "Lj Points": 0,
            "Xp": 0,
            "Forge Xp": 0,
            "Ticket": 0,
            "Miner Ticket": 0,
            "Inventory": {
                "Jade": 0, 
                "Cooper": 0, 
                "Coal": 0, 
                "Fluorite": 0, 
                "Debrit": 0, 
                "Obsidian": 0, 
                "Turquoise": 0, 
                "Mercury": 0, 
                "Coke": 0, 
                "Stone": 0, 
                "Iron": 0, 
                "Gold": 0, 
                "Silver": 0,
                "Diamond": 0, 
                "Rubis": 0, 
                "Saphir": 0, 
                "Platinium": 0, 
                "Randomite": 0, 
                "Magma Stone": 0, 
                "Joseph": 0, 
                "Sacred Stone": 0, 
                "Cobalt": 0, 
                "Fossil": 0, 
                "Emerald": 0, 
                "Grenat": 0, 
                "Amethist": 0,
                "Magnetite": 0,
                "Lucky Stone": 0,
                "Aigue Marine": 0,
                "Uranium": 0,
                "Plutonium": 0,
                "Quartz": 0,
                "Dragonite": 0,
                "Mithril": 0,
                "Dark Stone": 0,
                "Cursed Stone": 0,
                "Black Mithril": 0,
                "Fengarite": 0,
                "Iliosite": 0,
                "Alliages": [],
                "Rank": 0,
                "Item Limit": 1,
                "MP": [
                    0
                ],
                "P Item": [
                    0
                ],
                "P Rank": [
                    0
                ],
                "Plans": [],
                "P Forge" : [
                ]
            },
            "Inventory_2" : {}
        }
        

        with open("assets/player_data.json", 'w') as d:
            json.dump(data, d, indent=4)

        sign_embed = discord.Embed(title="Vous vous êtes inscrit avec succès !", description="Dans un monde fantastique, les **dieux** avaient toujours été neutres et n'avaient jamais pris parti dans les conflits des **mortels**.\n\nCependant, un jour, une **guerre** éclata entre les **dieux** eux-mêmes. Personne ne sait comment ni pourquoi cette **guerre** a commencé, mais elle a été si destructrice que les **dieux** ont finalement convenu de faire une **trêve**.\n\nDes **milliers d'années** se sont écoulées depuis la fin de la **guerre**, et la plupart des **mortels** ont oublié l'existence de ces **divinités**.\n\nCependant, les traces de cette **guerre** sont toujours présentes dans le monde. Les **ruines des cités divines**, les **vestiges des champs de bataille** et les **artefacts magiques** sont éparpillés à travers le monde, attendant d'être découverts par un **aventurier curieux**.", color=0xc3b828)
        sign_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        sign_embed.set_image(url="https://cdn.discordapp.com/attachments/772467241014919179/881885893638631464/819043164534079539.gif")
        await ctx.reply(embed=sign_embed)
    
    else:
        sign_embed = discord.Embed(title="Vous êtes déjà inscrit avec succès !", description="Dans un monde fantastique, les **dieux** avaient toujours été neutres et n'avaient jamais pris parti dans les conflits des **mortels**.\n\nCependant, un jour, une **guerre** éclata entre les **dieux** eux-mêmes. Personne ne sait comment ni pourquoi cette **guerre** a commencé, mais elle a été si destructrice que les **dieux** ont finalement convenu de faire une **trêve**.\n\nDes **milliers d'années** se sont écoulées depuis la fin de la **guerre**, et la plupart des **mortels** ont oublié l'existence de ces **divinités**.\n\nCependant, les traces de cette **guerre** sont toujours présentes dans le monde. Les **ruines des cités divines**, les **vestiges des champs de bataille** et les **artefacts magiques** sont éparpillés à travers le monde, attendant d'être découverts par un **aventurier curieux**.", color=0xc3b828)
        sign_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        sign_embed.set_image(url="https://cdn.discordapp.com/attachments/772467241014919179/881885893638631464/819043164534079539.gif")
        await ctx.reply(embed=sign_embed)