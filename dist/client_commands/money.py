import json, re, discord


async def CheckIfUserIsInGuild(ctx, arg):

    """
    0 --> No Problem
    1 --> La mention n'est pas dans le serveur
    2 --> Erreur lors de la mention
    """

    ping = [int(s) for s in re.findall(r'\d+', str(arg[0]))]

    if len(ping) == 1:
        return 0

    else:
        d = await ctx.reply("Veuillez mentionner un utlisateur correcte.")
        await d.delete(delay=15)
        return 2


async def Money(ctx, res, c):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    if not res:

        id = str(ctx.author.id)
        c = True

        for key in data.keys():
            if key == id:
                c = False

        if c:
            embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)

        else:
            money_embed = discord.Embed(color=0x5455b0)
            money_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            money_embed.add_field(name="Argent :", value=data[id]['Money'], inline=False)
            money_embed.add_field(name="Argent en banque :", value=data[id]['Bank'], inline=False)
            money_embed.add_field(name="💎 • Points de Mineur :", value=data[id]["Miner Points"])
            money_embed.add_field(name="🔩 • Points de Forge :", value=data[id]["Black-Smith Points"])
            money_embed.add_field(name="🪓 • Points de Bûcheron :", value=data[id]["Lumberjack Points"])
            await ctx.reply(embed=money_embed)

    elif await CheckIfUserIsInGuild(ctx, res) == 0:

        cc = True
        ping_id = re.findall(r'\d+', str(res[0]))[0]
        user = await c.bot.fetch_user(ping_id)

        for key in data.keys():
            if key == ping_id:
                cc = False

        if cc:
            d = await ctx.reply(f"<@{ping_id}> n'est pas inscrit.")
            await d.delete(delay=15)

        else:
            money_embed = discord.Embed(color=0x5455b0)
            money_embed.set_author(name=user, icon_url=user.avatar_url)
            money_embed.add_field(name="Argent :", value=data[ping_id]['Money'], inline=False)
            money_embed.add_field(name="Argent en banque :", value=data[ping_id]['Bank'], inline=False)
            await ctx.reply(embed=money_embed)
