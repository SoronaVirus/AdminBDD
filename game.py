import random
import time
from models import Character
from utils import *

def create_team(player_name):
    available_characters = get_all_characters()
    team = []

    clear_terminal()
    print_title("Team's creation")
    print(f"Player : {player_name}\n")

    for nb_member in range(1, 4):
        print(f"Selection of the character {nb_member}/3\n")
        print("Characters available:\n")

        for i, character in enumerate(available_characters, 1):
            print(f"{i}. {character}")

        print_line()

        choice = input_integer("Enter the number of the character: ", 1, len(available_characters))

        chosen_character = available_characters[choice - 1]
        team.append(chosen_character)

        available_characters.pop(choice - 1)

        print(f"\n{chosen_character.name} added to the team.\n")

        if nb_member < 3:
            clear_terminal()
            print("Actual team:")
            for j, character in enumerate(team, 1):
                print(f"Character {j} : {character.name}")
            print("\n")
            print_title("Team's creation")
            print(f"Player : {player_name}\n")

    return team

def print_team(team):
    print("\n--- Your team ---")
    for i, character in enumerate(team, 1):
        if character.is_alive():
            status = "Alive"
        else:
            status = "Dead"
        print(f'{status}. Character {i}: {character}')

def combat_turn(team, monster):
    print_line()
    print("Team's turn.")
    print_line()

    for character in team:
        if character.is_alive():
            damage, is_critical = character.attack(monster)
            if is_critical:
                print(f"MASTERCLASS CRITICAL HIT. {character.name} attacks {monster.name} and deals {damage} damage.")
            else:
                print(f"{character.name} attacks {monster.name} and deals {damage} damage.")

            if not monster.is_alive():
                print(f"\n{monster.name} is dead.")
                return True
            
            time.sleep(3)
    
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
        damage, hit_success = monster.attack(target)

        if hit_success:
            print(f"{monster.name} attacks {target.name} and deals {damage} damage.")
        else:
            print(f"OHMAGAAAAAD DODGED ATTACK MAAAN!!! {monster.name} attacks but {target.name} dodge like Wesker")

        if not target.is_alive():
            print(f"\n{target.name} is dead.")

    time.sleep(3)
    return False
            
def verified_defeat(team):
    for c in team:
        if c.is_alive():
            return False
    return True  

def start_game():
    clear_terminal()
    print_title("Starting game")

    player_name = input_text("Enter your name: ")
    team = create_team(player_name)

    clear_terminal()
    print_title("Starting fight.")
    print_team(team)

    time.sleep(2)

    wave = 0

    while True:
        wave +=1

        clear_terminal()
        print_title(f"Wave {wave}")

        monster = get_random_monster()
        print(f"\nA {monster.name} appears.")
        print(f"{monster}\n")

        print_team(team)

        time.sleep(2)

        while monster.is_alive() and not verified_defeat(team):
            victory = combat_turn(team, monster)

            if victory:
                break

            if verified_defeat(team):
                break

            clear_terminal()
            print_title(f"Wave {wave}")
            print(f"\nFighting {monster.name}...\n")
            print_team(team)
            time.sleep(2)
        
        if verified_defeat(team):
            clear_terminal()
            print_title("Defeat. get gud")
            print(f"\nYou lost at the wave number {wave}")
            if wave == 0:
                print(f"You've survived 0 wave.")
            elif wave == 1:
                print(f"You've survived 1 wave.")
            else:
                print(f"You've survived {wave - 1} waves.")

            save_score(player_name, wave - 1)
            print_line()
            break

        print(f"\nWave's finished.")
        time.sleep(3)