with open("input.txt") as f:
    lines = f.read().split("\n")

sp = [list(x) for x in lines]
for col in range(len(sp[0])):
    rocks = 0
    start = 0
    for row in range(len(sp)):
        if sp[row][col] == "O":
            rocks += 1
            sp[row][col] = "."
        if sp[row][col] == "#":
            if start == -1:
                start = row + 1
            else:
                while rocks > 0:
                    sp[start][col] = "O"
                    rocks -= 1
                    start += 1
                start = -1

    summ = 0
    for x in range(len(sp)):
        for y in sp[x]:
            if y == "O":
                summ += len(sp) - x

print(summ)
