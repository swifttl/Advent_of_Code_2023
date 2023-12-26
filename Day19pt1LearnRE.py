import re

input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2023/Day19/input191', 'r').read()

workflows, parts = input.split('\n\n')
work_regex = r'(\w+)\{([^}]+)\}'
#   r'(\w+)\{([^}]+)\}':   takes a string, and if a string matches the pattern, returns it
#   ():     capture and group
#   r'':    makes sure that the string being analyzed is a raw string
#   \w+:    a sequence of wordcharacter (a-z)(0-9)(_)
#   \{:     escapes the special character {;treats it as a normal character and doesnt return it
#   [^}]+:  [] matches any character enclosed; for this matches any character thats not } + rest of the characters
#   \}:     escapes the special character };treats it as a normal character and doesnt return it
cond_regex = r'(\w+)(<|>)(\d+):(\w+)'
#   r'(\w+)(<|>)(\d+):(\w+)':   takes a string, and if a string matches the pattern, returns it
#   ():     capture and group
#   r'':    makes sure that the string being analyzed is a raw string
#   \w+:    a sequence of wordcharacter (a-z)(0-9)(_)
#   <|>:    either < or >
#   \d+:    sequence of digits(0-9)
#   :  :    not sure; it checks to find a string that matches the pattern include that symbol, but does return that symbol
#   \w+:    sequence of wordcharcters; this ends the pattern so after this in the string, the pattern search will restart

flow = {}

for name, rules in re.findall(work_regex, workflows):
    conditional = re.findall(cond_regex, rules)
    final = rules.split(',')[-1]
    flow[name] = conditional + [final]

AArray = []

for x, m, a,s in re.findall(r'x=(\d+),m=(\d+),a=(\d+),s=(\d+)',parts):
    partDict = {}
    partDict['x'] = int(x)
    partDict['m'] = int(m)
    partDict['a'] = int(a)
    partDict['s'] = int(s)
    partSum = sum([int(x),int(m),int(a),int(s)])
    sender = 'in'

    while sender not in ('A','R'):

        for category, eval, number, destination in flow[sender][:-1]:
            if category in partDict:
                if eval == '<':
                    if partDict[category] < int(number):
                        sender = destination
                        if sender == "A":
                            AArray.append(partSum)
                            break
                        if sender == 'R':
                            break
                        break
                elif eval == '>':
                    if partDict[category] > int(number):
                        sender = destination
                        if sender == 'A':
                            AArray.append(partSum)
                            break
                        if sender == 'R':
                            break
                        break
        else:
            sender = flow[sender][-1]
            if sender == 'A':
                AArray.append(partSum)
                break
            if sender == 'R':
                break

print("The sum of all the accepted parts is:", sum(AArray))
