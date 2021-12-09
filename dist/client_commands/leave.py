

async def CheckVoice(ctx):
    for user in ctx.guild.members: 
        if user.id == 820344845918797854 and user.voice is None:
            d = await ctx.reply('Le bot n\'est pas connecté dans un salon vocal !')
            await d.delete(delay=15)
            return False
    if ctx.author.voice is None:
        d = await ctx.reply('Vous devez être dans un salon vocal pour pouvoir éxecuter cette commande !')
        await d.delete(delay=15)
        return False
    for user in ctx.guild.members: 
        if user.id == 820344845918797854:
            if ctx.author.voice.channel != user.voice.channel:
                d = await ctx.reply('Vous devez être dans le même salon vocal que le bot pour pouvoir le déconnecter !')
                await d.delete(delay=20)
                return False        
    return True

async def Leave(ctx):
    
    if await CheckVoice(ctx): 
        await ctx.voice_client.disconnect()
        await ctx.reply('Salon vocal quitté avec succès.')
