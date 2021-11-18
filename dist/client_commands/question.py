import discord
from selenium import webdriver

async def Question(ctx, question_, c):

    if not question_:
        deletedMessage = await ctx.reply("Veuillez choisir une question !\nc!question **question** <-- ICI")
        await deletedMessage.delete(delay=15)

    else:
        deleted_message = await ctx.reply("Veuillez patienter...")
        question__ = ""
        for word in question_:
            question__ += word
            question__ += " "

        driver = webdriver.Chrome(executable_path="assets/chromedriver.exe.exe", options=c.options)
        driver.get(f"https://www.ecosia.org/search?q={question__}")
        try:
            driver.find_element_by_class_name("no-results__lead")
            await deleted_message.delete()
            await ctx.reply("Aucun résultat.")
            driver.quit()
        except:
            result = driver.find_element_by_class_name("result-title.js-result-title")
            link = result.get_attribute("href")
            title = result.text

            driver.quit()
            embed = discord.Embed(title=title, url=link, description=link, color=0x6875a6)
            embed.set_footer(text=f"Requette de {ctx.author}")
            await deleted_message.delete()
            await ctx.reply(embed=embed)
