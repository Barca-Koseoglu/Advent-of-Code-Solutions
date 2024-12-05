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
    example[p1] = [int(i) for i in example[p1]]

    if example[p1][0] in before:
        before[example[p1][0]].append(example[p1][1])
    else:
        before[example[p1][0]] = [example[p1][1]]

    p1 += 1

p1 += 1
while p1 != len(example):
    example[p1] = example[p1].split(',')
    example[p1] = [int(i) for i in example[p1]]

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
        example[p1].sort()
        example[p1] = example[p1][::-1]
        print(example[p1])
        ans += example[p1][len(example[p1])//2]

    p1 += 1

print(ans)