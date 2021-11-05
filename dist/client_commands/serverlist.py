import discord
from discord.embeds import Embed


async def ServerList(ctx, c):
    
    if ctx.author.id == 598900088768692348:

        server_list_embed = discord.Embed(title="Servers List", color=0x6228b8)
        server_list_embed.set_footer(text="Admin Command")

        for guild in c.bot.guilds:
            server_list_embed.add_field(name=guild, value=f"Membres : {len(guild.members)}", inline=False)

        await ctx.reply(embed=server_list_embed)

    else:

        deletedMessage = await ctx.reply("Vous n'avez pas les permissions de faire cela !")
        await deletedMessage.delete(delay=15)
