input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day1/input.txt', 'r').read().splitlines()

written = {"one": "1", "two":"2", "three":"3","four": "4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
written2 = {"eno":"1","owt":"2", "eerht":"3", "ruof":"4", "evif":"5", "xis":"6", "neves":"7", "thgie":"8", "enin":"9"}
numberArray1 = []
numberArray2 = []
realArray1 = []
#function used later to determine if a string contains any digits
def num_there(s):
    return any(i.isdigit() for i in s)

#Goal is to parse through each line reading right to left; then determine whether which type of
#number comes first: a digit or a written number
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
                break
            else:
                for key in written:
                    if key in x:
                        if num_there(x[0:2]): #solution to issues such as "l5one" where the program would miss "5" for "one" when looking at index [l]
                            break
                        else:
                            num1x = written.get(key)
                            numberArray1.append(num1x)
                            firstwordfound = True
                            break
            y += 1
            if firstwordfound:
                break
    print(numberArray1)

#Goal is the same as partone, however reading backwards
def partTwo():
    for item in input:
        z = 0
        x = item[z:5+z]
        secondWordFound = False
        for dig2 in item[::-1]:
            backwardsline = item[::-1]
            x = backwardsline[z:5+z]
            if dig2.isdigit():
                num2 = dig2
                numberArray2.append(num2)
                break
            else:
                for key2 in written2:
                    if key2 in x:
                        if num_there(x[0:2]):
                            break
                        num2x = written2.get(key2)
                        numberArray2.append(num2x)
                        secondWordFound = True
                        break
            z += 1
            if secondWordFound:
                break
    print(numberArray2)
partOne()
partTwo()
realArray3 = []
realArray4 = []
for i in range(len(numberArray1)):       #goal is to populate realArray3 with the combine value at each index of the result of partOne and partTwo functions.
    realArray3.append(numberArray1[i] + (numberArray2[i]))

for i in range(len(realArray3)):         #goal is to change str in RA3 to int (most likely can take place somewhere else)
    realArray4.append(int(realArray3[i]))
print(realArray4)
FuckingForRealForReal = 0
for i in realArray4:                    #sum calculator
    FuckingForRealForReal += i
print(FuckingForRealForReal)
