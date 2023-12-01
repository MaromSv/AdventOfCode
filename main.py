Numbers = {
    "one" : 1,
    "two" : 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


numbers = ["one", "two", "three",  "four", "five", "six", "seven", "eight", "nine"]
def convertStringToRegular(A):
    for number in numbers:
        A = A.replace(number, number[0] + str(Numbers[number]) + number[-1])

    return A

def getCalForString(stringA):
    num = 0 
    nums = []
    for i in range(len(stringA)):
        if stringA[i].isnumeric():
            nums.append(stringA[i])
    
    num = int(nums[0] + nums[-1])
 

    return num



def main():
    file1 = open('Day 1\\input.txt', 'r')
    Lines = file1.readlines()
    print(Lines)
    sums = 0
    # Strips the newline character
    for line in Lines:
        line = convertStringToRegular(line) #Comment this line out to get 1a
        callVal = getCalForString(line.strip())
        sums += callVal
    print(sums)

main()


