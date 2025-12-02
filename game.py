import random
import time
from models import Character
from utils import *

def create_team(player_name):
    available_characters = get_all_characters()
    team = []

    print_title("Team's creation")
    print(f"Player : {player_name}")
    print("\nCharacters available:\n")

    for i, character in enumerate(available_characters, 1):
        print(f"{i}. {character}")

    print_line()

    for nb_member in range(1, 4):
        print(f"\nSelection of the character {nb_member}/3")
        choice = input_integer("Enter the number of the character: ", 1, len(available_characters))

        chosen_character = available_characters[choice - 1]
        team.append(chosen_character)

        available_characters.pop(choice - 1)

        print(f"{chosen_character} added to the team.")

        if nb_member < 3:
            print("\nActual team:")
            for j, character in enumerate(team, 1):
                print(f"Character {j} : {character}")

    return team

def print_team(team):
    print("\n--- Your team ---")
    for i, character in enumerate(team, 1):
        if character.is_alive():
            status = "Dead"
        else:
            status = "Alive"
        print(f'{status}. Character {i}: {character}')

def combat_turn(team, monster):
    print_line()
    print("Team's turn.")
    print_line()

    for character in team:
        if character.is_alive():
            damage = character.attack(monster)
            print(f"{character.name} attacks {monster.name} and deals {damage} damage.")

            if not monster.is_alive():
                print(f"\n{monster.name} is dead.")
                return True
            
            time.sleep(0.3)
    
    print(f"\n{monster.name} HP left: {monster.hp}/{monster.hp_max}")

    print_line()
    print("Monster's turn.")
    print_line()

    alive_characters = []
    for c in team:
        if c.is_alive():
            alive_characters.append(c)

    if alive_characters:
        target = random.choice(alive_characters)
        damage = monster.attack(target)
        print(f"{monster.name} attacks {character.name} and deals {damage} damage.")

        if not character.is_alive():
            print(f"\n{character.name} is dead.")

    time.sleep(0.3)
    return False
            
def verified_defeat(team):
    for c in team:
        if c.is_alive():
            return False
    return True  

def start_game():
    print_title("Starting game.")

    player_name = input_text("Enter your name: ")
    team = create_team(player_name)

    print_title("Starting fight.")
    print_team(team)

    time.sleep(1)

    wave = 0

    while True:
        wave +=1

        print_title(f"Wave {wave}")

        monster = get_random_monster()
        print(f"\n A {monster.name} appears.")
        print(f"{monster}\n")

        print_team(team)

        time.sleep(0.5)

        while monster.is_alive() and not verified_defeat(team):
            victory = combat_turn(team, monster)

            if victory:
                break

            if verified_defeat(team):
                break

            print_team(team)
            time.sleep(0.5)
        
        if verified_defeat(team):
            print_title("Defeat. get gud")
            print(f"\nYou lost at the wave number {wave}")
            if wave < 2:
                print(f"You've survived {wave} wave.")
            else:
                print(f"You've survived {wave} wave.")

            save_score(player_name, wave - 1)
            print_line()
            break

        print(f"\nWave's finished.")
        time.sleep(1)