import fileinput

input = open('input.txt','r').read()
position = 4

for i in input:
    string = input[position - 4:position]
    set_string = set(string)

    if len(set_string) == len(string):
        break

    position += 1

print(position)
