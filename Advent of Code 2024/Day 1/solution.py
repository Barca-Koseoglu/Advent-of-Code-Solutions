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

list1.sort()
list2.sort()

ans = 0
for i in range(len(list1)):
    ans += abs(list1[i] - list2[i])

print(ans)

#solution
inp = inp.replace('\n', ',')
inp = inp.split(',')
inp = [x.split("   ") for x in inp]

list1 = [int(x[0]) for x in inp]
list2 = [int(x[1]) for x in inp]

list1.sort()
list2.sort()

ans = 0
for i in range(len(list1)):
    ans += abs(list1[i] - list2[i])

print(ans)
