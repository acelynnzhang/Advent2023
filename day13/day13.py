colcount = 0
rowcount = 0


def check(str, int):
    move = min(int - 1, len(str) - int)
    l = int - 1
    r = int
    while move > 0:
        if str[l] != str[r]:
            return False
        move -= 1
        l -= 1
        r += 1
    return True


with open("input.txt", "r") as f:
    lines = f.readlines()

chunks = []
curr = []
for line in lines:
    if len(line) > 1:
        curr.append(line.replace("\n", ""))
    else:
        norms = curr.copy()
        curr.reverse()
        rownorm = 0
        save = 0
        for x in range(len(curr)):
            if curr[x] == norms[rownorm]:
                rownorm += 1
                if save == 0:
                    save = x
            elif save != 0:
                x = save
                rownorm = 0
            if rownorm == len(curr):
                break
        if save == 0:
            pot = []
            for x in norms:
                if len(pot) == 0:
                    for y in range(1, len(x)):
                        if x[y] == x[y - 1]:
                            if check(x, y):
                                pot.append(y)
                else:
                    while check(x, pot[0]) != True:
                        pot.pop(0)
            rowcount += save
            colcount += pot[0]
