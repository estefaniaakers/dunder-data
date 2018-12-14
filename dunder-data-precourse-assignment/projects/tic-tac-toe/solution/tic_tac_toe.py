'''
This Python module builds a tic-tac-toe game.
There function `tic_tac_toe` plays the game and defined at the bottom.
The other functions do exactly one task. Notice they are only a few lines of code.
The `tic_tac_toe` function calls each one of these other functions
The actual game is played in the `tic_tac_toe_games.py` file
'''

def create_empty_board():
    board = [[' ', ' ', ' '], 
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board

def verify_rc(val, name):
    if val not in range(3):
        raise ValueError(f'{name} out of range')

def verify_mark(mark):
    if mark not in ['x', 'o']:
        raise ValueError('mark must be x or o')

def verify_position_open(board, row, col):
    if board[row][col] != ' ':
        raise ValueError('Position taken!')

def get_round_num(board):
    round_num = 0
    for row in board:
        for mark in row:
            round_num += mark != ' '
    return round_num

def output_board(board, round_num):
    print(f'\nRound: {round_num}')
    for row in board:
        print(row)

def is_row_winner(board, mark):
    winner_str = mark * 3
    for row in board:
        if ''.join(row) == winner_str:
            return True
    return False

def is_col_winner(board, mark):
    winner_str = mark * 3
    for i in range(3):
        marks = ''
        for j in range(3):
            marks += board[j][i]
        if marks == winner_str:
            return True
    return False

def is_diag_winner(board, mark):
    winner_str = mark * 3
    diag1, diag2 = '', ''
    for i in range(3):
        diag1 += board[i][i]
        diag2 += board[i][2 - i]
    return  winner_str in [diag1, diag2]
        
def tic_tac_toe(board, mark, row, col):
    # verify row and col are in possible range (0, 1, 2)
    verify_rc(row, 'row')
    verify_rc(col, 'col')

    # verify mark is either x or o
    verify_mark(mark)

    # verify board position is open
    verify_position_open(board, row, col)

    # set mark
    board[row][col] = mark

    # get round number
    round_num = get_round_num(board)

    # output board to screen
    output_board(board, round_num)

    # check if there is a winner
    if is_row_winner(board, mark) or \
       is_col_winner(board, mark) or \
       is_diag_winner(board, mark):
        print(f'Winner is {mark}!')

    # check if all rounds have been played
    elif round_num == 9:
        print('Cats game!')
