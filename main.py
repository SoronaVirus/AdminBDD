from game import start_game
from utils import *

def print_menu():
    print_title("Surviving game - Menu")
    print("1. Start game")
    print("2. Show leaderboard")
    print("3. Ragequit\n")

def main():
    while True:
        clear_terminal()
        print_menu()
        choice = input_integer("Chose an option (1-3): ", 1, 3)

        match(choice):
            case 1:
                start_game()
            
            case 2:
                clear_terminal()
                print_leaderboard()
                input("\nPress Enter to continue")

            case 3:
                clear_terminal()
                print_title("Lowkey a noob")
                print("Thanks for playing tho")
                break

if __name__ == "__main__":
    main()