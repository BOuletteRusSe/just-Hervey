
import discord, json
from asyncio import sleep
from random import randint, choice
from colored import fg, attr
from datetime import datetime
from glob import glob

def change_connect_stat(e, client):
    client.voice_connect = False

async def CheckVoice(g):
    for user in g.members: 
        if user.id == 820344845918797854 and user.voice is not None:
            return False
    return True

async def RandomMusicPlay(client):
    
    members_on_voice = list()
    
    while True:
        
        with open(r'assets\servers_data.json') as sd:
            sdata = json.load(sd)
        
        for s, v in sdata['RdMusic'].items():
            if v and await CheckVoice(client.bot.get_guild(int(s))):
            
                sounds_paths = glob(r'assets\sounds\*.mp3')
                
                for member in client.bot.get_guild(int(s)).members:
                    if member.voice is not None: members_on_voice.append(member.voice)
                    
                if randint(0, 50) == 1 and len(members_on_voice) > 0:
                    voicechannel = choice(members_on_voice).channel
                    voice = await voicechannel.connect()
                    log_message = f"{str(datetime.now())} - {client.bot.get_guild(int(s))} : RandomJoin : Le bot a rejoin le salon {voicechannel} de manière aléatoire."
                    with open("logs/logs.log", "a", encoding="utf-8") as logs: logs.write('%s\n' % (log_message))
                    print(f"{fg(40)}{str(datetime.now())}{attr(1)} - {fg(255)}{client.bot.get_guild(int(s))} : {fg(3)}RandomJoin{attr(0)} : {fg(255)}Le bot a rejoin le salon {voicechannel} de manière aléatoire.{attr(0)}")
                    client.voice_connect = True
                    voice.play(discord.FFmpegPCMAudio(choice(sounds_paths)), after=lambda e: change_connect_stat(e, client))
                    while client.voice_connect: await sleep(0.1)
                    await voice.disconnect()
                else:
                    members_on_voice = list()
                    await sleep(5)
                    
            else: await sleep(0.1)
            
async def RdMusic(ctx, is_activate):

    with open(r'assets\servers_data.json') as sd:
        sdata = json.load(sd)
        
    if not is_activate:
        try:
            await ctx.reply('Le rdmusic est actuellement sur %s.\n(0 --> Arrêter le rdmusic | 1 --> Réactiver le rdmusic)' % (sdata['RdMusic'][str(ctx.guild.id)]))
        except:
            sdata['RdMusic'][str(ctx.guild.id)] = False
            with open(r"assets\servers_data.json", 'w') as sd: json.dump(sdata, sd, indent=4)
            await ctx.reply('Le rdmusic est actuellement sur %s.\n(0 --> Arrêter le rdmusic | 1 --> Réactiver le rdmusic)' % (sdata['RdMusic'][str(ctx.guild.id)]))
    elif is_activate[0] == '0':
        sdata['RdMusic'][str(ctx.guild.id)] = False
        with open(r"assets\servers_data.json", 'w') as sd: json.dump(sdata, sd, indent=4)
        await ctx.reply('Le rdmusic a bien été arrêté !')
    elif is_activate[0] == '1':
        sdata['RdMusic'][str(ctx.guild.id)] = True
        with open(r"assets\servers_data.json", 'w') as sd: json.dump(sdata, sd, indent=4)
        await ctx.reply('Le rdmusic a bien été activé !')     
    else: await ctx.reply('Veuillez entrer une valeure correcte !\n(0 --> Arrêter le rdmusic | 1 --> Réactiver le rdmusic)')  
