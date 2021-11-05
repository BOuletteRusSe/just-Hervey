import discord


async def Say(ctx, text):

    if not text:
        dele = await ctx.reply("Veuillez préciser un texte à dire !\nc!say **text**.")
        await dele.delete(delay=10)

    else:
        text_ = ""
        for word in text:
            text_ += word
            text_ += " "
        
        embed = discord.Embed(description=text_, color=0xcd7918)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=ctx.guild)
        await ctx.send(embed=embed)
        await ctx.message.delete()
