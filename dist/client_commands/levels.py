
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
        await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")
    else:
        
        levels_embed = discord.Embed(title="just Hervey 💎 | 🧪 NIVEAUX 🧪", description="Ici, vous pouvez consulter vos niveaux dans les différents métiers disponibles.", color=0x19DF43)
        levels_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        levels_embed.add_field(name="⛏ Métier de Mineur :", value=f"Niveau : `{data[id]['Level']}`\nXp : `{int(data[id]['Xp'])}`", inline=False)
        levels_embed.add_field(name="🔨 Métier de Forgeron :", value=f"Niveau : `{data[id]['Forge Level']}`\nXp : `{int(data[id]['Forge Xp'])}`", inline=False)
        levels_embed.set_footer(text="Pour plus d'informations, vous pouvez directement éxécuter la commande liée à chaque métier.")
        
        await ctx.send(embed=levels_embed)
