
from string import ascii_letters
import numpy as np
from random import choice
from PIL import Image
import requests
import discord

def BlackAndWhite(image):
    img = np.array(image)
    
    try:
        for x in range(img.shape[0]):
            for y in range(img.shape[1]): 
                img[x,y] = (img[x,y][2], img[x,y][2], img[x,y][2])
    except:
        for x in range(img.shape[0]):
            for y in range(img.shape[1]): 
                img[x,y] = (img[x,y][2], img[x,y][2], img[x,y][2], img[x,y][3])      
              
    return img

async def BlackNWhite(ctx):
    
    if ctx.message.attachments:
        
        try:
            file_name = str()
            for i in range(10): file_name += choice(ascii_letters)
            if str(ctx.message.attachments[0])[-3:] != 'png': file_name = r'cache\downloaded_imgs\%s.jpg' % (file_name) 
            else: file_name = r'cache\downloaded_imgs\%s.png' % (file_name) 
            with open(file_name,'wb') as f: f.write(requests.get(ctx.message.attachments[0]).content)
            image = Image.open(file_name)
            image = BlackAndWhite(image)
            img = Image.fromarray(image)
            if str(ctx.message.attachments[0])[-3:] != 'png': file_name = file_name[:-3] + 'blacknwhite.jpg'
            else: file_name = file_name[:-3] + 'blacknwhite.png'
            img.save(file_name)
            await ctx.reply(file=discord.File(file_name))
            
        except: await ctx.reply('Une erreur a été rencontrée.\nVeuillez essayer avec une autre image.')
            
    else: 
        d = await ctx.reply('Veuillez envoyer une image à transformer en noir et blanc.')
        await d.delete(delay=15)
