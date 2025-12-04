R = []

with open("3.txt") as f:
    for l in f:
        l = l.strip()
        R.append(l)

#1
x = 0
for r in R:
    f = 0
    i_f = 0
    s = 0
    for c in r[:-1]:
        if int(c) > f:
            f = int(c)
            i_f = r.index(c)
    for c in r[i_f+1:]:
        if int(c) > s:
            s = int(c)

    x += f*10 + s

print(x)

y = 0

#2
for r in R:
    v = []
    t = r
    new_start = 0
    start = 0
    while len(v) < 12:
        offset = len(r) + len(v) - 11
        f = 0
        start = new_start
        for c in t[start:offset]:
            if int(c) > f:
                f = int(c)
                new_start = start + t[start:offset].index(c) + 1
        v.append(f)

    y += int("".join([str(c) for c in v]))

print(y)