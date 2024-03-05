tot = 0
times = []
dis = []
linenum = 0
time = 0
dist = 0

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    words = line.split(" ")
    if linenum == 0:
        for i in range(1, len(words)):
            if words[i].strip() != "":
                times.append(words[i].strip())
        time = int("".join(times))
        linenum += 1
    else:
        for i in range(1, len(words)):
            if words[i].strip() != "":
                dis.append(words[i].strip())
        dist = int("".join(dis))

for vel in range(time):
    if (vel) * (time - vel) > dist:
        tot += 1

print(tot)
