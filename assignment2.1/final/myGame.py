import random
from myDatabase import MyDatabase

class MyGame:
    ''' The game Rock, Paper, Scissors '''

    def __init__(self):
        self.data = MyDatabase()
            
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
            self.data.player = int(inp)


    def gameProcessing(self):
        ''' Processes game '''
        
        #prints player's choice
        actions = {"1": "Rock","2": "Paper","3": "Scissors"}
        print("Player: "+actions[str(self.data.player)])

        #processes computer's choice
        self.computer = random.randint(1,3)
        print("Computer: "+actions[str(self.computer)])
        
    
    def winning(self):
        ''' Looks for a winner '''
        
        #player with Rock
        if self.data.player == 1 and self.computer == 1:
            print("Tie! 30 points")
            self.data.descriptionMove = "TIE"
            self.data.scoreMove = 30
        if self.data.player == 1 and self.computer == 2:
            print("You lost! 0 points")
            self.data.descriptionMove = "LOST"
            self.data.scoreMove = 0
        if self.data.player == 1 and self.computer == 3:
            print("You won! 100 points")
            self.data.descriptionMove = "WON"
            self.data.scoreMove = 100

        #player with Paper
        if self.data.player == 2 and self.computer == 1:
            print("You won! 100 points")
            self.data.descriptionMove = "WON"
            self.data.scoreMove = 100
        if self.data.player == 2 and self.computer == 2:
            print("Tie! 30 points")
            self.data.descriptionMove = "TIE"
            self.data.scoreMove = 30
        if self.data.player == 2 and self.computer == 3:
            print("You lost! 0 points")
            self.data.descriptionMove = "LOST"
            self.data.scoreMove = 0

        #player with Scissors
        if self.data.player == 3 and self.computer == 1:
            print("You lost! 0 points")
            self.data.descriptionMove = "LOST"
            self.data.scoreMove = 0
        if self.data.player == 3 and self.computer == 2:
            print("You won! 100 points")
            self.data.descriptionMove = "WON"
            self.data.scoreMove = 100
        if self.data.player == 3 and self.computer == 3:
            print("Tie! 30 points")
            self.data.descriptionMove = "TIE"
            self.data.scoreMove = 30

    def start(self):

        #initialization
        self.data.players = {}  #all players
        self.data.player = "" #current player
        self.data.numberPlayer = 0 #number of current player
        self.data.scoreMove = 0 #last move's score
        self.data.descriptionMove = "" #last move's description
                
        self.data.filePlayers()
        self.programRunning = True
        self.gameRunning = False
        print("Rock, Paper, Scissors!")

        #while user hasn't 'quit'
        while self.programRunning == True:  
            ''' Game Menu '''
            print("\n1: Play\n2: List Players\n3: List Top Score\n4: Quit\n")
            choose = raw_input("Choose: ")
            if choose == "1":
                #Play
                self.gameRunning = True
                self.data.verifyPlayer()
                print("\nWelcome, "+str(self.data.player)+"!")
                print("Stop the game at any time by typing 'stop'")
            elif choose == "2":
                #List Players
                self.gameRunning = False
                self.data.playersList()
            elif choose == "3":
                #List Top Score
                self.gameRunning = False
                self.data.highScore()
            elif choose == "4":
                #Quit
                self.gameRunning = False
                self.programRunning = False
            else:
                #Invalid Input
                self.programRunning = True
                self.gameRunning = False
                print("Invalid Input\n")

            #while user plays and doesn't 'stop'
            while self.gameRunning == True:
                ''' Game '''
                self.inputProcessing()    
                if self.gameRunning == True:
                    self.gameProcessing()
                    self.winning()
                    self.data.fileScore()

def main():
    game = MyGame()
    game.start()


if __name__ == "__main__":
    main()
