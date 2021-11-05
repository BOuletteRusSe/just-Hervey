import discord, requests, random
from bs4 import BeautifulSoup
from colored import fg, attr


async def Nude(ctx):

    if ctx.channel.is_nsfw():

        while True:

            url = "https://fr.pornhub.com"
            r = requests.get(url)

            if r.ok:
                soup = BeautifulSoup(r.text, "html.parser")

                nudeImages = soup.find_all('a',
                                        {
                                            'class': 'fade fadeUp videoPreviewBg linkVideoThumb js-linkVideoThumb img'})
                nudeImage = random.choice(nudeImages)
                nudeImage = nudeImage.find('img')
                nudeImage = nudeImage.get("data-src")
                embed = discord.Embed(title=f"**just Hervey 💎 || NUDE**", color=0xa40e93, url=nudeImage)
                embed.set_image(url=nudeImage)
                nudeMessage = await ctx.reply(embed=embed)
                await nudeMessage.add_reaction("❤")
                await nudeMessage.add_reaction("💔")
                break

            else:
                print("%sErreur lors du chargement de la commande nude. Recommencement en cours...%s" % (
                    fg(160), attr(1)))
                continue

    else:
        print(f"%s{ctx.author} a fait la commande !nude dans un salon hors NSFW%s" % (fg(126), attr(1)))
        alertMessage = await ctx.reply("Cette commande n'est seulement exécutable que dans un salon NSFW !")
        await alertMessage.delete(delay=15)
