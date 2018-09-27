print("BATTLESHIP")
grid = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
s = " "
y = 0
time = 1
boat = 5
while time < 6:
    top = -1
    lef = -1
    orient = ""
    if time == 1:
        boat = 5
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
    while not (orient == "v" or orient == "h"):
        orient = input("what orientation would you like your ship? (v/h)")
        orient = orient[0].lower()
        if orient == "v":
            while not 0 <= top <= (10 - boat):
                top = int(input("Space from top?"))
                top = top % 10
            while not 0 <= lef <= 9:
                lef = int(input("Space from left?"))
                lef = lef % 10
        elif orient == "h":
            while not 0 <= top <= 9:
                top = int(input("Space from top?"))
                top = top % 10
            while not 0 <= lef <= (10 - boat):
                lef = int(input("Space from left?"))
                lef = lef % 10
        else:
            continue
    if orient == "h":
        x = top * 10 + lef
        while y < boat:
            grid[x] = "X"
            x += 1
            y += 1
    else:
        x = (top * 10) + lef
        while y < boat:
            grid[x] = "X"
            x += 10
            y += 1
    time += 1
    y = 0
    print("  1 2 3 4 5 6 7 8 9 10")
    print("A " + s.join(grid[0:10]))
    print("B " + s.join(grid[10:20]))
    print("C " + s.join(grid[20:30]))
    print("D " + s.join(grid[30:40]))
    print("E " + s.join(grid[40:50]))
    print("F " + s.join(grid[50:60]))
    print("G " + s.join(grid[60:70]))
    print("H " + s.join(grid[70:80]))
    print("I " + s.join(grid[80:90]))
    print("J " + s.join(grid[90:100]))


    '''if top == A:
        top = 0
    elif top == B:
        top = 1
    elif top == C:
        top = 2
    elif top == D:
        top = 3
    elif top == E:
        top = 4
    elif top == F:
        top = 5
    elif top == G:
        top = 6
    elif top == H:
        top = 7
    elif top == I:
        top = 8
    elif top == J:
        top = 9'''
