import random, json, discord


async def Fountain(ctx, m):

    with open("assets/player_data.json") as data:
        data = json.load(data)

    c = True
    id = str(ctx.author.id)

    for key in data.keys():
        if key == id:
            c = False

    if c:
        embed=discord.Embed(title="Vous n'êtes pas encore inscrit", description="Pour vous inscrire, utilisez la commande `c!sign`", color=0x393838)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        if not m:
            
            fountain_embed = discord.Embed(title="just Hervey 💎 | ⛲ FONTAINE SACRÉE ⛲", description="Bienvenue à la Fontaine Sacrée ! Ici vous pouvez jeter une somme d'argent dans la fontaine et espérer en retour que les dieux vous bénissent... Plus la somme sera élevée plus les potentiels gains en retour seront conséquents.\n\n```c!fountain <montant>```  Pour parier une somme d'argent", color=0x0EF1ED)
            fountain_embed.set_image(url="https://i.ibb.co/MD1WRRw/fountain-2.png")
            fountain_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            fountain_embed.add_field(name="", value="", inline=False)
            fountain_embed.add_field(name="💵 • Argent :", value=data[id]["Money"], inline=False)
            fountain_embed.set_footer(text="On raconte que jadis, d'anciennes populations ont batti cette fontaine afin de prier les dieux.")
            
            await ctx.send(embed=fountain_embed)

        else:
            try:
                m = m[0]
                m = int(m)

                if m <= 0:
                    await ctx.reply("Vous ne pouvez pas faire ça !")

                elif data[id]['Money'] - m < 0:
                    await ctx.reply(f"Vous n'avez pas assez d'argent !\nArgent : **{data[id]['Money']}**")
                else:
                    
                    prob = {
                        "Ticket": 25,
                        "Double": 10,
                        "Aigue Marine": 10,
                        "Aigue Marine Plan": 5
                    }
                    
                    if 2 in data[id]["Inventory"]["P Forge"]:
                        l2 = 5
                    else:
                        l2 = 6
                    
                    if random.randint(0, l2) == 0:
                        r = list(random.choices(*zip(*prob.items())))[0]
                    else:
                        r = None
                        
                    if r == "Double":
                        data[id]['Money'] += m
                        fountain_embed = discord.Embed(title="⚡ LES DIEUX VOUS SONT RECONNAISSANTS ⚡", description=f"Vous avez gagné la confiance des dieux et ils vous remercient donc par un don de leur part.\nVous attendez attentivement et une pluie de billet d'une somme de `{m*2}`€ vous tombe dessus.", color=0x0EF180)
                        fountain_embed.set_image(url="https://i.ibb.co/r7bZpfp/fountain.png")
                        fountain_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        fountain_embed.add_field(name="💵 • Argent gagné :", value=m*2, inline=False)
                        fountain_embed.add_field(name="💵 • Argent actuel :", value=data[id]["Money"], inline=False)
                        fountain_embed.set_footer(text="On raconte que jadis, d'anciennes populations ont batti cette fontaine afin de prier les dieux.")
                    
                    elif r == "Ticket":
                        u = random.randint(1, 5)
                        data[id]['Ticket'] += u
                        fountain_embed = discord.Embed(title="✨ LES DIEUX VOUS REMERCIENT ✨", description=f"Les dieux ont fait gage de patience et vous accordent leur attention.\nIls vous donnent `{u}` tickets de casino trouvés dans leurs poches.", color=0xA9F10E)
                        fountain_embed.set_image(url="https://i.ibb.co/r7bZpfp/fountain.png")
                        fountain_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        fountain_embed.add_field(name="🎟 • Ticket(s) gagné(s) :", value=u, inline=False)
                        fountain_embed.add_field(name="🎟 • Ticket(s) actuel(s) :", value=data[id]["Ticket"], inline=False)
                        fountain_embed.add_field(name="💵 • Argent perdu :", value=m, inline=False)
                        fountain_embed.add_field(name="💵 • Argent actuel :", value=data[id]["Money"], inline=False)
                        fountain_embed.set_footer(text="On raconte que jadis, d'anciennes populations ont batti cette fontaine afin de prier les dieux.")
                        
                    elif r == "Aigue Marine" and m >= 1000:
                        data[id]["Inventory"]["Aigue Marine"] += 1
                        fountain_embed = discord.Embed(title="🔱 LES DIEUX VOUS RÉCOMPENSENT 🔱", description=f"Vous avez gagné la confiance des dieux et ils vous remercient donc par un don de leur part.\nSous un éclat d'étincelles une pierre bleue ciel apparait. Vous la prenez et sentez une vibration à l'intérieur de celle-ci. Ca semble rare, vous le gardez au chaud dans votre inventaire.", color=0xF3FF00)
                        fountain_embed.set_image(url="https://i.ibb.co/r7bZpfp/fountain.png")
                        fountain_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        fountain_embed.add_field(name="🔱 • Aigue Marine :", value=data[id]["Inventory"]["Aigue Marine"], inline=False)
                        fountain_embed.add_field(name="💵 • Argent perdu :", value=m, inline=False)
                        fountain_embed.add_field(name="💵 • Argent actuel :", value=data[id]["Money"], inline=False)
                        fountain_embed.set_footer(text="On raconte que jadis, d'anciennes populations ont batti cette fontaine afin de prier les dieux.")
                        
                    elif r == "Aigue Marine Plan" and m >= 1000 and 4 not in data[id]["Inventory"]["Plans"]:
                        fountain_embed = discord.Embed(title="💖 PAIX AVEC LES DIEUX 💖", description=f"Les dieux vous accordent une faveur de leur part.\nUn parchemin runique apparaît sous un nuage de fûmée, vous sentez une bonne impression.", color=0xACC2C6)
                        fountain_embed.set_image(url="https://i.ibb.co/r7bZpfp/fountain.png")
                        fountain_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        fountain_embed.add_field(name="🔱 • Plan de l'Aigue Marine :", value="Vous avez débloqué un plan de forge pour pouvoir fabriquer de l'Aigue Marine !\nFaites `c!forge recipes` pour consulter la recette !", inline=False)
                        fountain_embed.add_field(name="💵 • Argent perdu :", value=m, inline=False)
                        fountain_embed.add_field(name="💵 • Argent actuel :", value=data[id]["Money"], inline=False)
                        fountain_embed.set_footer(text="On raconte que jadis, d'anciennes populations ont batti cette fontaine afin de prier les dieux.")
                        
                        data[id]["Inventory"]["Plans"].append(4)
                        
                        
                    else:
                        data[id]['Money'] -= m
                        fountain_embed = discord.Embed(title="👀 LES DIEUX DÉTOURNENT LE REGARD 👀", description=f"Les dieux n'ont pas l'air d'avoir prêté attention à votre don.\nVous repartez donc les mains vides en ayant perdu `{m}`€.", color=0xE72B0E)
                        fountain_embed.set_image(url="https://i.ibb.co/MD1WRRw/fountain-2.png")
                        fountain_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                        fountain_embed.add_field(name="💵 • Argent perdu :", value=m, inline=False)
                        fountain_embed.add_field(name="💵 • Argent actuel :", value=data[id]["Money"], inline=False)
                        fountain_embed.set_footer(text="On raconte que jadis, d'anciennes populations ont batti cette fontaine afin de prier les dieux.")
                            
                with open("assets/player_data.json", 'w') as d:
                    json.dump(data, d, indent=4)
                    
                await ctx.reply(embed=fountain_embed)
            except:
                deleted_message = await ctx.reply("Veuillez choisir un montant correcte || c!fountain **montant**")
                await deleted_message.delete(delay=15)
