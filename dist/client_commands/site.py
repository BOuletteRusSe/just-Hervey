import random, requests


async def Site(ctx):

    running = True

    while running:

        url = "https://"
        url += random.choice([word.strip() for word in open("assets/texts/words_list.txt")])
        url += ".fr"

        try:
            requests.get(url)
            await ctx.reply(url)
            break
        except:
            continue
