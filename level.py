BRICK = "🧱"
EGG = "🥚"
GREEN ="🟩"
NEST = "🪹"
DONE = "🪺"
PAN = "🍳"


def load_level(levelname):
    with open(levelname, "r", encoding="utf-8") as level:
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

def print_level(levelmap, points, moves_left, previous_moves):
    for y in levelmap:
        print(''.join(y))
    print("Previous Moves:", previous_moves)
    print("Moves Left:", moves_left)
    print("Points:", points)