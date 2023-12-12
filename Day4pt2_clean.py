input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day4/input4.txt', 'r').read().splitlines()
#structure: goal is to find how many total cards should be read.
# Total cards will each each original + each copy of a line
# each copy of a line is earned by how many matching numbers were found via preious lines
# each card should have a list that is added to via the matches prior

def partTwo():

    lineNum = 0                                         #needed a reference for each card
    calSum = 0                                          #total card sum
    readCounter = [*(range(1,203))]                     #create a list for the num of cards that with a min of 1 (orig card)
    for u in range(len(readCounter)):
        readCounter[u] = 1
    for line in input:
        firstColumn = []                                #stolen from partOne, as we still needed to know num of matching nums
        winningNumbers = []
        yourNumbers = []
        match = []
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
        cardsCopied = len(match)                        #create a variable to know how many cards ahead will be copied
        lineNum += 1
        try:
            for i in range(0,readCounter[lineNum-1]):   #this is a loop to repeat adding copies the amount of times that the card# exists (if card 2 already exists twice, it must make a proceeding copy twice)
                for i in range(lineNum, lineNum+cardsCopied):   #this loop is to add 1 to the total number of copies of each line; from current line to however many lines after based on the number of matches
                    readCounter[i]+=1
        except IndexError:
            pass
    for i in readCounter:
        calSum+=i
    print("Total number of cards to be played:", calSum)
partTwo()