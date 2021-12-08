
import json
from random import choice
from string import ascii_letters
import pytube

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

def change_connect_stat(e, client):
    client.voice_connect = False
    
async def AppendJsonFile(ctx, data, d):
    for k, v in data.items():
        if k == str(ctx.guild.id):
            v.append(d)
            return True
    return False

async def Play(ctx, music, client):
    
    if CheckVoice(ctx):
        
        SOUNDS_CACHE = r'cache\downloaded_sounds'
        FILE_NAME = str()
        for i in range(10): FILE_NAME += choice(ascii_letters)
        FILE_NAME += '.mp3'
        
        voicechannel = ctx.author.channel
        voice = await voicechannel.connect()
        client.voice_connect = True
        
        __s__ = str()
        for w in music:
            __s__ += '%s ' % (w)
        
        s = str(pytube.Search(__s__).results[0])
        video_url = 'https://www.youtube.com/watch?v=%s' % (s[int(s.find('=')+1):][:-1])
        pytube.YouTube(video_url).streams.filter(only_audio=True).first().download(output_path=SOUNDS_CACHE, filename=FILE_NAME)
        
        with open('assets/servers_playlist.json') as j:
            data = json.load(j)
        
        if not await AppendJsonFile(ctx, data, FILE_NAME):
            data[str(ctx.guild.id)] = [FILE_NAME]
