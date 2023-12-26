input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day21/input211', 'r').read().splitlines()

for x in range(len(input)):
    line = input[x]
    for i in range(len(line)):
        if line[i] == "S":
            sInd = i
            sLine = x

try:
    u=1
    begin = [(sLine,sInd)]
    while u <= 64:
        tempLoc = []
        for i in begin:
            y = i[0]
            x = i[1]
            if input[y - 1][x] == "." or input[y - 1][x] == "S":
                tempLoc.append((y - 1, x))
            if input[y + 1][x] == "." or input[y + 1][x] == "S":
                tempLoc.append((y + 1, x))
            if input[y][x - 1] == "." or input[y][x-1] == "S":
                tempLoc.append((y, x - 1))
            if input[y][x + 1] == "." or input[y][x+1] == "S":
                tempLoc.append((y, x + 1))
            begin = set(tempLoc)
        u+=1
except IndexError:
    pass

print(set(tempLoc))
print("The total number of different locations is:", len(set(tempLoc)))
