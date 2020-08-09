from random import randint

from Boards import *


def getVerticalOrHorizontal(player):
    """Return true if vertical, false if horizontal"""
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
    """Gets the coordinates for the given boat for placement"""
    top = -1
    left = -1
    if vertical:
        maxSpaceFromTop = 10 - boatLength
        maxSpaceFromLeft = 9
    else:  # horizontal
        maxSpaceFromTop = 9
        maxSpaceFromLeft = 10 - boatLength

    if player:
        # positions boat placement
        while not 0 <= top <= maxSpaceFromTop:
            while top not in numbers:
                top = input("Space from top?")
            top = int(top)
        while not 0 <= left <= maxSpaceFromLeft:
            while left not in numbers:
                left = input("Space from left?")
            left = int(left)
    else:
        top = randint(0, maxSpaceFromTop)
        left = randint(0, maxSpaceFromLeft)
    return top, left


def placeBoat(boatLength, board, vertical, top, left):
    """Places the boat on the board, if unsuccessful, it will return false"""
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
    while time <= 5:  # computer boat placement
        if player:
            print("\n\n\n\n\n")
            printBoard(playerBoard, True)

        if time == 1:  # game timer
            boat = 5  # variable for boat length (pegs)
            gameOutput("Aircraft Carrier (5 pegs)", player)
        elif time == 2:
            boat = 4
            gameOutput("Battleship (4 pegs)", player)
        elif time == 3:
            boat = 3
            gameOutput("Submarine (3 pegs)", player)
        elif time == 4:
            boat = 3
            gameOutput("Cruiser (3 pegs)", player)
        elif time == 5:
            boat = 2
            gameOutput("Destroyer (2 pegs)", player)

        vertical = getVerticalOrHorizontal(player)

        top, left = getBoatPlacementCoords(player, vertical, boat)

        boatPlaced = placeBoat(boat, board, vertical, top, left)

        if boatPlaced:
            time += 1
        else:
            gameOutput("your boats collided! Reposition your boat.", player)
    return


def playerTurn():
    """Player's turn to shoot at a spot on the board"""
    top = -1
    left = -1
    # player's turn
    while not onBoard([left]):  # coordinates for shot
        while left not in numbers:
            left = input("X coordinate?")
        left = int(left) - 1
    while not onBoard([top]):  # coordinates for shot
        while top not in numbers:
            top = input("Y coordinate?")
        top = int(top) - 1
    if hiddenBoard[top][left] == "." and computerBoard[top][left] == ".":
        computerBoard[top][left] = "$"
        print("We missed, Cap'n.")
        return 0
    elif hiddenBoard[top][left] == "O" and computerBoard[top][left] == ".":
        computerBoard[top][left] = "X"
        print("We got 'em!")
        return 1
    elif computerBoard[top][left] == "$" or computerBoard[top][left] == "X":
        print("Oops, we already shot there.")
        return 0
    else:
        raise EnvironmentError('hidden or computer board not set up correctly')


def ComputerTryContinueShot(data):
    """Tries to shoot along a boat after 2 successful hits"""
    direction = data['direction']
    t = data['t']
    l = data['l']
    top = -1
    left = -1

    if direction:
        if direction == 'up':  # if boat upwards
            newX = t - 1
            newL = l
            change = newX
            changeVar = 't'
        elif direction == 'down':  # if boat down
            newX = t + 1
            newL = l
            change = newX
            changeVar = 't'
        elif direction == 'right':  # if boat to the right
            newX = t
            newL = l + 1
            change = newL
            changeVar = 'l'
        elif direction == 'left':  # if boat to the left
            newX = t
            newL = l - 1
            change = newL
            changeVar = 'l'

        if coordString([newX, newL]) not in eshots and onBoard([change]):
            top = newX
            left = newL
        else:  # turns h to opposite
            if changeVar == 't':
                y = t - change  # y = 1 or -1
                while playerBoard[t + y][l] == "X" and onBoard([t + y]):
                    y = y + 1 if y > 0 else y - 1
                newX = t + y
                newL = l
                change = newX
            else:
                y = l - change  # y = 1 or -1
                while playerBoard[t][l + y] == "X" and onBoard([l + y]):
                    y = y + 1 if y > 0 else y - 1
                newX = t
                newL = l + y
                change = newL
            if coordString([newX, newL]) not in eshots and onBoard([change]) and abs(y) < 5:
                top = newX
                left = newL
            else:
                t = -20
                l = -20
                direction = ''

    newData = {
        't': t,  # coordinates of last landed shot
        'l': l,
        'direction': direction,  # direction the boat is placed
        'top': top,  # coordinates for current shot
        'left': left
    }
    return newData


def handleCompHitOrMiss(d):  # d stands for data
    """Logs the computer shot in the eshots array and outputs text based on a hit or miss"""

    eshots.append(coordString([d['top'], d['left']]))
    if playerBoard[d['top']][d['left']] == ".":
        playerBoard[d['top']][d['left']] = "$"
        print("The enemy missed at %i,%i." %
              (d['left'] + 1, d['top'] + 1))
        return d, 0
    elif playerBoard[d['top']][d['left']] == "O":
        if onBoard([d['t'], d['l']]):
            if d['top'] - d['t'] == -1:
                d['direction'] = 'up'
            elif d['left'] - d['l'] == 1:
                d['direction'] = 'right'
            elif d['top'] - d['t'] == 1:
                d['direction'] = 'down'
            elif d['left'] - d['l'] == -1:
                d['direction'] = 'left'
            else:
                raise EnvironmentError('Unknown direction for computer shot')
        d['t'] = d['top']
        d['l'] = d['left']
        playerBoard[d['top']][d['left']] = "X"
        print("They hit us at %i,%i Cap'n!" %
              (d['left'] + 1, d['top'] + 1))
        return d, 1

    print("Their Circuits fried.")
    raise EnvironmentError('Computer didn\'t hit or miss')


def computerTurn(d):  # d stands for data
    """Computer shoots at a random spot on the board, and if it hits it tries to shoot around the same spot"""
    d['top'] = -1
    d['left'] = -1
    while not onBoard([d['top'], d['left']]):  # repeat if not in bounds

        d = ComputerTryContinueShot(d)

        # loop through all directions
        if d['direction'] == '' and onBoard([d['t'], d['l']]):
            d['direction'] = 'up'
            while d['direction']:
                if d['direction'] == 'up' and (d['t'] - 1) >= 0 and coordString([d['t'] - 1, d['l']]) not in eshots:
                    d['top'] = d['t'] - 1
                    d['left'] = d['l']
                    d['direction'] = ''
                    break
                else:
                    d['direction'] = 'right'
                if d['direction'] == 'right' and (d['l'] + 1) <= 9 and coordString([d['t'], d['l'] + 1]) not in eshots:
                    d['top'] = d['t']
                    d['left'] = d['l'] + 1
                    d['direction'] = ''
                    break
                else:
                    d['direction'] = 'down'
                if d['direction'] == 'down' and (d['t'] + 1) <= 9 and coordString([d['t'] + 1, d['l']]) not in eshots:
                    d['top'] = d['t'] + 1
                    d['left'] = d['l']
                    d['direction'] = ''
                    break
                else:
                    d['direction'] = 'left'
                if d['direction'] == 'left' and (d['l'] - 1) >= 0 and coordString([d['t'], d['l'] - 1]) not in eshots:
                    d['top'] = d['t']
                    d['left'] = d['l'] - 1
                    d['direction'] = ''
                    break
                else:
                    d['direction'] = ''
        if not onBoard([d['top'], d['left']]):  # take a random shot
            d['top'] = randint(0, 9)
            d['left'] = randint(0, 9)
            while coordString([d['top'], d['left']]) in eshots:
                d['top'] = randint(0, 9)
                d['left'] = randint(0, 9)

    return handleCompHitOrMiss(d)


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
        't': -20,  # coordinates of last landed shot
        'l': -20,  # t = top (y), l = left (x)
        'direction': '',  # direction the boat is placed
        'top': -1,  # coordinates for current shot
        'left': -1
    }

    playerPegsLeft = 17
    computerPegsLeft = 17
    # checks if player won or lost, starts main game loop
    while playerPegsLeft and computerPegsLeft:
        # turn functions return 1 if hit, else 0
        computerPegsLeft -= playerTurn()
        shotData, computerHit = computerTurn(shotData)
        playerPegsLeft -= computerHit

        printBoard(computerBoard, False)
        printBoard(playerBoard, True)
        print("\n\n\n\n\n\n")

    if not computerPegsLeft and playerPegsLeft:
        print("Cap'n we are victorious! Thanks to yerr fearless leadership.")
    elif not playerPegsLeft and computerPegsLeft:  # player not alive :(
        print("They sunk our fleet Cap'n! I'm going down with the ship!")
        print("It was an honor serving you...")
    else:
        print("It was a tie?? How is that possible??")


battleshipGame()
