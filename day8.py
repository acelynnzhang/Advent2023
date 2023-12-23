import math
dir = []
map = {}
with open('input.txt', 'r') as file:
    for line in file:
        if len(dir) == 0:
            for x in line:
                if x != '\n':
                    dir.append(x)
        elif len(line) > 1:
            part = line.split(" = ")
            map[part[0]] = part[1]

print(dir)
print(map)

curr = "MHA"
count = 0
while curr[2] != "Z":
    parts = map[curr].replace("(", "").replace(")", "").replace("\n", "").split(", ")
    print(parts)
    if dir[count % len(dir)] == 'R':
        print(parts[1])
        curr = parts[1]
    else:
        print(parts[0])
        curr = parts[0]
    count += 1

print(count)
print(math.lcm(16409,12643,21251,15871,19637,11567))