from pymongo import MongoClient
from models import Character, Monster
import random

def get_connection():
    client = MongoClient('mongodb://localhost:27017')
    return client['video_game']

def print_line():
    print("=" * 60)

def print_title(title):
    print_line()
    print(f"{title.upper()}")
    print_line()

def get_all_characters():
    db = get_connection()
    characters_db = list(db.characters.find())
    print(characters_db)
    return [Character(c['name'], c['attack'], c['armor'], c['hp']) for c in characters_db]

def get_random_monster():
    db = get_connection()
    monsters_db = list(db.monsters.find())
    monster_data = random.choice(monsters_db)
    return Monster(monster_data['name'], monster_data['attack'], monster_data['armor'], monster_data['hp'])

def save_score(player_name, score):
    db = get_connection()
    db.scores.insert_one({
        "player": player_name,
        "waves": score
    })

def get_best_scores():
    db = get_connection()
    scores = list(db.scores.find().sort("waves", -1).limit(3))
    return scores

def print_leaderboard():
    print_title("Leaderboard of the best scores.")
    scores = get_best_scores()

    if not scores:
        print("No score are saved actually")
    else:
        for i, score in enumerate(scores, 1):
            print(f"{i}. {score['player']} - {score['waves']} waves")

    print_line()

def input_integer(message, min_val, max_val):
    while True:
        try:
            value = input(message)
            value = int(value)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Chose a number between {min_val} and {max_val}.")
        except ValueError:
            print("Chose a correct number.")

def input_text(message):
    while True:
        text = input(message).strip()
        if text:
            return text
        else:
            print("The text cannot be empty.")