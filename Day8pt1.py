# Starting with AAA, you need to look up the next element based on the next left/right instruction in your input.
# If you run out of left/right instructions, repeat the whole sequence of instructions as necessary.
# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

#First should take input[0] as directions and assing dict values {r =


input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day8/input8', 'r').read().splitlines()
directions = input[0]
leftRightArray = []

def locator(string):
    a = 0
    finish = "placeholder"
    while finish != 'ZZZ':
        for instruction in string:
            if a==0:
                if instruction == "R":
                    for i in leftRightArray:
                        if i[0] == "AAA":
                            storeI = leftRightArray.index(i)
                            # print(leftRightArray.index(i))
                    finish = leftRightArray[storeI][2]
                    a += 1
                elif instruction == "L":
                    for i in leftRightArray:
                        if i[0] == "AAA":
                            storeI = leftRightArray.index(i)
                    finish = leftRightArray[storeI][1]
                    a += 1
            else:
                if instruction == "R":
                    for i in leftRightArray:
                        if i[0] == finish:
                            storeI = leftRightArray.index(i)
                    finish = leftRightArray[storeI][2]
                    a += 1
                else:
                    if instruction =='L':
                        for i in leftRightArray:
                            if i[0] == finish:
                                storeI = leftRightArray.index(i)
                        finish = leftRightArray[storeI][1]
                        a += 1
    print("The total number of steps is", a)

def partOne():
    for line in input[2:]:
        x = line.split("=")
        for i in x:
            leftRight = x[1].replace('(','').replace(')','').replace(',', '').strip().split()
        leftRight.insert(0, x[0].strip())
        leftRightArray.append(leftRight)

partOne()
locator(directions)
