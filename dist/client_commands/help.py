import discord


async def Help(ctx, arg, cc):

    commands_help = { 
        'Issou • 😆' : {
            "Command" : "issou",
            "Description" : "Envoie une  vidéo aléatoire de IssouTV (https://issoutv.com).",
            "Utilisation" : "c!issou",
            "Cooldown" : "1 Secondes par Utilisateur",
            "Category": "Fun",
            "Down" : False
        },      
        'Curse • ☢' : {
        "Command" : "curse",
        "Description" : "Traduit la phrase voulue dans le nombre langue(s) différente(s) voulue (max 100) avant de la retraduire en Français grâce à google traduction. Donne souvent des résultats amusants.",
        "Utilisation" : "c!curse <**nombre de langues**> <**phrase**>",
        "Cooldown" : "30 Secondes par Utilisateur",
        "Category": "Fun",
        "Down" : False
        },            
        'Filter • 🎨' : {
            "Command" : "filter",
            "Description" : "Applique un filtre de la couleure voulu sur l'image voulu. Pour plus d'info vous pouvez fire la commande sans argument.",
            "Utilisation" : "c!filter <**couleure**> <**image**>",
            "Cooldown" : "5 Secondes par Utilisateur",
            "Category": "Images et sons",
            "Down" : False
        },
        'BeatCut • 🎹' : {
            "Command" : "beatcut",
            "Description" : "Coupe 1/2 beat d'une musique YouTube à la fréquence voulu pûis rejoint le salon vocal pour jouer la musique. Pour plus d'info vous pouvez fire la commande sans argument.",
            "Utilisation" : "c!beatcut <**lien de la vidéo youtube**> <**fréquence de cut**>",
            "Cooldown" : "30 Secondes par Serveur",
            "Category": "Images et sons",
            "Down" : False
        },
        'BlackNWhite • 🖼' : {
            "Command" : "blacknwhite",
            "Description" : "Transforme l'image envoyée en noir et blanc.",
            "Utilisation" : "c!blacknwhite <**image**>",
            "Cooldown" : "5 Secondes par Utilisateur",
            "Category": "Images et sons",
            "Down" : False
        },
        "Choice • 🎭" : {
            "Command" : "choice",
            "Description" : "Envoie un \"Tu Préfères\", vous pouvez ensuite réagir avec les réactions appropriées selon votre opinion.",
            "Utilisation" : "c!choice",
            "Cooldown" : "5 Secondes par Utilisateur",
            "Category": "Fun",
            "Down" : True
        },
        "Clear • ⚪" : {
            "Command" : "clear",
            "Description" : "Envoie un message vide en guise de clear.",
            "Utilisation" : "c!clear",
            "Cooldown" : "30 Secondes par Salon",
            "Category": "Autre",
            "Down" : False
        },
        "Fight • ⚔" : {
            "Command" : "fight",
            "Description" : "1v1 gard du Nord.",
            "Utilisation" : "c!fight <@**utilisateur**>",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : False
        },
        "Gif • 🎈" : {
            "Command" : "gif",
            "Description" : "Envoie un gif aléatoire. Vous pouvez affiner la recherche en ajoutant des arguments après la commande.",
            "Utilisation" : "c!gif (<**recherche**>)",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : False
        },
        "Help • ❓" : {
            "Command" : "help",
            "Description" : "Affiche la liste des commandes.",
            "Utilisation" : "c!help (<**commande**>)",
            "Cooldown" : "Aucun",
            "Category": "Autre",
            "Down" : False
        },
        "Image • 🖼" : {
            "Command" : "image",
            "Description" : "Envoie une image aléatoire. Vous pouvez affiner la recherche en ajoutant des arguments après la commande.",
            "Utilisation" : "c!image (<**recherche**>)",
            "Cooldown" : "10 Secondes par Utilisateur",
            "Category": "Fun",
            "Down" : False
        },
        "Ki • 👾" : {
            "Command" : "ki",
            "Description" : "Pose une question (aléatoire) [**EN BETA**].",
            "Utilisation" : "c!ki",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : False
        },
        "Mot • 🅰" : {
            "Command" : "mot",
            "Description" : "Envoie un mot aléatoire. Vous pouvez ajouter des mots avant le mot.",
            "Utilisation" : "c!mot (<**mot/phrase**>)",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : False
        },
        "Philo • 👨‍🔬" : {
            "Command" : "philo",
            "Description" : "Hervey devient philosophe et vous envoie des phrases digne des plus grands.",
            "Utilisation" : "c!philo",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : False
        },
        "Phrase • 🆎" : {
            "Command" : "phrase",
            "Description" : "Envoie une phrase (aléatoire) [**EN BETA**].",
            "Utilisation" : "c!phrase",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : False
        },
        "Question • ❔" : {
            "Command" : "question",
            "Description" : "Recherche la réponse à votre question sur le dark-net et vous l'envoie..",
            "Utilisation" : "c!question <**question**>",
            "Cooldown" : "10 Secondes par Utilisateur",
            "Category": "Fun",
            "Down" : False
        },
        "Say • 🗣" : {
            "Command" : "say",
            "Description" : "Envoie un embed du texte inscrit après la commande.",
            "Utilisation" : "c!say <**texte**>",
            "Cooldown" : "5 Secondes par Utilisateur",
            "Category": "Autre",
            "Down" : False
        },
        "Site • 🧬" : {
            "Command" : "site",
            "Description" : "Envoie un URL d'un site (aléatoire).",
            "Utilisation" : "c!site",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : False
        },
        "VDM • 👴" : {
            "Command" : "vdm",
            "Description" : "Envoie une VDM provenant du site vdm officiel.",
            "Utilisation" : "c!vdm",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : True
        },
        "VDME • 🔞" : {
            "Command" : "vdme",
            "Description" : "Envoie une VDM Épicée provenant du site vdm officiel.",
            "Utilisation" : "c!vdme",
            "Cooldown" : "Aucun",
            "Category": "Fun",
            "Down" : True
        },
        "Vote • 📊" : {
            "Command" : "vote",
            "Description" : "Répond par oui ou non.",
            "Utilisation" : "c!vote (<**question**>)",
            "Cooldown" : "Aucun",
            "Category": "Autre",
            "Down" : False
        },
        "YouTube • 🎥" : {
            "Command" : "youtube",
            "Description" : "Envoie une vidéo YouTube aléatoire. Vous pouvez affiner la recherche en ajoutant des arguments après la commande.",
            "Utilisation" : "c!youtube (<*recherche*>)",
            "Cooldown" : "10 Secondes par Utilisateur",
            "Category": "Fun",
            "Down" : False
        },
        "Bank • 💰" : {
            "Command" : "bank",
            "Description" : "Permet de poser ou de retirer de l'argent en banque.",
            "Utilisation" : "c!bank **pos / get** <**montant**>",
            "Cooldown" : "Aucun",
            "Category": "Économie",
            "Down" : False
        },
        "Casino • 🎰" : {
            "Command" : "casino",
            "Description" : "Tentez votre chance en jouant au casino. L'argument rewards vous permet de voir les récompenses possible. L'argument buy vous permet d'acheter des tickets.",
            "Utilisation" : "c!casino (**rewards**) / (**buy** <**nombre de tickets**>)",
            "Cooldown" : "5 Secondes par Utilisateur",
            "Category": "Économie",
            "Down" : False
        },
        "Inventory • 🎁" : {
            "Command" : "inventory",
            "Description" : "Affiche le contenu de votre inventaire. Vous pouvez changer vos objets équipés avec les arguments. Pour voir l'inventaire de quelqu'un vous pouvez le mentionner après la commande.",
            "Utilisation" : "c!inventory (**equip** **item** <**id de l'item**> / **equip** **rank** <**id du rank**> / <@**utilisateur**>",
            "Cooldown" : "Aucun",
            "Category": "Économie",
            "Down" : False
        },
        "Leaderboard • 💹" : {
            "Command" : "leaderboard",
            "Description" : "Envoie le classement d'argent de tout le joueurs (inter-serveur).",
            "Utilisation" : "c!leaderboard",
            "Cooldown" : "Aucun",
            "Category": "Économie",
            "Down" : False
        },
        "Loto • 🎟" : {
            "Command" : "loto",
            "Description" : "Vous permet de parier de l'argent (soit doublé, soit perdu).",
            "Utilisation" : "c!loto <**montant**>",
            "Cooldown" : "Aucun",
            "Category": "Économie",
            "Down" : False
        },
        "Money • 💸" : {
            "Command" : "money",
            "Description" : "Affiche votre argent ou l'argent d'un utilisateur.",
            "Utilisation" : "c!money <@**utilisateur**>",
            "Cooldown" : "Aucun",
            "Category": "Économie",
            "Down" : False
        },
        "Poker • 🃏" : {
            "Command" : "poker",
            "Description" : "Vous permet de parier de l'argent avec un utilisateur, si l'utilisateur mentionné accepte la requête, vous payerez tout les deux le montant et la comme sera reversé aléatoirement à un de vous deux.",
            "Utilisation" : "c!poker <@**utilisateur**> <**montant**>",
            "Cooldown" : "Aucun",
            "Category": "Économie",
            "Down" : False
        },
        "Shop • 💱" : {
            "Command" : "shop",
            "Description" : "Affiche la boutique.",
            "Utilisation" : "c!shop (**item** (**buy** <**id de l'item**>)) / (**rank** (**buy** <**id du rank**>))",
            "Cooldown" : "Aucun",
            "Category": "Économie",
            "Down" : False
        },
        "Sign • 🗃" : {
            "Command" : "sign",
            "Description" : "Permet de vous inscrire.",
            "Utilisation" : "c!sign",
            "Cooldown" : "Aucun",
            "Category": "Économie",
            "Down" : False
        },
        "Work • ⚒" : {
            "Command" : "work",
            "Description" : "Vous permet de travailler pour gagner de l'xp et de l'argent.",
            "Utilisation" : "c!work (**xp**)",
            "Cooldown" : "5 Seconde par Utilisateur",
            "Category": "Économie",
            "Down" : False
        }
    }
    
    if ctx.guild.id == 772461266135416843:
        commands_help['Boule • 🧶'] = {"Command" : "boule", "Description" : "Envoie une boule.", "Utilisation" : "c!boule (**add** <**boule**>)", "Cooldown" : "Aucun", "Category": "Fun", "Down" : False}
        commands_help['Bouliste • 🎳'] = {"Command" : "bouliste", "Description" : "Envoie une combinaison de boules.", "Utilisation" : "c!bouliste", "Cooldown" : "Aucun", "Category": "Fun", "Down" : False}
        commands_help['Crush • 💖'] = {"Command" : "crush", "Description" : "Calcul votre amour.", "Utilisation" : "c!crush (**add** <**nom**> | <**prénom 1**> + <**prénom 2**>)", "Cooldown" : "Aucun", "Category": "Fun", "Down" : False}
        commands_help['Invite • ✉'] = {"Command" : "invite", "Description" : "Envoie une invitation vers un serveur discord au hasard (donne souvent une inbitation invalide).", "Utilisation" : "c!invite", "Cooldown" : "Aucun", "Category": "Autre", "Down" : False}
        commands_help['Music • 🎵'] = {"Command" : "music", "Description" : "Envoie une musique aléatoire de la playlist BEAUF.FR.", "Utilisation" : "c!music", "Cooldown" : "Aucun", "Category": "Fun", "Down" : False}
        commands_help['Nude • 🔞'] = {"Command" : "nude", "Description" : "Envoie une nude.", "Utilisation" : "c!nude", "Cooldown" : "Aucun", "Category": "Autre", "Down" : False}
        commands_help['Ph • 🟠⚫'] = {"Command" : "ph", "Description" : "Envoie un titre de vidéo provenant de ph.", "Utilisation" : "c!ph", "Cooldown" : "Aucun", "Category": "Autre", "Down" : False}
        commands_help['Ping • 🔗'] = {"Command" : "ping", "Description" : "Ping un utilisateur discord aléatoire (l'utilisateur est souvent invalide).", "Utilisation" : "c!ping", "Cooldown" : "Aucun", "Category": "Autre", "Down" : False}

    if not arg:

        categorys = {"Fun": "Fun • 🎉", "Images et sons": "Images et sons • 🎨", "Économie": "Économie • 📊", "Autre": "Autre • 🎲"}
        help_embed = discord.Embed(title="**just Hervey 💎 || Help <a:catGroove:881951879653892098>**", description="__Liste des Commandes 🎉 :__\n*Pour obtenir plus d'information sur une commande vous pouvez utiliser* **c!help <commande>**.", color=0xb09292)
        help_embed.set_author(name=cc.bot.user, icon_url=cc.bot.user.avatar_url)
        help_embed.set_thumbnail(url="https://media.tenor.com/images/36dd82e085114a98fe9cfe428d7a4031/tenor.gif")
        help_embed.set_footer(text="Hervey, just Hervey. (v. %s)" % (cc.client_version))

        for k_, v_ in categorys.items():
            final_chain = ""
            for k, v in commands_help.items():
                if v["Category"] == k_:
                    final_chain += f"`{v['Command']}`, "
            final_chain = final_chain[:-2]
            help_embed.add_field(name=v_, value=final_chain, inline=False)
                

        await ctx.reply(embed=help_embed)

    else:
        c = False
        for k, v in commands_help.items():
            if arg[0] == v["Command"]:
                c = True
                command_help_embed = discord.Embed(title=k, color=0xc39228)
                command_help_embed.add_field(name="💬 • Description :", value=v["Description"], inline=False)
                command_help_embed.add_field(name="🛠 • Utilisation :", value=v["Utilisation"], inline=False)
                command_help_embed.add_field(name="⏲ • Cooldown :", value=v["Cooldown"], inline=False)
                command_help_embed.add_field(name="🎳 • Catégorie :", value=v["Category"], inline=False)
                if v["Down"]:
                    command_help_embed.add_field(name="❌ • Commande Down :", value="La commande est down pour une durée indeteminée.", inline=False)

        if c: await ctx.reply(embed=command_help_embed)

        else:
            command_help_embed = discord.Embed(title="Commande Inconnue...", description="Commande inconnue, veillez à avoir écrit la commande sans majuscule et sans le préfix **c!**.", color=0xc33028)
            await ctx.reply(embed=command_help_embed)