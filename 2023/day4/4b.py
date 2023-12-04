def main(value, counter):
    file1 = open('2023\day4\input.txt', 'r')
    lines = file1.readlines()
    value = 0
    for line in lines:
        startIndex = line.index(':')
        line = line[startIndex + 1:int(len(line) - 1)]
        # print(line)
        endIndex = line.index('|')

        winningNumbers = line[:endIndex].split()
        ourNumbers = line[endIndex + 1:].split()
        # print(list(set(winningNumbers).intersection(ourNumbers)))
        # print(value)
        if len(list(set(winningNumbers).intersection(ourNumbers))) > 0:
            value += 2**(len(list(set(winningNumbers).intersection(ourNumbers))) - 1)
    print(value)