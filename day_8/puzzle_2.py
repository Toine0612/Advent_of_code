import fileinput

input = open('input.txt','r').read().splitlines()        
rows = [[] for i in range(len(input))]
columns = [[] for i in range(len(input[0]))]

for row in range(0, len(rows)):
    for col in range(0, len(columns)):
        rows[row].append(input[row][col])
        columns[col].append(input[row][col])

highest_scenic = 0
for row in range(1, len(rows) + 1):
    for col in range(1, len(columns) + 1):
        tree = input[row - 1][col - 1]

        left = 0
        for x in reversed(rows[row - 1][:col - 1]): # Left side horizontal
            left += 1
            if x >= tree:
                break

        right = 0
        for x in rows[row - 1][col:]: # Right side horizontal
            right += 1
            if x >= tree:
                break

        top = 0
        for x in reversed(columns[col - 1][:row - 1]): # Top side vertical
            top += 1
            if x >= tree:
                break
            
        bottom = 0
        for x in columns[col - 1][row:]: # Bottom side vertical
            bottom += 1
            if x >= tree:
                break
        
        scenic_score = top * left * right * bottom
        if scenic_score > highest_scenic:
            highest_scenic = scenic_score

print(highest_scenic)

        
