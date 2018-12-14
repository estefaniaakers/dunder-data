'''
This file plays several games of tic-tac-toe
Run it from the command line with `$python tic_tac_toe_games.py <game num>`
Where <game num> is an integer corresponding to the game number below
To play game 3 you would run: `$python tic_tac_toe_games.py 3`

You may add any number of games by defining them as a function.
This program uses the `inspect` module to determine how many game functions
there are.
'''

import sys
import inspect
from tic_tac_toe import tic_tac_toe, create_empty_board

# create an empty board
board = create_empty_board()

def game1():
    # Play Game #1
    tic_tac_toe(board, 'x', 1, 1)
    tic_tac_toe(board, 'o', 2, 0)

    tic_tac_toe(board, 'x', 0, 0)
    tic_tac_toe(board, 'o', 1, 0)

    tic_tac_toe(board, 'x', 2, 2) # x wins diagonally

def game2():
    ## Play Game #2
    tic_tac_toe(board, 'x', 1, 1)
    tic_tac_toe(board, 'o', 2, 0)

    tic_tac_toe(board, 'x', 0, 0)
    tic_tac_toe(board, 'o', 1, 0)

    tic_tac_toe(board, 'x', 2, 1)
    tic_tac_toe(board, 'o', 0, 1)

    tic_tac_toe(board, 'x', 1, 2)
    tic_tac_toe(board, 'o', 2, 2)

    tic_tac_toe(board, 'x', 0, 2) # cats game

def game3():
    ## Play Game #3
    board = create_empty_board()

    tic_tac_toe(board, 'x', 1, 1)
    tic_tac_toe(board, 'o', 2, 0)

    tic_tac_toe(board, 'x', 0, 0)
    tic_tac_toe(board, 'o', 2, 1)

    tic_tac_toe(board, 'x', 0, 1)
    tic_tac_toe(board, 'o', 2, 2) # o wins horizontally

def game4():
    ## Play Game #4
    board = create_empty_board()

    tic_tac_toe(board, 'x', 1, 1)
    tic_tac_toe(board, 'o', 2, 0)

    tic_tac_toe(board, 'x', 0, 1)
    tic_tac_toe(board, 'o', 2, 2)

    tic_tac_toe(board, 'x', 2, 1) # x wins vertically

def get_game_funcs():
    var_dict = globals()
    game_func_names = {}
    for name, obj in var_dict.items():
        if inspect.isfunction(obj) and name[:4] == 'game' and obj.__module__ == __name__:
            game_func_names[name] = obj
    return game_func_names

if __name__ == '__main__':
    if len(sys.argv) == 0:
        raise ValueError('You must pass a single command line integer as an argument '
                         'in the command line to choose the game number')
    game_num_str = sys.argv[1]

    if not game_num_str.isdigit():
        raise ValueError('Argument passed must be an integer')

    func_names = get_game_funcs()
    num_games = len(func_names)

    if int(game_num_str) < 1 or int(game_num_str) > num_games:
        raise ValueError(f'Choose a game number between 1 and {num_games}.')

    func_name = 'game' + game_num_str
    func_names[func_name]()
    