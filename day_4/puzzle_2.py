import fileinput

pairs = open('input.txt','r').read().splitlines()
anwser = 0

for p in pairs:
    a,b = p.split(",")

    a = [int(x) for x in a.split("-")]
    b = [int(x) for x in b.split("-")]
    if b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1] or a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]:
        anwser += 1

print(anwser)

