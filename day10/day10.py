start = []
grid = []
linecount = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

seen = [[0 for _ in range(len(lines[0]) - 1)] for _ in range(len(lines))]

for line in lines:
    currline = []
    for x in range(len(line)):
        currline.append(line[x])
        if line[x] == "S":
            start.append(linecount)
            start.append(x)
    linecount += 1
    grid.append(currline)

dirr = [1, 0]
currloc = []
currloc.append(start[0])
currloc.append(start[1])
steps = 0
walls = []
lim = [999 for _ in range(len(lines))]
while currloc != start or steps == 0:
    walls.append([currloc[0], currloc[1]])
    if lim[currloc[0]] > currloc[1]:
        lim[currloc[0]] = currloc[1]
    letter = grid[currloc[0] + dirr[0]][currloc[1] + dirr[1]]
    currloc[0] += dirr[0]
    currloc[1] += dirr[1]
    if letter == "L":
        if dirr[0] != 0:
            dirr[1] = 1
            dirr[0] = 0
        else:
            dirr[1] = 0
            dirr[0] = -1
    if letter == "J":
        if dirr[0] != 0:
            dirr[1] = -1
            dirr[0] = 0
        else:
            dirr[1] = 0
            dirr[0] = -1
    if letter == "7":
        if dirr[0] != 0:
            dirr[1] = -1
            dirr[0] = 0
        else:
            dirr[1] = 0
            dirr[0] = 1
    if letter == "F":
        if dirr[0] != 0:
            dirr[1] = 1
            dirr[0] = 0
        else:
            dirr[1] = 0
            dirr[0] = 1
    if letter == ".":
        break
    steps += 1


wall = sorted(walls, reverse=True)
count = 0
big = wall[0][0]

while len(wall) > 1:
    if wall[0][0] == wall[1][0]:
        while (
            len(wall) > 1
            and wall[0][1] - wall[1][1] - 1 == 0
            and grid[wall[0][0]][wall[0][1]] != "|"
            and grid[wall[1][0]][wall[1][1]] != "|"
        ):
            seen[wall[0][0]][wall[0][1]] = -1
            wall.pop(0)
        seen[wall[0][0]][wall[0][1]] = 1
        wall.pop(0)
    else:
        seen[wall[0][0]][wall[0][1]] = 1
        wall.pop(0)

tot = 0

for row in range(big):
    if lim[row] != -1:
        for col in range(lim[row], len(seen[row])):
            if seen[row][col] == 0:
                count = 0
                for x in range(col, len(seen[row])):
                    if seen[row][x] == 1:
                        count += 1
                if count % 2 == 1:
                    tot += 1

print(tot)
