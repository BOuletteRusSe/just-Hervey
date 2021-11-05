
import discord
from asyncio import sleep
from random import randint, choice
from colored import fg, attr
from datetime import datetime
from glob import glob

def change_connect_stat(e):
    global connected
    connected = False

async def RandomMusicPlay(client):
    global connected
    global is_running
    
    members_on_voice = list()
    connected = False
    is_running = True
    
    while True:
        
        if is_running:
        
            sounds_paths = glob(r'data\sounds\*.mp3')
            
            for member in client.bot.get_guild(772461266135416843).members:
                if member.voice is not None: members_on_voice.append(member.voice)
                
            if randint(0, 50) == 1 and len(members_on_voice) > 0:
                voicechannel = choice(members_on_voice).channel
                voice = await voicechannel.connect()
                log_message = f"{str(datetime.now())} - {client.bot.get_guild(772461266135416843)} : RandomJoin : Le bot a rejoin le salon {voicechannel} de manière aléatoire."
                with open("logs.log", "a", encoding="utf-8") as logs: logs.write('%s\n' % (log_message))
                print(f"{fg(40)}{str(datetime.now())}{attr(1)} - {fg(255)}{client.bot.get_guild(772461266135416843)} : {fg(3)}RandomJoin{attr(0)} : {fg(255)}Le bot a rejoin le salon {voicechannel} de manière aléatoire.{attr(0)}")
                connected = True
                voice.play(discord.FFmpegPCMAudio(choice(sounds_paths)), after=lambda e: change_connect_stat(e))
                while connected: await sleep(0.1)
                await voice.disconnect()
            else:
                members_on_voice = list()
                await sleep(5)
                
        else: await sleep(0.1)
            
async def RdMusic(ctx, is_activate):
    
    global is_running
    
    if ctx.author.id in [598900088768692348, 612378210235318282, 341635888184295446]:
        if not is_activate: await ctx.reply('Le rdmusic est actuellement sur %s.\n(0 --> Arrêter le rdmusic | 1 --> Réactiver le rdmusic)' % (is_running))
        elif is_activate[0] == '0': 
            is_running = False
            await ctx.reply('Le rdmusic a bien été arrêté !')
        elif is_activate[0] == '1':
            is_running = True
            await ctx.reply('Le rdmusic a bien été activé !')     
        else: await ctx.reply('Veuillez entrer une valeure correcte !\n(0 --> Arrêter le rdmusic | 1 --> Réactiver le rdmusic)')  
            
    else:
        d = await ctx.reply('Vous n\'avez pas les permissions pour executer cette commande !')
        await d.delete(delay=15)
