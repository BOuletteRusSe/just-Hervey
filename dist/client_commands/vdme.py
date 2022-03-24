import discord, requests
from bs4 import BeautifulSoup

async def Vdme(ctx):
    
    while True:
        try:
        
            response = requests.get("https://www.viedemerde.fr/aleatoire/epicees")
            soup = BeautifulSoup(response.text, "html.parser")

            article = soup.find('article')
            by = article.find("p", {"class": "text-blue-300 text-sm mt-2"}).text
            content = article.find("a", {"class": "block text-blue-500 my-4 spicy-hidden"})
            counters = article.find("div", {"class": "md:flex md:justify-between my-4 w-full flex-wrap"}).find_all('div')
            counter_a = counters[0].find("span", {"class": "rounded-r pr-4 py-3 md:py-2 font-bold bg-blue-500 text-xs text-right whitespace-nowrap w-20 vote-btn-count"}).text
            counter_b = counters[1].find("span", {"class": "rounded-r pr-4 py-3 md:py-2 font-bold bg-blue-500 text-xs text-right whitespace-nowrap w-20 vote-btn-count"}).text

            article_url = "https://www.viedemerde.fr%s" % (content.get("href"))
            content_text = content.text

            embed = discord.Embed(title="**just Hervey 💎 || VDME 🔞**", color=0x0e9a98, description=content_text, url=article_url)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Je valide, c'est une VDM 👍", value=counter_a, inline=False)
            embed.add_field(name="Tu l'as bien mérité 👎", value=counter_b, inline=False)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Logo_vdm.png")
            embed.set_footer(text=by)
            vdmMessage = await ctx.reply(embed=embed)
            await vdmMessage.add_reaction("👍")
            await vdmMessage.add_reaction("👎")
            
        except: 
            continue
        else:
            break
