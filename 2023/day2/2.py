

colors = ["red", "green", "blue"]

possibleGames = []

def getGameID(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i: j].isnumeric() and A[j] == ':' and A[i-1].isspace():
                gameID = A[i: j]
                return gameID
    return None


def gamePossible(A):
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    Red = 0
    Blue = 0
    Green = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
           if A[i: j].isnumeric() and A[j].isspace() and A[i-1].isspace():
            #    print(A[i: j])
               if A[j + 1] == 'r':
                    # maxRed -= int(A[i: j])
                    # print(maxRed)
                    Red += int(A[i: j])
               elif A[j + 1] == 'g':
                    # maxGreen -= int(A[i: j])
                    # print(maxGreen)
                    Green += int(A[i: j])
               elif A[j + 1] == 'b':
                    # maxBlue -= int(A[i: j])
                    # print(maxBlue)
                    Blue += int(A[i: j])
    return Red, Green, Blue
                   
    # if maxBlue < 0 or maxRed < 0 or maxGreen < 0:
    #     return False
    # return True



def setOfGamesPossible(A):
    # setPossible = True
    subStrings = A.split(';')
    reds = []
    greens = []
    blues = []
    for i in subStrings:
        red, green, blue = gamePossible(i)
        reds.append(red)
        greens.append(green)
        blues.append(blue)


    return max(reds), max(greens), max(blues)

        # if gamePossible(i) == False:
        #     setPossible = False
        # else:
        #     pass


    # return setPossible



def main():
    file1 = open('2023\day2\input.txt', 'r')
    Lines = file1.readlines()
    gameRequirements =[]
    for line in Lines:
        # if setOfGamesPossible(line):
        #     possibleGames.append(int(getGameID(line)))
        red, green, blue = setOfGamesPossible(line)
        power = red*blue*green
        gameRequirements.append(power)

    print(gameRequirements)
    print(sum(gameRequirements))

main()






A ="Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

# print(A.find("blue"))
# A = A.replace("blue", "done", 1)
# print(A.find("blue"))

print(gamePossible(A))