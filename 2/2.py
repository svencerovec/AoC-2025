R = []

with open("2.txt") as f:
    for l in f:
        l = l.strip()
        R += l.split(",")

#1
x = 0
for input in R:
    num_range = [int(e) for e in input.split("-")]
    for i in range(num_range[0], num_range[1] + 1):
        num_str = str(i)

        if len(num_str) % 2 != 0:
            continue
        first, second = num_str[:len(num_str)//2], num_str[len(num_str)//2:]

        if int(first) == int(second):
            x += i
print(x)

#2
def is_invalid(num_str, div):
    if div == len(num_str)+1:
        return False

    s = len(num_str)//div

    if s*div != len(num_str):
        return is_invalid(num_str, div+1)

    t = num_str
    p = int(t[:s])
    for i in range(div-1):
        t = t[s:]
        if int(t[:s]) != p:
            return is_invalid(num_str, div+1)
    return True


x = 0
for input in R:
    num_range = [int(e) for e in input.split("-")]
    for i in range(num_range[0], num_range[1] + 1):
        num_str = str(i)

        if is_invalid(num_str, 2):
            x += i
print(x)