input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day6/input6.txt', 'r').read().splitlines()


l1 = input[0].split()
l2 = input[1].split()
time = [int("".join(l1[1:]))]
distance = [int("".join(l2[1:]))]
recordArray = []
a=0
tRange = [*range(1,time[0]+1, 1)]
for i in range(len(tRange)):
    boatDistance = a*(len(tRange)-a)
    a+=1
    if boatDistance > distance[0]:
        recordArray.append((boatDistance))

print("The total ways to win is:", len(recordArray))
