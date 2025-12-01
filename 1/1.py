i = []

with open("1.txt") as f:
    for l in f:
        l = l.strip()
        t = l[0]
        d = int(l[1:])
        i.append((t, d))

dial = 50
count_of_0 = 0

for instruction in i:
    if instruction[0] == 'L':
        for i in range(instruction[1]):
            dial = dial - 1
            if dial % 100 == 0:
                count_of_0 += 1
    if instruction[0] == 'R':
        for i in range(instruction[1]):
            dial = dial + 1
            if dial % 100 == 0:
                count_of_0 += 1

print(count_of_0)
