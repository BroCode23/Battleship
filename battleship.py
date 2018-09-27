print("BATTLESHIP")
grid =  ['O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O',
         'O','O','O','O','O','O','O','O','O','O']
boat = 5
print("battleship (5 pegs)")
orient = input("what orientation would you like your ship? (v/h)")
orient = orient[0].lower()
if orient == "v":
  while not 0 <= btm <= (10 - boat):
    btm = int(input("Space from bottom?"))
    btm = 10 - (boat + (btm % 10))
  while not 0 <= lef <= 9:
    lef = int(input("Space from left?"))
    lef = lef % 10
else:
  while not 0 <= btm <= 9:
    btm = int(input("Space from bottom?"))
    btm = 10 - (1 + (btm % 10))
  while not 0 <= lef <= (10 - boat):
    lef = int(input("Space from left?"))
    lef = lef % 10
if orient == "h":
  grid[

  

□■●○
