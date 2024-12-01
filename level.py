import sys as sys
import time as time
import functions as ot

SLEEP_TIME = 0.1

BRICK = "🧱"
EGG = "🥚"
GREEN = "🟩"
NEST = "🪹"
DONE = "🪺"
PAN = "🍳"

# LOAD LEVEL
def load_level(filename):
    with open(f"levels/{filename}", encoding='utf-8') as level:
        row = int(level.readline().strip())
        maximum_moves = int(level.readline().strip())
        
        levelmap = []
        line_count = 0
        for line in level:
            if line_count >= row:
                break
            levelmap.append(list(line.strip()))
            line_count += 1
            
    return maximum_moves, levelmap

# PRINT LEVEL
def print_level(levelmap, points, moves, history):
    ot.clear_screen()
    for y in levelmap:
        print(''.join(y))
    print("Previous Moves:", ''.join(history))
    print("Moves Left:", moves)
    print("Points:", points)
    time.sleep(SLEEP_TIME)

# CHECK IF EGGS STILL IN BOARD    
def check_for_eggs(levelmap):
    for y in levelmap:
        if EGG in y:
            return True
    return False

# CHECK HOW MANY EGGS LEFT
def count_for_eggs(levelmap):
    egg_count = 0
    for y in levelmap:
        for char in y:
            if char == EGG:
                egg_count += 1
    return egg_count

# CHECK HOW MANY NESTS FILLED
def count_for_done(levelmap):
    done_count = 0
    for y in levelmap:
        for char in y:
            if char == DONE:
                done_count += 1
    return done_count