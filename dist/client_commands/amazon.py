import discord, random
from assets.selenium_presets import Driver
from selenium import webdriver
from string import ascii_lowercase

async def Amazon(ctx, arg):
    
    deleted_message = await ctx.reply("Veuillez patienter...")
    if not arg:
        arg = ""
        for i in range(random.randint(2, 6)):
            _temp = random.choice(ascii_lowercase)
            arg += _temp
    else:
        arg = ""
        for word in arg:
            arg += word
            arg += " "

    presets = Driver()
    driver = webdriver.Chrome(executable_path=presets.executable_path, options=presets.options)
    driver.get(f"https://www.amazon.fr/")
    driver.find_element_by_id("twotabsearchtextbox").send_keys(arg)

