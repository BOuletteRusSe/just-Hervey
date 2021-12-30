
import json, discord, pytube
from discord import player
from random import choice
from string import ascii_letters
from asyncio import sleep

async def CheckVoice(ctx):
    if ctx.author.voice is None:
        d = await ctx.reply('Vous devez être dans un salon vocal pour jouer une musique !')
        await d.delete(delay=15)
        return False
    for user in ctx.guild.members: 
        if user.id == 820344845918797854:
            if user.voice is not None:
                if ctx.author.voice.channel != user.voice.channel:
                    d = await ctx.reply('Vous devez être dans le même salon que le bot pour jouer de la musique !')
                    await d.delete(delay=15)
                    return False
    return True

def change_connect_stat(e, spd, guild, voicechannel_id, client):
    spd[str(guild.id)][str(voicechannel_id)] = spd[str(guild.id)][str(voicechannel_id)].pop(0)
    with open(r"assets\servers_playlist.json", 'w') as sp: 
        json.dump(spd, sp, indent=4)
    
async def AppendJsonFile(ctx, data, d):
    for k, v in data.items():
        if k == str(ctx.guild.id):
            for __k__, __v__ in v.items():
                __v__.append(d)
                return True
    return False

async def RdMusicIsNotActivate(ctx):
    with open(r'assets\servers_data.json') as sd:
        sdata = json.load(sd)
        
    for sid, v in sdata['RdMusic'].items():
        if sid == str(ctx.guild.id):
            if v: return False
            else: return True
    return True

async def PlayTask(client, voice, guild, voicechannel_id):
    
    global playing
    
    playing = True
    
    while playing:
        
        with open('assets/servers_playlist.json') as sp:
            spd = json.load(sp)

        for k, v in spd.items():
            if k == str(guild.id):
                for __k__, __v__ in v.items():
                    if len(__v__) == 0:
                        playing = False
                        await voice.disconnect()
                    else:
                        voice.play(discord.FFmpegPCMAudio('cache/downloaded_sounds/%s' % (__v__[0])), after=lambda e: change_connect_stat(e, spd, guild, voicechannel_id, client))
                        while client.voice_connect: await sleep(0.1)

async def Play(ctx, music, client):
    
    global playing
    
    if not await RdMusicIsNotActivate(ctx):
        d = await ctx.reply('Veuillez **désactiver** le **RdMusic** pour jouer une vidéo avec la commande play.\n(**c!rdmusic 0**)')
        await d.delete(delay=15)
    
    elif not music:
        d = await ctx.reply('Veuillez choisir une musique/vidéo à jouer !\n(c!play **recherche ou URL YouTube**)')
        await d.delete(delay=15)
        
    else:
    
        if await CheckVoice(ctx):
            
            SOUNDS_CACHE = r'cache\downloaded_sounds'
            FILE_NAME = str()
            for i in range(10): FILE_NAME += choice(ascii_letters)
            FILE_NAME += '.mp3'
            is_joining = False
            
            d = await ctx.reply('Téléchargement...')
            
            __s__ = str()
            for w in music:
                __s__ += '%s ' % (w)
            
            try: 
                s = pytube.Search(__s__).results[0]
            except:
                await d.delete()
                await ctx.reply('Vidéo non trouvée !')
            else:
                video_url = 'https://www.youtube.com/watch?v=%s' % (str(s)[int(str(s).find('=')+1):][:-1])
                pytube.YouTube(video_url).streams.filter(only_audio=True).first().download(output_path=SOUNDS_CACHE, filename=FILE_NAME)
            
            for user in ctx.guild.members: 
                if user.id == 820344845918797854 and user.voice is None:
                    voicechannel = ctx.author.voice.channel
                    voice = await voicechannel.connect()
                    client.voice_connect = True
                    is_joining = True
                
                with open('assets/servers_playlist.json') as j:
                    data = json.load(j)
                    
                for user in ctx.guild.members: 
                    if user.id == 820344845918797854:
                        voicechannel_id = str(user.voice.channel.id)
                
                if not await AppendJsonFile(ctx, data, FILE_NAME):
                    data[str(ctx.guild.id)] = {voicechannel_id: [FILE_NAME]}
                    
                with open(r"assets\servers_playlist.json", 'w') as sp: 
                    json.dump(data, sp, indent=4)
                
                embed = discord.Embed(title="%s ajoutée avec succès !" % (s.title), url=video_url, color=0xc9150f)
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await d.delete()
                await ctx.send(embed=embed)
                if not playing:
                    client.bot.loop.create_task(PlayTask(client, voice, ctx.guild, voicechannel_id))
