def reset_board(board):
    for x in range(3):
        for y in range(3):
            board[x][y] = ' '


opponent = 'x'
player = 'o'


def check_current_state(board):
    '''
    Verifies the state of the game.
    :param board: matrix
    :return: 10 if the player(AI) won, -10 if the opponent won , 0 if the game didn't reach its end.
    '''

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10

    for it in range(3):
        if board[it][0] == board[it][1] == board[it][2]:
            if board[it][0] == player:
                return 10
            elif board[it][0] == opponent:
                return -10
        if board[0][it] == board[1][it] == board[2][it]:
            if board[0][it] == player:
                return 10
            elif board[0][it] == opponent:
                return -10

    return 0


def minmax_algorithm(board, depth, minimizer_maximizer):
    '''
    Checks every combination from the current state of the game.
    :param minimizer_maximizer: bool
    :param board: matrix
    :param depth: int
    :return: best move score
    '''
    score = check_current_state(board)

    if score == 10 or score == -10:
        return score

    if not check_moves_left(board):
        return 0

    if minimizer_maximizer:
        # maximizer turn
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    best = max(best, minmax_algorithm(board, depth + 1, not minimizer_maximizer))
                    board[i][j] = ' '

        return best
    else:
        # minimizer turn
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = opponent
                    best = min(best, minmax_algorithm(board, depth + 1, not minimizer_maximizer))
                    board[i][j] = " "

        return best


def find_best_move(board):
    '''
    Together with the minmax algorithm determines the score returned by every other state of the game and determines the best one, returning the position in board.
    :param board: matrix
    :return: best_move[tuple]
    '''
    best_value = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player

                value = minmax_algorithm(board, 0, False)

                board[i][j] = ' '

                if value > best_value:
                    best_move = (i, j)
                    best_value = value

    return best_move


def check_moves_left(board):
    '''
    Verifies in the matrix board if there are any moves left to be done
    :param board: matrix
    :return: True if there are moves left in the board, False otherwise.
    '''
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    return False
