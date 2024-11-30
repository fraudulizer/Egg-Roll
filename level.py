import sys as sys
import time as time
import functions as ot

SLEEP_TIME = 0.1

BRICK = "🧱"
EGG = "🥚"
GREEN ="🟩"
NEST = "🪹"
DONE = "🪺"
PAN = "🍳"

def load_level():
    with open(sys.argv[1], encoding='utf-8') as level:
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
    

def print_level(levelmap, points, moves, history):
    ot.clear_screen()
    for y in levelmap:
        print(''.join(y))
    print("Previous Moves:",  ''.join(history))
    print("Moves Left:", moves)
    print("Points:", points)
    time.sleep(SLEEP_TIME)
    
def check_for_eggs(levelmap):
    for y in levelmap:
        if EGG in y:
            return True
    return False

def count_for_eggs(levelmap):
    egg_count = 0
    for y in levelmap:
        for char in y:
            if char == EGG:
                egg_count += 1
            else:
                egg_count += 0
    return egg_count

def count_for_done(levelmap):
    done_count = 0
    for y in levelmap:
        for char in y:
            if char == DONE:
                done_count += 1
            else:
                done_count += 0
    return done_count