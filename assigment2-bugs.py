# -*- coding: cp1252 -*-
import random
import csv

class MyGame:
    ''' The game Rock, Paper, Scissors '''
    def __init__(self):
        ''' Initializes the game '''
        pass

    def menu(self,players):
        choose = int(raw_input("Choose: "))
        if choose == 1:
            self.gameRunning = True
        elif choose == 2:
            self.gameRunning = False
            data.playersList(self,players)
        elif choose == 3:
            self.gameRunning = False
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
        while inputValid == False:
            inp = raw_input("\n1: Rock, 2: Paper, 3: Scissors? ")
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
            descriptionMove = ["TIE"]
            scoreMove = [30]
        if self.player == 1 and self.computer == 2:
            print("You lost! 0 points")
            descriptionMove = ["LOST"]
            scoreMove = [0]
        if self.player == 1 and self.computer == 3:
            print("You won! 100 points")
            descriptionMove = ["WON"]
            scoreMove = [100]

        #player with Paper
        if self.player == 2 and self.computer == 1:
            print("You won! 100 points")
            descriptionMove = ["WON"]
            scoreMove = [100]
        if self.player == 2 and self.computer == 2:
            print("Tie! 30 points")
            descriptionMove = ["TIE"]
            scoreMove = [30]
        if self.player == 2 and self.computer == 3:
            print("You lost! 0 points")
            descriptionMove = ["LOST"]
            scoreMove = [0]

        #player with Scissors
        if self.player == 3 and self.computer == 1:
            print("You lost! 0 points")
            descriptionMove = ["LOST"]
            scoreMove = [0]
        if self.player == 3 and self.computer == 2:
            print("You won! 100 points")
            descriptionMove = ["WON"]
            scoreMove = [100]
        if self.player == 3 and self.computer == 3:
            print("Tie! 30 points")
            descriptionMove = ["TIE"]
            scoreMove = [30]

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
            professionPlayer.append(row[2])

        for x in range(len(numberPlayer)):
            players[numberPlayer[x]] = namePlayer[x],professionPlayer[x]

        csv.close()

    def verifyPlayer(self,players,player,numberPlayer):
        
        ''' Receives and compares name or id player '''
        
        valid = False
        #asks for name or id
        while valid == False:
            nameOrId = raw_input("Enter your name or id: ")
            if nameOrId.isdigit() == True:
                if int(nameOrId) <= len(players) and int(nameOrId) > 0:
                    player[0] = players[nameOrId[0]][0]
                    numberPlayer[0] = int(nameOrId)
                    valid = True
            else:
                for x in range(len(players)):
                    if nameOrId == players[str(x+1)][0]:
                        player[0] = nameOrId
                        numberPlayer[0] = x+1
                        valid = True
                    
                    

    def playersList(self,players):
        ''' Print List of players '''

        for x in range(len(players)):
            print("Id. "+str(x+1)+": "+players[str(x+1)][0]+", "+players[str(x+1)][1])

    def fileScore(self,scoreMove,descriptionMove,numberPlayer):

        ''' Add results to the csv score file '''
        fileScore = open("score.csv","a")

        #scoreMove, descriptionMove e numberPlayer contem a informacao da ultima jogada.
        #altera o codigo abaixo (again, escrever em ficheiros, nao percebo bem da coisa)
        #quando acabares, retira o '#' do fileScore do main(), para correr esta parte

        for row in csv.readlines():
            row = row.rstrip("\n")
            row = row.split(",")
            numberPlayer.append(row[0])
            scoreMove.append(row[1])
            descriptionMove.append(row[2:])


        fileScore.write(numberPlayer , int(scoreMove), descriptionMove , "\n")
        scoresFile.close()

        fileScore.close()

    def highScore(self):
        ''' Read HighScores '''



def main():
    game = MyGame()
    data = MyDatabase()
    game.programRunning = True
    game.gameRunning = False
    player = [""] #current player
    scoreMove = [0]
    descriptionMove = [""]
    numberPlayer = [0]
    players = {}  #all players

    #initialization             
    data.filePlayers(players)
    print("Rock, Paper, Scissors!")
    
    while game.programRunning == True:  
        ''' Game Menu '''
        print("\n1: Play\n2: List Players\n3: List Top Score\n4: Quit\n")
        choose = int(raw_input("Choose: "))
        if choose == 1:
            #Play
            game.gameRunning = True
            data.verifyPlayer(players,player,numberPlayer)
            print("\nWelcome, "+str(player[0])+"!")
            print("Stop the game at any time by typing 'stop'")
        elif choose == 2:
            #List Players
            game.gameRunning = False
            data.playersList(players)
        elif choose == 3:
            #List Top Score
            game.gameRunning = False
        elif choose == 4:
            #Quit
            game.gameRunning = False
            game.programRunning = False
        else:
            #Invalid Input
            game.programRunning = True
            game.gameRunning = False
            print("Invalid Input\n")
            
        while game.gameRunning == True:
            ''' Game '''
            game.inputProcessing()    
            if game.gameRunning == True:
                game.gameProcessing()
                game.winning()
                #data.fileScore(scoreMove,descriptionMove,numberPlayer)
                


if __name__ == "__main__":
    main()
