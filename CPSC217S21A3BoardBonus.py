# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 SPRING 2021
# INSTRUCTOR: Jonathan Hudson
# RNkY9dhladt8yUgc1WHi
# DO NOT EDIT THE ABOVE LINES
# Christina He
# UCID: 30168171

# INFORMATION FOR YOUR TA

# Constants for piece types
EMPTY = 0
X = 1
O = 2


#
#  Insert your implementation of createBoard here (code and comments (in-line and function))
# Create a board using list comprehension
# parameters: integer number of rows and columns
# returns the board in 2D list format
def createBoard(rows=3, columns=3):
    board = [[EMPTY for c in range(columns)] for r in range(rows)]
    return board


# Find the number of rows in board by counting number of sub-lists in list
# parameter: 2D list of board
# returns the number of rows in integer
def  rowsIn(board):
    return len(board)


# Find the number of columns in board by counting number of elements in a sub-list
# parameter: 2D list of board
# returns the number of columns in integer
def colsIn(board):
    return len(board[0])


# Check to see if the spot is occupied. 
# parameters: board in the format of 2D list, specific row and column in integer
# returns a boolean value to determine whether the spot is occupied
def canPlay(board, row, column):
    if board[row][column] == EMPTY:
        return True
    return False


#  Place the piece onto the specific location
# parameters: board with a format of 2D list, row and column to place the piece in integer, piece type in strings
# no return value
def play(board, row, column, piece):
    board[row][column] = piece


# looping through all rows and columns to check if any spot open.
# parameter: board in the format of 2D list
# returns a boolean value to see if there is any open spot on the board
def full(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == EMPTY:
                return False
    return True


# Looping through the board to check if there are enough consecutive pieces in a row.
# parameters: board in the format of 2D list, row to check in integer, piece type in strings, number of pieces in a row to win
# returns a boolean value to indicate whether a player wins in the row
def winInRow(board, row, piece,pieces_to_win):
    inRow = board[row]
    win = 0
    for y in range(len(board[0])-(pieces_to_win - 1)):
        for x in range(pieces_to_win):
            if inRow[y+x] == piece:
                win += 1
            else:
                win = 0

        if win == pieces_to_win:
            return True
    return False


# Looping through the board to check if there are enough consecutive pieces in a column.
# parameters: board in the format of 2D list, column to check in integer, piece type in strings, number of pieces in a row to win
# returns a boolean value to indicate if a player wins in the column
def winInCol(board, column, piece,pieces_to_win):
    for y in range(len(board)-(pieces_to_win - 1)):
        win = 0
        for x in range(pieces_to_win):
            if board[y+x][column] == piece:
                win += 1
            else:
                win = 0
        if win == pieces_to_win:
            return True
    return False



# Looping through the board to check if there are enough consecutive pieces in a diagonal.
# Combination of winInRow and winInCol
# Needs to check both the forward slash and back slash
# parameters: board in the format of 2D list, piece type in the format of strings, number of pieces in a row to win
# returns a boolean value to check if a player wins in the diagonal
def winInDiag(board, piece,pieces_to_win):
    # winF is the counter to count pieces_to_win of consecutive pieces in a diagonal from left to right
    # winF is the counter to count pieces_to_win of consecutive pieces in a diagonal from right to left
    winF = 0
    winB = 0
    for y in range(len(board[0])-(pieces_to_win - 1)):
        for x in range(len(board)-(pieces_to_win - 1)):
            for z in range(pieces_to_win):
                if board[x+z][y+z] is piece:
                    winF += 1
                else:
                    winF = 0

                if board[x+z][len(board[0])-(y+z)-1] is piece:
                    winB += 1
                else:
                    winB = 0

                if winB == pieces_to_win or winF == pieces_to_win:
                    return True
    return False


#  Check if any player won by looping through columns and rows and calling check functions
# parameters: board in the format of 2D list, piece in the format of strings, number of pieces in a row to win
# returns a boolean value to check if the player has won.
def won(board, piece,pieces_to_win):
    if pieces_to_win <= len(board[0]):
        for row in range(len(board)):
            if winInRow(board, row, piece,pieces_to_win) is True:
                return True
    if pieces_to_win <= len(board):
        for col in range(len(board[0])):
            if winInCol(board, col, piece,pieces_to_win) is True:
                return True
    if pieces_to_win <= len(board) and pieces_to_win <= len(board[0]):
        if winInDiag(board, piece,pieces_to_win) is True:
            return True
    return False


#
#  Try all the possibilities to check how to win
# parameters: board in the format of 2D list, piece type in strings, number of pieces in a row to win
# returns the coordinates of possible winning position
def hint(board, piece,pieces_to_win):
    EMPTY = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if canPlay(board, row, col):
                play(board, row, col, piece)
                if won(board, piece,pieces_to_win):
                    board[row][col] = EMPTY
                    return row, col
                else:
                    board[row][col] = EMPTY
    return -1, -1

# Newly added parameter: number of pieces in a row to win
def gameover(board, pieces_to_win):
    """
    This function determines if the game is complete due to a win or tie by either player
    :param board: The 2D list board to check
    :return: True if game is complete, False otherwise
    """
    if full(board) or won(board, X, pieces_to_win) or won(board, O, pieces_to_win):
        return True
    return False
