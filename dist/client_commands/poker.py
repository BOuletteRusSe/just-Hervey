import json, random, re, discord


async def CheckIfUserIsInGuild(ctx, arg):

    """
    0 --> No Problem
    1 --> La mention n'est pas dans le serveur
    2 --> Erreur lors de la mention
    3 --> Auto-Mention
    """

    player_1_id = [int(s) for s in re.findall(r'\d+', str(arg[0]))]

    if len(player_1_id) == 1:

        if player_1_id[0] in [member.id for member in ctx.guild.members]:
            if player_1_id[0] == ctx.author.id:
                d = await ctx.reply("Tu ne peux pas t'auto-mentionner (ptit coquin).")
                await d.delete(delay=15)
                return 3
            else:
                return 0

        else:
            d = await ctx.reply("Veuillez mentionner un utilisateur étant dans le serveur.")
            await d.delete(delay=15)
            return 1

    else:
        d = await ctx.reply("Veuillez mentionner un utlisateur correcte avec qui parier.")
        await d.delete(delay=15)
        return 2


async def IfUserHasEnoughMoney(ctx, arg, player_1_id):

    """
    0 --> No Problem
    1 --> Pas assez de money
    2 --> Valeur incorrecte
    3 --> L'adversaire n'a pas assez de money
    4 --> Vous n'êtes pas incrit
    5 --> L'adversaire n'est pas inscrit
    6 --> Nombre négatif
    """
    
    player_0_id = str(ctx.author.id)

    try:
        pr = int(arg[1])

        if pr <= 0:
            d = await ctx.reply("Vous ne pouvez pas parier 0 ou en dessous de 0 !")
            await d.delete(delay=15)
            return 6
        
        else:

            with open("assets/player_data.json", "r") as data:

                data = json.load(data)
                c = True

                for key in data.keys():
                    if key == player_0_id:
                        c = False

                if c:
                    embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.reply(embed=embed)
                    return 4
                else:

                    c = True

                    for key in data.keys():
                        if key == player_1_id:
                            c = False

                    if c:
                        await ctx.reply(f"<@{player_1_id}> n'est pas inscrit, vous ne pouvez pas parier avec lui !")
                        return 5
                    else:

                        if data[player_0_id]["Money"] >= pr:
                            
                            if data[player_1_id]["Money"] >= pr:

                                return 0

                            else:
                                d = await ctx.reply(f"<@{player_1_id}> n'a pas assez d'argent pour parier {pr}€ !")
                                await d.delete(delay=15)
                                return 3

                        else:
                            d = await ctx.reply(f"Vous n'avez pas assez d'argent pour parier {pr}€ !")
                            await d.delete(delay=15)
                            return 1

    except:
        d = await ctx.reply("Veuillez sélectionner un montant valide.")
        await d.delete(delay=15)
        return 2


async def IfPlayer1IsOk(ctx, player_1_id, pr, c):
    """
    0 --> No Probem
    1 --> Player 1 pas d'accord
    2 --> Pas de réponse
    """

    player_0_id = str(ctx.author.id)

    message = await ctx.send(f"<@{player_1_id}>, {ctx.author.mention} veut parier {pr}€ avec vous.\n✅ --> **Accepter**\n❌ --> **Décliner**")
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    def CheckEmoji(reaction, user):
        return player_1_id == str(user.id) and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    try:
        reaction, user = await c.bot.wait_for("reaction_add", timeout=60, check=CheckEmoji)

        if reaction.emoji == "✅":
            return 0
        else:
            await ctx.reply("Demande refusée.")
            return 1

    except:
        await ctx.reply("Délai dépassé.")
        await message.delete()
        return 2


async def Poker(ctx, arg, c):

    if not arg:
        await ctx.reply("Veuillez mentionner un utilisateur et préciser un montant.\n")

    elif await CheckIfUserIsInGuild(ctx, arg) == 0:
        player_1_id = re.findall(r'\d+', str(arg[0]))[0]
        if await IfUserHasEnoughMoney(ctx, arg, player_1_id) == 0:
            pr = int(arg[1])
            if await IfPlayer1IsOk(ctx, player_1_id, pr, c) == 0:
                
                player_0_id = str(ctx.author.id)
                c = random.choice([True, False])

                with open("assets/player_data.json", "r") as data:
                    data = json.load(data)

                    if c:
                        data[player_1_id]["Money"] = round(data[player_1_id]["Money"] - pr, 2)
                        data[player_0_id]["Money"] = round(data[player_0_id]["Money"] + pr, 2)
                        await ctx.send(f"{ctx.author.mention} a gagné {pr}€ !\n<@{player_1_id}> vous perdez {pr}€.")
                    else:
                        data[player_1_id]["Money"] = round(data[player_1_id]["Money"] + pr, 2)
                        data[player_0_id]["Money"] = round(data[player_0_id]["Money"] - pr, 2)
                        await ctx.send(f"<@{player_1_id}> a gagné {pr}€ !\n{ctx.author.mention} vous perdez {pr}€.")

                    with open("assets/player_data.json", 'w') as d:
                        json.dump(data, d, indent=4)
