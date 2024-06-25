"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt1 = 0
    cnt2 = 0
    for i in board:
        for j in i:
            if j == X:
                cnt1 += 1
            elif j == O:
                cnt2 += 1
    if cnt1 == cnt2:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_list.append((i, j))
    return actions_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    turn = player(board)
    if len(action) != 2:
        raise ValueError("Invalid action")
    new_board[action[0]][action[1]] = turn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    def check_row(row):
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
        return None

    def check_col(temp_board, col):
        if temp_board[0][col] == temp_board[1][col] == temp_board[2][col] and temp_board[0][col] != EMPTY:
            return temp_board[0][col]
        return None

    check = check_row(board[0])
    if check is not None:
        return check
    check = check_row(board[1])
    if check is not None:
        return check
    check = check_row(board[2])
    if check is not None:
        return check
    check = check_col(board, 0)
    if check is not None:
        return check
    check = check_col(board, 1)
    if check is not None:
        return check
    check = check_col(board, 2)
    if check is not None:
        return check
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board),None
    turn = player(board)
    if turn == X:
        value,move=max_value(board)
    if turn == O:
        value,move=min_value(board)

    return value,move

def max_value(board):
    if terminal(board):
        return utility(board),None
    v=-math.inf
    best_move=None
    for i in actions(board):
        min_v,_=min_value(result(board,i))
        if min_v>v:
            v=min_v
            best_move=i

    return v,best_move


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    best_move = None
    for i in actions(board):
        max_v, _ = max_value(result(board, i))
        if max_v < v:
            v = max_v
            best_move = i

    return v, best_move

