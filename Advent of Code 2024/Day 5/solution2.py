with open('Day 5/example.txt', "r") as file:
    example = file.read()

with open('Day 5/input.txt', "r") as file:
    inp = file.read()

#example
ans = 0

example = example.replace('\n', ';')
example = example.split(';')

before = {}
p1 = 0
while example[p1] != '':
    example[p1] = example[p1].split('|')

    if example[p1][0] in before:
        before[example[p1][0]].append(example[p1][1])
    else:
        before[example[p1][0]] = [example[p1][1]]

    p1 += 1

p1 += 1
while p1 != len(example):
    example[p1] = example[p1].split(',')

    for i in range(len(example[p1])-1):
        if example[p1][i] not in before:
            valid = False
            break

        check = before[example[p1][i]]
        
        valid = True

        for j in range(i+1, len(example[p1])):
            if example[p1][j] not in check:
                valid = False
                break

        if not valid:
            break
    
    if not valid:
        make = []
        count = {}
        for i in example[p1]:
            count[i] = 0
            if i not in before:
                continue
            for j in example[p1]:
                if j in before[i]:
                    count[i] += 1
        count = {value: key for key, value in count.items()}
        for i in range(len(example[p1])-1, -1, -1):
            make.append(count[i])
        ans += int(make[len(make)//2])
    p1 += 1

print(ans)

#input
ans = 0

inp = inp.replace('\n', ';')
inp = inp.split(';')

before = {}
p1 = 0
while inp[p1] != '':
    inp[p1] = inp[p1].split('|')

    if inp[p1][0] in before:
        before[inp[p1][0]].append(inp[p1][1])
    else:
        before[inp[p1][0]] = [inp[p1][1]]

    p1 += 1

p1 += 1
while p1 != len(inp):
    inp[p1] = inp[p1].split(',')

    for i in range(len(inp[p1])-1):
        if inp[p1][i] not in before:
            valid = False
            break

        check = before[inp[p1][i]]
        
        valid = True

        for j in range(i+1, len(inp[p1])):
            if inp[p1][j] not in check:
                valid = False
                break

        if not valid:
            break
    
    if not valid:
        make = []
        count = {}
        for i in inp[p1]:
            count[i] = 0
            if i not in before:
                continue
            for j in inp[p1]:
                if j in before[i]:
                    count[i] += 1
        count = {value: key for key, value in count.items()}
        for i in range(len(inp[p1])-1, -1, -1):
            make.append(count[i])
        ans += int(make[len(make)//2])
    p1 += 1

print(ans)
