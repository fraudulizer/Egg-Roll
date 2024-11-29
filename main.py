import sys as sys
import level as lev
import input as inp
import functions as ot
import time as time

SLEEP_TIME = 0.1

def main():
    if len(sys.argv) < 2:
        print('The game requires a filename to start.', file=sys.stderr)
        return
    level = lev.load_level()
    
    levelmap = level[1]
    moves = level[0]
    history = []
    points = 0
    x = 0.0
    
    lev.print_level(levelmap, points, moves, history)

    Game = lev.check_for_eggs(levelmap)
    eggcount = lev.count_for_eggs(levelmap)
    donecount = lev.count_for_done(levelmap)

    while Game is True and moves > 0:
        user_in = input()
        char_list = ot.to_char_list(user_in)
        for character in char_list:
            game_update = inp.user_input(character, levelmap, moves, points, moves, history)
            if lev.count_for_done(levelmap) > donecount:
                x += (lev.count_for_done(levelmap) - donecount) * 2 + (moves)/5
                eggcount = lev.count_for_eggs(levelmap)
                donecount = lev.count_for_done(levelmap)
            if lev.count_for_eggs(levelmap) < eggcount:
                x -= (eggcount - lev.count_for_eggs(levelmap))
                eggcount = lev.count_for_eggs(levelmap)
            points = x * 5
            if game_update[1]:
                moves -= 1
                history.append(character)
            ot.clear_screen()
            lev.print_level(game_update[0], int(points), moves, history)
            time.sleep(SLEEP_TIME)

            Game = lev.check_for_eggs(game_update[0])
    ot.clear_screen()
    lev.print_level(game_update[0], int(points), moves, history)
        
if __name__ == "__main__":
    main()