with open("input.txt") as f:
    lines = f.readlines()

line_count = len(lines)


def inrange(x, y):
    # print(x, y)
    # print(x >= 0 and x < line_count and y >= 0 and y < len(lines[0].strip()))
    return x >= 0 and x < line_count and y >= 0 and y < len(lines[0].strip())


def issym(x):
    return x.isdigit()


# Create a grid to keep track of locations


def searchint(row, col):
    start = col
    end = col
    while inrange(end + 1, row) and lines[row][end + 1].isdigit():
        end = end + 1
    while inrange(start - 1, row) and lines[row][start - 1].isdigit():
        start = start - 1
    this = (row, start, end)
    return this


def toint(x):
    return int(lines[x[0]][x[1] : x[2] + 1])


tot = 0
for i in range(line_count):
    for j in range(len(lines[0].strip())):
        if lines[i][j] == "*":
            count = 0
            top = []
            bot = []
            currr = 1
            if inrange(j + 1, i) and issym(lines[i][j + 1]):
                currr *= toint(searchint(i, j + 1))
                count = count + 1
            if inrange(j - 1, i) and issym(lines[i][j - 1]):
                currr *= toint(searchint(i, j - 1))
                count = count + 1
            if inrange(j, i + 1) and issym(lines[i + 1][j]):
                bot.append(searchint(i + 1, j))
                currr *= toint(searchint(i + 1, j))
                count = count + 1
            if inrange(j, i - 1) and issym(lines[i - 1][j]):
                top.append(searchint(i - 1, j))
                currr *= toint(searchint(i - 1, j))
                count = count + 1
            if inrange(j + 1, i + 1) and issym(lines[i + 1][j + 1]):
                curr = searchint(i + 1, j + 1)
                if len(bot) != 0:
                    if bot[0][2] != curr[2]:
                        count = count + 1
                        currr *= toint(searchint(i + 1, j + 1))
                else:
                    bot.append(searchint(i + 1, j + 1))
                    count = count + 1
                    currr *= toint(searchint(i + 1, j + 1))
            if inrange(j - 1, i - 1) and issym(lines[i - 1][j - 1]):
                curr = searchint(i - 1, j - 1)
                if len(top) != 0:
                    if top[0][2] != curr[2]:
                        count = count + 1
                        currr *= toint(searchint(i - 1, j - 1))
                else:
                    top.append(searchint(i - 1, j - 1))
                    count = count + 1
                    currr *= toint(searchint(i - 1, j - 1))
            if inrange(j + 1, i - 1) and issym(lines[i - 1][j + 1]):
                curr = searchint(i - 1, j + 1)
                if len(top) != 0:
                    if top[0][2] != curr[2]:
                        count = count + 1
                        currr *= toint(searchint(i - 1, j + 1))
                else:
                    top.append(searchint(i - 1, j + 1))
                    count = count + 1
                    currr *= toint(searchint(i - 1, j + 1))
            if inrange(j - 1, i + 1) and issym(lines[i + 1][j - 1]):
                curr = searchint(i + 1, j - 1)
                if len(bot) != 0:
                    if bot[0][2] != curr[2]:
                        count = count + 1
                        currr *= toint(searchint(i + 1, j - 1))
                else:
                    bot.append(searchint(i + 1, j - 1))
                    count = count + 1
                    currr *= toint(searchint(i + 1, j - 1))
            if count == 2:
                tot += currr
print(tot)
