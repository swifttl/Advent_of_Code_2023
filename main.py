# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day1/input.txt', 'r').readlines()#.splitlines()
total = 0
sum = 0
newlist = []
for item in input:
    for dig1 in item:
        if dig1.isdigit():
            #print(dig1)
            break
    #rv = item[::-1]
    #print(rv)
    for dig2 in item[::-1]:
        if dig2.isdigit():
            #print(dig1+dig2)
            linevalue = int(dig1+dig2)
            print(linevalue)
            #total = int(linevalue)
            sum += linevalue
            break
print(sum)
    #total = int(linevalue)
    #realtotal = total + linevalue
    #print(realtotal)


#print(sum(int(linevalue)))

#print(input2)










