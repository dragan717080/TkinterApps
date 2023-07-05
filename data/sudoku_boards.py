import random

board_1 = [None, 7, None, None, 6, None, 2, None, None, None, 2, None, None, None, None, 8, None, None, None, 4, 6, 8, 9, None, 7, 1, 5, None, 8, 4, 7, 1, None, None, None, None, None, 9, 7, None, None, None, 1, 3, None,
    None, None, None, None, 5, 9, 4, 8, None, 6, 9, 7, None, 5, 8, 4, 3, None, None, None, 2, None, None, None, None, 8, None, None, None, 8, None, 6, None, None, 7, None]

board_2 = [5, 3, None, 6, None, None, None, 9, 8, None, 7, None, 1, 9, 5, None, None, None, None, None, None, None, None, None, None, 6, None, 8, None, None, 4, None, None, 7, None, None, None, 6, None, 8, None, 3,
    None, 2, None, None, None, 3, None, None, 1, None, None, 6, None, 6, None, None, None, None, None, None, None, None, None, None, 4, 1, 9, None, 8, None, 2, 8, None, None, None, 5,None, 7, 9]

boards = [board_1, board_2]
board = random.choice(boards)
