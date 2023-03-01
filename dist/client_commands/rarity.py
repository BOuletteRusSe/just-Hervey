
import discord


async def Rarity(ctx):
    
    
    rarity_embed = discord.Embed(title="just Hervey 💎 | 🎰 RARETÉS 🎰", description="Voici toutes les classes de raretés du jeu.", color=0xEEAC0A)
    rarity_embed.add_field(name="🟢 • Commun", value="Le plus courant, vous devriez en avoir beaucoup si vous jouez depuis au moins 5 secondes.", inline=False)
    rarity_embed.add_field(name="🔵 • Peu Commun", value="Un peu plus compliqué à trouver que le `commun`, après quelques minutes de jeu, vous trouverez vos premiers objets `peu communs`.", inline=False)
    rarity_embed.add_field(name="🟡 • Rare", value="Il faut avoir un peu plus de chance pour trouver des objets `rares` mais cela reste tout à fait envisageable.", inline=False)
    rarity_embed.add_field(name="🟣 • Épique", value="Les objets `épiques` demandent plus de temps pour être trouvés, vous devriez être assez content lorsque vous en trouvez.", inline=False)
    rarity_embed.add_field(name="🟠 • Légendaire", value="Les objets `légendaires` sont extrèmements rares et nécéssite beacoup de temps afins d'être trouvés, il vous faudra de la détermination !", inline=False)
    rarity_embed.add_field(name="🔴 • Mythique", value="Comme indiqué, ce sont des objets `mythiques`, personne ne les a jamais vu, mais pourtant ils sont biens présents, si vous en trouvez, vous êtes parmis les plus chanceux !", inline=False)
    rarity_embed.add_field(name="🟤 • Reliques", value="Les `reliques` sont d'une rareté inestimable, non pas qu'ils soient rares, mais qu'ils soient limités et peu détenus.", inline=False)
    rarity_embed.add_field(name="⚫ • Black Market", value="Les objets du `black market` sont des objets obtensibles presque uniquement via le Black Market. Leur détention risque d'attirer la colère des dieux.", inline=False)
    rarity_embed.add_field(name="⚪ • Divin", value="Les objets `divins`, si on peut encore apeller ça des objets, ne sont pas classables dans une échelle de rareté comme celle-ci. Si vous en trouvez, gardez le bien précieusement, vous serez peut-être le seul...", inline=False)
    
    await ctx.reply(embed=rarity_embed)