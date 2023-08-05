import random

board_1 = [None, 7, None, None, 6, None, 2, None, None, None, 2, None, None, None, None, 8, None, None, None, 4, 6, 8, 9, None, 7, 1, 5, None, 8, 4, 7, 1, None, None, None, None, None, 9, 7, None, None, None, 1, 3, None,
    None, None, None, None, 5, 9, 4, 8, None, 6, 9, 7, None, 5, 8, 4, 3, None, None, None, 2, None, None, None, None, 8, None, None, None, 8, None, 6, None, None, 7, None]

board_2 = [5, 3, None, 6, None, None, None, 9, 8, None, 7, None, 1, 9, 5, None, None, None, None, None, None, None, None, None, None, 6, None, 8, None, None, 4, None, None, 7, None, None, None, 6, None, 8, None, 3,
    None, 2, None, None, None, 3, None, None, 1, None, None, 6, None, 6, None, None, None, None, None, None, None, None, None, None, 4, 1, 9, None, 8, None, 2, 8, None, None, None, 5,None, 7, 9]

board_3 = [None, None, 3, None, 6, None, 4, 9, None, None, None, None, 9, 8, None, None, 3, 1, 2, None, None, None, 4, 3, None, None, 6, 9, None, 7, None, 4, None, None, None, 5,None, None, None, None, 9, 8, 4, None, 
    7, 8, 6, None, None, None, None, 1, None, 9, 6, None, None, 5, None, 8, 2, None, 9,None, None, 3, 1, None, None, None, 5, 6,9, None, 5, None, 7, 2, None, 3, 8]

board_4 = [1, None, None, 7, 3, None, None, None, None, 4, 8, 9, None, None, None, None, None, 1, None, None, 6, None, 4, None, 2, 9, 5, None, None, 7, 5, None, None, None, None, 6, 1, 2, None, 7, None, 3, None, 9, 5, 6, None, None, None, 
    None, 8, 7, None, None, 9, 1, 4, None, 2, None, 8, None, None, 6, None, None, None, None, None, 5, 1, 2, None, None, None, None, 3, 7, None, None, 4]

boards = [board_1, board_2, board_3, board_4]

print(len(board_4))

def get_board():
    return random.choice(boards)
