import fileinput
from collections import defaultdict

input = open('input.txt','r').read().splitlines()
dir_sizes = defaultdict(int)
path = []

for i in input:
    splitted_input = i.split(" ")
    if splitted_input[0] == "$":
        if splitted_input[1] == "cd":
            if splitted_input[2] == "/": # Go to root
                path = ["/"]
            elif splitted_input[2] == "..": # Remove path -> go 1 up
                path.pop()
            else: # Add path -> go 1 down
                path.append(splitted_input[2])
    elif splitted_input[0] != "dir": # If not dir -> size
        for p in range(1, len(path) + 1):
            # add size to all items of the path
            dir_sizes['/'.join(path[:p])] += int(splitted_input[0]) 

total_sum = 0
for k, v in dir_sizes.items():
    # print(k, v)
    total_sum += v if v <= 100000 else 0


print(total_sum)
    
        
