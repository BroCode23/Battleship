from random import randint
eshots = []  # array of all enemy shots, listed in the form of "(top)(left)"
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


def coordString(coords):
    if len(coords) == 2:
        return str(coords[0]) + str(coords[1])
    else:
        raise TypeError(
            'Unexpected coordinate length in coordString() function')


def onBoard(coords):
    """simplifies a lot of logic to tell if the coords are within the board"""
    if len(coords) == 1:
        return 0 <= coords[0] <= 9
    elif len(coords) == 2:
        return 0 <= coords[0] <= 9 and 0 <= coords[1] <= 9
    else:
        raise IndexError('used more than 2 arguments for onBoard() function')


def printBoard(input_board, player=True):
    """Outputs the board specified"""
    if player:
        print("      YOUR BOATS")
    else:
        print("      ENEMY BOATS")
    print("   1 2 3 4 5 6 7 8 9 10")
    print("1  " + " ".join(input_board[0]))
    print("2  " + " ".join(input_board[1]))
    print("3  " + " ".join(input_board[2]))
    print("4  " + " ".join(input_board[3]))
    print("5  " + " ".join(input_board[4]))
    print("6  " + " ".join(input_board[5]))
    print("7  " + " ".join(input_board[6]))
    print("8  " + " ".join(input_board[7]))
    print("9  " + " ".join(input_board[8]))
    print("10 " + " ".join(input_board[9]))


def getVerticalOrHorizontal(player):
    """return true if vertical, false if horizontal"""
    if player:
        choice = ""
        while not (choice == "v" or choice == "h"):  # input loop
            choice = input("Orientation? (v/h)")
            if not choice:
                continue
            choice = choice[0].lower()
        if choice == "v":
            vertical = True
        elif choice == "h":
            vertical = False
        return vertical
    else:
        return randint(0, 1)


def getBoatPlacementCoords(player, vertical, boatLength):
    """gets the coordinates for the given boat for placement"""
    top = -1
    left = -1
    if vertical:
        if player:
            # positions boat placement from top
            while not 0 <= top <= (10 - boatLength):
                while top not in numbers:
                    top = input("Space from top?")
                top = int(top)
            while not 0 <= left <= 9:  # positioning from left
                while left not in numbers:
                    left = input("Space from left?")
                left = int(left)
        else:
            top = randint(0, (9 - boatLength))
            left = randint(0, 9)
    else:
        if player:
            while not 0 <= top <= 9:
                while top not in numbers:
                    top = input("Space from top?")
                top = int(top)
            while not 0 <= left <= (10 - boatLength):
                while left not in numbers:
                    left = input("Space from left?")
                left = int(left)
        else:
            top = randint(0, 9)
            left = randint(0, (9 - boatLength))
    return top, left


def placeBoat(boatLength, board, vertical, top, left):
    """places the boat on the board, if unsuccessful, it will ask the user to replace their boat"""
    boatPegsPlaced = 0
    while boatPegsPlaced < boatLength and board[top][left] != "O":
        board[top][left] = "O"
        if vertical:  # if vertical
            top += 1
        else:
            left += 1
        boatPegsPlaced += 1
    if boatPegsPlaced < boatLength:
        # if it hits another boat while placing, it removes the partial of the boat placed
        while boatPegsPlaced > 0:
            if vertical:
                top -= 1
            else:
                left -= 1
            boatPegsPlaced -= 1
            board[top][left] = "."
        return False
    return True


def placeBoats(board, player):  # player: True for human, False for computer
    """Places boats onto the board to set up the game"""
    time = 1
    while time < 6:  # computer boat placement
        if player:
            print("\n\n\n\n\n")
            printBoard(playerBoard, True)

        if time == 1:  # game timer
            boat = 5  # variable for boat length (pegs)
            if player:
                print("Aircraft Carrier (5 pegs)")
        elif time == 2:
            boat = 4
            if player:
                print("Battleship (4 pegs)")
        elif time == 3:
            boat = 3
            if player:
                print("Submarine (3 pegs)")
        elif time == 4:
            boat = 3
            if player:
                print("Cruiser (3 pegs)")
        elif time == 5:
            boat = 2
            if player:
                print("Destroyer (2 pegs)")
        else:
            time = 1
            continue

        vertical = getVerticalOrHorizontal(player)

        top, left = getBoatPlacementCoords(player, vertical, boat)

        boatPlaced = placeBoat(boat, board, vertical, top, left)

        if boatPlaced:
            time += 1
        else:
            if player:
                print("your boats collided! Reposition your boat.")
    return


def playerTurn():
    """Player's turn to shoot at a spot on the board"""
    top = -1
    left = -1
    # player's turn
    while not 0 <= left <= 9:  # coordinates for shot
        while left not in numbers:
            left = input("X coordinate?")
        left = int(left) - 1
    while not 0 <= top <= 9:  # coordinates for shot
        while top not in numbers:
            top = input("Y coordinate?")
        top = int(top) - 1
    if hiddenBoard[top][left] == "." and computerBoard[top][left] == ".":
        computerBoard[top][left] = "$"
        print("We missed, Cap'n.")
    elif hiddenBoard[top][left] == "O" and computerBoard[top][left] == ".":
        computerBoard[top][left] = "X"
        print("We got 'em!")
    elif computerBoard[top][left] == "$" or computerBoard[top][left] == "X":
        print("Oops, we already shot there.")
    else:
        print("What just happened?")
    return


def ComputerTryContinueShot(data):
    """Tries to shoot along a boat after 2 successful hits"""
    data['top'] = -1
    data['left'] = -1
    if data['h']:
        if data['h'] == 'up':  # if boat upwards
            newX = data['x'] - 1
            newL = data['l']
            change = newX
            changeVar = 'x'
        elif data['h'] == 'right':  # if boat to the right
            newX = data['x']
            newL = data['l'] + 1
            change = newL
            changeVar = 'l'
        elif data['h'] == 'down':  # if boat down
            newX = data['x'] + 1
            newL = data['l']
            change = newX
            changeVar = 'x'
        elif data['h'] == 'left':  # if boat to the left
            newX = data['x']
            newL = data['l'] - 1
            change = newL
            changeVar = 'l'

        if coordString([newX, newL]) not in eshots and onBoard([change]):
            data['top'] = newX
            data['left'] = newL
        else:  # turns h to opposite
            if changeVar == 'x':
                y = data['x'] - change  # y = 1 or -1
                while playerBoard[data['x'] + y][data['l']] == "X" and onBoard([data['x'] + y]):
                    y = y + 1 if y > 0 else y - 1
                newX = data['x'] + y
                newL = data['l']
                change = newX
            else:
                y = data['l'] - change  # y = 1 or -1
                while playerBoard[data['x']][data['l'] + y] == "X" and onBoard([data['l'] + y]):
                    y = y + 1 if y > 0 else y - 1
                newX = data['x']
                newL = data['l'] + y
                change = newL
            if coordString([newX, newL]) not in eshots and onBoard([change]) and abs(y) < 5:
                data['top'] = newX
                data['left'] = newL
            else:
                data['x'] = -20
                data['l'] = -20
                data['h'] = ''
    return data


def handleCompHitOrMiss(data):
    """Logs the computer shot in the eshots array and outputs text based on a hit or miss"""
    eshots.append(coordString([data['top'], data['left']]))
    if playerBoard[data['top']][data['left']] == ".":
        playerBoard[data['top']][data['left']] = "$"
        print("The enemy missed at %i,%i." %
              (data['left'] + 1, data['top'] + 1))
    elif playerBoard[data['top']][data['left']] == "O":
        if onBoard([data['x'], data['l']]):
            if data['top'] - data['x'] == -1:
                data['h'] = 'up'
            elif data['left'] - data['l'] == 1:
                data['h'] = 'right'
            elif data['top'] - data['x'] == 1:
                data['h'] = 'down'
            elif data['left'] - data['l'] == -1:
                data['h'] = 'left'
            else:
                raise EnvironmentError('Unknown direction for computer shot')
        data['x'] = data['top']
        data['l'] = data['left']
        playerBoard[data['top']][data['left']] = "X"
        print("They hit us at %i,%i Cap'n!" %
              (data['left'] + 1, data['top'] + 1))
    else:
        print("Their Circuits fried.")
    return data


def computerTurn(data):
    """Computer shoots at a random spot on the board, and if it hits it tries to shoot around the same spot"""
    data['top'] = -1
    data['left'] = -1
    while not onBoard([data['top'], data['left']]):  # repeat if not in bounds

        ComputerTryContinueShot(data)

        # loop through all directions
        if data['h'] == '' and onBoard([data['x'], data['l']]):
            data['h'] = 'up'
            while data['h']:
                if data['h'] == 'up' and (data['x'] - 1) >= 0 and (str(data['x'] - 1) + str(data['l'])) not in eshots:
                    data['top'] = data['x'] - 1
                    data['left'] = data['l']
                    data['h'] = ''
                    break
                else:
                    data['h'] = 'right'
                if data['h'] == 'right' and (data['l'] + 1) <= 9 and (str(data['x']) + str(data['l'] + 1)) not in eshots:
                    data['top'] = data['x']
                    data['left'] = data['l'] + 1
                    data['h'] = ''
                    break
                else:
                    data['h'] = 'down'
                if data['h'] == 'down' and (data['x'] + 1) <= 9 and (str(data['x'] + 1) + str(data['l'])) not in eshots:
                    data['top'] = data['x'] + 1
                    data['left'] = data['l']
                    data['h'] = ''
                    break
                else:
                    data['h'] = 'left'
                if data['h'] == 'left' and (data['l'] - 1) >= 0 and (str(data['x']) + str(data['l'] - 1)) not in eshots:
                    data['top'] = data['x']
                    data['left'] = data['l'] - 1
                    data['h'] = ''
                    break
                else:
                    data['h'] = ''
        if not onBoard([data['top'], data['left']]):  # take a random shot
            data['top'] = randint(0, 9)
            data['left'] = randint(0, 9)
            while coordString([data['top'], data['left']]) in eshots:
                data['top'] = randint(0, 9)
                data['left'] = randint(0, 9)

    handleCompHitOrMiss(data)
    return data


def battleshipGame():
    """A game of battleship! Player places boats and will play against a computer player"""

    # Board setup
    print("      BATTLESHIP")
    placeBoats(hiddenBoard, False)
    placeBoats(playerBoard, True)

    # Shows completed board
    printBoard(computerBoard, False)
    printBoard(playerBoard, True)
    # boats placed correctly
    print("you're good to go Cap'n! Where should we shoot?")
    print("\n\n\n\n\n\n")

    # Loop for taking shots
    print("X = hit, $ = miss")  # key for characters
    shotData = {
        'x': -20,  # coordinates of last landed shot
        'l': -20,
        'h': ''  # direction the boat is placed
    }

    playerAlive = True
    computerHit = 0
    while playerAlive and computerHit < 17:  # checks if player won or lost, starts main game loop
        playerTurn()
        shotData = computerTurn(shotData)

        printBoard(computerBoard, False)
        printBoard(playerBoard, True)
        print("\n\n\n\n\n\n")

        # checks if player won or lost
        playerAlive = False
        for i in playerBoard:
            if i.count("O"):
                playerAlive = True
        computerHit = 0
        for i in computerBoard:
            computerHit += i.count("X")

    if computerHit == 17:
        print("Captain we are victorious! Thanks to your fearless leadership.")
    else:
        print("They sunk us Cap'n! I'm going down with the ship!")
        print("It was an honor serving you...")


battleshipGame()
