import requests
from bs4 import BeautifulSoup


async def Choice(ctx):

    url = "https://www.jeu-tu-preferes.fr/jouer?quizz=aleatoire"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    content = soup.find('section', {'id': 'content'})
    choices = content.find_all('span', {'class': 'text'})

    for choice in choices:
        await ctx.reply(choice.text)
