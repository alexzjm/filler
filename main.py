import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

gameboard = [[0 for x in range(8)] for y in range(7)]
colour = {1:"\u001b[31m██", 2:"\u001b[32m██", 3:"\u001b[33m██", 4:"\u001b[34m██", 5:"\u001b[35m██", 6:"\u001b[37m██"}

revcolour = {"\u001b[31m██":1, "\u001b[32m██":2, "\u001b[33m██":3, "\u001b[34m██":4, "\u001b[35m██":5, "\u001b[37m██":6}

def assigncolor(x,y):
  clear = True
  c = colour[random.randint(1,6)]
  if x != 0:
    if c == gameboard[x-1][y]:
      assigncolor(x,y)
      clear = False
  if y != 0:
    if c == gameboard[x][y-1]:
      assigncolor(x,y)
      clear = False
  if clear:
    gameboard[x][y] = c
    
def printboard():
  lin = ""
  for x in gameboard:
    for y in x:
      lin += (y+y)
    print(lin)
    print(lin)
    lin = ""
  
for x in range(7):
  for y in range(8):
    assigncolor(x,y)
while gameboard[6][0] == gameboard[0][7]:
  assigncolor(0,7)

#--- dont touch the above
player1 = [[False for x in range(8)] for y in range(7)]
colour1 = gameboard[6][0]
player1[6][0] = True
player2 = [[False for x in range(8)] for y in range(7)]
colour2 = gameboard[0][7]
player2[0][7] = True
master = [[False for x in range(8)] for y in range(7)]
master[6][0] = True
master[0][7] = True

colourlist = [True for x in range(6)]
colourlist[revcolour[colour1]-1] = False
colourlist[revcolour[colour2]-1] = False

def getscore(player):
  s = 0
  for x in player:
    for y in x:
      if y:
        s += 1
  return s
  
def printchoice():
  choice = "\u001b[0mThe following are legal moves: "
  for x in range(len(colourlist)):
    if colourlist[x]:
      choice += (colour[x+1][:-2] + str(x+1) + " ")
  print(choice)

def filled():
  for x in master:
    for y in x:
      if not y:
        return False
  return True

def check(x, y, player, colour):
  if x != 0:
    if player[x-1][y] == False:
      if gameboard[x-1][y] == colour:
        player[x-1][y] = True
        master[x-1][y] = True
  if x != 6:
    if player[x+1][y] == False:
      if gameboard[x+1][y] == colour:
        player[x+1][y] = True
        master[x+1][y] = True
  if y != 0:
    if player[x][y-1] == False:
      if gameboard[x][y-1] == colour:
        player[x][y-1] = True
        master[x][y-1] = True
  if y != 7:
    if player[x][y+1] == False:
      if gameboard[x][y+1] == colour:
        player[x][y+1] = True
        master[x][y+1] = True

print("\u001b[0m" + str(getscore(player1)) + "   vs   " + str(getscore(player2)))
printboard()
printchoice()

while not filled():
  #player1
  colourlist[revcolour[colour1]-1] = True
  temp = int(input("\u001b[00mPlayer 1: "))
  colour1 = colour[temp]
  colourlist[revcolour[colour1]-1] = False
  for x in range(7):
    for y in range(8):
      if player1[x][y]:
        gameboard[x][y] = colour1
        check(x, y, player1, colour1)
  cls()
  print("\u001b[0m" + str(getscore(player1)) + "   vs   " + str(getscore(player2)))
  printboard()
  printchoice()
  #player2
  colourlist[revcolour[colour2]-1] = True
  temp = int(input("\u001b[00mPlayer 2: "))
  colour2 = colour[temp]
  colourlist[revcolour[colour2]-1] = False
  for x in range(7):
    for y in range(8):
      if player2[x][y]:
        gameboard[x][y] = colour2
        check(x, y, player2, colour2)
  cls()
  print("\u001b[0m" + str(getscore(player1)) + "   vs   " + str(getscore(player2)))
  printboard()
  printchoice()

if getscore(player1) > getscore(player2):
  print("\u001b[0mPlayer 1 wins!")
elif getscore(player1) < getscore(player2):
  print("\u001b[0mPlayer 2 wins!")
else:
  print("\u001b[0mTie!")
