import fileinput

input = open('input.txt','r').read().splitlines()
crates = [[] for y in range(9)]

# Set input in double array
for i in range(9):
    for j in range (8):
        if input[j][i + i * 3 + 1] != ' ':
            crates[i].insert(0, input[j][i + i * 3 + 1])

for i in input[10:]:
    amount = int(i.split(" ")[1])
    start = int(i.split(" ")[3]) - 1
    dest = int(i.split(" ")[5]) - 1

    for j in range(amount):
        crates[dest].append(crates[start].pop())
        
anwser = ""
for i in range(9):
    anwser += crates[i].pop()

print(anwser)