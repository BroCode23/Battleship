import random
eshots = [] #array of all enemy shots, listed in the form of "(top)(left)"
numbers = ["0","1","2","3","4","5","6","7","8","9","10"]

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

def printBoard(input_board, player):
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
        while not (choice == "v" or choice == "h"): #input loop
            choice = input("Orientation? (v/h)")[0].lower()
        if choice == "v":
            vertical = True
        elif choice == "h":
            vertical = False
        return vertical
    else:
        return random.randint(0, 1)

def getBoatPlacementCoords(player, vertical, boatLength):
    """gets the coordinates for the given boat for placement"""
    top = -1
    left = -1
    if vertical:
        if player:
            while not 0 <= top <= (10 - boatLength): #positions boat placement from top
                while top not in numbers:
                    top = input("Space from top?")
                top = int(top)
            while not 0 <= left <= 9: #positioning from left
                while left not in numbers:
                    left = input("Space from left?")
                left = int(left)
        else:
            top = random.randint(0, (9 - boatLength))
            left = random.randint(0, 9)
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
            top = random.randint(0, 9)
            left = random.randint(0, (9 - boatLength))
    return top, left

def placeBoat(boatLength, board, vertical, top, left):
    """places the boat on the board, if unsuccessful, it will ask the user to replace their boat"""
    boatPegsPlaced = 0
    while boatPegsPlaced < boatLength and board[top][left] != "O":
        board[top][left] = "O"
        if vertical: #if vertical
            top += 1
        else:
            left += 1
        boatPegsPlaced += 1
    if boatPegsPlaced < boatLength:
        #if it hits another boat while placing, it removes the partial of the boat placed
        while boatPegsPlaced > 0:
            if vertical:
                top -= 1
            else:
                left -= 1
            boatPegsPlaced -= 1
            board[top][left] = "."
        return False
    return True

def placeBoats(board, player): #player: True for human, False for computer
    """Places boats onto the board to set up the game"""
    time = 1
    while time < 6: #computer boat placement
        if player:
            print("\n\n\n\n\n")
            printBoard(playerBoard, True)

        if time == 1: #game timer
            boat = 5 #variable for boat length (pegs)
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
    #player's turn
    while not 0 <= left <= 9: #coordinates for shot
        while left not in numbers:
            left = input("X coordinate?")
        left = int(left) - 1
    while not 0 <= top <= 9: #coordinates for shot
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

def computerTurn(x, l, h):
    """Computer shoots at a random spot on the board, and if it hits it tries to shoot around the same spot"""
    top = -1
    left = -1
    while not 0 <= top <= 9 and  not 0 <= left <= 9: #repeat if not in bounds
        y = 1
        top = -1
        left = -1
        if h == 1: #if boat upwards
            if not eshots.count(str(x - 1) + str(l)) and 0 <= x - 1 <= 9:
                top = x - 1
                left = l
            else: #turns h to 3
                while playerBoard[x + y][l] == "X" and 0 <= x + y <= 9:
                    y += 1
                if not eshots.count(str(x + y) + str(l)) and 0 <= x + y <= 9 and y < 5:
                    top = x + y
                    left = l
                else:
                    x = -20
                    l = -20
                    h = 0
        if h == 2:  # if boat to the right
            if not eshots.count(str(x) + str(l + 1)) and 0 <= l + 1 <= 9:
                top = x
                left = l + 1
            else: # turns h to 4
                while playerBoard[x][l - y] == "X" and 0 <= l - y <= 9:
                    y += 1
                if not eshots.count(str(x) + str(l - y)) and 0 <= l - y <= 9 and y < 5:
                    top = x
                    left = l - y
                else:
                    x = -20
                    l = -20
                    h = 0
        if h == 3: #if boat downwards
            if not eshots.count(str(x + 1) + str(l)) and 0 <= x + 1 <= 9:
                top = x + 1
                left = l
            else: #turn h to 1
                while playerBoard[x - y][l] == "X" and 0 <= x - y <= 9: #checks through the other side of the boat
                    y += 1
                if not eshots.count(str(x - y) + str(l)) and 0 <= x - y <= 9 and y < 5:
                    top = x - y
                    left = l
                else:
                    x = -20
                    l = -20
                    h = 0
        if h == 4:  # if boat to the left
            if not eshots.count(str(x) + str(l - 1)) and 0 <= l - 1 <= 9:
                top = x
                left = l - 1
            else: # turns h to 2
                while playerBoard[x][l + y] == "X" and 0 <= l + y <= 9:
                    y += 1
                if not eshots.count(str(x) + str(l + y)) and 0 <= l + y <= 9 and y < 5:
                    top = x
                    left = l + y
                else:
                    x = -20
                    l = -20
                    h = 0
        if h == 0 and 0 <= x <= 9 and 0 <= l <= 9:
            h = 1
            while 0 < h < 6:
                if h == 1 and (x - 1) >= 0 and not eshots.count(str(x - 1) + str(l)):
                    top = x - 1
                    left = l
                    h = 0
                    continue
                if h == 2 and (l + 1) <= 9 and not eshots.count(str(x) + str(l + 1)):
                    top = x
                    left = l + 1
                    h = 0
                    continue
                if h == 3 and (x + 1) <= 9 and not eshots.count(str(x + 1) + str(l)):
                    top = x + 1
                    left = l
                    h = 0
                    continue
                if h == 4 and (l - 1) >= 0 and not eshots.count(str(x) + str(l - 1)):
                    top = x
                    left = l - 1
                    h = 0
                    continue
                if h == 5:
                    top = random.randint(0, 9)
                    left = random.randint(0, 9)
                    while eshots.count(str(top) + str(left)):
                        top = random.randint(0, 9)
                        left = random.randint(0, 9)
                    h = 0
                    continue
                h += 1
        if not 0 <= top <= 9 or not 0 <= left <= 9:
            top = random.randint(0, 9)
            left = random.randint(0, 9)
            while eshots.count(str(top) + str(left)):
                top = random.randint(0, 9)
                left = random.randint(0, 9)

    eshots.append(str(top) + str(left))
    if playerBoard[top][left] == ".":
        playerBoard[top][left] = "$"
        print("The enemy missed at %i,%i." % (left + 1, top + 1))
    elif playerBoard[top][left] == "O":
        if 0 <= x <= 9 and 0 <= l <= 9:
            if top - x == 1:
                h = 3
            if top - x == -1:
                h = 1
            if left - l == 1:
                h = 2
            if left - l == -1:
                h = 4
        x = top
        l = left
        playerBoard[top][left] = "X"
        print("They hit us at %i,%i Cap'n!"%(left + 1, top + 1))
    else:
        print("Their Circuits fried.")
    return x, l, h

#MAIN GAME

#Board setup
print("      BATTLESHIP")
placeBoats(hiddenBoard, False)
placeBoats(playerBoard, True)

#Shows completed board
printBoard(computerBoard, False)
printBoard(playerBoard, True)
print("you're good to go Cap'n! Where should we shoot?") #boats placed correctly
print("\n\n\n\n\n\n")

#Loop for taking shots
print("X = hit, $ = miss") #key for characters
x = -20 #coordinates of last landed shot
l = -20
h = 0 #direction the boat is placed
playerAlive = True
computerHit = 0
while playerAlive and computerHit < 17: #checks if player won or lost, starts main game loop
    playerTurn()
    x, l, h = computerTurn(x, l, h)

    printBoard(computerBoard, False)
    printBoard(playerBoard, True)
    print("\n\n\n\n\n\n")

    #checks if player won or lost
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
