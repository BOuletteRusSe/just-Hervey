import discord


async def Logs(ctx):

    if ctx.author.id == 598900088768692348:

        logs_embed = discord.Embed(title="Logs", color=0xa20b0b)
        logs_embed.set_footer(text="Admin Command")

        n = 11

        with open('logs.log', 'r', encoding='utf8') as f:
            for line in f.readlines()[-10:]:
                n -= 1
                logs_embed.add_field(name=n, value=line, inline=False)

        await ctx.reply(embed=logs_embed)

    else:

        deletedMessage = await ctx.reply("Vous n'avez pas les permissions de faire cela !")
        await deletedMessage.delete(delay=15)
