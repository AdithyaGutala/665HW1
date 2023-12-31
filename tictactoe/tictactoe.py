import math

# Use these constants to fill in the game board
X = "X"
O = "O"
EMPTY = None
track_player = EMPTY

def start_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns which player (either X or O) who has the next turn on a board.

    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    """
    global track_player

    if track_player == EMPTY:
        print("Player: {}".format(track_player))
        track_player = X
    elif track_player == X:
        track_player = O
    else:
        track_player = X
    
    
    return track_player


def actions(board):
    """
    Returns the set of all possible actions (i, j) available on the board.

    The actions function should return a set of all the possible actions that can be taken on a given board.
    Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2)
    and j corresponds to the column of the move (also 0, 1, or 2).

    Possible moves are any cells on the board that do not already have an X or an O in them.

    Any return value is acceptable if a terminal board is provided as input.
    """
    
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
              actions.append((i,j))
    return actions


def succ(board, action):
    """
    Returns the board that results from making move (i, j) on the board, without modifying the original board.

    If `action` is not a valid action for the board, you  should raise an exception.

    The returned board state should be the board that would result from taking the original input board, and letting
    the player whose turn it is make their move at the cell indicated by the input action.

    Importantly, the original board should be left unmodified. This means that simply updating a cell in `board` itself
    is not a correct implementation of this function. You’ll likely want to make a deep copy of the board first before
    making any changes.
    """
    new_board = [row[:] for row in board]
    i , j = action
    
    if board[i][j] != EMPTY:
        raise CustomError("Cannot overwrite a filled in space")
    if track_player == X:
        print("Minimax X: {} : {}".format(i,j))
        new_board[i][j] = X
    else:
        print("Minimax O: {} : {}".format(i,j))
        new_board[i][j] = O
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.

    - If the X player has won the game, the function should return X.
    - If the O player has won the game, the function should return O.
    - If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the
      function should return None.

    You may assume that there will be at most one winner (that is, no board will ever have both players with
    three-in-a-row, since that would be an invalid board state).
    """
    winner = None
    game_over = False
    
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY:
           winner = board[i][0]
           break

    if winner != None:
        for j in range(3):
            if board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[0][j] != EMPTY:
                winner = board[0][j]
                break
    if winner != None:
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY: 
                winner = board[0][0]
    if winner != None:
        if board[2][0] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
            winner = board[2][0]    

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    If the game is over, either because someone has won the game or because all cells have been filled without anyone
    winning, the function should return True.

    Otherwise, the function should return False if the game is still in progress.
    """
    game_over = False
    
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY:
           game_over = True
           break

    for j in range(3):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[0][j] != EMPTY:
            game_over = True
            break
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY: 
            game_over = True
    if board[2][0] == board[1][1] == board[0][2] and board[2][0]:
            game_over = True

    if game_over == False:
        game_over = True
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    game_over = False
                    break
    
    return game_over


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    You may assume utility will only be called on a board if terminal(board) is True.
    """
    current_winner = winner(board)
    if current_winner:
        if current_winner == X:
            return 1
        else:
            return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board.

    If multiple moves are equally optimal, any of those moves is acceptable.

    If the board is a terminal board, the minimax function should return None.
    """
    action = None
    actions_list = []
    is_terminal = terminal(board)
    if not is_terminal:
      actions_list = actions(board)
    if len(actions_list):
          action = actions_list[0]

    return action
