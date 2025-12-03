import random
import time
from models import Character
from utils import *

#Affichage des persos dispo
def print_available_characters(available_characters):
    print("Characters available:\n")
    for i, character in enumerate(available_characters, 1):
        print(f"{i}. {character}")
    print_line()

#Affichage de l'équipe actuelle
def print_current_team(team):
    if team:
        print_line()
        print_title("Actual team")
        print_line()
        for j, character in enumerate(team, 1):
            print(f"Character {j} : {character.name}\n")

#Obternir le choix du perso
def get_character_choice(available_characters):
    choice = input_integer("Enter the number of the character: ", 1, len(available_characters))
    chosen_character = available_characters[choice - 1]
    available_characters.pop(choice - 1)
    return chosen_character

#Choisir le perso
def select_character(available_characters, team, number_member, player_name):
    clear_terminal()
    print_title("Team's creation")
    print(f"Player : {player_name}\n")
    if team:
        print_current_team(team)
    print(f"Selection of the character {number_member}/3\n")

    print_available_characters(available_characters)

    chosen_character = get_character_choice(available_characters)
    
    print(f"\n{chosen_character.name} added to the team.\n")
    time.sleep(2)
    
    return chosen_character

#Création de la team
def create_team(player_name):
    available_characters = get_all_characters()
    team = []

    for nb_member in range(1, 4):
        chosen_character = select_character(available_characters, team, nb_member, player_name)
        team.append(chosen_character)

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
            print_title("Defeated. get gud")
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