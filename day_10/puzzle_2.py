import fileinput
import math

input = open('input.txt','r').read().splitlines()        
sprite_middle = 1
signal_strength = 0
current_line = -1
next_line = 0
print_line = ""

for i in range(1, 241):
    index = (i % 40) - 1 if (i % 40) != 0 else 39
    if index >= sprite_middle - 1 and index <= sprite_middle + 1:
        print_line += "#"
    else:
        print_line += "."

    if i % 40 == 0:
        print(print_line)
        print_line = ""

    if input[next_line] == "noop":
        next_line += 1
        continue

    op, num = input[next_line].split(" ")
    if current_line != next_line:
        current_line = next_line
        continue

    next_line += 1
    sprite_middle += int(num)

print(signal_strength)