# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

input = open('C:/Users/Terry/Projects/AdventofCode2023/Day1/input.txt', 'r').readlines()#.splitlines()
total = 0
sum = 0
#written = {"one":"1","two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
#written2 = {"eno":"1","owt":"2", "eerht":"3", "ruof":"4", "evif":"5", "xis":"6", "neves":"7", "thgie":"8", "enin", "net"}
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
            #print(linevalue)
            #total = int(linevalue)
            sum += linevalue
            break
print(sum)
    #total = int(linevalue)
    #realtotal = total + linevalue
    #print(realtotal)
#print(written)

#print(sum(int(linevalue)))

#print(input2)


else:
for key in written:
    if key in x:
        # if num_there(x[0:2]):
        #     print(x[0:2])
        #     break
        num1x = written.get(key)
        numberArray1.append(num1x)
        # print(numberArray1)
        firstwordfound = True
        break







