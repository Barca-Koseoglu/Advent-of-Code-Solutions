with open('Day 4/example.txt', "r") as file:
    example = file.read()

with open('Day 4/input.txt', "r") as file:
    inp = file.read()

#example
ans = 0

example = example.replace('\n', ',')
example = example.split(',')

for i in example:
    ans += i.count('XMAS') + i.count('SAMX')

for i in range(len(example)):
    for j in range(len(example[i])):
        if example[i][j] == 'X':
            if i > 2 and j > 2:
                if example[i-1][j-1] == 'M' and example[i-2][j-2] == 'A' and example[i-3][j-3] == 'S':
                    ans += 1
            if i < len(example)-3 and j < len(example[i])-3:
                if example[i+1][j+1] == 'M' and example[i+2][j+2] == 'A' and example[i+3][j+3] == 'S':
                    ans += 1
            if i > 2 and j < len(example[i])-3:
                if example[i-1][j+1] == 'M' and example[i-2][j+2] == 'A' and example[i-3][j+3] == 'S':
                    ans += 1
            if i < len(example)-3 and j > 2:
                if example[i+1][j-1] == 'M' and example[i+2][j-2] == 'A' and example[i+3][j-3] == 'S':
                    ans += 1

example = [list(x) for x in example]
example = [list(x) for x in zip(*example[::-1])]
example = [''.join(x) for x in example]

for i in example:
    ans += i.count('XMAS') + i.count('SAMX')

print(ans)

#input
ans = 0

inp = inp.replace('\n', ',')
inp = inp.split(',')

for i in inp:
    ans += i.count('XMAS') + i.count('SAMX')

for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == 'X':
            if i > 2 and j > 2:
                if inp[i-1][j-1] == 'M' and inp[i-2][j-2] == 'A' and inp[i-3][j-3] == 'S':
                    ans += 1
            if i < len(inp)-3 and j < len(inp[i])-3:
                if inp[i+1][j+1] == 'M' and inp[i+2][j+2] == 'A' and inp[i+3][j+3] == 'S':
                    ans += 1
            if i > 2 and j < len(inp[i])-3:
                if inp[i-1][j+1] == 'M' and inp[i-2][j+2] == 'A' and inp[i-3][j+3] == 'S':
                    ans += 1
            if i < len(inp)-3 and j > 2:
                if inp[i+1][j-1] == 'M' and inp[i+2][j-2] == 'A' and inp[i+3][j-3] == 'S':
                    ans += 1

inp = [list(x) for x in inp]
inp = [list(x) for x in zip(*inp[::-1])]
inp = [''.join(x) for x in inp]

for i in inp:
    ans += i.count('XMAS') + i.count('SAMX')

print(ans)