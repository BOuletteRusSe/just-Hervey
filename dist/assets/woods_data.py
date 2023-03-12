# Liste des bois

c = "🟢 • Commun"
p = "🔵 • Peu Commun"
r = "🟡 • Rare"
e = "🟣 • Épique"
l = "🟠 • Légendaire"
m = "🔴 • Mythique"
re = "🟤 • Reliques"
b = "⚫ • Black Market"
d = "⚪ • Divin"

woods = {
    "Oak" : {
        "Proba": 7,
        "Hp": 5,
        "Name" : "un **Chêne** !",
        "Emoji" : "<:oak:1079481150822686781>",
        "Price" : 100,
        "Xp" : 25,
        "Color" : 0xE7DCC7,
        "Level Requierd" : 0,
        "Description": "Nom Scientifique : `Quercus`\nLe **bois de chêne** est **robuste** et **puissant**, comme un ancien guerrier de légende. Il résiste aux assauts du **temps** et des **éléments**, et son **écorce rugueuse** témoigne de la **dureté** de son existence. Mais sous cette apparence **rude** se **cache une âme généreuse**, capable de nourrir les flammes de la vie elle-même.",
        "Image" : "https://i.ibb.co/DLQ9X43/image-2023-02-26-201131792.png",
        "Lj Points": 25,
        "Id": 0,
        "Rareté": c
    },
    "Acacia" : {
        "Proba": 6,
        "Hp": 6,
        "Name" : "de l'**Acacia** !",
        "Emoji" : "<:acacia:1079483548353957918>",
        "Price" : 200,
        "Xp" : 50,
        "Color" : 0xCB960A,
        "Level Requierd" : 0,
        "Description": "Nom Scientifique : `Akis - Robinia Pseudacacia`\nLe **bois d'acacia** est **léger** et **élégant**, tel un danseur gracieux dans un ballet enchanté. Ses **branches délicates** se courbent sous le poids des feuilles, comme des franges d'un voile qui virevolte au vent. Mais ne vous y trompez pas, car ce bois est également **redoutable**, capable de **fendre les armures les plus solides**.",
        "Image" : "https://i.ibb.co/6Pt9fnf/acacia.png",
        "Lj Points": 40,
        "Id": 1,
        "Rareté": c
    },
    "Dark Oak" : {
        "Proba": 5,
        "Hp": 7,
        "Name" : "un **Chêne Noir** !\n",
        "Emoji" : "<:darkoak:1079485589512007740>",
        "Price" : 250,
        "Xp" : (50, 100),
        "Color" : 0x2E2A20,
        "Level Requierd" : 5,
        "Description": "Nom Scientifique : `Quercus`\nLe **bois de chêne noir** est **sombre** et **mystérieux**, comme les ombres qui se glissent dans la nuit. Il pousse dans les **terres maudites**, où les esprits tourmentés errent sans fin. Ses **racines** s'enfoncent **profondément dans la terre**, puisent dans **les ténèbres** pour renforcer leur essence. Mais qui sait ce qui se cache dans ses profondeurs ?",
        "Image" : "https://i.ibb.co/j3Rh3T2/dark-oak.png",
        "Lj Points": 50,
        "Id": 2,
        "Rareté": p
    },
    "Basswood" : {
        "Proba": 6,
        "Hp": 10,
        "Name" : "du **Tilleul** !",
        "Emoji" : "<:basswood:1079487621241241651>",
        "Price" : (150, 300),
        "Xp" : 75,
        "Color" : 0xD0AB4F,
        "Level Requierd" : 5,
        "Description": "Nom Scientifique : `Tilia cordata`\nLe **bois de tilleul** est **doux** et **apaisant**, comme une berceuse murmurée à l'oreille d'un enfant. Ses **feuilles odorantes** exhalent un **parfum sucré**, tandis que son **écorce lisse et soyeuse** invite au toucher. C'est un bois qui **soigne**, qui **réconforte**, qui **enveloppe** de son étreinte chaleureuse.",
        "Image" : "https://i.ibb.co/z2F0vfn/basswood.png",
        "Lj Points": (35, 50),
        "Id": 3,
        "Rareté": c
    },
    "Palm Tree" : {
        "Proba": 4,
        "Hp": 20,
        "Name" : "un **Palmier** !",
        "Emoji" : "<:palm_tree:1082723602434113616>",
        "Price" : (250, 500),
        "Xp" : 100,
        "Color" : 0x756e49,
        "Level Requierd" : 10,
        "Description": "Nom Scientifique : `Jessenia bataua`\nLe **palmier** est **exotique** et **flamboyant**, comme un coucher de soleil sur une plage de sable fin. Ses **feuilles en éventail** s'agitent sous la brise chaude, dans un mouvement ondulant qui rappelle les danses tribales. Mais ce bois est également **résistant**, capable de **résister aux tempêtes** les plus violentes et de **protéger les mortels** des dangers de l'océan.",
        "Image" : "https://i.ibb.co/TRsKJ8Y/palm-tree.png",
        "Lj Points": 50,
        "Id": 4,
        "Rareté": r
    }
}