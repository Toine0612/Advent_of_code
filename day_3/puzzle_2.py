import fileinput

rucksacks = open('input.txt','r').read().splitlines()
sum_of_priorities = 0

for i in range(0, len(rucksacks), 3):
    for letter in rucksacks[i]:
        if letter in rucksacks[i + 1] and letter in rucksacks[i + 2]:
            sum_of_priorities += ord(letter) - 64 + 26 if ord(letter) < 91 else ord(letter) - 96
            break

print(sum_of_priorities)
