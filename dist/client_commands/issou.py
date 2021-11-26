
import requests

async def Issou(ctx):
    
    r = requests.get('https://issoutv.com/videos/random/sfw')
    url = r.url
    await ctx.reply(url)
