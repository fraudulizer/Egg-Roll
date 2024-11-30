import level as lev
import functions as ot

def direction_parameters(direction, levelmap):
    if direction == "up":
        dy, dx = -1, 0
        start_y, start_x, end_y, end_x = 0, 0, len(levelmap) - 1, len(levelmap[0])
        step_y, step_x = 1, 1
    elif direction == "down":
        dy, dx = 1, 0
        start_y, start_x, end_y, end_x = len(levelmap) - 1, 0, 0, len(levelmap[0])
        step_y, step_x = -1, 1
    elif direction == "left":
        dy, dx = 0, -1
        start_y, start_x, end_y, end_x = 0, 0, len(levelmap), -1
        step_y, step_x = 1, 1
    elif direction == "right":
        dy, dx = 0, 1
        start_y, start_x, end_y, end_x = 0, len(levelmap[0]) - 1, len(levelmap), len(levelmap[0])
        step_y, step_x = 1, -1
    else:
        dy, dx = 0, 0
        start_y, start_x, end_y, end_x = 0, 0, 0, 0
        step_y, step_x = 0, 0
    return dy, dx, start_y, start_x, end_y, end_x, step_y, step_x

def swap(levelmap, direction, points, moves, history):
    levelmap_copy = ot.create_deep_copy(levelmap)
    dy, dx, start_y, start_x, end_y, end_x, step_y, step_x = direction_parameters(direction, levelmap_copy)
        
    store_levelmap = [ [row[:] for row in levelmap_copy] ]
    move = []

    for y in range(start_y, end_y, step_y):
        row_length = len(levelmap_copy[y])
        for x in range(start_x, row_length if step_x > 0 else -1, step_x):
            if levelmap_copy[y][x] == lev.EGG:
                if y + dy < 0 or y + dy >= len(levelmap_copy) or x + dx < 0 or x + dx >= len(levelmap_copy[y]):
                    continue
                elif levelmap_copy[y + dy][x + dx] in {lev.BRICK, lev.DONE, lev.EGG}:
                    continue
                elif levelmap_copy[y + dy][x + dx] == lev.PAN:
                    levelmap_copy[y][x] = lev.GREEN
                    move.append((y, x, lev.GREEN, y + dy, x + dx, lev.PAN))
                    continue
                elif levelmap_copy[y + dy][x + dx] == lev.NEST:
                    levelmap_copy[y][x] = lev.GREEN
                    move.append((y, x, lev.GREEN, y + dy, x + dx, lev.DONE))
                    continue
                elif levelmap_copy[y + dy][x + dx] == lev.GREEN:
                    levelmap_copy[y][x] = lev.GREEN
                    move.append((y, x, lev.GREEN, y + dy, x + dx, lev.EGG))

    for y, x, old_state, new_y, new_x, new_state in move:
        levelmap_copy[y][x] = old_state
        levelmap_copy[new_y][new_x] = new_state

    store_levelmap.append([row[:] for row in levelmap_copy])

    if len(store_levelmap) > 1 and store_levelmap[-1] == store_levelmap[-2] or lev.count_for_eggs(store_levelmap[-1]) == 0:
        return levelmap_copy
    else:
        for level in store_levelmap:  
            lev.print_level(level, int(points), moves, history)
        return swap(levelmap_copy, direction, points, moves, history)



def user_input(x, levelmap, points, moves, history):
    direction_map = {
        'F': "up",
        'B': "down",
        'L': "left",
        'R': "right"
    }
    if x in direction_map:
        direction = direction_map[x]
        gamestate = swap(levelmap, direction, points, moves, history)
        
        if gamestate == levelmap:
            Valid = False
        else:
            Valid = True
    else:
        gamestate = levelmap
        Valid = False
    return gamestate, Valid