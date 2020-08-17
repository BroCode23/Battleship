from random import randint

from Boards import *


class Player():

    def getVerticalOrHorizontal(self):
        """Used to place boats, return true if vertical, false if horizontal"""
        choice = ""
        while not (choice == "v" or choice == "h"):  # input loop
            choice = input("Orientation? (v/h)")
            if not choice:
                continue
            choice = choice[0].lower()
        if choice == "v":
            return True
        else:  # choice == "h"
            return False

    def getBoatPlacementCoords(self, vertical, boatLength):
        """Gets the coordinates for the given boat for placement"""
        top = -1
        left = -1
        if vertical:
            maxSpaceFromTop = 10 - boatLength
            maxSpaceFromLeft = 9
        else:  # horizontal
            maxSpaceFromTop = 9
            maxSpaceFromLeft = 10 - boatLength

         # positions boat placement
        while not 0 <= top <= maxSpaceFromTop:
            while top not in NUMBERS:
                top = input("Space from top?")
            top = int(top)
        while not 0 <= left <= maxSpaceFromLeft:
            while left not in NUMBERS:
                left = input("Space from left?")
            left = int(left)
        return top, left

    def placeBoat(self, boatLength, board, vertical, top, left):
        """Places the boat on the board, if unsuccessful, it will remove the partial boat and return false"""
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

    def placeBoats(self, board):
        """Places boats onto the board to set up the game"""
        time = 1
        while time <= 5:  # game state
            print("\n\n\n\n\n")
            printBoard(playerBoard, True)

            if time == 1:
                boat = 5  # variable for boat length (pegs)
                print("Aircraft Carrier (5 pegs)")
            elif time == 2:
                boat = 4
                print("Battleship (4 pegs)")
            elif time == 3:
                boat = 3
                print("Submarine (3 pegs)")
            elif time == 4:
                boat = 3
                print("Cruiser (3 pegs)")
            elif time == 5:
                boat = 2
                print("Destroyer (2 pegs)")

            vertical = self.getVerticalOrHorizontal()

            top, left = self.getBoatPlacementCoords(vertical, boat)

            if self.placeBoat(boat, board, vertical, top, left):
                time += 1
            else:
                print("your boats collided! Reposition your boat.")
        return

    def makeTurn(self):
        """Player's turn to shoot at a spot on the board"""
        top = -1
        left = -1
        while not onBoard(left):  # coordinates for shot
            while left not in NUMBERS:
                left = input("X coordinate?")
            left = int(left) - 1
        while not onBoard(top):  # coordinates for shot
            while top not in NUMBERS:
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
            raise EnvironmentError(
                'hidden or computer board not set up correctly')


class Computer(Player):

    def __init__(self):
        self.vertical = randint(0, 1)
        self.top = -1
        self.left = -1
        self.hit = False  # if last shot hit
        self.turnedAround = False  # if the computer was shooting along the boat but missed
        self.direction = ''  # direction the boat is placed
        self.shots = []
        self.hits = []

    def shotHereBefore(self, top, left):
        """returns true if the shot has already been taken, otherwise false"""
        return coordsToString(top, left) in self.shots

    def getPreviousHit(self):
        """grabs the last landed shot from self.hits"""
        if len(self.hits) == 0:
            raise IndexError("Must have a previous shot to use")
        return stringToCoords(self.hits[-1])

    def getVerticalOrHorizontal(self):
        """returns 1 or 0, vertical or horizontal"""
        self.vertical = randint(0, 1)

    def getBoatPlacementCoords(self, boatLength):
        """Gets the coordinates for the given boat for placement"""
        self.top = -1
        self.left = -1
        if self.vertical:
            maxSpaceFromTop = 10 - boatLength
            maxSpaceFromLeft = 9
        else:  # horizontal
            maxSpaceFromTop = 9
            maxSpaceFromLeft = 10 - boatLength

        self.top = randint(0, maxSpaceFromTop)
        self.left = randint(0, maxSpaceFromLeft)

    def placeBoats(self, board):
        """Places boats onto the board to set up the game"""
        time = 1
        while time <= 5:

            if time == 1:  # game state
                boat = 5  # variable for boat length (pegs)
            elif time == 2:
                boat = 4
            elif time == 3:
                boat = 3
            elif time == 4:
                boat = 3
            elif time == 5:
                boat = 2

            self.getVerticalOrHorizontal()

            self.getBoatPlacementCoords(boat)

            if self.placeBoat(boat, board, self.vertical, self.top, self.left):
                time += 1

    def tryContinueShot(self):
        """Tries to shoot along a boat after 2 successful hits"""
        self.turnedAround = False

        if self.direction:
            # if last shot missed but shooting along boat
            if not self.hit:
                self.turnedAround = True
                if self.direction == 'up':
                    self.direction = 'down'
                elif self.direction == 'down':
                    self.direction = 'up'
                elif self.direction == 'right':
                    self.direction = 'left'
                elif self.direction == 'left':
                    self.direction = 'right'
                else:
                    raise EnvironmentError('Unknown Direciton')

            # find the next shot along the boat
            iterations = 0
            maxIterations = 1  # should only move once if not turned around
            if self.turnedAround:
                maxIterations = 5  # at max could go full length of boat
            while iterations < maxIterations and self.shotHereBefore(self.top, self.left):
                if self.direction == 'up':
                    self.top -= 1
                    if not onBoard(self.top):
                        self.direction = 'down'
                elif self.direction == 'down':
                    self.top += 1
                    if not onBoard(self.top):
                        self.direction = 'up'
                elif self.direction == 'right':
                    self.left += 1
                    if not onBoard(self.left):
                        self.direction = 'left'
                elif self.direction == 'left':
                    self.left -= 1
                    if not onBoard(self.left):
                        self.direction = 'right'
                else:
                    raise EnvironmentError('Unknown Direciton')
                iterations += 1
                if not onBoard(self.top, self.left):
                    iterations = 0
                    maxIterations = 5
                    self.turnedAround = True

            # reset everything
            if not onBoard(self.top, self.left) or self.shotHereBefore(self.top, self.left):
                self.top = -1
                self.left = -1
                self.direction = ''
                self.hit = False
                self.turnedAround = False

    def handleHitOrMiss(self):
        """Logs the computer shot in the self.shots array and outputs text based on a hit or miss"""
        if len(self.hits) > 0:
            prevTop, prevLeft = self.getPreviousHit()
        self.shots.append(coordsToString(self.top, self.left))

        if playerBoard[self.top][self.left] == ".":
            playerBoard[self.top][self.left] = "$"
            print("The enemy missed at %i,%i." %
                  (self.left + 1, self.top + 1))
            # want to shoot in all directions
            if self.hit and len(self.hits) > 0 and not self.direction:
                self.top, self.left = prevTop, prevLeft
            else:
                self.hit = False
            if self.turnedAround:  # if already turned around and missed, find a new boat to shoot
                self.direction = ''
            return 0  # returns 0 so the player doesn't lose a life
        elif playerBoard[self.top][self.left] == "O":
            if len(self.shots) > 0 and self.hit:  # find direction
                if self.top - prevTop == -1:
                    self.direction = 'up'
                elif self.left - prevLeft == 1:
                    self.direction = 'right'
                elif self.top - prevTop == 1:
                    self.direction = 'down'
                elif self.left - prevLeft == -1:
                    self.direction = 'left'
                else:
                    self.direction = ''
            self.hit = True
            playerBoard[self.top][self.left] = "X"
            self.hits.append(coordsToString(self.top, self.left))
            print("They hit us at %i,%i Cap'n!" %
                  (self.left + 1, self.top + 1))
            return 1  # returns 1 because they hit the player's boat
        else:
            print("Their Circuits fried.")
            raise EnvironmentError('Computer didn\'t hit or miss')

    def makeTurn(self):
        """Computer shoots at a random spot on the board, and if it hits it tries to shoot around the same spot"""
        self.tryContinueShot()

        # loop through all directions if hit a boat for the first time
        if not self.direction and self.hit:
            prevTop, prevLeft = self.getPreviousHit()

            if onBoard(prevTop - 1) and not self.shotHereBefore(prevTop - 1, prevLeft):
                prevTop -= 1
                self.top, self.left = prevTop, prevLeft
            elif onBoard(prevLeft + 1) and not self.shotHereBefore(prevTop, prevLeft + 1):
                prevLeft += 1
                self.top, self.left = prevTop, prevLeft
            elif onBoard(prevTop + 1) and not self.shotHereBefore(prevTop + 1, prevLeft):
                prevTop += 1
                self.top, self.left = prevTop, prevLeft
            elif onBoard(prevLeft - 1) and not self.shotHereBefore(prevTop, prevLeft - 1):
                prevLeft -= 1
                self.top, self.left = prevTop, prevLeft
            else:
                self.hit = False

        # otherwise take a random shot
        if not onBoard(self.top, self.left) or self.shotHereBefore(self.top, self.left):
            self.top = randint(0, 9)
            self.left = randint(0, 9)
            while self.shotHereBefore(self.top, self.left):
                self.top = randint(0, 9)
                self.left = randint(0, 9)

        return self.handleHitOrMiss()


class BattleshipGame():

    def __init__(self):
        self.human = Player()
        self.computer = Computer()

    def playGame(self):
        """A game of battleship! Player places boats and will play against a computer player"""

        # Board setup
        print("      BATTLESHIP")
        self.computer.placeBoats(hiddenBoard)
        self.human.placeBoats(playerBoard)

        # Shows completed board
        printBoard(computerBoard, False)
        printBoard(playerBoard, True)

        # boats placed correctly
        print("you're good to go Cap'n! Where should we shoot?")
        print("\n\n\n\n\n\n")
        print("X = hit, $ = miss")  # key for characters

        playerPegsLeft = 17
        computerPegsLeft = 17
        # checks if player won or lost, starts main game loop
        while playerPegsLeft and computerPegsLeft:
            # turn functions return 1 if hit, else 0
            computerPegsLeft -= self.human.makeTurn()
            playerPegsLeft -= self.computer.makeTurn()

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


game = BattleshipGame()
game.playGame()
