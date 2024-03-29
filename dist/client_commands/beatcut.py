
import pytube
from string import ascii_letters
from random import choice
from scipy.io import wavfile
import numpy as np
import discord
from asyncio import sleep
import subprocess

def change_connect_stat(e, client):
    client.voice_connect = False

async def CheckVoice(ctx):
    if ctx.author.voice is None:
        d = await ctx.reply('Vous devez être dans un salon vocal pour pouvoir écouter le résultat !')
        await d.delete(delay=15)
        return False
    else:
        for user in ctx.guild.members: 
            if user.id == 820344845918797854 and user.voice is not None:
                await ctx.reply('Le bot est déjà dans un salon vocal !')
                return False
    return True

def beat_cut(path, frq):
    
    subprocess.call(['ffmpeg', '-i', path, path[:-3] + 'wav'])
    path = path[:-3] + 'wav'
    
    _t = 0
    to_del = []
    is_d = False
    fs, data = wavfile.read(path)

    for i in enumerate(data):
        
        if _t >= frq: is_d = True
        if _t <= 0: is_d = False
        
        if is_d: 
            _t -= 1
            to_del.append(i[0])
        else: _t += 1

    data = np.delete(data, to_del, 0)
    path = path[:-3] + 'beatcut.wav'
    wavfile.write(path, fs, data)
    
    return path

async def BeatCut(ctx, args, client):
    
    path_name = r'cache\downloaded_sounds'
    file_name = str()
    for i in range(10): file_name += choice(ascii_letters)
    file_name += '.mp3'
    steps = ['**1/3** : Vérification...', '**2/3** : Téléchargement de la vidéo...', '**3/3** : Coupage des beats...']
    
    if await CheckVoice(ctx):
        
        if not args:
            d = await ctx.reply('Veuillez sélectionner une frequence de cut ainsi qu\'une vidéo YouTube !\n(0 --> Cuts très rapides | 100000(+) --> Cuts très lents)')
            await d.delete(delay=20)
            
        else:
            try:
                c = await ctx.reply(steps[0])
                frq = int(args[-1])

                try:
                    if 'list' in args[:-1]: url = str(args[:-1])[:int(str(args[:-1]).index('list'))-1]
                    else: url = args[:-1]
                    await c.edit(content=steps[1])
                    __s__ = str()
                    for w in url:
                        __s__ += '%s ' % (w)         
                    s = str(pytube.Search(__s__).results[0])
                    video_url = 'https://www.youtube.com/watch?v=%s' % (s[int(s.find('=')+1):][:-1])
                    pytube.YouTube(video_url).streams.filter(only_audio=True).first().download(output_path=path_name, filename=file_name)
                    await c.edit(content=steps[2])
                    await sleep(1)
                    path = beat_cut(path_name + '\\' + file_name, frq)
                    await c.delete()
                    voicechannel = ctx.author.voice.channel
                    await ctx.reply('Terminé !\nJe rejoins le salon %s !\nVidéo en cours d\'écoute avec un beatcut de %s : %s' % (voicechannel, frq, video_url))
                    voice = await voicechannel.connect()
                    client.voice_connect = True
                    voice.play(discord.FFmpegPCMAudio(path), after=lambda e: change_connect_stat(e, client))
                    while client.voice_connect: await sleep(0.1)
                    await voice.disconnect()
                except: 
                    await c.delete()
                    await ctx.reply('URL invalide ou vidéo non-trouvée.')
                                           
            except:
                await c.delete()
                d = await ctx.reply('Veuillez entrer une valeure correcte !\n(0 --> Cuts très rapides | 100000(+) --> Cuts très lents)')
                await d.delete(delay=15)
