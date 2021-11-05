
import numpy as np
from PIL import Image
from random import choice
from string import ascii_letters
import requests
import discord

def DoFilter(image, filter: str):
            
    img = np.array(image)
    
    try:
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                if filter == "red":
                    img[x,y] = (img[x,y][0], 0, 0)
                elif filter == "green":
                    img[x,y] = (0, img[x,y][0], 0)
                else:
                    img[x,y] = (0, 0, img[x,y][0])   
    except:
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                if filter == "red":
                    img[x,y] = (img[x,y][0], 0, 0, img[x,y][3])
                elif filter == "green":
                    img[x,y] = (0, img[x,y][0], 0, img[x,y][3])
                else:
                    img[x,y] = (0, 0, img[x,y][0], img[x,y][3])
    return img

async def Filter(ctx, color):
    
    if not color:
        d = await ctx.reply('Veuillez choisir une couleur de filtre pour l\'image !\n(**red**, **green**, **blue**)')
        await d.delete(delay=20)
        
    elif color[0] not in ['red', 'green', 'blue']:
        d = await ctx.reply('Veuillez choisir une couleur de filtre correcte !\n(**red**, **green**, **blue**)')
        await d.delete(delay=15)
        
    elif not ctx.message.attachments :
        d = await ctx.reply('Veuillez envoyer une image à transformer avec la couleur du filtre !')
        
    else:
        file_name = str()
        for i in range(10): file_name += choice(ascii_letters)
        if str(ctx.message.attachments[0])[-3:] != 'png': file_name = r'cache\downloaded_imgs\%s.jpg' % (file_name) 
        else: file_name = r'cache\downloaded_imgs\%s.png' % (file_name) 
        with open(file_name, 'wb') as f: f.write(requests.get(ctx.message.attachments[0]).content)
        image = Image.open(file_name)
        image = DoFilter(image, color[0])
        img = Image.fromarray(image)
        if str(ctx.message.attachments[0])[-3:] != 'png': file_name = file_name[:-3] + 'filter.jpg'
        else: file_name = file_name[:-3] + 'filter.png'
        img.save(file_name)
        await ctx.reply(file=discord.File(file_name))
        