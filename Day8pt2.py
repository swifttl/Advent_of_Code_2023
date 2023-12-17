# s you follow each left/right instruction, use that instruction to simultaneously
# navigate away from both nodes you're currently on.
# Repeat this process until all of the nodes you're currently on end with Z.
# Simultaneously start on every node that ends with A.
# How many steps does it take before you're only on nodes that end with Z?

#still want to read first line as directions,
#we need to grab all "LRArray[0]" that end with A. maybe the working for loop should be a function
#to be called at the same time for each LRARRY[0] that ends with A
# those "finish" values can be appended to a list; when list all ends with "z" functino stops
#need to make them all go, so maybe for i in starter
#still need to store that answer i.e. 11B as final. that still needs to be called back
#for i in starters: go through index of instructions and append Zstorage.


input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day8/input8', 'r').read().splitlines()
directions = input[0]
leftRightArray = []
startersArray = []

# starter = leftRightArray[0][0][2] == 'A'  ###itll use these!!!!!!!!!!!!!!!!!!!!
# finish = leftRightArray[0][1][2] == 'Z'
# finish = leftRightArray[0][2][2] == 'Z'

# print(len(set(test)))
def zCounter(list):
    checker = list.count('Z')
    return checker

def locator(string):
    zStorage = []
    steps = 0
    indexReplacer = 0
    finish = "placeholder"
    while finish != 5:
        for instruction in string:
            zStorage = []
            if steps == 0:
                if instruction == "L":
                    for i in startersArray:
                        for l in leftRightArray:
                            if i == l[0]:
                                # print(i)
                                storeL = leftRightArray.index(l)
                        zStorage.append(leftRightArray[storeL][1][2])
                        startersArray[startersArray.index(i)] = leftRightArray[storeL][1]
                        # print(zStorage)
                    finish = zCounter(zStorage)
                    # print(startersArray)
                    # print(finish)
                    steps+=1
                    print("Step", steps)
            else:
                if instruction == "R":
                    for i in startersArray:
                        # print(i)
                        for l in leftRightArray:
                            if i == l[0]:
                                # print(i)
                                storeL = leftRightArray.index(l)
                        zStorage.append(leftRightArray[storeL][2][2])
                        startersArray[startersArray.index(i)] = leftRightArray[storeL][2]
                        # print(zStorage)
                    finish = zCounter(zStorage)
                    # print(startersArray)
                    # print(finish)
                    steps += 1
                    print("Step", steps)
                elif instruction == "L":
                    for i in startersArray:
                        for l in leftRightArray:
                            if i == l[0]:
                                # print(i)
                                storeL = leftRightArray.index(l)
                        zStorage.append(leftRightArray[storeL][1][2])
                        startersArray[startersArray.index(i)] = leftRightArray[storeL][1]
                        # print(zStorage)
                    finish = zCounter(zStorage)
                    # print(startersArray)
                    # print(finish)
                    steps += 1
                    print("Step", steps)
    print("The total number of steps is", steps)

# def locator(string):
#     steps = 0
#     dCounter = 0
#     finish = "placeholder"
#     # while finish != 'Z':
#     for i in startersArray:
#         print(directions[0])
#         print(i[0])
#         if steps == 0:
#             if directions[dCounter] == "R":
#                 for l in leftRightArray:
#                     if i == l[0]:
#                         storeL = leftRightArray.index(l)
#                 finish = leftRightArray[storeL][2]
#                 print(finish)
#                 steps += 1
#             elif directions[dCounter] == "L":
#                 for l in leftRightArray:
#                     if i == l[0]:
#                         print(i)
#                         storeL = leftRightArray.index(l)
#                 finish = leftRightArray[storeL][1]
#                 print(finish)
#                 steps += 1
# # #         else:
# #         if directions[dCounter] == "R":
# #             for i in leftRightArray:
# #                 if i[0] == finish:
# #                     storeI = leftRightArray.index(i)
# #             finish = leftRightArray[storeI][2]
# #             steps += 1
# #         else:
# #             if directions[dCounter] == "L":
# #                 for i in leftRightArray:
# #                     # print(i[0])
# #                     if i[0] == finish:
# #                         print("found ya boi")
# #                         storeI = leftRightArray.index(i)
# #                 finish = leftRightArray[storeI][1]
# #                 steps += 1
#     # print("The total number of steps is", steps)

def partOne():
    for line in input[2:]:
        x = line.split("=")
        for i in x:
            leftRight = x[1].replace('(','').replace(')','').replace(',', '').strip().split()
        leftRight.insert(0, x[0].strip())
        leftRightArray.append(leftRight)
        # print(leftRight)
        for i in leftRight:
            # print(i)
            if i[-1] == "A":
                startersArray.append(i)
                # print("A here")



partOne()
print(leftRightArray)
print(startersArray)
locator(directions)
# print(leftRightArray[0][0][2])###THIS IS THE MEAL TICKET

#Bet money this works but cant wait for 800 billion iterations.
#Taking the star and will return to find a better way