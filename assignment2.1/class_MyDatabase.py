import csv
class MyDatabase
	
	def filePlayers(players):

		 ''' ask for name '''
    	name = raw_input("Enter your name or id:")
  
    ''' Reads csv players file '''
    csv = open("players.csv","r")
    numberPlayer = []
    namePlayer = []
    professionPlayer = []
    for line in csv.readlines():
        line = line.rstrip("\n")
        line = line.split(",")
        numberPlayer.append(line[0])
        namePlayer.append(line[1:])
        professionPlayer.append(line[2:])

    for x in range(len(numberPlayer)):
        players[numberPlayer[x]] = namePlayer[x]

    csv.close()


    def fileScore(score):

    ''' Add results to the csv score file '''
    csv = open("score.csv","a")

    numberPlayer = []
    scoreMove = []
    descriptionMove = []

    for line in csv.readlines():
        line = line.rstrip("\n")
        line = line.split(",")
        numberPlayer.append(line[0])
        scoreMove.append(line[1:])
        descriptionMove.append(line[2:])

    csv.close()


    def main():
    #initializes variables (reads file)
    players = {}
    score = {}


    if __name__=="__main__":
    main()
