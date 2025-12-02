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

    return tea