
import json, discord

async def Levels(ctx):
    
    with open("assets/player_data.json") as data:
        data = json.load(data)

    c = True
    id = str(ctx.author.id)

    for key in data.keys():
        if key == id:
            c = False

    if c:
        embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        
        xpDashes = 25
        to_next_level = int(100 * ((data[id]["Forge Level"] / 2) * (data[id]["Forge Level"] / 2)))
        dashConvert = int(to_next_level / xpDashes)
        currentDashes = int(data[id]['Forge Xp'] / dashConvert)
        remain = xpDashes - currentDashes
        xpDisplay = '━' * currentDashes
        remainingDisplay = '᲼' * remain
        percent = f"{round(data[id]['Forge Xp'])}/{round(to_next_level)}"
        space = '᲼' * int((len(xpDisplay) + len(remainingDisplay)) / 2)
        
        to_next_level_2 = int(10 * (int(data[id]["Level"] / 2) * data[id]["Level"]))
        dashConvert2 = int(to_next_level_2 / xpDashes)
        currentDashes2 = int(data[id]['Xp'] / dashConvert2)
        remain2 = xpDashes - currentDashes2
        xpDisplay2 = '━' * currentDashes2
        remainingDisplay2 = '᲼' * remain2
        percent2 = f"{round(data[id]['Xp'])}/{round(to_next_level_2)}"
        space2 = '᲼' * int((len(xpDisplay2) + len(remainingDisplay2)) / 2)
        
        levels_embed = discord.Embed(title="just Hervey 💎 | 🧪 NIVEAUX 🧪", description="Ici, vous pouvez consulter vos niveaux dans les différents métiers disponibles.", color=0x19DF43)
        levels_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        levels_embed.add_field(name="⛏ Métier de Mineur :", value=f"Niveau : `{data[id]['Level']}`\nXp : **{data[id]['Level']}|{xpDisplay2}◈**{remainingDisplay2}**|{data[id]['Level'] + 1}**\n{space2}**{percent2}**", inline=False)
        levels_embed.add_field(name="🔨 Métier de Forgeron :", value=f"Niveau : `{data[id]['Forge Level']}`\nXp : **{data[id]['Forge Level']}|{xpDisplay}◈**{remainingDisplay}**|{data[id]['Forge Level'] + 1}**\n{space}**{percent}**", inline=False)
        levels_embed.set_footer(text="Pour plus d'informations, vous pouvez directement éxécuter la commande liée à chaque métier.")
        
        await ctx.send(embed=levels_embed)
