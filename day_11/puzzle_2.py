import fileinput
import math

ROUNDS = 10000
AMOUNT_OF_MONKEYS = 8

monkeys = open('input.txt','r').read().split("\n\n")
items = [[] for i in range(AMOUNT_OF_MONKEYS)]
inspections = [0 for i in range(AMOUNT_OF_MONKEYS)]

# Fill all items
for m in monkeys:
    m = m.splitlines()
    items[int(m[0][7])] = m[1].split(":")[1].strip().split(", ")

for i in range(ROUNDS):
    for m in monkeys:
        m = m.splitlines()
        # Get operations
        operation = eval("lambda old:" + m[2].split("=")[1])
        test = lambda x: x % int(m[3][21:]) == 0
        throw = {
            True: int(m[4][29:]),
            False: int(m[5][30:])
        }

        # Throw and clear all items
        monkey_items = items[int(m[0][7])]
        for j, item in enumerate(monkey_items):
            worry_level = operation(int(item))
            next_monkey = throw[test(worry_level)]
            items[next_monkey].append(worry_level)

        inspections[int(m[0][7])] += len(monkey_items)
        items[int(m[0][7])] = []
    
# Get 2 highest inspections
maxs = []
for i in range(2):
    maxs.append(max(inspections))
    inspections.remove(max(inspections))
business = maxs[0] * maxs[1]

print(business)
