import random, json


async def Loto(ctx, m):

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
        if not m:
            d = await ctx.reply("Veuillez sélectionner une valeur à parier ! || c!loto **valeur**")
            await d.delete(delay=15)
        else:
            try:
                m = m[0]
                m = float(m)
                round(m, 2)

                if m <= 0:
                    await ctx.reply("Vous ne pouvez pas faire ça !")

                elif data[id]['Money'] - m < 0:
                    await ctx.reply(f"Vous n'avez pas assez d'argent !\nArgent : **{data[id]['Money']}**")
                else:
                    r = random.choice([True, False])
                    if r:
                        data[id]['Money'] += m
                        await ctx.reply(f"Gagné !\nArgent : **{data[id]['Money']}**")
                    else:
                        data[id]['Money'] -= m
                        await ctx.reply(f"Perdu !\nArgent : **{data[id]['Money']}**")
                        if data[id]['Money'] <= 0:
                            await ctx.reply("Vous n'avez plus d'argent !\n(**c!work** pour travailler sale chômeur)")
                with open("assets/player_data.json", 'w') as d:
                    json.dump(data, d, indent=4)
            except:
                deleted_message = await ctx.reply("Veuillez choisir une valeur correcte || c!loto **valeur**")
                await deleted_message.delete(delay=15)
