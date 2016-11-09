''''''''''''''''''''''''
'''  Assignment 1  '''
'''  "Connect 3"   '''
'''                '''
'''      by        '''
''' Catarina Silva '''
'''      and       '''
'''  Joao Araujo   '''
''''''''''''''''''''''''


def init(settings, game):
 '''Initializes the board'''
 for x in range(settings["line"]):
  game.append([])
  for y in range(settings["col"]):
   game[x].append("-")
  #game variable is presented like:
  #game[line number][column number]

def defSettings(settings,debug):
 '''Defines Settings'''
 #debug True uses default settings
 if debug == False:
  #asks player for settings
  settings["play1"] = raw_input("Player 1 name (str): ")
  settings["play1s"] = raw_input(settings["play1"]+"'s symbol (str/lenght: 1): ")
  settings["play2"] = raw_input("Player 2 name (str): ")
  settings["play2s"] = raw_input(settings["play2"]+"'s symbol (str/lenght: 1): ")
  settings["diag"] = raw_input("Diagonal win condition? (y/n): ")
  settings["line"] = int(raw_input("Number of lines (int): "))
  settings["col"] = int(raw_input("Number of collums (int): "))
 else:
  #sets settings as default + easter egg for PT nerds
  settings["play1"] = "Capitao Falcao"
  settings["play1s"] = "x"
  settings["play2"] = "General Gaivota"
  settings["play2s"] = "o"
  settings["diag"] = "y"
  settings["line"] = 4
  settings["col"] = 5

def inputcheck(settings,player,game):
 ''' Receives input and checks if it's valid '''
 crash = 0
 change = raw_input(str(player[0])+"'s turn: ")
 #while the input doesn't exist/isn't a digit/is too big/collum is full...
 while len(str(change)) == 0 or change.isdigit() == False or len(change) > len(str(settings["col"])) or game[settings["line"]-1][int(change)-1] != "-":
  #if the input is exiting, is a digit, is the correct size and there is space for it...
  if len(str(change)) != 0 and change.isdigit() == True and int(change) <= settings["col"] and game[settings["line"]-1][int(change)-1] == "-":
   pass
  else:
   #ask again for a correct input
   print "INVALID MOVE"
   change = raw_input(str(player[0])+"'s turn: ")
   #+ easter egg for nerds
   crash += 1
   if crash >= 3:
    print "\nWell, my days of not taking you seriously are certainly coming to a middle\n"
    crash = -999
 #returns change value if it is correct
 return int(change)-1

def play(settings,player,game):
 ''' Processes player's move '''

 #receives input and checks if it's valid
 change = inputcheck(settings,player,game) 

 #checks each line for an empty spot called by player and changes it
 for x in range(settings["line"]):
  if game[x][change] == "-":
   if player[0] == settings["play1"]:
    game[x][change] = settings["play1s"]
   elif player[0] == settings["play2"]:
    game[x][change] = settings["play2s"]
   break

def prt(settings,game):
 ''' Prints board '''
 for x in range(settings["line"]):
  linetoprint = []
  linetoprint.append(str((x-settings["line"])*-1))
  for y in range(settings["col"]):
   linetoprint.append(game[((x-settings["line"])*-1)-1][y])
  print "".join(linetoprint)
 colnum = [" "]
 for x in range(settings["col"]):
  colnum.append(str(x+1))
 print "".join(colnum)

def chplayer(settings,player):
 ''' Changes player '''
 if player[0] == settings["play1"]:
  player[0] = settings["play2"]
 else:
  player[0] = settings["play1"]

def winner_horizontal(settings,win,game):
 ''' Checks for winner (horizontal) '''
 #horizontal check
 #play1
 for line in range(settings["line"]):
  for col in range(settings["col"]-2):
   if game[line][col] == settings["play1s"] and game[line][col+1] == settings["play1s"] and game[line][col+2] == settings["play1s"]:
    print settings["play1"]," won the game. Congratulations! \n"
    win[0] = True
 #play2
 for line in range(settings["line"]):
  for col in range(settings["col"]-2):
   if game[line][col] == settings["play2s"] and game[line][col+1] == settings["play2s"] and game[line][col+2] == settings["play2s"]:
    print settings["play2"]," won the game. Congratulations! \n"
    win[0] = True
def winner_vertical(settings,win,game):
 ''' Checks for winner (vertical) '''
 #vertical check
 #play1
 for line in range(settings["line"]-2):
  for col in range(settings["col"]):
   if game[line][col] == settings["play1s"] and game[line+1][col] == settings["play1s"] and game[line+2][col] == settings["play1s"]:
    print settings["play1"]," won the game. Congratulations! \n"
    win[0] = True
 #play2
 for line in range(settings["line"]-2):
  for col in range(settings["col"]):
   if game[line][col] == settings["play2s"] and game[line+1][col] == settings["play2s"] and game[line+2][col] == settings["play2s"]:
    print settings["play2"]," won the game. Congratulations! \n"
    win[0] = True
def winner_diagonal1(settings,win,game):
 ''' Checks for winner (diagonal - left to right) '''
  #diagonal check
  #left to right
  #play1
 for line in range(settings["line"]-2):
  for col in range(settings["col"]-2):
   if game[line][col] == settings["play1s"] and game[line+1][col+1] == settings["play1s"] and game[line+2][col+2] == settings["play1s"]:
    print settings["play1"]," won the game. Congratulations! \n"
    win[0] = True
  #play2
 for line in range(settings["line"]-2):
  for col in range(settings["col"]-2):
   if game[line][col] == settings["play2s"] and game[line+1][col+1] == settings["play2s"] and game[line+2][col+2] == settings["play2s"]:
    print settings["play2"]," won the game. Congratulations! \n"
    win[0] = True
def winner_diagonal2(settings,win,game):
 ''' Checks for winner (diagonal - left to right) '''
 #right to left
 #play1
 for line in range(settings["line"]):
  for col in range(settings["col"]-2):
   col += 2
   if game[line][col] == settings["play1s"] and game[line+1][col-1] == settings["play1s"] and game[line+2][col-2] == settings["play1s"]:
    print settings["play1"]," won the game. Congratulations! \n"
    win[0] = True
 #play2
 for line in range(settings["line"]):
  for col in range(settings["col"]-2):
   col += 2
   if game[line][col] == settings["play2s"] and game[line+1][col-1] == settings["play2s"] and game[line+2][col-2] == settings["play2s"]:
    print settings["play2"]," won the game. Congratulations! \n"
    win[0] = True 

    
def score(settings,player,scoreboard):
 ''' Defines and presents scoreboard '''
 ''' Please ignore the apparent reversal of scoreboard positions. We can't explain it, but we fixed it '''
 if player[0] == settings["play1"]:
  scoreboard[1] += 1
 else:
  scoreboard[0] += 1
 print "\nSCOREBOARD:\n",settings["play1"]+":",scoreboard[0]," victories.\n",settings["play2"]+":",scoreboard[1]," victories.\n"

def main():
 #initializes variables
 playmore = "y"
 scoreboard = [0,0]
 while playmore == "y":
  #initializes more variables
  settings = {}
  game = []
  win = [False]

  #In defSettings, the second input makes predefined settings if True
  ''' DEBUG MODE SET HERE - set defSettings's second argument to "debug = True" for DEBUG MODE '''
  defSettings(settings,debug = False)

  #initializes the game
  init(settings,game)
  player = [settings["play1"]]
  
  #Plays the game (while no winner is found)
  while win[0] == False:
   #processes game
   play(settings,player,game)
   #prints the board
   prt(settings,game)
   #changes player
   chplayer(settings,player)
   #checks for winner
   winner_horizontal(settings,win,game)
   winner_vertical(settings,win,game)
   if settings["diag"] == "y":
    winner_diagonal1(settings,win,game)
    winner_diagonal2(settings,win,game)

  #displays score at end of game
  score(settings,player,scoreboard)
  #asks for another round
  playmore = raw_input("Do you want to play again? (y/n)\n")
  print ""
 exit()

if __name__ == "__main__":
 main()
