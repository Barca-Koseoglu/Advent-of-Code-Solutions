with open('Day 3/example2.txt', "r") as file:
    example = file.read()

with open('Day 3/input.txt', "r") as file:
    inp = file.read()

#example
ans = 0

check = example.find("don't()")
doos = [(0, check)]
while True:
    check = example.find("do()", check)

    if check == -1:
        break
    lim = example.find("don't()", check)
    if lim == -1:
        doos.append((check, len(example)-1))
        break
    doos.append((check, lim))
    check = lim

start = 0
while True:
    start = example.find("mul(", start)

    if start == -1:
        break
    start += 4

    end = example.find(")", start)

    if end == -1:
        break

    if 3 <= end - start <= 7:
        potential = example[start:end]

        try:
            potential = potential.split(",")

            try:
                pot = int(potential[0]) * int(potential[1])

                for i in doos:
                    if i[0] < start < i[1]:
                        ans += pot
                        break

            except:
                pass

        except:
            pass

print(ans)

#input
ans = 0

check = inp.find("don't()")
doos = [(0, check)]
while True:
    check = inp.find("do()", check)

    if check == -1:
        break
    lim = inp.find("don't()", check)
    if lim == -1:
        doos.append((check, len(inp)-1))
        break
    doos.append((check, lim))
    check = lim

start = 0
while True:
    start = inp.find("mul(", start)

    if start == -1:
        break
    start += 4

    end = inp.find(")", start)

    if end == -1:
        break

    if 3 <= end - start <= 7:
        potential = inp[start:end]

        try:
            potential = potential.split(",")

            try:
                pot = int(potential[0]) * int(potential[1])

                for i in doos:
                    if i[0] < start < i[1]:
                        ans += pot
                        break

            except:
                pass

        except:
            pass

print(ans)
