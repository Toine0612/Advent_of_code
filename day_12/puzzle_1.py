import fileinput

NEIGHBORS = [[0, 1], [1, 0], [0, -1], [-1, 0]] # top, right, bottom, left

map = open('input.txt','r').read().split("\n")
rows = [[] for i in range(len(map))]
columns = [[] for i in range(len(map[0]))]
queue = [[20, 0, 0]] # Start position
path = []

for row in range(0, len(rows)):
    for col in range(0, len(columns)):
        rows[row].append(map[row][col])

while len(queue) > 0:
    pos = queue.pop(0)
    item = rows[pos[1]][pos[0]]
    item_height = ord(item) if item != "S" else ord('a')    

    if item == "E":
        print(pos[2])
        break

    for i in range(len(NEIGHBORS)):
        neighbor_set = [pos[0] + NEIGHBORS[i][0], pos[1] + NEIGHBORS[i][1]]
        neighbor_pos = [pos[0] + NEIGHBORS[i][0], pos[1] + NEIGHBORS[i][1], pos[2] + 1]
        # Check if pos is out of bounds
        if neighbor_pos[1] >= len(rows) or neighbor_pos[1] < 0 or neighbor_pos[0] >= len(rows[0]) or neighbor_pos[0] < 0:
            continue
        neighbor = rows[neighbor_pos[1]][neighbor_pos[0]]
        neighbor_height = ord(neighbor) if neighbor != "E" else ord('z')

        height_diff = neighbor_height - item_height

        if neighbor_set not in path and height_diff <= 1:
            queue.append(neighbor_pos)
            path.append(neighbor_set)
