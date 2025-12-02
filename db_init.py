from pymongo import MongoClient

def data_base_initialisation():
    client = MongoClient('mongodb://localhost:27017')
    db = client['video_game']

    db.personnages.drop()
    db.monstres.drop()
    db.scores.drop()

    personnages = [
        {"nom": "Guerrier", "attack": 15, "armor": 10, "hp": 100},
        {"nom": "Mage", "attack": 20, "armor": 5, "hp": 80},
        {"nom": "Archer", "attack": 18, "armor": 7, "hp": 90},
        {"nom": "Voleur", "attack": 22, "armor": 8, "hp": 85},
        {"nom": "Paladin", "attack": 14, "armor": 12, "hp": 110},
        {"nom": "Sorcier", "attack": 25, "armor": 3, "hp": 70},
        {"nom": "Chevalier", "attack": 17, "armor": 15, "hp": 120},
        {"nom": "Moine", "attack": 19, "armor": 9, "hp": 95},
        {"nom": "Berserker", "attack": 23, "armor": 6, "hp": 105},
        {"nom": "Chasseur", "attack": 16, "armor": 11, "hp": 100}
    ]

    monstres = [
        {"nom": "Gobelin", "attack": 10, "armor": 5, "hp": 50},
        {"nom": "Orc", "attack": 20, "armor": 8, "hp": 120},
        {"nom": "Dragon", "attack": 35, "armor": 20, "hp": 300},
        {"nom": "Zombie", "attack": 12, "armor": 6, "hp": 70},
        {"nom": "Troll", "attack": 25, "armor": 15, "hp": 200},
        {"nom": "Spectre", "attack": 18, "armor": 10, "hp": 100},
        {"nom": "Golem", "attack": 30, "armor": 25, "hp": 250},
        {"nom": "Vampire", "attack": 22, "armor": 12, "hp": 150},
        {"nom": "Loup-garou", "attack": 28, "armor": 18, "hp": 180},
        {"nom": "Squelette", "attack": 15, "armor": 7, "hp": 90}
    ]

    db.personnages.insert_many(personnages)
    db.monstres.insert_many(monstres)
    
    client.close()

if __name__ == "__main__":
    data_base_initialisation()