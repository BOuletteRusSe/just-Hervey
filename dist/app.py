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

import discord, time, os, json
from colored import fg, attr
from discord.ext import commands
from selenium import webdriver
from datetime import datetime
from cryptography.fernet import Fernet

with open(r"data\player_data.json") as data:
    data = json.load(data)

    class Client:

        def __init__(self):
            intents = discord.Intents().all()
            self.bot = commands.Bot(command_prefix="c!", description="#Nazomazochiste", intents=intents)
            self.is_stoping = False
            self.is_restarting = False
            self.options = webdriver.ChromeOptions()
            # options.add_argument("--headless")
            # options.add_argument("--disable-gpu")
            self.options.add_argument("--disable-dev-shm-usage")
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--disable-software-rasterizer")
            self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.lettres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            self.item_shop_price = {
                        0: {
                            "Name": "Aucun"
                        },
                        1: {
                            "Level": 0,
                            "Money": 1000,
                            "Price": False,
                            "Name": "😮-Mineur Débutant"
                        },
                        2: {
                            "Level": 10,
                            "Money": 2000,
                            "Price": False,
                            "Name": "😋-Mineur Amateur"
                        },
                        3: {
                            "Level": 20,
                            "Money": 5000,
                            "Price": False,
                            "Name": "⛏-Mineur Affirmé"
                        },
                        4: {
                            "Level": 30,
                            "Money": 10000,
                            "Price": False,
                            "Name": "😎-Mineur Professionel"
                        },
                        5: {
                            "Level": 50,
                            "Money": 50000,
                            "Price": False,
                            "Name": "🐱‍🏍-Mineur Légendaire"
                        },
                        6: {
                            "Level": 50,
                            "Money": 150000,
                            "Price": False,
                            "Name": "💎-Géologue"
                        },
                        7: {
                            "Level": 75,
                            "Money": 100000,
                            "Price": False,
                            "Name": "<:sacredstone:882234999145922621>-Récolteur de cristaux"
                        },
                        8: {
                            "Level": 75,
                            "Money": 500000,
                            "Price": False,
                            "Name": "🧚‍♀️-Mineur Mythique"
                        },
                        9: {
                            "Level": 100,
                            "Money": 1000000,
                            "Price": False,
                            "Name": "👑-Mineur Suprême"
                        },
                        10: {
                            "Level": 20,
                            "Money": 0,
                            "Price": ["Coke", 10],
                            "Name" : "<:drogue:882314468086931466>-DROGUÉ"
                        },
                        11: {
                            "Name": "<a:catGroove:881951879653892098>-Créateur"
                        },
                        12 : {
                            "Name": "<a:toucanhype:882315781277376542>-Gagnant du Loto"
                        }
                    }
            self.item_shop_price_2 = {

                        0: {
                            "Name": "Aucun"
                        },

                        
                        1: {
                            "Name": "🧲|Pioche en Fer",
                            "Price": ["Iron", 10],
                            "Money": 2000
                        },

                        2: {
                            "Name": "🥇|Pioche en Or",
                            "Price": ["Gold", 10],
                            "Money": 7500
                        },

                        3: {
                            "Name": "🔥|Pioche de Magma",
                            "Price": ["Magma Stone", 10],
                            "Money": 1000
                        },

                        4: {
                            "Name": "⛏|Alliage en Platine",
                            "Price": ["Platinium", 10],
                            "Money": 2000
                        },

                        5: {
                            "Name": "👨‍🔬|PIOCHE DU CHINOIS",
                            "Price": ["Joseph", 10],
                            "Money": 100000
                        },

                        6 : {
                            "Name": "✖|Pioche de Multiplication",
                            "Price": ["Cobalt", 30],
                            "Money": 50000
                        },

                        7: {
                            "Name": "🕵️‍♂️|Pioche du Maraudeur",
                            "Price": ["Stone", 1000],
                            "Money": 25000
                        },

                        8: {
                            "Name": "👾|Multi-Pioche",
                            "Price": ["Diamond", 5],
                            "Money": 100000
                        },

                        9 : {
                            "Name" : "<a:toucanhype:882315781277376542>|Pioche du Loto"
                        }
                    }

            key = open("key.key", "rb").read()
            f = Fernet(key)
            with open("token", "rb") as file:
                encrypted_data = file.read()
            self.decrypted_data = f.decrypt(encrypted_data)


        def Start(self):
            while True:
                try:
                    self.bot.run(self.decrypted_data.decode())
                    break
                except:
                    if self.is_stoping:
                        logs = open("logs.log", "a", encoding="utf-8")
                        logs.write(f"{str(datetime.now())} - {self.bot.user} loggout.")
                        logs.close()
                    elif self.is_restarting:
                        logs = open("logs.log", "a", encoding="utf-8")
                        logs.write(f"{str(datetime.now())} - {self.bot.user} restarting...")
                        logs.close()
                        os.system("start /min relaunch.bat")
                    else:
                        print("%sLogin error, retrying...%s" % (fg(160), attr(1)))
                        time.sleep(10)
                        os.system("start /min relaunch.bat")
                        exit()

        @staticmethod
        async def BlackNWhite(ctx): await BlackNWhite(ctx)

        @staticmethod
        async def Filter(ctx, color): await Filter(ctx, color)

        async def Poker(self, ctx, arg): await Poker(ctx, arg, self)

        @staticmethod
        async def RdMusic(ctx, is_activate): await RdMusic(ctx, is_activate)

        @staticmethod
        async def Bouliste(ctx): await Bouliste(ctx)

        @staticmethod
        async def BeatCut(ctx, args): await BeatCut(ctx, args)

        @staticmethod
        async def Music(ctx): await Music(ctx)

        @staticmethod
        async def Ping(ctx): await Ping(ctx)

        async def Inventory(self, ctx, equip): await Inventory(ctx, equip, self)

        @staticmethod
        async def Choice(ctx): await Choice(ctx)

        async def Casino(self, ctx, arg): await Casino(ctx, arg, self)

        @staticmethod
        async def Say(ctx, text): await Say(ctx, text)

        @staticmethod
        async def Logs(ctx):
            await Logs(ctx)

        @staticmethod
        async def Invite(ctx): await Invite(ctx)

        @staticmethod
        async def Sign(ctx): await Sign(ctx)

        @staticmethod
        async def Bank(ctx, pos): await Bank(ctx, pos)

        async def Shop(self, ctx, buy): await Shop(ctx, buy, self)
      
        async def Work(self, ctx, xp_): await Work(ctx, xp_, self)
        
        async def Money(self, ctx, res): await Money(ctx, res, self)

        async def ServerList(self, ctx): await ServerList(ctx, self)

        @staticmethod
        async def Loto(ctx, m): await Loto(ctx, m)

        async def Leaderboard(self, ctx): await Leaderboard(ctx, self)

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

        async def YouTube(self, ctx, search_=False): await Youtube(ctx, search_, self)

        async def Question(self, ctx, question_): await Question(ctx, question_, self)

        async def Image(self, ctx, image_=False): await Image(ctx, image_, self)

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

        async def Gif(self, ctx, gif_=False): await Gif(ctx, gif_, self)

        async def Thanos(self, ctx): await Thanos(ctx, self)