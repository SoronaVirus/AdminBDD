from pymongo import MongoClient

def db_initialisation():
    client = MongoClient('mongodb://localhost:27017')
    db = client['video_game']

    db.characters.drop()
    db.monsters.drop()
    db.scores.drop()

    characters = [
        {"name": "Guerrier", "attack": 15, "armor": 10, "hp": 100},
        {"name": "Mage", "attack": 20, "armor": 5, "hp": 80},
        {"name": "Archer", "attack": 18, "armor": 7, "hp": 90},
        {"name": "Voleur", "attack": 22, "armor": 8, "hp": 85},
        {"name": "Paladin", "attack": 14, "armor": 12, "hp": 110},
        {"name": "Sorcier", "attack": 25, "armor": 3, "hp": 70},
        {"name": "Chevalier", "attack": 17, "armor": 15, "hp": 120},
        {"name": "Moine", "attack": 19, "armor": 9, "hp": 95},
        {"name": "Berserker", "attack": 23, "armor": 6, "hp": 105},
        {"name": "Chasseur", "attack": 16, "armor": 11, "hp": 100}
    ]

    monsters = [
        {"name": "Gobelin", "attack": 10, "armor": 5, "hp": 50},
        {"name": "Orc", "attack": 20, "armor": 8, "hp": 120},
        {"name": "Dragon", "attack": 35, "armor": 20, "hp": 300},
        {"name": "Zombie", "attack": 12, "armor": 6, "hp": 70},
        {"name": "Troll", "attack": 25, "armor": 15, "hp": 200},
        {"name": "Spectre", "attack": 18, "armor": 10, "hp": 100},
        {"name": "Golem", "attack": 30, "armor": 25, "hp": 250},
        {"name": "Vampire", "attack": 22, "armor": 12, "hp": 150},
        {"name": "Loup-garou", "attack": 28, "armor": 18, "hp": 180},
        {"name": "Squelette", "attack": 15, "armor": 7, "hp": 90}
    ]

    db.characters.insert_many(characters)
    db.monsters.insert_many(monsters)
    
    client.close()

if __name__ == "__main__":
    db_initialisation()