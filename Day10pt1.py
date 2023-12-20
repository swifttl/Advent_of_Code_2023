input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day10/input101', 'r').read().splitlines()
import tkinter as tk
#| is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


answerArray = []

def UPDOWNFinder():
    if input[current[0]][current[1]] == "|":
        answerArray.append(input[current[0]][current[1]])
        if previous[0] > current[0]:
            previous[0] = current[0]
            current[0] -= 1
        elif previous[0] < current[0]:
            previous[0] = current[0]
            current[0] += 1
def sevFinder():
    if input[current[0]][current[1]] == "7":
        answerArray.append(input[current[0]][current[1]])
        if previous[0]>current[0]:
            previous[0]=current[0]
            previous[1]=current[1]
            current[1]-=1
        elif previous[1]<current[1]:
            previous[0] = current[0]
            previous[1] = current[1]
            current[0]+=1
def LFinder():
    if input[current[0]][current[1]] == "L":
        answerArray.append(input[current[0]][current[1]])
        if previous[0]<current[0]:
            previous[0] = current[0]
            previous[1] = current[1]
            current[1]+=1
        if previous[1]>current[1]:
            previous[0] = current[0]
            previous[1] = current[1]
            current[0]-=1
def LEFTRIGHTFinder():
    if input[current[0]][current[1]] == "-":
        answerArray.append(input[current[0]][current[1]])
        if previous[1] > current[1]:
            previous[0] = current[0]
            previous[1] = current[1]
            current[1] -= 1
        elif previous[1] < current[1]:
            previous[0] = current[0]
            previous[1] = current[1]
            current[1] += 1
def FFinder():
    if input[current[0]][current[1]] == "F":
        answerArray.append(input[current[0]][current[1]])
        if previous[0] > current[0]:
            previous[0] = current[0]
            previous[1] = current[1]
            current[1] += 1
        else:
            if previous[1] > current[1]:
                previous[0] = current[0]
                previous[1] = current[1]
                current[0] += 1
def JFinder():
    if input[current[0]][current[1]] == "J":
        answerArray.append(input[current[0]][current[1]])
        if previous[0] < current[0]:
            previous[0] = current[0]
            previous[1] = current[1]
            current[1] -= 1
        else:
            if previous[1] < current[1]:
                previous[0] = current[0]
                previous[1] = current[1]
                current[0] -= 1

for x in range(len(input)):
    line = input[x]
    for i in range(len(line)):
        if line[i] == "S":
            sFound = i
            sLine = x

previous = [sLine,sFound]
current = [sLine-1,sFound]

a = 1
while a<2:
    UPDOWNFinder()
    sevFinder()
    LFinder()
    LEFTRIGHTFinder()
    FFinder()
    JFinder()
    if input[current[0]][current[1]] == "S":
        break



ans = 1
for i in answerArray:
    ans+=1

print("The furthest steps away from animal is:", ans/2)
