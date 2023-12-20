input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day9/input91', 'r').read().splitlines()
print(input)

answer = []

def partOne():
    for line in input:
        sumList = []
        differences = []
        x = line.split()
        for i in range(1, len(x)):
            differences.append(int(x[i]) - int(x[i-1]))
        sumList.append(int(x[-1]))
        sumList.append(differences[-1])
        while len(set(differences))!= 1:
            for i in range(1, len(differences)):
                differences[i-1] = (int(differences[i])) - (int(differences[i - 1]))
            differences.pop()
            sumList.append(differences[-1])
        answer.append(sum(sumList))
partOne()

print("The answer is :" , sum(answer))
