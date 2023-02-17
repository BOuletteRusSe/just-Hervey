from client_commands.music import Music
from client_commands.bouliste import Bouliste
from client_commands.choice import Choice
from client_commands.casino import Casino
from client_commands.poker import Poker
from client_commands.logs import Logs
from client_commands.serverlist import ServerList
from client_commands.say import Say
from client_commands.clear import Clear
from client_commands.ping import Ping
from client_commands.invite import Invite
from client_commands.help import Help
from client_commands.thanos import Thanos
from client_commands.gif import Gif
from client_commands.nude import Nude
from client_commands.ph import Ph
from client_commands.vdme import Vdme
from client_commands.vdm import Vdm
from client_commands.boule import Boule
from client_commands.crush import Crush
from client_commands.fight import Fight
from client_commands.site import Site
from client_commands.image import Image
from client_commands.question import Question
from client_commands.bank import Bank
from client_commands.inventory import Inventory
from client_commands.ki import Ki
from client_commands.leaderboard import Leaderboard
from client_commands.loto import Loto
from client_commands.money import Money
from client_commands.philo import Philo
from client_commands.phrase import Phrase
from client_commands.shop import Shop
from client_commands.sign import Sign
from client_commands.work import Work
from client_commands.youtube import Youtube
from client_commands.random_music_play import RdMusic
from client_commands.blacknwhite import BlackNWhite
from client_commands.beatcut import BeatCut
from client_commands.filter import Filter
from client_commands.curse import Curse
from client_commands.issou import Issou
from client_commands.play import Play
from client_commands.leave import Leave
from client_commands.ban import Ban
from client_commands.banane import Banane
from client_commands.forge import Forge

import discord, time, os, json
from colored import fg, attr
from discord.ext import commands
from datetime import datetime
from cryptography.fernet import Fernet

with open(r"assets\player_data.json") as data:
    data = json.load(data)

    class Client:

        def __init__(self):
            intents = discord.Intents().all()
            self.bot = commands.Bot(command_prefix="c!", description="#Nazomazochiste", intents=intents)
            self.client_version = '3.9.4.1'
            self.key = open(".PRIVATE/key.key", "rb").read()
            f = Fernet(self.key)
            with open(".PRIVATE/token", "rb") as file: encrypted_data = file.read()
            self.decrypted_data = f.decrypt(encrypted_data)
            self.decrypted_data = self.decrypted_data.decode("utf-8")
            self.voice_connect = False
            print(f"{fg(6)}{discord.__version__} - {discord.version_info}{attr(0)}")
            print('%s%sClient Version : %s' % (fg(57), attr(1), self.client_version))
        
        def Start(self):
            while True:
                try:
                    self.bot.run(self.decrypted_data)
                    break
                except:
                    if self.is_stoping:
                        logs = open("logs/logs.log", "a", encoding="utf-8")
                        logs.write(f"{str(datetime.now())} - {self.bot.user} loggout.")
                        logs.close()
                    elif self.is_restarting:
                        logs = open("logs/logs.log", "a", encoding="utf-8")
                        logs.write(f"{str(datetime.now())} - {self.bot.user} restarting...")
                        logs.close()
                        os.system("start /min relaunch.bat")
                    else:
                        print("%sLogin error, retrying...%s" % (fg(160), attr(1)))
                        time.sleep(10)
                        os.system("start /min relaunch.bat")
                        exit()

        @staticmethod
        async def tssc(ctx, v):
            
            with open('assets/sscc.json') as sscc:
                ssccd = json.load(sscc)
                
            try:
                a = ssccd[str(ctx.guild.id)]
            except:
                a = False
                
            tssc_embed = discord.Embed(title='Les TSSC de ce serveur sont actuellement sur %s.' % (a), description='Pour les activer ou les désactiver vous pouvez faire la commande **c!tssc __consent__/__decline__**.', color=0xDED517)
            tssc_embed.add_field(name='**⚠ • Attention**', value='Certaines commandes peuvent être choquantes pour certaines personnes, en acceptant les TSSC, vous acceptez tout les messages choquants que le bot pourrait envoyer.')
                
            if not v:
                await ctx.reply(embed=tssc_embed)
            
            elif v[0] == 'consent':
                ssccd[str(ctx.guild.id)] = True
                with open('assets/sscc.json', 'w+') as sscc:
                    json.dump(ssccd, sscc, indent=4)
                await ctx.reply('Les TSSC ont bien été acceptées !')
            elif v[0] == 'decline':
                ssccd[str(ctx.guild.id)] = False
                with open('assets/sscc.json', 'w+') as sscc:
                    json.dump(ssccd, sscc, indent=4)
                await ctx.reply('Les TSSC ont bien été refusées !')
            else:
                await ctx.reply(embed=tssc_embed)

        @staticmethod
        async def Banane(ctx): await Banane(ctx)

        @staticmethod
        async def BlackNWhite(ctx): await BlackNWhite(ctx)

        @staticmethod
        async def Ban(ctx): await Ban(ctx)

        @staticmethod
        async def Filter(ctx, color): await Filter(ctx, color)

        async def Poker(self, ctx, arg): await Poker(ctx, arg, self)

        @staticmethod
        async def Curse(ctx, translat): await Curse(ctx, translat)

        @staticmethod
        async def RdMusic(ctx, is_activate): await RdMusic(ctx, is_activate)

        async def Play(self, ctx, music): await Play(ctx, music, self)

        @staticmethod
        async def Issou(ctx): await Issou(ctx)

        @staticmethod
        async def Bouliste(ctx): await Bouliste(ctx)

        @staticmethod
        async def Leave(ctx): await Leave(ctx)

        async def BeatCut(self, ctx, args): await BeatCut(ctx, args, self)

        @staticmethod
        async def Music(ctx): await Music(ctx)

        @staticmethod
        async def Ping(ctx): await Ping(ctx)
        
        async def Inventory(self, ctx, equip): await Inventory(ctx, equip, self)

        @staticmethod
        async def Choice(ctx): await Choice(ctx)

        @staticmethod
        async def Casino(ctx, arg): await Casino(ctx, arg)

        @staticmethod
        async def Say(ctx, text): await Say(ctx, text)

        @staticmethod
        async def Logs(ctx): await Logs(ctx)

        @staticmethod
        async def Invite(ctx): await Invite(ctx)

        @staticmethod
        async def Sign(ctx): await Sign(ctx)

        @staticmethod
        async def Bank(ctx, pos): await Bank(ctx, pos)

        @staticmethod
        async def Shop(ctx, buy): await Shop(ctx, buy)
      
        async def Work(self, ctx, xp_): await Work(ctx, xp_, self)
        
        async def Money(self, ctx, res): await Money(ctx, res, self)

        async def ServerList(self, ctx): await ServerList(ctx, self)

        @staticmethod
        async def Loto(ctx, m): await Loto(ctx, m)
        
        @staticmethod
        async def Forge(ctx, arg): await Forge(ctx, arg)

        @staticmethod
        async def Leaderboard(ctx): await Leaderboard(ctx)

        @staticmethod
        async def Phrase(ctx):
            await Phrase(ctx)

        @staticmethod
        async def Clear(ctx): await Clear(ctx)

        @staticmethod
        async def Ki(ctx): await Ki(ctx)

        @staticmethod
        async def Philo(ctx): await Philo(ctx)

        async def Help(self, ctx, arg): await Help(ctx, arg, self)

        @staticmethod
        async def YouTube(ctx, search_=False): await Youtube(ctx, search_)

        @staticmethod
        async def Question(ctx, question_): await Question(ctx, question_)

        @staticmethod
        async def Image(ctx, image_=False): await Image(ctx, image_)

        @staticmethod
        async def Site(ctx): await Site(ctx)

        @staticmethod
        async def Fight(ctx, name): await Fight(ctx, name)
            
        @staticmethod
        async def Crush(ctx, add=""): await Crush(ctx, add)

        @staticmethod
        async def Boule(ctx, arg=""): await Boule(ctx, arg)

        @staticmethod
        async def Vdm(ctx): await Vdm(ctx)

        @staticmethod
        async def Vdme(ctx): await Vdme(ctx)

        @staticmethod
        async def Ph(ctx): await Ph(ctx)

        @staticmethod
        async def Nude(ctx): await Nude(ctx)

        @staticmethod
        async def Gif(ctx, gif_=False): await Gif(ctx, gif_)

        async def Thanos(self, ctx): await Thanos(ctx, self)
