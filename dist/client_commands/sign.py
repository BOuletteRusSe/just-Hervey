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
            "Forge Points" : 0,
            "Forge Cooldown" : {"": 0},
            "Bank": 0,
            "Level": 0,
            "Xp": 0,
            "Hobby": None,
            "Ticket": 0,
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
                "Platinium Alliage": False,
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
                "P Forge" : [
                ]
            }
        }

        with open("assets/player_data.json", 'w') as d:
            json.dump(data, d, indent=4)

        sign_embed = discord.Embed(description="Vous vous êtes inscrit avec succès !", color=0xc3b828)
        sign_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        sign_embed.set_image(url="https://cdn.discordapp.com/attachments/772467241014919179/881885893638631464/819043164534079539.gif")
        await ctx.reply(embed=sign_embed)
    
    else:
        d = await ctx.reply("Vous êtes déjà inscrit !")
        await d.delete(delay=15)