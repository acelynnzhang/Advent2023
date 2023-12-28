with open('input2.txt', 'r') as file:
    for line in file:
        slots = len(line)
        split = line.split(' ')
        seenbroken = []
        unknownintervals = []
        intervalq = [0,0]
        intervalb = [0,0]
        currinq = False
        currinb = False
        for x in range(len(split[0])):
            if split[0][x] != '?' and currinq:
                currin = False
                interval[1] = x
                unknownintervals.append(interval)
            if split[0][x] == '?' and not currinq:
                currin = True
                interval[0] = x
            if split[0][x] == '#' and not currinb:
                currinb = True
                intervalb[0] = x
            if split[0][x] != '#' and currinb:
                currinb = False
                intervalb[1] = x
                seenbroken.append(intervalb[1] - intervalb[0])
        broken =split[1].split(',').strip()
        find = []
        for x in range(len(broken)):
            if int(broken[x]) == seenbroken[x]
            