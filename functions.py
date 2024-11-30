import os as os

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux (posix)
        os.system('clear')
        
def to_char_list(input):
    if isinstance(input, str):
        return list(input)
    else:
        return

def create_deep_copy(levelmap):
    return [row[:] for row in levelmap]