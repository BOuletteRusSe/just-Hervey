import discord, json
from assets.items_price import item_shop_price, item_shop_price_2


async def Leaderboard(ctx):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    t = {}
    r = {}
    tb = []
    ll = {}

    for key in data.keys():
        t[key] = data[key]["Money"]

    for key in data.keys():
        t[key] += data[key]["Bank"]

    for key in t.keys():
        try:
            r[key] = item_shop_price[data[key]["Inventory"]["Rank"]]["Name"]
        except:
            continue

    for key in data.keys():
            ll[key] = data[key]["Level"]


    for k, v in sorted(t.items(), key=lambda x: x[1], reverse=True):
        if k in (ll.keys() and r.keys()):
            tb.append(f"{ll[k]} | <@{k}> [{r[k]}] : {v}\n")
        else:
            tb.append(f"<@{k}> : {v}\n")

    d = ""
    for e in tb:
        d += f"{e}\n"

    embed=discord.Embed(title="Money Leaderboard", description=d, color=0x9c9abc)
    await ctx.reply(embed=embed)
