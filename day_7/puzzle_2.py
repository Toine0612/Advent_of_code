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


max_used_space = 70000000 - 30000000
total_size = dir_sizes['/'] # Root has total size
space_needed = total_size - max_used_space # Space needed for update

size_deleted_dir = total_size
for k, v in dir_sizes.items():
    if size_deleted_dir > v >= space_needed:
        # print(k, v)
        size_deleted_dir = v


print(size_deleted_dir)
    
        
