# numbers array used for user input
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# board containing the player's boats and computer's shots
playerBoard = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

# computer board that shows where the player has shot
computerBoard = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

# other computer board that isn't shown to the player
hiddenBoard = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]


def coordsToString(top, left):
    """Creates a string of coordinates to use to track places the computer has shot"""
    return str(top) + str(left)


def stringToCoords(string):
    """does the opposite of coordsToString"""
    if len(string) != 2:
        raise IndexError("string parameter doesn't have expected length")
    return int(string[0]), int(string[1])


def onBoard(top, left=0):
    """Simplifies a lot of logic to tell if the coords are within the board"""
    return 0 <= top <= 9 and 0 <= left <= 9


def printBoard(inputBoard, player=True):
    """Outputs the board specified"""
    if player:
        print("      YOUR BOATS")
    else:
        print("      ENEMY BOATS")
    print("   1 2 3 4 5 6 7 8 9 10")
    print("1  " + " ".join(inputBoard[0]))
    print("2  " + " ".join(inputBoard[1]))
    print("3  " + " ".join(inputBoard[2]))
    print("4  " + " ".join(inputBoard[3]))
    print("5  " + " ".join(inputBoard[4]))
    print("6  " + " ".join(inputBoard[5]))
    print("7  " + " ".join(inputBoard[6]))
    print("8  " + " ".join(inputBoard[7]))
    print("9  " + " ".join(inputBoard[8]))
    print("10 " + " ".join(inputBoard[9]))
