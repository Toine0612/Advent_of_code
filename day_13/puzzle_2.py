import fileinput

def compare(list_1, list_2):
    if isinstance(list_1, int) and isinstance(list_2, int):
        return list_1 - list_2
    elif isinstance(list_1, list) and isinstance(list_2, int):
        return compare(list_1, [list_2])
    elif isinstance(list_1, int) and isinstance(list_2, list):
        return compare([list_1], list_2)
        
    for a, b in zip(list_1, list_2):
        v = compare(a, b)
        if v :
            return v
    return len(list_1) - len(list_2)

pairs = open('input.txt','r').read().split("\n\n")

i2 = 1
i6 = 2
for i, p in enumerate(pairs):
    lists = p.split("\n")
    for l in lists:
        l = eval(l)

        if compare(l, [[2]]) < 0:
            i2 += 1
            i6 += 1
        elif compare(l, [[6]]) < 0:
            i6 += 1


print(i2 * i6)
