# -*- coding: utf-8 -*-

import discord, random, sys, re, json
from colored import fg, attr
from discord import client
from discord.ext import commands as cmd
from discord.ext.commands.cooldowns import BucketType
from client import Client
from datetime import datetime
from client_commands.activity import ChangeActivity
from client_commands.random_music_play import RandomMusicPlay
from pytube import Playlist

client = Client()
client.bot.remove_command("help")

def CommandWriteLogs(ctx, command_name):
    logs = open("logs/logs.log", "a", encoding="utf-8")
    log_message = f"{str(datetime.now())} - {ctx.message.guild.name} : {ctx.message.channel.name} : {ctx.message.author} ({ctx.author.id}) : {command_name} : {ctx.message.content}"
    print(f"{fg(40)}{str(datetime.now())}{attr(1)} - {fg(255)}{ctx.message.guild.name}{attr(0)} : {fg(21)}{ctx.message.channel.name}{attr(1)} : {fg(160)}{ctx.message.author}{attr(1)} ({ctx.author.id}) : {fg(3)}{command_name}{attr(0)} : {fg(255)}{ctx.message.content}{attr(0)}")
    logs.write(f"{log_message}\n")
    logs.close()

@client.bot.event
async def on_ready():
    logs = open("logs/logs.log", "a", encoding="utf-8")
    playlist = Playlist('https://www.youtube.com/playlist?list=PLjZi4YemnDB6vu8fhQ2gfTb2FuUuGlr-F')
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    with open(r'assets\texts\links.txt', 'w+', encoding='utf-8') as url_file:
        for url in playlist.video_urls: url_file.write('%s\n' % (url))
    with open('assets/servers_playlist.json', 'w+') as j: json.dump({}, j, indent=4)
    logs.write(f"{str(datetime.now())} - Bot: Logged as {client.bot.user}\n")
    logs.close()
    print(f'{fg(2)}Logged as {client.bot.user} !{attr(1)}')
    for guild in client.bot.guilds:
        print(f"{fg(255)}Logged in{attr(0)} {fg(190)}{guild}{attr(1)}")
    client.bot.loop.create_task(ChangeActivity(client))
    client.bot.loop.create_task(RandomMusicPlay(client))

@client.bot.event
async def on_guild_join(guild):
    print(f"{fg(20)}Joined {guild}.{attr(1)}")
    logs = open("logs/logs.log", "a", encoding="utf-8")
    logs.write(f"Joined {guild}.\n")
    logs.close()
    embed = discord.Embed(title=f"just Hervey 💎 • {guild}", description=f"**Salut**, merci de m'avoir ajouter à {guild} ! <a:wavydance:882574990380265472>\n<a:arrow:882574892636200990> Pour consulter la **liste des commandes** vous pouvez faire la commande **c!help** !\nPour toute **demande** ou **report de bug** vous pouvez vous adresser à <@809412081358733332> (mes mp sont ouverts tant que c'est pas pour n'importe quoi).", color=0x3f12e2)
    embed.set_footer(text=f"Objectif serveurs : {len(client.bot.guilds)} / 100.")
    no_general = True
    for channel in guild.text_channels:
        try:
            if "general" in str(channel):
                await channel.send(embed=embed)
                no_general = False
                break
        except:
            1 + 1
    if no_general:
        try:
            for channel in guild.text_channels: 
                await channel.send(embed=embed)
                break
        except:
            print(f"{fg(1)}Pas de salon textutel pour envoyer le message de bienvenue dans le serveur {guild}.{attr(0)}")


@client.bot.event
async def on_guild_remove(guild):
    print(f"{fg(20)}Quited {guild}.{attr(1)}")
    logs = open("logs/logs.log", "a", encoding="utf-8")
    logs.write(f"Quited {guild}.\n")
    logs.close()


@client.bot.event
async def on_message(message):
    chats = open("logs/chat.log", "a", encoding="utf-8")
    if message.attachments:
        chats.write(f"{str(datetime.now())} - {message.guild.name} : {message.channel.name} : {message.author} ({message.author.id}) : {str(message.attachments)}\n")
    else:
        chats.write(f"{str(datetime.now())} - {message.guild.name} : {message.channel.name} : {message.author} ({message.author.id}) : {message.content}\n")
    chats.close()
    await client.bot.process_commands(message)


@client.bot.command()
async def poker(ctx, *arg):
    CommandWriteLogs(ctx, "Poker")
    await client.Poker(ctx, arg)
    
@client.bot.command()
@cmd.cooldown(2, 3, cmd.BucketType.user)
async def forge(ctx, *arg):
    CommandWriteLogs(ctx, "Forge")
    await client.Forge(ctx, arg)
    
@client.bot.command()
@cmd.cooldown(3, 3, cmd.BucketType.user)
async def mabite(ctx, *arg):
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        CommandWriteLogs(ctx, "MaBite")
        await client.MaBite(ctx, arg)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')

@client.bot.command()
async def money(ctx, *res):
    CommandWriteLogs(ctx, "Money")
    await client.Money(ctx, res)

@client.bot.command()
async def rdmusic(ctx, *is_activate):
    CommandWriteLogs(ctx, 'RdMusic')
    await client.RdMusic(ctx, is_activate)

@client.bot.command()
@cmd.cooldown(1, 5, cmd.BucketType.user)
async def blacknwhite(ctx):
    CommandWriteLogs(ctx, 'BlackNWhite')
    await client.BlackNWhite(ctx)

@client.bot.command()
@cmd.cooldown(1, 30, cmd.BucketType.user)
async def curse(ctx, *, translat=None):
    CommandWriteLogs(ctx, 'Curse')
    await client.Curse(ctx, translat)

@client.bot.command()
@cmd.cooldown(1, 5, cmd.BucketType.user)
async def filter(ctx, *color):
    CommandWriteLogs(ctx, "Filter")
    await client.Filter(ctx, color)
    
@client.bot.command(aliases=["s"])
async def shop(ctx, *buy):
    CommandWriteLogs(ctx, "Shop")
    await client.Shop(ctx, buy)

@client.bot.command()
async def choice(ctx):
    CommandWriteLogs(ctx, "Choice")
    # await client.Choice(ctx)
    d = await ctx.reply("Bientôt disponible !")
    await d.delete(delay=15)


@client.bot.command()
async def join(ctx):
    CommandWriteLogs(ctx, 'Join')
    await client.Join(ctx)


@client.bot.command()
async def ping(ctx, *arg):
    CommandWriteLogs(ctx, "Ping")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Ping(ctx, arg)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@client.bot.command()
@cmd.cooldown(1, 3, cmd.BucketType.user)
async def casino(ctx, *arg):
    CommandWriteLogs(ctx, "Casino")
    await client.Casino(ctx, arg)


@client.bot.command()
async def logs(ctx):
    CommandWriteLogs(ctx, "Logs")
    await client.Logs(ctx)


@client.bot.command()
async def serverlist(ctx):
    CommandWriteLogs(ctx, "ServerList")
    await client.ServerList(ctx)


@client.bot.command()
async def sign(ctx):
    CommandWriteLogs(ctx, "Sign")
    await client.Sign(ctx)


@client.bot.command(aliases=["ivt"])
async def inventory(ctx, *equip):
    CommandWriteLogs(ctx, "Inventory")
    await client.Inventory(ctx, equip)


@client.bot.command()
@cmd.cooldown(1, 30, cmd.BucketType.channel)
async def clear(ctx):
    CommandWriteLogs(ctx, "Clear")
    await client.Clear(ctx)


@client.bot.command(aliases=["lb"])
async def leaderboard(ctx):
    CommandWriteLogs(ctx, "Leaderboard")
    await client.Leaderboard(ctx)

@client.bot.command()
@cmd.cooldown(1, 3, cmd.BucketType.user)
async def work(ctx, *xp):
    CommandWriteLogs(ctx, "Work")
    await client.Work(ctx, xp)
    
@client.bot.command(aliases=['bj'])
@cmd.cooldown(3, 3, cmd.BucketType.user)
async def bronjames(ctx, *arg):
    CommandWriteLogs(ctx, "bronJames")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.bronJames(ctx, arg)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')
        
@client.bot.command()
@cmd.cooldown(1, 5, BucketType.user)
async def say(ctx, *text):
    CommandWriteLogs(ctx, "Say")
    await client.Say(ctx, text)

@client.bot.command()
async def leave(ctx):
    CommandWriteLogs(ctx, 'Leave')
    await client.Leave(ctx)

@client.bot.command()
async def bank(ctx, *pos):
    CommandWriteLogs(ctx, "Bank")
    await client.Bank(ctx, pos)


@client.bot.command()
async def help(ctx, *arg):
    CommandWriteLogs(ctx, "Help")
    await client.Help(ctx, arg)


@client.bot.command()
async def play(ctx, *music):
    CommandWriteLogs(ctx, 'Play')
    # await client.Play(ctx, music)
    d = await ctx.reply('Commande down...')
    await d.delete(delay=10)

@client.bot.command()
@cmd.cooldown(3, 2.5, cmd.BucketType.user)
async def music(ctx):
    CommandWriteLogs(ctx, "Music")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Music(ctx)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@client.bot.command()
@cmd.cooldown(1, 300, cmd.BucketType.user)
async def fountain(ctx, *m):
    CommandWriteLogs(ctx, "Foutain")
    await client.Fountain(ctx, m)

@client.bot.command()
async def bouliste(ctx):
    CommandWriteLogs(ctx, "Bouliste")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Bouliste(ctx)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@client.bot.command()
@cmd.cooldown(1, 5, cmd.BucketType.user)
async def youtube(ctx, *search_):
    CommandWriteLogs(ctx, "Youtube")
    await client.YouTube(ctx, search_)


@client.bot.command()
@cmd.cooldown(1, 10, cmd.BucketType.user)
async def question(ctx, *question_):
    CommandWriteLogs(ctx, "Question")
    await client.Question(ctx, question_)


@client.bot.command()
@cmd.cooldown(1, 3600, cmd.BucketType.guild)
async def banana(ctx):
    CommandWriteLogs(ctx, "Banana")
    await ctx.reply("https://i2.wp.com/secretnews.fr/wp-content/uploads/2016/12/saucisson-porc-banane-halal.jpg?fit=1200%2C800&ssl=1")


@client.bot.command()
@cmd.cooldown(1, 10, cmd.BucketType.user)
async def image(ctx, *image_):
    CommandWriteLogs(ctx, "Image")
    await client.Image(ctx, image_)


@client.bot.command()
@cmd.cooldown(1, 30, cmd.BucketType.guild)
async def beatcut(ctx, *args):
    CommandWriteLogs(ctx, 'BeatCut')
    d = await ctx.reply('Commande temporairement down !')
    # await client.BeatCut(ctx, args)
    await d.delete(delay=7)


@client.bot.command()
async def vote(ctx):
    CommandWriteLogs(ctx, "Vote")
    await ctx.reply(random.choice(["Oui", "Non"]))


@client.bot.command()
@cmd.cooldown(1, 5, cmd.BucketType.user)
async def site(ctx):
    CommandWriteLogs(ctx, "Site")
    await client.Site(ctx)


@client.bot.command()
async def restart(ctx):
    CommandWriteLogs(ctx, "Restart")
    if ctx.author.id == 809412081358733332:
        await ctx.reply("Redémarrage du bot en cours...")
        client.is_restarting = True
        sys.exit()
    else:
        deletedMessage = await ctx.reply("Vous n'avez pas les permissions de faire cela !")
        await deletedMessage.delete(delay=15)


@client.bot.command()
async def stop(ctx):
    CommandWriteLogs(ctx, "Stop")
    if ctx.author.id == 809412081358733332:
        await ctx.reply("Le bot a bien été arrêté !")
        client.is_stoping = True
        sys.exit()
    else:
        deletedMessage = await ctx.reply("Vous n'avez pas les permissions de faire cela !")
        await deletedMessage.delete(delay=15)


@client.bot.command()
async def fight(ctx, *name):
    CommandWriteLogs(ctx, "Fight")
    await client.Fight(ctx, name)


@client.bot.command()
async def invite(ctx):
    CommandWriteLogs(ctx, "Invite")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Invite(ctx)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@client.bot.command()
async def crush(ctx, *add):
    CommandWriteLogs(ctx, "Crush")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Crush(ctx, add)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@client.bot.command()
async def boule(ctx, *arg):
    CommandWriteLogs(ctx, "Boule")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Boule(ctx, arg)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@client.bot.command()
@cmd.cooldown(5, 3, cmd.BucketType.user)
async def vdm(ctx):
    CommandWriteLogs(ctx, "Vdm")
    await client.Vdm(ctx)


@client.bot.command()
@cmd.cooldown(5, 3, cmd.BucketType.user)
async def vdme(ctx):
    CommandWriteLogs(ctx, "Vdme")
    await client.Vdme(ctx)


@client.bot.command()
@cmd.cooldown(2, 10, cmd.BucketType.user)
async def ph(ctx):
    CommandWriteLogs(ctx, "Ph")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Ph(ctx)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@client.bot.command()
async def tssc(ctx, *v):
    CommandWriteLogs(ctx, 'TSSC')
    await client.tssc(ctx, v)


@client.bot.command()
@cmd.cooldown(1, 5, cmd.BucketType.user)
async def nude(ctx):
    CommandWriteLogs(ctx, "Nude")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Nude(ctx)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@client.bot.command()
@cmd.cooldown(3, 2, cmd.BucketType.user)
async def gif(ctx, *gif_):
    CommandWriteLogs(ctx, "Gif")
    await client.Gif(ctx, gif_)

@client.bot.command()
@cmd.cooldown(1, 3, cmd.BucketType.user)
async def issou(ctx):
    CommandWriteLogs(ctx, "Issou")
    await client.Issou(ctx)

@client.bot.command()
@cmd.cooldown(3, 2, cmd.BucketType.user)
async def mot(ctx, *arg):
    CommandWriteLogs(ctx, "Mot")
    if not arg: await ctx.reply(random.choice([word.strip() for word in open("assets/texts/words_list.txt")]))
    else:
        w = ""
        for word in arg:
            w += word
            w += " "
            
        rm = random.choice([word.strip() for word in open('assets/texts/words_list.txt')])
        await ctx.reply(f"{w}{rm}")

@client.bot.command()
@cmd.cooldown(3, 2, cmd.BucketType.user)
async def philo(ctx):
    CommandWriteLogs(ctx, "Philo")
    await client.Philo(ctx)


@client.bot.command()
@cmd.cooldown(3, 2, cmd.BucketType.user)
async def ki(ctx):
    CommandWriteLogs(ctx, "Ki")
    await client.Ki(ctx)


@client.bot.command()
@cmd.cooldown(1, 300, cmd.BucketType.default)
async def banane(ctx):
    CommandWriteLogs(ctx, 'Banane')
    await client.Banane(ctx)


@client.bot.command()
async def ban(ctx):
    CommandWriteLogs(ctx, 'Ban')
    await client.Ban(ctx)


@client.bot.command()
@cmd.cooldown(1, 3600, cmd.BucketType.guild)
async def cki(ctx):
    CommandWriteLogs(ctx, "Cki")
    await ctx.reply("cmoi")


@client.bot.command()
@cmd.cooldown(1, 5, cmd.BucketType.user)
async def phrase(ctx):
    CommandWriteLogs(ctx, "Phrase")
    await client.Phrase(ctx)

@client.bot.command()
@cmd.cooldown(1, 1280, cmd.BucketType.default)
async def thanos(ctx):
    CommandWriteLogs(ctx, "Thanos")
    with open('assets/sscc.json') as sscc:
        ssccd = json.load(sscc)
    if ssccd[str(ctx.guild.id)]:
        await client.Thanos(ctx)
    else:
        await ctx.reply('Vous devez accepter les TSSC pour pourvoir utiliser cette commande.\nPour plus d\'info vous pouvez faire la commande **c!tssc** ou **c!help tssc**.')


@fountain.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@say.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@music.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)
        
@issou.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)      
  
@curse.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@casino.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@blacknwhite.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@bronjames.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@ki.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)
        
@forge.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@clear.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@philo.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)
    
@philo.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@mabite.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@mot.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@banane.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@gif.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@filter.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@ph.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@site.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@vdm.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@vdme.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@work.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@youtube.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@question.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@banana.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@beatcut.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)
        
@image.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)


@nude.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@cki.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@thanos.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

if __name__ == '__main__':
    client.Start()
