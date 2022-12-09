import fileinput
import math

input = open('input.txt','r').read().splitlines()        
head = [0, 0]
tail = [0, 0]
positions = []

for i in input:
    dir, amount = i.split(" ")
    for a in range(0, int(amount)):

        if dir == "R":
            head[0] += 1
        if dir == "L":
            head[0] -= 1
        if dir == "U":
            head[1] += 1
        if dir == "D":
            head[1] -= 1

        distance = math.sqrt((tail[0] - head[0])**2 + (tail[1] - head[1])**2)

        if distance == 2:
            if dir == "R":
                tail[0] += 1
            if dir == "L":
                tail[0] -= 1
            if dir == "U":
                tail[1] += 1
            if dir == "D":
                tail[1] -= 1   
        elif distance > 2:
            if head[0] > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1
            
            if head[1] > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1

        p = [tail[0], tail[1]]
        if p not in positions:
            positions.append(p)

print(len(positions))
