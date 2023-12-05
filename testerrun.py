input = open('C:/Users/Terry/Projects/AdventofCode2023/Day1/tester.txt', 'r').read().splitlines()

written = {"one": "1", "two":"2", "three":"3","four": "4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
written2 = {"eno":"1","owt":"2", "eerht":"3", "ruof":"4", "evif":"5", "xis":"6", "neves":"7", "thgie":"8", "enin":"9"}
numberArray1 = []
numberArray2 = []
realArray1 = []
def partOne():
    for item in input:
        y = 0
        x = item[0+y:5+y]
        firstwordfound = False
        for dig1 in item:
            x = item[y:5+y]
            if dig1.isdigit():
                num1 = dig1
                numberArray1.append(num1)
                #print(numberArray1)
                break
            if dig1.isdigit() == False:
                for key in written:
                    if key in x:
                        num1x = written.get(key)
                        numberArray1.append(num1x)
                        #print(numberArray1)
                        firstwordfound = True
                        break
            y += 1
            if firstwordfound:
                break
    print(numberArray1)


def partTwo():
    for item in input:
        z = 0
        x = item[z:5+z]
        secondWordFound = False
        secondDigitFound = False
        for dig2 in item[::-1]:
            backwardsline = item[::-1]
            x = backwardsline[z:5+z]
            if dig2.isdigit():
                num2 = dig2
                numberArray2.append(num2)
                secondDigitFound = True
                break
            #if dig2.isdigit() == False:
            else:
                for key2 in written2:
                    if key2 in x:
                        num2x = written2.get(key2)
                        numberArray2.append(num2x)
                        secondWordFound = True
                        break
            z += 1
            if secondDigitFound:
                break
            if secondWordFound:
                break
    print(numberArray2)
partOne()
partTwo()
realArray3 = []
realArray4 = []
for i in range(len(numberArray1)):
    realArray3.append(numberArray1[i] + (numberArray2[i]))

for i in range(len(realArray3)):
    realArray4.append(int(realArray3[i]))
print(realArray4)
FuckingForRealForReal = 0
for i in realArray4:
    FuckingForRealForReal += i
print(FuckingForRealForReal)




# def PartThree():
#     for l in PartOne():
#         print(numberArray1)


#they work separately but not together
#may have to have separte lists and then combine the lists




    #print()
    #for dig1 in item:
        #if dig1.isdigit() != True:
            #if dig1 in written:
            #print(dig1)
            #break
    #rv = item[::-1]
    #print(rv)
    #for dig2 in item[::-1]:
        #if dig2.isdigit():
            #print(dig1+dig2)
            #linevalue = int(dig1+dig2)
            #print(linevalue)
            #total = int(linevalue)
            #sum += linevalue
            #break
#print(sum)
    #total = int(linevalue)
    #realtotal = total + linevalue
    #print(realtotal)
#print(written)

#print(sum(int(linevalue)))

#print(input2)










