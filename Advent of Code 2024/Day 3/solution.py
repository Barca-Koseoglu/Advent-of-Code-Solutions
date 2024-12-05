with open('Day 3/example.txt', "r") as file:
    example = file.read()

with open('Day 3/input.txt', "r") as file:
    inp = file.read()

#example
ans = 0

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
                ans += int(potential[0]) * int(potential[1])

            except:
                pass

        except:
            pass
     
print(ans)

#input
ans = 0

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
                ans += int(potential[0]) * int(potential[1])

            except:
                pass

        except:
            pass
     
print(ans)
