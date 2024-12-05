with open('Day 1/example.txt', "r") as file:
    example = file.read()

with open('Day 1/input.txt', "r") as file:
    inp = file.read()

#example
example = example.replace('\n', ',')
example = example.split(',')
example = [x.split("   ") for x in example]

list1 = [int(x[0]) for x in example]
list2 = [int(x[1]) for x in example]

right = {}

for i in list2:
    if i in right:
        right[i] += 1
    else:
        right[i] = 1

ans = 0
for i in list1:
    if i in right:
        ans += i * right[i]

print(ans)

#input
inp = inp.replace('\n', ',')
inp = inp.split(',')
inp = [x.split("   ") for x in inp]

list1 = [int(x[0]) for x in inp]
list2 = [int(x[1]) for x in inp]

right = {}

for i in list2:
    if i in right:
        right[i] += 1
    else:
        right[i] = 1

ans = 0
for i in list1:
    if i in right:
        ans += i * right[i]

print(ans)