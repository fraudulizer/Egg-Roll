import sys as sys
import level as lev
import input as inp
import functions as ot
import time as time

# IF UNDO
def undo(levelmap_history, history, points_history, points, moves, levelmap):
    if levelmap_history and history and points_history:
        if len(levelmap_history) > 1:
            levelmap = levelmap_history[-2]
            levelmap_history.pop()
            history.pop()
            points_history.pop()
            points = points_history[-1]
            moves += 1
            lev.print_level(levelmap, int(points), moves, history)
    return levelmap_history, history, points_history, points, moves, levelmap

# IF HELP
def help(levelmap_history, history, points_history, points, moves, levelmap):
    print("F : UP")
    print("B : DOWN")
    print("L : LEFT")
    print("R : RIGHT")
    print("undo : UNDO LAST MOVE")
    print("help : HELP")
    print("CASE SENSITIVE")
    return levelmap_history, history, points_history, points, moves, levelmap

# DICT FOR UNDO
commands = {
    "undo": undo,
    "help": help
}

# ACTUAL GAME
def play(filename):
    level = lev.load_level(filename)

    levelmap_history = []
    levelmap = level[1]
    levelmap_history.append(levelmap)
    moves = level[0]
    history = []
    points = 0
    points_history = [0]
    x = 0.0

    lev.print_level(levelmap, points, moves, history)

    Game = lev.check_for_eggs(levelmap)
    eggcount = lev.count_for_eggs(levelmap)
    donecount = lev.count_for_done(levelmap)

    while Game is True and moves > 0:
        print("Enter Move/s:", end="")
        user_in = input()
        
        if user_in in commands:
            levelmap_history, history, points_history, points, moves, levelmap = commands[user_in](levelmap_history, history, points_history, points, moves, levelmap)
        else:
            char_list = ot.to_char_list(user_in)
            for character in char_list:
                game_update = inp.user_input(character, levelmap, points, moves, history)
                levelmap = game_update[0]
                
                if lev.count_for_done(levelmap) > donecount:
                    x += ((lev.count_for_done(levelmap) - donecount) * 2) + moves / 5
                    eggcount = lev.count_for_eggs(levelmap)
                    donecount = lev.count_for_done(levelmap)

                if lev.count_for_eggs(levelmap) < eggcount:
                    x -= (eggcount - lev.count_for_eggs(levelmap))
                    eggcount = lev.count_for_eggs(levelmap)
                    
                points = x * 5
                points_history.append(points)
                
                if game_update[1]:
                    moves -= 1
                    history.append(character)
                    
                lev.print_level(levelmap, int(points), moves, history)
                
                if not game_update[1]:
                    print("Nothing would change.")
                
                levelmap_history.append(levelmap)

            Game = lev.check_for_eggs(levelmap)

    lev.print_level(levelmap, int(points), moves, history)
    return int(points)
