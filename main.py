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
    draw_line()
    print("Input your preferred level's name to play the level. Input \"BACK\" to go back. Case-sensitive.")
    while True:
        user_in = input()
        if user_in in files:
            print("Input your name to save.")
            while True:
                user_name = input()
                
                if not user_name.strip():
                    print("Invalid name.")
                else:
                    play_game(user_in, user_name)
                    break
            break
        elif user_in == "BACK":
            main_menu()
            break
        else:
            print("Invalid Input")

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
    print("""These are the levels with an existing scoreboard. Enter a levels name to check its scoreboard.""")
    print("""Type in "BACK" to go back.""")
    draw_line()
    scores = [] #SCORES FROM FILE
    groupedbylevel = {} #GROUPS THE SCORES IN A DICTIONARY BY THEIR LEVELNAME
    try:
        with open("files/scores.txt") as file:
            for line in file:
                user_in, score, user_name = line.strip().split(",")
                scores.append((user_in, int(score), user_name))
            for score in scores:
                if score[0] not in groupedbylevel:
                    groupedbylevel[score[0]] = []
                groupedbylevel[score[0]].append(score)
        if groupedbylevel:
            for key in groupedbylevel.keys():
                print(key)
        draw_line()
        print("""Input your command...""")
        while True:
            user_input = input()
            if user_input in groupedbylevel:
                sorted_scores = sorted(groupedbylevel[user_input], key=lambda x: (-x[1]))
                ot.clear_screen()
                print("""LEVEL NAME | SCORE | PLAYER""")
                draw_line()
                for score in sorted_scores:
                    print(score, "\n")
                break
            elif user_input == "BACK":
                main_menu()
                break
            else:
                print("Invalid")
    except FileNotFoundError:  # IF LEADERBOARD DOESNT EXIST
        print("There is no leaderboard yet.")
    
    go_back()

# ABOUT_MENU
def about_menu():
    with open("files/about.txt", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
    
    go_back()

# EXIT
def exit_game():
    exit()

# INPUT BACK IN ALL THE MENUS TO RETURN BACK TO MAIN MENU
def go_back():
    draw_line()
    print("Input \"BACK\" to go back to the main menu.")
    while True:
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
    draw_line()
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

# DRAWS A LINE
def draw_line():
    print("""----------------------------------------------------""")

# ACTUAL PROGRAM
def main():
    main_menu()

if __name__ == "__main__":
    main()
