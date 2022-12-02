import fileinput

def get_players_value(opponent, match_result):
    if opponent == 1:
        return 2 if match_result == 2 else 3
    if opponent == 2:
        return 3 if match_result == 2 else 1
    if opponent == 3:
        return 1 if match_result == 2 else 2

matches = open('input.txt','r').read().splitlines()
total_score = 0

for m in matches:
    m = m.split()
    opponent = ord(m[0]) - 64
    match_result = ord(m[1]) - 88

    if match_result == 2:
        total_score += 6 + get_players_value(opponent, match_result)
    elif match_result == 1:
        total_score += 3 + opponent
    else:
        total_score += get_players_value(opponent, match_result)

print(total_score)
