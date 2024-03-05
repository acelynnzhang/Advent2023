import math

direction = []
mapping = {}
with open("input.txt", "r") as file:
    for line in file:
        if len(direction) == 0:
            for x in line:
                if x != "\n":
                    direction.append(x)
        elif len(line) > 1:
            part = line.split(" = ")
            mapping[part[0]] = part[1]


curr = "AAA"
count = 0
while curr[2] != "Z":
    parts = (
        mapping[curr].replace("(", "").replace(")", "").replace("\n", "").split(", ")
    )
    if direction[count % len(direction)] == "R":
        curr = parts[1]
    else:
        curr = parts[0]
    count += 1

print(count)
