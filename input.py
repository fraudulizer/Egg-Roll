import level as lev
import clear_screen as ot

def to_char_list(input):
    if isinstance(input, str):
        return list(input)
    else:
        return

def swap(levelmap, y, x, direction):
    if direction == "up":
        dy, dx = -1, 0
    elif direction == "down":
        dy, dx = 1, 0
    elif direction == "left":
        dy, dx = 0, -1
    elif direction == "right":
        dy, dx = 0, 1
    else:
        dy, dx = 0, 0
        
    if y + dy < 0 or y + dy >= len(levelmap) or x + dx < 0 or x + dx >= len(levelmap[y]):
        return levelmap
    if levelmap[y+dy][x+dx] == lev.BRICK or levelmap[y-1][x] == lev.DONE:
        return levelmap
    elif levelmap[y+dy][x+dx] == lev.EGG:
        return levelmap
    elif levelmap[y+dy][x+dx] == lev.PAN:
        levelmap[y][x] = lev.GREEN
        return levelmap
    elif levelmap[y+dy][x+dx] == lev.NEST:
        levelmap[y+dy][x+dx] = lev.DONE
        levelmap[y][x] = lev.GREEN
        return levelmap
    elif levelmap[y+dy][x+dx] == lev.GREEN:
        levelmap[y+dy][x+dx] = lev.EGG
        levelmap[y][x] = lev.GREEN
        swap(levelmap, y+dy, x+dx, direction)
    return levelmap

def user_input(x, levelmap, moves_left):
    if x == 'F':
        for y in range(len(levelmap)):
            for x in range(len(levelmap[y])):
                if levelmap[y][x] == lev.EGG:
                     gamestate = swap(levelmap, y, x, "up")
                     Valid = True
    elif x == 'B':
        for y in range(len(levelmap) - 1, -1, -1):
            for x in range(len(levelmap[y])):
                if levelmap[y][x] == lev.EGG:
                     gamestate = swap(levelmap, y, x,  "down")
                     Valid = True
    elif x == 'L':
        for y in range(len(levelmap)):
            for x in range(len(levelmap[y])):
                if levelmap[y][x] == lev.EGG:
                    gamestate = swap(levelmap, y, x, "left")
                    Valid = True
    elif x == 'R':
        for y in range(len(levelmap)):
            for x in range(len(levelmap[y]) - 1, -1, -1):
                if levelmap[y][x] == lev.EGG:
                    gamestate = swap(levelmap, y, x, "right")
                    Valid = True
    else:
        gamestate = levelmap
        Valid = False
    return gamestate, Valid
    

        
def check_for_eggs(levelmap):
    for y in levelmap:
        if lev.EGG in y:
            return True
    return False

def count_for_eggs(levelmap):
    egg_count = 0
    for y in levelmap:
        for char in y:
            if char == lev.EGG:
                egg_count += 1
            else:
                egg_count += 0
    return egg_count

def count_for_done(levelmap):
    done_count = 0
    for y in levelmap:
        for char in y:
            if char == lev.DONE:
                done_count += 1
            else:
                done_count += 0
    return done_count