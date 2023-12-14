input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day5/input5.txt', 'r').read().splitlines()
##Each line within a map contains three numbers:
# the destination range start, the source range start, and the range length.
## I WASTED DAYS BECAUSE I DIDNT UNDERSTAND THE PROMPT. IT IS BETTER TO KEEP EACH LINE, RATHER THAT SPLITTING LINE BY\
#DEST, SOURCE, RANGE. LORD HELP ME
def num_there(s):
    return any(i.isdigit() for i in s)

def partOne():
    seedsArray = []
    seedSoilArray = []
    soilFertArray = []
    fertWaterArray = []
    waterLightArray = []
    lightTempArray = []
    tempHumArray = []
    humLocArray = []
    destinationArray = []
    #sourceArray = []
    rangeArray = []

    dictMap = {"seeds:":seedsArray,"seed-to-soil":[],"soil-to-fertilizer":[],\
               "fertilizer-to-water":[], "water-to-light":[],"light-to-temperature":[],\
               "temperature-to-humidity":[],"humidity-to-location":[]}

    try:
        print(input)
        newInput = []
        # #print(input)
        for i in  range(len(input)):
            newLines = input[i].strip().split()
            #print(newLines)
            for i in newLines:
                if i == 'map:':
                    newLines.remove('map:')
            if newLines != []:
                newInput.append(newLines)
        # print(newInput)
        for i in range(len(newInput)):
            line = newInput[i]
            #print(line)
            if 'seeds:' in line:
                for s in range(1,len(line)):
                    #print(int(line[s]))

                    seedsArray.append(int(line[s]))
            #print("LOOK", seedsArray)
            if i != 0:
                for key in dictMap:
                    c=0
                    if key in line:
                        #print(key)
                        #print(i)
                        for find in newInput[i+1:]:
                            if num_there(find):
                                numFound = [int(x) for x in find]
                                #print("numfound!",numFound)
        #                         #print(dictMap.get(key)[1])
                                dictMap.get(key).append(numFound)
        #                         #dictMap.get(key)[1].append(find[1])
        #                         #dictMap.get(key)[2].append(find[2])
                            else:
                                break
    except IndexError:
        pass
    # print(dictMap.get("seed-to-soil"))
    # print(dictMap.get("soil-to-fertilizer"))
    # print(dictMap.get("fertilizer-to-water"))
    # print(dictMap.get("water-to-light"))
    # print(dictMap.get("light-to-temperature"))
    # print(dictMap.get("temperature-to-humidity"))
    # print(dictMap.get("humidity-to-location"))
    #print(seedsArray)
    for i in seedsArray:
        print(i)
        sourceRangeList = []
        for l in dictMap.get("seed-to-soil"):
            sourceRange = [*range(l[1], l[1] + l[2], 1)]
            sourceRangeList.append(sourceRange)
        for z in sourceRangeList:
            if i in z:
                print(i)
                whichIndextoRun = sourceRangeList.index(z)
                whichLinetoRun = dictMap.get("seed-to-soil")[whichIndextoRun]
                calcDiff = (whichLinetoRun[0] - whichLinetoRun[1])
                seedsArray[seedsArray.index(i)] = i + calcDiff
    print(seedsArray)
    for i in seedsArray:
        sourceRangeList = []
        for l in dictMap.get("soil-to-fertilizer"):
            sourceRange = [*range(l[1], l[1] + l[2], 1)]
            sourceRangeList.append(sourceRange)
        for z in sourceRangeList:
            if i in z:
                whichIndextoRun = sourceRangeList.index(z)
                whichLinetoRun = dictMap.get("soil-to-fertilizer")[whichIndextoRun]
                calcDiff = (whichLinetoRun[0] - whichLinetoRun[1])
                seedsArray[seedsArray.index(i)] = i + calcDiff
    print(seedsArray)
    for i in seedsArray:
        sourceRangeList = []
        for l in dictMap.get("fertilizer-to-water"):
            sourceRange = [*range(l[1], l[1] + l[2], 1)]
            sourceRangeList.append(sourceRange)
        for z in sourceRangeList:
            if i in z:
                whichIndextoRun = sourceRangeList.index(z)
                whichLinetoRun = dictMap.get("fertilizer-to-water")[whichIndextoRun]
                calcDiff=(whichLinetoRun[0]-whichLinetoRun[1])
                seedsArray[seedsArray.index(i)] = i + calcDiff
    print(seedsArray)
    for i in seedsArray:
        sourceRangeList = []
        for l in dictMap.get("water-to-light"):
            sourceRange = [*range(l[1], l[1] + l[2], 1)]
            sourceRangeList.append(sourceRange)
        for z in sourceRangeList:
            if i in z:
                whichIndextoRun = sourceRangeList.index(z)
                whichLinetoRun = dictMap.get("water-to-light")[whichIndextoRun]
                calcDiff=(whichLinetoRun[0]-whichLinetoRun[1])
                seedsArray[seedsArray.index(i)] = i + calcDiff
    print(seedsArray)
    for i in seedsArray:
        sourceRangeList = []
        for l in dictMap.get("light-to-temperature"):
            sourceRange = [*range(l[1], l[1] + l[2], 1)]
            sourceRangeList.append(sourceRange)
        for z in sourceRangeList:
            if i in z:
                whichIndextoRun = sourceRangeList.index(z)
                whichLinetoRun = dictMap.get("light-to-temperature")[whichIndextoRun]
                calcDiff=(whichLinetoRun[0]-whichLinetoRun[1])
                seedsArray[seedsArray.index(i)] = i + calcDiff
    print(seedsArray)
    for i in seedsArray:
        sourceRangeList = []
        for l in dictMap.get("temperature-to-humidity"):
            sourceRange = [*range(l[1], l[1] + l[2], 1)]
            sourceRangeList.append(sourceRange)
        for z in sourceRangeList:
            if i in z:
                whichIndextoRun = sourceRangeList.index(z)
                whichLinetoRun = dictMap.get("temperature-to-humidity")[whichIndextoRun]
                calcDiff=(whichLinetoRun[0]-whichLinetoRun[1])
                seedsArray[seedsArray.index(i)] = i + calcDiff
    print(seedsArray)
    for i in seedsArray:
        sourceRangeList = []
        for l in dictMap.get("humidity-to-location"):
            sourceRange = [*range(l[1], l[1] + l[2], 1)]
            sourceRangeList.append(sourceRange)
        #print(sourceRangeList)
        #print(i)
        for z in sourceRangeList:
            if i in z:
                print(i)
                #print("found")
                whichIndextoRun = sourceRangeList.index(z)
                whichLinetoRun = dictMap.get("humidity-to-location")[whichIndextoRun]
                #print(whichLinetoRun)
                calcDiff=(whichLinetoRun[0]-whichLinetoRun[1])
                seedsArray[seedsArray.index(i)] = i + calcDiff
                #print(seedsArray[seedsArray.index(i)])
                #print(i+calcDiff)
    print(seedsArray)
    lowestLoc = min(seedsArray)
    print("The lowest location number that corresponds to any of the initial seed numbers is", lowestLoc)




partOne()









        # if num_there(newInput[i+1]):
        #     numFound = newInput[i + 1]
        # #     print("find")
        #     print(numFound)
        # if newInput[i+1] == newInput[len(newInput)-1]:
        #     #print(newInput[len(newInput)-2])
        #     print("end")

        # destinationArray.append(numFound[0])
        # while num_there(newInput[i+1+c]):
        #
        #
        #
        #
        #     if newInput[i+1+c] != newInput[len(newInput)-1]:
        #         numFound = newInput[i + 1 + c]
        #
        #     elif newInput[i+1+c] == newInput[len(newInput)-1]:
        #         numFound = newInput[i + 1 + c]
        #         print(c)
        #         print(numFound[0])
        #         destinationArray.append(numFound[0])
        #
        #     c += 1
        #     elif

        # print(destinationArray)

        #         print(line)
        # print(newInput[line])
        # if newInput[i] in dictMap:
        # print(line)
        # print(i)

        # for i in range(len(line)):
        #     if line[i] == 'map:':
        #         #print(newInput[i])
        #         print("map")
        #         newInput.remove('map:')
        #
        #     print("sf",newInput[i])
        # print(newInput)
        # for lines in range(len(input)):
        # print(input[lines])
        # print(input[22])
        #
        #
        # for i in x:
        #     if i == 'map:':
        #         x.remove('map:')
        #
        # if 'seeds:' in x:
        #     for i in range(1,len(x)):
        #         seedsArray.append(x[i])
        #
        # #print(x)
        # #print(input[22])
        # for i in range(len(x)):
        #     #print(x[i])
        #     #print(i)
        #
        #     if lines != 0:
        #         if x[i] in dictMap:
        # print(x[i])
        # print(lineCounter)
        # c=0
        # for i in range(lines,len(input)):
        #     if num_there(input[lines+1+c]):
        #         numFound = input[lines + 1 + c].strip().split()  # for i in len(numfound) append separate lists, destin/source/range
        #         #print(numFound)
        #         destinationArray.append(numFound[0])
        #         # c+=1
        #         try:
        #             c += 1
        #         except:
        #
        #             pass
        # print(destinationArray)
        # else:
        #     print("too long")

        #                             #print("num here")
        #                             c+=1
        # #                         #print(input[lines+1])
        #
        #                         #print(numFound)
        #
        # #                         for char in numFound:
        # #                             #print(char)
        # #                             for i in range(len(numFound)):
        # #                                 #print(numFound[i])
        # # #         #
        # #                                 if i == 0:
        #         #                             trash = i
        # #         #                             #destinationArray.append(numFound[0])
        # #         #                             #print(numFound[0])
        # #         #                         elif i == 1:
        # #         #                             trash=i
        # #         #                         elif i == 2:
        # #         #                             trash=i
        # #         # #
        # #         # #
        # #                         c+=1
        # #

        #                         sourceArray.append(numFound[1])
        #                         rangeArray.append(numFound[2])

        #                         #print(destinationArray)
        #

        # print(x)
            # try:
            #     for key in dictMap:
            #         if key in x[i]:
            #             print(x[i])
            #             while x[i + c].isdigit():
            #                 number = x[i + c]
            #                 destinationArray.append(number)
            #                 print(number)
            #                 c += 1
            # except:
            #     pass


            #print(destinationArray)
    #
    # print(x)
    #c=1
    # for i in range(len(x)):
    #     c = 1
    #     try:
    #         for key in dictMap:
    #             if key in x[i]:
    #                 while x[i+c].isdigit():
    #                     number = x[i+c]
    #                     dictMap.get(key).append(int(number))
    #                     #print(x[i+c])
    #                     c+=1
    #     except IndexError:
    #         pass
    # print(soilFertArray)
    ### we have successfully parsed the input and created arrays with corresponding titles/values via a dict
    #these arrays will need to be split into 3s, maybe by grabbing specific index lists i.e. 0,1,2;3,4,5
    #for i in range [i:
    #####may have to redo using splitlines! easier to go line by line and only work with 3 indices at a time
