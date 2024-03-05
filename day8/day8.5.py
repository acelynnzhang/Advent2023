import math

direction = []
mapping = {}
curr = []

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    if len(direction) == 0:
        for x in line:
            if x != "\n":
                direction.append(x)
    elif len(line) > 1:
        part = line.split(" = ")
        if part[0][2] == "A":
            curr.append(part[0])
        mapping[part[0]] = (
            part[1].replace("(", "").replace(")", "").replace("\n", "").split(", ")
        )

goal = len(curr)
count = 0
multi = []
while len(multi) != goal:
    for x in range(0, len(curr)):
        if curr[x] != "0":
            parts = mapping[curr[x]]
            if direction[count % len(direction)] == "R":
                curr[x] = parts[1]
            else:
                curr[x] = parts[0]
            if curr[x][2] == "Z":
                multi.append(count + 1)
                curr[x] = "0"
    count += 1

print(math.lcm(*multi))
