import fileinput

calories = open('input.txt','r').read().splitlines()
total_calories = 0
largest_calories = []

for c in calories:
    if c == '':
        largest_calories.append(total_calories)
        total_calories = 0
        continue

    total_calories += int(c)

print(max(largest_calories))

total_largest_calories = 0

for i in range(3):
    total_largest_calories += int(max(largest_calories))
    largest_calories.remove(max(largest_calories))


print(total_largest_calories)
