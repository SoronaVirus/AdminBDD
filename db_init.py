from pymongo import MongoClient

def db_initialisation():
    client = MongoClient('mongodb://localhost:27017')
    db = client['video_game']

    db.characters.drop()
    db.monsters.drop()
    db.effects.drop()
    db.rarities.drop()

    characters = [
        {"name": "Guerrier", "attack": 15, "armor": 10, "hp": 100, "crit_chance": 12, "evasion": 10, "lifesteal": 0, "thorns": 0},
        {"name": "Mage", "attack": 20, "armor": 5, "hp": 80, "crit_chance": 18, "evasion": 8, "lifesteal": 0, "thorns": 0},
        {"name": "Archer", "attack": 18, "armor": 7, "hp": 90, "crit_chance": 28, "evasion": 15, "lifesteal": 0, "thorns": 0},
        {"name": "Voleur", "attack": 22, "armor": 8, "hp": 85, "crit_chance": 35, "evasion": 30, "lifesteal": 0, "thorns": 0},
        {"name": "Paladin", "attack": 14, "armor": 12, "hp": 110, "crit_chance": 8, "evasion": 5, "lifesteal": 0, "thorns": 0},
        {"name": "Sorcier", "attack": 25, "armor": 3, "hp": 70, "crit_chance": 22, "evasion": 12, "lifesteal": 0, "thorns": 0},
        {"name": "Chevalier", "attack": 17, "armor": 15, "hp": 120, "crit_chance": 10, "evasion": 3, "lifesteal": 0, "thorns": 0},
        {"name": "Moine", "attack": 19, "armor": 9, "hp": 95, "crit_chance": 25, "evasion": 25, "lifesteal": 0, "thorns": 0},
        {"name": "Berserker", "attack": 23, "armor": 6, "hp": 105, "crit_chance": 20, "evasion": 7, "lifesteal": 0, "thorns": 0},
        {"name": "Chasseur", "attack": 16, "armor": 11, "hp": 100, "crit_chance": 30, "evasion": 18, "lifesteal": 0, "thorns": 0}
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

    effects = [
        {
            "key": "evasion_boost",
            "name": "Evasion boost",
            "stat": "evasion",
            "description": "EVA",
            "values": {
                "Common": 3,
                "Rare": 5,
                "Epic": 8,
                "Exotic": 12,
                "Legendary": 18
            }
        },
        {
            "key": "crit_boost",
            "name": "Accuracy boosted",
            "stat": "crit_chance",
            "description": "CRIT",
            "values": {
                "Common": 3,
                "Rare": 5,
                "Epic": 8,
                "Exotic": 12,
                "Legendary": 18
            }
        },
        {
            "key": "crit_mult_boost",
            "name": "Critical multiplier boosted",
            "stat": "crit_multiplier",
            "description": "Critical multiplier",
            "values": {
                "Common": 0.2,
                "Rare": 0.4,
                "Epic": 0.6,
                "Exotic": 0.9,
                "Legendary": 1.3
            }
        },
        {
            "key": "attack_boost",
            "name": "Attack boosted",
            "stat": "attack_power",
            "description": "ATK",
            "values": {
                "Common": 2,
                "Rare": 4,
                "Epic": 6,
                "Exotic": 9,
                "Legendary": 13
            }
        },
        {
            "key": "defense_boost",
            "name": "Armor boosted",
            "stat": "armor",
            "description": "DEF",
            "values": {
                "Common": 2,
                "Rare": 3,
                "Epic": 5,
                "Exotic": 7,
                "Legendary": 10
            }
        },
        {
            "key": "health_boost",
            "name": "Heal",
            "stat": "hp",
            "description": "HP",
            "values": {
                "Common": 15,
                "Rare": 30,
                "Epic": 50,
                "Exotic": 80,
                "Legendary": 120
            }
        },
        {
            "key": "vampire",
            "name": "Lifesteal",
            "stat": "lifesteal",
            "description": "Lifesteal (%)",
            "values": {
                "Common": 5,
                "Rare": 10,
                "Epic": 15,
                "Exotic": 22,
                "Legendary": 30
            }
        },
        {
            "key": "thorns",
            "name": "Thorns",
            "stat": "thorns",
            "description": "Returned damage",
            "values": {
                "Common": 3,
                "Rare": 5,
                "Epic": 8,
                "Exotic": 12,
                "Legendary": 18
            }
        }
    ]

    rarities = [
        {"name": "Common", "weight": 50, "color": "\033[90m"},
        {"name": "Rare", "weight": 30, "color": "\033[34m"},
        {"name": "Epic", "weight": 15, "color": "\033[35m"},
        {"name": "Exotic", "weight": 4, "color": "\033[91m"},
        {"name": "Legendary", "weight": 1, "color": "\033[93m"}
    ]

    db.characters.insert_many(characters)
    db.monsters.insert_many(monsters)
    db.effects.insert_many(effects)
    db.rarities.insert_many(rarities)
    
    client.close()

if __name__ == "__main__":
    db_initialisation()