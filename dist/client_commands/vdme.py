import discord, requests
from bs4 import BeautifulSoup
from colored import fg, attr

async def Vdme(ctx):

    url = "https://www.viedemerde.fr/aleatoire/epicees"
    r = requests.get(url)

    while True:

        if r.ok:
            soup = BeautifulSoup(r.text, "html.parser")
            vdmAleatoire = soup.find('div', {"class": 'panel'})
            vdmContent = vdmAleatoire.find("span", {'class': "spicy-hidden"}).text
            link = f"https://www.viedemerde.fr{vdmAleatoire.find('a', {'class': 'article-link'}).get('href')}"
            author = vdmAleatoire.find("div")
            embed = discord.Embed(title="**just Hervey 💎 || VDM ÉPICÉE**", url=link, color=0x830707,
                        description=vdmContent)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Logo_vdm.png")
            embed.set_footer(text=author.text)
            vdmMessage = await ctx.reply(embed=embed)
            await vdmMessage.add_reaction("👍")
            await vdmMessage.add_reaction("👎")
            break

        else:
            print("%sErreur lors du chargement du VDM. Recommencement en cours...%s" % (fg(160), attr(1)))
            continue
