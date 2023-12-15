#Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1
# Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank
# Five of a kind > Four of a kind > Full house > Three of a kind > Two pair > One pair > High card
# Want the total winnings (rank *bid (lowest score is rank 1)).
#
# Need to create a new list that orders their rank.
# (Dont think we need to separate hand and bid, this will simplify things in the future but could be problematic)
# ((the analysis of the rank will have to be done on index0 of the hand line))
# The index +1 in the rank list will be their "rank"
#
# need to take that line and multiply line[2] by the (rank.index(line)+1)
#
# May be easier to separate hands by which type i.e. all five of a kinds have a list
# from there we would need to order the list based off 1st card... 2nd card... etc
# then in a master rank list, we would append starting at high card ->5 of a kind.

input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day7/input7.txt', 'r').read().splitlines()


fiveKind = []
fourKind = []
fullHouse = []
threeKind = []
twoPair = []
onePair = []
highCard = []
finalSum = []
cardValueMap = {'J': 10, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 11, 'K': 12, 'A': 13}

def strengthFunction(string):
    val = [cardValueMap.get(i) for i in string]
    return val
def SORT(list):
    list.sort(key=lambda list:list[2])

def find_duplicates(string):
    duplicates = {}
    for letter in string:
        if string.count(letter) > 1 and letter not in duplicates:
            duplicates.update({letter:string.count(letter)})
        else:
            if string.count(letter) == 1 and letter == string[-1] and len(duplicates) == 0:
                duplicates.update({"highCard":1})
    return duplicates

def partOne():
    for line in input:
        x = line.split()
        x[1] = int(x[1])
        for i in range(0,1):
            duplicates = find_duplicates(x[i])

            for d in duplicates:
                if duplicates.get(d) == 5:
                    x.append(strengthFunction(x[0]))
                    fiveKind.append(x)
                elif duplicates.get(d) == 4:
                    x.append(strengthFunction(x[0]))
                    fourKind.append(x)
                elif len(duplicates) == 2:
                    iterd = iter(duplicates)
                    d1 = next(iterd)
                    d2 = next(iterd)
                    if duplicates.get(d2) == 3 and duplicates.get(d) ==2:
                        x.append(strengthFunction(x[0]))
                        fullHouse.append(x)
                    elif duplicates.get(d2) == 2 and duplicates.get(d) == 3:
                        x.append(strengthFunction(x[0]))
                        fullHouse.append(x)
                    if duplicates.get(d) == 2 and x not in twoPair and x not in fullHouse:
                        x.append(strengthFunction(x[0]))
                        twoPair.append(x)
                elif duplicates.get(d) == 3 and len(duplicates) == 1:
                    x.append(strengthFunction(x[0]))
                    threeKind.append(x)
                elif duplicates.get(d) == 2 and len(duplicates) == 1:
                    x.append(strengthFunction(x[0]))
                    onePair.append(x)
                elif d == "highCard":
                    x.append(strengthFunction(x[0]))
                    highCard.append(x)


    SORT(highCard)
    for i in highCard:
        finalSum.append(i)
    SORT(onePair)
    for i in onePair:
        finalSum.append(i)
    SORT(twoPair)
    for i in twoPair:
        finalSum.append(i)
    SORT(threeKind)
    for i in threeKind:
        finalSum.append(i)
    SORT(fullHouse)
    for i in fullHouse:
        finalSum.append(i)
    SORT(fourKind)
    for i in fourKind:
        finalSum.append(i)
    SORT(fiveKind)
    for i in fiveKind:
        finalSum.append(i)

    c = 1
    total = 0

    for i in finalSum:
        total+= c*i[1]
        c+=1
    print("The final total is", total)

partOne()
