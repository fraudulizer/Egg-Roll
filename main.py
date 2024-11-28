import level as lev
import input as inp
import clear_screen as ot
import time as time

SLEEP_TIME = 0.1

def main():
    level = lev.load_level("level.in")
    levelmap = level[1]
    moves = level[0]
    history = ""
    points = 0
    x = 0.0

    lev.print_level(levelmap, points, moves, history)

    Game = inp.check_for_eggs(levelmap)
    eggcount = inp.count_for_eggs(levelmap)
    donecount = inp.count_for_done(levelmap)

    while Game is True and moves > 0:
        user_in = input()
        char_list = inp.to_char_list(user_in)
        for character in char_list:
            game_update = inp.user_input(character, levelmap, moves, points, moves, history)
            if inp.count_for_done(levelmap) > donecount:
                x += (inp.count_for_done(levelmap) - donecount) * 2 + moves/5
                eggcount = inp.count_for_eggs(levelmap)
                donecount = inp.count_for_done(levelmap)
    
            if inp.count_for_eggs(levelmap) < eggcount:
                x -= (eggcount - inp.count_for_eggs(levelmap))
                eggcount = inp.count_for_eggs(levelmap)
        
            points = x * 5
        
            if game_update[1] is True:
                moves -= 1
            if game_update[1] is True:
                history += character
            ot.clear_screen()
            lev.print_level(game_update[0], int(points), moves, history)
            time.sleep(SLEEP_TIME)

            Game = inp.check_for_eggs(levelmap)
    ot.clear_screen()
    lev.print_level(game_update[0], int(points), moves, history)
        
if __name__ == "__main__":
    main()