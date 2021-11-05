import discord, requests
from bs4 import BeautifulSoup
from colored import fg, attr

async def Vdm(ctx):

    url = "https://www.viedemerde.fr/aleatoire"
    r = requests.get(url)

    while True:

        if r.ok:
            soup = BeautifulSoup(r.text, "html.parser")
            vdmAleatoire = soup.find('article', {'class': 'bg-white'})
            vdmContent = vdmAleatoire.find("a", {'class': "block"})
            link = f"https://www.viedemerde.fr{vdmContent}"
            author = vdmAleatoire.find("div", {'class': 'flex'})
            embed = discord.Embed(title="**just Hervey 💎 || VDM**", url=link, color=0x0e9a98, description=vdmContent.text)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Logo_vdm.png")
            embed.set_footer(text=author.text)
            vdmMessage = await ctx.reply(embed=embed)
            await vdmMessage.add_reaction("👍")
            await vdmMessage.add_reaction("👎")
            break

        else:
            print("%sErreur lors du chargement du VDM. Recommencement en cours...%s" % (fg(160), attr(1)))
            continue
