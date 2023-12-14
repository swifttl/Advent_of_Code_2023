input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day6/input6.txt', 'r').read().splitlines()


l1 = input[0].split()
l2 = input[1].split()
time = [int(i) for i in l1[1:]]
distance = [int(i) for i in l2[1:]]
recordArray = []
waysToWin = []
a=0
# for i in range((len(time))):
#     recordArray = []
#     tRange = [*range(1,time[i]+1, 1)]
#     a = 0
#     for x in tRange:
#         boatDistance = a*(len(tRange)-a)
#         a+=1
#         if boatDistance > distance[i]:
#             recordArray.append((boatDistance))
#     waysToWin.append(len(recordArray))
# calProduct = 1
# for i in waysToWin:
#     calProduct *= i
#
# print("The total ways to win is:", calProduct)
