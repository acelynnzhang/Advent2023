import math
dir = []
map = {}
curr= []
with open('input.txt', 'r') as file:
    for line in file:
        if len(dir) == 0:
            for x in line:
                if x != '\n':
                    dir.append(x)
        elif len(line) > 1:
            part = line.split(" = ")
            if part[0][2] == 'A':
                curr.append(part[0])
            map[part[0]] = part[1].replace("(", "").replace(")", "").replace("\n", "").split(", ")

#print(dir)
#print(map)
print(curr)
goal = len(curr)
count = 0
multi = []
while len(multi) != goal:
    next = []
    for x in range(0, len(curr)):
        if curr[x] != '0':
            parts = map[curr[x]]
            if dir[count % len(dir)] == 'R':
                #print(parts[1])
                curr[x] = parts[1]
            else:
                #print(parts[0])
                curr[x] = parts[0]
            if curr[x][2] == 'Z':
                print(curr[x])
                multi.append(count + 1)
                curr[x] = '0'
        print(curr)
    count += 1
    
print(multi)
print(math.lcm(11567, 12643, 15871, 16409, 19637, 21251))