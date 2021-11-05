# -*- coding: utf-8 -*-

import discord, random, sys
from colored import fg, attr
from discord import client
from discord.ext import commands as cmd
from discord.ext.commands.cooldowns import BucketType
from app import Client
from datetime import datetime
from client_commands.activity import ChangeActivity
from client_commands.random_music_play import RandomMusicPlay

client = Client()
client.bot.remove_command("help")

def CommandWriteLogs(ctx, command_name):
    logs = open("logs.log", "a", encoding="utf-8")
    log_message = f"{str(datetime.now())} - {ctx.message.guild.name} : {ctx.message.channel.name} : {ctx.message.author} ({ctx.author.id}) : {command_name} : {ctx.message.content}"
    print(f"{fg(40)}{str(datetime.now())}{attr(1)} - {fg(255)}{ctx.message.guild.name}{attr(0)} : {fg(21)}{ctx.message.channel.name}{attr(1)} : {fg(160)}{ctx.message.author}{attr(1)} ({ctx.author.id}) : {fg(3)}{command_name}{attr(0)} : {fg(255)}{ctx.message.content}{attr(0)}")
    logs.write(f"{log_message}\n")
    logs.close()


@client.bot.event
async def on_ready():
    print(f"{fg(6)}{discord.__version__} - {discord.version_info}{attr(0)}\n{fg(2)}Logged as {client.bot.user} !{attr(1)}")
    logs = open("logs.log", "a", encoding="utf-8")
    logs.write(f"{str(datetime.now())} - Bot: Logged as {client.bot.user}\n")
    logs.close()
    for guild in client.bot.guilds:
        print(f"{fg(255)}Logged in{attr(0)} {fg(190)}{guild}{attr(1)}")
    client.bot.loop.create_task(ChangeActivity(client))
    client.bot.loop.create_task(RandomMusicPlay(client))


@client.bot.event
async def on_guild_join(guild):
    print(f"{fg(20)}Joined {guild}.{attr(1)}")
    logs = open("logs.log", "a", encoding="utf-8")
    logs.write(f"Joined {guild}.\n")
    logs.close()
    embed = discord.Embed(title=f"just Hervey 💎 • {guild}", description=f"**Salut**, merci de m'avoir ajouter à {guild} ! <a:wavydance:882574990380265472>\n<a:arrow:882574892636200990> Pour consulter la **liste des commandes** vous pouvez faire la commande **c!help** !\nPour toute **demande** ou **report de bug** vous pouvez vous adresser à <@598900088768692348> (mes mp sont ouverts tant que c'est pas pour n'importe quoi).", color=0x3f12e2)
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
    logs = open("logs.log", "a", encoding="utf-8")
    logs.write(f"Quited {guild}.\n")
    logs.close()


@client.bot.event
async def on_message(message):
    chats = open("chat.log", "a", encoding="utf-8")
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
@cmd.cooldown(1, 5, cmd.BucketType.user)
async def filter(ctx, *color):
    CommandWriteLogs(ctx, "Filter")
    await client.Filter(ctx, color)
    
@client.bot.command()
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
async def ping(ctx):
    CommandWriteLogs(ctx, "Ping")
    if ctx.guild.id == 772461266135416843:
        await client.Ping(ctx)


@client.bot.command()
@cmd.cooldown(1, 5, cmd.BucketType.user)
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


@client.bot.command()
async def inventory(ctx, *equip):
    CommandWriteLogs(ctx, "Inventory")
    await client.Inventory(ctx, equip)


@client.bot.command()
@cmd.cooldown(1, 30, cmd.BucketType.channel)
async def clear(ctx):
    CommandWriteLogs(ctx, "Clear")
    await client.Clear(ctx)


@client.bot.command()
async def leaderboard(ctx):
    CommandWriteLogs(ctx, "Leaderboard")
    await client.Leaderboard(ctx)

@client.bot.command()
@cmd.cooldown(1, 3, cmd.BucketType.user)
async def work(ctx, *xp):
    CommandWriteLogs(ctx, "Work")
    await client.Work(ctx, xp)


@client.bot.command()
@cmd.cooldown(1, 5, BucketType.user)
async def say(ctx, *text):
    CommandWriteLogs(ctx, "Say")
    await client.Say(ctx, text)


@client.bot.command()
async def bank(ctx, *pos):
    CommandWriteLogs(ctx, "Bank")
    await client.Bank(ctx, pos)


@client.bot.command()
async def help(ctx, *arg):
    CommandWriteLogs(ctx, "Help")
    await client.Help(ctx, arg)


@client.bot.command()
@cmd.cooldown(3, 2.5, cmd.BucketType.user)
async def music(ctx):
    CommandWriteLogs(ctx, "Music")
    if ctx.guild.id == 772461266135416843:
        await client.Music(ctx)


@client.bot.command()
@cmd.cooldown(1, 2, cmd.BucketType.user)
async def loto(ctx, *m):
    CommandWriteLogs(ctx, "Loto")
    await client.Loto(ctx, m)

@client.bot.command()
async def bouliste(ctx):
    CommandWriteLogs(ctx, "Bouliste")
    if ctx.guild.id == 772461266135416843:
        await client.Bouliste(ctx)


@client.bot.command()
@cmd.cooldown(1, 10, cmd.BucketType.user)
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
    await client.BeatCut(ctx, args)


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
    if ctx.author.id == 598900088768692348:
        await ctx.reply("Redémarrage du bot en cours...")
        client.is_restarting = True
        sys.exit()
    else:
        deletedMessage = await ctx.reply("Vous n'avez pas les permissions de faire cela !")
        await deletedMessage.delete(delay=15)


@client.bot.command()
async def stop(ctx):
    CommandWriteLogs(ctx, "Stop")
    if ctx.author.id == 598900088768692348:
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
    if ctx.guild.id == 772461266135416843:
        await client.Invite(ctx)


@client.bot.command()
async def crush(ctx, *add):
    CommandWriteLogs(ctx, "Crush")
    if ctx.guild.id == 772461266135416843:
        await client.Crush(ctx, add)


@client.bot.command()
async def boule(ctx, *arg):
    CommandWriteLogs(ctx, "Boule")
    if ctx.guild.id in [772461266135416843, 830088796002975764]:
        await client.Boule(ctx, arg)


@client.bot.command()
@cmd.cooldown(2, 10, cmd.BucketType.user)
async def vdm(ctx):
    CommandWriteLogs(ctx, "Vdm")
    # await client.Vdm(ctx)
    d = await ctx.reply('Commande down...')
    await d.delete(delay=10)


@client.bot.command()
@cmd.cooldown(2, 10, cmd.BucketType.user)
async def vdme(ctx):
    CommandWriteLogs(ctx, "Vdme")
    # await client.Vdme(ctx)
    d = await ctx.reply('Commande down...')
    await d.delete(delay=10)


@client.bot.command()
@cmd.cooldown(2, 10, cmd.BucketType.user)
async def ph(ctx):
    CommandWriteLogs(ctx, "Ph")
    if ctx.guild.id == 772461266135416843:
        await client.Ph(ctx)


@client.bot.command()
@cmd.cooldown(1, 5, cmd.BucketType.user)
async def nude(ctx):
    CommandWriteLogs(ctx, "Nude")
    if ctx.guild.id == 772461266135416843:
        await client.Nude(ctx)


@client.bot.command()
@cmd.cooldown(3, 2, cmd.BucketType.user)
async def gif(ctx, *gif_):
    CommandWriteLogs(ctx, "Gif")
    await client.Gif(ctx, gif_)


@client.bot.command()
@cmd.cooldown(3, 2, cmd.BucketType.user)
async def mot(ctx, *arg):
    CommandWriteLogs(ctx, "Mot")
    if not arg: await ctx.reply(random.choice([word.strip() for word in open("liste_francais.txt")]))
    else:
        w = ""
        for word in arg:
            w += word
            w += " "
            
        rm = random.choice([word.strip() for word in open('liste_francais.txt')])
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
@cmd.cooldown(1, 3600, cmd.BucketType.guild)
async def cki(ctx):
    CommandWriteLogs(ctx, "Cki")
    await ctx.reply("cmoi")


@client.bot.command()
@cmd.cooldown(3, 2, cmd.BucketType.user)
async def phrase(ctx):
    CommandWriteLogs(ctx, "Phrase")
    await client.Phrase(ctx)

@client.bot.command()
@cmd.cooldown(1, 120, cmd.BucketType.default)
async def thanos(ctx):
    CommandWriteLogs(ctx, "Thanos")
    if ctx.guild.id == 772461266135416843:
        await client.Thanos(ctx)


@loto.error
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

@ki.error
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

@phrase.error
async def work_error(ctx, error):
    if isinstance(error, cmd.CommandOnCooldown):
        dele = await ctx.reply(f'La commande est en cooldown, veuillez réssayer dans {int(error.retry_after)} secondes !')
        await dele.delete(delay=1)

@mot.error
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


client.Start()