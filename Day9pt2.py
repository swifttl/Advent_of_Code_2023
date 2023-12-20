input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day9/input91', 'r').read().splitlines()
print(input)

answer = []

def partOne():
    for line in input:
        sumList = []
        differences = []
        x = line.split()
        for i in range(0, (len(x)-1)):
            differences.append(int(x[i]) - int(x[i+1]))
        sumList.append(int(x[0]))
        sumList.append(differences[0])
        while len(set(differences))!= 1:
            for i in range(0, (len(differences)-1)):
                differences[i] = (int(differences[i])) - (int(differences[i + 1]))
                print(differences)
            differences.pop()
            print(differences)
            sumList.append(differences[0])
        answer.append(sum(sumList))
partOne()

print("The answer is :" , sum(answer))
