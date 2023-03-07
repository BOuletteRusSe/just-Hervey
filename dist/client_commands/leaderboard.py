import discord, json
from assets.items_price import item_shop_price, item_shop_price_2


async def Leaderboard(ctx, cc):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    t = {}
    r = {}

    for key in data.keys():
        t[key] = data[key]["Money"]

    for key in data.keys():
        t[key] += data[key]["Bank"]

    for key in t.keys():
        try:
            r[key] = item_shop_price[data[key]["Inventory"]["Rank"]]["Name"]
        except:
            continue

    embed = discord.Embed(title="just Hervey 💎 | 📈 Money Leaderboard", description="Voici le classement des joueurs en fonction de leur argent.", color=0x9c9abc)

    for k, v in sorted(t.items(), key=lambda x: x[1], reverse=True):
        if k in r.keys():
            embed.add_field(name=f"__{await cc.bot.fetch_user(k)}__ [{r[k]}]", value=f"<@{k}> • `{v}`", inline=False)
        else:
            embed.add_field(name=f"__{await cc.bot.fetch_user(k)}__", value=f"<@{k}> • `{v}`", inline=False)

    await ctx.reply(embed=embed)
