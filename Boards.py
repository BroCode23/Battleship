eshots = []  # Array of all enemy shots, listed in the form of "(top)(left)"
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

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


def gameOutput(message, player=True):
    """if player variable is set, output message"""
    if player:
        print(message)


def coordString(coords):
    """Creates a string of coordinates to use to track places the computer has shot"""
    if len(coords) == 2:
        return str(coords[0]) + str(coords[1])
    else:
        raise TypeError(
            'Unexpected coordinate length in coordString() function')


def onBoard(coords):
    """Simplifies a lot of logic to tell if the coords are within the board"""
    if len(coords) == 1:
        return 0 <= coords[0] <= 9
    elif len(coords) == 2:
        return 0 <= coords[0] <= 9 and 0 <= coords[1] <= 9
    else:
        raise IndexError('used more than 2 arguments for onBoard() function')


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
