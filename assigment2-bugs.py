import random
import csv

class MyGame:
    ''' The game Rock, Paper, Scissors '''
    def __init__(self):
        ''' Initializes the game '''
        pass
    
    def menu(self):
        choose = int(raw_input("Choose: "))
        if choose >= 1 and choose <= 3:
            self.gameRunning = True
        elif choose == 4:
            self.gameRunning = False
            self.programRunning = False
        else:
            self.programRunning = True
            self.gameRunning = False
            print("Invalid Input\n")
        
    def inputProcessing(self):
        ''' Processes input '''
        inputValid = False
        print("\nStop the game at any time by typing 'stop'\n")
        while inputValid == False:
            inp = raw_input("1: Rock, 2: Paper, 3: Scissors? ")
            if inp.isdigit() == True and int(inp) >= 1 and int(inp) <= 3 or inp == "stop":
                inputValid = True
            else:
                print("Invalid Input\n")
        if inp == "stop":
            self.gameRunning = False
        else:
            self.player = int(inp)


    def gameProcessing(self):
        ''' Processes game '''
        #prints player's choice
        actions = {"1": "Rock","2": "Paper","3": "Scissors"}
        print("Player: "+actions[str(self.player)])

        #processes computer's choice
        self.computer = random.randint(1,3)
        print("Computer: "+actions[str(self.computer)])
        
    
    def winning(self):
        ''' Looks for a winner '''
        #player with Rock
        if self.player == 1 and self.computer == 1:
            print("Tie! 30 points")
        if self.player == 1 and self.computer == 2:
            print("You lost! 0 points")
        if self.player == 1 and self.computer == 3:
            print("You won! 100 points")

        #player with Paper
        if self.player == 2 and self.computer == 1:
            print("You won! 100 points")
        if self.player == 2 and self.computer == 2:
            print("Tie! 30 points")
        if self.player == 2 and self.computer == 3:
            print("You lost! 0 points")

        #player with Scissors
        if self.player == 3 and self.computer == 1:
            print("You lost! 0 points")
        if self.player == 3 and self.computer == 2:
            print("You won! 100 points")
        if self.player == 3 and self.computer == 3:
            print("Tie! 30 points")

class MyDatabase:
    

    def filePlayers(self,players):
    
        ''' Reads csv players file '''
        csv = open("players.csv","r")
        numberPlayer = []
        namePlayer = []
        professionPlayer = []
        
        for row in csv.readlines():
            row = row.rstrip("\n")
            row = row.split(",")
            numberPlayer.append(row[0])
            namePlayer.append(row[1])
            professionPlayer.append(row[2:])

        for x in range(len(numberPlayer)):
            players[numberPlayer[x]] = namePlayer[x]

    
        csv.close()

    def verifyPlayer(players):
        
        ''' Receives and compares name or id player '''

        #ask for name
        nameOrId = raw_input("Enter your name or id:")

        if nameOrId == numberPlayer[] or nameOrId == namePlayer[] 
            return True
        else:
            return False
            print("Player not define. Try again")

    def playersList(self,players):
    
        ''' Print List of players from cvs file '''
        readList = open("players.csv","r")
    
        
        for row in readList:
           print (row)
    
        readList.close()


    def fileScore(score):

        ''' Add results to the csv score file '''
        fileScore = open("score.csv","a")

        numberPlayer = []
        scoreMove = []
        descriptionMove = []

        for row in csv.readlines():
            row = row.rstrip("\n")
            row = row.split(",")
            numberPlayer.append(row[0])
            scoreMove.append(row[1])
            descriptionMove.append(row[2:])


        fileScore.write(numberPlayer , int(scoreMove), descriptionMove "\n")
        scoresFile.close()

        fileScore.close()

    def highScore(score):
        ''' Read HighScores '''




def main():
    game = MyGame()
    data = MyDatabase()
    game.programRunning = True
    game.gameRunning = False
    players = {}
    score = {}
    
                    
    print("Rock, Paper, Scissors!\n\n1: Play\n2: List Players\n3: List Top Score\n4: Quit\n")
    while game.programRunning == True:
        game.menu()
        while game.gameRunning == True:
            data.filePlayers()
            data.verifyPlayer()
            game.inputProcessing()
            if game.gameRunning == True:
                game.gameProcessing()
                game.winning()
                data.fileScore()
                data.playersList()
                


if __name__ == "__main__":
    main()