'''
ToDO

Player variable doesn't change
'''

print "\n--------------------------------------"
print "---------Welcome to Connect 4---------"
print "Type 'play' to play or 'exit' to leave\n"
state = raw_input()
#to exit:
if state == "exit":
    exit()

#global variables
global game
game = []
global line
line = 4 #import
global col
col = 5  #import
global play1
play1 = "a"
global play2
play2 = "b"
global play1s
play1s = "x"
global play2s
play2s = "o"
global player
player = play1
global win
win = False
global rule #import
rule = False

def play():
    ''' Initializes the game '''
    global player
    global play1
    global play2
    global game
    global win

    game = [] #clears the board
    
    #import from text file - player name/winning cond. (0/1)/tamanho da board
    #player info:
    play1 = "" #import
    play2 = "" #import
    if play1 == "" or play2 == "":              #asks player name and symbol
        play1 = raw_input("Player 1 name: ")
        play2 = raw_input("Player 2 name: ")
    play1s = raw_input("Player 1 symbol: ")
    play2s = raw_input("Player 2 symbol: ")

    player = play1 #starts with player 1
        
    #initialize board
    for x in range(line*col):
        game.append("-")
        
def change():
    ''' Processes the game '''   
    global player
    global play1
    global play2
    global play1s
    global play2s
    global game

    #asks move of player
    change = (int(raw_input(str(player)+"'s turn: ")))-1

    #checks each line to see if position called by player is empty (or "-")
    if game[(line*col-col)+change] == "-":
        for x in range(0,line):
            if game[(x*col)+change] == "-":
                if player == play1:
                    game[(x*col)+change] = play1s
                    chplayer()
                    break
                elif player == play2:
                    game[(x*col)+change] = play2s
                    chplayer()
                    break
    else:
        print "\nINVALID MOVE"
                
def chplayer():
    ''' Switches players'''

    global player
    global play1
    global play2

    if player == play1:
        player = play2
    else:
        player = play1

def prt():
    ''' Prints board to console '''
    turn = col
    print ""
    for x in range(0,line):
        toprt = ""
        for y in range(0,col):
            toprt = toprt+game[(line*col)-turn+y]
        turn += col
        print toprt

def wingame():
    ''' Looks for a winner '''
    global game
    global win
    global play1
    global play2
    global play1s
    global play2s
    global rule

    #horizontal check
    for x in range(0,line*col):
            #did play1 win the game?
            if game[x] == play1s:
                if game[x+1] == play1s and x+1%col != 0:
                    if game[x+2] == play1s and x+2%col != 0:
                        if rule == True and game[x+3] == play1s and x+3%col != 0:
                            print play1," won the game. Congratulatioins! \n"
                            win = True
                        print play1," won the game. Congratulations! \n"
                        win = True

            #did play2 win the game?
            if game[x] == play2s:
                if game[x+1] == play2s and x+1%col != 0:
                    if game[x+2] == play2s and x+2%col != 0:
                        if rule == True and game[x+3] == play2s and x+3%col != 0:
                            print play2," won the game. Congratulatioins! \n"
                            win = True
                        print play2," won the game. Congratulations! \n"
                        win = True
    #vertical check
    for x in range(0,line*col):
            #did play1 win the game?
            if game[x] == play1s:
                if game[x+col] == play1s:
                    if game[x+col*2] == play1s
                        if rule == True and game[x+col*3] == play1s:
                            print play1," won the game. Congratulatioins! \n"
                            win = True
                        print play1," won the game. Congratulations! \n"
                        win = True

            #did play2 win the game?
            if game[x] == play2s:
                if game[x+col] == play2s:
                    if game[x+col*2] == play2s:
                        if rule == True and game[x+col*3] == play2s:
                            print play2," won the game. Congratulatioins! \n"
                            win = True
                        print play2," won the game. Congratulations! \n"
                        win = True
    #diagonal check
    #maybe something like game[x] then game[x+col+1] and so on, repeating with game[x] then game[x+col-1]    
        

def main():
    global win
    play()
    while win == False:
        change()
        prt()
        wingame()
    if win == True:
        ask = raw_input("Do you want to play again? (y/n)\n")
        if ask == "y":
            win = False
            main()
        elif ask == "n":
            exit()

if state == "play":
    main()
