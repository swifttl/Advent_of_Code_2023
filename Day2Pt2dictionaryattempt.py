#The power of a set of cubes is equal to the
#numbers of red, green, and blue cubes multiplied together.
#For each game, find the minimum set of cubes that must have been present.
#What is the sum of the power of these sets?

input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day2/input2pt1.txt', 'r').read().splitlines()

#Map: Read line by line, skipping first 7 indices for game ID
#split by comma? or split by number?
#need the number and key to be returned
#need to log each time a key is returned, and then compare it to similar keys to find lowest
#maybe create and recall a function that would find the lowest?
#have to multiply the 3 lowest line by line (power)
#add power to array for sum

redArray = []
greenArray = []
blueArray = []
powerArray = []
colorlist = {"red" : redArray, "green" : greenArray, "blue" : blueArray}

def partOne():
    # redArray = []
    # greenArray = []
    # blueArray = []
    #y=[]
    calSum = 0
    for line in input:
        split = line.split()
        print(line)
        for i in split:
            if i.isdigit():
                number = i
                #print(number)
            for color in colorlist:
                if color in i:
                    colorlist.get(color).append(int(number))
                    #y.append(number)
                    #print(y)
                    #print(redArray)
                    #y.clear()
                    # if color == "red":
                    #     redArray.append(number)
                    # if color == "green":
                    #     greenArray.append(number)
                    # if color == "blue":
                    #     blueArray.append(number)
                    #print(color)
                    #print(redArray)
                    #redArray.clear()
                    #greenArray.clear()
                    #blueArray.clear()
                    #print(colorlist.get(color))
        red = max(redArray)
        green = max(greenArray)
        blue = max(blueArray)
        power = red*green*blue
        powerArray.append(power)
        print("The minimum amount of dice needed for the game above are:", red, "red,", green, "green," " and", blue, "blue.")
        print("The power generated from these dice is:", power, "\n")
        #print(powerArray)
        # print(greenArray)
        # print(blueArray)

        redArray.clear()
        greenArray.clear()
        blueArray.clear()
    for i in powerArray:
        calSum += i
        #print(calSum)
    print("The total amount of power generated from all 100 games is:", calSum)

partOne()