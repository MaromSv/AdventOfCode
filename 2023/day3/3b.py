import numpy as np
def string_to_2d_array():
    file1 = open('2023\day3\input.txt', 'r')
    lines = file1.readlines()
    return np.array([[char for char in line.strip()] for line in lines])

def numberAssociatedToIndex(table, i, j):
    leftj = j

    try:
        while table[i][leftj].isnumeric():
            leftj -= 1
    except:
        pass
    numberStart = leftj + 1

    rightj = j
    try:
        while table[i][rightj].isnumeric():
            rightj += 1
    except:
        pass
    numberEnd = rightj -1
    
    numberArr = table[i][numberStart:numberEnd + 1]
    # print(numberArr)
    number = "" 
    for i in numberArr:
        number += i

    return int(number) 


def getGearRatio(table, i, j):
    numberIndiciesNearMe = []
    numbersNearMe = 0
    try:
        if table[i+1][j].isnumeric(): #RIGHT
            numbersNearMe+=1
            numberIndiciesNearMe.append((i+1, j))
    except:
        pass

    try:
        if table[i-1][j].isnumeric(): #LEFT
            numbersNearMe+=1
            numberIndiciesNearMe.append((i-1, j))
    except:
        pass
    try:
        if table[i][j+1].isnumeric():#BELLOW
            numbersNearMe+=1
            numberIndiciesNearMe.append((i, j+1))
    except:
        pass
    try:
        if table[i][j-1].isnumeric():#ABOVE
            numbersNearMe+=1
            numberIndiciesNearMe.append((i, j-1))
    except:
        pass
    try:    
        if table[i+1][j+1].isnumeric():#Bottom-right
            numbersNearMe+=1
            numberIndiciesNearMe.append((i+1, j+1))
    except:
        pass
    try:
        if table[i+1][j-1].isnumeric():#top right
            numbersNearMe+=1
            numberIndiciesNearMe.append((i+1, j-1))
    except:
        pass
    try:
        if table[i-1][j-1].isnumeric():#top left 
            numbersNearMe+=1
            numberIndiciesNearMe.append((i-1, j-1))
    except:
        pass
    try:
        if table[i-1][j+1].isnumeric(): #bottom left
            numbersNearMe+=1
            numberIndiciesNearMe.append((i-1, j+1))
    except:
        pass

 
    numbers = []
    # numberIndiciesNearMe = list(dict.fromkeys(numberIndiciesNearMe))
    for index in numberIndiciesNearMe:
        num = numberAssociatedToIndex(table, index[0], index[1])
       
        numbers.append(num)
    
    numbers = list(dict.fromkeys(numbers))
    print(numbers)
    if len(numbers) == 2:
        return numbers[0]*numbers[1] #Gear Ratio
    else:
        return 0



def findGearRatioSum():
    table = string_to_2d_array()
    x = np.where(table == "*")
    ratios = []
    for i in range(len(x[0])):
        ratio = getGearRatio(table, x[0][i],x[1][i])
        ratios.append(ratio)
    # print(ratios)
    print(sum(ratios))
findGearRatioSum()