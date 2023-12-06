#The Elf would first like to know which games would have been possible if
#the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#What is the sum of the IDs of those games?

input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day2/input2pt1.txt', 'r').read().splitlines()

#dictionary (maybe should be list)
colors = {"red" : 12, "green" : 13, "blue" : 14}
highNumbersArray = []
IDArray = []
FailingIDArray = []

def partOne():
    IDValue = 0
    calSum = 0
    for line in input:
        for x in range(5,7):
            if line[x].isdigit():
                if line[x-1].isdigit():
                    #trash = line[x-1]
                    break
                IDValue = (int(line[x]))
                if line[x+1].isdigit():
                    #print(line[x+1])
                    tensID = (int(line[x]) * 10)
                    onesID = int(line[x + 1])
                    IDValue = (tensID + onesID)
                    #print(IDValue)
                    if line[x+2].isdigit():                         #nested loops to account for multiple digit values
                        hunsID = (int(line[x]) * 100)
                        tensID = (int(line[x+1]) * 10)
                        onesID = int(line[x + 2])
                        IDValue = (hunsID + tensID + onesID)
                        break
                else:
                    IDValue = (int(line[x]))
                    break
        IDArray.append(IDValue)
        #print(IDArray)
        for i in range(7, len(line)):                               #skips the ID indices
            if line[i].isdigit():
                if line[i-1].isdigit():
                    trash = line[i-1]
                if line[i+1].isdigit():
                    tens = (int(line[i]) * 10)
                    ones = int(line[i+1])
                    doubleDigit = (tens+ones)
                    #print(doubleDigit)
                    for key in colors:
                        if key in line[i:i+8]:
                            if doubleDigit > colors.get(key):
                                highNumbers = doubleDigit
                                highNumbersArray.append(highNumbers)
                                FailingIDArray.append(IDValue)
                                print("The Game ID:", IDValue, "has a failing number below:")
                                print(highNumbers, key)
                                break
    distinctFailingArray = list(set(FailingIDArray))
    print(FailingIDArray)
    print (distinctFailingArray)

    for i in distinctFailingArray:
        if i in IDArray:
            IDArray.remove(i)
        #print(IDArray)
        #calSum += i
    print(IDArray)
    for i in IDArray:
        #print(IDArray[i])
        calSum += i
        print(calSum)


partOne()

#IT DOES NOT DO 100S
#IT HAS BEEN SEEN GRABBING WRONG KEY (GAME 19)
# def partTwo():
#     for i in IDArray:
#         sum += i
#         print(sum)



#may be easier to get real values reading backwards to
##Save  #if line[x-2].isdigit():
                    #trash2 = line[x-2]
        #         # if line[x+2].isdigit():
        #         #     hunstens = (int(line[x+1]) * 10)
        #         #     hunsones = (int(line[x+2]))
        #         #     hunsID = (int(line[x]) * 100)
        #         #     IDValue = (hunsID+hunstens+hunsones)
        #         #     #print(IDValue)
        #         # else: