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

sum = 0
for i, p in enumerate(pairs):
    list_1, list_2 = p.split("\n")
    list_1 = eval(list_1)
    list_2 = eval(list_2)

    if compare(list_1, list_2) < 0:
        sum += i + 1

print(sum)
