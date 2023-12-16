#only 12 red cubes, 13 green cubes, and 14 blue cubes?

total = 0
for line in open("input.txt"):
    #print('\n'+ line)
    stuff = line.split(';')
    colorcount = {'red': 0, 'green': 0, 'blue': 0}
    for x in stuff:
        for color in colorcount.keys():
            if x.find(color) != -1:
                num = 0
                if x[x.find(color)-3].isdigit():
                    num = int(x[x.find(color)-3])*10 + int(x[x.find(color)-2])
                else:
                    num = int(x[x.find(color)-2])
                if colorcount[color] < num:
                    colorcount[color] = num
    power = 1
    print(colorcount)
    for val in colorcount.values():
        power*= val
    total+=power
print(total)