import fileinput
import math

input = open('input.txt','r').read().splitlines()        
head = [0, 0]
prevs = [head, [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tail_positions = []

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

        prevs[0] = head

        for p in range(1, len(prevs)):
            distance = math.sqrt((prevs[p][0] - prevs[p - 1][0])**2 + (prevs[p][1] - prevs[p - 1][1])**2)
            
            if distance == 2:
                if prevs[p - 1][0] > prevs[p][0]:
                    prevs[p][0] += 1
                if prevs[p - 1][0] < prevs[p][0]:
                    prevs[p][0] -= 1
                if prevs[p - 1][1] > prevs[p][1]:
                    prevs[p][1] += 1
                if prevs[p - 1][1] < prevs[p][1]:
                    prevs[p][1] -= 1   
            elif distance > 2:
                if prevs[p - 1][0] > prevs[p][0]:
                    prevs[p][0] += 1
                else:
                    prevs[p][0] -= 1
                
                if prevs[p - 1][1] > prevs[p][1]:
                    prevs[p][1] += 1
                else:
                    prevs[p][1] -= 1
        
        p = [prevs[len(prevs) - 1][0], prevs[len(prevs) - 1][1]]
        if p not in tail_positions:
            tail_positions.append(p)

print(len(tail_positions))
