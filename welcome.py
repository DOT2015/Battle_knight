from os import system
from startup import knights, items


# Function to draw state of the board, based on knights and items.
def board_state():

    # Create an empty 8* board.
    board = [[' ']*8 for i in range(8)]

    # items in their correct board squares, if they have no holder.
    for item in items:
        if item.holder is None:
            board[item.position[0]][item.position[1]] = item.code

    # knights in their correct board squares, when alive.
    for knight in knights:
        if knight.status == 'ALIVE':
            board[knight.position[0]][knight.position[1]] = knight.code

    # Print the board, with separator pipes.
    for line in board:
        print('|'.join(line))

def welcome():
    for item in items:
        system('cls')
        print('\nWELCOME TO BATTLE KNIGHTS!\n')
        board_state()
        print('\n')
        