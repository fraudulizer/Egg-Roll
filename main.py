import functions as ot
import os as os
import game as game

extension = '.in'

# DISPLAYS AND ASKS THE USER TO INPUT FILE AND NAME FOR LEVEL LOADING
def play_menu():
    folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'levels')
    files = [file for file in os.listdir(folder_path) if file.endswith(extension)]
    
    for file in files:
        print(file, "\n")
    
    print("Input your preferred level's name to play the level. Input \"BACK\" to go back. Case-sensitive.")
    user_in = input()
    
    if user_in in files:
        print("Input your name to save.")
        user_name = input()
        
        if not user_name.strip():
            print("Invalid name")
            user_name = input()
        else:
            play_game(user_in, user_name)
    
    elif user_in == "back":
        main_menu()
    else:
        print("Invalid Input")
        user_in = input()

# RESTART LEVEL
def play_game(user_in, user_name):
    while True:
        score = game.play(user_in)
        save_score = user_in, score
        
        with open("files/scores.txt", mode="a", newline="") as file:
            file.write(f"{user_in}, {score}, {user_name}\n")
        
        print("Do you wish to play again? Y or N")
        restart_game = input()
        
        if restart_game == "Y":
            continue
        elif restart_game == "N":
            main_menu()
            break
        else:
            print("Invalid, please input Y or N.")

# INSTRUCTIONS     
def instructions_menu():
    with open("files/instructions.txt", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
    
    go_back()

# OPEN SCORES.TXT AND SORT FOR LEADERBOARD
def leaderboard_menu():
    print("""LEVEL NAME | SCORE | PLAYER""")
    scores = []
    
    try:
        with open("files/scores.txt") as file:
            for line in file:
                user_in, score, user_name = line.strip().split(",")
                scores.append((user_in, int(score), user_name))
        
        sorted_scores = sorted(scores, key=lambda x: (x[0], -x[1]))
        
        for score in sorted_scores:
            print(score, "\n")
    
    except FileNotFoundError:  # IF LEADERBOARD DOESNT EXIST
        print("There is no leaderboard yet.")
    
    go_back()

# ABOUT_MENU
def about_menu():
    with open("files/about.txt", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
    
    go_back()

# EXIT
def exit_game():
    exit()

# INPUT BACK IN ALL THE MENUS TO RETURN BACK TO MAIN MENU
def go_back():
    while True:
        print("Input \"BACK\" to go back.")
        user_in = input().upper()
        
        if user_in == "BACK":
            main_menu()
            break
        else:
            print("Invalid Input")

# COMMANDS FOR MAIN MENU
main_menu_commands = {
    "PLAY": play_menu,
    "INSTRUCTIONS": instructions_menu,
    "LEADERBOARD": leaderboard_menu,
    "ABOUT": about_menu,
    "EXIT": exit_game
}

# LOADS TITLE SCREEN
def main_menu():
    ot.clear_screen()
    title_screen()
    main_menu_controls()

# ART    
def title_screen():
    with open("files/title.txt", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            print(line, end=" ")
    
    print("\n")

# MAIN MENU CONTROLS
def main_menu_controls():
    print("""PLAY | INSTRUCTIONS | LEADERBOARD | ABOUT | EXIT""")
    print("""Input your command:""")
    
    while True:
        user_in = input().upper()
        
        if user_in in main_menu_commands:
            ot.clear_screen()
            main_menu_commands[user_in]()
            break
        else:
            print("Invalid Input")

# ACTUAL PROGRAM
def main():
    main_menu()

if __name__ == "__main__":
    main()
