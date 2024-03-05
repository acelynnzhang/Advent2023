total = 0

numstring = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    firstfound = 1000
    lastfound = -1
    for i in range(0, len(line)):
        if firstfound == 1000:
            if line[i].isnumeric():
                firstfound = line[i]

            for num in numstring:
                if line[0:i].find(num) != -1:
                    firstfound = numstring.index(num) + 1
        if lastfound == -1:
            if line[len(line) - i - 1].isnumeric():
                lastfound = line[len(line) - i - 1]

            for num in numstring:
                if line[len(line) - i - 1 :].find(num) != -1:
                    lastfound = numstring.index(num) + 1
        if firstfound != 1000 and lastfound != -1:
            total += int(firstfound) * 10 + int(lastfound)
            break

print(total)
