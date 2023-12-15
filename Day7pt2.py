#Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1

#J is now joker (assign map value of 0) This shouldnt affect stregnth scoring and sorting
#most of the new work will have to be done in the appeding based on dupes
input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day7/input7.txt', 'r').read().splitlines()


fiveKind = []
fourKind = []
fullHouse = []
threeKind = []
twoPair = []
onePair = []
highCard = []
finalSum = []
cardValueMap = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 11, 'K': 12, 'A': 13}

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

def find_jokers(string):
    for letter in range(len(string)):
        if string[letter] == "J":
            return string[letter]

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
                    if find_jokers(x[0]) == "J" and d != "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                        x.append(strengthFunction(x[0]))
                        fiveKind.append(x)
                    elif d =="J":
                        x.append(strengthFunction(x[0]))
                        fiveKind.append(x)
                    else:
                        if x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                            x.append(strengthFunction(x[0]))
                            fourKind.append(x)
                elif len(duplicates) == 2:
                    iterd = iter(duplicates)
                    d1 = next(iterd)
                    d2 = next(iterd)
                    if duplicates.get(d) == 2 and duplicates.get(d2) == 3:
                        if find_jokers(x[0]) == "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                            x.append(strengthFunction(x[0]))
                            fiveKind.append(x)
                        else:
                            if find_jokers(x[0]) != "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                                x.append(strengthFunction(x[0]))
                                fullHouse.append(x)
                    elif duplicates.get(d) == 3 and duplicates.get(d2) == 2:
                        if find_jokers(x[0]) == "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                            x.append(strengthFunction(x[0]))
                            fiveKind.append(x)
                        else:
                            if find_jokers(x[0]) != "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                                x.append(strengthFunction(x[0]))
                                fullHouse.append(x)
                    elif duplicates.get(d) == 2 and duplicates.get(d2) ==2 and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                        if d == "J" or d2 == "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                            x.append(strengthFunction(x[0]))
                            fourKind.append(x)
                        elif d != "J" and d2 != "J" and find_jokers(x[0]) =="J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                            x.append(strengthFunction(x[0]))
                            fullHouse.append(x)
                        else:
                            if d != "J" and d2 != "J" and find_jokers(x[0]) != "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                                x.append(strengthFunction(x[0]))
                                twoPair.append(x)
                elif duplicates.get(d) == 3 and len(duplicates) == 1:
                    if find_jokers(x[0]) == "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                        x.append(strengthFunction(x[0]))
                        fourKind.append(x)
                    elif d == "J" and x not in twoPair and x not in threeKind and x not in fullHouse and x not in fourKind and x not in fiveKind:
                        x.append(strengthFunction(x[0]))
                        threeKind.append(x)
                    else:
                        if find_jokers(x[0]) != "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                            x.append(strengthFunction(x[0]))
                            threeKind.append(x)
                elif duplicates.get(d) == 2 and len(duplicates) == 1:
                    if find_jokers(x[0]) == "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                        x.append(strengthFunction(x[0]))
                        threeKind.append(x)

                    else:
                        x.append(strengthFunction(x[0]))
                        onePair.append(x)
                elif d == "highCard":
                    if find_jokers(x[0]) == "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
                        x.append(strengthFunction(x[0]))
                        onePair.append(x)
                    else:
                        if find_jokers(x[0]) != "J" and x not in twoPair and x not in threeKind and x not in fullHouse\
                            and x not in fourKind and x not in fiveKind:
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
