# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 SPRING 2021
# INSTRUCTOR: Jonathan Hudson
# eIOv8k6dPgp2uLJI6O8v
# DO NOT EDIT THE ABOVE LINES OR BELOW LINES (TAs will use there own version of this file for grading)

from pprint import pprint
import traceback
import inspect
import sys
from copy import deepcopy
from CPSC217S21A3Board import *

# Constants to turn off tests for parts of assignment
TESTPART1 = True
TESTPART2 = True
TESTPART3 = True
TESTPART4 = True
TESTPART5 = True
TESTPART6 = True
TESTPART7 = True
STOP1STFAIL = True


def runTests():
    if not testCreateBoard():
        sys.exit(1)
    if not testPlay():
        sys.exit(1)
    if STOP1STFAIL and not testFull():
        sys.exit(1)
    if STOP1STFAIL and not testWinInRow():
        sys.exit(1)
    if STOP1STFAIL and not testWinInCol():
        sys.exit(1)
    if STOP1STFAIL and not testWinInDiag():
        sys.exit(1)
    if STOP1STFAIL and not testWon():
        sys.exit(1)
    if STOP1STFAIL and not testHint():
        sys.exit(1)


##############################################################################
#
# Code below is for testing student functions (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
#
##############################################################################

# Determine whether or not a function exists in the namespace at the time
# this function is called
# Parameters:
#   name: The name of the function to check the existence of
# Returns: True if the function exists, False otherwise
def functionExists(name):
    members = inspect.getmembers(sys.modules[__name__])
    for (n, m) in members:
        if n == name and inspect.isfunction(m):
            return True
    return False


# Run a series of tests on the createBoard function
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testCreateBoard():
    if not TESTPART1:
        return True

    print("Testing createBoard...")

    # Is the argument count correct
    if len(inspect.getfullargspec(createBoard).args) != 2:
        print("  createBoard should have 2 arguments!")
        print("Failed testCreateBoard!!!!!")
        return False

    # Are argument names correct
    if inspect.getfullargspec(createBoard).args is ['rows', 'cols']:
        print("  createBoard should have arguments 'rows','cols'!")
        print("Failed testCreateBoard!!!!!")
        return False

    try:
        createBoard(3, 3)
        print("  The createBoard(3,3) execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during createBoard(3,3).")
        print("Failed testCreateBoard!!!!!")
        return False

    try:
        createBoard()
        print("  The createBoard() execution (default 'rows' and 'cols') ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during createBoard().")
        print("createBoard() may not have defaults for 'rows' and 'cols' parameters")
        print("Failed testCreateBoard!!!!!")
        return False

    if type(createBoard()) != list:
        print("  createBoard attribute 'board' should be type list!")
        print("Failed testCreateBoard!!!!!")
        return False

    for (test_rows, test_cols) in [(3, 3), (3, 4), (4, 3), (4, 4), (3, 5), (5, 3), (4, 5), (5, 4), (5, 5)]:
        # Try and call the function
        try:
            print(f"  Attempting to examine 2d list made by Board({test_rows}, {test_cols})... ")
            test_board = createBoard(test_rows, test_cols)
        except Exception:
            print("An exception occurred during the attempt.")
            traceback.print_exc(file=sys.stdout)
            print("Failed testCreateBoard!!!!!")
            return False

        # Does it have the set the board field to a correct type?
        if type(test_board) is not list:
            print(f"    The value of board was a {type(test_board)} not a list.")
            print("Failed testCreateBoard!!!!!")
            return False

        # Does the list have the correct number of elements?
        if len(test_board) != test_rows:
            print(f"    The board had {len(test_board)} rows when {test_rows} were expected.\n")
            print("Failed testCreateBoard!!!!!")
            return False

        # Is each row a list?  Does each row have the correct length?
        for test_row in range(len(test_board)):
            if type(test_board[test_row]) is not list:
                print(f"    The row at index {test_row} is a {test_board[test_row]}, not a list.\n")
                print("Failed testCreateBoard!!!!!")
                return False
            if len(test_board[test_row]) != test_cols:
                print(
                    f"    The row at index {test_row} had {len(test_board[test_row])} elements when {test_cols} were expected.\n")
                print("Failed testCreateBoard!!!!!")
                return False

        # Is each row unique
        for test_row in range(len(test_board)):
            for test_col in range(len(test_board)):
                if test_row != test_col:
                    if test_board[test_row] is test_board[test_col]:
                        print(
                            f"    The row at index {test_row} is pointing to the same row as the row at index {test_col}.")
                        print("Failed testCreateBoard!!!!!")
                        return False

        # Is every space on the board populated with an integer value between
        # 0 and syms (not including syms)?
        for test_row in range(0, len(test_board)):
            for test_col in range(0, len(test_board[test_row])):
                if type(test_board[test_row][test_col]) is not int:
                    print(
                        f"    The value in row {test_row}, column {test_col} is a {type(test_board[test_row][test_col])}, not an integer")
                    print("Failed testCreateBoard!!!!!")
                    return False
                if test_board[test_row][test_col] != EMPTY:
                    print(
                        f"    The integer in row {test_row} column {test_col} is a {test_board[test_row][test_col]} which is not EMPTY==0")
                    print("Failed testCreateBoard!!!!!")
                    return False
    try:
        rowsIn([[]])
        print("  The rowsIn() method seems to exist...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("  The rowsIn() method doesn't seem to exist!!!!!")
        print("Failed testCreateBoard!!!!!")
        return False
    if type(rowsIn(createBoard(3, 4))) is not int or rowsIn(createBoard(3, 4)) != 3:
        print("  The rowsIn() method does not seem to be defined properly...")
        print("Failed testCreateBoard!!!!!")
        return False

    try:
        colsIn([[0]])
        print("  The colsIn() method seems to exist...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("  The colsIn() method doesn't seem to exist!!!!!")
        print("Failed testCreateBoard!!!!!")
        return False
    if type(colsIn(createBoard(3, 4))) is not int or colsIn(createBoard(3, 4)) != 4:
        print("  The colsIn() method does not seem to be defined properly...")
        print("Failed testCreateBoard!!!!!")
    print("Passed testCreateBoard.")
    print()
    return True


# Run a series of tests on the canPlay and play functions
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testPlay():
    if not TESTPART2:
        return True
    print("Testing play, canPlay...")
    # Does the play, canPlay function exist?
    if functionExists("canPlay"):
        print("  The method canPlay seems to exist...")
    else:
        print("  The canPlay method doesn't seem to exist...")
        print("Failed testPlay!!!!!")
        return False

    if functionExists("play"):
        print("  The method play seems to exist...")
    else:
        print("  The play method doesn't seem to exist...")
        print("Failed testPlay!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(canPlay).args) != 3:
        print("  canPlay should have 3 arguments!")
        print("Failed testPlay!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(play).args) != 4:
        print("  play should have 4 arguments!")
        print("Failed testPlay!!!!!")
        return False

    try:
        play(createBoard(3, 3), 0, 0, EMPTY)
        print("  The play(board, 0,0,EMPTY) method execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during play(board, 0,0,EMPTY).")
        print("Failed testPlay!!!!!")
        return False

    try:
        canPlay(createBoard(3, 3), 0, 0)
        print("  The canplay(board, 0,0) method execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during canplay(board, 0,0).")
        print("Failed testPlay!!!!!")
        return False

    for rows in [3, 4]:
        for cols in [3, 4]:
            test_board = createBoard(rows, cols)
            print("  The canPlay for all spots in empty board...")
            for row_row in range(rows):
                for test_col in range(cols):
                    canplay_result = canPlay(test_board, row_row, test_col)
                    # Check return type and value? Should be able to play everywhere.
                    if type(canplay_result) is not bool:
                        print(f"    The value returned was a {type(canplay_result)}, not a boolean.")
                        print("Failed testPlay!!!!!")
                        return False
                    if canplay_result is False:
                        print(
                            f"    The board {test_board} is empty but canPlay(board, {row_row}, {test_col}) was False.")
                        print("Failed testPlay!!!!!")
                        return False
                    test_board[row_row][test_col] = X
                    canplay_result = canPlay(test_board, row_row, test_col)
                    # Check return type and value? Should not be able to play here now.
                    if type(canplay_result) is not bool:
                        print(f"    The value returned was a {type(canplay_result)}, not a boolean.")
                        print("Failed testPlay!!!!!")
                        return False
                    if canplay_result is True:
                        print(
                            f"    The board {test_board} has piece at this spot but canPlay(board, {row_row}, {test_col}) was True.")
                        print("Failed testPlay!!!!!")
                        return False
                    test_board[row_row][test_col] = EMPTY
            copy = deepcopy(test_board)
            # Change a copy of the board and check if result of play, canPlay matches changes expected
            print(f"  Test play/canPlay before and after playing at every location in {rows}x{cols} empty board")
            for row_row in range(rows):
                for test_col in range(cols):
                    test_canplay_result0 = canPlay(test_board, row_row, test_col)
                    if test_canplay_result0 is False:
                        print(
                            f"   The board {test_board} is empty but canPlay(board, {row_row}, {test_col}) was False.")
                        print("Failed testPlay!!!!!")
                        return False
                    # Play an X. Should not be able to play in this spot now.
                    test_canplay_result1 = play(test_board, row_row, test_col, X)
                    if test_canplay_result1 is not None:
                        print(
                            f"    The value returned by play(board, {row_row}, {test_col}, {X}) was a {test_canplay_result1}, not None.")
                        print("Failed testPlay!!!!!")
                        return False
                    copy[row_row][test_col] = X
                    if copy != test_board:
                        print(
                            f"    The board {test_board} returned by play(board, {row_row}, {test_col}, {X}) was not {copy}")
                        print("Failed testPlay!!!!!")
                        return False
                    test_canplay_result2 = canPlay(test_board, row_row, test_col)
                    if test_canplay_result2 is True:
                        print(
                            f"   The board {test_board} is occupied but canPlay(board, {row_row}, {test_col}) was True.")
                        return True
                    # Play an EMPTY. Should be able to play in this spot now.
                    test_canplay_result3 = play(test_board, row_row, test_col, EMPTY)
                    if test_canplay_result3 is not None:
                        print(
                            f"    The value returned by play(board, {row_row}, {test_col}, {EMPTY}) was a {test_canplay_result3}, not None.")
                        print("Failed testPlay!!!!!")
                        return False
                    copy[row_row][test_col] = EMPTY
                    if copy != test_board:
                        print(
                            f"    The board {test_board} returned by play(board, {row_row}, {test_col}, {EMPTY}) was not {copy}")
                        print("Failed testPlay!!!!!")
                        return False
                    test_canplay_result4 = canPlay(test_board, row_row, test_col)
                    if test_canplay_result4 is False:
                        print(
                            f"   The board {test_board} is empty but canPlay(board, {row_row}, {test_col}) was False.")
                        print("Failed testPlay!!!!!")
                        return False
                    # Play an O. Should not be able to play in this spot now.
                    test_canplay_result5 = play(test_board, row_row, test_col, O)
                    if test_canplay_result5 is not None:
                        print(
                            f"    The value returned by play(board, {row_row}, {test_col}, {0}) was a {test_canplay_result5}, not None.")
                        print("Failed testPlay!!!!!")
                        return False
                    copy[row_row][test_col] = O
                    if copy != test_board:
                        print(
                            f"    The board {test_board} returned by play(board, row, col, 0) was not {copy}")
                        print("Failed testPlay!!!!!")
                        return False
                    test_canplay_result6 = canPlay(test_board, row_row, test_col)
                    if test_canplay_result6 is True:
                        print(
                            f"   The board {test_board} is occupied but canPlay(board, {row_row}, {test_col}) was True.")
                        return True
                    # Play an EMPTY. Should be able to play in this spot now.
                    test_canplay_result7 = play(test_board, row_row, test_col, EMPTY)
                    if test_canplay_result7 is not None:
                        print(
                            f"    The value returned by play(board, {row_row}, {test_col}, {EMPTY}) was a {test_canplay_result7}, not None.")
                        print("Failed testPlay!!!!!")
                        return False
                    copy[row_row][test_col] = EMPTY
                    if copy != test_board:
                        print(
                            f"    The board {test_board} returned by play(board, {row_row}, {test_col}, {EMPTY}) was not {copy}")
                        print("Failed testPlay!!!!!")
                        return False
                    test_canplay_result8 = canPlay(test_board, row_row, test_col)
                    if test_canplay_result8 is False:
                        print(
                            f"   The board {test_board} is empty but canPlay(board, {row_row}, {test_col}) was False.")
                        print("Failed testPlay!!!!!")
                        return False
    print("Passed testPlay.")
    print()
    return True


# Run a series of tests on the full functions
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def testFull():
    if not TESTPART3:
        return True

    print("Testing full...")

    # Does the full function exist?
    if functionExists("full"):
        print("  The method full seems to exist...")
    else:
        print("  The full method doesn't seem to exist...")
        print("Failed testFull!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(full).args) != 1:
        print("  play should have 1 argument!")
        print("Failed testFull!!!!!")
        return False

    try:
        full(createBoard(3, 3))
        print("  The full() method execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during full().")
        print("Failed testFull!!!!!")
        return False

    for rows in [3, 4]:
        for cols in [3, 4]:
            print(f"Testing full for a board of size {rows}x{cols}")
            test_board = createBoard(rows, cols)
            # Does full return right for empty board?
            print("  Testing call to full for empty board.")
            full_result = full(test_board)
            if type(full_result) is not bool:
                print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                print("Failed testFull!!!!!")
                return False
            if full_result:
                print(f"    The board {test_board} is empty but full returned True.")
                print("Failed testFull!!!!!")
                return False
            for row in range(rows):
                for col in range(cols):
                    test_board[row][col] = X
            full_result = full(test_board)
            # Does full return right for full board?
            print("  Testing call to full for board full of Xs.")
            if type(full_result) is not bool:
                print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                print("Failed testFull!!!!!")
                return False
            if not full_result:
                print(f"    The board {test_board} is full but full returned False.")
                print("Failed testFull!!!!!")
                return False
            # Does full return right if we selectively remove single piece from anywhere on board?
            print("  Testing full for almost full board of Xs with one EMPTY spot")
            for row in range(rows):
                for col in range(cols):
                    test_board[row][col] = EMPTY
                    full_result = full(test_board)
                    if type(full_result) is not bool:
                        print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                        print("Failed testFull!!!!!")
                        return False
                    if full_result:
                        print(f"    The board {test_board} is not full returned True.")
                        print("Failed testFull!!!!!")
                        return False
                    test_board[row][col] = X
            for row in range(rows):
                for col in range(cols):
                    test_board[row][col] = O
            full_result = full(test_board)
            # Does full return right for full board?
            print("  Testing call to full for board full of Os.")
            if type(full_result) is not bool:
                print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                print("Failed testFull!!!!!")
                return False
            if not full_result:
                print(f"    The board {test_board} is full but full returned False.")
                print("Failed testFull!!!!!")
                return False
            # Does full return right if we selectively remove single piece from anywhere on board?
            print("  Testing full for almost full board of Os with one EMPTY spot")
            for row in range(rows):
                for col in range(cols):
                    test_board[row][col] = EMPTY
                    full_result = full(test_board)
                    if type(full_result) is not bool:
                        print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                        print("Failed testFull!!!!!")
                        return False
                    if full_result:
                        print(f"    The board {test_board} is not full returned True.")
                        print("Failed testFull!!!!!")
                        return False
                    test_board[row][col] = O
    print("testFull Passed..")
    print()
    return True


#
# Run a series of tests on the winInRow function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInRow():
    if not TESTPART4:
        return True
    print("Testing winInRow...")

    # Does the winInRow function exist?
    if functionExists("winInRow"):
        print("  The function winInRow seems to exist...")
    else:
        print("  The winInRow function doesn't seem to exist...\n")
        print("Failed testWinInRow!!!!!")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(winInRow).args) != 3:
        print("  winInRow should have 3 arguments!")
        print("Failed testWinInRow!!!!!")
        return False

    try:
        winInRow(createBoard(3, 3), 0, X)
        print("  The winInRow() method execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during winInRow().")
        print("Failed testWinInRow!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_row, test_piece, test_exp_result) in [
        # Board sizes with wins
        ([[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]], 0, 1, True),
        ([[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]], 0, 1, True),
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        # Win in other rows
        ([[0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 1, True),
        ([[0, 0, 0, 0],
          [0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 1, True),
        ([[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]], 2, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 1],
          [0, 0, 0, 0]], 2, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0]], 2, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0]], 3, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 1]], 3, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 1]], 3, 1, True),
        # Win with other piece type
        ([[0, 0, 0, 0],
          [2, 2, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, True),
        ([[0, 0, 0, 0],
          [2, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, True),
        # Win has other type around
        ([[1, 1, 1, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[2, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        # Win isn't with asked about piece type
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 2, False),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 2, False),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 2, False),
        ([[2, 2, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[2, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        # Win broken by non empty
        ([[1, 1, 2, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[1, 2, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 1]], 0, 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1]], 0, 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 1, 1]], 0, 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 0, 1, False)]:

        # Attempt the function call
        try:
            for loop_row in range(len(test_board)):
                attempt += 1
                wininrow_result = winInRow(test_board, loop_row, test_piece)
                # Does it have the correct return type?
                if type(wininrow_result) is not bool:
                    print(f"  Attempting to use winInRow Test {attempt}")
                    print("The board was:")
                    pprint(test_board)
                    print(f"FAILED: For row = {loop_row} piece = {test_piece}")
                    print(f"FAILED: The value returned was a {type(wininrow_result)}, not a Boolean.")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                if test_exp_result and not wininrow_result and test_row == loop_row:
                    print(f"  Attempting to use winInRow Test {attempt}")
                    print("The board was:")
                    pprint(test_board)
                    print(f"FAILED: For row = {loop_row} piece = {test_piece}")
                    print(f"FAILED: The value returned was {wininrow_result} when {test_exp_result} was expected.")
                    print(f"FAILED: winInRow should say True to winInRow {loop_row} but said False.")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif test_exp_result and wininrow_result and test_row != loop_row:
                    print(f"  Attempting to use winInRow Test {attempt}")
                    print("The board was:")
                    pprint(test_board)
                    print(f"FAILED: For row = {loop_row} piece = {test_piece}")
                    print(f"FAILED: The value returned was {wininrow_result} when {test_exp_result} was expected.")
                    print(f"FAILED: winInRow should say True to winInRow but for {test_row} and not {loop_row}.")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                elif not test_exp_result and wininrow_result:
                    print(f"  Attempting to use winInRow Test {attempt}")
                    print("The board was:")
                    pprint(test_board)
                    print(f"FAILED: For row = {loop_row} piece = {test_piece}")
                    print(f"FAILED: The value returned was {wininrow_result} when {test_exp_result} was expected.")
                    print(f"FAILED: winInRow should not returning True.")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                passed += 1
        except Exception:
            traceback.print_exc(file=sys.stdout)
            print(f"  Attempting to use winInRow Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board)
            print()
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"testWinInRow Failed {failed} test cases of {attempt}")
    else:
        print(f"testWinInRow Passed all tests. <{attempt}>")

    print()
    return True


#
# Run a series of tests on the winInCol function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInCol():
    if not TESTPART4:
        return True
    print("Testing winInCol...")

    # Does the winInCol function exist?
    if functionExists("winInCol"):
        print("  The function winInCol seems to exist...")
    else:
        print("  The winInCol function doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(winInCol).args) != 3:
        print("  winInCol should have 3 arguments!")
        print("Failed testWinInCol!!!!!")
        return False

    try:
        winInCol(createBoard(3, 3), 0, X)
        print("  The winInCol() method execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during winInCol().")
        print("Failed testWinInCol!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_col, test_piece, test_exp_result) in [
        ([[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]], 0, 1, True),
        ([[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [0, 0, 0]], 0, 1, True),
        ([[0, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]], 0, 1, True),
        ([[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]], 0, 1, True),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, True),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, True),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, True),
        # Win in other rows
        ([[0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 1, 1, True),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0]], 1, 1, True),
        ([[0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0]], 1, 1, True),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 2, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 2, 1, True),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 2, 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0]], 3, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 3, 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 3, 1, True),
        # Win with other piece type
        ([[0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0]], 1, 2, True),
        ([[0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0]], 1, 2, True),
        # Win has other type around
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [2, 0, 0, 0]], 0, 1, True),
        ([[2, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, True),
        # Win isn't with asked about piece type
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]], 0, 2, False),
        ([[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 2, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 2, False),
        ([[2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0]], 0, 1, False),
        ([[2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0]], 0, 1, False),
        # Win broken by non empty
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [2, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 0],
          [2, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 0, 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 0, 1, False)]:

        # Attempt the function call
        try:
            for loop_col in range(len(test_board[0])):
                attempt += 1
                winincol_result = winInCol(test_board, loop_col, test_piece)
                # Does it have the correct return type?
                if type(winincol_result) is not bool:
                    print(f"  Attempting to use winInCol Test {attempt}")
                    print("The board was:")
                    pprint(test_board)
                    print(f"FAILED: For row = {loop_col} piece = {test_piece}")
                    print(f"FAILED: The value returned was a {type(winincol_result)}, not a Boolean.")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif test_exp_result and not winincol_result and test_col == loop_col:
                    print(f"  Attempting to use winInCol Test {attempt}")
                    print("The board was:")
                    pprint(test_board)
                    print(f"FAILED: For row = {loop_col} piece = {test_piece}")
                    print(f"FAILED: The value returned was {winincol_result} when {test_exp_result} was expected.")
                    print(f"FAILED: winInCol should say True to winInCol {loop_col} but said False.")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif test_exp_result and winincol_result and test_col != loop_col:
                    print(f"  Attempting to use winInCol Test {attempt}")
                    print("The board was:")
                    pprint(test_board)
                    print(f"FAILED: For row = {loop_col} piece = {test_piece}")
                    print(f"FAILED: The value returned was {winincol_result} when {test_exp_result} was expected.")
                    print(f"FAILED: winInCol should say True to winInCol but for {test_col} and not {loop_col}.")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                elif not test_exp_result and winincol_result:
                    print(f"  Attempting to use winInCol Test {attempt}")
                    print("The board was:")
                    pprint(test_board)
                    print(f"FAILED: For row = {loop_col} piece = {test_piece}")
                    print(f"FAILED: The value returned was {winincol_result} when {test_exp_result} was expected.")
                    print(f"FAILED: winInCol should not returning True.")
                    failed += 1
                    if STOP1STFAIL:
                        return
                    else:
                        continue
                passed += 1
        except Exception:
            print(f"  Attempting to use winInCol Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board)
            print()
            traceback.print_exc(file=sys.stdout)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"testWinInCol Failed {failed} test cases of {attempt}")
    else:
        print(f"testWinInCol Passed all tests. <{attempt}>")
    print()
    return True


#
# Run a series of tests on the winInDiag function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWinInDiag():
    if not TESTPART5:
        return True
    print("Testing winInDiag...")

    # Does the winInDiag function exist?
    if functionExists("winInDiag"):
        print("  The function winInDiag seems to exist...")
    else:
        print("  The winInDiag function doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(winInDiag).args) != 2:
        print("  winInDiag should have 2 arguments!")
        print("Failed testWinInDiag!!!!!")
        return False

    try:
        winInDiag(createBoard(3, 3), X)
        print("  The winInDiag() method execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during winInDiag().")
        print("Failed testWinInDiag!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_piece, test_exp_result) in [
        # win in different board sizes
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 1, True),
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1],
          [0, 0, 0]], 1, True),
        ([[0, 0, 0],
          [1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 1, True),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0]], 1, True),
        ([[0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, True),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, True),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, True),
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 1, True),
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0],
          [0, 0, 0]], 1, True),
        ([[0, 0, 0],
          [0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 1, True),
        ([[0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0]], 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, True),
        # Win with other piece type
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, True),
        # Win has other type around
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [1, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 1],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, True),
        # Win isn't with asked about piece type
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 2, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 2, False),
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 1, False),
        # Win broken by non empty
        ([[1, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 2, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 2, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 1, False),
        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 2, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 1, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 2, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 1, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 2, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 1, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 2, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 2, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 2, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 2, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 2, False)]:

        # Attempt the function call
        try:
            attempt += 1
            winindiag_result = winInDiag(test_board, test_piece)
            # Does it have the correct return type?
            if type(winindiag_result) is not bool:
                print(f"  Attempting to use winInDiag Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was a {type(winindiag_result)}, not a Boolean.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            if test_exp_result and not winindiag_result:
                print(f"  Attempting to use winInDiag Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {winindiag_result} when {test_exp_result} was expected.")
                print(f"FAILED: winInDiag should've returned True.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not test_exp_result and winindiag_result:
                print(f"  Attempting to use winInDiag Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {winindiag_result} when {test_exp_result} was expected.")
                print(f"FAILED: winInDiag should've returned False.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception:
            print(f"  Attempting to use winInDiag Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board)
            print()
            traceback.print_exc(file=sys.stdout)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"testWinInDiag Failed {failed} test cases of {attempt}")
    else:
        print(f"testWinInDiag Passed all tests. <{attempt}>")
    print()
    return True


#
# Run a series of tests on the won function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testWon():
    if not TESTPART6:
        return True
    print("Testing won...")

    # Does the won function exist?
    if functionExists("won"):
        print("  The function won seems to exist...")
    else:
        print("  The won won doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(won).args) != 2:
        print("  won should have 2 arguments!")
        print("Failed testWon!!!!!")
        return False

    try:
        won(createBoard(3, 3), X)
        print("  The won() method execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during won().")
        print("Failed testWon!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_piece, test_exp_result) in [
        ([[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]], 1, True),
        ([[0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]], 1, True),
        ([[0, 0, 0],
          [0, 0, 0],
          [1, 1, 1]], 1, True),
        ([[2, 2, 2],
          [0, 0, 0],
          [0, 0, 0]], 2, True),
        ([[0, 0, 0],
          [2, 2, 2],
          [0, 0, 0]], 2, True),
        ([[0, 0, 0],
          [0, 0, 0],
          [2, 2, 2]], 2, True),
        ([[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]], 2, False),
        ([[0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]], 2, False),
        ([[0, 0, 0],
          [0, 0, 0],
          [1, 1, 1]], 2, False),
        ([[2, 2, 2],
          [0, 0, 0],
          [0, 0, 0]], 1, False),
        ([[0, 0, 0],
          [2, 2, 2],
          [0, 0, 0]], 1, False),
        ([[0, 0, 0],
          [0, 0, 0],
          [2, 2, 2]], 1, False),
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 1, True),
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 1, True),
        ([[2, 0, 0],
          [0, 2, 0],
          [0, 0, 2]], 2, True),
        ([[0, 0, 2],
          [0, 2, 0],
          [2, 0, 0]], 2, True),
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 2, False),
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 2, False),
        ([[2, 0, 0],
          [0, 2, 0],
          [0, 0, 2]], 1, False),
        ([[0, 0, 2],
          [0, 2, 0],
          [2, 0, 0]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 2, False),
        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 1, False),
        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 2, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 1, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 2, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 1, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 2, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 1, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 2, False),
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [2, 2, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 1],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 2, 2, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 2, 2]], 2, True),
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [2, 2, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 1],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 2, 2, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 2, 2]], 1, False),
        ([[1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 1]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 1, 1]], 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, True),
        ([[0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0]], 2, True),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 1, True),
        ([[0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 2]], 2, True),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 2, False),
        ([[0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0]], 1, False),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 2, False),
        ([[0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 2]], 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, True),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0]], 2, True),
        ([[0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, True),
        ([[0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0]], 2, True),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 2, False),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0]], 1, False),
        ([[0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 2, False),
        ([[0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 2, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 2, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 2, False)]:

        # Attempt the function call
        try:
            attempt += 1
            won_result = won(test_board, test_piece)
            # Does it have the correct return type?
            if type(won_result) is not bool:
                print(f"  Attempting to use won Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was a {type(won_result)}, not a Boolean.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue

            # Did it return the correct value
            if test_exp_result and not won_result:
                print(f"  Attempting to use won Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {won_result} when {test_exp_result} was expected.")
                print(f"FAILED: won should've returned True.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not test_exp_result and won_result:
                print(f"  Attempting to use won Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {won_result} when {test_exp_result} was expected.")
                print(f"FAILED: won should've returned False.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception:
            print(f"  Attempting to use won Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board)
            print()
            traceback.print_exc(file=sys.stdout)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"testWon Failed {failed} test cases of {attempt}")
    else:
        print(f"testWon Passed all tests. <{attempt}>")
    print()
    return True


#
# Run a series of tests on the hint function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def testHint():
    if not TESTPART7:
        return True
    print("Testing hint...")

    # Does the hint function exist?
    if functionExists("hint"):
        print("  The function hint seems to exist...")
    else:
        print("  The winInDiag hint doesn't seem to exist...\n")
        return

    # Is the argument count correct
    if len(inspect.getfullargspec(hint).args) != 2:
        print("  hint should have 2 arguments!")
        print("Failed testHint!!!!!")
        return False

    try:
        hint(createBoard(3, 3), X)
        print("  The hint() method execution ran without exception...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("An exception occurred during hint().")
        print("Failed testHint!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_piece, test_row, test_col) in [
        ([[1, 1, 0],
          [0, 0, 0],
          [0, 0, 0]], 1, 0, 2),
        ([[1, 1, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]], 1, 0, 2),
        ([[1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 2),
        ([[1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 2),
        ([[0, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 1),
        ([[0, 0, 0, 0],
          [2, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, 1, 1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, 1, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 0]], 1, 2, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 0]], 1, 2, 1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 0, 2, 0]], 2, 3, 1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 2]], 2, 3, 2),
        ([[1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [2, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 0, 2, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 2]], 1, -1, -1),
        ([[1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 2),
        ([[1, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[1, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 1]], 1, 3, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 1, 1]], 1, 3, 1),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, 0),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, 1, 0),
        ([[0, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, 1, 1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 0]], 2, 2, 1),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 1, 1, 2),
        ([[0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 2, 1, 3),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 2]], 2, 2, 3),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 2, -1, -1),
        ([[0, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 0]], 1, -1, -1),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 2, -1, -1),
        ([[0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 2]], 1, -1, -1),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, 2, 0),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, -1, -1),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, 1, 0),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, 2, 3),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, -1, -1),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 1, 1, 3),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, 1, 2),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, 2, 2),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, 1, 2),
        ([[0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, 2, 3),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 2, 0, 2),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, 3, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0]], 2, 1, 3),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 2, -1, -1),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 2, -1, -1),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 2, -1, -1),
        ([[0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0]], 1, -1, -1)

    ]:

        # Attempt the function call
        try:
            attempt += 1
            row_result, col_result = hint(deepcopy(test_board), test_piece)
            # Does it have the correct return type?
            if type(row_result) is not int:
                print(f"  Attempting to use hint Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(f"FAILED: The row value returned was a {type(row_result)}, not a Integer.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            if type(col_result) is not int:
                print(f"  Attempting to use hint Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(f"FAILED: The col value returned was a {type(col_result)}, not a Integer.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            if test_row != row_result or test_col != col_result:
                print(f"  Attempting to use hint Test {attempt}")
                print("The board was:")
                pprint(test_board)
                print(
                    f"FAILED: The value returned was {row_result},{col_result} for piece = {test_piece} when {test_row},{test_col} was expected.")
                failed += 1
                if STOP1STFAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception:
            print(f"  Attempting to use hint Test {attempt}")
            print("The board was:")
            pprint(test_board)
            print("FAILED: An exception occurred during the attempt.")
            traceback.print_exc(file=sys.stdout)
            failed += 1
            if STOP1STFAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"testHint Failed {failed} test cases of {attempt}")
    else:
        print(f"testHint Passed all tests. <{attempt}>")
    print()
    return True


if __name__ == "__main__":
    runTests()
