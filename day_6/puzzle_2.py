import fileinput

input = open('input.txt','r').read()
position = 14

for i in input:
    string = input[position - 14:position]
    set_string = set(string)

    if len(set_string) == len(string):
        break

    position += 1

print(position)
