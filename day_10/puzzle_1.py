import fileinput
import math

input = open('input.txt','r').read().splitlines()        
amount = 1
signal_strength = 0
current_line = -1
next_line = 0

for i in range(1, 221):
    if i % 40 == 20:
        signal_strength += i * amount

    if input[next_line] == "noop":
        next_line += 1
        continue

    op, num = input[next_line].split(" ")
    if current_line != next_line:
        current_line = next_line
        continue

    next_line += 1
    amount += int(num)

print(signal_strength)