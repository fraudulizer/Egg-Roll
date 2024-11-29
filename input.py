import level as lev
import functions as ot
import time as time

SLEEP_TIME = 0.1

def swap(levelmap, direction, points, moves, history):
    if direction == "up":
        dy, dx = -1, 0
        start_y, start_x, end_y, end_x = 0, 0, len(levelmap) -1, len(levelmap[0])
        step_y, step_x = 1, 1
    elif direction == "down":
        dy, dx = 1, 0
        start_y, start_x, end_y, end_x = len(levelmap) -1, 0, 0, len(levelmap[0])
        step_y, step_x = -1, 1
    elif direction == "left":
        dy, dx = 0, -1
        start_y, start_x, end_y, end_x = 0, len(levelmap[0]) - 1, len(levelmap), -1
        step_y, step_x = 1, -1
    elif direction == "right":
        dy, dx = 0, 1
        start_y, start_x, end_y, end_x = 0, 0, len(levelmap), len(levelmap[0])
        step_y, step_x = 1, 1
    else:
        dy, dx = 0, 0
        start_y, start_x, end_y, end_x = 0, 0, 0, 0
        step_y, step_x = 0, 0
        
    store_levelmap = [ [row[:] for row in levelmap] ] 
    move = []
    
    for y in range(start_y, end_y, step_y):
        row_length = len(levelmap[y])
        for x in range(start_x, row_length if step_x > 0 else -1, step_x):
            if levelmap[y][x] == lev.EGG:
                if y + dy < 0 or y + dy >= len(levelmap) or x + dx < 0 or x + dx >= len(levelmap[y]):
                    continue
                elif levelmap[y+dy][x+dx] == lev.BRICK or levelmap[y+dy][x+dx] == lev.DONE:
                    continue
                elif levelmap[y+dy][x+dx] == lev.EGG:
                    continue
                elif levelmap[y+dy][x+dx] == lev.PAN:
                    move.append((y, x, lev.GREEN, y+dy, x+dx, lev.PAN))
                    continue
                elif levelmap[y+dy][x+dx] == lev.NEST:
                    move.append((y, x, lev.GREEN, y+dy, x+dx, lev.DONE))
                    continue
                elif levelmap[y+dy][x+dx] == lev.GREEN:
                    levelmap[y][x] = lev.GREEN
                    move.append((y, x, lev.GREEN, y+dy, x+dx, lev.EGG))
                                        
    for y, x, old_state, new_y, new_x, new_state in move:
        levelmap[y][x] = old_state
        levelmap[new_y][new_x] = new_state

    store_levelmap.append([row[:] for row in levelmap])
        
    if len(store_levelmap) > 1 and store_levelmap[-1] == store_levelmap[-2] or lev.count_for_eggs(store_levelmap[-1]) == 0:
        levelmap = store_levelmap[-1]
        return levelmap
    else:
        for level in store_levelmap:  
            ot.clear_screen()  
            lev.print_level(level, int(points), moves, history)
            time.sleep(SLEEP_TIME)
        return swap(levelmap, direction, points, moves, history)


def user_input(x, levelmap, moves_left, points, moves, history):
    if x == 'F':
        gamestate = swap(levelmap,"up", points, moves, history)
        Valid = True
    elif x == 'B':
        gamestate = swap(levelmap, "down", points, moves, history)
        Valid = True
    elif x == 'L':
        gamestate = swap(levelmap, "left", points, moves, history)
        Valid = True
    elif x == 'R':
        gamestate = swap(levelmap, "right", points, moves, history)
        Valid = True
    else:
        gamestate = levelmap
        Valid = False
    return gamestate, Valid