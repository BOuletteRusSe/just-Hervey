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
        "Description": "Nom Scientifique : `Quercus`\nLe **Bois de Chêne** est **robuste** et **puissant**, comme un ancien guerrier de légende. Il résiste aux assauts du **temps** et des **éléments**, et son **écorce rugueuse** témoigne de la **dureté** de son existence. Mais sous cette apparence **rude** se **cache une âme généreuse**, capable de nourrir les flammes de la vie elle-même.",
        "Image" : "https://i.ibb.co/DLQ9X43/image-2023-02-26-201131792.png",
        "Lj Points": 25,
        "Id": 0,
        "Rareté": c,
        "Ex": 100
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
        "Description": "Nom Scientifique : `Akis - Robinia Pseudacacia`\nLe **Bois d'Acacia** est **léger** et **élégant**, tel un danseur gracieux dans un ballet enchanté. Ses **branches délicates** se courbent sous le poids des feuilles, comme des franges d'un voile qui virevolte au vent. Mais ne vous y trompez pas, car ce bois est également **redoutable**, capable de **fendre les armures les plus solides**.",
        "Image" : "https://i.ibb.co/6Pt9fnf/acacia.png",
        "Lj Points": 40,
        "Id": 1,
        "Rareté": c,
        "Ex": 200
    },
    "Birch" : {
        "Proba": 5,
        "Hp": 8,
        "Name" : "du **Bouleau** !",
        "Emoji" : "<:birch:1085287711843307590>",
        "Price" : 200,
        "Xp" : 75,
        "Color" : 0xd1d1d1,
        "Level Requierd" : 0,
        "Description": "Nom Scientifique : `Betula pendula`\n",
        "Image" : "https://i.ibb.co/vdcDXPL/birch.png",
        "Lj Points": (20, 60),
        "Id": 5,
        "Rareté": c,
        "Ex": 225
    },
    "Plane Tree" : {
        "Proba": 4.5,
        "Hp": 20,
        "Name" : "du **Platane** !",
        "Emoji" : "<:plane_tree:1085287711843307590>",
        "Price" : 300,
        "Xp" : 70,
        "Color" : 0x614126,
        "Level Requierd" : 5,
        "Description": "Nom Scientifique : `Platanus`\nLe **Bois de Platane** est un matériau noble, qui a traversé les siècles sans prendre une ride. Il est à la fois **résistant** et **élégant**, comme un guerrier vêtu de sa plus belle armure. Ses **fibres solides** peuvent encaisser les coups les plus rudes, et sa couleur sombre témoigne de sa longue histoire. On dit que les armes forgées dans ce bois ont une âme, et que leur propriétaire est béni par les dieux.",
        "Image" : "https://i.ibb.co/5rRvfKD/plane-tree.png",
        "Lj Points": 75,
        "Id": 6,
        "Rareté": r,
        "Ex": 500
    },
    "Dark Oak" : {
        "Proba": 5,
        "Hp": 10,
        "Name" : "un **Chêne Noir** !\n",
        "Emoji" : "<:darkoak:1079485589512007740>",
        "Price" : 250,
        "Xp" : (50, 100),
        "Color" : 0x2E2A20,
        "Level Requierd" : 5,
        "Description": "Nom Scientifique : `Quercus`\nLe **Bois de Chêne Noir** est **sombre** et **mystérieux**, comme les ombres qui se glissent dans la nuit. Il pousse dans les **terres maudites**, où les esprits tourmentés errent sans fin. Ses **racines** s'enfoncent **profondément dans la terre**, puisent dans **les ténèbres** pour renforcer leur essence. Mais qui sait ce qui se cache dans ses profondeurs ?",
        "Image" : "https://i.ibb.co/j3Rh3T2/dark-oak.png",
        "Lj Points": 50,
        "Id": 2,
        "Rareté": p,
        "Ex": 175
    },
    "Basswood" : {
        "Proba": 6,
        "Hp": 10,
        "Name" : "du **Tilleul** !",
        "Emoji" : "<:basswood:1085288491807678577>",
        "Price" : (150, 300),
        "Xp" : 75,
        "Color" : 0xD0AB4F,
        "Level Requierd" : 5,
        "Description": "Nom Scientifique : `Tilia cordata`\nLe **bois de tilleul** est **doux** et **apaisant**, comme une berceuse murmurée à l'oreille d'un enfant. Ses **feuilles odorantes** exhalent un **parfum sucré**, tandis que son **écorce lisse et soyeuse** invite au toucher. C'est un bois qui **soigne**, qui **réconforte**, qui **enveloppe** de son étreinte chaleureuse.",
        "Image" : "https://i.ibb.co/VqrF7k5/basswood.png",
        "Lj Points": (35, 50),
        "Id": 3,
        "Rareté": c,
        "Ex": 150
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
        "Description": "Nom Scientifique : `Jessenia bataua`\nLe **Palmier** est **exotique** et **flamboyant**, comme un coucher de soleil sur une plage de sable fin. Ses **feuilles en éventail** s'agitent sous la brise chaude, dans un mouvement ondulant qui rappelle les danses tribales. Mais ce bois est également **résistant**, capable de **résister aux tempêtes** les plus violentes et de **protéger les mortels** des dangers de l'océan.",
        "Image" : "https://i.ibb.co/TRsKJ8Y/palm-tree.png",
        "Lj Points": 50,
        "Id": 4,
        "Rareté": r,
        "Ex": 250
    },
    "Fir": {
        "Proba": 5,
        "Hp": 12,
        "Name" : "du **sapin** !",
        "Emoji" : "<:fir:1085526551673720886>",
        "Price" : 400,
        "Xp" : 120,
        "Color" : 0x1A6600,
        "Level Requierd" : 10,
        "Description": "Nom Scientifique : `Pinus`\nLe **Sapin** est un arbre majestueux, au feuillage dense et aux branches solides. Son bois est très apprécié pour sa résistance et son odeur caractéristique, qui rappelle les fêtes de fin d'année. Mais attention, car ce bois est également très **glissant** et peut causer des accidents lors de la manipulation.",
        "Image" : "https://i.ibb.co/yddF19S/fir.png",
        "Lj Points": 80,
        "Id": 7,
        "Rareté": p,
        "Ex": 350
    },
    "Dark Conifer" : {
        "Proba": 2.5,
        "Hp": 15,
        "Name" : "un **Conifère sombre** !",
        "Emoji" : "<:dark_conifer:1085528910395097148>",
        "Price" : 500,
        "Xp" : 150,
        "Color" : 0x2B2B2B,
        "Level Requierd" : 10,
        "Description": "Nom Scientifique : `Pinus Nigra`\nLe **Conifère Sombre** est un arbre majestueux qui domine les forêts de haute montagne. Son bois est **dense** et **résistant**, capable de supporter les pires conditions climatiques. Les **aiguilles sombres** de cet arbre imposant sont un symbole de force et de puissance, un rappel de la nature impitoyable qui nous entoure.",
        "Image" : "https://i.ibb.co/4sTNR17/dark-conifer.png",
        "Lj Points": 100,
        "Id": 8,
        "Rareté": e,
        "Ex": 750
    },
    "Hêtre" : {
        "Proba": 3,
        "Hp": 30,
        "Name" : "de l'**Hêtre** !",
        "Emoji" : "<:hetre:1085978345755394189>",
        "Price" : 600,
        "Xp" : 300,
        "Color" : 0x8B5A2B,
        "Level Requierd" : 10,
        "Description": "Nom Scientifique : `Fagus Sylvatica`\nL'**Hêtre** est un arbre majestueux au tronc imposant et aux feuilles en forme de coeur. Il est considéré comme l'un des arbres les plus sacrés de la forêt, et on raconte que ses racines plongent dans les profondeurs de la terre jusqu'au royaume des morts. Les branches du Hêtre sont le refuge de nombreuses créatures magiques et mystiques, mais il est également connu pour être le lieu de rassemblement des sorcières lors des nuits de pleine lune.",
        "Image" : "https://i.ibb.co/F8h0pd4/hetre.png",
        "Lj Points": 75,
        "Id": 10,
        "Rareté": r,
        "Ex": 800
    },
    "Death Tree" : {
        "Proba": 2,
        "Hp": 3,
        "Name" : "un **Arbre Mort** !",
        "Emoji" : "<:death_tree:1085981143821729882>",
        "Price" : 100,
        "Xp" : 75,
        "Color" : 0x808080,
        "Level Requierd" : 20,
        "Description": "Dans les profondeurs des bois hantés, se dresse un **Arbre Mort**. Son tronc est recouvert de marques et de cicatrices qui semblent avoir été infligées par des griffes acérées. Les racines s'étendent telle une toile qui piége tout ce qui s'en approche. Les feuilles, autrefois vertes et pleines de vie, sont maintenant fanées et desséchées, donnant à l'arbre un aspect sinistre et mortuaire. Pourtant, malgré cette apparence effrayante, les voyageurs intrépides qui osent s'en approcher pourront y trouver des trésors enfouis depuis des siècles.",
        "Image" : "https://i.ibb.co/bL18WKg/death-tree.png",
        "Lj Points": 75,
        "Id": 11,
        "Rareté": r,
        "Ex": 500
    },
    "Moon Conifer": {
        "Proba": 1,
        "Hp": 50,
        "Name": "un **Conifère Lunaire** !",
        "Emoji": "<:moon_conifer:1085529718020915220>",
        "Price": 1000,
        "Xp": 250,
        "Color": 0x593AC2,
        "Level Requierd": 20,
        "Description": "Nom Scientifique : `Arbor Noctis - Pinus Lunaris`\nLe **Conifère Lunaire** est une créature végétale de la nuit, née de **la lune** elle-même. Son **bois noir** et **coriace** est imprégné d'une **magie ancienne**, capable de maudire les ennemis les plus téméraires. Ses **épines acérées** reflètent la lumière lunaire, faisant briller l'obscurité de la forêt comme des étoiles tombées du ciel. Ses **racines** se nourrissent de l'**énergie sombre** de la nuit, lui conférant une **force inépuisable**. Mais prenez garde, car le **Conifère Lunaire** ne tolère aucun intrus sur son territoire, et ceux qui osent défier sa puissance en ressortent souvent changés à jamais.",
        "Image": "https://i.ibb.co/7r0rpK6/moon-conifer.png",
        "Lj Points": 150,
        "Id": 9,
        "Rareté": l,
        "Ex": 1500
    },
    "Sacred Oak": {
        "Proba": 0.125,
        "Hp": 100,
        "Name": "un **Chêne Sacré** !",
        "Emoji": "<:sacred_oak:1085982467044950047>",
        "Price": 10000,
        "Xp": 750,
        "Color": 0x5D4037,
        "Level Requierd": 25,
        "Description": "Le **Chêne sacré** est un arbre millénaire qui incarne la puissance de la nature. Ses racines plongent profondément dans la terre, tandis que ses branches majestueuses s'élèvent vers le ciel, tel un témoignage de la grandeur et de la sagesse des anciens dieux. Les feuilles du Chêne sacré sont d'un vert émeraude éclatant, mais leur beauté cache un pouvoir mystique et terrifiant. Quiconque ose profaner l'arbre sacré en sera maudit à jamais, condamné à errer dans les ténèbres éternelles.",
        "Image": "https://i.ibb.co/gFGnGS4/sacred-oak.png",
        "Lj Points": 2500,
        "Id": 12,
        "Rareté": d,
        "Ex": 17500
    }
}

seeds = {
    
}