import random


async def Ping(ctx, arg):
    
    if not arg:
        id = random.randint(100000000000000000, 999999999999999999)
        await ctx.reply(f"<@{id}>")
    else:
        try:
            n = int(arg[0])
        except:
            await ctx.reply("Veuillez entrer un nombre valide après la commande !")
        else:
            
            if 1 <= n <= 50:
                t = str()
                for i in range(n):
                    t += f"<@{random.randint(100000000000000000, 999999999999999999)}> "
                await ctx.reply(t)
            else:
                await ctx.reply("Veuillez entrer un nombre valide après la commande !")