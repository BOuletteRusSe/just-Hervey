import requests

async def Drug(ctx):
    
    url = "https://psychonautwiki.org/wiki/Special:Random"
    r = requests.get(url)
        
    await ctx.reply(r.url)
