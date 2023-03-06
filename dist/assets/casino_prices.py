rewards = {
    (":heavy_dollar_sign:", ":heavy_dollar_sign:", ":heavy_dollar_sign:") : {
        "Description" : {
            ":heavy_dollar_sign: :heavy_dollar_sign: :heavy_dollar_sign:•" : "Vous gagnez **5,000**€."
        },
        "Money" : 5000
    },
    (":moneybag:", ":moneybag:", ":moneybag:") : {
        "Description" : {
            ":moneybag: :moneybag: :moneybag: •" : "Vous gagnez **10,000**€."
        },
        "Money" : 10000
    },
    (":gem:", ":gem:", ":gem:") : {
        "Description": {
            ":gem: :gem: :gem: •" : "Vous gagnez **25,000**€."
        },
        "Money" : 25000
    },
    (":question:", ":question:", ":question:") : {
        "Description" : {
            ":question: :question: :question: •" : "Vous gagnez entre **0** et **10,000**€ (aléatoire)."
        },
        "Money" : [0, 10000]
    },
    (":pick:", ":pick:", ":pick:") : {
        "Description" : {
            ":pick: :pick: :pick: •" : "Vous gagnez la pioche du casino (chaque fois que vous minez vous avez **1/10** de chance d'obtenir un ticket pour le casino)."
        },
        "Item" : 10
    },
    (":seven:", ":seven:", ":seven:") : {
        "Description" : {
            ":seven: :seven: :seven: •" : "Vous gagnez un grade \"Gagnant du Casino\"."
        },
        "Rank" : 12
    }
}
rewards_mineur = {
    ":test_tube:": {
        "Description": ":test_tube: • Vous gagnez de l'xp pour le métier de mineur !",
        "Xp": [1000, 10000]
    },
    ":scroll:": {
        "Description": ":scroll: • Vous avec trouvé un parchemin !",
        "Plan": {
            "2": 7,
            "4": 5,
            "7": 9,
            "0": 8   
            }
    }
}