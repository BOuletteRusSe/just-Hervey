import discord, requests, random
from bs4 import BeautifulSoup
from colored import fg, attr


async def Ph(ctx):

    url = "https://fr.pornhub.com/"
    r = requests.get(url)

    while True:

        if r.ok:
            soup = BeautifulSoup(r.text, "html.parser")
            try:
                titresPh = soup.find_all('span', {'class': 'title'})
                titrePh = random.choice(titresPh)
                titrePh = titrePh.find('a')
                embed = discord.Embed(title="**just Hervey 💎 || PORNHUB TITLE**", description=f'**{titrePh.text}**',
                            color=0xf24f00)
                embed.set_thumbnail(
                    url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Pornhub-logo.svg/1280px-Pornhub-logo.svg.png")
                phMessage = await ctx.reply(embed=embed)

            except:
                print("%sErreur lors du scraping de la commande PH. Recommencement en cours...%s" % (
                    fg(160), attr(1)))
                continue

            await phMessage.add_reaction("🥵")
            await phMessage.add_reaction("🤮")
            break

        else:
            print(
                "%sErreur lors du chargement de la commande PH. Recommencement en cours...%s" % (fg(160), attr(1)))
            continue
