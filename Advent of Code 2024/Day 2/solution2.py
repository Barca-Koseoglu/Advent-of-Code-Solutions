with open('Day 2/example.txt', "r") as file:
    example = file.read()

with open('Day 2/input.txt', "r") as file:
    inp = file.read()

#example
example = example.replace('\n', ',')
example = example.split(',')
example = [x.split(" ") for x in example]
example = [[int(x) for x in y] for y in example]


def increase(i):
    for j in range(1, len(i)):
        if i[j] >= i[j-1] or i[j-1] - i[j] > 3:
            return True
        
    return False


def decrease(i):
    for j in range(1, len(i)):
        if i[j] <= i[j-1] or i[j] - i[j-1] > 3:
            return True
        
    return False

ans = 0

for i in example:
    check = i.copy()
    good = 0
    bad = 0

    if i[0] > i[-1]:
        for j in range(1, len(i)):
            if i[j] >= i[j-1] or i[j-1] - i[j] > 3:
                del check[j]

                if increase(check):
                    bad += 1
                else:
                    good += 1

                check = i.copy()

                del check[j-1]

                if increase(check):
                    bad += 1
                else:
                    good += 1

                check = i.copy()

        if good == bad == 0 or good > 0:
            ans += 1

    elif i[0] < i[-1]:
        for j in range(1, len(i)):
            if i[j] <= i[j-1] or i[j] - i[j-1] > 3:
                del check[j]

                if decrease(check):
                    bad += 1
                else:
                    good += 1

                check = i.copy()

                del check[j-1]

                if decrease(check):
                    bad += 1
                else:
                    good += 1

                check = i.copy()

        if good == bad == 0 or good > 0:
            ans += 1

print(ans)

#input
inp = inp.replace('\n', ',')
inp = inp.split(',')
inp = [x.split(" ") for x in inp]
inp = [[int(x) for x in y] for y in inp]

ans = 0

for i in inp:
    check = i.copy()
    good = 0
    bad = 0

    if i[0] > i[-1]:
        for j in range(1, len(i)):
            if i[j] >= i[j-1] or i[j-1] - i[j] > 3:
                del check[j]

                if increase(check):
                    bad += 1
                else:
                    good += 1

                check = i.copy()

                del check[j-1]

                if increase(check):
                    bad += 1
                else:
                    good += 1

                check = i.copy()

        if good == bad == 0 or good > 0:
            ans += 1

    elif i[0] < i[-1]:
        for j in range(1, len(i)):
            if i[j] <= i[j-1] or i[j] - i[j-1] > 3:
                del check[j]

                if decrease(check):
                    bad += 1
                else:
                    good += 1

                check = i.copy()

                del check[j-1]

                if decrease(check):
                    bad += 1
                else:
                    good += 1

                check = i.copy()

        if good == bad == 0 or good > 0:
            ans += 1

print(ans)
