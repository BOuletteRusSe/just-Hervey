
import discord, json, time, random


async def Daily(ctx):
    
    with open("assets/player_data.json") as data:
        data = json.load(data)
            
    id = str(ctx.author.id)
    c = True

    for key in data.keys():
        if key == id:
            c = False

    if c:
        await ctx.reply("Veuillez vous inscrire avec la commande **c!sign** !")

    else:
        
        delta_t = time.time()
        last_daily = data[id]["Last Daily"]
        
        if delta_t - 43200 <= last_daily:
            waiting = int(last_daily - (delta_t - 43200))
            waiting_embed = discord.Embed(title="just Hervey 💎 | 🏆 RÉCOMPENSES QUOTIDIENNES 🏆", description=f"Vous avez déjà réclamé votre récompense quotidienne !\nTemps avant la prochaine récompense **{round(waiting/3600, 1)}h**.", color=0x2C8BD6)
            waiting_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            waiting_embed.set_footer(text="Soyez actif tout les jours afin de ne pas rater les récompense quotidiennes !")
            await ctx.reply(embed=waiting_embed)
            
        else:
            lots = {
                "Platinium": 20,
                "Coal": 25,
                "Ticket": 20,
                "Money": 25,
                "Diamond": 10
            }
            
            r = list(random.choices(*zip(*lots.items())))[0]
            
            if r == "Platinium":
                n = random.randint(1, 5)
                data[id]["Inventory"]["Platinium"] += n
                reward_embed = discord.Embed(title="just Hervey 💎 | 🏆 RÉCOMPENSES QUOTIDIENNES 🏆", description=f"Vous avez obtenu `{n}` de platine !", color=0x2C8BD6)
                reward_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                reward_embed.add_field(name="<:platinium:1078401302838661120> • Platine", value=data[id]["Inventory"]["Platinium"])
                reward_embed.set_footer(text="Soyez actif tout les jours afin de ne pas rater les récompense quotidiennes !")
            
            elif r == "Coal":
                n = random.randint(1, 10)
                data[id]["Inventory"]["Coal"] += n
                reward_embed = discord.Embed(title="just Hervey 💎 | 🏆 RÉCOMPENSES QUOTIDIENNES 🏆", description=f"Vous avez obtenu `{n}` de charbon !", color=0x2C8BD6)
                reward_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                reward_embed.add_field(name="<:coal:1078401112807317615> • Charbon", value=data[id]["Inventory"]["Coal"])
                reward_embed.set_footer(text="Soyez actif tout les jours afin de ne pas rater les récompense quotidiennes !")
                
            elif r == "Diamond":
                data[id]["Inventory"]["Diamond"] += 1
                reward_embed = discord.Embed(title="just Hervey 💎 | 🏆 RÉCOMPENSES QUOTIDIENNES 🏆", description=f"Vous avez obtenu `1` diamant !", color=0x2C8BD6)
                reward_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                reward_embed.add_field(name="<:diamond:1078401167425536071> • Diamant", value=data[id]["Inventory"]["Diamond"])
                reward_embed.set_footer(text="Soyez actif tout les jours afin de ne pas rater les récompense quotidiennes !")
                
            elif r == "Ticket":
                n = random.randint(1, 5)
                data[id]["Ticket"] += n
                reward_embed = discord.Embed(title="just Hervey 💎 | 🏆 RÉCOMPENSES QUOTIDIENNES 🏆", description=f"Vous avez obtenu `{n}` tickets de casino !", color=0x2C8BD6)
                reward_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                reward_embed.add_field(name="🎟 • Tickets", value=data[id]["Ticket"])
                reward_embed.set_footer(text="Soyez actif tout les jours afin de ne pas rater les récompense quotidiennes !")
                
            elif r == "Money":
                n = random.randint(500, 2500)
                data[id]["Money"] += n
                reward_embed = discord.Embed(title="just Hervey 💎 | 🏆 RÉCOMPENSES QUOTIDIENNES 🏆", description=f"Vous avez obtenu `{n}`€ !", color=0x2C8BD6)
                reward_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                reward_embed.add_field(name="💵 • Argent", value=data[id]["Money"])
                reward_embed.set_footer(text="Soyez actif tout les jours afin de ne pas rater les récompense quotidiennes !")
            
            data[id]["Last Daily"] = delta_t
            
            with open("assets/player_data.json", 'w') as d:
                json.dump(data, d, indent=4)
            await ctx.reply(embed=reward_embed)
