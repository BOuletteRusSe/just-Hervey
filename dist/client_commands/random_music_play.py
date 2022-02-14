
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
            if v[0] and await CheckVoice(client.bot.get_guild(int(s))):
            
                sounds_paths = glob(r'assets\sounds\*.mp3')
                
                for member in client.bot.get_guild(int(s)).members:
                    if member.voice is not None: members_on_voice.append(member.voice)
                    
                if randint(0, v[1]) == 0 and len(members_on_voice) > 0:
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
            if sdata['RdMusic'][str(ctx.guild.id)][0]:
                await ctx.reply('Le rdmusic est actuellement sur **%s** avec un ratio de 1 chance sur %s de join toute les 5 secondes.\n(**0** --> Arrêter le rdmusic | **1** --> Réactiver le rdmusic | **ratio <nombre>** --> Changer le ratio de join (1 chance sur le nombre choisit de join toute les 5 secondes))' % (sdata['RdMusic'][str(ctx.guild.id)][0], sdata['RdMusic'][str(ctx.guild.id)][1]))
            else:
                await ctx.reply('Le rdmusic est actuellement sur **%s**.\n(**0** --> Arrêter le rdmusic | **1** --> Réactiver le rdmusic | **ratio <nombre>** --> Changer le ratio de join (1 chance sur le nombre choisit de join toute les 5 secondes))' % (sdata['RdMusic'][str(ctx.guild.id)][0]))
        except:
            sdata['RdMusic'][str(ctx.guild.id)] = [False]
            with open(r"assets\servers_data.json", 'w') as sd: json.dump(sdata, sd, indent=4)
            await ctx.reply('Le rdmusic est actuellement sur **%s**.\n(**0** --> Arrêter le rdmusic | **1** --> Réactiver le rdmusic | **ratio <nombre>** --> Changer le ratio de join (1 chance sur le nombre choisit de join toute les 5 secondes))' % (sdata['RdMusic'][str(ctx.guild.id)][0]))
    elif is_activate[0] == '0':
        sdata['RdMusic'][str(ctx.guild.id)] = [False]
        with open(r"assets\servers_data.json", 'w') as sd: json.dump(sdata, sd, indent=4)
        await ctx.reply('Le rdmusic a bien été arrêté !')
    elif is_activate[0] == '1':
        if len(sdata['RdMusic'][str(ctx.guild.id)]) == 1:
            sdata['RdMusic'][str(ctx.guild.id)] = [True, 50]
        with open(r"assets\servers_data.json", 'w') as sd: json.dump(sdata, sd, indent=4)
        await ctx.reply('Le rdmusic a bien été activé !') 
    elif is_activate[0] == 'ratio':
        if not sdata['RdMusic'][str(ctx.guild.id)][0]:
            await ctx.reply('Vous devez d\'abord activer le RdMusic pour pouvoir modifier le ratio de join.\n(**c!rdmusic 1** pour activer le RdMusic)')
        else:
            try:
                ratio = int(is_activate[1])
            except:
                await ctx.reply('Veuillez entrer un ratio correcte !\n(c!rdmusic ratio **<nombre>** (1 chance sur le nombre choisit de join toute les 5 secondes)')
            else:
                sdata['RdMusic'][str(ctx.guild.id)][1] = int(ratio)
                await ctx.reply('Le RdMusic a bien été modifié a %s' % (ratio))
                with open(r"assets\servers_data.json", 'w') as sd: json.dump(sdata, sd, indent=4)
    else: await ctx.reply('Veuillez entrer une valeure correcte !\n(0 --> Arrêter le rdmusic | 1 --> Réactiver le rdmusic | **ratio <nombre>** --> Changer le ratio de join (1 chance sur le nombre choisit de join toute les 5 secondes))')  
