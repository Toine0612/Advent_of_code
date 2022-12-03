import fileinput

rucksacks = open('input.txt','r').read().splitlines()
sum_of_priorities = 0

for r in rucksacks:
    a,b = r[:len(r)//2], r[len(r)//2:]

    for letter in a:
        if letter in b:
            sum_of_priorities += ord(letter) - 64 + 26 if ord(letter) < 91 else ord(letter) - 96
            break
        
print(sum_of_priorities)
