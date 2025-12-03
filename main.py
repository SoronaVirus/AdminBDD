from game import start_game
from utils import print_leaderboard, print_title, input_integer

def print_menu():
    print_title("Surviving game - Menu")
    print("1. Start game")
    print("2. Show leaderboard")
    print("3. Ragequit\n")

def main():
    while True:
        print_menu()
        choice = input_integer("Chose an option (1-3): ", 1, 3)
        print("\n")

        match(choice):
            case 1:
                start_game()
            
            case 2:
                print_leaderboard()
                input("\nPress Enter to continue")

            case 3:
                print_title("Lowkey a noob")
                print("Thanks for playing tho")
                break

if __name__ == "__main__":
    main()