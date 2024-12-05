with open('Day 2/example.txt', "r") as file:
    example = file.read()

with open('Day 2/input.txt', "r") as file:
    inp = file.read()

#example
example = example.replace('\n', ',')
example = example.split(',')
example = [x.split(" ") for x in example]
example = [[int(x) for x in y] for y in example]

ans = 0

for i in example:
    if i[0] > i[-1]:
        for j in range(1, len(i)):
            if i[j] >= i[j-1] or i[j-1] - i[j] > 3:
                ans -= 1
                break

        ans += 1

    elif i[0] < i[-1]:
        for j in range(1, len(i)):
            if i[j] <= i[j-1] or i[j] - i[j-1] > 3:
                ans -= 1
                break

        ans += 1

print(ans)

#solution
inp = inp.replace('\n', ',')
inp = inp.split(',')
inp = [x.split(" ") for x in inp]
inp = [[int(x) for x in y] for y in inp]

ans = 0

for i in inp:
    if i[0] > i[-1]:
        for j in range(1, len(i)):
            if i[j] >= i[j-1] or i[j-1] - i[j] > 3:
                ans -= 1
                break

        ans += 1

    elif i[0] < i[-1]:
        for j in range(1, len(i)):
            if i[j] <= i[j-1] or i[j] - i[j-1] > 3:
                ans -= 1
                break

        ans += 1

print(ans)
