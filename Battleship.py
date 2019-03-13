import random
eshots = []
num = ["0","1","2","3","4","5","6","7","8","9","10"]

player_board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

computer_board =   [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

hidden_board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		  [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

def print_board(input_board, player):
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

def place_boats(board, player): #player: True for human, False for computer
	time = 1
	while time < 6: #computer boat placement
		y = 0
		top = -1
		lef = -1
		choice = ""

		if player:
			print("\n\n\n\n\n")
			print_board(player_board, True)
		
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
		
		if player:
			orient = False
			while not (choice == "v" or choice == "h"): #input loop
				choice = input("Orientation? (v/h)")[0].lower()
				if choice == "v":
					orient = True
				elif choice == "h":
					orient = False
				else:
					continue
		else:
			orient = random.randint(0,1)
			
		if orient: #vertical
			if player:
				while not 0 <= top <= (10 - boat): #positions boat placement from top
					while num.count(top) == 0:
						top = input("Space from top?")
					top = int(top)
				while not 0 <= lef <= 9: #positioning from left
					while num.count(lef) == 0:
						lef = input("Space from left?")
					lef = int(lef)
			else:
				top = random.randint(0,(9 - boat))
				lef = random.randint(0,9)
		else:
			if player:
				while not 0 <= top <= 9:
					while num.count(top) == 0:
						top = input("Space from top?")
					top = int(top)
				while not 0 <= lef <= (10 - boat):
					while num.count(lef) == 0:
						lef = input("Space from left?")
					lef = int(lef)
			else:	
				top = random.randint(0,9)
				lef = random.randint(0,(9 - boat))
				
		while y < boat and board[top][lef] != "O":
			board[top][lef] = "O"
			if orient:
				top += 1
			else:
				lef += 1
			y += 1
		if board[top][lef] == "O": #if it hits another boat while placing, it removes the partial of the boat placed
			while y > 0:
				if orient:
					top -= 1
				else:
					lef -= 1
				y -= 1
				board[top][lef] = "."
			if player:
				print("your boats collided! Reposition your boat.")
			continue
		time += 1
	return None

def player_turn():
	top = -1
	lef = -1
	#player's turn
	while not 0 <= lef <= 9: #coordinates for shot
		while num.count(lef) == 0:
			lef = input("X coordinate?")
		lef = int(lef) - 1
	while not 0 <= top <= 9: #coordinates for shot
		while num.count(top) == 0:
			top = input("Y coordinate?")
		top = int(top) - 1
	if hidden_board[top][lef] == "." and computer_board[top][lef] == ".":
		computer_board[top][lef] = "$"
		print("We missed, Cap'n.")
	elif hidden_board[top][lef] == "O" and computer_board[top][lef] == ".":
		computer_board[top][lef] = "X"
		print("We got 'em!")
	elif computer_board[top][lef] == "$" or computer_board[top][lef] == "X":
		print("Oops, we already shot there.")
	else:
		print("What just happened?")
	return

def computer_turn(x, l, h):
	top = -1
	lef = -1
	while not 0 <= top <= 9 and  not 0 <= lef <= 9: #repeat if not in bounds
		y = 1
		top = -1
		lef = -1
		if h == 1: #if boat upwards
			if not eshots.count(str(x - 1) + str(l)) and 0 <= x - 1 <= 9:
				top = x - 1
				lef = l
			else: #turns h to 3
				while player_board[x + y][l] == "X" and 0 <= x + y <= 9:
					y += 1
				if not eshots.count(str(x + y) + str(l)) and 0 <= x + y <= 9 and y < 5:
					top = x + y
					lef = l
				else:
					x = -20
					l = -20
					h = 0
		if h == 2:  # if boat to the right
			if not eshots.count(str(x) + str(l + 1)) and 0 <= l + 1 <= 9:
				top = x
				lef = l + 1
			else: # turns h to 4
				while player_board[x][l - y] == "X" and 0 <= l - y <= 9:
					y += 1
				if not eshots.count(str(x) + str(l - y)) and 0 <= l - y <= 9 and y < 5:
					top = x
					lef = l - y
				else:
					x = -20
					l = -20
					h = 0
		if h == 3: #if boat downwards
			if not eshots.count(str(x + 1) + str(l)) and 0 <= x + 1 <= 9:
				top = x + 1
				lef = l
			else: #turn h to 1
				while player_board[x - y][l] == "X" and 0 <= x - y <= 9: #checks through the other side of the boat
					y += 1
				if not eshots.count(str(x - y) + str(l)) and 0 <= x - y <= 9 and y < 5:
					top = x - y
					lef = l
				else:
					x = -20
					l = -20
					h = 0
		if h == 4:  # if boat to the left
			if not eshots.count(str(x) + str(l - 1)) and 0 <= l - 1 <= 9:
				top = x
				lef = l - 1
			else: # turns h to 2
				while player_board[x][l + y] == "X" and 0 <= l + y <= 9:
					y += 1
				if not eshots.count(str(x) + str(l + y)) and 0 <= l + y <= 9 and y < 5:
					top = x
					lef = l + y
				else:
					x = -20
					l = -20
					h = 0
		if h == 0 and 0 <= x <= 9 and 0 <= l <= 9:
			h = 1
			while 0 < h < 6:
				if h == 1 and (x - 1) >= 0 and not eshots.count(str(x - 1) + str(l)):
					top = x - 1
					lef = l
					h = 0
					continue
				if h == 2 and (l + 1) <= 9 and not eshots.count(str(x) + str(l + 1)):
					top = x
					lef = l + 1
					h = 0
					continue
				if h == 3 and (x + 1) <= 9 and not eshots.count(str(x + 1) + str(l)):
					top = x + 1
					lef = l
					h = 0
					continue
				if h == 4 and (l - 1) >= 0 and not eshots.count(str(x) + str(l - 1)):
					top = x
					lef = l - 1
					h = 0
					continue
				if h == 5:
					top = random.randint(0, 9)
					lef = random.randint(0, 9)
					while eshots.count(str(top) + str(lef)):
						top = random.randint(0, 9)
						lef = random.randint(0, 9)
					h = 0
					continue
				h += 1
		if not 0 <= top <= 9 or not 0 <= lef <= 9:
			top = random.randint(0, 9)
			lef = random.randint(0, 9)
			while eshots.count(str(top) + str(lef)):
				top = random.randint(0, 9)
				lef = random.randint(0, 9)
				
	eshots.append(str(top) + str(lef))
	if player_board[top][lef] == ".":
		player_board[top][lef] = "$"
		print("The enemy missed at %i,%i." % (lef + 1, top + 1))
	elif player_board[top][lef] == "O":
		if 0 <= x <= 9 and 0 <= l <= 9:
			if top - x == 1:
				h = 3
			if top - x == -1:
				h = 1
			if lef - l == 1:
				h = 2
			if lef - l == -1:
				h = 4
		x = top
		l = lef
		player_board[top][lef] = "X"
		print("They hit us at %i,%i Cap'n!"%(lef + 1, top + 1))
	else:
		print("Their Circuits fried.")
	return x, l, h

#MAIN GAME

#Board setup
print("      BATTLESHIP")
place_boats(hidden_board, False)
place_boats(player_board, True)

#Shows completed board
print_board(computer_board, False)
print_board(player_board, True)
print("you're good to go Cap'n! Where should we shoot?") #boats placed correctly
print("\n\n\n\n\n\n")

#Loop for taking shots
print("X = hit, $ = miss") #key for characters
x = -20 #coordinates of last landed shot
l = -20
h = 0 #direction the boat is placed
player_alive = True
computer_hit = 0
while player_alive and computer_hit < 17: #checks if player won or lost, starts main game loop
	player_turn()
	x, l, h = computer_turn(x, l, h)
	
	print_board(computer_board, False)
	print_board(player_board, True)
	print("\n\n\n\n\n\n")

	#checks if player won or lost
	player_alive = False
	for i in player_board:
		if i.count("O"):
			player_alive = True
	computer_hit = 0
	for i in computer_board:
		computer_hit += i.count("X")
		
if not player_alive:
	print("They sunk us Cap'n! I'm going down with the ship!")
	print("It was an honor serving you...")
else:
	print("Captain we are victorious! Thanks to your fearless leadership.")
