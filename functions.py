import os as os

#CLEARSCREEN
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux (posix)
        os.system('clear')

#CONVERT STRING TO CHAR LIST        
def to_char_list(input):
    if isinstance(input, str):
        return list(input)
    else:
        return

#FOR STORING LEVELMAP IN HISTORY
def create_deep_copy(levelmap):
    return [row[:] for row in levelmap]