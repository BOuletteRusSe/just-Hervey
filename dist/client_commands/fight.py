


async def Fight(ctx, name):
    if not name:
        deletedMessage = await ctx.reply("Veuillez choisir une cible !\nc!fight **cible** <-- ICI")
        await deletedMessage.delete(delay=15)

    else:
        name_ = ""
        for word in name:
            name_ += word
            name_ += " "

        await ctx.send(f"{ctx.author.mention} a persécuté {name_}")
