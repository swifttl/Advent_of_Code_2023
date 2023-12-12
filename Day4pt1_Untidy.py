input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day4/input4.txt', 'r').read().splitlines()

# Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|):
## a list of winning numbers and then a list of numbers you have.
# As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear
## in the list of winning numbers. The first match makes the card worth one point and
## each match after the first doubles the point value of that card.

#Take a seat in the large pile of colorful cards. How many points are they worth in total?


def partOne():
    calSum = 0
    pointsArray = []
    for line in input:
        firstColumn = []
        winningNumbers = []
        yourNumbers = []
        match = []
        initializer = 1
        x = line.split('|')
        y = x[0]
        firstColumn.append(y[y.index(':')+2:])
        for string in firstColumn:
            WNumbers = string.split()
            for i in WNumbers:
                winningNumbers.append(int(i))
        YNumbers = x[1].split()
        for string in YNumbers:
            yourNumbers.append(int(string))
        for num in yourNumbers:
            if num in winningNumbers:
                match.append(num)
        if match == []:
            pointsArray.append(0)
        else:
            for count in range(len(match)-1):
                initializer *= 2
            pointsArray.append(initializer)
    for i in pointsArray:
        calSum += i
    print("The final tally of total points equals: ", calSum)

partOne()
