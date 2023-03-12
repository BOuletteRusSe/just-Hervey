
import json, discord, re

async def CheckIfUserIsInGuild(ctx, arg, data):

    user_id = [int(s) for s in re.findall(r'\d+', str(arg[0]))]

    if len(user_id) == 1:

        if user_id[0] in [member.id for member in ctx.guild.members]:
            if user_id[0] == ctx.author.id:
                return 2
            else:
                c_ = True
                for key in data.keys():
                    if key == str(user_id[0]):
                        c_ = False
                if c_:
                    await ctx.reply(f"<@{user_id[0]}> n'est pas inscrit, vous ne pouvez pas voir ses niveaux !")
                    return 1
                else:
                    return 0

        else:
            d = await ctx.reply("Veuillez mentionner un utilisateur étant dans le serveur.\n**c!levels <@utilisateur>**")
            await d.delete(delay=15)
            return 1

    else:
        d = await ctx.reply("Veuillez mentionner un utilisateur étant dans le serveur.\n**c!levels <@utilisateur>**")
        await d.delete(delay=15)
        return 1

async def Levels(ctx, arg, cc):
    
    with open("assets/player_data.json") as data:
        data = json.load(data)

    c = True
    id = str(ctx.author.id)

    for key in data.keys():
        if key == id:
            c = False
    
    if not arg:
        ret = 2
    else:
        ret = await CheckIfUserIsInGuild(ctx, arg, data)
    if ret in [0, 2]:

        if c and ret == 2:
            embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
        else:
            if ret == 0:
                id = re.findall(r'\d+', str(arg[0]))[0]
            
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
            
            to_next_level_3 = int(10 * (int(data[id]["Lj Level"] / 2) * data[id]["Lj Level"]))
            dashConvert3 = int(to_next_level_3 / xpDashes)
            currentDashes3 = int(data[id]['Lj Xp'] / dashConvert3)
            remain3 = xpDashes - currentDashes3
            xpDisplay3 = '━' * currentDashes3
            remainingDisplay3 = '᲼' * remain3
            percent3 = f"{round(data[id]['Lj Xp'])}/{round(to_next_level_3)}"
            space3 = '᲼' * int((len(xpDisplay3) + len(remainingDisplay3)) / 2)
            
            levels_embed = discord.Embed(title="just Hervey 💎 | 🧪 NIVEAUX 🧪", description="Ici, vous pouvez consulter vos niveaux dans les différents métiers disponibles.", color=0x19DF43)
            user = await cc.bot.fetch_user(id)
            levels_embed.set_author(name=user, icon_url=user.avatar_url)
            levels_embed.add_field(name="⛏ • Métier de Mineur :", value=f"Niveau : `{data[id]['Level']}`\nXp : **{data[id]['Level']}|{xpDisplay2}◈**{remainingDisplay2}**|{data[id]['Level'] + 1}**\n{space2}**{percent2}**", inline=False)
            levels_embed.add_field(name="🔨 • Métier de Forgeron :", value=f"Niveau : `{data[id]['Forge Level']}`\nXp : **{data[id]['Forge Level']}|{xpDisplay}◈**{remainingDisplay}**|{data[id]['Forge Level'] + 1}**\n{space}**{percent}**", inline=False)
            levels_embed.add_field(name="🪓 • Métier de Bûcheron :", value=f"Niveau : `{data[id]['Lj Level']}`\nXp : **{data[id]['Lj Level']}|{xpDisplay3}◈**{remainingDisplay3}**|{data[id]['Lj Level'] + 1}**\n{space3}**{percent3}**", inline=False)
            levels_embed.set_footer(text="Pour plus d'informations, vous pouvez directement éxécuter la commande liée à chaque métier.")
            
            await ctx.send(embed=levels_embed)
            