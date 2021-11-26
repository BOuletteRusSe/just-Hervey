
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException
from random import choice

async def Curse(ctx, translat):
    if not translat:
        d = await ctx.reply('Veuillez entrer un nombre de langue et une phrase valide après la commande !')
        await d.delete(delay=15)    
    else:
        try:
            ln = int(translat[:int(translat.find(' '))])  
        except: 
            d = await ctx.reply('Veuillez entrer un nombre de langue et une phrase valide après la commande !')
            await d.delete(delay=15)       
        else:
            if not translat:
                d = await ctx.reply('Veuillez entrer un nombre de langue et une phrase valide après la commande !')
                await d.delete(delay=15)
            else:
                translated = str()
                translated = translat[int(translat.find(' ')):]
                if not (0 < ln <= 100):
                    d = await ctx.reply('Veuillez entrer un nombre de langue entre 0 et 100 !')
                    await d.delete(delay=15)              
                else:
                    
                    try: int(translated)
                    except: 
                        from_langs = [word.strip() for word in open("assets/texts/ISO_639-1.txt", encoding="utf-8")]
                        from_lang = list()
                        for i in range(ln): from_lang.append(choice(from_langs))
                        
                        mess = await ctx.reply('**0/%s** : %s' % (ln, translated))
                        
                        for lang in range(len(from_lang)):
                            try: translated = GoogleTranslator(source='auto', target=from_lang[lang]).translate(translated)
                            except LanguageNotSupportedException: pass
                            else: await mess.edit(content='**%s/%s** : %s' % (lang, ln, translated))
                            
                        translated = GoogleTranslator(source='auto', target='fr').translate(translated)
                        await mess.delete()
                        await ctx.reply(translated)
                    else: 
                        d = await ctx.reply('Veuillez entrer du texte !')
                        await d.delete(delay=20)
