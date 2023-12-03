def string_to_2d_array():
    file1 = open('2023\day3\input.txt', 'r')
    lines = file1.readlines()
    return [[char for char in line.strip()] for line in lines]


def symbolNearMe(table, i, j):

    try:
        if table[i+1][j] != "." and not table[i+1][j].isnumeric(): #RIGHT
            return True
    except:
        pass

    try:
        if table[i-1][j] != "." and not table[i-1][j].isnumeric(): #LEFT
            return True
    except:
        pass
    try:
        if table[i][j+1] != "." and not table[i][j+1].isnumeric():#BELLOW
            return True
    except:
        pass
    try:
        if table[i][j-1] != "." and not table[i][j-1] .isnumeric():#ABOVE
            return True
    except:
        pass
    try:    
        if table[i+1][j+1] != "." and not table[i+1][j+1].isnumeric():#Bottom-right
            return True
    except:
        pass
    try:
        if table[i+1][j-1] != "." and not table[i+1][j-1] .isnumeric():#top right
            return True
    except:
        pass
    try:
        if table[i-1][j-1] != "." and not table[i-1][j-1].isnumeric():#top left 
            return True
    except:
        pass
    try:
        if table[i-1][j+1] != "." and not table[i-1][j+1].isnumeric(): #bottom left
            return True
    except:
        pass
    return False

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

def sumOfEngineString():
    table = string_to_2d_array()
    numberIndicies = []
    for i in range(len(table[0])):
        for j in range(len(table[:][0])):
            if table[i][j].isnumeric():
                if symbolNearMe(table, i, j):
                    numberIndicies.append((i, j))
    
    numberIndiciesFixed = []
    for index in range(len(numberIndicies)):
        index = numberIndicies[index]
        indexi = index[0]
        indexj = index[1]
        if (indexi, indexj-1) in numberIndicies:
            pass
        else:
            numberIndiciesFixed.append(index)

    numbers = []
    for index in numberIndiciesFixed:
        # print(table[index[1]][index[0]])
        num = numberAssociatedToIndex(table, index[0], index[1])
        numbers.append(num)

    print(sum(numbers))

sumOfEngineString()