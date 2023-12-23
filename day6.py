tot = 1
times = []
dis = []
linenum = 0
with open('input.txt', 'r') as file:
    for line in file:
        words = line.split(' ')
        if linenum == 0:
            for i in range(1, words.__len__()):
                if words[i].strip() != '':
                    times.append(int(words[i].strip()))
            linenum += 1
        else:
           for i in range(1, words.__len__()):
                if words[i].strip() != '':
                    dis.append(int(words[i].strip()))

print(times)
print(dis)
for i in range(0, times.__len__()):
    count = 0
    for vel in range(0, int(times[i])):
        if (vel) * (times[i] - vel) > dis[i]:
            count += 1
    if count != 0:
        print(count)
        tot *= count
print(tot)