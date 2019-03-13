import random
brk = False
s = " "
eshots = []
time = 1
boat = 5
num = ["0","1","2","3","4","5","6","7","8","9","10"]
player = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

comp =   [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

hidden = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

def board():
    print("      YOUR BOATS")
    print("   1 2 3 4 5 6 7 8 9 10")
    print("1  " + s.join(player[0]))
    print("2  " + s.join(player[1]))
    print("3  " + s.join(player[2]))
    print("4  " + s.join(player[3]))
    print("5  " + s.join(player[4]))
    print("6  " + s.join(player[5]))
    print("7  " + s.join(player[6]))
    print("8  " + s.join(player[7]))
    print("9  " + s.join(player[8]))
    print("10 " + s.join(player[9]))

def enemy():
    print("      ENEMY BOATS")
    print("   1 2 3 4 5 6 7 8 9 10")
    print("1  " + s.join(comp[0]))
    print("2  " + s.join(comp[1]))
    print("3  " + s.join(comp[2]))
    print("4  " + s.join(comp[3]))
    print("5  " + s.join(comp[4]))
    print("6  " + s.join(comp[5]))
    print("7  " + s.join(comp[6]))
    print("8  " + s.join(comp[7]))
    print("9  " + s.join(comp[8]))
    print("10 " + s.join(comp[9]))

def hid():
    print("      HIDDEN BOATS")
    print("   1 2 3 4 5 6 7 8 9 10")
    print("1  " + s.join(hidden[0]))
    print("2  " + s.join(hidden[1]))
    print("3  " + s.join(hidden[2]))
    print("4  " + s.join(hidden[3]))
    print("5  " + s.join(hidden[4]))
    print("6  " + s.join(hidden[5]))
    print("7  " + s.join(hidden[6]))
    print("8  " + s.join(hidden[7]))
    print("9  " + s.join(hidden[8]))
    print("10 " + s.join(hidden[9]))

print("      BATTLESHIP")

#Board setup
while time < 6: #computer boat placement
    y = 0
    top = -1
    lef = -1
    orient = ""

    if time == 1: #game timer
        boat = 5 #variable for boat length (pegs)
    elif time == 2:
        boat = 4
    elif time == 3:
        boat = 3
    elif time == 4:
        boat = 3
    elif time == 5:
        boat = 2

    orient = random.randint(0,1)
    if orient: #vertical
        top = random.randint(0,(9 - boat))
        lef = random.randint(0,9)
    else: #horizontal
        top = random.randint(0,9)
        lef = random.randint(0,(9 - boat))

    if orient: #vertical
        while y < boat and hidden[top][lef] != "O":
            hidden[top][lef] = "O"
            top += 1
            y += 1
        if hidden[top][lef] == "O": #if it hits another boat while placing, it removes the partial of the boat placed
            while y > 0:
                top -= 1
                y -= 1
                hidden[top][lef] = "."
            continue
        time += 1
    else: #horizontal
        while y < boat and hidden[top][lef] != "O": #places the boat
            hidden[top][lef] = "O"
            lef += 1
            y += 1
        if hidden[top][lef] == "O":  # checks if a boat was already placed there
            while y > 0:  # while loop to undo boat placement
                lef -= 1
                y -= 1
                hidden[top][lef] = "."
            continue  # if boats collide, it will repeat to same boat
        time += 1

time = 1
boat = 5
while time < 6: #player boat placement
    y = 1
    top = -1
    lef = -1
    orient = ""
    print("|\n|\n|\n|\n|")
    board()
    if time == 1: #game timer
        boat = 5 #variable for boat length (pegs)
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
    while not (orient == "v" or orient == "h"): #input loop
        orient = input("Orientation? (v/h)")
        orient = orient[0].lower()
        if orient == "v":
            while not 0 <= top <= (10 - boat): #positions boat placement from top
                while num.count(top) == 0:
                    top = input("Space from top?")
                top = int(top)
            while not 0 <= lef <= 9: #positioning from left
                while num.count(lef) == 0:
                    lef = input("Space from left?")
                lef = int(lef)
        elif orient == "h":
            while not 0 <= top <= 9:
                while num.count(top) == 0:
                    top = input("Space from top?")
                top = int(top)
            while not 0 <= lef <= (10 - boat):
                while num.count(lef) == 0:
                    lef = input("Space from left?")
                lef = int(lef)
        else:
            continue
    if orient == "h": #graphs out the points for the boat
        while y <= boat:
            if player[top][lef] == "O": #checks if a boat was already placed there
                brk = True
                while y > 1: #while loop to undo boat placement
                    lef -= 1
                    y -= 1
                    player[top][lef] = "."
                print("your boats collided! Reposition your boat.")
                break #if boats collide, it will repeat to same boat
            player[top][lef] = "O"
            lef += 1
            y += 1
        if brk:
            brk = False
            continue
        time += 1
    else: #if orientation is vertical
        while y <= boat:
            if player[top][lef] == "O":
                brk = True
                while y > 1:
                    top -= 1
                    y -= 1
                    player[top][lef] = "."
                print("your boats collided! Reposition your boat.")
                break
            player[top][lef] = "O"
            top += 1
            y += 1
        if brk:
            brk = False
            continue
        time += 1
enemy()
board()
print("you're good to go Cap'n! Where should we shoot?") #boats placed correctly
print()
print()
print()
print()
print()
print()
print("X = hit, $ = miss") #key for characters
x = -20 #coordinates of last landed shot
l = -20
h = 0
coun = False
counc = 0
for i in player:
    if i.count("O"):
        coun = True
for i in comp:
    if i.count("X"):
        counc += i.count("X")
while coun and counc < 17:
    top = -1
    lef = -1
    #player's turn
    while not 0 <= lef <= 9: #coordinates for shot
        while num.count(lef) == 0:
            lef = str(input("X coordinate?"))
        lef = int(lef) - 1
    while not 0 <= top <= 9: #coordinates for shot
        while num.count(top) == 0:
            top = str(input("Y coordinate?"))
        top = int(top) - 1
    if hidden[top][lef] == "." and comp[top][lef] == ".":
        comp[top][lef] = "$"
        print("We missed, Cap'n.")
    elif hidden[top][lef] == "O" and comp[top][lef] == ".":
        comp[top][lef] = "X"
        print("We got 'em!")
    elif comp[top][lef] == "$" or comp[top][lef] == "X":
        print("Oops, we already shot there.")
    else:
        print("What just happened?")
    top = -1
    lef = -1
    #computer's turn
    while not 0 <= top <= 9 and  not 0 <= lef <= 9: #repeat if not in bounds
        y = 1
        top = -1
        lef = -1
        if h == 1: #if boat upwards
            if not eshots.count(str(x - 1) + str(l)) and 0 <= x - 1 <= 9:
                top = x - 1
                lef = l
            else: #turns h to 3
                while player[x + y][l] == "X" and 0 <= x + y <= 9:
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
                while player[x][l - y] == "X" and 0 <= l - y <= 9:
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
                while player[x - y][l] == "X" and 0 <= x - y <= 9: #checks through the other side of the boat
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
                while player[x][l + y] == "X" and 0 <= l + y <= 9:
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
    if player[top][lef] == ".":
        player[top][lef] = "$"
        print("The enemy missed at %i,%i." % (lef + 1, top + 1))
    elif player[top][lef] == "O":
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
        player[top][lef] = "X"
        print("They hit us at %i,%i Cap'n!"%(lef + 1, top + 1))
    else:
        print("Their Circuits fried.")
    enemy()
    board()
    print()
    print()
    print()
    print()
    print()
    print()
    coun = False
    for i in player:
        if i.count("O"):
            coun = True
    counc = 0
    for i in comp:
        if i.count("X"):
            counc += i.count("X")
if not coun:
    print("They sunk us Cap'n! I'm going down with the ship!")
    print("It was an honor serving you...")
else:
    print("Captain we are victorious! Thanks to your fearless leadership.")
