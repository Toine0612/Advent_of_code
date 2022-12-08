import fileinput

input = open('input.txt','r').read().splitlines()        
rows = [[] for i in range(len(input))]
columns = [[] for i in range(len(input[0]))]

for row in range(0, len(rows)):
    for col in range(0, len(columns)):
        rows[row].append(input[row][col])
        columns[col].append(input[row][col])

visible_trees = 0
for row in range(1, len(rows) + 1):
    for col in range(1, len(columns) + 1):
        tree = input[row - 1][col - 1]
        if all(x < tree for x in rows[row - 1][:col - 1]) or all(x < tree for x in rows[row - 1][col:]) or all(x < tree for x in columns[col - 1][:row - 1]) or all(x < tree for x in columns[col - 1][row:]):
            visible_trees += 1

print(visible_trees)

        
