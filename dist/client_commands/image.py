import random, discord
from selenium import webdriver
from string import ascii_lowercase
from assets.selenium_presets import Driver

async def Image(ctx, image_):

    deleted_message = await ctx.reply("Veuillez patienter...")
    if not image_:
        image_ = ""
        for i in range(random.randint(2, 6)):
            _temp = random.choice(ascii_lowercase)
            image_ += _temp
    else:
        _image = ""
        for word in image_:
            _image += word
            _image += " "

    presets = Driver()
    driver = webdriver.Chrome(executable_path=presets.executable_path, options=presets.options)
    driver.get(f"https://www.ecosia.org/images?q={image_}")
    try:
        driver.find_element_by_class_name("message-tips__title")
        await deleted_message.delete()
        await ctx.reply("Aucun résultat.")
        driver.quit()
    except:
        image__ = random.choice(driver.find_elements_by_class_name("image-result__image")).get_attribute("src")

        driver.quit()
        embed = discord.Embed(title="**just Hervey 💎 || IMAGE**", url=image__, color=0xffdd00)
        embed.set_image(url=image__)
        embed.set_footer(text=f"Requette de {ctx.author}")
        await deleted_message.delete()
        await ctx.reply(embed=embed)
