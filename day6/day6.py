tot = 1
times = []
dis = []
linenum = 0

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    words = line.split(" ")
    if linenum == 0:
        for i in range(1, len(words)):
            if words[i].strip() != "":
                times.append(int(words[i].strip()))
        linenum += 1
    else:
        for i in range(1, len(words)):
            if words[i].strip() != "":
                dis.append(int(words[i].strip()))

for i in range(len(times)):
    count = 0
    for vel in range(int(times[i])):
        if (vel) * (times[i] - vel) > dis[i]:
            count += 1
    if count != 0:
        tot *= count

print(tot)
