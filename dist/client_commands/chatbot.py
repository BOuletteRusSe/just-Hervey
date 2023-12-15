from selenium import webdriver
import discord
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from assets.selenium_presets import Driver

async def Chatbot(ctx, arg):
    
    content = ""
    for word in arg:
        content += word
        content += " "
    if content == "":
        deleteMessage = await ctx.reply("Veuillez choisir un message à envoyer au bot !\nc!chatbot **contenue** <-- ICI")
        await deleteMessage.delete(delay=15)
    else:
    
        presets = Driver()
        driver = webdriver.Chrome(executable_path=presets.executable_path, options=presets.options)
        driver.get(f"https://robomatic.ai")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'RoboMaticIn')))
        sleep(1)

        i = driver.find_element_by_class_name('RoboMaticIn')
        s = driver.find_element_by_class_name('RoboMaticSend')
        
        lastmessage = "You:"
        i.send_keys(content)
        s.click()

        while "You:" in lastmessage:

            sleep(2)
            lastmessage = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/ul")[-1]
            lastmessage = lastmessage.text.splitlines()[-1]

        embed = discord.Embed(title="**🦔 just Hervey vous répond ! 🦔**", description=lastmessage, color=0xA08FD8)
        embed.set_footer(text=ctx.author)
        
        await ctx.reply(embed=embed)
        driver.quit()
