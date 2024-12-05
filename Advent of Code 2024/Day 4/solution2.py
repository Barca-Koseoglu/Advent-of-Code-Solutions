with open('Day 4/example2.txt', "r") as file:
    example = file.read()

with open('Day 4/input.txt', "r") as file:
    inp = file.read()

#example
ans = 0

example = example.replace('\n', ',')
example = example.split(',')

for i in range(1, len(example)-1):
    for j in range(1, len(example[i])-1):
        if example[i][j] == 'A':
            if example[i-1][j-1] == 'S' and example[i+1][j+1] == 'M':
                if example[i-1][j+1] == "S" and example[i+1][j-1] == "M":
                    ans += 1
                    continue
                if example[i-1][j+1] == "M" and example[i+1][j-1] == "S":
                    ans += 1
                    continue
            if example[i-1][j-1] == 'M' and example[i+1][j+1] == 'S':
                if example[i-1][j+1] == "M" and example[i+1][j-1] == "S":
                    ans += 1
                    continue
                if example[i-1][j+1] == "S" and example[i+1][j-1] == "M":
                    ans += 1
                    continue

print(ans)

#input
ans = 0

inp = inp.replace('\n', ',')
inp = inp.split(',')

for i in range(1, len(inp)-1):
    for j in range(1, len(inp[i])-1):
        if inp[i][j] == 'A':
            if inp[i-1][j-1] == 'S' and inp[i+1][j+1] == 'M':
                if inp[i-1][j+1] == "S" and inp[i+1][j-1] == "M":
                    ans += 1
                    continue
                if inp[i-1][j+1] == "M" and inp[i+1][j-1] == "S":
                    ans += 1
                    continue
            if inp[i-1][j-1] == 'M' and inp[i+1][j+1] == 'S':
                if inp[i-1][j+1] == "M" and inp[i+1][j-1] == "S":
                    ans += 1
                    continue
                if inp[i-1][j+1] == "S" and inp[i+1][j-1] == "M":
                    ans += 1
                    continue

print(ans)
