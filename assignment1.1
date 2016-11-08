def init(settings, game):
 '''Initializes the board'''
 for x in range(settings["line"]):
  game.append([])
  for y in range(settings["col"]):
   game[x].append("-")

  #game[line number][collumn number]

def defSettings(settings, jump):
 '''Defines Settings'''
 settings["line"] = 4 #change line here
 settings["col"] = 5  #change columns here
 #jump False uses default settings
 if jump == True:
  #asks player for settings
  settings["play1"] = raw_input("Player 1 name: ")
  settings["play1s"] = raw_input(settings["play1"]+"'s symbol: ")
  settings["play2"] = raw_input("Player 2 name: ")
  settings["play2s"] = raw_input(settings["play2"]+"'s symbol: ")
  settings["diag"] = raw_input("Diagonal win condition? (y/n): ")
 else:
  #sets settings as default
  settings["play1"] = "Player 1"
  settings["play1s"] = "x"
  settings["play2"] = "Player 2"
  settings["play2s"] = "o"
  settings["diag"] = "n"
  
def play(settings,player,game):
 '''Changes the board / Plays the game'''
 change = -1
 while change < 0 or change >= settings["col"]:
  temp = raw_input(str(player[0])+"'s turn: ")
  if len(temp) <= len(str(settings["col"])):
   change = ord(temp)-48-1
  else:
   change = -1
   print "\nINVALID MOVE! SILLY HOOMAN\n"
   if player[0] == settings["play1"]:
    player[0] = settings["play2"]
   else:
    player[0] = settings["play1"]

 #checks if player tried to place chip over board
 if game[settings["line"]-1][change] != "-":
  print "\nINVALID MOVE\n"
  if player[0] == settings["play1"]:
   player[0] = settings["play2"]
  else:
   player[0] = settings["play1"]
 else:
  #checks each line for an empty spot called by player and changes it
  for x in range(settings["line"]):
   if game[x][change] == "-":
    if player[0] == settings["play1"]:
     game[x][change] = settings["play1s"]
    elif player[0] == settings["play2"]:
     game[x][change] = settings["play2s"]
    break

def prt(settings,game):
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
 if player[0] == settings["play1"]:
  player[0] = settings["play2"]
 else:
  player[0] = settings["play1"]

def winner(settings,win,game):
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
 if settings["diag"] == "y":
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
  #right to left
  #play1
   for line in range(settings["line"]-2):
    line = line + 2
    for col in range(settings["col"]-2):
     col = col + 2
     if game[line][col] == settings["play1s"] and game[line-1][col-1] == settings["play1s"] and game[line-2][col-2] == settings["play1s"]:
      print settings["play1"]," won the game. Congratulations! \n"
      win[0] = True
  #play2
   for line in range(settings["line"]-2):
    line = line + 2
    for col in range(settings["col"]-2):
     col = col + 2
     if game[line][col] == settings["play2s"] and game[line-1][col-1] == settings["play2s"] and game[line-2][col-2] == settings["play2s"]:
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
 playing = "y"
 scoreboard = [0,0]
 while playing == "y":
  playing = "n"
  #initializes more variables
  settings = {}
  game = []
  win = [False]

  #In defSettings second input is predefined settings (True/False)
  defSettings(settings, True)
  init(settings,game)
  #initializes yet another variable
  player = [settings["play1"]]

  while win[0] == False:
   #processes a play
   play(settings,player,game)
   #prints the board
   prt(settings,game)
   #changes player
   chplayer(settings,player)
   #checks for winner
   winner(settings,win,game)

  score(settings,player,scoreboard)
  playing = raw_input("\nDo you want to play again? (y/n)\n")
  print ""

 exit()

if __name__ == "__main__":
 main()
