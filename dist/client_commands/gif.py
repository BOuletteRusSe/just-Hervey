import discord, requests, random
from bs4 import BeautifulSoup
from colored import fg, attr

async def Gif(ctx, gif_, c):

    while True:

        if not gif_:
            search = ""
            for i in range(random.randint(2, 6)):
                _temp = str(random.choice(c.lettres))
                search += _temp
        else:
            search = ""
            for word in gif_:
                search += word
                search += " "

        try:
            url = f"https://tenor.com/search/{search}-gifs"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            gifs = soup.find_all('img', src=True, alt=True, style=True)
            gif_ = random.choice(gifs)
            fUrl = gif_.get('src')

        except:
            if not gif_:
                print(
                    "%sErreur lors du chargement de la commande GIF. Recommencement en cours...%s" % (fg(160), attr(1)))
                continue
            else:
                await ctx.reply("Aucun résultat.")
                break

        embed = discord.Embed(title="**just Hervey 💎 || GIF**", url=fUrl, color=0x110ea4)
        embed.set_image(url=fUrl)
        embed.set_footer(text=f"Requette de {ctx.author}")
        message = await ctx.reply(embed=embed)
        await message.add_reaction("😂")
        await message.add_reaction("😒")
        break
