import random
from colored import fg, attr
from string import ascii_lowercase
from selenium import webdriver
from assets.selenium_presets import Driver

async def Youtube(ctx, search_):

    deleted_message = await ctx.reply("Chargement...")
    presets = Driver()
    driver = webdriver.Chrome(executable_path=presets.executable_path, options=presets.options)

    while True:

        if not search_:
            search = ""
            c = True
            for i in range(random.randint(2, 8)):
                _temp = random.choice(ascii_lowercase)
                search += _temp
        else:
            search = ""
            c = False
            for word in search_:
                search += word
                search += " "

        driver.get(f"https://www.youtube.com/results?search_query={search}")

        for button in driver.find_elements_by_class_name(
                "VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.IIdkle"):
            if button.get_attribute("aria-label") is None:
                continue
            else:
                button.click()

        try:
            random.choice(driver.find_element_by_id("contents").find_elements_by_tag_name(
                "ytd-video-renderer")).find_element_by_class_name(
                "text-wrapper.style-scope.ytd-video-renderer").click()
            video_url = driver.current_url
            driver.quit()
            await deleted_message.delete()
            await ctx.reply(video_url)
        except:
            k = False
            for e in driver.find_elements_by_id("button"):
                if e.get_attribute("aria-label") == "Accepter l'utilisation de cookies et autres données aux fins décrites ci-dessus":
                    k = True
                    e.click()
                    break
            if k:
                try:
                    random.choice(driver.find_element_by_id("contents").find_elements_by_tag_name("ytd-video-renderer")).find_element_by_class_name("text-wrapper.style-scope.ytd-video-renderer").click()
                    video_url = driver.current_url
                    driver.quit()
                    await deleted_message.delete()
                    await ctx.reply(video_url)
                except:
                    if not c:
                        await ctx.reply("Aucun résultat.")
                        break
                    else:
                        print("%sErreur lors du chargement de la commande YouTube. Recommencement en cours...%s" % (fg(160), attr(1)))
                        continue
            else:
                if not c:
                    await ctx.reply("Aucun résultat.")
                    break
                else:
                    print("%sErreur lors du chargement de la commande YouTube. Recommencement en cours...%s" % (fg(160), attr(1)))
                    continue
