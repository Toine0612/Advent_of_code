import fileinput

matches = open('input.txt','r').read().splitlines()
total_score = 0

for m in matches:
    m = m.split()
    opponent = ord(m[0]) - 64
    player = ord(m[1]) - 87

    total_score += player
    
    match_result = opponent - player
    if match_result == 2 or match_result == -1:
        total_score += 6
    elif match_result == 0:
        total_score += 3

print(total_score)
